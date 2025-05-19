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

