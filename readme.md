# Offensive Security Python
> From Zaid Sabih

**Topics**
- Changing MAC Address 
- Network Scanner
- ARP Spoofing
- Packet Sniffer
- DNS Spoofer
- Replace Download

## Playbook
> Check on how to use these tools 

## Dependencies on PIP
- scapy
- scapy_http
- netfilterqueue
- netifaces

## Changing the MAC Address 

This tool will change your current MAC address. 
MAC Address is auto generated randomly. Just Specify the the interface. 

```bash
python mac_changer.py -i <INTERFACE> # template
python mac_changer.py -i wlan0 # usage
```
> You can Manually add the mac address by doin -m   
> -h for more info

## Network Scanner

This tool will ping all the connected device inside the network/router.

```bash
python network_scanner.py -t <IP SUBNET> # Template
python network_scanner.py -t 192.168.1.1/24 # Usage
```

## ARP Spoofing 

This tools makes you the man in the middle. 
Tricks the gateway and the target IP to send you the data.
Poisoning the ARP. 

```bash
python arp_spoof.py -t <TARGET IP> -g <GATEWAY IP> # Template
python arp_spoof.py -t 192.168.1.2 -g 192.168.1.1 # Usage
```

---

### Python 3 Compatibility

pip3 install scapy-python3

#### Same line Printing 
print("\r [+] Info counter", end="")

