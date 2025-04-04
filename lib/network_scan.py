import nmap

def scan_network(subnet="192.168.1.0/24"):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=subnet, arguments='-sn')
    return scanner.all_hosts()