# Playbook

## Steps 
mac_changer -> network_scanner -> arp_spoof -> packet_sniffer

## Sniffing Credentials
network_scanner -> arp_spoof -> packet_sniffer

## Replace Download
network_scanner -> arp_spoof -> replace_download

## Hooking in Beef
network_scanner > arp_spoof > code_injector

> Scan first to get your target's IP
> then arp spoof to become the man in the middle
> then inject your script using code injector to hook
> them in the BEEF Xss framework
