# Scapy 101 Cheat Sheet
> import scapy.all as scapy

packet  
> Data from the network 

scapy.IP(packet)
> To use the packet from the scapy object


scapy.ls()
> To show field list of functions

scapy.ARP()

exammple:

scapy.ls(scapy.ARP())
```
hwtype     : XShortField                         = 1               (1)
ptype      : XShortEnumField                     = 2048            (2048)
hwlen      : FieldLenField                       = None            (None)
plen       : FieldLenField                       = None            (None)
op         : ShortEnumField                      = 1               (1)
hwsrc      : MultipleTypeField                   = '88:e9:fe:76:6d:0a' (None)
psrc       : MultipleTypeField                   = '192.168.254.107' (None)
hwdst      : MultipleTypeField                   = '00:00:00:00:00:00' (None)
pdst       : MultipleTypeField                   = '0.0.0.0'       (None)
```
scapy.show()

Scapy Layers
- IP
- TCP
- UDP
- Raw