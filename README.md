# 🔐 OWASP Quick Auditor

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Linux-orange?style=flat-square)
![OWASP](https://img.shields.io/badge/OWASP-Top%2010-red?style=flat-square)

A Python-based web security auditing tool that checks for **OWASP Top 10** 
vulnerabilities — with a unique **Cyber Mentor Mode** that explains every 
finding in plain English and provides ready-to-use fix code snippets.

> ⚡ Built for beginners, useful for professionals.

---

## 📸 Screenshots

### Terminal Output
<img width="1920" height="936" alt="Tool_execution" src="https://github.com/user-attachments/assets/7666b0a9-78ba-488d-ba47-490aa26ff849" />
<img width="1920" height="936" alt="tool_execution2" src="https://github.com/user-attachments/assets/a1949dd2-0c64-4eb7-a37c-1ae8db378eae" />


### HTML Report
![Report](screenshots/report.png)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🛡️ Security Headers | Detects missing CSP, X-Frame-Options, HSTS, and more |
| 🍪 Cookie Flags | Checks for missing Secure, HttpOnly, SameSite flags |
| 📂 Directory Listing | Scans for exposed directories like /admin, /.git |
| 💉 XSS Detection | Tests parameters for reflected XSS payloads |
| 🗄️ SQL Injection | Detects SQL error-based injection points |
| 🌐 CORS Misconfiguration | Finds wildcard and credential-leaking CORS headers |
| 🤖 Cyber Mentor Mode | Explains every finding + gives fix code snippets |
| 📊 HTML Report | Dark-themed, color-coded severity report |

---

## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/SumitRaj511/OWASP-quick-auditor.git
cd OWASP-quick-auditor

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install requests colorama jinja2
```

---

## ▶️ Usage

```bash
# Basic scan
python3 auditor.py https://target.com

# Scan with parameters (for XSS/SQLi testing)
python3 auditor.py http://testphp.vulnweb.com searchFor,artist
```

> ⚠️ **Only test on websites you own or have written permission to test.**  
> Legal practice target: `http://testphp.vulnweb.com`

---

## 📁 Project Structure
owasp-auditor/
├── auditor.py          # Main runner
├── advisor.py          # Cyber Mentor Mode (fix suggestions)
├── reporter.py         # HTML report generator
└── checks/
├── headers.py      # Security header checks
├── cookies.py      # Cookie flag checks
├── directory.py    # Directory listing checks
├── xss.py          # XSS reflection checks
├── sqli.py         # SQL injection checks
└── cors.py         # CORS misconfiguration checks
---

## 🧠 What Makes This Different

Most scanners just show raw findings.  
This tool acts like a **mentor** — for every vulnerability found, it explains:
- **What it is** in plain English
- **Why it's dangerous**
- **How to fix it** with a real code snippet

---

## 🎯 Tech Stack

- **Python 3** — Core language
- **Requests** — HTTP requests
- **Colorama** — Colored terminal output
- **Jinja2** — HTML report templating

---

## ⚠️ Disclaimer

This tool is for **educational and authorized testing purposes only**.  
The developer is not responsible for any misuse.

---

## 👤 Author

**Sumit Raj**  
[GitHub](https://github.com/SumitRaj511)
