#!/usr/bin/env python3
"""
Verify that all files we removed list() from have proper get() methods
that support both listing (no param) and getting specific (with param).
"""

import re
from pathlib import Path

# Map of endpoint paths to their expected parameter names (from API docs)
EXPECTED_PARAMS = {
    # Firewall endpoints with {name}
    "firewall/address": "name",
    "firewall/address6": "name",
    "firewall/address6_template": "name",
    "firewall/addrgrp": "name",
    "firewall/addrgrp6": "name",
    "firewall/access_proxy": "name",
    "firewall/access_proxy6": "name",
    "firewall/access_proxy_ssh_client_cert": "name",
    "firewall/access_proxy_virtual_host": "name",
    "firewall/wildcard_fqdn_custom": "name",
    "firewall/wildcard_fqdn_group": "name",
    "firewall/vendor_mac_summary": "id",
    
    # Firewall DoS policies with {policyid}
    "firewall/dos_policy": "policyid",
    "firewall/dos_policy6": "policyid",
    
    # Firewall IP/MAC binding with {seq-num}
    "firewall/ipmacbinding_table": "seq_num",
    
    # Router endpoints with {seq-num}
    "router/static": "seq_num",
    "router/static6": "seq_num",
    "router/policy": "seq_num",
    "router/policy6": "seq_num",
    
    # Router endpoints with {name}
    "router/auth_path": "name",
    "router/key_chain": "name",
    "router/multicast_flow": "name",
    "router/prefix_list": "name",
    "router/prefix_list6": "name",
    "router/route_map": "name",
    "router/community_list": "name",
    "router/extcommunity_list": "name",
    
    # CASB endpoints with {name}
    "casb/attribute_match": "name",
    "casb/profile": "name",
    "casb/saas_application": "name",
    
    # DLP endpoints
    "dlp/data_type": "name",
    "dlp/dictionary": "name",
    "dlp/exact_data_match": "name",
    "dlp/filepattern": "id",
    "dlp/label": "name",
    "dlp/profile": "name",
    "dlp/sensor": "name",
    
    # ICAP endpoints with {name}
    "icap/profile": "name",
    "icap/server": "name",
    "icap/server_group": "name",
    
    # IPS endpoints with {name}
    "ips/custom": "name",
    "ips/decoder": "name",
    "ips/rule": "name",
    "ips/rule_settings": "name",
    "ips/sensor": "name",
    "ips/view_map": "name",
    
    # Application endpoints with {name}
    "application/custom": "name",
    "application/group": "name",
    
    # Diameter filter with {name}
    "diameter_filter/profile": "name",
}

def check_file(filepath, expected_param):
    """Check if the file's get() method uses the expected parameter."""
    path = Path(filepath)
    if not path.exists():
        return f"❌ File not found"
    
    content = path.read_text()
    
    # Check if it has a get() method
    if "def get(" not in content:
        return f"❌ No get() method"
    
    # Find the get() method - use DOTALL to match across lines
    # Look for the function definition up to the return type annotation
    get_match = re.search(r'def get\((.+?)\)\s*->', content, re.DOTALL)
    if not get_match:
        return f"❌ Cannot parse get() signature"
    
    signature = get_match.group(0)
    params = get_match.group(1)  # Just the parameters
    
    # Check if expected param is in the signature and is Optional
    if expected_param == "seq_num":
        # Check for seq_num as Optional[int] or int | None
        if re.search(r'seq_num:\s*(Optional\[int\]|int\s*\|\s*None)\s*=\s*None', params):
            return f"✅ Correct: seq_num: Optional[int] or int | None"
        else:
            return f"⚠️  Missing or wrong: expected seq_num: Optional[int] = None"
    
    elif expected_param == "policyid":
        # Check for policyid as Optional[int or str] or int | None or str | None
        if re.search(r'policyid:\s*(Optional\[(int|str|Union\[)|int\s*\|\s*None|str\s*\|\s*None)', params):
            return f"✅ Correct: policyid: Optional[...] or ... | None"
        else:
            return f"⚠️  Missing or wrong: expected policyid: Optional[...] = None"
    
    elif expected_param == "id":
        # Check for id as Optional[int] or int | None
        if re.search(r'\bid:\s*(int\s*\|\s*None|Optional\[int\])\s*=\s*None', params):
            return f"✅ Correct: id: Optional[int] or int | None"
        else:
            return f"⚠️  Missing or wrong: expected id: Optional[int]"
    
    elif expected_param == "name":
        # Check for name as Optional[str] or str | None
        if re.search(r'name:\s*(Optional\[str\]|str\s*\|\s*None)\s*=\s*None', params):
            return f"✅ Correct: name: Optional[str] or str | None"
        else:
            return f"⚠️  Missing or wrong: expected name: Optional[str] = None"
    
    return f"⚠️  Unknown parameter type: {expected_param}"


def main():
    print("=" * 80)
    print("Verifying get() methods have correct parameter types")
    print("=" * 80)
    print()
    
    correct = 0
    warnings = 0
    errors = 0
    
    for endpoint, param in sorted(EXPECTED_PARAMS.items()):
        # Convert endpoint path to file path
        filepath = f"hfortix/FortiOS/api/v2/cmdb/{endpoint}.py"
        
        result = check_file(filepath, param)
        
        if result.startswith("✅"):
            correct += 1
        elif result.startswith("⚠️"):
            warnings += 1
        else:
            errors += 1
        
        print(f"{endpoint:50s} → {result}")
    
    print()
    print("=" * 80)
    print(f"RESULTS: ✅ {correct} correct, ⚠️  {warnings} warnings, ❌ {errors} errors")
    print("=" * 80)


if __name__ == "__main__":
    main()
