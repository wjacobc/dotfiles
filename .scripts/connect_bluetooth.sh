devices=$(echo "power on \n paired-devices \n exit" | bluetoothctl | sed -n '/Agent registered/,$p' | grep Device)
name=$(echo $devices | cut -f 3- -d " " | dmenu -p "Choose a device to connect to" -fn "Hack:pixelsize=27")
choice=$(echo $devices | grep "$name" | awk '{print $2}')
echo "connect $choice \n exit" | bluetoothctl | grep "connect to"
echo "exit" | bluetoothctl | cut -f 1 -d " " | grep "#" | tail -n 1


