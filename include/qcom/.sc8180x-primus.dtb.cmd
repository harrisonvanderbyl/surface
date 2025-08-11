savedcmd_arch/arm64/boot/dts/qcom/sc8180x-primus.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.sc8180x-primus.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.sc8180x-primus.dtb.dts.tmp arch/arm64/boot/dts/qcom/sc8180x-primus.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/sc8180x-primus.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.sc8180x-primus.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.sc8180x-primus.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.sc8180x-primus.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.sc8180x-primus.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.sc8180x-primus.dtb.d 

source_arch/arm64/boot/dts/qcom/sc8180x-primus.dtb := arch/arm64/boot/dts/qcom/sc8180x-primus.dts

deps_arch/arm64/boot/dts/qcom/sc8180x-primus.dtb := \
  scripts/dtc/include-prefixes/dt-bindings/firmware/qcom,scm.h \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/input/gpio-keys.h \
  scripts/dtc/include-prefixes/dt-bindings/input/input.h \
  scripts/dtc/include-prefixes/dt-bindings/input/linux-event-codes.h \
  scripts/dtc/include-prefixes/dt-bindings/regulator/qcom,rpmh-regulator.h \
  arch/arm64/boot/dts/qcom/sc8180x.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dispcc-sm8250.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dsi-phy-28nm.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gcc-sc8180x.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gpucc-sm8150.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,icc.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,osm-l3.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,sc8180x.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/phy/phy-qcom-qmp.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,rpmh-rsc.h \
  scripts/dtc/include-prefixes/dt-bindings/thermal/thermal.h \
  arch/arm64/boot/dts/qcom/sc8180x-pmics.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/spmi/spmi.h \
  scripts/dtc/include-prefixes/dt-bindings/iio/qcom,spmi-vadc.h \

arch/arm64/boot/dts/qcom/sc8180x-primus.dtb: $(deps_arch/arm64/boot/dts/qcom/sc8180x-primus.dtb)

$(deps_arch/arm64/boot/dts/qcom/sc8180x-primus.dtb):
