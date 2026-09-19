# Wi-Fi QR Code Generator

یک ابزار پایتونی ساده و قابل استفاده برای ساخت QR Code اتصال به شبکهٔ Wi-Fi. این پروژه از نوت‌بوک ارسالی توسعه داده شده و علاوه بر نسخهٔ Jupyter، یک ماژول قابل استفاده، رابط خط فرمان، تست و مدیریت وابستگی دارد.

## قابلیت‌ها

- ساخت QR Code استاندارد با فرمت `WIFI:`
- پشتیبانی از WPA، WPA2، WEP و شبکهٔ بدون رمز
- پشتیبانی از شبکه‌های مخفی
- Escape کردن کاراکترهای ویژه در نام شبکه و رمز
- خروجی PNG با کیفیت مناسب برای اسکن موبایل
- اجرای تعاملی یا خط فرمان
- تست خودکار با pytest

## نصب

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## استفادهٔ تعاملی

```bash
python -m src.wifi_qrcode
```

## استفاده با خط فرمان

```bash
python -m src.wifi_qrcode \\
  --ssid "Home WiFi" \\
  --password "your-password" \\
  --security WPA2 \\
  --output output/wifi_qrcode.png
```

برای شبکهٔ بدون رمز:

```bash
python -m src.wifi_qrcode --ssid "Guest" --security nopass --output output/guest.png
```

برای شبکهٔ مخفی، گزینهٔ `--hidden` را اضافه کنید.

## اجرای تست‌ها

```bash
pip install -r requirements-dev.txt
pytest
```

## اجرای نوت‌بوک اصلی

فایل اصلی ارسالی در مسیر `notebooks/wifiqrcode_original.ipynb` حفظ شده است. برای اجرای آن:

```bash
pip install notebook
jupyter notebook notebooks/wifiqrcode_original.ipynb
```

## نکات امنیتی

رمز Wi-Fi داخل QR Code ذخیره می‌شود؛ بنابراین تصویر QR را فقط با افراد مورد اعتماد به اشتراک بگذارید. این پروژه رمز شبکه را در فایل یا سرویس خارجی ذخیره نمی‌کند.

## مجوز

MIT
