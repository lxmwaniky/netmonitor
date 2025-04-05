import speedtest
import requests

def run_speed_test(stdscr=None):
    """Robust speed test with fallback"""
    try:
        if stdscr:
            stdscr.addstr("Initializing speed test...")
            stdscr.refresh()
            
        st = speedtest.Speedtest(
            config={'download_timeout': 10, 'upload_timeout': 10}
        )
        
        if stdscr:
            stdscr.addstr("Finding best server...")
            stdscr.refresh()
            
        st.get_best_server()
        
        if stdscr:
            stdscr.addstr("Testing download...")
            stdscr.refresh()
        download = round(st.download() / 1_000_000, 2)
        
        if stdscr:
            stdscr.addstr("Testing upload...")
            stdscr.refresh()
        upload = round(st.upload() / 1_000_000, 2)
        
        return {
            "status": "success",
            "download": download,
            "upload": upload,
            "server": st.results.server["sponsor"]
        }
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "solution": "Try again later or check internet connection"
        }