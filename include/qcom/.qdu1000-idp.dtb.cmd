savedcmd_arch/arm64/boot/dts/qcom/qdu1000-idp.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.qdu1000-idp.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.qdu1000-idp.dtb.dts.tmp arch/arm64/boot/dts/qcom/qdu1000-idp.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/qdu1000-idp.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.qdu1000-idp.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.qdu1000-idp.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.qdu1000-idp.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.qdu1000-idp.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.qdu1000-idp.dtb.d 

source_arch/arm64/boot/dts/qcom/qdu1000-idp.dtb := arch/arm64/boot/dts/qcom/qdu1000-idp.dts

deps_arch/arm64/boot/dts/qcom/qdu1000-idp.dtb := \
  scripts/dtc/include-prefixes/dt-bindings/regulator/qcom,rpmh-regulator.h \
  arch/arm64/boot/dts/qcom/qdu1000.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,qdu1000-gcc.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/dma/qcom-gpi.h \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,icc.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,qdu1000-rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,rpmh-rsc.h \
  arch/arm64/boot/dts/qcom/pm8150.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/input/input.h \
  scripts/dtc/include-prefixes/dt-bindings/input/linux-event-codes.h \
  scripts/dtc/include-prefixes/dt-bindings/spmi/spmi.h \
  scripts/dtc/include-prefixes/dt-bindings/iio/qcom,spmi-vadc.h \

arch/arm64/boot/dts/qcom/qdu1000-idp.dtb: $(deps_arch/arm64/boot/dts/qcom/qdu1000-idp.dtb)

$(deps_arch/arm64/boot/dts/qcom/qdu1000-idp.dtb):
