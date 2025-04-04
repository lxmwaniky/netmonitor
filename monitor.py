#!/usr/bin/env python3
from lib import ip_tools, network_scan, speed_test, bandwidth
import argparse
import time

def main():
    parser = argparse.ArgumentParser(description="Basic Network Monitor")
    parser.add_argument("--ip", action="store_true", help="Check IP")
    parser.add_argument("--scan", action="store_true", help="Scan network")
    parser.add_argument("--speed", action="store_true", help="Test speed")
    parser.add_argument("--bandwidth", action="store_true", help="Check bandwidth")
    parser.add_argument("--interval", type=float, default=1.0, help="Polling interval in seconds")
    
    args = parser.parse_args()
    
    if args.ip:
        print("IP Info:", ip_tools.get_network_info())
    
    if args.scan:
        print("Network Scan:", network_scan.scan_network())
    
    if args.speed:
        print("Speed Test:", speed_test.run_speed_test())
    
    if args.bandwidth:
        try:
            while True:
                start = bandwidth.get_bandwidth()
                time.sleep(args.interval)
                end = bandwidth.get_bandwidth()
                
                print(f"Sent: {(end['sent'] - start['sent'])/args.interval:.2f} B/s | "
                    f"Recv: {(end['recv'] - start['recv'])/args.interval:.2f} B/s")
                    
        except KeyboardInterrupt:
            print("\nMonitoring stopped")

if __name__ == "__main__":
    main()