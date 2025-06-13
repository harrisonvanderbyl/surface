mkdir ./build/
# cpp -nostdinc -undef -x assembler-with-cpp -E ./vivo.dts -I./files > ./build/vivo.dts
# dtc -I dts -O dtb ./build/vivo.dts -o ./build/vivo.dtb
cpp -nostdinc -undef -x assembler-with-cpp -E ./surface.dts -I./files > ./build/surface.dts
dtc -I dts -O dtb ./build/surface.dts -o ./build/surface.dtb