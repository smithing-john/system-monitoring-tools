#!/usr/bin/env python3
"""
Network monitoring module
Tracks bandwidth usage and connection statistics
"""

import psutil
import time
from datetime import datetime

def get_network_stats():
    """Get current network statistics"""
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

def bytes_to_mb(bytes_value):
    """Convert bytes to megabytes"""
    return round(bytes_value / (1024**2), 2)

def monitor_bandwidth(interval=5):
    """Monitor bandwidth usage over time"""
    print("Starting network monitor...")
    print("Press Ctrl+C to stop\n")
    
    prev_stats = get_network_stats()
    
    try:
        while True:
            time.sleep(interval)
            curr_stats = get_network_stats()
            
            sent_mb = bytes_to_mb(curr_stats['bytes_sent'] - prev_stats['bytes_sent'])
            recv_mb = bytes_to_mb(curr_stats['bytes_recv'] - prev_stats['bytes_recv'])
            
            timestamp = datetime.now().strftime('%H:%M:%S')
            print(f"[{timestamp}] ↑ {sent_mb} MB/s | ↓ {recv_mb} MB/s")
            
            prev_stats = curr_stats
            
    except KeyboardInterrupt:
        print("\nNetwork monitoring stopped.")

if __name__ == "__main__":
    monitor_bandwidth()