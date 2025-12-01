import tkinter as tk
from tkinter import ttk
import psutil

# Step 1: Create the GUI

root = tk.Tk()
root.title("Linux System Monitor")

# Step 2: Create Notebook widget to seperate categories of information

notebook = ttk.Notebook(root)
notebook.pack()

# Step 3: Create Frames

cpu_frame = ttk.Frame(notebook, padding=10)
ram_frame = ttk.Frame(notebook, padding=10)
disk_frame = ttk.Frame(notebook, padding=10)
network_frame = ttk.Frame(notebook, padding=10)

# Step 4: Add Frames to Notebook

notebook.add(cpu_frame, text="CPU Info")
notebook.add(ram_frame, text="RAM Info")
notebook.add(disk_frame, text="Disk Info")
notebook.add(network_frame, text="Network Info")

# Step 5: Create Labels for the Frames

# Add CPU Info Labels

cpu_percent_label = ttk.Label(cpu_frame)
cpu_percent_label.pack()

# Add RAM Info Labels

ram_percent_label = ttk.Label(ram_frame)
ram_percent_label.pack()

# Add Disk Info Labels

disk_percent_label = ttk.Label(disk_frame)
disk_percent_label.pack()

# Add Network Info Labels

network_label = ttk.Label(network_frame)
network_label.pack()

# Step 6: Populate Labels with real time information


def update_labels():
    # CPU Info
    cpu_percent = psutil.cpu_percent()
    cpu_percent_label.config(text=f"CPU Usage: {cpu_percent}%")

    # RAM Info
    ram_percent = psutil.virtual_memory().percent
    ram_percent_label.config(text=f"RAM Usage: {ram_percent}%")

    # Disk Info
    disk_percent = psutil.disk_usage("/").percent
    disk_percent_label.config(text=f"Disk Usage: {disk_percent}%")

    # Network Info
    network_stats = psutil.net_io_counters()
    network_label.config(
        text=f"Network Stats:\nBytes Sent: {network_stats.bytes_sent}\nBytes Recieved: {network_stats.bytes_recv}"
    )

    # Refresh info every second
    root.after(1000, update_labels)


update_labels()

root.mainloop()
