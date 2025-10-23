#!/usr/bin/env python3
"""
System Monitoring Tool
Tracks CPU, memory, disk, and network usage with logging
"""

import psutil
import time
import yaml
from datetime import datetime
from logger import setup_logger, log_system_stats

def load_config():
    """Load configuration from config.yaml"""
    try:
        with open('config.yaml', 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print("Config file not found. Using defaults.")
        return {'monitoring': {'interval': 5}}

def check_cpu():
    """Get CPU usage percentage"""
    return psutil.cpu_percent(interval=1)

def check_memory():
    """Get memory usage statistics"""
    mem = psutil.virtual_memory()
    return {
        'percent': mem.percent,
        'used_gb': round(mem.used / (1024**3), 2),
        'total_gb': round(mem.total / (1024**3), 2)
    }

def check_disk():
    """Get disk usage statistics"""
    disk = psutil.disk_usage('/')
    return {
        'percent': disk.percent,
        'used_gb': round(disk.used / (1024**3), 2),
        'total_gb': round(disk.total / (1024**3), 2)
    }

def display_stats(cpu, memory, disk):
    """Display formatted system statistics"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n{'='*50}")
    print(f"System Monitor - {timestamp}")
    print(f"{'='*50}")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory: {memory['used_gb']}GB / {memory['total_gb']}GB ({memory['percent']}%)")
    print(f"Disk: {disk['used_gb']}GB / {disk['total_gb']}GB ({disk['percent']}%)")
    print(f"{'='*50}")

def main():
    """Main monitoring loop"""
    config = load_config()
    interval = config.get('monitoring', {}).get('interval', 5)
    logger = setup_logger()
    
    print(f"Starting system monitor (interval: {interval}s)")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            cpu = check_cpu()
            memory = check_memory()
            disk = check_disk()
            display_stats(cpu, memory, disk)
            log_system_stats(logger, cpu, memory, disk)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")
        logger.info("Monitoring session ended")

if __name__ == "__main__":
    main()