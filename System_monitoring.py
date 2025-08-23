import psutil
import time
import os

def clear_screen():
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\") 

    print("========== System Monitor ==========")
    print(f"CPU Usage   : {cpu}%")
    print(f"RAM Usage   : {ram.percent}% ({ram.used / (1024**3):.2f} GB used of {ram.total / (1024**3):.2f} GB)")
    print(f"Disk Usage  : {disk.percent}% ({disk.used / (1024**3):.2f} GB used of {disk.total / (1024**3):.2f} GB)")
    print("====================================")

if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            display_system_stats()
            time.sleep(5)  # Update every 5 seconds
    except KeyboardInterrupt:
        print("\nExiting System Monitor...")
