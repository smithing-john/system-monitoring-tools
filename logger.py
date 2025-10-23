#!/usr/bin/env python3
"""
Logging utility for system monitoring
"""

import logging
from datetime import datetime
import os

def setup_logger(name='system_monitor'):
    """Setup and configure logger"""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # File handler
    log_file = f"logs/monitor_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def log_system_stats(logger, cpu, memory, disk):
    """Log system statistics"""
    logger.info(f"CPU: {cpu}% | Memory: {memory['percent']}% | Disk: {disk['percent']}%")
    
    if cpu > 90:
        logger.warning(f"High CPU usage detected: {cpu}%")
    if memory['percent'] > 85:
        logger.warning(f"High memory usage detected: {memory['percent']}%")
    if disk['percent'] > 90:
        logger.warning(f"High disk usage detected: {disk['percent']}%")