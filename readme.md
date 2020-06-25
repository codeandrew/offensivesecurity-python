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

MAC Address is auto generated randomly. Just Specify the the interface. 

```bash
python mac_changer.py -i <INTERFACE> # template
python mac_changer.py -i wlan0 # usage
```
> You can Manually add the mac address by doin -m   
> -h for more info

## Network Scanner
> My own version of nmap 


```bash
python network_scanner.py -t <IP SUBNET> # Template
python network_scanner.py -t 192.168.1.1/24 # Usage

```


### Python 3 Compatibility

pip3 install scapy-python3

#### Same line Printing 
print("\r [+] Info counter", end="")

