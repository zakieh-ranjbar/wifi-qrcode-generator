# Wi-Fi QR Code Generator

این پروژه یک ابزار ساده و کاربردی با Python برای ساخت QR Code اتصال به شبکه‌های Wi-Fi است. اطلاعات شبکه مثل نام، رمز عبور و نوع امنیت را وارد می‌کنید و برنامه QR Code مربوط به آن شبکه را برایتان می‌سازد.

ایدهٔ اولیهٔ این پروژه از یک Jupyter Notebook شروع شد، اما در ادامه توسعه پیدا کرد تا استفاده از آن راحت‌تر و ساختار پروژه هم استانداردتر شود. در حال حاضر علاوه بر نسخهٔ Notebook، پروژه شامل کد اصلی قابل استفاده، رابط خط فرمان (CLI)، تست‌ها و مدیریت وابستگی‌هاست.

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
