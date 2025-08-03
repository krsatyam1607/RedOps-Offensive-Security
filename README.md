# 🔴 RedOps: Offensive Security Simulation Framework

RedOps is an open-source Python framework to simulate offensive security engagements. It automates scanning, exploitation, payload generation, and reporting — modular, scriptable, and extensible.

---

## 📌 Features

| Module        | Description |
|---------------|-------------|
| 🕵️ Scanner         | Nmap, Nikto, Gobuster wrapper |
| 💥 Exploit Engine  | (Coming Soon) SQLi, XSS, LFI auto-exploitation |
| 🐚 Payload Gen     | (Coming Soon) Bash, PHP, Python reverse shells |
| 📜 Report Builder  | (Coming Soon) Markdown → PDF report with CVSS |
| 🔗 Automation      | Full attack chain execution |
| 🖥️ Interface       | CLI-first, Flask Web UI (optional in later phase) |

---

## 🗂️ Project Structure

```
RedOps/
├── core/
│   ├── scanner.py        # Recon wrapper (Nmap, Nikto, Gobuster)
│   ├── exploit_web.py    # (Coming Soon)
│   ├── payload_gen.py    # (Coming Soon)
│   ├── report_gen.py     # (Coming Soon)
│   └── utils.py
├── ui/
│   └── cli.py
├── reports/              # Scan outputs
├── payloads/             # Reverse shell payloads
├── logs/                 # Runtime logs
├── venv/                 # Virtual environment
├── README.md
├── TODO.md
└── requirements.txt
```

---

## ⚙️ Setup Instructions

### 🧪 Prerequisites

- Python 3.10+ (use `python3 --version`)
- Git, Nmap, Nikto, Gobuster
- WSL2 with Ubuntu or Kali
- Optional: VirtualBox + Metasploitable2/DVWA

### 🧰 Install tools

```bash
sudo apt update && sudo apt install nmap nikto gobuster dirb git python3-full python3-venv
```

### 🧱 Setup Environment

```bash
git clone https://github.com/krsatyam1607/RedOps-Offensive-Security.git
cd RedOps-Offensive-Security

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🚀 Scanner Module (Week 2)

### 🔹 Usage

```bash
python3 core/scanner.py -t http://192.168.1.52/DVWA -m all
```

| Option | Description |
|--------|-------------|
| `-t`   | Target IP or URL |
| `-m`   | Module to run: `nmap`, `nikto`, `gobuster`, `all` |

### 🔹 Output Example

```
reports/
└── http192.168.1.52DVWA_20250803-234528/
    ├── nmap.txt
    ├── nikto.txt
    └── gobuster.txt
```

---

## 📋 TODO Tracker

See `TODO.md` for weekly progress.

---

## 📚 Resources

- [Nmap Reference](https://nmap.org/book/man.html)
- [Nikto Docs](https://cirt.net/Nikto2)
- [Gobuster GitHub](https://github.com/OJ/gobuster)

---

## 📜 License

MIT
