#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)


scan("10.0.2.1/24")