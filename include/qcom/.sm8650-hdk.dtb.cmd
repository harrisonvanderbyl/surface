savedcmd_arch/arm64/boot/dts/qcom/sm8650-hdk.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.sm8650-hdk.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.sm8650-hdk.dtb.dts.tmp arch/arm64/boot/dts/qcom/sm8650-hdk.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/sm8650-hdk.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -@ -d arch/arm64/boot/dts/qcom/.sm8650-hdk.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.sm8650-hdk.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.sm8650-hdk.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.sm8650-hdk.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.sm8650-hdk.dtb.d 

source_arch/arm64/boot/dts/qcom/sm8650-hdk.dtb := arch/arm64/boot/dts/qcom/sm8650-hdk.dts

deps_arch/arm64/boot/dts/qcom/sm8650-hdk.dtb := \
  scripts/dtc/include-prefixes/dt-bindings/leds/common.h \
  scripts/dtc/include-prefixes/dt-bindings/regulator/qcom,rpmh-regulator.h \
  arch/arm64/boot/dts/qcom/sm8650.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dsi-phy-28nm.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sm8650-camcc.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sm8650-dispcc.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sm8650-gcc.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sm8650-gpucc.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sm8650-tcsr.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sm8650-videocc.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sm8450-videocc.h \
  scripts/dtc/include-prefixes/dt-bindings/dma/qcom-gpi.h \
  scripts/dtc/include-prefixes/dt-bindings/firmware/qcom,scm.h \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,icc.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,sm8650-rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,osm-l3.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/mailbox/qcom-ipcc.h \
  scripts/dtc/include-prefixes/dt-bindings/phy/phy-qcom-qmp.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom,rpmhpd.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  scripts/dtc/include-prefixes/dt-bindings/reset/qcom,sm8650-gpucc.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,gpr.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,rpmh-rsc.h \
  scripts/dtc/include-prefixes/dt-bindings/sound/qcom,q6dsp-lpass-ports.h \
  scripts/dtc/include-prefixes/dt-bindings/thermal/thermal.h \
  arch/arm64/boot/dts/qcom/pm8010.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/spmi/spmi.h \
  arch/arm64/boot/dts/qcom/pm8550.dtsi \
  arch/arm64/boot/dts/qcom/pm8550b.dtsi \
  arch/arm64/boot/dts/qcom/pm8550ve.dtsi \
  arch/arm64/boot/dts/qcom/pm8550vs.dtsi \
  arch/arm64/boot/dts/qcom/pmk8550.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/input/input.h \
  scripts/dtc/include-prefixes/dt-bindings/input/linux-event-codes.h \

arch/arm64/boot/dts/qcom/sm8650-hdk.dtb: $(deps_arch/arm64/boot/dts/qcom/sm8650-hdk.dtb)

$(deps_arch/arm64/boot/dts/qcom/sm8650-hdk.dtb):
