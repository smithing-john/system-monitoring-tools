# System Monitoring Tools

A comprehensive collection of Python scripts for monitoring system performance, resource utilization, and network activity.

## Features
- Real-time CPU and memory monitoring
- Disk usage tracking with alerts
- Network bandwidth monitoring
- Detailed system information display
- Configurable alert thresholds
- Automatic logging to files

## Requirements
- Python 3.8+
- psutil
- pyyaml

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### Basic System Monitoring
```bash
python monitor.py
```

### Network Monitoring
```bash
python network_monitor.py
```

### System Information
```bash
python system_info.py
```

## Configuration
Edit `config.yaml` to customize:
- Monitoring intervals
- Alert thresholds
- Enabled metrics
- Logging preferences


## License
MIT License - See LICENSE file for details

## Contributing
This is a personal project for my homelab setup. Feel free to fork and modify for your own use.

## Notes
Just some utilities I use for monitoring my personal systems. Nothing fancy, but gets the job done.

## Security

This project does not store any sensitive information in the repository.
All credentials and private data should be stored locally or in environment variables.

See `.gitignore` for excluded file patterns.