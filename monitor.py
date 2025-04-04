#!/usr/bin/env python3
from lib import ip_tools, network_scan, speed_test, bandwidth
import argparse

def main():
    parser = argparse.ArgumentParser(description="Network Monitor Tool")
    parser.add_argument("--ip", action="store_true", help="Show IP info")
    parser.add_argument("--scan", action="store_true", help="Scan local network")
    parser.add_argument("--speed", action="store_true", help="Run speed test")
    parser.add_argument("--bandwidth", action="store_true", help="Monitor bandwidth")
    
    args = parser.parse_args()
    
    if args.ip:
        print(ip_tools.get_network_info())
    
    if args.scan:
        print("Active hosts:", network_scan.scan_network())
    
    if args.speed:
        print("Speed test:", speed_test.run_speed_test())
    
    if args.bandwidth:
        print("Bandwidth:", bandwidth.get_bandwidth())

if __name__ == "__main__":
    main()