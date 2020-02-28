#!/usr/bin/env python

import scapy.all as scapy

def scapy_scan(ip):
    scapy.arping(ip)

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # 34. Combining Frames Review
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC Address")
    print("-"*50)
    for e in answered_list:
        print(e[1].psrc + "\t\t" + e[1].hwsrc)

scan("10.0.2.1/24")