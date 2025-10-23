#!/usr/bin/env python3
"""
Unit tests for logging functionality
"""

import unittest
import os
import sys
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logger import setup_logger, log_system_stats

class TestLogger(unittest.TestCase):
    
    def setUp(self):
        """Setup test environment"""
        self.test_log_dir = 'test_logs'
        if not os.path.exists(self.test_log_dir):
            os.makedirs(self.test_log_dir)
    
    def tearDown(self):
        """Cleanup test environment"""
        if os.path.exists(self.test_log_dir):
            for file in os.listdir(self.test_log_dir):
                os.remove(os.path.join(self.test_log_dir, file))
            os.rmdir(self.test_log_dir)
    
    def test_logger_creation(self):
        """Test logger setup"""
        logger = setup_logger('test_monitor')
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, 'test_monitor')
    
    def test_log_system_stats_normal(self):
        """Test logging normal system stats"""
        logger = setup_logger('test_monitor')
        cpu = 50.0
        memory = {'percent': 60.0, 'used_gb': 8.0, 'total_gb': 16.0}
        disk = {'percent': 70.0, 'used_gb': 350.0, 'total_gb': 500.0}
        
        # Should not raise any exceptions
        log_system_stats(logger, cpu, memory, disk)
    
    def test_log_system_stats_high_cpu(self):
        """Test logging high CPU usage"""
        logger = setup_logger('test_monitor')
        cpu = 95.0
        memory = {'percent': 60.0, 'used_gb': 8.0, 'total_gb': 16.0}
        disk = {'percent': 70.0, 'used_gb': 350.0, 'total_gb': 500.0}
        
        with self.assertLogs(logger, level='WARNING') as cm:
            log_system_stats(logger, cpu, memory, disk)
            self.assertTrue(any('High CPU usage' in msg for msg in cm.output))

if __name__ == '__main__':
    unittest.main()