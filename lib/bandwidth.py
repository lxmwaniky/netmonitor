import psutil
import time

def get_bandwidth(interface="eth0", interval=1):
    old = psutil.net_io_counters(pernic=True)[interface]
    time.sleep(interval)
    new = psutil.net_io_counters(pernic=True)[interface]
    return {
        "sent": (new.bytes_sent - old.bytes_sent) / interval,
        "recv": (new.bytes_recv - old.bytes_recv) / interval
    }