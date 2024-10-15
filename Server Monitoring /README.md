# Automated Server Monitoring Script

This project implements an automated server monitoring script using Python. The script monitors system resources, including CPU, RAM, and disk usage, and sends alerts via email when usage exceeds specified thresholds. 

## Features

- Monitor CPU, RAM, and disk usage in real-time.
- Send email alerts when resource usage exceeds predefined thresholds.
- Log resource usage statistics for historical reference.
- Easy to configure and extend.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `psutil` library for system resource monitoring
- An email account (e.g., Gmail) for sending alerts

### Install Required Libraries

To install the required libraries, you can use the following command:

```bash
pip install psutil
