#!/bin/bash

# LogHawk Installation Script
# Requires: Ubuntu/Debian Linux with sudo privileges

# =============================================
# 1. Install Dependencies
# =============================================
echo "[*] Installing dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip python3-dev git
sudo pip3 install pyyaml python-dateutil

# =============================================
# 2. Download LogHawk
# =============================================
echo "[*] Downloading LogHawk..."
sudo git clone https://github.com/yourusername/LogHawk.git /opt/LogHawk
sudo chown -R $(whoami):$(whoami) /opt/LogHawk

# =============================================
# 3. Configure LogHawk
# =============================================
echo "[*] Setting up configuration..."

# Create alert log with proper permissions
sudo touch /var/log/loghawk_alerts.log
sudo chown root:adm /var/log/loghawk_alerts.log
sudo chmod 640 /var/log/loghawk_alerts.log

# Create default rules file
sudo tee /opt/LogHawk/configs/default_rules.yaml > /dev/null <<'EOL'
rules:
  - name: "SSH Brute Force"
    pattern: "Failed password for .* from <IP>"
    threshold: 5
    severity: "high"
    
  - name: "Critical System Error"
    pattern: "(ERROR|CRITICAL)"
    severity: "critical"
EOL

# =============================================
# 4. Setup Cron Job (Runs every 10 minutes)
# =============================================
echo "[*] Configuring cron job..."
(crontab -l 2>/dev/null; echo "*/10 * * * * /usr/bin/sudo /usr/bin/python3 /opt/LogHawk/src/loghawk.py -l /var/log/auth.log -c /opt/LogHawk/configs/default_rules.yaml >> /var/log/loghawk.log 2>&1") | sudo crontab -

# =============================================
# 5. Create Systemd Service (Alternative)
# =============================================
echo "[*] Creating systemd service..."
sudo tee /etc/systemd/system/loghawk.service > /dev/null <<'EOL'
[Unit]
Description=LogHawk Security Monitor
After=network.target

[Service]
User=root
ExecStart=/usr/bin/sudo /usr/bin/python3 /opt/LogHawk/src/loghawk.py -l /var/log/auth.log -d
Restart=always

[Install]
WantedBy=multi-user.target
EOL

# =============================================
# 6. Configure Log Rotation
# =============================================
echo "[*] Setting up log rotation..."
sudo tee /etc/logrotate.d/loghawk > /dev/null <<'EOL'
/var/log/loghawk*.log {
    daily
    rotate 7
    compress
    missingok
    notifempty
    create 640 root adm
}
EOL

# =============================================
# 7. Start Services
# =============================================
echo "[*] Starting services..."
sudo systemctl daemon-reload
sudo systemctl enable loghawk.service
sudo systemctl start loghawk.service

# =============================================
# 8. Sudoers Configuration (Secure Access)
# =============================================
echo "[*] Configuring sudo privileges..."
sudo tee /etc/sudoers.d/loghawk > /dev/null <<'EOL'
%adm ALL=(root) NOPASSWD: /usr/bin/tail /var/log/*
%adm ALL=(root) NOPASSWD: /usr/bin/python3 /opt/LogHawk/src/loghawk.py
EOL

# =============================================
# 9. Verification
# =============================================
echo "[*] Verifying installation..."
sudo python3 /opt/LogHawk/src/loghawk.py -l /var/log/auth.log --test

echo -e "\n[+] LogHawk installation complete!"
echo "    - Main directory: /opt/LogHawk"
echo "    - Alerts log: /var/log/loghawk_alerts.log"
echo "    - Config files: /opt/LogHawk/configs/"
echo "    - Run manually: sudo python3 /opt/LogHawk/src/loghawk.py -l /path/to/logfile"
