import subprocess
import customtkinter as ctk
from tkinter import messagebox


# ==============================
# DNS OPTIONS
# ==============================

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
    "DnsPro": ["87.107.110.109", "87.107.110.110"],
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


# ==============================
# NETWORK FUNCTIONS 
# ==============================

def get_active_interfaces():
    interfaces = []
    try:
        result = subprocess.run(
            ["netsh", "interface", "show", "interface"],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 4 and parts[0] == "Enabled" and parts[1] == "Connected":
                interfaces.append(" ".join(parts[3:]))
    except Exception as e:
        print(f"Error detecting interfaces: {e}")
    return interfaces


def is_admin():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def set_dns(dns_list, selected_interfaces=None):
    if not is_admin():
        print("Run as Administrator.")
        return False

    all_interfaces = get_active_interfaces()
    if not all_interfaces:
        print("No active interfaces found.")
        return False

    if selected_interfaces is None:
        selected_interfaces = all_interfaces

    success_count = 0

    for interface in selected_interfaces:
        try:
            subprocess.run(
                ["netsh", "interface", "ipv4", "set", "dns",
                 f"name={interface}", "static", dns_list[0]],
                capture_output=True, text=True
            )

            if len(dns_list) > 1:
                subprocess.run(
                    ["netsh", "interface", "ipv4", "add", "dns",
                     f"name={interface}", dns_list[1], "index=2"],
                    capture_output=True, text=True
                )

            success_count += 1

        except Exception as e:
            print(f"Error setting DNS: {e}")

    return success_count > 0


# ==============================
# MODERN UI
# ==============================

def gui_mode():

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def apply_dns():
        try:
            if manual_switch.get():
                primary = primary_entry.get().strip()
                secondary = secondary_entry.get().strip()

                if not primary:
                    messagebox.showwarning("Warning", "Enter Primary DNS.")
                    return

                dns_to_apply = [primary]
                if secondary:
                    dns_to_apply.append(secondary)
            else:
                selected_dns = dns_dropdown.get()
                dns_to_apply = dns_options[selected_dns]

            selected_interfaces = [
                all_interfaces[i]
                for i, var in enumerate(interface_vars)
                if var.get()
            ]

            if not selected_interfaces:
                messagebox.showwarning("Warning", "Select at least one interface.")
                return

            apply_btn.configure(text="Applying...", state="disabled")
            root.update()

            result = set_dns(dns_to_apply, selected_interfaces)

            apply_btn.configure(text="Apply DNS", state="normal")

            if result:
                messagebox.showinfo("Success", "DNS Applied Successfully.")
            else:
                messagebox.showerror("Error", "Run as Administrator.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    all_interfaces = get_active_interfaces()

    root = ctk.CTk()
    root.geometry("540x680")
    root.title("DNS Switcher")

    # Header
    header = ctk.CTkFrame(root, corner_radius=0, fg_color="transparent")
    header.pack(fill="x", padx=25, pady=(25, 10))

    ctk.CTkLabel(
        header,
        text="sudocode DNS Switcher",
        font=ctk.CTkFont(size=28, weight="bold")
    ).pack(anchor="w")

    ctk.CTkLabel(
        header,
        text="Network DNS Manager",
        text_color="gray"
    ).pack(anchor="w")

    # DNS Card
    dns_card = ctk.CTkFrame(root, corner_radius=18)
    dns_card.pack(fill="x", padx=25, pady=10)

    ctk.CTkLabel(
        dns_card,
        text="DNS Provider",
        font=ctk.CTkFont(size=15, weight="bold")
    ).pack(anchor="w", padx=20, pady=(20, 8))

    dns_dropdown = ctk.CTkOptionMenu(
        dns_card,
        values=list(dns_options.keys())
    )
    dns_dropdown.pack(fill="x", padx=20, pady=(0, 20))

    # Manual DNS Card
    manual_card = ctk.CTkFrame(root, corner_radius=18)
    manual_card.pack(fill="x", padx=25, pady=10)

    manual_switch = ctk.CTkSwitch(
        manual_card,
        text="Use Manual DNS"
    )
    manual_switch.pack(anchor="w", padx=20, pady=20)

    primary_entry = ctk.CTkEntry(
        manual_card,
        placeholder_text="Primary DNS"
    )
    primary_entry.pack(fill="x", padx=20, pady=5)

    secondary_entry = ctk.CTkEntry(
        manual_card,
        placeholder_text="Secondary DNS (optional)"
    )
    secondary_entry.pack(fill="x", padx=20, pady=(0, 20))

    # Interface Card
    interface_card = ctk.CTkFrame(root, corner_radius=18)
    interface_card.pack(fill="both", expand=True, padx=25, pady=10)

    ctk.CTkLabel(
        interface_card,
        text="Network Interfaces",
        font=ctk.CTkFont(size=15, weight="bold")
    ).pack(anchor="w", padx=20, pady=20)

    interface_vars = []
    for iface in all_interfaces:
        var = ctk.BooleanVar(value=True)
        interface_vars.append(var)
        ctk.CTkCheckBox(
            interface_card,
            text=iface,
            variable=var
        ).pack(anchor="w", padx=30)

    # Apply Button
    apply_btn = ctk.CTkButton(
        root,
        text="Apply DNS",
        height=55,
        corner_radius=20,
        command=apply_dns
    )
    apply_btn.pack(fill="x", padx=25, pady=25)

    root.mainloop()


if __name__ == "__main__":
    gui_mode()