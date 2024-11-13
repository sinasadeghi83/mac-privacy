new_mac=$(python3 /usr/local/bin/generate_mac.py)  # Run Python script to get the new MAC address

# Get the current MAC address of the interface
current_mac=$(cat /sys/class/net/$interface/address)

# Only change the MAC if it's different from the desired MAC
if [[ "$1" == "$interface" && "$2" == "up" && "$current_mac" != "$new_mac" ]]; then
    ip link set $interface down
    ip link set $interface address $new_mac
    ip link set $interface up
    echo "MAC address changed to $new_mac"
else
    echo "MAC address is already set to $new_mac"
fi
