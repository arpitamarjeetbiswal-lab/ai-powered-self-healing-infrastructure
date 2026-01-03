import psutil
import time
import csv
from datetime import datetime
import os

# Ensure data directory exists
os.makedirs("../data", exist_ok=True)

with open("../data/system_metrics.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["timestamp", "cpu_percent", "memory_percent", "disk_percent"])

    while True:
        timestamp = datetime.now().isoformat()
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage("/").percent

        writer.writerow([timestamp, cpu, memory, disk])
        print(f"[{timestamp}] CPU={cpu}% MEM={memory}% DISK={disk}%")

        time.sleep(5)

