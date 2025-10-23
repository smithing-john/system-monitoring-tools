#!/usr/bin/env python3
"""
Display detailed system information
"""

import psutil
from utils import get_system_info, format_bytes, calculate_uptime

def display_system_info():
    """Display comprehensive system information"""
    info = get_system_info()
    boot_time = psutil.boot_time()
    uptime = calculate_uptime(boot_time)
    
    print("\n" + "="*60)
    print("SYSTEM INFORMATION")
    print("="*60)
    print(f"Hostname: {info['hostname']}")
    print(f"Platform: {info['platform']} {info['platform_release']}")
    print(f"Architecture: {info['architecture']}")
    print(f"Processor: {info['processor']}")
    print(f"IP Address: {info['ip_address']}")
    print(f"System Uptime: {uptime}")
    print("="*60)
    
    # CPU Information
    print("\nCPU INFORMATION")
    print("-"*60)
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    cpu_freq = psutil.cpu_freq()
    if cpu_freq:
        print(f"Max Frequency: {cpu_freq.max:.2f} MHz")
        print(f"Current Frequency: {cpu_freq.current:.2f} MHz")
    
    # Memory Information
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    print("\nMEMORY INFORMATION")
    print("-"*60)
    print(f"Total: {format_bytes(mem.total)}")
    print(f"Available: {format_bytes(mem.available)}")
    print(f"Used: {format_bytes(mem.used)} ({mem.percent}%)")
    print(f"Swap Total: {format_bytes(swap.total)}")
    print(f"Swap Used: {format_bytes(swap.used)} ({swap.percent}%)")
    
    # Disk Information
    disk = psutil.disk_usage('/')
    print("\nDISK INFORMATION")
    print("-"*60)
    print(f"Total: {format_bytes(disk.total)}")
    print(f"Used: {format_bytes(disk.used)} ({disk.percent}%)")
    print(f"Free: {format_bytes(disk.free)}")
    print("="*60 + "\n")

if __name__ == "__main__":
    display_system_info()