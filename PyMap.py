import subprocess
import argparse
import tempfile
import os

from parser import parse_nmap_xml
from rules import load_rules, apply_rules
from report import print_report

# parses args from the cli
def parse_args():
    parser = argparse.ArgumentParser(
        description='Nmap automoation vulnurability scanner'
    )

    parser.add_argument(
        'target',
        help='Target IP, hostname or CIDR range (e.g. 192.168.1.0/24)'
    )

    parser.add_argument(
        '--mode',
        choices=['fast', 'full', 'service'],
        default='fast',
        help='Scan mode (default: fast)'
    )

    parser.add_argument(
        '--rules',
        default='vuln_rules.json',
        help='Path to vulnerability rules JSON (default: vuln_rules.json)'
    )

    return parser.parse_args()
    

def run_nmap(target: str, mode: str, output_file: str) -> None:
    if mode == 'fast':
        args = ['-F', '-sV']
    elif mode == 'full':
        args = ['-p-', '-sV']
    elif mode == 'service':
        args = ['sV']
    else: 
        raise ValueError(f'Unknown mode: {mode}')
    
    cmd = ['nmap', *args, '-oX', output_file, target]
    print(f'[+] Running command: {" ".join(cmd)}')

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f'[-] Error running nmap: {result.stderr}')
        raise SystemExit(1)
    else:
        print(f'[+] Nmap scan completed successfully.')

def main():
    arg = parse_args()

if __name__ == '__main__':
    main()