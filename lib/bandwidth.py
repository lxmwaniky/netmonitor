import psutil
import time

def get_bandwidth(stdscr=None, interval=1):
    """Human-readable bandwidth with rates"""
    try:
        if stdscr:
            stdscr.addstr("Measuring bandwidth...")
            stdscr.refresh()
            
        start = psutil.net_io_counters()
        time.sleep(interval)
        end = psutil.net_io_counters()
        
        sent = end.bytes_sent - start.bytes_sent
        recv = end.bytes_recv - start.bytes_recv
        
        return {
            "status": "success",
            "sent_bytes": sent,
            "recv_bytes": recv,
            "sent_rate": f"{sent/interval:.2f} B/s",
            "recv_rate": f"{recv/interval:.2f} B/s",
            "sent_mbps": f"{(sent*8)/1_000_000/interval:.2f} Mbps",
            "recv_mbps": f"{(recv*8)/1_000_000/interval:.2f} Mbps"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }