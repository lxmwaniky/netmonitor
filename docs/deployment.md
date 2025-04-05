# Deployment Guide

## 1. Docker Deployment
```bash
# Production
docker run -d \
  --name netmonitor \
  --network host \
  --privileged \
  --restart unless-stopped \
  ghcr.io/lxmwaniky/netmonitor:latest

# With custom config
docker run -v ./config:/app/config ...
```

## 2. Bare Metal Installation
```bash
# Install dependencies
sudo apt install nmap python3-pip

# Install package
pip install git+https://github.com/lxmwaniky/netmonitor.git

# Run
netmonitor --ip
```

## 3. Kubernetes (Helm Chart)
```bash
helm install netmonitor ./charts \
  --set networkPolicy.enabled=true
```