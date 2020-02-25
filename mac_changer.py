#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest="interface",
                      help=' Interface to change its MAC address ')
    parser.add_option('-m', '--mac', dest="mac_address",
                      help=' New MAC address to use')
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Specify an interface, use --help")
    if not options.mac_address:
        parser.error("[-] Please Specify an new MAC address, use --help")
    
    return options
    

def change_mac(interface, mac_address):
    print()
    print("-"*60)
    print("[+] Changing MAC address for {} to {}".format(interface, mac_address))

    subprocess.call([ "ifconfig", interface, "down" ])
    subprocess.call([ "ifconfig", interface, "hw", "ether", mac_address ])
    subprocess.call([ "ifconfig", interface, "up" ])

# interface=options.interface
# mac_address=options.mac_address

# interface="wlan0"
# mac_address="00.11.22.33.44.55"

options = get_arguments()
change_mac(options.interface, options.mac_address)