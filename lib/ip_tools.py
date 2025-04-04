import requests
import socket

def get_public_ip():
    try:
        return requests.get('https://api.ipify.org').text
    except:
        return "Error: No internet connection"

def get_local_ips():
    return socket.gethostbyname_ex(socket.gethostname())[2]

def get_network_info():
    return {
        "public_ip": get_public_ip(),
        "local_ips": get_local_ips(),
        "hostname": socket.gethostname()
    }