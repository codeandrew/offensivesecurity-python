import psutil
import socket
"""
pip install psutil
python3.11
"""

def get_ipv4_addresses():
    addrs = {}
    for interface, addresses in psutil.net_if_addrs().items():
        for addr in addresses:
            if addr.family == socket.AF_INET:
                addrs[interface] = addr.address
    return addrs
    
"""
get_ipv4_addresses()
{'lo0': '127.0.0.1', 'en0': '192.168.100.27'}
"""

if __name__ == '__main__':
    print(get_ipv4_addresses())
