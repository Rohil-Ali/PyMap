import json 
from typing import List, Dict, Any 

def load_rules(path: str) -> List[Dict[str, Any]]:
    # loads vulnurability from json file
    with open(path, 'r') as f:
        data = json.load(f)
    return data.get('rules', [])

def match_rule(port_info: Dict[str, Any], rule: Dict[str, Any]) -> bool:
    # checks if rules match the given port/service
    match = rule.get('match', {})

    # match port numbers
    rule_port = match.get('port')
    if rule_port is not None and rule_port != port_info.get('port'):
        return False
    
    # match service names
    rule_service = match.get('service')
    if rule_service is not None:
        service_name = (port_info.get('service') or '').lower()
        if rule_service.lower() != service_name:
            return False
    
    # substring match for version/product string
    contains_version = rule.get("contains_in_version")
    if contains_version:
        version_str = " ".join(
            [
                str(port_info.get("product") or ""),
                str(port_info.get("version") or ""),
                str(port_info.get("extrainfo") or ""),
            ]
        ).lower()

        if contains_version.lower() not in version_str:
            return False

    return True

def apply_rules(hosts: List[Dict[str, Any]], rules : List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Apply vulnerability rules to parsed host data.

    Returns a list of findings:
    {
        "host_ip": str,
        "hostname": str or None,
        "port": int,
        "service": str or None,
        "rule_id": str,
        "title": str,
        "severity": str,
        "description": str,
    }
    """

    findings = []

    for host in hosts:
        for port in host.get('ports', []):
            for rule in rules:
                if match_rule(port, rule):
                    findings.append(
                        {
                            'host_ip': host.get('ip'),
                            'hostname': host.get('hostname'),
                            'port': port.get('port'),
                            'service': port.get('service'),
                            'rule_id': rule.get('id'),
                            'title': rule.get('title'),
                            'severity': rule.get('severity'),
                            'description': rule.get('description'),
                        }
                    )

    return findings
