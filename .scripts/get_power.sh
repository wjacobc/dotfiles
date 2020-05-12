percent=$(cat /sys/class/power_supply/BAT0/capacity)
charging=$(cat /sys/class/power_supply/BAT0/status)

if [ "$percent" = "100" ]; then
    echo   100%
    exit 0
fi
if [ "$charging" = "Charging" ]; then
    charging_icon=
fi

case $percent in
    [9]*)
        icon=
        ;;
    [7-8]*)
        icon=
        ;;
    [4-6]*)
        icon=
        ;;
    [1-3]*)
        icon=
        ;;
    *)
        icon=
        ;;
esac

echo $charging_icon $icon $percent%
