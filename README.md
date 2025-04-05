# NetMonitor - Python Network Monitoring Tool

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

A lightweight command-line network diagnostic tool written in Python.

## Features

- 🌐 Real-time bandwidth monitoring (KB/s)
- 🔍 Network device scanning (nmap-powered)
- ⚡ Internet speed testing
- 📶 IP address detection (public + local)
- 🖥️ Interactive curses interface
- 📊 Minimal resource usage

## Installation

### Requirements
- Python 3.9+
- Linux system
- Nmap 7.80+

```bash
# Clone repository
git clone https://github.com/lxmwaniky/netmonitor.git
cd netmonitor

# Install dependencies
sudo apt install nmap python3-pip
pip install -r requirements.txt  # or use pipenv
```

## Usage

### Interactive Mode
```bash
./monitor.py
```
Use arrow keys to navigate, Enter to select, Q to quit.

### Command Line Options
```bash
./monitor.py [OPTION]
```

| Option          | Description                      | Example                     |
|-----------------|----------------------------------|-----------------------------|
| `--ip`          | Show IP information              | `./monitor.py --ip`         |
| `--scan`        | Scan local network               | `sudo ./monitor.py --scan`  |
| `--speed`       | Run speed test                   | `./monitor.py --speed`      |
| `--bandwidth`   | Real-time bandwidth monitoring   | `./monitor.py --bandwidth`  |

## Keyboard Controls

| Key          | Action                          |
|--------------|---------------------------------|
| ▲/▼ arrows   | Navigate menu                   |
| Enter        | Select option                   |
| Q            | Quit program                    |
| Ctrl+C       | Force exit                      |

## Screenshots

**Main Menu:**
```
┌──────────────────────────────────────┐
│       NETMONITOR v1.0 - MAIN MENU    │
├──────────────────────────────────────┤
│  > IP Info                           │
│    Network Scan                      │
│    Speed Test                        │
│    Bandwidth Monitor                 │
└──────────────────────────────────────┘
```

**Bandwidth Monitoring:**
```
Download: 845.72 KB/s
Upload: 312.56 KB/s
Total: 15.2 MB transferred
```

## Troubleshooting

**Common Issues:**

1. **Nmap not found**:
   ```bash
   sudo apt install nmap
   ```

2. **Missing dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Permission errors** (for scanning):
   ```bash
   sudo setcap cap_net_raw,cap_net_admin+ep $(which nmap)
   ```

## Development

```bash
# Setup virtual environment
python -m venv venv
source venv/bin/activate

# Install dev requirements
pip install -r requirements-dev.txt

# Run tests
pytest tests/
```

## License

MIT License - See [LICENSE](LICENSE) for details.