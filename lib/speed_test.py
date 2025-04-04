import speedtest

def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()
    return {
        "download": st.download() / 1_000_000,  # Mbps
        "upload": st.upload() / 1_000_000,
        "ping": st.results.ping
    }