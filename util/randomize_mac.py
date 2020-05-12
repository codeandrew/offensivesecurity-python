import string
import random

characters = string.ascii_lowercase + string.digits

def randomize(char):
    return random.choice(list(char))

mac_raw = []

for i in range(6):
    if len(mac_raw) is not 0:
        mac_raw.append(":")
    for ii in range(2):
        mac_raw.append(randomize(characters))

mac_address = "".join(mac_raw)

print(mac_address)
