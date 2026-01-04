import pandas as pd
from sklearn.ensemble import IsolationForest
from datetime import datetime

# Load metrics
data = pd.read_csv("../data/system_metrics.csv")

features = data[["cpu_percent", "memory_percent", "disk_percent"]]

# Train model
model = IsolationForest(contamination=0.05, random_state=42)
data["anomaly"] = model.fit_predict(features)

# Check latest record
latest = data.iloc[-1]

if latest["anomaly"] == -1:
    action = "RESTART_SERVICE"
    status = "HEALED"
else:
    action = "NONE"
    status = "NORMAL"

# Log healing action
with open("../data/healing_log.txt", "a") as log:
    log.write(
        f"{datetime.now().isoformat()} | "
        f"CPU={latest['cpu_percent']} | "
        f"ACTION={action} | STATUS={status}\n"
    )

print("Self-healing status:", status)
print("Action taken:", action)
