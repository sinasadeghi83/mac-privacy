import os
import subprocess

def remove_set_mac():
    try:
        subprocess.run(["sudo", "rm", "/etc/NetworkManager/dispatcher.d/99-set-mac.sh"], check=True)
        subprocess.run(["sudo", "rm", "/usr/local/bin/generate_mac.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating service set-mac: {e}")

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
else:
    remove_set_mac()
