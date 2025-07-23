import re
import sys
from collections import defaultdict

def parse_crs_block(block):
    mems = re.findall(r'Memory32Fixed\s*\(.*?,\s*0x([0-9A-Fa-f]+),\s*0x([0-9A-Fa-f]+)', block)
    irqs = re.findall(r'Interrupt\s*\(.*?\)\s*{\s*(\d+)', block)
    return mems, irqs

def extract_ufs_devices(dsl):
    devices = re.findall(r'Device\s+\((UFS\d?)\)\s*{(.*?)}\s*}', dsl, re.DOTALL)
    output = {}

    for name, body in devices:
        node = {"label": name.lower(), "path": f"\\_SB.{name}"}
        hid = re.search(r'Name\s+\(_HID,\s*"([^"]+)"\)', body)
        cid = re.search(r'Name\s+\(_CID,\s*"([^"]+)"\)', body)
        crs = re.search(r'Name\s+\(_CRS,\s*ResourceTemplate\s*\(\)\s*{(.*?)}\s*', body, re.DOTALL)

        node["hid"] = hid.group(1) if hid else None
        node["cid"] = cid.group(1) if cid else None

        if crs:
            mems, irqs = parse_crs_block(crs.group(1))
            node["reg"] = mems
            node["interrupts"] = irqs

        output[node["path"]] = node
    return output

def parse_pep_package(dsl_text):
    """
    Extracts all CLOCK and FOOTSWITCH entries for devices in the PEP BPCC table.
    """
    device_blocks = re.findall(r'Package\s*\(0x06\)\s*{\s*"DEVICE",\s*"([^"]+)",\s*(Package.*?)\n\s*},', dsl_text, re.DOTALL)
    output = {}

    for device_path, device_data in device_blocks:
        clocks = set()
        footswitches = set()

        # Extract CLOCK blocks
        clock_matches = re.findall(r'"CLOCK",\s*Package\s*\(0x0?[24]\)\s*{([^}]+)}', device_data)
        for clock_entry in clock_matches:
            clock_lines = [x.strip().strip('"') for x in clock_entry.split(",") if '"' in x]
            if clock_lines:
                clocks.add(clock_lines[0])  # Only the clock name

        # Extract FOOTSWITCH blocks
        footswitch_matches = re.findall(r'"FOOTSWITCH",\s*Package\s*\(0x02\)\s*{\s*"([^"]+)",', device_data)
        for switch in footswitch_matches:
            footswitches.add(switch.strip())

        output[device_path] = {
            "clocks": sorted(clocks),
            "footswitches": sorted(footswitches),
        }

    return output

def emit_dts(node):
    lines = []

    reg_addr = node["reg"][0][0].lstrip("0") if node.get("reg") else "0"
    lines.append(f'{node["label"]}: ufs@{reg_addr} {{')

    if node.get("cid"):
        lines.append(f'    compatible = "qcom,{node["cid"].lower()}";')
    elif node.get("hid"):
        lines.append(f'    compatible = "{node["hid"].lower()}";')

    if node.get("reg"):
        for base, size in node["reg"]:
            lines.append(f'    reg = <0x{base} 0x{size}>;')

    if node.get("interrupts"):
        irq_line = "    interrupts = <" + " ".join(node["interrupts"]) + ">;"
        lines.append(irq_line)

    if node.get("clocks"):
        clk_handles = [f"<&gcc {clk}>" for clk in node["clocks"]]
        lines.append(f"    clocks = {', '.join(clk_handles)};")
        clk_names = [f'"{clk.replace("gcc_", "")}"' for clk in node["clocks"]]
        lines.append(f"    clock-names = {', '.join(clk_names)};")

    if node.get("footswitches"):
        for switch in node["footswitches"]:
            lines.append(f"    power-domains = <&gcc {switch}>;")

    lines.append("};")
    return "\n".join(lines)

def merge_acpi_pep(acpi_nodes, pep_nodes):
    for path, pep in pep_nodes.items():
        if path in acpi_nodes:
            acpi_nodes[path].update(pep)
    return acpi_nodes

def main(dsl_path):
    with open(dsl_path, "r") as f:
        content = f.read()

    acpi = extract_ufs_devices(content)
    pep = parse_pep_package(content)

    merged = merge_acpi_pep(acpi, pep)

    for node in merged.values():
        print("==== Merged UFS DTS Node ====")
        print(emit_dts(node))
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python acpi_ufs_merge.py <dsl_file>")
        sys.exit(1)

    main(sys.argv[1])
