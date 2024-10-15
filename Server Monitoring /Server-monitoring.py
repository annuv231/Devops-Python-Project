import psutil
import smtplib
from email.mime.text import MIMEText
import os

# Function to check CPU usage
def check_cpu_usage(threshold=80):
    usage = psutil.cpu_percent(interval=1)
    if usage > threshold:
        return f"High CPU usage detected: {usage}%"
    return f"Current CPU usage: {usage}%"

# Function to check Memory usage
def check_memory_usage(threshold=80):
    memory = psutil.virtual_memory()
    if memory.percent > threshold:
        return f"High Memory usage detected: {memory.percent}%"
    return f"Current Memory usage: {memory.percent}%"

# Function to check Disk usage
def check_disk_usage(threshold=80, path='/'):
    disk = psutil.disk_usage(path)
    if disk.percent > threshold:
        return f"Low Disk space: {disk.percent}% used on {path}"
    return f"Current Disk usage: {disk.percent}% on {path}"

# Main function to monitor the system
def monitor_system():
    alerts = []

    # Gather CPU, Memory, and Disk usage details
    cpu_status = check_cpu_usage()
    memory_status = check_memory_usage()
    disk_status = check_disk_usage()

    # Collect all the usage details
    alerts.append(cpu_status)
    alerts.append(memory_status)
    alerts.append(disk_status)

    # Join the alerts into a single message
    message = '\n'.join(alerts)
    
    # Send the email with the current usages
    print('Current System Resource Usage', message)

if __name__ == "__main__":
    monitor_system()
