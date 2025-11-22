import xml.etree.ElementTree as ET
from typing import List, Dict, Any

def parse_nmap_xml(xml_path: str) -> List[Dict[str, Any]]:

    # turns the xml to a rooted tree
    tree = ET.parse(xml_path)
    root = tree.getroot()

    hosts = []
    for host in root.findall('host'):
        # ip address 
        address_elem = host.find("address[@addrtype='ipv4']")
        ip = address_elem.get('addr') if address_elem is not None else None
        
        # Hostname 
        hostname_elem = host.find('hostnames/hostname')
        hostname = hostname_elem.get('name') if hostname_elem is not None else None
    
        # open ports
        ports_info = []
        ports_elem = host.find('ports')
        if ports_elem is not None:
            for port_elem in ports_elem.findall('port'):
                state_elem = port_elem.find('state') # gets state of port from state element.
                if state_elem is None or state_elem.get('state') != 'open':
                    continue
                
                # gets service info running on ports
                service_elem = port_elem.find('service') 
                service_name = service_elem.get('name') if service_elem is not None else None 
                product = service_elem.get('product') if service_elem is not None else None
                version = service_elem.get('version') if service_elem is not None else None
                extrainfo = service_elem.get('extrainfo') if service_elem is not None else None

                ports_info.append(
                    {
                        'port': int(port_elem.get('portid')),
                        'protocol': port_elem.get('protocol'),
                        'service': service_name,
                        'product': product,
                        'version': version, 
                        'extrainfo': extrainfo
                    }
                )

                host.append(
                    {
                        'ip': ip,
                        'hostname': hostname,
                        'ports': ports_info
                    }
                )