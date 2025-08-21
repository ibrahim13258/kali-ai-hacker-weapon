# Set proper permissions
chmod 700 ~/ai-assistant
chmod 600 ~/ai-assistant/*.py

# Configure fail2ban for SSH protection
sudo apt install fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban

# Enable system logging
sudo mkdir -p /var/log/ai-assistant
