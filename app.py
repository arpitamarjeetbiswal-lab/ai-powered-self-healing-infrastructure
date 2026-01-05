import streamlit as st

st.set_page_config(
    page_title="AI System Health Analyzer",
    layout="centered"
)

st.title("🛠️ AI System Health Analyzer")
st.subheader("Detect abnormal CPU, memory, and disk behavior using machine learning.")

import pandas as pd
import matplotlib.pyplot as plt

# Load demo data
demo_data = pd.read_csv("data/system_metrics.csv")

st.subheader("📊 Demo: System Metrics with Anomaly Detection")



from sklearn.ensemble import IsolationForest

# Run anomaly detection
features = demo_data[["cpu_percent", "memory_percent", "disk_percent"]]
model = IsolationForest(contamination=0.05, random_state=42)
demo_data["anomaly"] = model.fit_predict(features)
anomalies = demo_data[demo_data["anomaly"] == -1]

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(demo_data["cpu_percent"], label="CPU %")
ax.plot(demo_data["memory_percent"], label="Memory %")
ax.plot(demo_data["disk_percent"], label="Disk %")

# Highlight anomalies
ax.scatter(
    anomalies.index,
    anomalies["cpu_percent"],
    color="red",
    label="Anomaly",
    zorder=5
)

ax.set_ylabel("Usage (%)")
ax.set_xlabel("Time")
ax.legend()

st.pyplot(fig)
st.markdown("### 🧠 System Insight")

if len(anomalies) == 0:
    st.success("System behavior appears normal. No anomalies detected.")
else:
    st.warning(f"{len(anomalies)} anomaly detected.")
    st.write(
        "This anomaly may indicate an unusual spike in resource usage. "
        "Suggested action: Monitor the system or investigate running processes."
    )
    st.divider()

st.markdown("### 📂 Try Your Own Data")

uploaded_file = st.file_uploader(
    "Upload a CSV with cpu_percent, memory_percent, disk_percent columns",
    type=["csv"]
)
st.divider()

if uploaded_file is not None:
    demo_data = pd.read_csv(uploaded_file)

    features = demo_data[["cpu_percent", "memory_percent", "disk_percent"]]
    model = IsolationForest(contamination=0.05, random_state=42)
    demo_data["anomaly"] = model.fit_predict(features)

    anomalies = demo_data[demo_data["anomaly"] == -1]

    st.success("Custom data loaded. Scroll up to see updated results.")
    st.divider()

st.markdown("### 🔄 Re-run Analysis")

if st.button("Re-run Anomaly Detection"):
    features = demo_data[["cpu_percent", "memory_percent", "disk_percent"]]
    model = IsolationForest(contamination=0.05, random_state=42)
    demo_data["anomaly"] = model.fit_predict(features)
    anomalies = demo_data[demo_data["anomaly"] == -1]

    st.success("Analysis re-run successfully. Scroll up to view results.")

    st.markdown("---")
st.caption("Built by Arpit Amarjeet Biswal • AI-Powered Self-Healing Infrastructure Demo")

