#!/usr/bin/env python

import scapy.all as scapy

def scapy_scan(ip):
    scapy.arping(ip)

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()
    # 34. Combining Frames Review

    arp_request_broadcast = broadcast/arp_request
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show()

    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())

scan("10.0.2.1/24")