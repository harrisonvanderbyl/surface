savedcmd_arch/arm64/boot/dts/qcom/msm8996-mtp.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.msm8996-mtp.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.msm8996-mtp.dtb.dts.tmp arch/arm64/boot/dts/qcom/msm8996-mtp.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/msm8996-mtp.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.msm8996-mtp.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.msm8996-mtp.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.msm8996-mtp.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.msm8996-mtp.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.msm8996-mtp.dtb.d 

source_arch/arm64/boot/dts/qcom/msm8996-mtp.dtb := arch/arm64/boot/dts/qcom/msm8996-mtp.dts

deps_arch/arm64/boot/dts/qcom/msm8996-mtp.dtb := \
  arch/arm64/boot/dts/qcom/msm8996.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,dsi-phy-28nm.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,gcc-msm8996.h \
    $(wildcard include/config/NOC_CLK_SRC) \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,mmcc-msm8996.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmcc.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,msm8996.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,msm8996-cbf.h \
  scripts/dtc/include-prefixes/dt-bindings/firmware/qcom,scm.h \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,apr.h \
  scripts/dtc/include-prefixes/dt-bindings/thermal/thermal.h \

arch/arm64/boot/dts/qcom/msm8996-mtp.dtb: $(deps_arch/arm64/boot/dts/qcom/msm8996-mtp.dtb)

$(deps_arch/arm64/boot/dts/qcom/msm8996-mtp.dtb):
