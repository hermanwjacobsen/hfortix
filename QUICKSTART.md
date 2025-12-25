# HFortix - Quick Reference

## Installation

### From PyPI (Recommended)

```bash
pip install hfortix
```

### From Source

```bash
git clone https://github.com/hermanwjacobsen/hfortix.git
cd hfortix
pip install -e .
```

## Import Patterns

### Recommended: Unified Package Import

```python
from hfortix import FortiOS
```

### Alternative: Direct Module Import

```python
from hfortix.FortiOS import FortiOS
```

### Exception Imports

```python
from hfortix import APIError, ResourceNotFoundError, FortinetError
```

### Future Products (Coming Soon)

```python
# FortiManager / FortiAnalyzer are planned; currently FortiOS is available.
from hfortix import FortiOS
```

## Quick Start

## Basic Connection

```python
from hfortix import FortiOS, APIError

# Production environment - with valid SSL certificate
fgt = FortiOS(
    host='fortigate.company.com',
    token='your-api-token',  # 25+ alphanumeric characters
    verify=True  # Recommended: Verify SSL certificates
)
# Uses conservative defaults: max_connections=10, max_keepalive=5
# Run fgt.api.utils.performance_test() to get optimal settings for YOUR device!

# Development/Testing - with self-signed certificate
fgt_dev = FortiOS(
    host='192.168.1.99',
    token='your-api-token',  # Minimum 25 characters
    verify=False  # Only for dev/test with self-signed certs
)

# Token validation catches common errors:
# ❌ Token too short (< 25 chars)
# ❌ Token with spaces (copy-paste errors)  
# ❌ Invalid characters (only letters, numbers, hyphens, underscores)
# ❌ Placeholders ("your_token_here", "xxx", etc.)

# Alternative: Username/Password (FortiOS ≤7.4.x only, removed in 7.6.x+)
fgt_userpass = FortiOS(
    host='192.168.1.99',
    username='admin',      # Both required together
    password='password',   # Both required together
    verify=False
)

# Custom timeouts for slow/unreliable networks
fgt_slow = FortiOS(
    host='remote-site.company.com',
    token='your-api-token',
    connect_timeout=30.0,  # 30 seconds to establish connection
    read_timeout=600.0     # 10 minutes to read response
)

# Custom timeouts for fast local networks
fgt_fast = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    connect_timeout=5.0,   # 5 seconds to connect
    read_timeout=60.0      # 1 minute to read
)

# Optimized settings based on performance testing (NEW in v0.3.17!)
# Run performance test first to get device-specific recommendations
results = fgt_dev.api.utils.performance_test()

# Apply recommended settings for high-performance device
fgt_optimized = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False,
    max_connections=60,           # From performance test results
    max_keepalive_connections=30  # From performance test results
)

# Basic operations
try:
    # List
    addresses = fgt.api.cmdb.firewall.address.list()

    # Create
    result = fgt.api.cmdb.firewall.address.create(
        name='web-server',
        subnet='10.0.1.100/32'
    )

    # Or use dictionary pattern
    config = {'name': 'db-server', 'subnet': '10.0.1.200/32'}
    result = fgt.api.cmdb.firewall.address.create(data_dict=config)

    # Update
    result = fgt.api.cmdb.firewall.address.update(
        name='web-server',
        comment='Updated'
    )

    # Delete
    result = fgt.api.cmdb.firewall.address.delete(name='web-server')

except APIError as e:
    print(f"Error: {e.message} (Code: {e.error_code})")
```

## Dual-Pattern Interface

HFortix supports flexible syntax - use dictionaries, keywords, or mix both:

```python
# Pattern 1: Dictionary-based (great for templates/configs)
config = {
    'name': 'web-server',
    'subnet': '192.168.10.50/32',
    'comment': 'Production server'
}
fgt.api.cmdb.firewall.address.create(data_dict=config)

# Pattern 2: Keyword-based (readable/interactive)
fgt.api.cmdb.firewall.address.create(
    name='web-server',
    subnet='192.168.10.50/32',
    comment='Production server'
)

# Pattern 3: Mixed (template + overrides)
base = load_template('server.json')
fgt.api.cmdb.firewall.address.create(
    data_dict=base,
    name=f'server-{site_id}',      # Override from template
    comment=f'Site: {site_name}'    # Add site-specific info
)

# Service operations also support dual-pattern
fgt.service.sniffer.start(data_dict={'mkey': 'capture1'})
fgt.service.sniffer.start(mkey='capture1')  # Same result
```

