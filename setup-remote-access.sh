#!/bin/bash

# Passwordless sudo for specific commands
echo "$USER ALL=(ALL) NOPASSWD: /usr/bin/apt, /usr/bin/systemctl, /usr/sbin/iptables" | sudo tee /etc/sudoers.d/ai-assistant

# Enable remote services
sudo systemctl enable ssh
sudo systemctl start ssh

# Configure VNC
vncserver :1 -geometry 1920x1080 -depth 24

# Set up firewall rules for remote access
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 5900:5910 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 3389 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 5000 -j ACCEPT

# Save iptables rules
sudo iptables-save | sudo tee /etc/iptables/rules.v4
