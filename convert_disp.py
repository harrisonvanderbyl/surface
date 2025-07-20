import re
import json
import xml.etree.ElementTree as ET

def parse_buffer_to_xml(buffer_content):
    # Remove comments and whitespace
    cleaned_content = re.sub(r'/\*.*?\*/', '', buffer_content, flags=re.DOTALL)
    cleaned_content = re.sub(r'//.*', '', cleaned_content)
    cleaned_content = re.sub(r'\s+', '', cleaned_content)

    # Extract hex values
    hex_values = re.findall(r'0x([0-9A-Fa-f]{2})', cleaned_content)
    
    # Convert hex to ASCII
    ascii_string = bytes([int(h, 16) for h in hex_values]).decode('utf-8', errors='ignore')
    
    # Find the XML part
    xml_match = re.search(r'<\?xml.*?>.*</Group>', ascii_string, re.DOTALL)
    if xml_match:
        xml_string = xml_match.group(0)
        # Replace HTML entities with actual characters
        xml_string = xml_string.replace('<', '<').replace('>', '>')
        try:
            root = ET.fromstring(xml_string)
            return etree_to_dict(root)
        except ET.ParseError as e:
            print(f"XML parsing error: {e}")
            return None
    return None

def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = {}
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                if k in dd:
                    if not isinstance(dd[k], list):
                        dd[k] = [dd[k]]
                    dd[k].append(v)
                else:
                    dd[k] = v
        d = {t.tag: dd}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

