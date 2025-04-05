from lib import ip_tools
import socket
import pytest

def test_get_network_info(monkeypatch, mock_network):
    def mock_get_public_ip():
        return mock_network["public_ip"]
    
    monkeypatch.setattr(ip_tools, "get_public_ip", mock_get_public_ip)
    
    result = ip_tools.get_network_info()
    assert result["public_ip"] == "203.0.113.1"
    assert isinstance(result["local_ips"], list)