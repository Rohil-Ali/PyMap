# Nmap Automation Vulnerability Scanner

---

## 🔧 Features

- Runs Nmap automatically from Python  
- Supports three scan modes:
  - `fast` – fast scan with service detection  
  - `full` – full port scan + service detection  
  - `service` – service/version detection only  
- Parses hosts, open ports, service versions, and metadata  
- Applies vulnerability rules defined in `vuln_rules.json`  
- Generates a simple human-readable report  
- Clean, modular structure (`nmap_runner.py`, `parser.py`, `rules.py`, `reporting.py`)

---

## 📦 Requirements

- **Python 3.8+**
- **Nmap installed** on your system  
  (must be runnable using the `nmap` command)
- Python libraries:
  - `argparse` (built-in)
  - `subprocess` (built-in)
  - `json` (built-in)
  - `xml.etree.ElementTree` (built-in)
  - `typing` (built-in)

No external packages needed — everything is standard Python.

---

## 🛠️ Getting Started

1. Install **Nmap**  
   - Linux:  
     ```bash
     sudo apt install nmap
     ```
   - macOS:  
     ```bash
     brew install nmap
     ```
   - Windows:  
     Install from the official Nmap installer.

2. Clone or download this project folder.

3. Ensure the project contains:
   - `scanner.py`  
   - `parser.py`  
   - `rules.py`  
   - `reporter.py`  
   - `vuln_rules.json`

4. You’re ready to run scans.

---

## ▶️ How to Run

Examples:

```bash
python scanner.py scanme.nmap.org --mode fast
python scanner.py 192.168.1.10 --mode full --rules vuln_rules.json
python scanner.py example.com --mode service

## 🚀 Why I Built This Project

I’ve been doing a lot of coding projects recently, but I wanted something **networking/cybersecurity-related** to deepen my understanding of:

- How port scanning works  
- How Nmap gathers service/version information  
- How vulnerability scanners match rules against scan output  
- How real security tools automate interpretation instead of just printing raw results  

This project bridges **networking knowledge** and **Python automation**, giving me hands-on experience with concepts used in real-world security tools.

---

## 📚 What I Learned

### 🧠 Networking / Cybersecurity

During this project I learned:

- How Nmap performs:
  - Host discovery  
  - Port scanning  
  - Service/version detection (`-sV`)  
- How scanning modes impact performance (`-T4`, `--top-ports`, `-Pn`, etc.)
- How open ports expose attack surfaces  
- How version banners can be used to check for vulnerabilities  
- The legality of scanning and using safe targets like `scanme.nmap.org`  

### 🐍 Python

I also strengthened my Python skills:

- Running external commands with `subprocess`
- Parsing XML using `xml.etree.ElementTree`
- Project structuring with multiple modules
- Handling errors and validating Nmap output

---

## 🔮 Future Improvements

- Add faster scan profiles
- Integrate CVE lookups
- Export reports to JSON/HTML formats
- Add multithreaded scanning for large networks
- Support OS detection (`-O`) and Nmap script scanning (`-sC`)
- Build a more advanced rule engine 
- Optional web dashboard UI for viewing scan results
