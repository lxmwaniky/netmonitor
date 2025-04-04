import nmap
from lib import ip_tools  # Add this import

def scan_network():
    """Basic network scan using first local IP"""
    try:
        scanner = nmap.PortScanner()
        local_ip = ip_tools.get_network_info()['local_ips'][0]
        subnet = ".".join(local_ip.split('.')[:3]) + ".0/24"
        scanner.scan(hosts=subnet, arguments='-sn')
        return scanner.all_hosts()
    except Exception as e:
        return f"Scan failed: {str(e)}"