**Available on:** All create/update methods across all implemented categories

## Exception Quick Reference

### HTTP Exceptions

- `ResourceNotFoundError` - 404
- `BadRequestError` - 400
- `MethodNotAllowedError` - 405
- `RateLimitError` - 429
- `ServerError` - 500

### FortiOS-Specific

- `DuplicateEntryError` - Object already exists
- `EntryInUseError` - Object in use, can't delete
- `InvalidValueError` - Invalid parameter value
- `PermissionDeniedError` - Insufficient permissions

## Package Information

```python
from hfortix import get_available_modules, get_version

print(get_version())
print(get_available_modules())  
# {'FortiOS': True, 'FortiManager': False, 'FortiAnalyzer': False}
```

## Common Patterns

### Environment Configuration

```python
import os
from dotenv import load_dotenv

load_dotenv()

fgt = FortiOS(
    host=os.getenv('FGT_HOST'),
    token=os.getenv('FGT_TOKEN'),
    verify=os.getenv('FGT_VERIFY_SSL', 'false') == 'true',
    connect_timeout=float(os.getenv('FGT_CONNECT_TIMEOUT', '10.0')),
    read_timeout=float(os.getenv('FGT_READ_TIMEOUT', '300.0'))
)
```

### Timeout Configuration

```python
# Default timeouts (suitable for most scenarios)
# - connect_timeout: 10 seconds (connection establishment)
# - read_timeout: 300 seconds (response read)

# High latency networks (international, satellite, etc.)
fgt = FortiOS(
    host='remote.company.com',
    token='your-api-token',
    connect_timeout=30.0,   # Allow more time to establish connection
    read_timeout=600.0      # Allow more time for large responses
)

# Fast local network (LAN)
fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    connect_timeout=5.0,    # Fail fast on connection issues
    read_timeout=60.0       # Most operations should be quick
)

# Large operations (backups, log queries, reports)
fgt = FortiOS(
    host='fortigate.company.com',
    token='your-api-token',
    read_timeout=900.0      # 15 minutes for large operations
)
```

### Pagination

```python
# Get all items (handles pagination automatically)
all_addresses = fgt.api.cmdb.firewall.address.list()

# Manual pagination
page1 = fgt.api.cmdb.firewall.address.list(start=0, count=100)
page2 = fgt.api.cmdb.firewall.address.list(start=100, count=100)
```

### Filtering

```python
# Filter by name
result = fgt.api.cmdb.firewall.address.get(name='web-server')

# Filter in list (FortiOS filter syntax)
addresses = fgt.api.cmdb.firewall.address.list(
    filter='name==web-*'
)
```

### Working with Special Characters

```python
# Objects with special characters in names are automatically handled
# (underscores, slashes in IP addresses, spaces, etc.)

# Create address with CIDR notation
fgt.api.cmdb.firewall.address.create(
    name='Test_NET_192.0.2.0/24',  # Slash and underscores are fine
    subnet='192.0.2.0/24'
)

# Get/update/delete - special characters handled automatically
address = fgt.api.cmdb.firewall.address.get(name='Test_NET_192.0.2.0/24')
fgt.api.cmdb.firewall.address.update(
    name='Test_NET_192.0.2.0/24',
    comment='Updated address'
)
fgt.api.cmdb.firewall.address.delete(name='Test_NET_192.0.2.0/24')

# Works with all special characters: / _ - . @ : ( ) [ ] spaces
```

## API Structure

### CMDB (Configuration Management Database) - 51 endpoints across 14 categories

