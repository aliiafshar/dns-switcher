import os
import subprocess 
import customtkinter as ctk
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
        # تلاش برای نوشتن مستقیم
        with open("/etc/resolv.conf", "w") as f:
            for dns in dns_list:
                f.write(f"nameserver {dns}\n")
        messagebox.showinfo("Success", "DNS updated successfully.")
    except PermissionError:
        # ساخت دستور برای pkexec فقط برای نوشتن
        cmd = "echo '{}' | pkexec tee /etc/resolv.conf > /dev/null".format(
            "\n".join(f"nameserver {dns}" for dns in dns_list)
        )
        try:
            subprocess.run(cmd, shell=True, check=True)
            messagebox.showinfo("Success", "DNS updated successfully (via root).")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to write DNS. Root permissions required.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def gui_mode():
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("DNS Switcher")
    root.geometry("400x500")
    
    frame = ctk.CTkFrame(root, corner_radius=15)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    label = ctk.CTkLabel(frame, text="Choose a DNS Provider:", font=ctk.CTkFont(size=16))
    label.pack(pady=10)

    listbox = ctk.CTkOptionMenu(frame, values=list(dns_options.keys()))
    listbox.pack(pady=10)

    def apply_selected_dns():
        selected = listbox.get()
        if selected in dns_options:
            set_dns(dns_options[selected])
        else:
            messagebox.showwarning("Warning", "Select a DNS first.")

    apply_btn = ctk.CTkButton(frame, text="Apply Selected DNS", command=apply_selected_dns)
    apply_btn.pack(pady=10)

    manual_label = ctk.CTkLabel(frame, text="Or enter custom DNS:", font=ctk.CTkFont(size=14))
    manual_label.pack(pady=10)

    entry1 = ctk.CTkEntry(frame, placeholder_text="Primary DNS")
    entry1.pack(pady=5)
    entry2 = ctk.CTkEntry(frame, placeholder_text="Secondary DNS")
    entry2.pack(pady=5)

    def apply_manual_dns():
        dns1 = entry1.get().strip()
        dns2 = entry2.get().strip()
        if dns1:
            dns_list = [dns1]
            if dns2:
                dns_list.append(dns2)
            set_dns(dns_list)
        else:
            messagebox.showwarning("Warning", "Enter at least one DNS.")

    manual_btn = ctk.CTkButton(frame, text="Apply Manual DNS", command=apply_manual_dns)
    manual_btn.pack(pady=10)

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