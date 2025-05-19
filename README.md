# 🔐 Web Log Intrusion Detection System (IDS)

This project is a basic Intrusion Detection System (IDS) that analyzes Apache/Nginx web server access logs to detect suspicious activities such as brute force login attempts, directory traversal attacks, and high-frequency request spikes.

---

## 🚀 Features

- ✅ Parses real Apache-style log files using Python
- 🔍 Detects:
  - Brute force login attempts (`401` / `403`)
  - Directory traversal patterns (`../`)
  - High request rate from specific IPs
- 📊 Uses `pandas` for data handling and analysis
- 💡 Easy to extend for more advanced detections

---

## 📁 Project Structure
web-log-ids/
├── main.py # Main detection script
├── sample_logs/
│ └── access.log # Example log file
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore


---

## 🛠️ How to Use

### 1. Clone this repository

```bash
git clone https://github.com/vardhan232/web-log-ids.git
cd web-log-ids


pip install -r requirements.txt

python3 main.py




=== Brute Force IPs ===
192.168.1.10    4

=== Directory Traversal Attempts ===
192.168.1.20 GET /../../etc/passwd

=== Top 5 IPs by Request Count ===
192.168.1.10    6
192.168.1.30    2
...


---

Let me know once it’s added! I can also help you make a GitHub project banner or badge if you want to make the repo stand out visually.

