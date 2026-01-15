"""
Simple Object Mode Example

Demonstrates clean attribute access with response_mode="object"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from __client__ import fgt_ResponseModeObject as fgt

# Type hint for better autocomplete (helps Pylance when sys.path manipulation is used)
from hfortix_fortios import FortiOS
fgt: FortiOS  # Explicit type annotation for autocomplete

# Get firewall policies
print("\n🔥 Firewall Policies:\n")
print("=" * 80)

# Fetch all policies - returns list of policy objects
policies = fgt.api.cmdb.firewall.policy.get()

print(f"\n📊 Found {len(policies)} firewall policies")
print(f"Response type: {type(policies)}")

for policy in policies:
    print(f"- Policy ID: {policy.policyid}, Name: {policy.name}, Src: {policy.srcintf}, Dst: {policy.dstintf}, Action: {policy.action}, nat: {policy.nat}, poolname: {policy.poolname}")

## Get specific group by name - should return single GroupObject (not list!)
group = fgt.api.cmdb.firewall.service.group.get(name="test_duplicates", response_mode="object")

# NOW THIS SHOULD WORK - group is a single object, not a list!
print(f"Group name: {group.name}")
print(f"Members: {len(group.member)}")

for member in group.member:
    print(f"  - {member.name}")