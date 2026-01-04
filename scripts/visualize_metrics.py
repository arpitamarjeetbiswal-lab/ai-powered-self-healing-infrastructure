import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Load data
data = pd.read_csv("../data/system_metrics.csv")

features = data[["cpu_percent", "memory_percent", "disk_percent"]]

# Train model (same logic)
model = IsolationForest(contamination=0.05, random_state=42)
data["anomaly"] = model.fit_predict(features)

# Convert timestamp
data["timestamp"] = pd.to_datetime(data["timestamp"])

plt.figure(figsize=(12, 6))

plt.plot(data["timestamp"], data["cpu_percent"], label="CPU Usage")
plt.plot(data["timestamp"], data["memory_percent"], label="Memory Usage")
plt.plot(data["timestamp"], data["disk_percent"], label="Disk Usage")

# Highlight anomalies
anomalies = data[data["anomaly"] == -1]
plt.scatter(
    anomalies["timestamp"],
    anomalies["cpu_percent"],
    marker="x",
    s=100,
    label="Anomaly"
)

plt.xlabel("Time")
plt.ylabel("Usage (%)")
plt.title("System Metrics with Detected Anomalies")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
