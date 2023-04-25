# Stress Tesing 

## USAGE

```
sudo python3 file IP PORT
```

## Monitor Traffic 
> To monitor the traffic that is being sent to machine

TCP SYN packets sent to your machine
```
sudo tcpdump 'tcp[tcpflags] & tcp-syn != 0'
```

if you want to save the captured packets to a file, you can use the -w option followed by a filename:
```
sudo tcpdump -w output.pcap 'tcp[tcpflags] & tcp-syn != 0'
```

This will save the captured packets to a file called output.pcap. You can then use a tool like Wireshark to analyze the captured packets in more detail.



To capture UDP packets, you can use a similar command but filter for UDP packets instead:
```
sudo tcpdump 'udp'
```