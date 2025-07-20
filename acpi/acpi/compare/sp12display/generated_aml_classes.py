#!/usr/bin/env python3
"""
Generated AML Object-Oriented Classes

This file contains object-oriented representations of AML packages.
Generated automatically from AML source code.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass


class AMLPackage:
    """Base class for all AML package types."""
    
    def __init__(self, package_type: str):
        self.type = package_type
        self.values = []
    
    def __repr__(self):
        return f"{self.__class__.__name__}(type='{self.type}')"


class Busarb(AMLPackage):
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
        return f"Busarb(master='{self.master}', slave='{self.slave}')"


class Clock(AMLPackage):
    """Represents a clock resource package in AML."""
    
    def __init__(self, clock_name: str = None, state: int = 0, frequency: int = None):
        super().__init__("CLOCK")
        self.clock_name = clock_name
        self.state = state
        self.frequency = frequency
    
    def __repr__(self):
        return f"Clock(name='{self.clock_name}', state={self.state})"


class Component(AMLPackage):
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
        return f"Component(id={self.component_id})"


class Delay(AMLPackage):
    """Represents a DELAY package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DELAY")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Delay({self.properties})"


class Device(AMLPackage):
    """Represents a device package in AML."""
    
    def __init__(self, device_id: str = None, path: str = None):
        super().__init__("DEVICE")
        self.device_id = device_id
        self.path = path
        self.components = []
    
    def add_component(self, component):
        self.components.append(component)
    
    def __repr__(self):
        return f"Device(id='{self.device_id}', path='{self.path}')"


class Exit(AMLPackage):
    """Represents a EXIT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("EXIT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Exit({self.properties})"


class Footswitch(AMLPackage):
    """Represents a FOOTSWITCH package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("FOOTSWITCH")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Footswitch({self.properties})"


class Fstate(AMLPackage):
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
        return f"Fstate(id={self.state_id})"


class HlosDrv(AMLPackage):
    """Represents a HLOS_DRV package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("HLOS_DRV")
        self.properties = kwargs
    
    def __repr__(self):
        return f"HlosDrv({self.properties})"


class IcbidMasterAppssProc(AMLPackage):
    """Represents a ICBID_MASTER_APPSS_PROC package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_APPSS_PROC")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterAppssProc({self.properties})"


class IcbidMasterMdp(AMLPackage):
    """Represents a ICBID_MASTER_MDP package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_MDP")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterMdp({self.properties})"


class IcbidMasterMnocHfMemNoc(AMLPackage):
    """Represents a ICBID_MASTER_MNOC_HF_MEM_NOC package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_MNOC_HF_MEM_NOC")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterMnocHfMemNoc({self.properties})"


class IcbidSlaveDisplayCfg(AMLPackage):
    """Represents a ICBID_SLAVE_DISPLAY_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_DISPLAY_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveDisplayCfg({self.properties})"


class IcbidSlaveEbi1(AMLPackage):
    """Represents a ICBID_SLAVE_EBI1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_EBI1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveEbi1({self.properties})"


class IcbidSlaveMnocHfMemNoc(AMLPackage):
    """Represents a ICBID_SLAVE_MNOC_HF_MEM_NOC package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_MNOC_HF_MEM_NOC")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveMnocHfMemNoc({self.properties})"


class InitFstate(AMLPackage):
    """Represents a INIT_FSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("INIT_FSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"InitFstate({self.properties})"


class IoctlPmGpioConfigDigitalOutput(AMLPackage):
    """Represents a IOCTL_PM_GPIO_CONFIG_DIGITAL_OUTPUT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("IOCTL_PM_GPIO_CONFIG_DIGITAL_OUTPUT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IoctlPmGpioConfigDigitalOutput({self.properties})"


class Nparesource(AMLPackage):
    """Represents a NPARESOURCE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("NPARESOURCE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Nparesource({self.properties})"


class Pmicgpio(AMLPackage):
    """Represents a PMICGPIO package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PMICGPIO")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pmicgpio({self.properties})"


class Pmicvregvote(AMLPackage):
    """Represents a PMICVREGVOTE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PMICVREGVOTE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pmicvregvote({self.properties})"


class PppResourceIdClk6A(AMLPackage):
    """Represents a PPP_RESOURCE_ID_CLK6_A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_CLK6_A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdClk6A({self.properties})"


class PppResourceIdLdo14B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO14_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO14_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo14B({self.properties})"


class PppResourceIdLdo1C(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO1_C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO1_C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo1C({self.properties})"


class PppResourceIdLdo1D(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO1_D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO1_D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo1D({self.properties})"


class PppResourceIdLdo1I(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO1_I package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO1_I")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo1I({self.properties})"


class PppResourceIdLdo1J(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO1_J package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO1_J")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo1J({self.properties})"


class PppResourceIdLdo2B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2B({self.properties})"


class PppResourceIdLdo2C(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2C({self.properties})"


class PppResourceIdLdo2D(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2D({self.properties})"


class PppResourceIdLdo2J(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_J package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_J")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2J({self.properties})"


class PppResourceIdLdo3D(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3D({self.properties})"


class PppResourceIdLdo3J(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_J package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_J")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3J({self.properties})"


class PppResourceIdLdo8B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO8_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO8_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo8B({self.properties})"


class PreloadFstate(AMLPackage):
    """Represents a PRELOAD_FSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PRELOAD_FSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PreloadFstate({self.properties})"


class PreloadPstate(AMLPackage):
    """Represents a PRELOAD_PSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PRELOAD_PSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PreloadPstate({self.properties})"


class Pstate(AMLPackage):
    """Represents a PSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pstate({self.properties})"


class PstateSet(AMLPackage):
    """Represents a PSTATE_SET package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PSTATE_SET")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PstateSet({self.properties})"


class Required(AMLPackage):
    """Represents a REQUIRED package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("REQUIRED")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Required({self.properties})"


class Tlmmgpio(AMLPackage):
    """Represents a TLMMGPIO package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("TLMMGPIO")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Tlmmgpio({self.properties})"


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
    device = Device("0x82", "\\_SB.GPU0")
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
