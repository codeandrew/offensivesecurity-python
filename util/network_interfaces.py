import netifaces

def get_interfaces_with_ipv4():
    """
    Returns a dictionary containing the names and IPv4 addresses of all the network interfaces.
    """
    interfaces = {}
    for iface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            ipv4_addr = addrs[netifaces.AF_INET][0]['addr']
            interfaces[iface] = ipv4_addr
    return interfaces
"""
Tested on Ubuntu
>>> get_interfaces_with_ipv4()
{'lo': '127.0.0.1', 'eth0': '111.111.1111.111', 'eth1': '10.104.0.2', 'docker0': '172.17.0.1', 'br-a5fec66624dd': '172.24.0.1', 'br-2b3ebff17e3b': '192.168.16.1', 'br-6539607c7ed5': '172.21.0.1'}
"""



# import socket

# def get_ipv4_addresses():
#     ip_addresses = []
#     for interface in socket.if_nameindex():
#         interface_name = interface[1]
#         addresses = socket.getaddrinfo(interface_name, None)
#         for address in addresses:
#             if address[0] == socket.AF_INET:
#                 ip_address = address[4][0]
#                 ip_addresses.append((interface_name, ip_address))
#     return ip_addresses

# if __name__ == '__main__':
#     print(get_ipv4_addresses())


# import socket

# def get_ipv4_addresses(interface_name):
#     # Get all address info for the specified interface name
#     addresses = socket.getaddrinfo(interface_name, None)
    
#     # Filter for IPv4 addresses only
#     ipv4_addresses = [addr[4][0] for addr in addresses if addr[0] == socket.AF_INET]
    
#     return ipv4_addresses

# # Example usage
# print(get_ipv4_addresses('en0'))

# import subprocess
# import re

# def get_ipv4_addresses():
#     # Get the output of the ifconfig command
#     output = subprocess.check_output(['ifconfig'])
#     print(output)
#     # Use regular expressions to find the interface names and IPv4 addresses
#     pattern = r'(\w+):.*?inet (\d+\.\d+\.\d+\.\d+)'
#     matches = re.findall(pattern, output, flags=re.DOTALL)

#     # Create a dictionary of interface names and their IPv4 addresses
#     ipv4_addresses = {}
#     for match in matches:
#         ipv4_addresses[match[0]] = match[1]

#     return ipv4_addresses

# import socket   
# hostname=socket.gethostname()   
# IPAddr=socket.gethostbyname(hostname)   
# print("Your Computer Name is:"+hostname)   
# print("Your Computer IP Address is:"+IPAddr)   

import socket

import fcntl
import struct

def get_ipv4_addresses():
    addresses = []
    for interface in socket.if_nameindex():
        try:
            socket_fd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip_address = socket.inet_ntoa(fcntl.ioctl(socket_fd.fileno(), 0x8915, struct.pack('256s', interface[1].encode()))[20:24])
            addresses.append((interface[1], ip_address))
        except IOError:
            pass
    return addresses


# def get_ipv4_addresses():
#     ip_list = []
#     for interface in socket.if_nameindex():
#         if interface[1].startswith('lo'):  # skip loopback interface
#             continue
#         addresses = socket.getaddrinfo(interface[1], None)
#         for address in addresses:
#             ip = address[4][0]
#             if '.' in ip:  # check if IPv4 address
#                 ip_list.append((interface[1], ip))
#     return ip_list

if __name__ == '__main__':
    print(get_ipv4_addresses())
