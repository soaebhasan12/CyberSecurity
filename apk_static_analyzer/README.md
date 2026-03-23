# 🚀 APK Static Analyzer (Using Androguard)

A lightweight static analysis tool for Android APK files built with **Python** and **Androguard**.

This project scans APK files and generates a structured security report highlighting:

- Dangerous permissions
- Suspicious API usage
- Hardcoded URLs / IP addresses
- Basic risk indicators


---
## 🎯 Project Objective

**Input:** `app.apk`  
**Output:** JSON security report  

The analyzer performs static inspection of the APK without executing it.

---

## 🏗️ Project Structure

```

apk_static_analyzer/
│
├── main.py
├── config.py
├── analyzer/
│   ├── apk_loader.py
│   ├── permission_analyzer.py
│   ├── string_analyzer.py
│   ├── api_analyzer.py
│   ├── report_generator.py
│
├── reports/
├── samples/
│   └── test.apk
│
└── requirements.txt

````

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
````

---

## ▶️ Usage

```bash
python main.py
```

Output report will be generated inside:

```
reports/output.json
```

---

## 🔍 Features

* Static APK parsing using Androguard
* Dangerous permission detection
* Suspicious API usage detection
* Hardcoded URL discovery
* Modular and extensible architecture

---

## 📊 Sample Output

```json
{
    "dangerous_permissions": [
        "android.permission.SEND_SMS"
    ],
    "suspicious_strings": [
        "http://malicious-site.com"
    ],
    "suspicious_api_usage": [
        "SmsManager->sendTextMessage"
    ]
}
```

---

## 🧠 Concepts Covered

* Static Code Analysis
* Rule-Based Security Detection
* Pattern Matching
* Android Permission Model
* API Signature Analysis
* Modular Software Architecture
* JSON Report Generation

---

## 🔥 Future Improvements

* Risk Scoring System
* Control Flow Graph (CFG) generation
* Batch APK scanning support
* Command-line argument support
* SQLite integration for result storage
* Web dashboard using Flask
* Malware family classification
* CI/CD integration for automated scanning

---

## 📌 Why This Project?

This project demonstrates:

* Python proficiency
* Android security understanding
* Static analysis knowledge
* Clean software design
* Security automation fundamentals

---

## ⚠️ Disclaimer

This tool is for educational and research purposes only.