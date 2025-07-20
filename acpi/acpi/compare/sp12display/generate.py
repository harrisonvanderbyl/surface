#!/usr/bin/env python3
"""
AML to Object Converter

This script reads an AML source file and converts it into instantiated objects
using the generated AML classes. It creates a complete object hierarchy that
mirrors the original AML structure.
"""

import re
import json
import os
import sys
from typing import Dict, List, Any, Optional, Union, Tuple
from dataclasses import dataclass


class AMLConverter:
    """Converts AML source files into instantiated object hierarchies."""
    
    def __init__(self, classes_module_path: str = None):
        self.classes_module = None
        self.devices = []
        self.current_scope = None
        
        # If classes module path is provided, try to import it
        if classes_module_path and os.path.exists(classes_module_path):
            self._import_classes_module(classes_module_path)
    
    def _import_classes_module(self, module_path: str) -> None:
        """Dynamically import the generated classes module."""
        import importlib.util
        
        spec = importlib.util.spec_from_file_location("aml_classes", module_path)
        self.classes_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.classes_module)
        print(f"Successfully imported classes from {module_path}")
    
    def convert_file(self, aml_file_path: str) -> List:
        """Convert an AML file to object instances."""
        with open(aml_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return self.convert_content(content)
    
    def convert_content(self, content: str) -> List:
        """Convert AML content string to object instances."""
        # Clean and normalize the content
        content = self._normalize_content(content)
        
        # Parse the structure
        parsed_structure = self._parse_aml_structure(content)
        
        # Convert to objects
        self.devices = self._create_objects_from_structure(parsed_structure)
        
        return self.devices
    
    def _normalize_content(self, content: str) -> str:
        """Normalize AML content for easier parsing."""
        # Remove comments
        content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        
        # Normalize whitespace
        content = re.sub(r'\s+', ' ', content)
        
        # Normalize package syntax
        content = re.sub(r'Package\s*\(\s*0x([0-9A-Fa-f]+)\s*\)', r'Package(\1)', content)
        content = re.sub(r'Package\s*\(\s*(\d+)\s*\)', r'Package(\1)', content)
        
        # Normalize common ACPI constants
        replacements = {
            'Zero': '0',
            'One': '1',
            'Ones': '0xFFFFFFFF'
        }
        
        for old, new in replacements.items():
            content = re.sub(rf'\b{old}\b', new, content)
        
        return content.strip()
    
    def _parse_aml_structure(self, content: str) -> Dict[str, Any]:
        """Parse the AML structure into a nested dictionary."""
        structure = {
            'scope': None,
            'variables': {},
            'devices': []
        }
        
        # Extract scope
        scope_match = re.search(r'Scope\s*\(\s*([^)]+)\s*\)', content)
        if scope_match:
            structure['scope'] = scope_match.group(1).strip()
        
        # Find all Name definitions (like IDP0)
        name_pattern = r'Name\s*\(\s*([^,]+),\s*Package\s*\([^)]+\)\s*\{(.*?)\}\s*\)'
        name_matches = re.finditer(name_pattern, content, re.DOTALL)
        
        for match in name_matches:
            var_name = match.group(1).strip()
            var_content = match.group(2)
            
            if 'IDP' in var_name:  # Assuming IDP contains device definitions
                structure['devices'] = self._parse_device_list(var_content)
            else:
                structure['variables'][var_name] = self._parse_package_content(var_content)
        
        return structure
    
    def _parse_device_list(self, content: str) -> List[Dict[str, Any]]:
        """Parse a list of device packages."""
        devices = []
        
        # Find top-level packages that represent devices
        package_depth = 0
        current_package = ""
        package_start = -1
        
        i = 0
        while i < len(content):
            if content[i:i+7] == 'Package':
                if package_depth == 0:
                    package_start = i
                package_depth += 1
                # Skip to the opening brace
                brace_pos = content.find('{', i)
                if brace_pos != -1:
                    i = brace_pos + 1
                continue
            elif content[i] == '{':
                package_depth += 1
            elif content[i] == '}':
                package_depth -= 1
                if package_depth == 0 and package_start != -1:
                    # We've found a complete top-level package
                    package_content = content[package_start:i+1]
                    device = self._parse_device_package(package_content)
                    if device:
                        devices.append(device)
                    package_start = -1
            
            i += 1
        
        return devices
    
    def _parse_device_package(self, content: str) -> Optional[Dict[str, Any]]:
        """Parse a single device package."""
        # Extract the package contents between braces
        brace_start = content.find('{')
        brace_end = content.rfind('}')
        
        if brace_start == -1 or brace_end == -1:
            return None
        
        inner_content = content[brace_start+1:brace_end]
        elements = self._parse_package_elements(inner_content)
        
        # Check if this is a device package
        if not elements or (isinstance(elements[0], str) and elements[0] != "DEVICE"):
            return None
        
        device = {
            'type': 'DEVICE',
            'id': None,
            'path': None,
            'components': []
        }
        
        # Parse device elements: ["DEVICE", id, path, components_package]
        if len(elements) >= 3:
            if len(elements) > 1:
                device['id'] = elements[1]
            if len(elements) > 2:
                device['path'] = elements[2]
            if len(elements) > 3 and isinstance(elements[3], dict):
                device['components'] = self._parse_components_package(elements[3])
        
        return device
    
    def _parse_components_package(self, package_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Parse components within a device package."""
        components = []
        
        if 'elements' not in package_data:
            return components
        
        elements = package_data['elements']
        i = 0
        
        while i < len(elements):
            if isinstance(elements[i], str) and elements[i] == "COMPONENT":
                component = {
                    'type': 'COMPONENT',
                    'id': 0,
                    'fstates': [],
                    'pstates': []
                }
                
                # Get component ID
                if i + 1 < len(elements):
                    component['id'] = elements[i + 1]
                
                # Look for FSTATE/PSTATE packages
                if i + 2 < len(elements) and isinstance(elements[i + 2], dict):
                    states_package = elements[i + 2]
                    component['fstates'] = self._parse_states_package(states_package, 'FSTATE')
                    component['pstates'] = self._parse_states_package(states_package, 'PSTATE')
                
                components.append(component)
                i += 3
            else:
                i += 1
        
        return components
    
    def _parse_states_package(self, package_data: Dict[str, Any], state_type: str) -> List[Dict[str, Any]]:
        """Parse FSTATE or PSTATE packages."""
        states = []
        
        if 'elements' not in package_data:
            return states
        
        elements = package_data['elements']
        i = 0
        
        while i < len(elements):
            if isinstance(elements[i], str) and elements[i] == state_type:
                state = {
                    'type': state_type,
                    'id': 0,
                    'resources': []
                }
                
                # Get state ID
                if i + 1 < len(elements):
                    state['id'] = elements[i + 1]
                
                # Parse resources
                if i + 2 < len(elements) and isinstance(elements[i + 2], dict):
                    resources_package = elements[i + 2]
                    state['resources'] = self._parse_resources_package(resources_package)
                
                states.append(state)
                i += 3
            else:
                i += 1
        
        return states
    
    def _parse_resources_package(self, package_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Parse resources within a state package."""
        resources = []
        
        if 'elements' not in package_data:
            return resources
        
        elements = package_data['elements']
        i = 0
        
        while i < len(elements):
            if isinstance(elements[i], str):
                resource_type = elements[i]
                
                # Look for the next element which should be the resource data
                if i + 1 < len(elements) and isinstance(elements[i + 1], dict):
                    resource_data = elements[i + 1]
                    resource = self._parse_single_resource(resource_type, resource_data)
                    if resource:
                        resources.append(resource)
                    i += 2
                else:
                    i += 1
            else:
                i += 1
        
        return resources
    
    def _parse_single_resource(self, resource_type: str, resource_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Parse a single resource based on its type."""
        resource = {
            'type': resource_type,
            'parameters': {}
        }
        
        if 'elements' not in resource_data:
            return resource
        
        elements = resource_data['elements']
        
        # Parse based on resource type
        if resource_type == "CLOCK":
            if len(elements) >= 2:
                resource['parameters'] = {
                    'clock_name': elements[0] if isinstance(elements[0], str) else None,
                    'state': elements[1] if len(elements) > 1 else 0,
                    'frequency': elements[2] if len(elements) > 2 else None
                }
        
        elif resource_type == "BUSARB":
            if len(elements) >= 5:
                resource['parameters'] = {
                    'arb_type': elements[0] if len(elements) > 0 else 0,
                    'master': elements[1] if len(elements) > 1 else None,
                    'slave': elements[2] if len(elements) > 2 else None,
                    'bandwidth': elements[3] if len(elements) > 3 else 0,
                    'latency': elements[4] if len(elements) > 4 else 0
                }
        
        elif resource_type == "NPARESOURCE":
            if len(elements) >= 3:
                resource['parameters'] = {
                    'enable': elements[0] if len(elements) > 0 else 0,
                    'resource_name': elements[1] if len(elements) > 1 else None,
                    'value': elements[2] if len(elements) > 2 else 0
                }
        
        elif resource_type == "PMICVREGVOTE":
            if len(elements) >= 8:
                resource['parameters'] = {
                    'resource_id': elements[0] if len(elements) > 0 else None,
                    'enable': elements[1] if len(elements) > 1 else 0,
                    'voltage': elements[2] if len(elements) > 2 else 0,
                    'enable_state': elements[3] if len(elements) > 3 else 0,
                    'mode': elements[4] if len(elements) > 4 else 0,
                    'head_room': elements[5] if len(elements) > 5 else 0,
                    'driver': elements[6] if len(elements) > 6 else None,
                    'required': elements[7] if len(elements) > 7 else None
                }
        
        elif resource_type == "TLMMGPIO":
            if len(elements) >= 6:
                resource['parameters'] = {
                    'gpio_num': elements[0] if len(elements) > 0 else 0,
                    'enable': elements[1] if len(elements) > 1 else 0,
                    'direction': elements[2] if len(elements) > 2 else 0,
                    'value': elements[3] if len(elements) > 3 else 0,
                    'pull': elements[4] if len(elements) > 4 else 0,
                    'strength': elements[5] if len(elements) > 5 else 0
                }
        
        elif resource_type == "DELAY":
            if len(elements) >= 1:
                resource['parameters'] = {
                    'delay_us': elements[0] if len(elements) > 0 else 0
                }
        
        else:
            # Generic resource handling
            resource['parameters'] = {f'param_{i}': elem for i, elem in enumerate(elements)}
        
        return resource
    
    def _parse_package_elements(self, content: str) -> List[Any]:
        """Parse package elements (strings, numbers, nested packages)."""
        elements = []
        i = 0
        
        while i < len(content):
            # Skip whitespace and commas
            while i < len(content) and content[i] in ' \t\n\r,':
                i += 1
            
            if i >= len(content):
                break
            
            # Parse quoted strings
            if content[i] == '"':
                end_quote = content.find('"', i + 1)
                if end_quote != -1:
                    elements.append(content[i+1:end_quote])
                    i = end_quote + 1
                else:
                    i += 1
            
            # Parse hex numbers
            elif content[i:i+2] == '0x' or content[i:i+2] == '0X':
                hex_match = re.match(r'0x[0-9A-Fa-f]+', content[i:])
                if hex_match:
                    elements.append(hex_match.group(0))
                    i += len(hex_match.group(0))
                else:
                    i += 1
            
            # Parse decimal numbers
            elif content[i].isdigit():
                num_match = re.match(r'\d+', content[i:])
                if num_match:
                    elements.append(int(num_match.group(0)))
                    i += len(num_match.group(0))
                else:
                    i += 1
            
            # Parse nested packages
            elif content[i:i+7] == 'Package':
                package_start = i
                package_depth = 0
                brace_found = False
                
                # Find the opening brace
                while i < len(content) and not brace_found:
                    if content[i] == '{':
                        brace_found = True
                        package_depth = 1
                        i += 1
                        break
                    i += 1
                
                if brace_found:
                    package_content_start = i
                    
                    # Find matching closing brace
                    while i < len(content) and package_depth > 0:
                        if content[i] == '{':
                            package_depth += 1
                        elif content[i] == '}':
                            package_depth -= 1
                        i += 1
                    
                    if package_depth == 0:
                        package_content = content[package_content_start:i-1]
                        nested_elements = self._parse_package_elements(package_content)
                        elements.append({
                            'type': 'package',
                            'elements': nested_elements
                        })
                    else:
                        i += 1
                else:
                    i += 1
            
            else:
                i += 1
        
        return elements
    
    def _parse_package_content(self, content: str) -> Dict[str, Any]:
        """Parse generic package content."""
        return {
            'type': 'package',
            'elements': self._parse_package_elements(content)
        }
    
    def _create_objects_from_structure(self, structure: Dict[str, Any]) -> List:
        """Create object instances from the parsed structure."""
        if not self.classes_module:
            print("Warning: No classes module loaded. Returning parsed structure as-is.")
            return structure
        
        devices = []
        
        for device_data in structure.get('devices', []):
            device = self._create_device_object(device_data)
            if device:
                devices.append(device)
        
        return devices
    
    def _create_device_object(self, device_data: Dict[str, Any]):
        """Create a Device object from device data."""
        if not hasattr(self.classes_module, 'Device'):
            print("Warning: Device class not found in module")
            return device_data
        
        Device = self.classes_module.Device
        device = Device(
            device_id=device_data.get('id'),
            path=device_data.get('path')
        )
        
        # Add components
        for comp_data in device_data.get('components', []):
            component = self._create_component_object(comp_data)
            if component:
                device.add_component(component)
        
        return device
    
    def _create_component_object(self, comp_data: Dict[str, Any]):
        """Create a Component object from component data."""
        if not hasattr(self.classes_module, 'Component'):
            print("Warning: Component class not found in module")
            return comp_data
        
        Component = self.classes_module.Component
        component = Component(comp_data.get('id', 0))
        
        # Add fstates
        for fstate_data in comp_data.get('fstates', []):
            fstate = self._create_fstate_object(fstate_data)
            if fstate:
                component.add_fstate(fstate)
        
        # Add pstates
        for pstate_data in comp_data.get('pstates', []):
            pstate = self._create_pstate_object(pstate_data)
            if pstate:
                component.add_pstate(pstate)
        
        return component
    
    def _create_fstate_object(self, fstate_data: Dict[str, Any]):
        """Create an Fstate object from fstate data."""
        if not hasattr(self.classes_module, 'Fstate'):
            print("Warning: Fstate class not found in module")
            return fstate_data
        
        Fstate = self.classes_module.Fstate
        fstate = Fstate(fstate_data.get('id', 0))
        
        # Add resources
        for resource_data in fstate_data.get('resources', []):
            resource = self._create_resource_object(resource_data)
            if resource:
                fstate.add_resource(resource)
        
        return fstate
    
    def _create_pstate_object(self, pstate_data: Dict[str, Any]):
        """Create a Pstate object from pstate data."""
        # If Pstate class exists, use it; otherwise treat like Fstate
        if hasattr(self.classes_module, 'Pstate'):
            Pstate = self.classes_module.Pstate
            return Pstate(pstate_data.get('id', 0))
        else:
            return self._create_fstate_object(pstate_data)
    
    def _create_resource_object(self, resource_data: Dict[str, Any]):
        """Create a resource object based on its type."""
        resource_type = resource_data.get('type', '')
        parameters = resource_data.get('parameters', {})
        
        # Try to find the appropriate class
        class_name = resource_type.title().replace('_', '')
        
        if hasattr(self.classes_module, class_name):
            ResourceClass = getattr(self.classes_module, class_name)
            try:
                return ResourceClass(**parameters)
            except Exception as e:
                print(f"Warning: Could not create {class_name} object: {e}")
                # Fall back to generic object
                return self._create_generic_resource(resource_type, parameters)
        else:
            return self._create_generic_resource(resource_type, parameters)
    
    def _create_generic_resource(self, resource_type: str, parameters: Dict[str, Any]):
        """Create a generic resource object."""
        if hasattr(self.classes_module, 'AMLPackage'):
            AMLPackage = self.classes_module.AMLPackage
            resource = AMLPackage(resource_type)
            resource.parameters = parameters
            return resource
        else:
            return {'type': resource_type, 'parameters': parameters}
    
    def print_object_hierarchy(self, devices: List = None) -> None:
        """Print the object hierarchy in a readable format."""
        if devices is None:
            devices = self.devices
        
        for i, device in enumerate(devices):
            print(f"Device {i}: {device}")
            
            if hasattr(device, 'components'):
                for j, component in enumerate(device.components):
                    print(f"  Component {j}: {component}")
                    
                    if hasattr(component, 'fstates'):
                        for k, fstate in enumerate(component.fstates):
                            print(f"    FState {k}: {fstate}")
                            
                            if hasattr(fstate, 'resources'):
                                for l, resource in enumerate(fstate.resources):
                                    print(f"      Resource {l}: {resource}")
    
    def save_as_json(self, filename: str, devices: List = None) -> None:
        """Save the object hierarchy as JSON (for debugging)."""
        if devices is None:
            devices = self.devices
        
        # Convert objects to dictionaries for JSON serialization
        def obj_to_dict(obj):
            if hasattr(obj, '__dict__'):
                return {key: obj_to_dict(value) for key, value in obj.__dict__.items()}
            elif isinstance(obj, list):
                return [obj_to_dict(item) for item in obj]
            else:
                return obj
        
        json_data = obj_to_dict(devices)
        
        with open(filename, 'w') as f:
            json.dump(json_data, f, indent=2)
        
        print(f"Object hierarchy saved to {filename}")


def main():
    """Main function to demonstrate the converter."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert AML files to object instances')
    parser.add_argument('aml_file', help='Path to the AML source file')
    parser.add_argument('--classes', help='Path to the generated classes module', 
                       default='generated_aml_classes.py')
    parser.add_argument('--output', help='Output file for JSON representation',
                       default='converted_objects.json')
    parser.add_argument('--print-hierarchy', action='store_true',
                       help='Print the object hierarchy to console')
    
    args = parser.parse_args()
    
    # Check if files exist
    if not os.path.exists(args.aml_file):
        print(f"Error: AML file '{args.aml_file}' not found")
        sys.exit(1)
    
    if not os.path.exists(args.classes):
        print(f"Warning: Classes file '{args.classes}' not found")
        print("Will return parsed structure without object instantiation")
        args.classes = None
    
    # Create converter and process file
    converter = AMLConverter(args.classes)
    
    try:
        devices = converter.convert_file(args.aml_file)
        
        print(f"Successfully converted {args.aml_file}")
        print(f"Found {len(devices)} device(s)")
        
        # Print hierarchy if requested
        if args.print_hierarchy:
            print("\nObject Hierarchy:")
            print("-" * 50)
            converter.print_object_hierarchy(devices)
        
        # Save as JSON
        converter.save_as_json(args.output, devices)
        
    except Exception as e:
        print(f"Error converting file: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    # If running without command line args, use the sample data
    if len(sys.argv) == 1:
        print("Demo mode: Using sample AML content")
        
        # Sample AML content for demonstration
        sample_content = '''
        Scope (\\_SB)
        {
            Name (IDP0, Package (0x01)
            {
                Package (0x04)
                {
                    "DEVICE", 
                    0x82, 
                    "\\_SB.GPU0", 
                    Package (0x0C)
                    {
                        "COMPONENT", 
                        Zero, 
                        Package (0x03)
                        {
                            "FSTATE", 
                            Zero, 
                            Package (0x1E)
                            {
                                Package (0x02)
                                {
                                    "CLOCK", 
                                    Package (0x02)
                                    {
                                        "gcc_disp_xo_clk", 
                                        One
                                    }
                                }, 
                                Package (0x02)
                                {
                                    "BUSARB", 
                                    Package (0x05)
                                    {
                                        0x03, 
                                        "ICBID_MASTER_APPSS_PROC", 
                                        "ICBID_SLAVE_DISPLAY_CFG", 
                                        0x023C3460, 
                                        Zero
                                    }
                                }
                            }
                        }
                    }
                }
            })
        }
        '''
        
        converter = AMLConverter()
        devices = converter.convert_content(sample_content)
        
        print("Parsed structure:")
        converter.print_object_hierarchy(devices)
        
        converter.save_as_json("demo_output.json", devices)
    else:
        main()