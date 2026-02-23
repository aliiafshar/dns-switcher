import os
import tkinter as tk
from tkinter import messagebox

dns_options = {
    "Shecan": ["178.22.122.100", "185.51.200.2"],
    "403": ["10.202.10.202", "10.202.10.102"],
    "HostIran": ["172.29.0.100", "172.29.2.100"],
    "Begzar": ["185.55.226.26", "185.55.225.25"],
    "Hamava": ["185.20.163.2", "185.20.163.4"],
    "Asiatech": ["194.36.174.161", "178.22.122.100"],
    "RadarGame": ["10.202.10.10", "10.202.10.11"],
    "Electro": ["78.157.42.100", "78.157.42.101"],
    "Cloudflare": ["1.1.1.1", "1.0.0.1"],
    "Google": ["8.8.8.8", "8.8.4.4"],
    "Google2": ["8.8.8.8", "4.2.2.4"],
    "OpenDNS": ["208.67.222.222", "208.67.220.220"],
    "Quad9": ["9.9.9.9", "149.112.112.112"],
    "Comodo Secure DNS": ["8.26.56.26", "8.20.247.20"],
    "LagZero": ["95.38.132.152", "95.38.132.153"],
    "DnsPro": ["87.107.110.109","87.107.110.110"],
    "Cisco": ["208.67.222.222", "208.67.222.20"],
    "Verisign": ["64.6.64.6", "64.6.65.6"],
    "Shelter": ["91.92.250.185", "91.92.244.233"],
    "Pishgaman": ["5.202.100.100", "5.202.100.101"],
    "Shatel": ["85.15.1.14", "85.15.1.15"],
    "Hamrah Aval": ["208.67.220.200", "208.67.222.222"],
    "Irancell": ["74.82.42.42", "0.0.0.0"],
    "Rightel": ["91.239.100.100", "89.223.43.71"],
    "NTT": ["129.250.35.250", "129.250.35.251"],
    "NextDNS": ["45.90.28.190", "45.90.30.190"]

} 

def set_dns(dns_list):
    try:
        with open("/etc/resolv.conf", "w") as f:
            for dns in dns_list:
                f.write(f"nameserver {dns}\n")
        print("DNS updated successfully.")
    except PermissionError:
        z
    except Exception as e:
        print(f"Error: {e}")

def gui_mode():
    def apply_dns():
        selected = listbox.get(listbox.curselection())
        set_dns(dns_options[selected])
        messagebox.showinfo("Success", f"{selected} DNS applied.")

    root = tk.Tk()
    root.title("DNS Switcher")

    label = tk.Label(root, text="Choose a DNS Provider:")
    label.pack(pady=10)

    listbox = tk.Listbox(root, height=15, width=40)
    for name in dns_options:
        listbox.insert(tk.END, name)
    listbox.pack(pady=10)

    btn = tk.Button(root, text="Apply", command=apply_dns)
    btn.pack(pady=10)

    root.mainloop()

def cli_mode():
    print("Select a DNS Provider:")
    for i, name in enumerate(dns_options.keys(), 1):
        print(f"{i}. {name}")
    try:
        choice = int(input("Enter number: ")) - 1
        selected_name = list(dns_options.keys())[choice]
        set_dns(dns_options[selected_name])
        print(f"{selected_name} DNS applied.")
    except (IndexError, ValueError):
        print("Invalid selection.")
    except Exception as e:
        print(f"Error: {e}")

def is_display_available():
    return os.environ.get('DISPLAY') is not None

if __name__ == "__main__":
    if is_display_available():
        gui_mode()
    else:
        cli_mode()