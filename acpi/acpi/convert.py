#!/usr/bin/env python3
"""
AML to Object-Oriented Parser

This script parses ACPI AML code and converts it into object-oriented Python classes.
It automatically detects package types and creates corresponding class definitions.
"""

import re
import json
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from collections import defaultdict


class AMLParser:
    """Parser for ACPI AML code that converts packages into object-oriented structures."""
    
    def __init__(self):
        self.package_types = set()
        self.parsed_data = {}
        self.class_definitions = {}
        
    def parse_file(self, content: str) -> Dict[str, Any]:
        """Parse the AML content and extract package structures."""
        # Clean up the content
        content = self._clean_content(content)
        
        # Find all package types
        self._extract_package_types(content)
        
        # Parse the main structure
        self.parsed_data = self._parse_packages(content)
        
        # Generate class definitions
        self._generate_classes()
        
        return self.parsed_data
    
    def _clean_content(self, content: str) -> str:
        """Clean and normalize the AML content."""
        # Remove extra whitespace and normalize
        content = re.sub(r'\s+', ' ', content)
        # Fix package syntax
        content = re.sub(r'Package\s*\(\s*0x([0-9A-Fa-f]+)\s*\)', r'Package(\1)', content)
        return content.strip()
    
    def _extract_package_types(self, content: str) -> None:
        """Extract all unique package types from the content."""
        # Find quoted strings that appear to be package types
        type_pattern = r'"([A-Z_][A-Z0-9_]*)"'
        matches = re.findall(type_pattern, content)
        
        # Common AML package types
        known_types = {
            'DEVICE', 'COMPONENT', 'FSTATE', 'PSTATE', 'EXIT', 'ENTRY',
            'NPARESOURCE', 'BUSARB', 'CLOCK', 'FOOTSWITCH', 'PMICVREGVOTE',
            'TLMMGPIO', 'DELAY', 'PMICGPIO', 'IOCTL_PM_GPIO_CONFIG_DIGITAL_OUTPUT'
        }
        
        # Add found types to our set
        for match in matches:
            if match in known_types or len(match) > 3:  # Filter out short non-type strings
                self.package_types.add(match)
        
        print(f"Found package types: {sorted(self.package_types)}")
    
    def _parse_packages(self, content: str) -> Dict[str, Any]:
        """Parse package structures recursively."""
        # This is a simplified parser - in reality, AML parsing is quite complex
        # We'll focus on the structure visible in the provided example
        
        result = {
            "scope": "_SB",
            "devices": []
        }
        
        # Extract the main IDP0 package content
        idp0_match = re.search(r'Name \(IDP0, Package.*?\{(.*)\}\s*\)', content, re.DOTALL)
        if idp0_match:
            package_content = idp0_match.group(1)
            result["devices"] = self._parse_device_packages(package_content)
        
        return result
    
    def _parse_device_packages(self, content: str) -> List[Dict[str, Any]]:
        """Parse device package structures."""
        devices = []
        
        # Find device packages
        device_pattern = r'Package \([^)]+\)\s*\{\s*"DEVICE"[^}]+\}'
        device_matches = re.finditer(device_pattern, content, re.DOTALL)
        
        for match in device_matches:
            device_content = match.group(0)
            device = self._parse_single_device(device_content)
            if device:
                devices.append(device)
        
        return devices
    
    def _parse_single_device(self, content: str) -> Optional[Dict[str, Any]]:
        """Parse a single device package."""
        # Extract basic device info
        parts = re.findall(r'"([^"]+)"|0x([0-9A-Fa-f]+)|(\d+)', content)
        
        if not parts:
            return None
        
        device = {
            "type": "DEVICE",
            "id": None,
            "path": None,
            "components": []
        }
        
        # Parse the device structure based on the pattern in the file
        string_parts = [p[0] for p in parts if p[0]]
        hex_parts = [p[1] for p in parts if p[1]]
        
        if len(string_parts) >= 2:
            device["path"] = string_parts[1] if string_parts[1].startswith("\\") else None
        
        if hex_parts:
            device["id"] = hex_parts[0]
        
        # Parse components
        components = self._parse_components(content)
        device["components"] = components
        
        return device
    
    def _parse_components(self, content: str) -> List[Dict[str, Any]]:
        """Parse component structures within a device."""
        components = []
        
        # Look for COMPONENT packages
        component_pattern = r'"COMPONENT"[^}]+\}'
        component_matches = re.finditer(component_pattern, content, re.DOTALL)
        
        for match in component_matches:
            component_content = match.group(0)
            component = {
                "type": "COMPONENT",
                "id": 0,
                "fstates": self._parse_fstates(component_content)
            }
            components.append(component)
        
        return components
    
    def _parse_fstates(self, content: str) -> List[Dict[str, Any]]:
        """Parse FSTATE structures."""
        fstates = []
        
        # Look for FSTATE packages
        fstate_pattern = r'"FSTATE"[^}]+\}'
        fstate_matches = re.finditer(fstate_pattern, content, re.DOTALL)
        
        for match in fstate_matches:
            fstate_content = match.group(0)
            fstate = {
                "type": "FSTATE",
                "id": 0,
                "resources": self._parse_resources(fstate_content)
            }
            fstates.append(fstate)
        
        return fstates
    
    def _parse_resources(self, content: str) -> List[Dict[str, Any]]:
        """Parse resource packages within FSTATE."""
        resources = []
        
        # Parse different resource types
        for package_type in self.package_types:
            if package_type in ['DEVICE', 'COMPONENT', 'FSTATE']:
                continue
                
            pattern = rf'"{package_type}"[^}}]+\}}'
            matches = re.finditer(pattern, content, re.DOTALL)
            
            for match in matches:
                resource_content = match.group(0)
                resource = self._parse_resource(package_type, resource_content)
                if resource:
                    resources.append(resource)
        
        return resources
    
    def _parse_resource(self, resource_type: str, content: str) -> Optional[Dict[str, Any]]:
        """Parse a specific resource type."""
        # Extract values from the resource content
        values = []
        
        # Find quoted strings
        string_matches = re.findall(r'"([^"]+)"', content)
        values.extend(string_matches)
        
        # Find hex numbers
        hex_matches = re.findall(r'0x([0-9A-Fa-f]+)', content)
        values.extend([f"0x{h}" for h in hex_matches])
        
        # Find decimal numbers
        dec_matches = re.findall(r'\b(\d+)\b', content)
        values.extend(dec_matches)
        
        return {
            "type": resource_type,
            "values": values
        }
    
    def _generate_classes(self) -> None:
        """Generate Python class definitions based on discovered package types."""
        self.class_definitions = {}
        
        # Base class
        base_class = '''
class AMLPackage:
    """Base class for all AML package types."""
    
    def __init__(self, package_type: str):
        self.type = package_type
        self.values = []
    
    def __repr__(self):
        return f"{self.__class__.__name__}(type='{self.type}')"
'''
        self.class_definitions['AMLPackage'] = base_class
        
        # Generate specific classes
        for package_type in sorted(self.package_types):
            class_def = self._generate_class_definition(package_type)
            self.class_definitions[package_type] = class_def
    
    def _generate_class_definition(self, package_type: str) -> str:
        """Generate a class definition for a specific package type."""
        class_name = package_type.title().replace('_', '')
        
        if package_type == 'DEVICE':
            return f'''
class {class_name}(AMLPackage):
    """Represents a device package in AML."""
    
    def __init__(self, device_id: str = None, path: str = None):
        super().__init__("DEVICE")
        self.device_id = device_id
        self.path = path
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)
    
    def __repr__(self):
        return f"{class_name}(id='{"{self.device_id}"}', path='{"{self.path}"}')"
'''
        
        elif package_type == 'COMPONENT':
            return f'''
class {class_name}(AMLPackage):
    """Represents a component package in AML."""
    
    def __init__(self, component_id: int = 0):
        super().__init__("COMPONENT")
        self.component_id = component_id
        self.fstates = []
        self.pstates = []
    
    def add_fstate(self, fstate):
        self.fstates.append(fstate)
    
    def add_pstate(self, pstate):
        self.pstates.append(pstate)
    
    def __repr__(self):
        return f"{class_name}(id={"{self.component_id}"})"
'''
        
        elif package_type == 'FSTATE':
            return f'''
class {class_name}(AMLPackage):
    """Represents an FSTATE (functional state) package in AML."""
    
    def __init__(self, state_id: int = 0):
        super().__init__("FSTATE")
        self.state_id = state_id
        self.resources = []
        self.exit_resources = []
        self.entry_resources = []
    
    def add_resource(self, resource):
        self.resources.append(resource)
    
    def add_exit_resource(self, resource):
        self.exit_resources.append(resource)
    
    def add_entry_resource(self, resource):
        self.entry_resources.append(resource)
    
    def __repr__(self):
        return f"{class_name}(id={"{self.state_id}"})"
'''
        
        elif package_type == 'CLOCK':
            return f'''
class {class_name}(AMLPackage):
    """Represents a clock resource package in AML."""
    
    def __init__(self, clock_name: str = None, state: int = 0, frequency: int = None):
        super().__init__("CLOCK")
        self.clock_name = clock_name
        self.state = state
        self.frequency = frequency
    
    def __repr__(self):
        return f"{class_name}(name='{"{self.clock_name}"}', state={"{self.state}"})"
'''
        
        elif package_type == 'BUSARB':
            return f'''
class {class_name}(AMLPackage):
    """Represents a bus arbitration resource package in AML."""
    
    def __init__(self, arb_type: int = 0, master: str = None, slave: str = None, 
                 bandwidth: int = 0, latency: int = 0):
        super().__init__("BUSARB")
        self.arb_type = arb_type
        self.master = master
        self.slave = slave
        self.bandwidth = bandwidth
        self.latency = latency
    
    def __repr__(self):
        return f"{class_name}(master='{"{self.master}"}', slave='{"{self.slave}"}')"
'''
        
        else:
            # Generic class for other types
            return f'''
class {class_name}(AMLPackage):
    """Represents a {package_type} package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("{package_type}")
        self.properties = kwargs
    
    def __repr__(self):
        return f"{class_name}({"{self.properties}"})"
'''
    
    def generate_python_code(self) -> str:
        """Generate complete Python code with all classes."""
        code = '''#!/usr/bin/env python3
"""
Generated AML Object-Oriented Classes

This file contains object-oriented representations of AML packages.
Generated automatically from AML source code.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass

'''
        
        # Add all class definitions
        for class_name, class_def in self.class_definitions.items():
            code += class_def + '\n'
        
        # Add a factory function
        code += '''
class AMLFactory:
    """Factory class for creating AML objects from parsed data."""
    
    @staticmethod
    def create_from_data(data: Dict[str, Any]) -> List[Device]:
        """Create AML objects from parsed data structure."""
        devices = []
        
        for device_data in data.get('devices', []):
            device = Device(
                device_id=device_data.get('id'),
                path=device_data.get('path')
            )
            
            for comp_data in device_data.get('components', []):
                component = Component(comp_data.get('id', 0))
                
                for fstate_data in comp_data.get('fstates', []):
                    fstate = Fstate(fstate_data.get('id', 0))
                    
                    for resource_data in fstate_data.get('resources', []):
                        resource_type = resource_data.get('type', '')
                        resource_class = globals().get(resource_type.title().replace('_', ''))
                        
                        if resource_class:
                            resource = resource_class(**resource_data.get('values', {}))
                            fstate.add_resource(resource)
                    
                    component.add_fstate(fstate)
                
                device.add_component(component)
            
            devices.append(device)
        
        return devices

# Example usage:
if __name__ == "__main__":
    # Example of how to use the generated classes
    device = Device("0x82", "\\\\_SB.GPU0")
    component = Component(0)
    fstate = Fstate(0)
    
    # Add some resources
    clock = Clock("gcc_disp_xo_clk", 1)
    fstate.add_resource(clock)
    
    busarb = Busarb(3, "ICBID_MASTER_APPSS_PROC", "ICBID_SLAVE_DISPLAY_CFG", 0x023C3460, 0)
    fstate.add_resource(busarb)
    
    component.add_fstate(fstate)
    device.add_component(component)
    
    print(f"Created device: {device}")
    print(f"With component: {component}")
    print(f"With fstate: {fstate}")
'''
        
        return code
    
    def save_classes(self, filename: str = "aml_classes.py") -> None:
        """Save the generated classes to a Python file."""
        code = self.generate_python_code()
        with open(filename, 'w') as f:
            f.write(code)
        print(f"Generated classes saved to {filename}")


def main():
    """Main function to demonstrate the parser."""
    # Read the AML content from the provided file
    content = open("./dsdt.dsl", "r").read()
    
    # Parse the content
    parser = AMLParser()
    parsed_data = parser.parse_file(content)
    
    print("Parsed data structure:")
    print(json.dumps(parsed_data, indent=2))
    
    print("\nGenerated class definitions:")
    for class_name in sorted(parser.class_definitions.keys()):
        print(f"- {class_name}")
    
    # Generate and save the Python code
    parser.save_classes("generated_aml_classes.py")
    
    print("\nGenerated Python code preview:")
    print(parser.generate_python_code()[:1000] + "...")


if __name__ == "__main__":
    main()