mkdir ./build/
# cpp -nostdinc -undef -x assembler-with-cpp -E ./vivo.dts -I./files > ./build/vivo.dts
# dtc -I dts -O dtb ./build/vivo.dts -o ./build/vivo.dtb
rm ./build/surface.dts
cpp -nostdinc -undef -x assembler-with-cpp -E ./sp12.dts -I./dts -I./dt_includes -I./include > ./build/surface.dts
rm ./build/x1e80100-microsoft-denali.dtb
dtc -I dts -O dtb ./build/surface.dts -o ./build/x1e80100-microsoft-denali.dtb
# if no output, then the dtc command failed
if [ ! -f ./build/x1e80100-microsoft-denali.dtb ];
then
    echo "Error: dtc command failed, no output file created."
    exit 1
fi
sudo cp ./build/x1e80100-microsoft-denali.dtb /boot/dtbs/6.16.0-rc6/qcom/x1p42100-lenovo-ideapad-5-2in1.dtb
sudo rm /var/log/journal/fa46730e33564e71aa0bc4196801cd6f/*
# rm ./build/surface.dts
# flush usb drive
sync
# unmount usb drive
# sudo umount /run/media/harrison/root2410
# echo "Build complete. Output file