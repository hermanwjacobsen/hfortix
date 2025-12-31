#!/usr/bin/env python3
"""
Generate API reference documentation files for all CMDB and Monitor categories.
This creates individual .rst files for each API category.
"""

import os
from pathlib import Path

# CMDB categories (from the actual API structure)
CMDB_CATEGORIES = [
    ('alertemail', 'Alert Email', 'Email alerting configuration'),
    ('antivirus', 'Antivirus', 'Antivirus profiles and settings'),
    ('application', 'Application', 'Application control and lists'),
    ('authentication', 'Authentication', 'Authentication settings'),
    ('automation', 'Automation', 'Automation stitches and actions'),
    ('casb', 'CASB', 'Cloud Access Security Broker'),
    ('certificate', 'Certificate', 'Certificate management'),
    ('diameter-filter', 'Diameter Filter', 'Diameter filtering profiles'),
    ('dlp', 'DLP', 'Data Loss Prevention'),
    ('dnsfilter', 'DNS Filter', 'DNS filtering profiles'),
    ('emailfilter', 'Email Filter', 'Email filtering profiles'),
    ('endpoint-control', 'Endpoint Control', 'Endpoint control settings'),
    ('ethernet-oam', 'Ethernet OAM', 'Ethernet OAM configuration'),
    ('extension-controller', 'Extension Controller', 'FortiExtender controller'),
    ('file-filter', 'File Filter', 'File filtering profiles'),
    ('firewall', 'Firewall', 'Firewall policies, addresses, and services'),
    ('ftp-proxy', 'FTP Proxy', 'FTP proxy settings'),
    ('icap', 'ICAP', 'ICAP server configuration'),
    ('ips', 'IPS', 'Intrusion Prevention System'),
    ('log', 'Log', 'Logging configuration'),
    ('monitoring', 'Monitoring', 'Monitoring configuration'),
    ('report', 'Report', 'Report settings'),
    ('router', 'Router', 'Routing configuration'),
    ('rule', 'Rule', 'Rule-based configuration'),
    ('sctp-filter', 'SCTP Filter', 'SCTP filtering'),
    ('switch-controller', 'Switch Controller', 'Switch controller settings'),
    ('system', 'System', 'System configuration and settings'),
    ('user', 'User', 'User and authentication'),
    ('videofilter', 'Video Filter', 'Video filtering'),
    ('virtual-patch', 'Virtual Patch', 'Virtual patching'),
    ('voip', 'VoIP', 'VoIP configuration'),
    ('vpn', 'VPN', 'VPN configuration'),
    ('waf', 'WAF', 'Web Application Firewall'),
    ('web-proxy', 'Web Proxy', 'Web proxy settings'),
    ('webfilter', 'Web Filter', 'Web filtering profiles'),
    ('wireless-controller', 'Wireless Controller', 'Wireless controller'),
    ('ztna', 'ZTNA', 'Zero Trust Network Access'),
]

