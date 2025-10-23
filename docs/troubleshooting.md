# Troubleshooting Guide

Common issues and solutions for system monitoring tools.

## Installation Issues

### psutil installation fails
```bash
# On Ubuntu/Debian
sudo apt-get install python3-dev

# On macOS
brew install python3

# Then retry
pip install psutil --break-system-packages
```

### ImportError: No module named 'yaml'
```bash
pip install PyYAML --break-system-packages
```

## Runtime Issues

### Permission denied when accessing system metrics
Run with sudo on Linux systems:
```bash
sudo python3 monitor.py
```

### Logs directory not created
Check write permissions in current directory. The script needs to create a `logs/` folder.

### High CPU usage from monitoring script
Increase the monitoring interval in `config.yaml`:
```yaml
monitoring:
  interval: 10  # Increase from 5 to 10 seconds
```

## Configuration Issues

### YAML parsing errors
Ensure proper indentation in `config.yaml`. Use spaces, not tabs.

### Alerts not working
1. Check email configuration
2. Verify SMTP settings
3. Test with a simple alert first

## Performance Issues

### Script consuming too much memory
Reduce retention days for logs:
```yaml
logging:
  retention_days: 7  # Reduce from 30
```

### Disk filling up with logs
Run log cleanup:
```bash
find logs/ -name "*.log" -mtime +7 -delete
```

## Common Error Messages

### "Connection refused" on network monitoring
Check if network interfaces are accessible. May need elevated privileges.

### "Disk usage > 100%"
This is a bug in some psutil versions. Update psutil:
```bash
pip install --upgrade psutil
```

## Getting Help

If you encounter issues not listed here:
1. Check the GitHub issues page
2. Review system logs in `logs/` directory
3. Run with debug logging enabled
4. Include error messages when asking for help

## Debug Mode

Enable verbose logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---
*Last updated: October 2025*