```python
# Security Features
fgt.api.cmdb.antivirus.*               # Antivirus profiles
fgt.api.cmdb.dlp.*                     # Data Loss Prevention (8 endpoints)
fgt.api.cmdb.dnsfilter.*               # DNS filtering (2 endpoints)
fgt.api.cmdb.emailfilter.*             # Email filtering (8 endpoints)
fgt.api.cmdb.file_filter.*             # File filtering

# Network & Access Control
fgt.api.cmdb.firewall.address.*        # Firewall addresses
fgt.api.cmdb.application.*             # Application control (4 endpoints)
fgt.api.cmdb.endpoint_control.*        # Endpoint control (3 endpoints)
fgt.api.cmdb.ethernet_oam.*            # Ethernet OAM (hardware required)

# Infrastructure & Management
fgt.api.cmdb.extension_controller.*    # FortiExtender & FortiGate connectors (6 endpoints)
fgt.api.cmdb.certificate.*             # Certificate management (5 endpoints)
fgt.api.cmdb.authentication.*          # Authentication (3 endpoints)

# Other Categories
fgt.api.cmdb.alertemail.*              # Email alerts
fgt.api.cmdb.automation.*              # Automation settings
fgt.api.cmdb.casb.*                    # Cloud Access Security Broker (3 endpoints)
fgt.api.cmdb.diameter_filter.*         # Diameter filtering
fgt.api.cmdb.firewall.policy.*         # Firewall policies
fgt.api.cmdb.firewall.service.*        # Services
fgt.api.cmdb.system.interface.*        # Interfaces
fgt.api.cmdb.system.global_.*          # Global settings
fgt.api.cmdb.router.static.*           # Static routes
fgt.api.cmdb.vpn.ipsec.*              # IPSec VPN
```

### Monitor

```python
fgt.api.monitor.system.interface.*     # Interface stats
fgt.api.monitor.firewall.session.*     # Session table
fgt.api.monitor.system.resource.*      # Resource usage
```

### Log

```python
fgt.api.log.disk.traffic.*             # Traffic logs
fgt.api.log.disk.event.*               # Event logs
fgt.api.log.disk.virus.*               # Antivirus logs
```

## Error Codes Reference

| Code | Meaning |
| ---- | ------- |
| -1 | Invalid parameter/value |
| -5 | Object already exists |
| -14 | Permission denied |
| -15 | Duplicate entry |
| -23 | Object in use |
| -100 | Name already exists |
| -651 | Invalid input/format |

See `exceptions_forti.py` for complete list of 387 error codes.

## Tips

✅ **DO:**

- Use API tokens (only authentication method supported)
- Handle specific exceptions
- Set `verify=True` in production
- Use pagination for large datasets
- Check error codes in exception handlers
- Use async mode for concurrent operations (see ASYNC_GUIDE.md)
- Configure error handling for convenience wrappers based on your use case

❌ **DON'T:**

- Hardcode credentials
- Ignore SSL verification in production
- Use bare `except:` clauses
- Make too many rapid API calls (rate limiting)

## Advanced Features

### Error Handling Configuration (NEW in v0.3.24!)

Convenience wrappers support configurable error handling:

```python
from hfortix import FortiOS

# Set defaults for all operations
fgt = FortiOS(
    host='192.168.1.1',
    token='your-api-token',
    error_mode="return",      # "raise" | "return" | "print"
    error_format="simple"     # "detailed" | "simple" | "code_only"
)

# Batch operations - program continues on error
for policy in policies_to_create:
    result = fgt.firewall.policy.create(**policy)
    if result.get("status") == "error":
        print(f"Failed: {result['error_code']}")

# Override for specific call
result = fgt.firewall.policy.create(
    name="CriticalPolicy",
    ...,
    error_mode="raise",      # Override to raise exception
    error_format="detailed"  # Override to get full details
)
```

**Error Modes:**

| Mode | Stops Program? | Returns Data? | Need try/except? |
|------|---------------|---------------|------------------|
| `"raise"` | ❌ YES (without try/except) | ❌ No (raises exception) | ✅ Yes (if you want to continue) |
| `"return"` | ✅ NEVER | ✅ Yes (error dict) | ❌ No |
| `"print"` | ✅ NEVER | ⚠️ Prints to stderr, returns None | ❌ No |

**Details:**
- **`"raise"`** (default): Raises exception - program stops unless caught with try/except. Best for critical operations.
- **`"return"`**: Returns error dict - program always continues. Best for batch operations.
- **`"print"`**: Prints error to stderr and returns None - program always continues. Best for simple scripts and notebooks.

