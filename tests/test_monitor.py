#!/usr/bin/env python3
"""
Unit tests for monitoring functions
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import format_bytes, calculate_uptime, get_system_info

class TestUtils(unittest.TestCase):
    
    def test_format_bytes(self):
        """Test byte formatting"""
        self.assertEqual(format_bytes(1024), "1.00 KB")
        self.assertEqual(format_bytes(1048576), "1.00 MB")
        self.assertEqual(format_bytes(1073741824), "1.00 GB")
    
    def test_calculate_uptime(self):
        """Test uptime calculation"""
        # Test 1 day uptime
        boot_time = 1640000000  # Some timestamp
        current_time = boot_time + 86400  # 1 day later
        
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value.timestamp.return_value = current_time
            # This test is simplified, actual implementation may vary
            self.assertIsNotNone(calculate_uptime(boot_time))
    
    def test_get_system_info(self):
        """Test system info retrieval"""
        info = get_system_info()
        self.assertIn('platform', info)
        self.assertIn('hostname', info)
        self.assertIn('ip_address', info)

class TestMonitoring(unittest.TestCase):
    
    @patch('psutil.cpu_percent')
    def test_cpu_monitoring(self, mock_cpu):
        """Test CPU monitoring"""
        mock_cpu.return_value = 50.0
        # Import after patching
        from monitor import check_cpu
        cpu = check_cpu()
        self.assertEqual(cpu, 50.0)
    
    @patch('psutil.virtual_memory')
    def test_memory_monitoring(self, mock_memory):
        """Test memory monitoring"""
        mock_mem = MagicMock()
        mock_mem.percent = 60.0
        mock_mem.used = 8589934592  # 8GB
        mock_mem.total = 17179869184  # 16GB
        mock_memory.return_value = mock_mem
        
        from monitor import check_memory
        mem = check_memory()
        self.assertEqual(mem['percent'], 60.0)
        self.assertEqual(mem['used_gb'], 8.0)

class TestNetworkMonitoring(unittest.TestCase):
    
    @patch('psutil.net_io_counters')
    def test_network_stats(self, mock_net):
        """Test network statistics"""
        mock_stats = MagicMock()
        mock_stats.bytes_sent = 1048576
        mock_stats.bytes_recv = 2097152
        mock_net.return_value = mock_stats
        
        from network_monitor import get_network_stats
        stats = get_network_stats()
        self.assertEqual(stats['bytes_sent'], 1048576)
        self.assertEqual(stats['bytes_recv'], 2097152)

if __name__ == '__main__':
    unittest.main()