# Offensive Security Python
> Offensive Security Python. Collection of python scripts that I created/pirated/curated to help me understand CyberSecurity. I find it helpful to write the tools you use to help you really understand what it does and what's the purpose of it.    
> "When you try to understand everything, you stumble on a few things along the way"  
> "Code is the best place to capture current understanding of a model"  
 
**Topics**
- Changing MAC Address 
- Network Scanner
- ARP Spoofing
- Packet Sniffer
- DNS Spoofer
- Replace Download
- XSS Scanner 
- Network Scanner
- Utilities
  - Fake Profile Generator
  - Randomize MAC Address
  - Combine Wordlist

## Targets

1. DVWA
```
docker run --rm -it -p 80:80 vulnerables/web-dvwa:latest
```
2. metasploitable2
```
docker run --name container-name -it tleemcjr/metasploitable2:latest sh -c "/bin/services.sh && bash"
```

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


## Network Interfaces

| Network Interface | Description                                                    |
|-------------------|----------------------------------------------------------------|
| eth0              | Default network interface on Linux systems                     |
| wlan0             | Wireless network interface on Linux systems                    |
| en0               | Default network interface on macOS systems                     |
| en1               | Wireless network interface on macOS systems                    |
| Ethernet          | Default network interface on Windows systems (older versions)  |
| Wi-Fi             | Wireless network interface on Windows systems (older versions) |
| Ethernet0         | Default network interface on Windows systems (newer versions)  |
| Wi-Fi0            | Wireless network interface on Windows systems (newer versions) |
