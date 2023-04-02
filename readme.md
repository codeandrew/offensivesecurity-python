# Offensive Security Python
> Creating Offensive security tools using python

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