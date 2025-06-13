import os
import random
import time

interface = "eth0"  # shyiramo interface yawe

while True:
    new_ip = f"192.168.1.{random.randint(1, 254)}"
    cmd = f"sudo ifconfig {interface} {new_ip} netmask 255.255.255.0 up"
    os.system(cmd)
    print(f"Local IP are changed: {new_ip}")
    time.sleep(1)
