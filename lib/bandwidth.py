import psutil

def get_bandwidth():
    """Returns raw sent/received bytes"""
    io = psutil.net_io_counters()
    return {'sent': io.bytes_sent, 'recv': io.bytes_recv}