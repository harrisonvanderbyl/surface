savedcmd_arch/arm64/boot/dts/qcom/sdm670-google-sargo.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.sdm670-google-sargo.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.sdm670-google-sargo.dtb.dts.tmp arch/arm64/boot/dts/qcom/sdm670-google-sargo.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/sdm670-google-sargo.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.sdm670-google-sargo.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.sdm670-google-sargo.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.sdm670-google-sargo.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.sdm670-google-sargo.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.sdm670-google-sargo.dtb.d 

source_arch/arm64/boot/dts/qcom/sdm670-google-sargo.dtb := arch/arm64/boot/dts/qcom/sdm670-google-sargo.dts

deps_arch/arm64/boot/dts/qcom/sdm670-google-sargo.dtb := \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/input/input.h \
  scripts/dtc/include-prefixes/dt-bindings/input/linux-event-codes.h \
  scripts/dtc/include-prefixes/dt-bindings/leds/common.h \
  scripts/dtc/include-prefixes/dt-bindings/pinctrl/qcom,pmic-gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  arch/arm64/boot/dts/qcom/sdm670.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,camcc-sdm845.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dispcc-sdm845.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dsi-phy-28nm.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gcc-sdm845.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gpucc-sdm845.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/dma/qcom-gpi.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,osm-l3.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,sdm670-rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/phy/phy-qcom-qusb2.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,rpmh-rsc.h \
  arch/arm64/boot/dts/qcom/pm660.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/iio/qcom,spmi-vadc.h \
  scripts/dtc/include-prefixes/dt-bindings/spmi/spmi.h \
  scripts/dtc/include-prefixes/dt-bindings/thermal/thermal.h \
  arch/arm64/boot/dts/qcom/pm660l.dtsi \

arch/arm64/boot/dts/qcom/sdm670-google-sargo.dtb: $(deps_arch/arm64/boot/dts/qcom/sdm670-google-sargo.dtb)

$(deps_arch/arm64/boot/dts/qcom/sdm670-google-sargo.dtb):
