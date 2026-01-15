# HFortix Test Suite - v0.5.0

Auto-generated tests for all 1,219 FortiOS API endpoints.

## Quick Start

```bash
# Run all tests
python __runtests__.py

# Run with verbose output
python __runtests__.py -v

# Run only CMDB tests
python __runtests__.py --cmdb

# Run only Monitor tests
python __runtests__.py --monitor

# Run specific category
python __runtests__.py --category firewall

# Run with coverage report
python __runtests__.py --cov

# Generate HTML report
python __runtests__.py --html report.html
```

## Test Structure

```
.tests/pytests/
├── __runtests__.py          # Test runner script
├── __client__.py            # Shared FortiGate client for tests
├── conftest.py              # Pytest configuration
└── api/
    ├── cmdb/                # CMDB (configuration) tests (~886 tests)
    │   ├── firewall/
    │   │   ├── auto_test_address.py
    │   │   ├── auto_test_policy.py
    │   │   └── ...
    │   ├── system/
    │   ├── user/
    │   ├── vpn/
    │   └── ...
    ├── monitor/             # Monitor (status) tests (~295 tests)
    │   ├── firewall/
    │   ├── system/
    │   ├── vpn/
    │   └── ...
    └── log/                 # Log query tests (~5 tests)
        ├── test_disk.py
        ├── test_memory.py
        ├── test_fortianalyzer.py
        ├── test_forticloud.py
        └── test_search.py
```

## Test Categories

### CMDB Tests (886 endpoints)

Auto-generated tests for configuration endpoints:

- **Firewall**: addresses, policies, schedules, shapers, VIPs, etc.
- **System**: interfaces, admin, SNMP, DNS, NTP, etc.
- **User**: local users, LDAP, RADIUS, groups, etc.
- **VPN**: IPsec, SSL-VPN, L2TP, PPTP, etc.
- **Router**: static routes, BGP, OSPF, RIP, etc.
- **WiFi**: WTPs, VAPs, profiles, etc.
- **Switch**: managed switches, VLANs, QoS, etc.

**Test Operations**:
- GET (list all, get specific)
- VDOM parameter testing
- Filter parameter testing
- exists() method testing
- Validator import testing

### Monitor Tests (295 endpoints)

Auto-generated tests for monitoring endpoints:

- **System**: resources, performance, interfaces
- **Firewall**: sessions, policy stats, shaper stats
- **VPN**: IPsec status, SSL-VPN sessions
- **Router**: routing table, BGP neighbors, OSPF neighbors
- **User**: firewall users, banned users
- **WiFi**: client status, rogue APs
- **Switch**: managed switch status, VLANs

**Test Operations**:
- GET (retrieve status/statistics)
- Basic structure validation

### Log Tests (5 endpoints)

Manual structure tests for log query endpoints:

- Disk logs
- Memory logs
- FortiAnalyzer logs
- FortiCloud logs
- Search logs

**Test Operations**:
- Class import verification
- Method existence checks
- Mock call validation

## Usage Examples

### Run All Tests

```bash
cd /app/dev/classes/fortinet/.tests/pytests
python __runtests__.py
```

### Run Specific Test Categories

```bash
# Only CMDB tests
python __runtests__.py --cmdb

# Only Monitor tests
python __runtests__.py --monitor

# Only Log tests
python __runtests__.py --log

# Specific category (firewall)
python __runtests__.py --category firewall
```

### Test Output Options

```bash
# Verbose (show test names)
python __runtests__.py -v

# Very verbose (show detailed output)
python __runtests__.py -vv

# Quiet (minimal output)
python __runtests__.py -q

# Summary only
python __runtests__.py --summary

# Exit on first failure
python __runtests__.py -x
```

### Advanced Options

```bash
# Run with coverage
python __runtests__.py --cov

# Generate HTML report
python __runtests__.py --html test_report.html

# Re-run only failed tests
python __runtests__.py --failed

# Skip slow tests
python __runtests__.py --fast

# Combine options
python __runtests__.py --cmdb -v --cov --html cmdb_report.html
```

### Run Specific Test Files

```bash
# Using pytest directly
pytest api/cmdb/firewall/auto_test_address.py -v

# Using test runner with additional pytest args
python __runtests__.py api/cmdb/firewall/auto_test_address.py -v
```

## Test Client Configuration

The shared test client is configured in `__client__.py`:

```python
from hfortix_fortios import FortiOS

fgt = FortiOS(
    host="192.168.1.99",
    token="...",
    port=443,
    verify=False,
    error_mode="return",
    vdom="test",  # Use test VDOM
    circuit_breaker_threshold=99999999,  # Disable for testing
    circuit_breaker_timeout=1
)
```

**Note**: Tests use the `test` VDOM to avoid affecting production configurations.

## Understanding Test Results

### Test Names

Auto-generated tests follow this naming convention:

- `auto_test_get_list_all()` - Get all items
- `auto_test_get_specific_item()` - Get specific item by key
- `auto_test_get_with_vdom()` - Test VDOM parameter
- `auto_test_get_with_filters()` - Test filter parameters
- `auto_test_exists_method()` - Test exists() helper
- `auto_test_validator_import()` - Test validator imports

### Expected Behavior

**Passing Tests** (✅):
- Endpoint is accessible
- Returns valid data structure
- Parameters work correctly
- Validators can be imported

**Skipped Tests** (⚠️):
- No existing data to test with
- Endpoint requires specific hardware
- Feature not enabled in test environment

**Failed Tests** (❌):
- API error (check FortiGate status)
- Authentication issues
- Network connectivity problems
- Code generation bugs (report these!)

## Coverage Report

Generate coverage report to see which endpoints are tested:

```bash
python __runtests__.py --cov

# Coverage report will be in:
# - Terminal output (summary)
# - htmlcov/index.html (detailed HTML report)
```

## Continuous Integration

For CI/CD pipelines:

```bash
# Run all tests with coverage and HTML report
python __runtests__.py --cov --html test_report.html -v

# Run with JUnit XML output for CI
pytest api/ --junitxml=test-results.xml
```

## Troubleshooting

### Connection Issues

If tests fail with connection errors:

1. Check FortiGate is accessible: `curl -k https://192.168.1.99`
2. Verify API token is valid
3. Check firewall rules allow access
4. Verify VDOM exists: `test`

### Authentication Errors

If tests fail with 401/403 errors:

1. Verify API token has correct permissions
2. Check token hasn't expired
3. Ensure super_admin token for cross-VDOM access

### Test VDOM

Tests use `vdom="test"` to avoid affecting production:

```bash
# Create test VDOM if it doesn't exist
config vdom
    edit test
    next
end
```

### Skipped Tests

Many tests will skip if there's no existing data:

```python
if not all_items or len(all_items) == 0:
    pytest.skip("No existing items to test with")
```

This is **normal** - create some test data to enable those tests.

## Contributing

When adding new endpoints:

1. Regenerate all code: `cd .dev/generator && python generate.py --all`
2. Tests are auto-generated
3. Run tests: `python __runtests__.py`
4. Fix any failures
5. Commit with test results

## Notes

- **Beta Status**: All tests are in beta until v1.0.0
- **Read-Only**: Most auto-generated tests are read-only (GET operations)
- **Safe**: Tests won't modify production configurations (test VDOM)
- **Fast**: Most tests complete in <1 second per endpoint
- **Complete**: 1,200+ tests covering all 1,219 endpoints

## Support

- **Issues**: https://github.com/hermanwjacobsen/hfortix/issues
- **Documentation**: See main README.md
- **API Coverage**: See docs/fortios/API_COVERAGE.md
