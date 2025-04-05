from unittest.mock import Mock, patch
from lib import speed_test

def test_speed_test(monkeypatch):
    mock_speedtest = Mock()
    mock_speedtest.download.return_value = 50_000_000  # 50 Mbps
    mock_speedtest.upload.return_value = 10_000_000    # 10 Mbps
    
    monkeypatch.setattr("speedtest.Speedtest", lambda: mock_speedtest)
    
    result = speed_test.run_speed_test()
    assert result["download"] == 50.0
    assert result["upload"] == 10.0