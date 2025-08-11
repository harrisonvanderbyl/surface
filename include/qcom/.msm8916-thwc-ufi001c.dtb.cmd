savedcmd_arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.msm8916-thwc-ufi001c.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.msm8916-thwc-ufi001c.dtb.dts.tmp arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.msm8916-thwc-ufi001c.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.msm8916-thwc-ufi001c.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.msm8916-thwc-ufi001c.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.msm8916-thwc-ufi001c.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.msm8916-thwc-ufi001c.dtb.d 

source_arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dtb := arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dts

deps_arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dtb := \
  arch/arm64/boot/dts/qcom/msm8916-ufi.dtsi \
  arch/arm64/boot/dts/qcom/msm8916-pm8916.dtsi \
  arch/arm64/boot/dts/qcom/msm8916.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/arm/coresight-cti-dt.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dsi-phy-28nm.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gcc-msm8916.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmcc.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,msm8916.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  scripts/dtc/include-prefixes/dt-bindings/reset/qcom,gcc-msm8916.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,apr.h \
  scripts/dtc/include-prefixes/dt-bindings/thermal/thermal.h \
  arch/arm64/boot/dts/qcom/pm8916.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/iio/qcom,spmi-vadc.h \
  scripts/dtc/include-prefixes/dt-bindings/input/linux-event-codes.h \
  scripts/dtc/include-prefixes/dt-bindings/spmi/spmi.h \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/leds/common.h \

arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dtb: $(deps_arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dtb)

$(deps_arch/arm64/boot/dts/qcom/msm8916-thwc-ufi001c.dtb):
