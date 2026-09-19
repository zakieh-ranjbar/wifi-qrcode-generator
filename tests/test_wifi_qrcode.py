import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from src.wifi_qrcode import build_wifi_payload, generate_qr


def test_payload_contains_network_data():
    assert build_wifi_payload("Home WiFi", "p;ass", "WPA2") == "WIFI:S:Home WiFi;T:WPA2;P:p\\;ass;H:false;;"


def test_nopass_ignores_password():
    assert "T:NOPASS" in build_wifi_payload("Guest", "secret", "nopass")
    assert "P:;" in build_wifi_payload("Guest", "secret", "nopass")


def test_generate_qr(tmp_path):
    output = generate_qr("Test", "password", output=tmp_path / "wifi.png")
    assert output.exists()
    assert output.stat().st_size > 100
