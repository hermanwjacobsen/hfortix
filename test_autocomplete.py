#!/usr/bin/env python3
"""
Test file to verify IDE autocomplete works

Open this file in VS Code and test:
1. Type 'fgt.' - should see 'api' in autocomplete
2. Type 'fgt.api.' - should see 'cmdb', 'log', 'monitor', 'service'
3. Type 'fgt.api.cmdb.' - should see 'firewall', 'antivirus', etc.
4. Type 'fgt.api.cmdb.firewall.' - should see 'address', 'policy', etc.
"""

from FortiOS import FortiOS

# Initialize client
fgt = FortiOS("192.0.2.10", token="test_token", verify=False)

# TEST AUTOCOMPLETE HERE:
# Try typing the following lines and check if autocomplete appears:

# 1. Basic access - should show 'api'
result1 = fgt.api  # <- cursor here after 'fgt.' should show 'api'

# 2. API categories - should show cmdb, log, monitor, service
result2 = fgt.api.cmdb  # <- cursor here after 'fgt.api.' should show categories

# 3. CMDB modules - should show firewall, antivirus, dlp, etc.
result3 = fgt.api.cmdb.firewall  # <- cursor after 'cmdb.' should show modules

# 4. Firewall endpoints - should show address, policy, etc.
result4 = fgt.api.cmdb.firewall.address  # <- cursor after 'firewall.' should show endpoints

# 5. Methods - should show list, get, create, update, delete
addresses = fgt.api.cmdb.firewall.address.list()  # <- cursor after 'address.' should show methods

print("✅ If autocomplete worked for all lines above, everything is configured correctly!")
print("❌ If not, try:")
print("   1. Restart VS Code")
print("   2. Reload window (Ctrl+Shift+P -> 'Developer: Reload Window')")
print("   3. Restart language server (Ctrl+Shift+P -> 'Python: Restart Language Server')")
print("   4. Check Python interpreter is set correctly")
