# DNS Switcher / سوییچر DNS

A simple script to switch between various Iranian DNS providers.
Supports **Linux** (Python) and **Windows** versions, with both **GUI (Tkinter)** and **CLI (terminal)** modes based on your environment.

یک اسکریپت ساده برای تغییر DNS به سرورهای ایرانی.
نسخه‌های **لینوکس** (پایتون) و **ویندوز** را پشتیبانی می‌کند و هم **GUI** و هم **CLI** دارد.

---

## ✅ Features / ویژگی‌ها

* Selectable DNS providers like Shecan, 403, RadarGame, and more.
* انتخاب ارائه‌دهندگان DNS مثل Shecan، 403، RadarGame و غیره
* Applies DNS automatically:

  * **Linux:** writes to `/etc/resolv.conf`
  * **ویندوز:** تغییر DNS روی کارت شبکه انتخابی
* Automatically detects if GUI is available, otherwise runs in terminal
* **Windows version:** GUI included and supports per-network adapter selection

  * Works for Wi-Fi, Ethernet, and other adapters

---

## 🚀 How to Run / نحوه اجرا

### Linux / لینوکس

```bash
sudo python3 dns_switcher.py
```

### Windows / ویندوز

* Run `dns_switcherWin.py` (GUI) or `dns_switcher.py` (CLI)
* Run the GUI and select the network adapter (Wi-Fi, Ethernet, etc.)
* اجرای GUI و انتخاب کارت شبکه (Wi-Fi, Ethernet و غیره)

---

## 🔧 DNS Providers Included / سرورهای DNS موجود

| Provider / ارائه‌دهنده | DNS Servers / سرورها           |
| ---------------------- | ------------------------------ |
| Shecan                 | 178.22.122.100, 185.51.200.2   |
| 403                    | 10.202.10.202, 10.202.10.102   |
| HostIran               | 172.29.0.100, 172.29.2.100     |
| Begzar                 | 185.55.226.26, 185.55.225.25   |
| HamAva                 | 185.20.163.2, 185.20.163.4     |
| Asiatech               | 194.36.174.161, 178.22.122.100 |
| RadarGame              | 10.202.10.10, 10.202.10.11     |
| Electro                | 78.157.42.100, 78.157.42.101   |
| Cloudflare             | 1.1.1.1, 1.0.0.1               |
| Google                 | 8.8.8.8, 8.8.4.4               |
| OpenDNS                | 208.67.222.222, 208.67.220.220 |
| Quad9                  | 9.9.9.9, 149.112.112.112       |
| Comodo Secure DNS      | 8.26.56.26, 8.20.247.20        |
| LagZero                | 95.38.132.152, 95.38.132.153   |
| DnsPro                 | 87.107.110.109, 87.107.110.110 |

---

## 🆕 Changelog / تغییرات نسخه جدید

* Added **Windows version**

  * اضافه شدن نسخه ویندوز
* GUI available if detected

  * اضافه شدن رابط گرافیکی (GUI) در صورت موجود بودن
* Per-network adapter DNS selection (Wi-Fi, Ethernet, etc.)

  * انتخاب کارت شبکه برای اعمال تنظیمات DNS
