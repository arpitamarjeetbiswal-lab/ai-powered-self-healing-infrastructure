# AI-Powered Self-Healing Cloud Infrastructure

## 📌 Overview
This project implements an AI-powered self-healing system that monitors system resources, detects anomalies using machine learning, and automatically takes corrective actions.

The system continuously collects CPU, memory, and disk usage metrics, applies an Isolation Forest model to identify abnormal behavior, and triggers self-healing actions when required.

---

## 🚀 Key Features
- Real-time system monitoring (CPU, Memory, Disk)
- Machine Learning-based anomaly detection
- Automated self-healing logic
- Action logging for traceability
- Visualization of system metrics and anomalies
- Clean Git-based project structure

---

## 🧠 System Architecture
Monitor → Detect → Decide → Heal → Log → Visualize

---

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Git

---

## 📁 Project Structure
aI_driven_self_healing_infrastructure/
├── scripts/
│ ├── collectmetrices.py
│ ├── detect_anomalies.py
│ ├── visualize_metrics.py
│ └── self_healing.py
├── data/
│ ├── system_metrics.csv
│ └── healing_log.txt
├── README.md
└── .git/

yaml
Copy code

---

## ⚙️ How to Run
1. Collect system metrics  
`python scripts/collectmetrices.py`

2. Detect anomalies  
`python scripts/detect_anomalies.py`

3. Visualize metrics  
`python scripts/visualize_metrics.py`

4. Trigger self-healing  
`python scripts/self_healing.py`

---

## 🎯 Use Cases
- Cloud infrastructure monitoring
- Fault-tolerant systems
- Intelligent DevOps automation
- Predictive system maintenance

---

## 🏆 Outcome
This project demonstrates how AI can be applied to system reliability engineering by enabling automated detection and resolution of infrastructure issues.

---

## 👨‍💻 Author
Arpit Amarjeet Biswal