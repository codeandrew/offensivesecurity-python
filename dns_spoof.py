#!/usr/bin/env python
import netfilterqueue
import subprocess
import scapy.all as scapy

def proccess_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    print(scapy_packet.show())
    packet.accept()

subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0", shell=True)
subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0", shell=True)

try:
    while True:
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, proccess_packet)
        queue.run()
except KeyboardInterrupt:
    subprocess.call("iptables --flush", shell=True)
    print("\nStopped.. IP Tables Flushed")