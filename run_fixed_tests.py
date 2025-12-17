#!/usr/bin/env python3
"""
Run a subset of tests to verify fixes.
"""
import subprocess
import sys
from pathlib import Path

# Tests that should now be fixed
tests_to_run = [
    # Fixed: wildcard_fqdn (2 tests)
    "X/tests/FortiOS/cmdb/firewall/test_wildcard_fqdn_custom.py",
    "X/tests/FortiOS/cmdb/firewall/test_wildcard_fqdn_group.py",
    
    # Fixed: system tests (4 tests)  
    "X/tests/FortiOS/cmdb/system/test_admin.py",
    "X/tests/FortiOS/cmdb/system/test_global_settings.py",
    "X/tests/FortiOS/cmdb/system/test_interface.py",
    "X/tests/FortiOS/cmdb/system/test_snmp_user.py",
    
    # Fixed: required parameters (4 tests)
    "X/tests/FortiOS/cmdb/firewall/test_decrypted_traffic_mirror.py",
    "X/tests/FortiOS/cmdb/firewall/test_identity_based_route.py",
    "X/tests/FortiOS/cmdb/firewall/test_interface_policy.py",
    "X/tests/FortiOS/cmdb/firewall/test_interface_policy6.py",
    
    # Fixed: validate_mkey issues (7 tests)
    "X/tests/FortiOS/cmdb/firewall/test_city.py",
    "X/tests/FortiOS/cmdb/firewall/test_country.py",
    "X/tests/FortiOS/cmdb/firewall/test_dnstranslation.py",
    
    # Fixed: internet_service files (17 tests)
    "X/tests/FortiOS/cmdb/firewall/test_internet_service.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_addition.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_botnet.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_custom.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_custom_group.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_definition.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_extension.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_fortiguard.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_group.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_ipbl_reason.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_ipbl_vendor.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_list.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_name.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_owner.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_reputation.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_sld.py",
    "X/tests/FortiOS/cmdb/firewall/test_internet_service_subapp.py",
]

passed = 0
failed = 0
failed_tests = []

print(f"\n{'='*80}")
print(f"Running {len(tests_to_run)} tests that should now be fixed...")
print(f"{'='*80}\n")

for test_path in tests_to_run:
    test_file = Path(test_path)
    if not test_file.exists():
        print(f"⚠️  NOT FOUND: {test_path}")
        continue
    
    test_name = test_path.split('/')[-1].replace('test_', '').replace('.py', '')
    print(f"Running: {test_name}...", end=' ', flush=True)
    
    result = subprocess.run(
        [sys.executable, str(test_file)],
        capture_output=True,
        text=True,
        timeout=30
    )
    
    if result.returncode == 0:
        print("✅ PASS")
        passed += 1
    else:
        print("❌ FAIL")
        failed += 1
        # Get the last line of error
        error_lines = result.stdout.split('\n') if result.stdout else result.stderr.split('\n')
        error = next((line for line in reversed(error_lines) if line.strip()), "Unknown error")
        failed_tests.append((test_name, error[:100]))

print(f"\n{'='*80}")
print(f"RESULTS: {passed}/{len(tests_to_run)} passed ({passed/len(tests_to_run)*100:.1f}%)")
print(f"{'='*80}\n")

if failed_tests:
    print("Failed tests:")
    for name, error in failed_tests:
        print(f"  ❌ {name}: {error}")
    print()
