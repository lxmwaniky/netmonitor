import socket
import requests
from netifaces import interfaces, ifaddresses, AF_INET

def get_network_info():
    """Get both public and local network IP"""
    # Public IP (unchanged)
    public_ip = requests.get('https://api.ipify.org').text
    
    # Local IP - improved method
    local_ips = []
    for iface in interfaces():
        addrs = ifaddresses(iface).get(AF_INET, [])
        for addr in addrs:
            if 'addr' in addr and not addr['addr'].startswith('127.'):
                local_ips.append(addr['addr'])
    
    return {
        "public_ip": public_ip,
        "local_ips": local_ips or ["No LAN IP found"]
    }