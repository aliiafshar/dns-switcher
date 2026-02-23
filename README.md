# DNS Switcher / سوییچر DNS

A simple script to switch between various Iranian DNS providers.
Supports **Linux** (Python) and **Windows** versions, with both **GUI (Tkinter)** and **CLI (terminal)** modes based on your environment.

یک اسکریپت ساده برای تغییر DNS به سرورهای ایرانی.
نسخه‌های **لینوکس** (پایتون) و **ویندوز** را پشتیبانی می‌کند و هم **GUI** و هم **CLI** دارد.

![Windows Screenshot](screenshot.png)

---

## ✅ Features / ویژگی‌ها

* Selectable DNS providers like Shecan, 403, RadarGame, and more.
* انتخاب ارائه‌دهندگان DNS مثل Shecan، 403، RadarGame و غیره
* Applies DNS automatically:

  * **Linux:** writes to `/etc/resolv.conf`
  * **ویندوز:** تغییر DNS روی کارت شبکه انتخابی
* Automatically detects if GUI is available, otherwise runs in terminal
* **Windows version:** GUI included, supports per-network adapter selection, and comes as **exe**

  * Works for Wi-Fi, Ethernet, and other adapters

---

## 🚀 How to Run / نحوه اجرا

### Linux / لینوکس

```bash
sudo python3 dns_switcher.py
```

### Windows / ویندوز

Run as administrator (Powershell):

```bash
# Python version
python3 dns_switcherWin.py

# EXE version
DNS_Switcher.exe
```

---

## 🔧 DNS Providers Included / سرورهای DNS موجود

**26 DNS providers available** - شامل ۲۶ سرویس‌دهنده DNS

### Iranian DNS Providers / سرویس‌دهندگان ایرانی

| Provider / ارائه‌دهنده | DNS Servers / سرورها           | Best For / مناسب برای             |
| ---------------------- | ------------------------------ | --------------------------------- |
| Shecan                 | 178.22.122.100, 185.51.200.2   | Gaming & Download / بازی و دانلود |
| 403                    | 10.202.10.202, 10.202.10.102   | General / عمومی                   |
| HostIran               | 172.29.0.100, 172.29.2.100     | General / عمومی                   |
| Begzar                 | 185.55.226.26, 185.55.225.25   | Gaming / بازی                     |
| HamAva                 | 185.20.163.2, 185.20.163.4     | General / عمومی                   |
| Asiatech               | 194.36.174.161, 178.22.122.100 | General / عمومی                   |
| RadarGame              | 10.202.10.10, 10.202.10.11     | Gaming & Download / بازی و دانلود |
| Electro                | 78.157.42.100, 78.157.42.101   | Gaming & Download / بازی و دانلود |
| Shelter                | 91.92.250.185, 91.92.244.233   | Gaming & Download / بازی و دانلود |
| Pishgaman              | 5.202.100.100, 5.202.100.101   | Connection / کانکشن               |
| Shatel                 | 85.15.1.14, 85.15.1.15         | Connection / کانکشن               |
| LagZero                | 95.38.132.152, 95.38.132.153   | Gaming / بازی                     |
| DnsPro                 | 87.107.110.109, 87.107.110.110 | General / عمومی                   |

### Mobile Carrier DNS / DNS اپراتورهای موبایل

| Provider / ارائه‌دهنده | DNS Servers / سرورها           |
| ---------------------- | ------------------------------ |
| Hamrah Aval            | 208.67.220.200, 208.67.222.222 |
| Irancell               | 74.82.42.42, 0.0.0.0           |
| Rightel                | 91.239.100.100, 89.223.43.71   |

### International DNS Providers / سرویس‌دهندگان بین‌المللی

| Provider / ارائه‌دهنده | DNS Servers / سرورها           | Best For / مناسب برای |
| ---------------------- | ------------------------------ | --------------------- |
| Cloudflare             | 1.1.1.1, 1.0.0.1               | Download / دانلود     |
| Google                 | 8.8.8.8, 8.8.4.4               | Download / دانلود     |
| Google2                | 8.8.8.8, 4.2.2.4               | Download / دانلود     |
| OpenDNS                | 208.67.222.222, 208.67.220.220 | Download / دانلود     |
| Cisco                  | 208.67.222.222, 208.67.222.20  | PS5                   |
| Quad9                  | 9.9.9.9, 149.112.112.112       | Gaming / بازی         |
| Verisign               | 64.6.64.6, 64.6.65.6           | Gaming / بازی         |
| NTT                    | 129.250.35.250, 129.250.35.251 | Gaming / بازی         |
| NextDNS                | 45.90.28.190, 45.90.30.190     | Gaming / بازی         |
| Comodo Secure DNS      | 8.26.56.26, 8.20.247.20        | Security / امنیت      |

---

## 🆕 Changelog / تغییرات نسخه جدید

* Added **Windows version** and **exe**
* GUI available if detected
* Per-network adapter DNS selection (Wi-Fi, Ethernet, etc.)
