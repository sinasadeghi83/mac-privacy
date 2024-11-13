import os
import subprocess

def create_set_mac(interface):
    dispatcher = ["#!/bin/bash", f"interface={interface}"]
    with open("/etc/NetworkManager/dispatcher.d/99-set-mac.sh", 'w') as f:
        for line in dispatcher:
            f.write(f"{line}\n")
        with open("./99-set-mac.sh", 'r') as r:
            f.write(r.read())
    try:
        subprocess.run(["sudo", "cp", "./generate_mac.py", "/usr/local/bin/"], check=True)
        subprocess.run(["sudo", "chmod", "+x", "/etc/NetworkManager/dispatcher.d/99-set-mac.sh"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating service set-mac: {e}")

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
else:
    # Replace 'wlan0' with your actual network interface name
    interface_name = input("Enter your interface name:")  
    create_set_mac(interface_name)
