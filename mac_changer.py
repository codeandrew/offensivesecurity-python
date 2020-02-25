#!/usr/bin/env python

import subprocess

interface="wlan0"
mac_address="00.11.22.33.44.55"

subprocess.call("ifconfig {} down".format(interface), shell=True)
subprocess.call("ifconfig {} hw ether {}".format(interface, mac_address), shell=True)
subprocess.call("ifconfig {} up".format(interface), shell=True)