import pytest
from lib import ip_tools, bandwidth

@pytest.fixture
def mock_network():
    return {
        "public_ip": "203.0.113.1",
        "local_ips": ["192.168.1.10"]
    }