def parse_disp_txt(content):
    json_output = {}
    current_device = None
    current_method = None
    
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Device (GPU0)
        device_match = re.match(r'Device \((.*?)\)', line)
        if device_match:
            device_name = device_match.group(1)
            current_device = {"name": device_name, "properties": {}}
            json_output[device_name] = current_device
            i += 1
            continue

        if current_device:
            # Name (_HID, "QCOM0D17")
            name_match = re.match(r'Name \((.*?),\s*(.*?)\)', line)
            if name_match:
                prop_name = name_match.group(1)
                prop_value = name_match.group(2).strip()
                
                # Clean up values
                if prop_value.startswith('"') and prop_value.endswith('"'):
                    prop_value = prop_value[1:-1]
                elif prop_value.startswith('0x'):
                    prop_value = int(prop_value, 16)
                elif prop_value == "Zero":
                    prop_value = 0
                elif prop_value == "One":
                    prop_value = 1
                
                current_device["properties"][prop_name] = prop_value
                i += 1
                continue

            # Method (_ADR, 0, NotSerialized)
            method_match = re.match(r'Method \((.*?),\s*(\d+),\s*(.*?)\)', line)
            if method_match:
                method_name = method_match.group(1)
                num_args = int(method_match.group(2))
                serialization = method_match.group(3)
                current_method = {"name": method_name, "args": num_args, "serialization": serialization, "content": {}}
                if "methods" not in current_device:
                    current_device["methods"] = []
                current_device["methods"].append(current_method)
                
                # Read method content until '}'
                method_content_lines = []
                i += 1
                brace_count = 1 # For the method's opening brace
                while i < len(lines):
                    method_line = lines[i].strip()
                    if '{' in method_line:
                        brace_count += method_line.count('{')
                    if '}' in method_line:
                        brace_count -= method_line.count('}')
                    method_content_lines.append(method_line)
                    if brace_count == 0:
                        break
                    i += 1
                
                method_content = "\n".join(method_content_lines[:-1]).strip() # Exclude the closing brace
                
                if method_name in ["_ROM", "ROE1", "ROE2", "ROE3", "ROE4", "ROE5", "ROE6"]:
                    buffer_match = re.search(r'Buffer \(0x[0-9A-Fa-f]+\)\s*\{(.*?)\}', method_content, re.DOTALL)
                    if buffer_match:
                        xml_data = parse_buffer_to_xml(buffer_match.group(1))
                        current_method["content"]["buffer_xml"] = xml_data
                    else:
                        current_method["content"]["raw_buffer"] = method_content
                elif method_name == "_CRS":
                    # Parse Memory32Fixed, Interrupt, GpioIo
                    resources = []
                    mem_fixed_pattern = re.compile(r'Memory32Fixed \((.*?),\s*0x([0-9A-Fa-f]+),\s*0x([0-9A-Fa-f]+),\s*\)')
                    interrupt_pattern = re.compile(r'Interrupt \((.*?),\s*(.*?),\s*(.*?),\s*(.*?),\s*,\s*,\s*\)\s*\{\s*0x([0-9A-Fa-f]+),\s*\}')
                    gpio_io_pattern = re.compile(r'GpioIo \((.*?),\s*(.*?),\s*0x([0-9A-Fa-f]+),\s*0x([0-9A-Fa-f]+),\s*(.*?),\s*"(.*?)"')

                    for res_line in method_content.split('\n'):
                        mem_match = mem_fixed_pattern.search(res_line)
                        if mem_match:
                            resources.append({
                                "type": "Memory32Fixed",
                                "access": mem_match.group(1),
                                "base": int(mem_match.group(2), 16),
                                "length": int(mem_match.group(3), 16)
                            })
                            continue
                        
                        int_match = interrupt_pattern.search(res_line)
                        if int_match:
                            resources.append({
                                "type": "Interrupt",
                                "consumer": int_match.group(1),
                                "level": int_match.group(2),
                                "active": int_match.group(3),
                                "exclusive": int_match.group(4),
                                "value": int(int_match.group(5), 16)
                            })
                            continue

                        gpio_match = gpio_io_pattern.search(res_line)
                        if gpio_match:
                            resources.append({
                                "type": "GpioIo",
                                "shared": gpio_match.group(1),
                                "pull": gpio_match.group(2),
                                "val1": int(gpio_match.group(3), 16),
                                "val2": int(gpio_match.group(4), 16),
                                "restriction": gpio_match.group(5),
                                "path": gpio_match.group(6)
                            })
                            continue
                    current_method["content"]["resources"] = resources
                elif method_name == "RESI":
                    package_content_match = re.search(r'Package \(0x[0-9A-Fa-f]+\)\s*\{(.*?)\}', method_content, re.DOTALL)
                    if package_content_match:
                        package_items = []
                        # Split by 'Package (0x03)' to get individual resource packages
                        sub_packages = re.findall(r'Package \(0x03\)\s*\{(.*?)\}', package_content_match.group(1), re.DOTALL)
                        for sp in sub_packages:
                            parts = [p.strip().replace('"', '') for p in sp.split(',')]
                            if len(parts) == 3:
                                package_items.append({
                                    "type": parts[0],
                                    "name": parts[1],
                                    "category": parts[2]
                                })
                        current_method["content"]["package_info"] = package_items
                    else:
                        current_method["content"]["raw_content"] = method_content
                elif method_name == "_DEP":
                    package_content_match = re.search(r'Package \(0x[0-9A-Fa-f]+\)\s*\{(.*?)\}', method_content, re.DOTALL)
                    if package_content_match:
                        dependencies = [dep.strip() for dep in package_content_match.group(1).split(',') if dep.strip()]
                        current_method["content"]["dependencies"] = dependencies
                    else:
                        current_method["content"]["raw_content"] = method_content
                elif method_name == "CHDV":
                    package_content_match = re.search(r'Package \(0x[0-9A-Fa-f]+\)\s*\{(.*?)\}', method_content, re.DOTALL)
                    if package_content_match:
                        # This is a bit more complex, needs careful parsing
                        # For simplicity, let's just store the raw content for now
                        current_method["content"]["raw_package_content"] = package_content_match.group(1).strip()
                    else:
                        current_method["content"]["raw_content"] = method_content
                else:
                    # For other methods, just store the raw content
                    current_method["content"]["raw_content"] = method_content
                
                i += 1
                continue
            
            # Alias (\_SB.PHRV, _HRV)
            alias_match = re.match(r'Alias \((.*?),\s*(.*?)\)', line)
            if alias_match:
                current_device["properties"]["Alias"] = {
                    "source": alias_match.group(1),
                    "target": alias_match.group(2)
                }
                i += 1
                continue

            # Handle _DOD
            dod_match = re.match(r'Name \(_DOD, Package \(0x01\)\s*\{\s*(.*?)\s*\}\)', line)
            if dod_match:
                current_device["properties"]["_DOD"] = [int(x.strip(), 16) for x in dod_match.group(1).split(',') if x.strip()]
                i += 1
                continue

        i += 1
    return json_output

# Read the content from disp.txt
with open('disp.txt', 'r') as f:
    disp_content = f.read()

# Parse the content
parsed_data = parse_disp_txt(disp_content)

# Write the JSON output to disp.json
with open('disp.json', 'w') as f:
    json.dump(parsed_data, f, indent=4)

print("Conversion complete. Output written to disp.json")
