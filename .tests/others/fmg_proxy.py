#!/usr/bin/env python3
"""
Simple FortiManager Proxy Example

This example shows how to connect to FortiManager and proxy API calls
to managed FortiGate devices.
"""

from hfortix_fortios import FortiManagerProxy

# Force reload to pick up latest changes during development
import importlib
import hfortix_fortios.models
importlib.reload(hfortix_fortios.models)

# Verify we're using local code
import hfortix_fortios
print(f"🔍 Using FortiOS from: {hfortix_fortios.__file__}")


# =============================================================================
# Basic Connection
# =============================================================================

# Connect to FortiManager
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password",
    verify=False,  # Set True in production with valid certs
    adom="HWJ",   # Default ADOM
)

# Get a proxied FortiOS client for a specific device
fgt = fmg.proxy(device="hwj-fw", vdom="test")



# Now use the exact same FortiOS API!

create_address = fgt.api.cmdb.firewall.address.set(
    name="Test-Address-01",
    subnet="192.168.1.100/32",
)

print(create_address)

addresses = fgt.api.cmdb.firewall.address.get()


for addr in addresses:
    if addr.name.startswith("Test"):
        print(f"Found test address: {addr.name} -> {addr.subnet}")  
        print(fgt.api.cmdb.firewall.address.delete(name=addr.name))

print("---- After Deletion ----")

addresses_after = fgt.api.cmdb.firewall.address.get()
for addr in addresses_after:
    if addr.name.startswith("Test"):
        print(f"Found test address: {addr.name} -> {addr.subnet}")  


alertemail = fgt.api.cmdb.alertemail.setting.get()
print(f"mailto1: {alertemail.mailto1}")

set_mailto1 = fgt.api.cmdb.alertemail.setting.put(
    mailto1="herman@wjacobsen.fo"
)

print(f"Set mailto1 response: {set_mailto1}")
alertemail = fgt.api.cmdb.alertemail.setting.get()
print(f"mailto1: {alertemail.mailto1}")

set_mailto1 = fgt.api.cmdb.alertemail.setting.put(
    mailto1=""
)
print(f"Set mailto1 response: {set_mailto1}")
alertemail = fgt.api.cmdb.alertemail.setting.get()
print(f"mailto1: {alertemail.mailto1}")


# =============================================================================
# With Context Manager (recommended)
# =============================================================================

# with FortiManagerProxy(
#     host="fmg.example.com",
#     username="admin", 
#     password="password",
#     adom="production",
# ) as fmg:
    
#     # Proxy to a device in the production ADOM
#     fgt = fmg.proxy(device="edge-fw-01", vdom="root")
    
#     # Get firewall policies
#     policies = fgt.api.cmdb.firewall.policy.get()
#     print(f"Found {len(policies)} policies")
    
#     # Get system status via monitor API
#     # resources = fgt.api.monitor.system.resource.usage.get()
#     # print(f"CPU: {resources.results.cpu}%")


# =============================================================================
# Multiple Devices
# =============================================================================

# with FortiManagerProxy(
#     host="fmg.example.com",
#     username="admin",
#     password="password",
# ) as fmg:
    
#     devices = ["fw-site-a", "fw-site-b", "fw-site-c"]
    
#     for device_name in devices:
#         fgt = fmg.proxy(adom="sites", device=device_name)
        
#         # Get interface info
#         interfaces = fgt.api.cmdb.system.interface.get()
#         print(f"\n{device_name}: {len(interfaces)} interfaces")


# =============================================================================
# Create/Update Objects Through Proxy
# =============================================================================

# with FortiManagerProxy(
#     host="fmg.example.com",
#     username="admin",
#     password="password",
#     adom="root",
# ) as fmg:
    
#     fgt = fmg.proxy(device="firewall-01")
    
#     # Create a new address object
#     fgt.api.cmdb.firewall.address.post(
#         name="Server-Web-01",
#         subnet="10.1.1.100/32",
#         comment="Web server created via FMG proxy",
#     )
    
#     # Update an existing address
#     fgt.api.cmdb.firewall.address.put(
#         name="Server-Web-01",
#         comment="Updated comment",
#     )
    
#     # Delete an address
#     # fgt.api.cmdb.firewall.address.delete(name="Server-Web-01")

print("✅ FortiManagerProxy example loaded successfully!")

