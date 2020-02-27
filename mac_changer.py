#!/usr/bin/env python

import subprocess
import optparse
import re

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

def get_current_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig", interface])
    print(ifconfig_result)

    mac_adddress_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_adddress_search_result:
        return mac_adddress_search_result(0)
    else:
        print("[-] No MAC address")

# interface=options.interface
# mac_address=options.mac_address

# interface="wlan0"
# mac_address="00.11.22.33.44.55"

options = get_arguments()
print("Current MAC Adress: " + str(get_current_mac(options.interface)))
change_mac(options.interface, options.mac_address)

new_mac = get_current_mac(options.interface)
if new_mac == options.mac_address:
    print("[+] MAC address Successfully changed to {}".format(new_mac))
else:
    print("[-] MAC address did not get changed.")