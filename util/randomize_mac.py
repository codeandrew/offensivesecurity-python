import string
import random

characters = string.ascii_lowercase + string.digits

def randomize(char):
    return random.choice(list(char))

def get_mac_address(characters=characters, mac_raw=[]):
    for i in range(6):
        if len(mac_raw) is not 0:
            mac_raw.append(":")
        for ii in range(2):
            mac_raw.append(randomize(characters))

    return "".join(mac_raw)

if __name__ == '__main__':
    mac_address = get_mac_address(characters)
    print(mac_address)

