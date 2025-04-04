import speedtest

def run_speed_test():
    """Basic speed test only"""
    st = speedtest.Speedtest()
    st.get_best_server()
    return {
        "download": round(st.download() / 1_000_000, 2),
        "upload": round(st.upload() / 1_000_000, 2)  
    }