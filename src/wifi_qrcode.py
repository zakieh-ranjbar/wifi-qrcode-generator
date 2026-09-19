"""Generate Wi-Fi QR codes using the standard WIFI: payload format."""
from __future__ import annotations

from pathlib import Path
import argparse
import qrcode


def escape_wifi(value: str) -> str:
    """Escape characters reserved by the Wi-Fi QR payload format."""
    return value.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace(":", "\\:")


def build_wifi_payload(ssid: str, password: str = "", security: str = "WPA", hidden: bool = False) -> str:
    """Build a standards-compatible Wi-Fi QR payload."""
    if not ssid.strip():
        raise ValueError("SSID cannot be empty")
    security = security.upper().strip()
    if security not in {"WPA", "WPA2", "WEP", "nopass".upper()}:
        raise ValueError("security must be WPA, WPA2, WEP, or nopass")
    if security == "NOPASS":
        password = ""
    return f"WIFI:S:{escape_wifi(ssid)};T:{security};P:{escape_wifi(password)};H:{str(hidden).lower()};;"


def generate_qr(ssid: str, password: str = "", security: str = "WPA", hidden: bool = False, output: str | Path = "wifi_qrcode.png") -> Path:
    """Generate and save a Wi-Fi QR PNG, returning its path."""
    payload = build_wifi_payload(ssid, password, security, hidden)
    image = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
    image.add_data(payload)
    image.make(fit=True)
    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.make_image(fill_color="black", back_color="white").save(output_path)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a QR code for a Wi-Fi network")
    parser.add_argument("--ssid", help="Wi-Fi network name")
    parser.add_argument("--password", help="Wi-Fi password")
    parser.add_argument("--security", choices=["WPA", "WPA2", "WEP", "nopass"], default="WPA")
    parser.add_argument("--hidden", action="store_true", help="Mark the network as hidden")
    parser.add_argument("--output", default="wifi_qrcode.png", help="Output PNG path")
    args = parser.parse_args()
    ssid = args.ssid or input("نام Wi-Fi را وارد کنید: ")
    password = args.password if args.password is not None else input("رمز Wi-Fi را وارد کنید: ")
    security = args.security if args.ssid else input("نوع امنیت (WPA/WPA2/WEP/nopass): ") or "WPA"
    path = generate_qr(ssid, password, security, args.hidden, args.output)
    print(f"QR Code با موفقیت ساخته شد: {path}")


if __name__ == "__main__":
    main()