See [docs/ERROR_HANDLING_CONFIG.md](docs/ERROR_HANDLING_CONFIG.md) for comprehensive guide.

### Firewall Policy Convenience Wrappers (NEW in v0.3.21!)

Simplified interface for common firewall policy operations:

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.1', token='your-api-token')

# Create policy with flexible input formats
fgt.firewall.policy.create(
    name="Allow-Web-Traffic",
    srcintf="port1",                    # ✅ String works (normalized to list)
    dstintf=["port2"],                  # ✅ List works
    srcaddr="Internal-Network",         # ✅ String works
    dstaddr=["all"],                    # ✅ List works
    action="accept",
    schedule="always",
    service=["HTTP", "HTTPS"],          # ✅ List of strings works
    logtraffic="all",
    status="enable"
)

# Update policy (same flexible format)
fgt.firewall.policy.update(
    policyid="1",
    comment="Updated via API",
    status="disable"
)

# Move policy to top
fgt.firewall.policy.move(policyid="5", position="top")

# Move policy before another
fgt.firewall.policy.move(policyid="5", before="3")

# Get specific policy
policy = fgt.firewall.policy.get(policyid="1")

# List all policies
policies = fgt.firewall.policy.list()

# Delete policy
fgt.firewall.policy.delete(policyid="1")
```

**Benefits:**

- Automatic input normalization (strings → lists where needed)
- More Pythonic interface
- Fewer lines of code
- Same functionality as API layer

**See [docs/FIREWALL_POLICY_WRAPPER.md](docs/FIREWALL_POLICY_WRAPPER.md) for complete wrapper documentation.**

### Schedule Convenience Methods (NEW in v0.3.34!)

All schedule types now have consistent convenience methods:

```python
from hfortix import FortiOS
from hfortix.FortiOS.api._helpers import get_mkey, is_success

fgt = FortiOS(host='192.168.1.1', token='your-api-token')

# Get schedule data directly (not full API response)
schedule = fgt.firewall.schedule_onetime.get_by_name("maintenance-window")
if schedule:
    print(f"Start: {schedule['start']}, End: {schedule['end']}")

# Rename a schedule in one call
fgt.firewall.schedule_recurring.rename(
    name="old-business-hours",
    new_name="new-business-hours"
)

# Clone schedule with modifications
fgt.firewall.schedule_onetime.clone(
    name="maintenance-window",
    new_name="extended-maintenance",
    end="20:00 2026/01/15",  # Override end time
    color=10  # Override color
)

# Use response helpers for cleaner code
result = fgt.firewall.schedule_group.create(
    name="backup-schedules",
    member=["schedule1", "schedule2"]
)
print(f"Created: {get_mkey(result)}")
print(f"Success: {is_success(result)}")
```

**Available for:**
- `fgt.firewall.schedule_onetime` - One-time schedules
- `fgt.firewall.schedule_recurring` - Recurring schedules
- `fgt.firewall.schedule_group` - Schedule groups

**See [SCHEDULE_CONVENIENCE_METHODS.md](SCHEDULE_CONVENIENCE_METHODS.md) and [examples/schedule_convenience_demo.py](examples/schedule_convenience_demo.py) for complete documentation.**

### IP/MAC Binding Convenience Wrapper (NEW in v0.3.34!)

Simplified interface for IP/MAC binding management:

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.1', token='your-api-token')

# Create IP/MAC binding
fgt.firewall.ipmac_binding_table.create(
    seq_num=100,
    ip="192.168.1.50",
    mac="00:11:22:33:44:55",
    name="server-01",
    status="enable"
)

# Check if binding exists
if fgt.firewall.ipmac_binding_table.exists(seq_num=100):
    print("Binding exists!")

# Enable/disable binding
fgt.firewall.ipmac_binding_table.disable(seq_num=100)
fgt.firewall.ipmac_binding_table.enable(seq_num=100)

# Update binding
fgt.firewall.ipmac_binding_table.update(
    seq_num=100,
    name="server-01-updated"
)

# Get all bindings
bindings = fgt.firewall.ipmac_binding_table.get_all()

# Delete binding
fgt.firewall.ipmac_binding_table.delete(seq_num=100)
```

