#!/bin/bash

# Mini Project 01: Linux Sysadmin Automation Kit
# Description: Automated server health monitoring script
# Author: Yash Redkar

LOG_DIR="./logs"
LOG_FILE="$LOG_DIR/server_health.log"

mkdir -p "$LOG_DIR"

SERVICES=("ssh" "cron" "docker")

echo "Server Health Check Report" >> "$LOG_FILE"
echo "Date and Time : $(date)" >> "$LOG_FILE"
echo "Hostname      : $(hostname)" >> "$LOG_FILE"
echo "Current User  : $(whoami)" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

echo "Disk Usage:" >> "$LOG_FILE"
df -h >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

echo "RAM Usage:" >> "$LOG_FILE"
if command -v free >/dev/null 2>&1
then
    free -h >> "$LOG_FILE"
else
    echo "RAM usage command is not available in this terminal environment." >> "$LOG_FILE"
fi
echo "" >> "$LOG_FILE"

echo "CPU Load Average:" >> "$LOG_FILE"
uptime >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

echo "Top Running Processes:" >> "$LOG_FILE"
ps aux | head -n 6 >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

echo "Service Status:" >> "$LOG_FILE"

for service in "${SERVICES[@]}"
do
    if command -v systemctl >/dev/null 2>&1
    then
        if systemctl is-active --quiet "$service" 2>/dev/null
        then
            echo "$service : Running" >> "$LOG_FILE"
        else
            echo "$service : Not running or not installed" >> "$LOG_FILE"
        fi
    else
        echo "$service : Service check requires Linux systemctl support" >> "$LOG_FILE"
    fi
done

echo "" >> "$LOG_FILE"

echo "Logged-in Users:" >> "$LOG_FILE"
if command -v who >/dev/null 2>&1
then
    who >> "$LOG_FILE"
else
    echo "No logged-in user details available." >> "$LOG_FILE"
fi
echo "" >> "$LOG_FILE"

echo "Health check completed successfully." >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

echo "Report generated successfully: $LOG_FILE"
