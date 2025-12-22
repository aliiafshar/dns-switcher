import os
import tkinter as tk
from tkinter import messagebox
import subprocess

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

def get_active_interfaces():
    """Get the names of all active network interfaces on Windows."""
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
                # Interface name is everything after the third column
                interfaces.append(" ".join(parts[3:]))
    except Exception as e:
        print(f"Error detecting interfaces: {e}")
    return interfaces

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

def set_dns(dns_list, selected_interfaces=None):
    """Set DNS servers for selected Windows network interfaces."""
    if not is_admin():
        print("Error: Administrator privileges required!")
        print("Please run this script as Administrator (right-click -> Run as administrator)")
        return False
    
    all_interfaces = get_active_interfaces()
    if not all_interfaces:
        print("Error: Could not detect any active network interfaces.")
        print("Please check your network connection.")
        return False
    
    # If no interfaces selected, ask user to choose
    if selected_interfaces is None:
        print(f"Found {len(all_interfaces)} active interface(s):")
        for i, iface in enumerate(all_interfaces, 1):
            print(f"  {i}. {iface}")
        print(f"  {len(all_interfaces) + 1}. All interfaces")
        print()
        
        try:
            choice = input("Select interface number (or 'all' for all interfaces): ").strip().lower()
            
            if choice == 'all' or choice == str(len(all_interfaces) + 1):
                selected_interfaces = all_interfaces
            else:
                choice_num = int(choice)
                if 1 <= choice_num <= len(all_interfaces):
                    selected_interfaces = [all_interfaces[choice_num - 1]]
                else:
                    print("Invalid selection.")
                    return False
        except (ValueError, IndexError):
            print("Invalid input.")
            return False
    
    print()
    print(f"Applying DNS to {len(selected_interfaces)} interface(s)...")
    print()
    
    success_count = 0
    for interface in selected_interfaces:
        print(f"Setting DNS for: {interface}")
        try:
            # Set primary DNS
            cmd = [
                "netsh", "interface", "ipv4", "set", "dns",
                f"name={interface}", "static", dns_list[0]
            ]
            print(f"  Running: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                continue
            
            # Add secondary DNS if available
            if len(dns_list) > 1:
                cmd = [
                    "netsh", "interface", "ipv4", "add", "dns",
                    f"name={interface}", dns_list[1], "index=2"
                ]
                print(f"  Running: {' '.join(cmd)}")
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"  Warning: Could not add secondary DNS: {result.stderr}")
            
            print(f"  ✓ DNS updated successfully for {interface}")
            print(f"    Primary DNS: {dns_list[0]}")
            if len(dns_list) > 1:
                print(f"    Secondary DNS: {dns_list[1]}")
            print()
            success_count += 1
        except Exception as e:
            print(f"  Error: {e}")
            print()
    
    if success_count > 0:
        print(f"DNS updated successfully on {success_count}/{len(selected_interfaces)} interface(s).")
        return True
    else:
        print("Failed to update DNS on any interface.")
        return False

def gui_mode():
    """Run the DNS switcher in GUI mode with interface selection."""
    def apply_dns():
        try:
            # Get selected DNS provider
            selected_dns = listbox_dns.get(listbox_dns.curselection())
            
            # Get selected interfaces
            selected_interfaces = []
            for i, var in enumerate(interface_vars):
                if var.get():
                    selected_interfaces.append(all_interfaces[i])
            
            if not selected_interfaces:
                messagebox.showwarning("Warning", "Please select at least one network interface.")
                return
            
            # Apply DNS in the background
            result = set_dns(dns_options[selected_dns], selected_interfaces)
            
            if result:
                messagebox.showinfo("Success", f"{selected_dns} DNS applied successfully to {len(selected_interfaces)} interface(s)!")
            else:
                messagebox.showerror("Error", "Failed to set DNS. Make sure you're running as Administrator.")
            
            # Close the window after showing result
            root.quit()
            root.destroy()
                
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a DNS provider first.")
    
    # Get all interfaces first
    all_interfaces = get_active_interfaces()
    if not all_interfaces:
        print("Error: Could not detect any active network interfaces.")
        return
    
    root = tk.Tk()
    root.title("DNS Switcher - Windows")
    
    # DNS Provider selection
    label_dns = tk.Label(root, text="Choose a DNS Provider:", font=("Arial", 10, "bold"))
    label_dns.pack(pady=(10, 5))
    
    listbox_dns = tk.Listbox(root, height=10, width=40)
    for name in dns_options:
        listbox_dns.insert(tk.END, name)
    listbox_dns.pack(pady=5)
    
    # Interface selection
    label_iface = tk.Label(root, text="Select Network Interface(s):", font=("Arial", 10, "bold"))
    label_iface.pack(pady=(10, 5))
    
    interface_frame = tk.Frame(root)
    interface_frame.pack(pady=5)
    
    interface_vars = []
    for i, iface in enumerate(all_interfaces):
        var = tk.BooleanVar(value=True)  # Default: all selected
        interface_vars.append(var)
        cb = tk.Checkbutton(interface_frame, text=iface, variable=var)
        cb.pack(anchor='w')
    
    # Apply button
    btn = tk.Button(root, text="Apply DNS", command=apply_dns, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
    btn.pack(pady=15)
    
    root.mainloop()

def cli_mode():
    """Run the DNS switcher in CLI mode."""
    print("Select a DNS Provider:")
    for i, name in enumerate(dns_options.keys(), 1):
        print(f"{i}. {name}")
    
    try:
        choice = int(input("Enter number: ")) - 1
        selected_name = list(dns_options.keys())[choice]
        if set_dns(dns_options[selected_name]):
            print(f"{selected_name} DNS applied successfully.")
        else:
            print("Failed to apply DNS.")
    except (IndexError, ValueError):
        print("Invalid selection.")
    except Exception as e:
        print(f"Error: {e}")

def is_display_available():
    """Check if a display is available for GUI mode."""
    try:
        # On Windows, try to import tkinter and create a test window
        root = tk.Tk()
        root.withdraw()
        root.destroy()
        return True
    except Exception:
        return False

if __name__ == "__main__":
    if is_display_available():
        gui_mode()
    else:
        cli_mode()
