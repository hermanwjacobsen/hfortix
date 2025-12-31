#!/usr/bin/env python3
"""
Regenerate index.rst files for API reference documentation.

This script scans the generated endpoint files and creates proper index.rst
files with correct references using the actual filenames (underscores, not hyphens).
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple


def title_case_from_filename(filename: str) -> str:
    """Convert filename to title case for display."""
    # Remove .rst extension
    name = filename.replace('.rst', '')
    
    # Special cases
    special_cases = {
        'DoS_policy': 'DoS Policy',
        'DoS_policy6': 'DoS Policy6',
        'global_': 'Global',
        'ssh_host_key': 'SSH Host Key',
        'ssl_ssh_profile': 'SSL/SSH Profile',
        'ssl_server': 'SSL Server',
        'ipv6': 'IPv6',
        'ipv4': 'IPv4',
        'ip_translation': 'IP Translation',
        'ippool': 'IP Pool',
        'ippool6': 'IPv6 IP Pool',
        'vip': 'VIP',
        'vip6': 'VIP6',
        'vipgrp': 'VIP Group',
        'vipgrp6': 'VIP6 Group',
        'ips': 'IPS',
        'waf': 'WAF',
        'vpn': 'VPN',
        'sdn': 'SDN',
        'api': 'API',
        'dns': 'DNS',
        'dhcp': 'DHCP',
        'ntp': 'NTP',
        'smtp': 'SMTP',
        'snmp': 'SNMP',
        'ha': 'HA',
        'fsso': 'FSSO',
        'utm': 'UTM',
        'ztna': 'ZTNA',
    }
    
    # Check for exact matches
    if name in special_cases:
        return special_cases[name]
    
    # Replace underscores with spaces and capitalize each word
    words = name.replace('_', ' ').split()
    
    # Capitalize each word, handling special cases
    result = []
    for word in words:
        if word.lower() in special_cases:
            result.append(special_cases[word.lower()])
        elif word.upper() in ['IP', 'IPS', 'VIP', 'DNS', 'DHCP', 'NTP', 'SMTP', 'SNMP', 'HA', 'FSSO', 'UTM', 'WAF', 'VPN', 'SDN', 'API', 'ZTNA']:
            result.append(word.upper())
        elif word.lower() in ['ipv4', 'ipv6']:
            result.append(word.upper())
        else:
            result.append(word.capitalize())
    
    return ' '.join(result)


def scan_endpoints(directory: Path) -> List[Tuple[str, str]]:
    """Scan a directory for endpoint files and return (filename, title) tuples."""
    endpoints = []
    
    for rst_file in sorted(directory.glob('*.rst')):
        if rst_file.name == 'index.rst':
            continue
        
        filename = rst_file.stem  # Without .rst
        title = title_case_from_filename(filename)
        
        endpoints.append((filename, title))
    
    return endpoints


def generate_category_index(category_dir: Path, category_name: str, description: str = None):
    """Generate an index.rst for a category directory."""
    
    endpoints = scan_endpoints(category_dir)
    
    if not endpoints:
        return
    
    # Build the index content
    lines = [
        category_name,
        "=" * len(category_name),
        "",
    ]
    
    if description:
        lines.extend([
            description,
            "",
        ])
    
    lines.extend([
        "Overview",
        "--------",
        "",
        f"The ``{category_dir.parent.name}.{category_dir.name}`` namespace provides configuration management for:",
        "",
    ])
    
    # Add endpoint list
    for filename, title in endpoints:
        lines.append(f"- :doc:`{title} <{filename}>` - {title} configuration endpoint.")
    
    lines.extend([
        "",
        "",
        "Quick Start",
        "-----------",
        "",
        ".. code-block:: python",
        "",
        "   from hfortix_fortios import FortiOS",
        "   ",
        "   fgt = FortiOS(host='192.168.1.99', token='your-token')",
        "   ",
        f"   # Access endpoints via:",
        f"   fgt.api.{category_dir.parent.name}.{category_dir.name}.<endpoint>",
        "",
        "Available Endpoints",
        "-------------------",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   ",
    ])
    
    # Add toctree entries
    for filename, title in endpoints:
        lines.append(f"   {filename}")
    
    lines.extend([
        "",
        "See Also",
        "--------",
        "",
        f"- :doc:`/{category_dir.parent.parent.name}/api-reference/{category_dir.parent.name}/index` - {category_dir.parent.name.upper()} API overview",
        "- :doc:`/fortios/user-guide/client` - FortiOS client reference",
        "- :doc:`/fortios/user-guide/endpoint-methods` - Endpoint methods guide",
        "",
    ])
    
    # Write the file
    output_file = category_dir / 'index.rst'
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Generated: {output_file.relative_to(output_file.parents[4])}")


def generate_main_category_index(category_dir: Path, category_name: str):
    """Generate the main category index (e.g., cmdb/index.rst)."""
    
    # Find all subcategories
    subcategories = []
    for subdir in sorted(category_dir.iterdir()):
        if subdir.is_dir() and not subdir.name.startswith('_'):
            # Count endpoints in this subcategory
            endpoint_count = len([f for f in subdir.glob('*.rst') if f.name != 'index.rst'])
            if endpoint_count > 0:
                title = title_case_from_filename(subdir.name)
                subcategories.append((subdir.name, title, endpoint_count))
    
    if not subcategories:
        return
    
    lines = [
        category_name.upper(),
        "=" * len(category_name),
        "",
        f"{category_name.upper()} API Reference",
        "",
        f"This section contains all {category_name.upper()} endpoints for FortiOS configuration and monitoring.",
        "",
        "Categories",
        "----------",
        "",
    ]
    
    # Add category list
    for dirname, title, count in subcategories:
        lines.append(f"- :doc:`{title} <{dirname}/index>` - {count} endpoints")
    
    lines.extend([
        "",
        "",
        "Quick Start",
        "-----------",
        "",
        ".. code-block:: python",
        "",
        "   from hfortix_fortios import FortiOS",
        "   ",
        "   fgt = FortiOS(host='192.168.1.99', token='your-token')",
        "   ",
        f"   # Access {category_name.upper()} endpoints via:",
        f"   fgt.api.{category_name}.<category>.<endpoint>",
        "",
        "All Categories",
        "---------------",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   ",
    ])
    
    # Add toctree
    for dirname, title, count in subcategories:
        lines.append(f"   {dirname}/index")
    
    lines.append("")
    
    # Write file
    output_file = category_dir / 'index.rst'
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Generated: {output_file.relative_to(output_file.parents[3])}")


def main():
    """Main entry point."""
    base_dir = Path(__file__).parent / 'docs' / 'source' / 'fortios' / 'api-reference'
    
    if not base_dir.exists():
        print(f"Directory not found: {base_dir}")
        return
    
    print("Regenerating index files...")
    print(f"Base directory: {base_dir}")
    print()
    
    categories = ['cmdb', 'monitor', 'log', 'service']
    
    total_indices = 0
    
    for category in categories:
        category_dir = base_dir / category
        if not category_dir.exists():
            continue
        
        print(f"\nProcessing category: {category}")
        print("-" * 40)
        
        # Generate main category index
        generate_main_category_index(category_dir, category)
        total_indices += 1
        
        # Generate subcategory indices
        for subdir in sorted(category_dir.iterdir()):
            if subdir.is_dir() and not subdir.name.startswith('_'):
                # Check if it has endpoint files
                endpoint_files = [f for f in subdir.glob('*.rst') if f.name != 'index.rst']
                if endpoint_files:
                    title = title_case_from_filename(subdir.name)
                    generate_category_index(subdir, title)
                    total_indices += 1
    
    print()
    print("=" * 40)
    print(f"Generated {total_indices} index files")
    print("=" * 40)


if __name__ == '__main__':
    main()
