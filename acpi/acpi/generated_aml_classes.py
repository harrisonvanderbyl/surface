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


class AbandonDstate(AMLPackage):
    """Represents a ABANDON_DSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ABANDON_DSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"AbandonDstate({self.properties})"


class Acpi0007(AMLPackage):
    """Represents a ACPI0007 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ACPI0007")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Acpi0007({self.properties})"


class Acpi000C(AMLPackage):
    """Represents a ACPI000C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ACPI000C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Acpi000C({self.properties})"


class Acpi0010(AMLPackage):
    """Represents a ACPI0010 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ACPI0010")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Acpi0010({self.properties})"


class Acpiqcom06Db(AMLPackage):
    """Represents a ACPIQCOM06DB package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ACPIQCOM06DB")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Acpiqcom06Db({self.properties})"


class Agn00000(AMLPackage):
    """Represents a AGN00000 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("AGN00000")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Agn00000({self.properties})"


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


class Childdev(AMLPackage):
    """Represents a CHILDDEV package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("CHILDDEV")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Childdev({self.properties})"


class Cipr(AMLPackage):
    """Represents a CIPR package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("CIPR")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Cipr({self.properties})"


class Clock(AMLPackage):
    """Represents a clock resource package in AML."""
    
    def __init__(self, clock_name: str = None, state: int = 0, frequency: int = None):
        super().__init__("CLOCK")
        self.clock_name = clock_name
        self.state = state
        self.frequency = frequency
    
    def __repr__(self):
        return f"Clock(name='{self.clock_name}', state={self.state})"


class Compatibleids(AMLPackage):
    """Represents a COMPATIBLEIDS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("COMPATIBLEIDS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Compatibleids({self.properties})"


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


class CoreTopology(AMLPackage):
    """Represents a CORE_TOPOLOGY package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("CORE_TOPOLOGY")
        self.properties = kwargs
    
    def __repr__(self):
        return f"CoreTopology({self.properties})"


class CrashdumpDstate(AMLPackage):
    """Represents a CRASHDUMP_DSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("CRASHDUMP_DSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"CrashdumpDstate({self.properties})"


class CrashdumpException(AMLPackage):
    """Represents a CRASHDUMP_EXCEPTION package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("CRASHDUMP_EXCEPTION")
        self.properties = kwargs
    
    def __repr__(self):
        return f"CrashdumpException({self.properties})"


class Crd08380(AMLPackage):
    """Represents a CRD08380 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("CRD08380")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Crd08380({self.properties})"


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


class Disabl(AMLPackage):
    """Represents a DISABL package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DISABL")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Disabl({self.properties})"


class Display(AMLPackage):
    """Represents a DISPLAY package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DISPLAY")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Display({self.properties})"


class Dm0G(AMLPackage):
    """Represents a DM0G package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DM0G")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dm0G({self.properties})"


class Dm7G(AMLPackage):
    """Represents a DM7G package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DM7G")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dm7G({self.properties})"


class Dm8G(AMLPackage):
    """Represents a DM8G package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DM8G")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dm8G({self.properties})"


class Dm9G(AMLPackage):
    """Represents a DM9G package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DM9G")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dm9G({self.properties})"


class Dmds(AMLPackage):
    """Represents a DMDS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMDS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmds({self.properties})"


class Dmep(AMLPackage):
    """Represents a DMEP package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMEP")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmep({self.properties})"


class Dmkg(AMLPackage):
    """Represents a DMKG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMKG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmkg({self.properties})"


class Dmlg(AMLPackage):
    """Represents a DMLG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMLG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmlg({self.properties})"


class Dmmg(AMLPackage):
    """Represents a DMMG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMMG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmmg({self.properties})"


class Dmpa(AMLPackage):
    """Represents a DMPA package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMPA")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmpa({self.properties})"


class Dmpb(AMLPackage):
    """Represents a DMPB package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMPB")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmpb({self.properties})"


class Dmpl(AMLPackage):
    """Represents a DMPL package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMPL")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmpl({self.properties})"


class Dmpo(AMLPackage):
    """Represents a DMPO package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMPO")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmpo({self.properties})"


class Dmpr(AMLPackage):
    """Represents a DMPR package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMPR")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmpr({self.properties})"


class Dmps(AMLPackage):
    """Represents a DMPS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMPS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmps({self.properties})"


class Dmrs(AMLPackage):
    """Represents a DMRS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMRS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmrs({self.properties})"


class Dmsb(AMLPackage):
    """Represents a DMSB package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DMSB")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dmsb({self.properties})"


class DpAuxPolaritySel5(AMLPackage):
    """Represents a DP_AUX_POLARITY_SEL5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DP_AUX_POLARITY_SEL5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"DpAuxPolaritySel5({self.properties})"


class DpAuxSwitchSel5(AMLPackage):
    """Represents a DP_AUX_SWITCH_SEL5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DP_AUX_SWITCH_SEL5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"DpAuxSwitchSel5({self.properties})"


class DpPhyRegs(AMLPackage):
    """Represents a DP_PHY_REGS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DP_PHY_REGS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"DpPhyRegs({self.properties})"


class Dsdt(AMLPackage):
    """Represents a DSDT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DSDT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dsdt({self.properties})"


class Dstate(AMLPackage):
    """Represents a DSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("DSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Dstate({self.properties})"


class ExecuteFunction(AMLPackage):
    """Represents a EXECUTE_FUNCTION package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("EXECUTE_FUNCTION")
        self.properties = kwargs
    
    def __repr__(self):
        return f"ExecuteFunction({self.properties})"


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


