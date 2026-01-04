import pandas as pd
from sklearn.ensemble import IsolationForest

# Load system metrics
data = pd.read_csv("../data/system_metrics.csv")

# Select features
features = data[["cpu_percent", "memory_percent", "disk_percent"]]

# Train Isolation Forest
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

data["anomaly"] = model.fit_predict(features)

# -1 = anomaly, 1 = normal
anomalies = data[data["anomaly"] == -1]

print("Total records:", len(data))
print("Anomalies detected:", len(anomalies))
print("\nSample anomalies:")
print(anomalies.head())
