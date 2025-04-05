import psutil
from lib import bandwidth

def test_get_bandwidth():
    result = bandwidth.get_bandwidth(interval=0.1)
    assert "sent" in result
    assert "recv" in result
    assert isinstance(result["sent"], int)
    assert isinstance(result["recv"], int)