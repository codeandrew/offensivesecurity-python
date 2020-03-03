#!/usr/bin/env python
import netfilterqueue

def proccess_packet(packet):
    print(packet)
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, proccess_packet)

queue.run()