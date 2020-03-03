#!/usr/bin/env python
import netfilterqueue

def proccess_packet(packet):
    print(packet)

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, proccess_packet)

queue.run