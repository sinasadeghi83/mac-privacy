import random
import time

def generate_mac():
    seed = int(time.time()/10)
    random.seed(seed)
    # Generate a MAC address with locally administered address bit set
    mac = [random.randint(0x00, 0xFF) & (~3),
           random.randint(0x00, 0x7F), 
           random.randint(0x00, 0xFF), 
           random.randint(0x00, 0xFF), 
           random.randint(0x00, 0xFF), 
           random.randint(0x00, 0xFF)]
    return ':'.join(f"{octet:02x}" for octet in mac)

print(generate_mac())
