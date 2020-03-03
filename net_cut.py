#!/usr/bin/env python
import netfilterqueue

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, proccess_packet)

queue.run