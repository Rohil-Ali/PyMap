# Nmap Automation Vulnerability Scanner

A simple Python tool that:
1. Runs Nmap against a target.
2. Parses the XML output.
3. Applies custom vulnerability rules.
4. Prints a human-readable report.

## Features

- Supports multiple scan modes:
  - `fast` (fast scan, service detection)
  - `full` (all ports, service detection)
  - `service` (service/version detection only)
- Parses open ports and services from Nmap XML output.
- Applies basic vulnerability rules from `vuln_rules.json`.
- Outputs a simple text-based vulnerability report.

## Requirements

- Python 3.8+
- Nmap installed on your system (`nmap` must be on PATH).

## Usage

```bash
python scanner.py 192.168.1.10 --mode fast
python scanner.py 192.168.1.0/24 --mode full
python scanner.py example.com --mode service
