savedcmd_arch/arm64/boot/dts/qcom/qcm6490-idp.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.qcm6490-idp.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.qcm6490-idp.dtb.dts.tmp arch/arm64/boot/dts/qcom/qcm6490-idp.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/qcm6490-idp.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.qcm6490-idp.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.qcm6490-idp.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.qcm6490-idp.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.qcm6490-idp.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.qcm6490-idp.dtb.d 

source_arch/arm64/boot/dts/qcom/qcm6490-idp.dtb := arch/arm64/boot/dts/qcom/qcm6490-idp.dts

deps_arch/arm64/boot/dts/qcom/qcm6490-idp.dtb := \
  scripts/dtc/include-prefixes/dt-bindings/input/linux-event-codes.h \
  scripts/dtc/include-prefixes/dt-bindings/leds/common.h \
  scripts/dtc/include-prefixes/dt-bindings/pinctrl/qcom,pmic-gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/regulator/qcom,rpmh-regulator.h \
  arch/arm64/boot/dts/qcom/sc7280.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,camcc-sc7280.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dispcc-sc7280.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dsi-phy-28nm.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gcc-sc7280.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gpucc-sc7280.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,lpassaudiocc-sc7280.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,lpasscorecc-sc7280.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,videocc-sc7280.h \
  scripts/dtc/include-prefixes/dt-bindings/dma/qcom-gpi.h \
  scripts/dtc/include-prefixes/dt-bindings/firmware/qcom,scm.h \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,icc.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,osm-l3.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,sc7280.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/mailbox/qcom-ipcc.h \
  scripts/dtc/include-prefixes/dt-bindings/phy/phy-qcom-qmp.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  scripts/dtc/include-prefixes/dt-bindings/reset/qcom,sdm845-aoss.h \
  scripts/dtc/include-prefixes/dt-bindings/reset/qcom,sdm845-pdc.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,apr.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,rpmh-rsc.h \
  scripts/dtc/include-prefixes/dt-bindings/sound/qcom,lpass.h \
  scripts/dtc/include-prefixes/dt-bindings/sound/qcom,q6asm.h \
  scripts/dtc/include-prefixes/dt-bindings/thermal/thermal.h \
  arch/arm64/boot/dts/qcom/pm7250b.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/iio/qcom,spmi-vadc.h \
  scripts/dtc/include-prefixes/dt-bindings/spmi/spmi.h \
  arch/arm64/boot/dts/qcom/pm7325.dtsi \
  arch/arm64/boot/dts/qcom/pm8350c.dtsi \
  arch/arm64/boot/dts/qcom/pmk8350.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/input/input.h \

arch/arm64/boot/dts/qcom/qcm6490-idp.dtb: $(deps_arch/arm64/boot/dts/qcom/qcm6490-idp.dtb)

$(deps_arch/arm64/boot/dts/qcom/qcm6490-idp.dtb):
