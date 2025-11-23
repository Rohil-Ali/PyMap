from typing import List, Dict, Any

def print_report(hosts : List[Dict[str, Any]], findings : List[Dict[str, Any]]) -> None:
    print("\n================= SCAN SUMMARY =================\n")
    if not hosts: 
        print("No hosts found.")
        return
    
    for host in hosts: 
        ip = host.get('ip')
        hostname = host.get('hostname') or 'N/A'
        print(f"Host: {ip} ({hostname})")
        print('-' * 40)

        if not host.get('ports'):
            print(' No open ports.')
        else: 
            print(' Open ports:')
            for port in host['ports']:
                service = port.get('service') or 'unknown'
                product = port.get('product') or ''
                version = port.get('version') or ''
                extra = port.get('extrainfo') or ''

                details = ' '.join(x for x in [product, version, extra] if x)
                if details:
                    details = f' ({details})'

                print(f"    - {port['port']}/{port['protocol']}  {service}{details}\n")

    if not findings:
        print('  No vulnerabilities found.\n')
        return
            
    print("\n================ VULNERABILITY FINDINGS ===============\n")

    for finding in findings:
        host_display = f'{finding["host_ip"]} ({finding["hostname"] or "-"})'
        print(f'[{finding["severity"].upper()}] {finding["title"]}')
        print(f'  Host   : {host_display}')
        print(f'  Port   : {finding["port"]} ({finding["service"] or "unknown"})')
        print(f'  Rule ID: {finding["rule_id"]}')
        print(f'  Detail : {finding["description"]}')
        print()