# Monitor categories
MONITOR_CATEGORIES = [
    ('azure', 'Azure', 'Azure connector monitoring'),
    ('casb', 'CASB', 'CASB monitoring'),
    ('endpoint-control', 'Endpoint Control', 'Endpoint monitoring'),
    ('extender-controller', 'Extender Controller', 'FortiExtender monitoring'),
    ('extension-controller', 'Extension Controller', 'Extension controller monitoring'),
    ('firewall', 'Firewall', 'Firewall statistics and sessions'),
    ('firmware', 'Firmware', 'Firmware information'),
    ('fortiguard', 'FortiGuard', 'FortiGuard services'),
    ('fortiview', 'FortiView', 'FortiView statistics'),
    ('geoip', 'GeoIP', 'GeoIP information'),
    ('ips', 'IPS', 'IPS monitoring'),
    ('license', 'License', 'License information'),
    ('log', 'Log', 'Log monitoring'),
    ('network', 'Network', 'Network monitoring'),
    ('registration', 'Registration', 'Device registration'),
    ('router', 'Router', 'Routing information'),
    ('sdwan', 'SD-WAN', 'SD-WAN monitoring'),
    ('service', 'Service', 'System services'),
    ('switch-controller', 'Switch Controller', 'Switch monitoring'),
    ('system', 'System', 'System status and resources'),
    ('user', 'User', 'User monitoring'),
    ('utm', 'UTM', 'UTM statistics'),
    ('videofilter', 'Video Filter', 'Video filter monitoring'),
    ('virtual-wan', 'Virtual WAN', 'Virtual WAN monitoring'),
    ('vpn', 'VPN', 'VPN monitoring'),
    ('vpn-certificate', 'VPN Certificate', 'VPN certificate monitoring'),
    ('wanopt', 'WAN Optimization', 'WAN optimization monitoring'),
    ('web-ui', 'Web UI', 'Web UI monitoring'),
    ('webcache', 'Web Cache', 'Web cache monitoring'),
    ('webfilter', 'Web Filter', 'Web filter monitoring'),
    ('webproxy', 'Web Proxy', 'Web proxy monitoring'),
    ('wifi', 'WiFi', 'WiFi monitoring'),
]


def create_category_file(api_type, filename, title, description):
    """Create a category RST file."""
    module_name = filename.replace('-', '_')
    
    content = f'''{title}
{'=' * len(title)}

{description}.

.. automodule:: hfortix_fortios.api.v2.{api_type}.{module_name}
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

.. note::
   This category provides access to FortiOS {title} configuration through
   the ``fgt.api.{api_type}.{module_name}`` namespace.

Example Usage
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Access {title} endpoints
   result = fgt.api.{api_type}.{module_name}.<endpoint>.list()

See Also
--------

- :doc:`index` - {api_type.upper()} API overview
- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Endpoint methods guide
'''
    
    return content


def create_index_file(api_type, categories, api_title, description):
    """Create index file for CMDB or Monitor API."""
    
    content = f'''{api_title}
{'=' * len(api_title)}

{description}

.. toctree::
   :maxdepth: 1
   :caption: Categories

'''
    
    for filename, _, _ in categories:
        content += f'   {filename}\n'
    
    content += f'''

Overview
--------

The {api_title} provides {len(categories)} categories of endpoints:

'''
    
    for filename, title, desc in categories:
        module_name = filename.replace('-', '_')
        content += f'''**{title}** (``{api_type}.{module_name}``)
   {desc}

'''
    
    content += f'''
Usage Pattern
-------------

All {api_title} endpoints follow the same pattern:

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # List resources
   items = fgt.api.{api_type}.<category>.<endpoint>.list()
   
   # Get specific resource
   item = fgt.api.{api_type}.<category>.<endpoint>.get(mkey='name')
   
   # Create resource (CMDB only)
   result = fgt.api.{api_type}.<category>.<endpoint>.create(data)
   
   # Update resource (CMDB only)
   result = fgt.api.{api_type}.<category>.<endpoint>.update(mkey='name', data)
   
   # Delete resource (CMDB only)
   result = fgt.api.{api_type}.<category>.<endpoint>.delete(mkey='name')

See Also
--------

- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/endpoint-methods` - Complete endpoint methods guide
- :doc:`../../user-guide/filtering` - Filtering and query guide
'''
    
    return content


