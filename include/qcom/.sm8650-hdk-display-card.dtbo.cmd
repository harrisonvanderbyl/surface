savedcmd_arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtbo := gcc -E -Wp,-MMD,arch/arm64/boot/dts/qcom/.sm8650-hdk-display-card.dtbo.d.pre.tmp -nostdinc -I ./scripts/dtc/include-prefixes -undef -D__DTS__ -x assembler-with-cpp -o arch/arm64/boot/dts/qcom/.sm8650-hdk-display-card.dtbo.dts.tmp arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtso ; ./scripts/dtc/dtc -o arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtbo -b 0 -iarch/arm64/boot/dts/qcom/ -i./scripts/dtc/include-prefixes -Wno-unique_unit_address -Wno-unit_address_vs_reg -Wno-avoid_unnecessary_addr_size -Wno-alias_paths -Wno-graph_child_address -Wno-simple_bus_reg   -d arch/arm64/boot/dts/qcom/.sm8650-hdk-display-card.dtbo.d.dtc.tmp arch/arm64/boot/dts/qcom/.sm8650-hdk-display-card.dtbo.dts.tmp ; cat arch/arm64/boot/dts/qcom/.sm8650-hdk-display-card.dtbo.d.pre.tmp arch/arm64/boot/dts/qcom/.sm8650-hdk-display-card.dtbo.d.dtc.tmp > arch/arm64/boot/dts/qcom/.sm8650-hdk-display-card.dtbo.d 

source_arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtbo := arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtso

deps_arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtbo := \
  scripts/dtc/include-prefixes/dt-bindings/gpio/gpio.h \
  scripts/dtc/include-prefixes/dt-bindings/interrupt-controller/irq.h \

arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtbo: $(deps_arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtbo)

$(deps_arch/arm64/boot/dts/qcom/sm8650-hdk-display-card.dtbo):
