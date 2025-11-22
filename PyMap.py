import subprocess
import argparse
import tempfile
import os

# from parser import parse_nmap_xml
# from rules import load_rules, apply_rules
# from report import print_report

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
    pass

if __name__ == '__main__':
    main()