**Features:**
- Full CRUD operations
- Built-in validation (IP, MAC, status)
- Convenience methods: `exists()`, `enable()`, `disable()`
- Comprehensive test suite: [examples/ipmacbinding_test_suite.py](examples/ipmacbinding_test_suite.py)

### Validation Framework (NEW in v0.3.21!)

832 auto-generated validators for all API endpoints:

```python
from hfortix import FortiOS
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy as policy_helpers

# Check valid values before creating resources
print("Valid actions:", policy_helpers.VALID_BODY_ACTION)
# Output: ['accept', 'deny', 'ipsec']

print("Valid log traffic options:", policy_helpers.VALID_BODY_LOGTRAFFIC)
# Output: ['all', 'utm', 'disable']

# Validate before API call
def create_policy_validated(action, logtraffic, **kwargs):
    if action not in policy_helpers.VALID_BODY_ACTION:
        raise ValueError(f"Invalid action. Valid: {policy_helpers.VALID_BODY_ACTION}")

    if logtraffic not in policy_helpers.VALID_BODY_LOGTRAFFIC:
        raise ValueError(f"Invalid logtraffic. Valid: {policy_helpers.VALID_BODY_LOGTRAFFIC}")

    return fgt.firewall.policy.create(action=action, logtraffic=logtraffic, **kwargs)

# Create with validation
create_policy_validated(
    action="accept",      # ✅ Valid
    logtraffic="all",     # ✅ Valid
    name="Test-Policy",
    srcintf="port1",
    dstintf="port2",
    srcaddr="all",
    dstaddr="all",
    service=["ALL"],
    schedule="always"
)
```

**Coverage:**

- 832 validation modules across 77 categories
- CMDB, Monitor, Log, Service APIs
- Enum, length, range, pattern validation
- Body and query parameter constants

**See [docs/VALIDATION_GUIDE.md](docs/VALIDATION_GUIDE.md) for complete validation documentation.**

### Builder Pattern (NEW in v0.3.21!)

Eliminates code duplication with reusable payload builders:

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers.policy_helpers import (
    build_policy_payload,
    build_policy_payload_normalized
)

# API layer: Build exact payload
payload = build_policy_payload(
    name="Test",
    srcintf=["port1"],
    dstintf=["port2"],
    action="accept"
)

# Wrapper layer: Build with normalization
payload = build_policy_payload_normalized(
    name="Test",
    srcintf="port1",     # Normalized to [{"name": "port1"}]
    dstintf=["port2"],   # Normalized to [{"name": "port2"}]
    action="accept"
)

# Use in your code
result = fgt.api.cmdb.firewall.policy.create(payload_dict=payload)
```

**Benefits:**

- 13% code reduction (454 lines removed from policy endpoints)
- Consistent behavior across methods
- Easier maintenance
- Better testing

**See [docs/BUILDER_PATTERN_GUIDE.md](docs/BUILDER_PATTERN_GUIDE.md) for implementation details.**

### Async/Await Support

For high-performance concurrent operations, use async mode:

```python
import asyncio
from hfortix import FortiOS

async def main():
    # Enable async mode
    async with FortiOS(host='...', token='...', mode="async") as fgt:
        # All methods work with await
        addresses = await fgt.api.cmdb.firewall.address.list()

        # Run multiple operations concurrently
        addr, pol, svc = await asyncio.gather(
            fgt.api.cmdb.firewall.address.list(),
            fgt.api.cmdb.firewall.policy.list(),
            fgt.api.cmdb.firewall.service.custom.list()
        )

asyncio.run(main())
```

**See [docs/ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ASYNC_GUIDE.md) for complete async documentation.**

## Support

- 📖 [Full Documentation](https://github.com/hermanwjacobsen/hfortix/blob/main/README.md)
- 🚀 [Async/Await Guide](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ASYNC_GUIDE.md)
- 🐛 [Report Issues](https://github.com/hermanwjacobsen/hfortix/issues)
- 💬 [Discussions](https://github.com/hermanwjacobsen/hfortix/discussions)