class GfxInterrupt(AMLPackage):
    """Represents a GFX_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("GFX_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"GfxInterrupt({self.properties})"


class GfxLpacInterrupt(AMLPackage):
    """Represents a GFX_LPAC_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("GFX_LPAC_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"GfxLpacInterrupt({self.properties})"


class GfxRegs(AMLPackage):
    """Represents a GFX_REGS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("GFX_REGS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"GfxRegs({self.properties})"


class GmuToHostInterrupt(AMLPackage):
    """Represents a GMU_TO_HOST_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("GMU_TO_HOST_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"GmuToHostInterrupt({self.properties})"


class GpuPdcRegs(AMLPackage):
    """Represents a GPU_PDC_REGS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("GPU_PDC_REGS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"GpuPdcRegs({self.properties})"


class Graphics(AMLPackage):
    """Represents a GRAPHICS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("GRAPHICS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Graphics({self.properties})"


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


class IcbidMasterPcie0(AMLPackage):
    """Represents a ICBID_MASTER_PCIE_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_PCIE_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterPcie0({self.properties})"


class IcbidMasterPcie1(AMLPackage):
    """Represents a ICBID_MASTER_PCIE_1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_PCIE_1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterPcie1({self.properties})"


class IcbidMasterPcie2(AMLPackage):
    """Represents a ICBID_MASTER_PCIE_2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_PCIE_2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterPcie2({self.properties})"


class IcbidMasterPcie3(AMLPackage):
    """Represents a ICBID_MASTER_PCIE_3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_PCIE_3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterPcie3({self.properties})"


class IcbidMasterPcie4(AMLPackage):
    """Represents a ICBID_MASTER_PCIE_4 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_PCIE_4")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterPcie4({self.properties})"


class IcbidMasterPcie5(AMLPackage):
    """Represents a ICBID_MASTER_PCIE_5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_PCIE_5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterPcie5({self.properties})"


class IcbidMasterPcie6A(AMLPackage):
    """Represents a ICBID_MASTER_PCIE_6A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_PCIE_6A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterPcie6A({self.properties})"


class IcbidMasterQup0(AMLPackage):
    """Represents a ICBID_MASTER_QUP_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_QUP_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterQup0({self.properties})"


class IcbidMasterQup1(AMLPackage):
    """Represents a ICBID_MASTER_QUP_1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_QUP_1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterQup1({self.properties})"


class IcbidMasterQupCore0(AMLPackage):
    """Represents a ICBID_MASTER_QUP_CORE_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_QUP_CORE_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterQupCore0({self.properties})"


class IcbidMasterQupCore1(AMLPackage):
    """Represents a ICBID_MASTER_QUP_CORE_1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_QUP_CORE_1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterQupCore1({self.properties})"


class IcbidMasterSdcc2(AMLPackage):
    """Represents a ICBID_MASTER_SDCC_2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_SDCC_2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterSdcc2({self.properties})"


class IcbidMasterUfsMem(AMLPackage):
    """Represents a ICBID_MASTER_UFS_MEM package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_UFS_MEM")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterUfsMem({self.properties})"


class IcbidMasterUsb2(AMLPackage):
    """Represents a ICBID_MASTER_USB2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_USB2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterUsb2({self.properties})"


class IcbidMasterUsb30(AMLPackage):
    """Represents a ICBID_MASTER_USB3_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_USB3_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterUsb30({self.properties})"


class IcbidMasterUsb31(AMLPackage):
    """Represents a ICBID_MASTER_USB3_1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_USB3_1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterUsb31({self.properties})"


class IcbidMasterUsb32(AMLPackage):
    """Represents a ICBID_MASTER_USB3_2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_USB3_2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterUsb32({self.properties})"


class IcbidMasterUsb3Mp(AMLPackage):
    """Represents a ICBID_MASTER_USB3_MP package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_MASTER_USB3_MP")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidMasterUsb3Mp({self.properties})"


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


class IcbidSlavePcie0Cfg(AMLPackage):
    """Represents a ICBID_SLAVE_PCIE_0_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_PCIE_0_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlavePcie0Cfg({self.properties})"


class IcbidSlavePcie1Cfg(AMLPackage):
    """Represents a ICBID_SLAVE_PCIE_1_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_PCIE_1_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlavePcie1Cfg({self.properties})"


class IcbidSlavePcie2Cfg(AMLPackage):
    """Represents a ICBID_SLAVE_PCIE_2_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_PCIE_2_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlavePcie2Cfg({self.properties})"


class IcbidSlavePcie3Cfg(AMLPackage):
    """Represents a ICBID_SLAVE_PCIE_3_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_PCIE_3_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlavePcie3Cfg({self.properties})"


class IcbidSlavePcie4Cfg(AMLPackage):
    """Represents a ICBID_SLAVE_PCIE_4_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_PCIE_4_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlavePcie4Cfg({self.properties})"


class IcbidSlavePcie5Cfg(AMLPackage):
    """Represents a ICBID_SLAVE_PCIE_5_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_PCIE_5_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlavePcie5Cfg({self.properties})"


class IcbidSlavePcie6ACfg(AMLPackage):
    """Represents a ICBID_SLAVE_PCIE_6A_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_PCIE_6A_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlavePcie6ACfg({self.properties})"


class IcbidSlaveQup0(AMLPackage):
    """Represents a ICBID_SLAVE_QUP_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_QUP_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveQup0({self.properties})"


class IcbidSlaveQup1(AMLPackage):
    """Represents a ICBID_SLAVE_QUP_1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_QUP_1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveQup1({self.properties})"


class IcbidSlaveQupCore0(AMLPackage):
    """Represents a ICBID_SLAVE_QUP_CORE_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_QUP_CORE_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveQupCore0({self.properties})"


class IcbidSlaveQupCore1(AMLPackage):
    """Represents a ICBID_SLAVE_QUP_CORE_1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_QUP_CORE_1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveQupCore1({self.properties})"


class IcbidSlaveUfsMemCfg(AMLPackage):
    """Represents a ICBID_SLAVE_UFS_MEM_CFG package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_UFS_MEM_CFG")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveUfsMemCfg({self.properties})"


class IcbidSlaveUsb2(AMLPackage):
    """Represents a ICBID_SLAVE_USB2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_USB2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveUsb2({self.properties})"


class IcbidSlaveUsb30(AMLPackage):
    """Represents a ICBID_SLAVE_USB3_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_USB3_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveUsb30({self.properties})"


class IcbidSlaveUsb31(AMLPackage):
    """Represents a ICBID_SLAVE_USB3_1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_USB3_1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveUsb31({self.properties})"


class IcbidSlaveUsb32(AMLPackage):
    """Represents a ICBID_SLAVE_USB3_2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_USB3_2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveUsb32({self.properties})"


class IcbidSlaveUsb3Mp(AMLPackage):
    """Represents a ICBID_SLAVE_USB3_MP package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("ICBID_SLAVE_USB3_MP")
        self.properties = kwargs
    
    def __repr__(self):
        return f"IcbidSlaveUsb3Mp({self.properties})"


class Idp08380(AMLPackage):
    """Represents a IDP08380 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("IDP08380")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Idp08380({self.properties})"


class Idps8380(AMLPackage):
    """Represents a IDPS8380 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("IDPS8380")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Idps8380({self.properties})"


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


class Left(AMLPackage):
    """Represents a LEFT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("LEFT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Left({self.properties})"


class MdpRegs(AMLPackage):
    """Represents a MDP_REGS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MDP_REGS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"MdpRegs({self.properties})"


class Msbn(AMLPackage):
    """Represents a MSBN package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSBN")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Msbn({self.properties})"


class Msft(AMLPackage):
    """Represents a MSFT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSFT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Msft({self.properties})"


class Mshw0473(AMLPackage):
    """Represents a MSHW0473 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0473")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0473({self.properties})"


class Mshw0474(AMLPackage):
    """Represents a MSHW0474 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0474")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0474({self.properties})"


class Mshw0560(AMLPackage):
    """Represents a MSHW0560 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0560")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0560({self.properties})"


class Mshw0561(AMLPackage):
    """Represents a MSHW0561 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0561")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0561({self.properties})"


class Mshw0562(AMLPackage):
    """Represents a MSHW0562 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0562")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0562({self.properties})"


class Mshw0565(AMLPackage):
    """Represents a MSHW0565 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0565")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0565({self.properties})"


class Mshw0566(AMLPackage):
    """Represents a MSHW0566 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0566")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0566({self.properties})"


class Mshw0567(AMLPackage):
    """Represents a MSHW0567 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0567")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0567({self.properties})"


class Mshw0568(AMLPackage):
    """Represents a MSHW0568 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0568")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0568({self.properties})"


class Mshw0577(AMLPackage):
    """Represents a MSHW0577 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("MSHW0577")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Mshw0577({self.properties})"


class Nparesource(AMLPackage):
    """Represents a NPARESOURCE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("NPARESOURCE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Nparesource({self.properties})"


class Oem2Updx65Mbcl(AMLPackage):
    """Represents a OEM2UPDX65MBCL package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBCL")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbcl({self.properties})"


class Oem2Updx65Mbj0(AMLPackage):
    """Represents a OEM2UPDX65MBJ0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBJ0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbj0({self.properties})"


class Oem2Updx65Mbj1(AMLPackage):
    """Represents a OEM2UPDX65MBJ1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBJ1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbj1({self.properties})"


class Oem2Updx65Mbj2(AMLPackage):
    """Represents a OEM2UPDX65MBJ2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBJ2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbj2({self.properties})"


class Oem2Updx65Mbj3(AMLPackage):
    """Represents a OEM2UPDX65MBJ3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBJ3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbj3({self.properties})"


class Oem2Updx65Mbs0(AMLPackage):
    """Represents a OEM2UPDX65MBS0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBS0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbs0({self.properties})"


class Oem2Updx65Mbs1(AMLPackage):
    """Represents a OEM2UPDX65MBS1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBS1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbs1({self.properties})"


class Oem2Updx65Mbs2(AMLPackage):
    """Represents a OEM2UPDX65MBS2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBS2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbs2({self.properties})"


class Oem2Updx65Mbs3(AMLPackage):
    """Represents a OEM2UPDX65MBS3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MBS3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mbs3({self.properties})"


class Oem2Updx65Mjct(AMLPackage):
    """Represents a OEM2UPDX65MJCT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MJCT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mjct({self.properties})"


class Oem2Updx65Mpa(AMLPackage):
    """Represents a OEM2UPDX65MPA package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MPA")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mpa({self.properties})"


class Oem2Updx65Mpa1(AMLPackage):
    """Represents a OEM2UPDX65MPA1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MPA1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mpa1({self.properties})"


class Oem2Updx65Mskn(AMLPackage):
    """Represents a OEM2UPDX65MSKN package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65MSKN")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Mskn({self.properties})"


class Oem2Updx65Ts01(AMLPackage):
    """Represents a OEM2UPDX65TS01 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX65TS01")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx65Ts01({self.properties})"


class Oem2Updx75Tmd1(AMLPackage):
    """Represents a OEM2UPDX75TMD1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd1({self.properties})"


class Oem2Updx75Tmd2(AMLPackage):
    """Represents a OEM2UPDX75TMD2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd2({self.properties})"


class Oem2Updx75Tmd3(AMLPackage):
    """Represents a OEM2UPDX75TMD3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd3({self.properties})"


class Oem2Updx75Tmd4(AMLPackage):
    """Represents a OEM2UPDX75TMD4 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD4")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd4({self.properties})"


class Oem2Updx75Tmd5(AMLPackage):
    """Represents a OEM2UPDX75TMD5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd5({self.properties})"


class Oem2Updx75Tmd6(AMLPackage):
    """Represents a OEM2UPDX75TMD6 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD6")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd6({self.properties})"


class Oem2Updx75Tmd7(AMLPackage):
    """Represents a OEM2UPDX75TMD7 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD7")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd7({self.properties})"


class Oem2Updx75Tmd8(AMLPackage):
    """Represents a OEM2UPDX75TMD8 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD8")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd8({self.properties})"


class Oem2Updx75Tmd9(AMLPackage):
    """Represents a OEM2UPDX75TMD9 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TMD9")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Tmd9({self.properties})"


class Oem2Updx75Ts1(AMLPackage):
    """Represents a OEM2UPDX75TS1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TS1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Ts1({self.properties})"


class Oem2Updx75Ts2(AMLPackage):
    """Represents a OEM2UPDX75TS2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TS2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Ts2({self.properties})"


class Oem2Updx75Ts3(AMLPackage):
    """Represents a OEM2UPDX75TS3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TS3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Ts3({self.properties})"


class Oem2Updx75Ts4(AMLPackage):
    """Represents a OEM2UPDX75TS4 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TS4")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Ts4({self.properties})"


class Oem2Updx75Ts5(AMLPackage):
    """Represents a OEM2UPDX75TS5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TS5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Ts5({self.properties})"


class Oem2Updx75Ts6(AMLPackage):
    """Represents a OEM2UPDX75TS6 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OEM2UPDX75TS6")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Oem2Updx75Ts6({self.properties})"


class Ovti02C1(AMLPackage):
    """Represents a OVTI02C1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OVTI02C1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Ovti02C1({self.properties})"


class Ovtid858(AMLPackage):
    """Represents a OVTID858 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("OVTID858")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Ovtid858({self.properties})"


class PcieDrv(AMLPackage):
    """Represents a PCIE_DRV package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PCIE_DRV")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PcieDrv({self.properties})"


class PcieForceWakeCmd(AMLPackage):
    """Represents a PCIE_FORCE_WAKE_CMD package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PCIE_FORCE_WAKE_CMD")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PcieForceWakeCmd({self.properties})"


class PcieHwDrvResource(AMLPackage):
    """Represents a PCIE_HW_DRV_RESOURCE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PCIE_HW_DRV_RESOURCE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PcieHwDrvResource({self.properties})"


class PcieL1SsExceptionExecuteFunction(AMLPackage):
    """Represents a PCIE_L1SS_EXCEPTION_EXECUTE_FUNCTION package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PCIE_L1SS_EXCEPTION_EXECUTE_FUNCTION")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PcieL1SsExceptionExecuteFunction({self.properties})"


class PciePlimEnableDisableCmd(AMLPackage):
    """Represents a PCIE_PLIM_ENABLE_DISABLE_CMD package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PCIE_PLIM_ENABLE_DISABLE_CMD")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PciePlimEnableDisableCmd({self.properties})"


class Pm22BclbigBan(AMLPackage):
    """Represents a PM22_BCLBIG_BAN package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PM22_BCLBIG_BAN")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pm22BclbigBan({self.properties})"


class Pm22BclbigLvl0(AMLPackage):
    """Represents a PM22_BCLBIG_LVL0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PM22_BCLBIG_LVL0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pm22BclbigLvl0({self.properties})"


class Pm22BclbigLvl1(AMLPackage):
    """Represents a PM22_BCLBIG_LVL1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PM22_BCLBIG_LVL1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pm22BclbigLvl1({self.properties})"


class Pm22BclbigLvl2(AMLPackage):
    """Represents a PM22_BCLBIG_LVL2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PM22_BCLBIG_LVL2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pm22BclbigLvl2({self.properties})"


class Pm2BclbigBan(AMLPackage):
    """Represents a PM2_BCLBIG_BAN package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PM2_BCLBIG_BAN")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pm2BclbigBan({self.properties})"


class Pm2BclbigLvl0(AMLPackage):
    """Represents a PM2_BCLBIG_LVL0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PM2_BCLBIG_LVL0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pm2BclbigLvl0({self.properties})"


class Pm2BclbigLvl1(AMLPackage):
    """Represents a PM2_BCLBIG_LVL1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PM2_BCLBIG_LVL1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pm2BclbigLvl1({self.properties})"


class Pm2BclbigLvl2(AMLPackage):
    """Represents a PM2_BCLBIG_LVL2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PM2_BCLBIG_LVL2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pm2BclbigLvl2({self.properties})"


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


class Pnp0A03(AMLPackage):
    """Represents a PNP0A03 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0A03")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0A03({self.properties})"


class Pnp0A05(AMLPackage):
    """Represents a PNP0A05 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0A05")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0A05({self.properties})"


class Pnp0A08(AMLPackage):
    """Represents a PNP0A08 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0A08")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0A08({self.properties})"


class Pnp0C0D(AMLPackage):
    """Represents a PNP0C0D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0C0D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0C0D({self.properties})"


class Pnp0Ca0(AMLPackage):
    """Represents a PNP0CA0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0CA0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0Ca0({self.properties})"


class Pnp0Ca1(AMLPackage):
    """Represents a PNP0CA1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0CA1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0Ca1({self.properties})"


class Pnp0Ca2(AMLPackage):
    """Represents a PNP0CA2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0CA2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0Ca2({self.properties})"


class Pnp0Ca3(AMLPackage):
    """Represents a PNP0CA3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0CA3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0Ca3({self.properties})"


class Pnp0D15(AMLPackage):
    """Represents a PNP0D15 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0D15")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0D15({self.properties})"


class Pnp0D80(AMLPackage):
    """Represents a PNP0D80 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PNP0D80")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pnp0D80({self.properties})"


class PppResourceIdBuckBoost1B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_BUCK_BOOST1_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_BUCK_BOOST1_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdBuckBoost1B({self.properties})"


class PppResourceIdBuckBoost2B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_BUCK_BOOST2_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_BUCK_BOOST2_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdBuckBoost2B({self.properties})"


class PppResourceIdClk3A(AMLPackage):
    """Represents a PPP_RESOURCE_ID_CLK3_A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_CLK3_A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdClk3A({self.properties})"


class PppResourceIdClk4A(AMLPackage):
    """Represents a PPP_RESOURCE_ID_CLK4_A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_CLK4_A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdClk4A({self.properties})"


class PppResourceIdClk5A(AMLPackage):
    """Represents a PPP_RESOURCE_ID_CLK5_A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_CLK5_A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdClk5A({self.properties})"


class PppResourceIdClk6A(AMLPackage):
    """Represents a PPP_RESOURCE_ID_CLK6_A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_CLK6_A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdClk6A({self.properties})"


class PppResourceIdClk7A(AMLPackage):
    """Represents a PPP_RESOURCE_ID_CLK7_A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_CLK7_A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdClk7A({self.properties})"


class PppResourceIdClk8A(AMLPackage):
    """Represents a PPP_RESOURCE_ID_CLK8_A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_CLK8_A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdClk8A({self.properties})"


class PppResourceIdLdo10B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO10_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO10_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo10B({self.properties})"


class PppResourceIdLdo12B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO12_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO12_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo12B({self.properties})"


class PppResourceIdLdo13B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO13_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO13_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo13B({self.properties})"


class PppResourceIdLdo14B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO14_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO14_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo14B({self.properties})"


class PppResourceIdLdo15B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO15_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO15_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo15B({self.properties})"


class PppResourceIdLdo16B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO16_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO16_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo16B({self.properties})"


class PppResourceIdLdo17B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO17_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO17_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo17B({self.properties})"


class PppResourceIdLdo1B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO1_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO1_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo1B({self.properties})"


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


class PppResourceIdLdo1E(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO1_E package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO1_E")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo1E({self.properties})"


class PppResourceIdLdo1F(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO1_F package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO1_F")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo1F({self.properties})"


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


class PppResourceIdLdo1M(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO1_M package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO1_M")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo1M({self.properties})"


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


class PppResourceIdLdo2E(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_E package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_E")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2E({self.properties})"


class PppResourceIdLdo2F(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_F package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_F")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2F({self.properties})"


class PppResourceIdLdo2I(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_I package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_I")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2I({self.properties})"


class PppResourceIdLdo2J(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_J package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_J")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2J({self.properties})"


class PppResourceIdLdo2M(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO2_M package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO2_M")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo2M({self.properties})"


class PppResourceIdLdo3C(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3C({self.properties})"


class PppResourceIdLdo3D(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3D({self.properties})"


class PppResourceIdLdo3E(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_E package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_E")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3E({self.properties})"


class PppResourceIdLdo3F(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_F package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_F")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3F({self.properties})"


class PppResourceIdLdo3I(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_I package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_I")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3I({self.properties})"


class PppResourceIdLdo3J(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_J package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_J")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3J({self.properties})"


class PppResourceIdLdo3M(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO3_M package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO3_M")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo3M({self.properties})"


class PppResourceIdLdo4B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO4_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO4_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo4B({self.properties})"


class PppResourceIdLdo4M(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO4_M package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO4_M")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo4M({self.properties})"


class PppResourceIdLdo5B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO5_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO5_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo5B({self.properties})"


class PppResourceIdLdo5M(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO5_M package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO5_M")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo5M({self.properties})"


class PppResourceIdLdo6B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO6_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO6_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo6B({self.properties})"


class PppResourceIdLdo6M(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO6_M package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO6_M")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo6M({self.properties})"


class PppResourceIdLdo7B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO7_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO7_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo7B({self.properties})"


class PppResourceIdLdo7M(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO7_M package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO7_M")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo7M({self.properties})"


class PppResourceIdLdo8B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO8_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO8_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo8B({self.properties})"


class PppResourceIdLdo9B(AMLPackage):
    """Represents a PPP_RESOURCE_ID_LDO9_B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_LDO9_B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdLdo9B({self.properties})"


class PppResourceIdSmps1D(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS1_D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS1_D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps1D({self.properties})"


class PppResourceIdSmps1E(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS1_E package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS1_E")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps1E({self.properties})"


class PppResourceIdSmps1F(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS1_F package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS1_F")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps1F({self.properties})"


class PppResourceIdSmps1G(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS1_G package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS1_G")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps1G({self.properties})"


class PppResourceIdSmps1I(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS1_I package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS1_I")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps1I({self.properties})"


class PppResourceIdSmps2I(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS2_I package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS2_I")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps2I({self.properties})"


class PppResourceIdSmps4C(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS4_C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS4_C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps4C({self.properties})"


class PppResourceIdSmps4I(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS4_I package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS4_I")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps4I({self.properties})"


class PppResourceIdSmps5J(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS5_J package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS5_J")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps5J({self.properties})"


class PppResourceIdSmps5K(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS5_K package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS5_K")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps5K({self.properties})"


class PppResourceIdSmps8D(AMLPackage):
    """Represents a PPP_RESOURCE_ID_SMPS8_D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PPP_RESOURCE_ID_SMPS8_D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PppResourceIdSmps8D({self.properties})"


class PreloadDstate(AMLPackage):
    """Represents a PRELOAD_DSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PRELOAD_DSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PreloadDstate({self.properties})"


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


class Ps8830(AMLPackage):
    """Represents a PS8830 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PS8830")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Ps8830({self.properties})"


class Pstate(AMLPackage):
    """Represents a PSTATE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PSTATE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Pstate({self.properties})"


class PstateAdjust(AMLPackage):
    """Represents a PSTATE_ADJUST package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PSTATE_ADJUST")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PstateAdjust({self.properties})"


class PstateSet(AMLPackage):
    """Represents a PSTATE_SET package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("PSTATE_SET")
        self.properties = kwargs
    
    def __repr__(self):
        return f"PstateSet({self.properties})"


class Qcom0427(AMLPackage):
    """Represents a QCOM0427 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0427")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0427({self.properties})"


class Qcom04B2(AMLPackage):
    """Represents a QCOM04B2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM04B2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom04B2({self.properties})"


class Qcom04Dd(AMLPackage):
    """Represents a QCOM04DD package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM04DD")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom04Dd({self.properties})"


class Qcom04De(AMLPackage):
    """Represents a QCOM04DE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM04DE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom04De({self.properties})"


class Qcom068F(AMLPackage):
    """Represents a QCOM068F package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM068F")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom068F({self.properties})"


class Qcom06C2(AMLPackage):
    """Represents a QCOM06C2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06C2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06C2({self.properties})"


class Qcom06D8(AMLPackage):
    """Represents a QCOM06D8 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06D8")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06D8({self.properties})"


class Qcom06Db(AMLPackage):
    """Represents a QCOM06DB package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06DB")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06Db({self.properties})"


class Qcom06Dc(AMLPackage):
    """Represents a QCOM06DC package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06DC")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06Dc({self.properties})"


class Qcom06Dd(AMLPackage):
    """Represents a QCOM06DD package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06DD")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06Dd({self.properties})"


class Qcom06De(AMLPackage):
    """Represents a QCOM06DE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06DE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06De({self.properties})"


class Qcom06Df(AMLPackage):
    """Represents a QCOM06DF package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06DF")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06Df({self.properties})"


class Qcom06E0(AMLPackage):
    """Represents a QCOM06E0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06E0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06E0({self.properties})"


class Qcom06E1(AMLPackage):
    """Represents a QCOM06E1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06E1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06E1({self.properties})"


class Qcom06E5(AMLPackage):
    """Represents a QCOM06E5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06E5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06E5({self.properties})"


class Qcom06E7(AMLPackage):
    """Represents a QCOM06E7 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM06E7")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom06E7({self.properties})"


class Qcom0C07(AMLPackage):
    """Represents a QCOM0C07 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C07")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C07({self.properties})"


class Qcom0C08(AMLPackage):
    """Represents a QCOM0C08 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C08")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C08({self.properties})"


class Qcom0C09(AMLPackage):
    """Represents a QCOM0C09 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C09")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C09({self.properties})"


class Qcom0C0A(AMLPackage):
    """Represents a QCOM0C0A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C0A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C0A({self.properties})"


class Qcom0C0B(AMLPackage):
    """Represents a QCOM0C0B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C0B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C0B({self.properties})"


class Qcom0C0C(AMLPackage):
    """Represents a QCOM0C0C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C0C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C0C({self.properties})"


class Qcom0C0D(AMLPackage):
    """Represents a QCOM0C0D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C0D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C0D({self.properties})"


class Qcom0C10(AMLPackage):
    """Represents a QCOM0C10 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C10")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C10({self.properties})"


class Qcom0C11(AMLPackage):
    """Represents a QCOM0C11 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C11")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C11({self.properties})"


class Qcom0C12(AMLPackage):
    """Represents a QCOM0C12 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C12")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C12({self.properties})"


class Qcom0C13(AMLPackage):
    """Represents a QCOM0C13 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C13")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C13({self.properties})"


class Qcom0C14(AMLPackage):
    """Represents a QCOM0C14 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C14")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C14({self.properties})"


class Qcom0C16(AMLPackage):
    """Represents a QCOM0C16 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C16")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C16({self.properties})"


class Qcom0C17(AMLPackage):
    """Represents a QCOM0C17 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C17")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C17({self.properties})"


class Qcom0C1B(AMLPackage):
    """Represents a QCOM0C1B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C1B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C1B({self.properties})"


class Qcom0C20(AMLPackage):
    """Represents a QCOM0C20 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C20")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C20({self.properties})"


class Qcom0C25(AMLPackage):
    """Represents a QCOM0C25 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C25")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C25({self.properties})"


class Qcom0C27(AMLPackage):
    """Represents a QCOM0C27 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C27")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C27({self.properties})"


class Qcom0C2A(AMLPackage):
    """Represents a QCOM0C2A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C2A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C2A({self.properties})"


class Qcom0C2B(AMLPackage):
    """Represents a QCOM0C2B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C2B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C2B({self.properties})"


class Qcom0C2C(AMLPackage):
    """Represents a QCOM0C2C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C2C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C2C({self.properties})"


class Qcom0C2D(AMLPackage):
    """Represents a QCOM0C2D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C2D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C2D({self.properties})"


class Qcom0C2F(AMLPackage):
    """Represents a QCOM0C2F package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C2F")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C2F({self.properties})"


class Qcom0C32(AMLPackage):
    """Represents a QCOM0C32 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C32")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C32({self.properties})"


class Qcom0C33(AMLPackage):
    """Represents a QCOM0C33 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C33")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C33({self.properties})"


class Qcom0C56(AMLPackage):
    """Represents a QCOM0C56 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C56")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C56({self.properties})"


class Qcom0C58(AMLPackage):
    """Represents a QCOM0C58 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C58")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C58({self.properties})"


class Qcom0C59(AMLPackage):
    """Represents a QCOM0C59 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C59")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C59({self.properties})"


class Qcom0C5A(AMLPackage):
    """Represents a QCOM0C5A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C5A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C5A({self.properties})"


class Qcom0C5C(AMLPackage):
    """Represents a QCOM0C5C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C5C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C5C({self.properties})"


class Qcom0C5E(AMLPackage):
    """Represents a QCOM0C5E package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C5E")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C5E({self.properties})"


class Qcom0C5F(AMLPackage):
    """Represents a QCOM0C5F package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C5F")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C5F({self.properties})"


class Qcom0C60(AMLPackage):
    """Represents a QCOM0C60 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C60")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C60({self.properties})"


class Qcom0C61(AMLPackage):
    """Represents a QCOM0C61 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C61")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C61({self.properties})"


class Qcom0C62(AMLPackage):
    """Represents a QCOM0C62 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C62")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C62({self.properties})"


class Qcom0C63(AMLPackage):
    """Represents a QCOM0C63 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C63")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C63({self.properties})"


class Qcom0C64(AMLPackage):
    """Represents a QCOM0C64 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C64")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C64({self.properties})"


class Qcom0C68(AMLPackage):
    """Represents a QCOM0C68 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C68")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C68({self.properties})"


class Qcom0C69(AMLPackage):
    """Represents a QCOM0C69 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C69")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C69({self.properties})"


class Qcom0C6B(AMLPackage):
    """Represents a QCOM0C6B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C6B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C6B({self.properties})"


class Qcom0C6D(AMLPackage):
    """Represents a QCOM0C6D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C6D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C6D({self.properties})"


class Qcom0C70(AMLPackage):
    """Represents a QCOM0C70 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C70")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C70({self.properties})"


class Qcom0C77(AMLPackage):
    """Represents a QCOM0C77 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C77")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C77({self.properties})"


class Qcom0C82(AMLPackage):
    """Represents a QCOM0C82 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C82")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C82({self.properties})"


class Qcom0C83(AMLPackage):
    """Represents a QCOM0C83 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C83")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C83({self.properties})"


class Qcom0C84(AMLPackage):
    """Represents a QCOM0C84 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C84")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C84({self.properties})"


class Qcom0C87(AMLPackage):
    """Represents a QCOM0C87 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C87")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C87({self.properties})"


class Qcom0C88(AMLPackage):
    """Represents a QCOM0C88 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C88")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C88({self.properties})"


class Qcom0C8B(AMLPackage):
    """Represents a QCOM0C8B package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C8B")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C8B({self.properties})"


class Qcom0C8C(AMLPackage):
    """Represents a QCOM0C8C package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C8C")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C8C({self.properties})"


class Qcom0C8D(AMLPackage):
    """Represents a QCOM0C8D package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C8D")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C8D({self.properties})"


class Qcom0C8E(AMLPackage):
    """Represents a QCOM0C8E package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C8E")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C8E({self.properties})"


class Qcom0C91(AMLPackage):
    """Represents a QCOM0C91 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C91")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C91({self.properties})"


class Qcom0C95(AMLPackage):
    """Represents a QCOM0C95 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C95")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C95({self.properties})"


class Qcom0C96(AMLPackage):
    """Represents a QCOM0C96 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C96")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C96({self.properties})"


class Qcom0C98(AMLPackage):
    """Represents a QCOM0C98 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0C98")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0C98({self.properties})"


class Qcom0Ca4(AMLPackage):
    """Represents a QCOM0CA4 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CA4")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Ca4({self.properties})"


class Qcom0Ca8(AMLPackage):
    """Represents a QCOM0CA8 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CA8")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Ca8({self.properties})"


class Qcom0Cac(AMLPackage):
    """Represents a QCOM0CAC package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CAC")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cac({self.properties})"


class Qcom0Cb0(AMLPackage):
    """Represents a QCOM0CB0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CB0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cb0({self.properties})"


class Qcom0Cbf(AMLPackage):
    """Represents a QCOM0CBF package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CBF")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cbf({self.properties})"


class Qcom0Cc3(AMLPackage):
    """Represents a QCOM0CC3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CC3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cc3({self.properties})"


class Qcom0Ccc(AMLPackage):
    """Represents a QCOM0CCC package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CCC")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Ccc({self.properties})"


class Qcom0Cd3(AMLPackage):
    """Represents a QCOM0CD3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CD3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cd3({self.properties})"


class Qcom0Cd5(AMLPackage):
    """Represents a QCOM0CD5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CD5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cd5({self.properties})"


class Qcom0Cda(AMLPackage):
    """Represents a QCOM0CDA package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CDA")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cda({self.properties})"


class Qcom0Ce4(AMLPackage):
    """Represents a QCOM0CE4 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CE4")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Ce4({self.properties})"


class Qcom0Cf1(AMLPackage):
    """Represents a QCOM0CF1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf1({self.properties})"


class Qcom0Cf2(AMLPackage):
    """Represents a QCOM0CF2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf2({self.properties})"


class Qcom0Cf3(AMLPackage):
    """Represents a QCOM0CF3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf3({self.properties})"


class Qcom0Cf4(AMLPackage):
    """Represents a QCOM0CF4 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF4")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf4({self.properties})"


class Qcom0Cf5(AMLPackage):
    """Represents a QCOM0CF5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf5({self.properties})"


class Qcom0Cf6(AMLPackage):
    """Represents a QCOM0CF6 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF6")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf6({self.properties})"


class Qcom0Cf7(AMLPackage):
    """Represents a QCOM0CF7 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF7")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf7({self.properties})"


class Qcom0Cf8(AMLPackage):
    """Represents a QCOM0CF8 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF8")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf8({self.properties})"


class Qcom0Cf9(AMLPackage):
    """Represents a QCOM0CF9 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CF9")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cf9({self.properties})"


class Qcom0Cfb(AMLPackage):
    """Represents a QCOM0CFB package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CFB")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cfb({self.properties})"


class Qcom0Cfc(AMLPackage):
    """Represents a QCOM0CFC package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0CFC")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0Cfc({self.properties})"


class Qcom0D01(AMLPackage):
    """Represents a QCOM0D01 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D01")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D01({self.properties})"


class Qcom0D04(AMLPackage):
    """Represents a QCOM0D04 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D04")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D04({self.properties})"


class Qcom0D06(AMLPackage):
    """Represents a QCOM0D06 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D06")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D06({self.properties})"


class Qcom0D07(AMLPackage):
    """Represents a QCOM0D07 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D07")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D07({self.properties})"


class Qcom0D08(AMLPackage):
    """Represents a QCOM0D08 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D08")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D08({self.properties})"


class Qcom0D09(AMLPackage):
    """Represents a QCOM0D09 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D09")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D09({self.properties})"


class Qcom0D0A(AMLPackage):
    """Represents a QCOM0D0A package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D0A")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D0A({self.properties})"


class Qcom0D14(AMLPackage):
    """Represents a QCOM0D14 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D14")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D14({self.properties})"


class Qcom0D17(AMLPackage):
    """Represents a QCOM0D17 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D17")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D17({self.properties})"


class Qcom0D18(AMLPackage):
    """Represents a QCOM0D18 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM0D18")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom0D18({self.properties})"


class Qcom24A5(AMLPackage):
    """Represents a QCOM24A5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM24A5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcom24A5({self.properties})"


class Qcomffe0(AMLPackage):
    """Represents a QCOMFFE0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFE0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffe0({self.properties})"


class Qcomffe1(AMLPackage):
    """Represents a QCOMFFE1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFE1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffe1({self.properties})"


class Qcomffe2(AMLPackage):
    """Represents a QCOMFFE2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFE2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffe2({self.properties})"


class Qcomffe3(AMLPackage):
    """Represents a QCOMFFE3 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFE3")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffe3({self.properties})"


class Qcomffe4(AMLPackage):
    """Represents a QCOMFFE4 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFE4")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffe4({self.properties})"


class Qcomffe5(AMLPackage):
    """Represents a QCOMFFE5 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFE5")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffe5({self.properties})"


class Qcomffe9(AMLPackage):
    """Represents a QCOMFFE9 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFE9")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffe9({self.properties})"


class Qcomffea(AMLPackage):
    """Represents a QCOMFFEA package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFEA")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffea({self.properties})"


class Qcomffeb(AMLPackage):
    """Represents a QCOMFFEB package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFEB")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffeb({self.properties})"


class Qcomffec(AMLPackage):
    """Represents a QCOMFFEC package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOMFFEC")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qcomffec({self.properties})"


class QcomAvstream(AMLPackage):
    """Represents a QCOM_AVSTREAM package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QCOM_AVSTREAM")
        self.properties = kwargs
    
    def __repr__(self):
        return f"QcomAvstream({self.properties})"


class Qup0Se0(AMLPackage):
    """Represents a QUP_0_SE_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QUP_0_SE_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qup0Se0({self.properties})"


class Qup0Se4(AMLPackage):
    """Represents a QUP_0_SE_4 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QUP_0_SE_4")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qup0Se4({self.properties})"


class Qup1Se0(AMLPackage):
    """Represents a QUP_1_SE_0 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QUP_1_SE_0")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qup1Se0({self.properties})"


class Qup1Se1(AMLPackage):
    """Represents a QUP_1_SE_1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("QUP_1_SE_1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Qup1Se1({self.properties})"


class Required(AMLPackage):
    """Represents a REQUIRED package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("REQUIRED")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Required({self.properties})"


class Resource(AMLPackage):
    """Represents a RESOURCE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("RESOURCE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Resource({self.properties})"


class RpmhCommit(AMLPackage):
    """Represents a RPMH_COMMIT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("RPMH_COMMIT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"RpmhCommit({self.properties})"


class ScpPurwa(AMLPackage):
    """Represents a SCP_PURWA package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("SCP_PURWA")
        self.properties = kwargs
    
    def __repr__(self):
        return f"ScpPurwa({self.properties})"


class Smo55F1(AMLPackage):
    """Represents a SMO55F1 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("SMO55F1")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Smo55F1({self.properties})"


class Suppressible(AMLPackage):
    """Represents a SUPPRESSIBLE package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("SUPPRESSIBLE")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Suppressible({self.properties})"


class Tlmmgpio(AMLPackage):
    """Represents a TLMMGPIO package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("TLMMGPIO")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Tlmmgpio({self.properties})"


class Tlmmport(AMLPackage):
    """Represents a TLMMPORT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("TLMMPORT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Tlmmport({self.properties})"


class Unknown(AMLPackage):
    """Represents a UNKNOWN package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("UNKNOWN")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Unknown({self.properties})"


class Upper(AMLPackage):
    """Represents a UPPER package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("UPPER")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Upper({self.properties})"


class Usb4Hr0DpAp0Interrupt(AMLPackage):
    """Represents a USB4_HR_0_DP_AP_0_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("USB4_HR_0_DP_AP_0_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Usb4Hr0DpAp0Interrupt({self.properties})"


class Usb4Hr0DpAp1Interrupt(AMLPackage):
    """Represents a USB4_HR_0_DP_AP_1_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("USB4_HR_0_DP_AP_1_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Usb4Hr0DpAp1Interrupt({self.properties})"


class Usb4Hr1DpAp0Interrupt(AMLPackage):
    """Represents a USB4_HR_1_DP_AP_0_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("USB4_HR_1_DP_AP_0_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Usb4Hr1DpAp0Interrupt({self.properties})"


class Usb4Hr1DpAp1Interrupt(AMLPackage):
    """Represents a USB4_HR_1_DP_AP_1_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("USB4_HR_1_DP_AP_1_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Usb4Hr1DpAp1Interrupt({self.properties})"


class Usb4Hr2DpAp0Interrupt(AMLPackage):
    """Represents a USB4_HR_2_DP_AP_0_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("USB4_HR_2_DP_AP_0_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Usb4Hr2DpAp0Interrupt({self.properties})"


class Usb4Hr2DpAp1Interrupt(AMLPackage):
    """Represents a USB4_HR_2_DP_AP_1_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("USB4_HR_2_DP_AP_1_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Usb4Hr2DpAp1Interrupt({self.properties})"


class Usbc000(AMLPackage):
    """Represents a USBC000 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("USBC000")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Usbc000({self.properties})"


class VidcInterrupt(AMLPackage):
    """Represents a VIDC_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("VIDC_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"VidcInterrupt({self.properties})"


class Video(AMLPackage):
    """Represents a VIDEO package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("VIDEO")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Video({self.properties})"


class Video2(AMLPackage):
    """Represents a VIDEO2 package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("VIDEO2")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Video2({self.properties})"


class Video2Interrupt(AMLPackage):
    """Represents a VIDEO2_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("VIDEO2_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Video2Interrupt({self.properties})"


class Video2Regs(AMLPackage):
    """Represents a VIDEO2_REGS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("VIDEO2_REGS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Video2Regs({self.properties})"


class VideoRegs(AMLPackage):
    """Represents a VIDEO_REGS package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("VIDEO_REGS")
        self.properties = kwargs
    
    def __repr__(self):
        return f"VideoRegs({self.properties})"


class VsyncInterrupt(AMLPackage):
    """Represents a VSYNC_INTERRUPT package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("VSYNC_INTERRUPT")
        self.properties = kwargs
    
    def __repr__(self):
        return f"VsyncInterrupt({self.properties})"


class Xmil(AMLPackage):
    """Represents a XMIL package in AML."""
    
    def __init__(self, **kwargs):
        super().__init__("XMIL")
        self.properties = kwargs
    
    def __repr__(self):
        return f"Xmil({self.properties})"


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