def main():
    """Generate all API reference files."""
    script_dir = Path(__file__).parent
    api_ref_dir = script_dir / 'source' / 'api-reference'
    
    # Create CMDB directory and files
    cmdb_dir = api_ref_dir / 'cmdb'
    cmdb_dir.mkdir(exist_ok=True)
    
    print("Generating CMDB API reference files...")
    for filename, title, description in CMDB_CATEGORIES:
        content = create_category_file('cmdb', filename, title, description)
        file_path = cmdb_dir / f'{filename}.rst'
        file_path.write_text(content)
        print(f"  Created: {file_path}")
    
    # Create CMDB index
    cmdb_index = create_index_file(
        'cmdb',
        CMDB_CATEGORIES,
        'CMDB API Reference',
        'Configuration Management Database - Device configuration and settings'
    )
    (cmdb_dir / 'index.rst').write_text(cmdb_index)
    print(f"  Created: {cmdb_dir / 'index.rst'}")
    
    # Create Monitor directory and files
    monitor_dir = api_ref_dir / 'monitor'
    monitor_dir.mkdir(exist_ok=True)
    
    print("\\nGenerating Monitor API reference files...")
    for filename, title, description in MONITOR_CATEGORIES:
        content = create_category_file('monitor', filename, title, description)
        file_path = monitor_dir / f'{filename}.rst'
        file_path.write_text(content)
        print(f"  Created: {file_path}")
    
    # Create Monitor index
    monitor_index = create_index_file(
        'monitor',
        MONITOR_CATEGORIES,
        'Monitor API Reference',
        'Real-time monitoring, statistics, and status information'
    )
    (monitor_dir / 'index.rst').write_text(monitor_index)
    print(f"  Created: {monitor_dir / 'index.rst'}")
    
    # Create Log API index
    log_dir = api_ref_dir / 'log'
    log_dir.mkdir(exist_ok=True)
    
    log_index = '''Log API Reference
==================

Log query and retrieval functionality.

.. automodule:: hfortix_fortios.api.v2.log
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

Overview
--------

The Log API provides access to FortiGate log data across multiple log types:

- **Disk Logs**: Logs stored on disk
- **Memory Logs**: Logs in memory
- **FortiAnalyzer Logs**: Logs sent to FortiAnalyzer
- **FortiCloud Logs**: Logs in FortiCloud
- **Syslog Logs**: Syslog configuration

Usage Example
-------------

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Query traffic logs
   logs = fgt.api.log.disk.traffic.list(
       filter='srcip==192.168.1.100',
       rows=100
   )
   
   # Query system event logs
   events = fgt.api.log.disk.event.list(rows=50)

See Also
--------

- :doc:`../client` - FortiOS client reference
- :doc:`../../user-guide/filtering` - Log filtering guide
'''
    (log_dir / 'index.rst').write_text(log_index)
    print(f"\\nCreated: {log_dir / 'index.rst'}")
    
    # Create Service API index
    service_dir = api_ref_dir / 'service'
    service_dir.mkdir(exist_ok=True)
    
    service_index = '''Service API Reference
======================

System service operations (sniffer, security rating, etc.).

.. automodule:: hfortix_fortios.api.v2.service
   :members:
   :undoc-members:
   :show-inheritance:
   :recursive:

Overview
--------

The Service API provides control over FortiGate system services:

- **Sniffer**: Packet capture operations
- **Security Rating**: Security posture assessment
- **SAML**: SAML authentication services

Usage Examples
--------------

Packet Sniffer
^^^^^^^^^^^^^^

.. code-block:: python

   from hfortix_fortios import FortiOS

   fgt = FortiOS(host='192.168.1.99', token='your-token')
   
   # Start packet capture
   fgt.service.sniffer.start(mkey='capture1')
   
   # Stop packet capture
   fgt.service.sniffer.stop(mkey='capture1')
   
   # Download capture file
   pcap = fgt.service.sniffer.download(mkey='capture1')

Security Rating
^^^^^^^^^^^^^^^

.. code-block:: python

   # Get security rating
   rating = fgt.service.security_rating.get()
   print(f"Security score: {rating['score']}")

See Also
--------

- :doc:`../client` - FortiOS client reference
'''
    (service_dir / 'index.rst').write_text(service_index)
    print(f"Created: {service_dir / 'index.rst'}")
    
    print(f"\\n✅ Generated {len(CMDB_CATEGORIES)} CMDB + {len(MONITOR_CATEGORIES)} Monitor + 2 other = {len(CMDB_CATEGORIES) + len(MONITOR_CATEGORIES) + 2} category files!")


if __name__ == '__main__':
    main()
