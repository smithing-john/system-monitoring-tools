#!/usr/bin/env python3
"""
Utility functions for system monitoring
"""

import platform
import socket
from datetime import datetime

def get_system_info():
    """Get basic system information"""
    return {
        'platform': platform.system(),
        'platform_release': platform.release(),
        'platform_version': platform.version(),
        'architecture': platform.machine(),
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'processor': platform.processor()
    }

def format_bytes(bytes_value):
    """Format bytes into human-readable format"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} PB"

def format_timestamp(format_str='%Y-%m-%d %H:%M:%S'):
    """Get formatted current timestamp"""
    return datetime.now().strftime(format_str)

def calculate_uptime(boot_time):
    """Calculate system uptime from boot time"""
    uptime_seconds = datetime.now().timestamp() - boot_time
    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    return f"{days}d {hours}h {minutes}m"