import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import font
import subprocess
import requests
import threading
import time
import datetime
import json
import socket

def get_default_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except:
        return "127.0.0.1"

def save_config():
    config = {"ip_address": ip_address.get(), "url": url.get()}
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file)

def load_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)
            ip_address.set(config.get("ip_address", get_default_ip()))
            url.set(config.get("url", ""))
    except FileNotFoundError:
        ip_address.set(get_default_ip())
        url.set("")

def update_image(online):
    """
    Update the displayed image based on online status.
    """
    new_image = PhotoImage(file="uptimekuma.png" if online else "uptimekumadown.png")
    logo_label.configure(image=new_image)
    logo_label.image = new_image

def monitor_ip():
    global monitoring
    while monitoring:
        response = subprocess.run(["ping", "-c", "1", ip_address.get()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        online = response.returncode == 0
        update_image(online)
        if online:
            try:
                requests.get(url.get())
            except requests.RequestException as e:
                print("Error making request:", e)
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if not online_time.get():
                online_time.set(current_time)
            offline_time.set("")
        else:
            if not offline_time.get() and online_time.get():
                offline_time.set(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(3)

def start_monitoring():
    global monitoring
    if not ip_address.get() or not url.get():
        messagebox.showerror("Error", "Please enter both IP address and URL.")
        return
    save_config()
    monitoring = True
    monitor_thread = threading.Thread(target=monitor_ip, daemon=True)
    monitor_thread.start()

def stop_monitoring():
    global monitoring
    monitoring = False
    online_time.set("")
    offline_time.set("")

# GUI Setup
root = tk.Tk()
root.title("Uptime Kuma Client")

# Load and display the logo
# Initially load the 'offline' image
logo = PhotoImage(file="uptimekumadown.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack(side="top", pady=10)

# Variables
monitoring = False
ip_address = tk.StringVar()
url = tk.StringVar()
online_time = tk.StringVar()
offline_time = tk.StringVar()

load_config()

# Start monitoring automatically if IP address and URL are set
if ip_address.get() and url.get():
    start_monitoring()

# Input fields
tk.Label(root, text="IP/Domain:").pack()
ip_entry = tk.Entry(root, textvariable=ip_address, justify='center')
ip_entry.pack()

tk.Label(root, text="Push URL:").pack()
url_entry = tk.Entry(root, textvariable=url)
url_entry.pack()

start_button = tk.Button(root, text="Save", command=start_monitoring)
start_button.pack()

# Display areas
tk.Label(root, text="First online:").pack()
tk.Label(root, textvariable=online_time).pack()

tk.Label(root, text="Offline since:").pack()
tk.Label(root, textvariable=offline_time).pack()

# Footer Frame
footer_frame = tk.Frame(root)
footer_frame.pack(side="bottom", pady=10)

# Custom smaller font for footer
footer_font = font.Font(size=8)

# Footer Label
footer_label = tk.Label(footer_frame, text="Built with ❤️ by rdnsx", font=footer_font)
footer_label.pack(side="left")

root.mainloop()
