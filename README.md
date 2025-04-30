Loghawk 🦅
Automated Log Monitoring for Security Teams

Python License

🔍 What is Loghawk?
LogHawk is a lightweight, open-source tool that automatically scans log files for security threats like:

Failed login attempts (SSH, web apps)

Brute force attacks

Suspicious cron jobs

Critical system errors

Unusual traffic spikes

Why use it?

Catch threats before they become incidents

No expensive SIEM required

Customizable detection rules

Designed for security teams and sysadmins

🚀 Installation
Requirements
Linux/macOS

Python 3.6+

sudo access (for reading system logs)

1. Install Dependencies
bash
sudo apt update && sudo apt install -y python3 python3-pip git
2. Download Loghawk
bash
git clone [https://github.com/saurabhalang/Loghawk]
cd LogHawk
pip3 install -r requirements.txt
3. Verify Installation
bash
python3 src/loghawk.py --version
✅ Expected output: Loghawk v1.0

🛠 How to Use
Basic Scan
bash
sudo python3 src/loghawk.py -l /var/log/auth.log
With Custom Rules
bash
sudo python3 src/loghawk.py -l /var/log/nginx/access.log -c configs/web_rules.yaml
Continuous Monitoring
bash
sudo python3 src/loghawk.py -l /var/log/syslog -d  # Runs as a daemon
📋 Example Output
plaintext
[2025-04-29 14:30:01] 🚨 SSH Brute Force (Severity: HIGH)  
Apr 04 14:30:01 server sshd[1234]: Failed password for root from 192.168.1.100  

[2025-04-29 14:30:02] 🚨 Suspicious Cron Job (Severity: CRITICAL)  
Apr 04 14:30:02 server CRON[5678]: (root) CMD (curl http://malicious.site)  
Alerts are also saved to: /var/log/loghawk_alerts.log

⏰ Automate with Cron
To run Loghawk every 10 minutes:

Edit crontab:

bash
sudo crontab -e
Add this line:

bash
*/10 * * * * /usr/bin/python3 /path/to/Loghawk/src/loghawk.py -l /var/log/auth.log >> /var/log/loghawk.log 2>&1
🛡 Customize Detection Rules
Edit configs/default_rules.yaml:

yaml
rules:
  - name: "SQL Injection Attempt"
    pattern: ".*(union select|1=1|sleep\().*"
    severity: "critical"
  
  - name: "Traffic Spike"
    pattern: "<IP>"
    threshold: 100  # Alert if IP hits 100+ times/hour
