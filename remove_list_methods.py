#!/usr/bin/env python3
"""
Remove redundant list() methods from files that have both list() and get().
The get() method should already handle listing when called without parameters.
"""

import re
from pathlib import Path

files_to_process = [
    "hfortix/FortiOS/api/v2/cmdb/application/custom.py",
    "hfortix/FortiOS/api/v2/cmdb/application/group.py",
    "hfortix/FortiOS/api/v2/cmdb/casb/attribute_match.py",
    "hfortix/FortiOS/api/v2/cmdb/casb/profile.py",
    "hfortix/FortiOS/api/v2/cmdb/casb/saas_application.py",
    "hfortix/FortiOS/api/v2/cmdb/diameter_filter/profile.py",
    "hfortix/FortiOS/api/v2/cmdb/dlp/data_type.py",
    "hfortix/FortiOS/api/v2/cmdb/dlp/dictionary.py",
    "hfortix/FortiOS/api/v2/cmdb/dlp/exact_data_match.py",
    "hfortix/FortiOS/api/v2/cmdb/dlp/filepattern.py",
    "hfortix/FortiOS/api/v2/cmdb/dlp/label.py",
    "hfortix/FortiOS/api/v2/cmdb/dlp/profile.py",
    "hfortix/FortiOS/api/v2/cmdb/dlp/sensor.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/access_proxy.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/access_proxy6.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/access_proxy_ssh_client_cert.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/access_proxy_virtual_host.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/address.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/address6.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/address6_template.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/addrgrp.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/addrgrp6.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/addrgrp_refactored.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/dos_policy.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/dos_policy6.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/ipmacbinding_table.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/vendor_mac_summary.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/wildcard_fqdn_custom.py",
    "hfortix/FortiOS/api/v2/cmdb/firewall/wildcard_fqdn_group.py",
    "hfortix/FortiOS/api/v2/cmdb/icap/profile.py",
    "hfortix/FortiOS/api/v2/cmdb/icap/server.py",
    "hfortix/FortiOS/api/v2/cmdb/icap/server_group.py",
    "hfortix/FortiOS/api/v2/cmdb/ips/custom.py",
    "hfortix/FortiOS/api/v2/cmdb/ips/decoder.py",
    "hfortix/FortiOS/api/v2/cmdb/ips/rule.py",
    "hfortix/FortiOS/api/v2/cmdb/ips/rule_settings.py",
    "hfortix/FortiOS/api/v2/cmdb/ips/sensor.py",
    "hfortix/FortiOS/api/v2/cmdb/ips/view_map.py",
    "hfortix/FortiOS/api/v2/cmdb/router/auth_path.py",
    "hfortix/FortiOS/api/v2/cmdb/router/community_list.py",
    "hfortix/FortiOS/api/v2/cmdb/router/extcommunity_list.py",
    "hfortix/FortiOS/api/v2/cmdb/router/key_chain.py",
    "hfortix/FortiOS/api/v2/cmdb/router/multicast_flow.py",
    "hfortix/FortiOS/api/v2/cmdb/router/policy.py",
    "hfortix/FortiOS/api/v2/cmdb/router/policy6.py",
    "hfortix/FortiOS/api/v2/cmdb/router/prefix_list.py",
    "hfortix/FortiOS/api/v2/cmdb/router/prefix_list6.py",
    "hfortix/FortiOS/api/v2/cmdb/router/route_map.py",
    "hfortix/FortiOS/api/v2/cmdb/router/static.py",
    "hfortix/FortiOS/api/v2/cmdb/router/static6.py",
]


def remove_list_method(filepath):
    """Remove the list() method from a file."""
    path = Path(filepath)
    if not path.exists():
        print(f"❌ File not found: {filepath}")
        return False
    
    content = path.read_text()
    
    # Check if both methods exist
    if "def list(" not in content:
        print(f"⚠️  No list() method in: {filepath}")
        return False
    
    if "def get(" not in content:
        print(f"⚠️  No get() method in: {filepath}")
        return False
    
    # Find the list() method and remove it
    # Pattern: from "def list(" to the line before the next "def "
    # We need to be careful to match the entire method including docstring and body
    
    lines = content.split('\n')
    new_lines = []
    skip_mode = False
    indent_level = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if we're starting a list() method
        if not skip_mode and re.match(r'^\s*def list\(', line):
            skip_mode = True
            # Get the indentation level of the def statement
            indent_level = len(line) - len(line.lstrip())
            i += 1
            continue
        
        # If we're in skip mode, check if we've reached the next method at the same or lower indentation
        if skip_mode:
            stripped = line.lstrip()
            if stripped and not stripped.startswith('#'):
                current_indent = len(line) - len(stripped)
                # If we hit a def at the same indentation level, or a class/pass at lower level, stop skipping
                if (current_indent <= indent_level and 
                    (stripped.startswith('def ') or stripped.startswith('class ') or 
                     current_indent < indent_level)):
                    skip_mode = False
                    indent_level = None
        
        if not skip_mode:
            new_lines.append(line)
        
        i += 1
    
    new_content = '\n'.join(new_lines)
    
    # Check if we actually removed something
    if new_content == content:
        print(f"❌ Failed to remove list() from: {filepath}")
        return False
    
    # Write back
    path.write_text(new_content)
    print(f"✅ Removed list() from: {filepath}")
    return True


def main():
    print("=" * 80)
    print("Removing redundant list() methods from 50 files...")
    print("=" * 80)
    print()
    
    success_count = 0
    failed_count = 0
    
    for filepath in files_to_process:
        if remove_list_method(filepath):
            success_count += 1
        else:
            failed_count += 1
    
    print()
    print("=" * 80)
    print(f"RESULTS: {success_count} success, {failed_count} failed/skipped")
    print("=" * 80)


if __name__ == "__main__":
    main()
