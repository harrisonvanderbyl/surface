savedcmd_arch/arm64/boot/dts/qcom/qcs9100-ride.dtb := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.qcs9100-ride.dtb.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.qcs9100-ride.dtb.dts.tmp arch/arm64/boot/dts/qcom/qcs9100-ride.dts ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/qcs9100-ride.dtb -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.qcs9100-ride.dtb.d.dtc.tmp arch/arm64/boot/dts/qcom/.qcs9100-ride.dtb.dts.tmp ; cat arch/arm64/boot/dts/qcom/.qcs9100-ride.dtb.d.pre.tmp arch/arm64/boot/dts/qcom/.qcs9100-ride.dtb.d.dtc.tmp > arch/arm64/boot/dts/qcom/.qcs9100-ride.dtb.d 

source_arch/arm64/boot/dts/qcom/qcs9100-ride.dtb := arch/arm64/boot/dts/qcom/qcs9100-ride.dts

deps_arch/arm64/boot/dts/qcom/qcs9100-ride.dtb := \
  arch/arm64/boot/dts/qcom/sa8775p-ride.dts \
  arch/arm64/boot/dts/qcom/sa8775p-ride.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/regulator/qcom,rpmh-regulator.h \
  arch/arm64/boot/dts/qcom/sa8775p.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,icc.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/arm-gic.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sa8775p-dispcc.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sa8775p-gcc.h \
  scripts/dtc/include-prefixes/dt-bindings/clock/qcom,sa8775p-gpucc.h \
  scripts/dtc/include-prefixes/dt-bindings/dma/qcom-gpi.h \
  scripts/dtc/include-prefixes/dt-bindings/interconnect/qcom,sa8775p-rpmh.h \
  scripts/dtc/include-prefixes/dt-bindings/mailbox/qcom-ipcc.h \
  scripts/dtc/include-prefixes/dt-bindings/firmware/qcom,scm.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom,rpmhpd.h \
  scripts/dtc/include-prefixes/dt-bindings/power/qcom-rpmpd.h \
  scripts/dtc/include-prefixes/dt-bindings/soc/qcom,rpmh-rsc.h \
  arch/arm64/boot/dts/qcom/sa8775p-pmics.dtsi \
  scripts/dtc/include-prefixes/dt-bindings/input/input.h \
  scripts/dtc/include-prefixes/dt-bindings/input/linux-event-codes.h \
  scripts/dtc/include-prefixes/dt-bindings/spmi/spmi.h \

arch/arm64/boot/dts/qcom/qcs9100-ride.dtb: $(deps_arch/arm64/boot/dts/qcom/qcs9100-ride.dtb)

$(deps_arch/arm64/boot/dts/qcom/qcs9100-ride.dtb):
