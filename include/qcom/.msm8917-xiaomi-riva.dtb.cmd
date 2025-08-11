savedcmd_arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.msm8917-xiaomi-riva.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.msm8917-xiaomi-riva.dtb.dts.tmp arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.msm8917-xiaomi-riva.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.msm8917-xiaomi-riva.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.msm8917-xiaomi-riva.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.msm8917-xiaomi-riva.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.msm8917-xiaomi-riva.dtb.d 

source_arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dtb := arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dts

deps_arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dtb := \
  scripts/dtc/include-prefixes/dt-bindings/arm/qcom,ids.h \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  arch/arm64/boot/dts/qcom/msm8917.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dsi-phy-28nm.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gcc-msm8917.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmcc.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  scripts/dtc/include-prefixes/dt-bindings/thermal/thermal.h \
  arch/arm64/boot/dts/qcom/pm8937.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/iio/qcom,spmi-vadc.h \
  scripts/dtc/include-prefixes/dt-bindings/input/linux-event-codes.h \
  scripts/dtc/include-prefixes/dt-bindings/spmi/spmi.h \

arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dtb: $(deps_arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dtb)

$(deps_arch/arm64/boot/dts/qcom/msm8917-xiaomi-riva.dtb):
