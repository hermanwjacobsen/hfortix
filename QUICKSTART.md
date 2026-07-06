# HFortix - Quick Reference

✨ **New in v0.5.152**: Batch Transactions with commit/rollback, HTTP API Request Inspection for debugging and audit logging!

✨ **New in v0.5.148**: Comprehensive documentation updates, improved response object documentation, FortiManager Proxy clarification!

## Installation

### From PyPI (Recommended)

```bash
# Install everything (meta-package)
pip install hfortix

# Or install only what you need (modular packages - v0.4.0+)
pip install hfortix-fortios  # FortiOS/FortiGate client only
pip install hfortix-core     # Core exceptions and HTTP framework only
```

**Note:** Version 0.5.x introduces auto-generated endpoints with full type stubs. See [CHANGELOG.md](CHANGELOG.md) for version history.

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

### Alternative: Direct Module Import (v0.4.0+)

```python
# Modular package imports (v0.4.0+)
from hfortix_fortios import FortiOS
from hfortix_core import FortinetError, APIError

# FortiManager Proxy (v0.5.77+)
from hfortix_fortios import FortiManagerProxy
```

### Exception Imports

```python
from hfortix import APIError, ResourceNotFoundError, FortinetError
```

## Quick Start

### Basic Connection

```python
from hfortix import FortiOS

# Connect to FortiGate
fgt = FortiOS(
    host="192.168.1.99",
    token="your-api-token",
    verify=False  # Set True for production
)

# All endpoints are accessed via fgt.api
# Examples:
# - fgt.api.cmdb.firewall.address - Firewall addresses
# - fgt.api.cmdb.firewall.policy - Firewall policies  
# - fgt.api.monitor.firewall.session - Active sessions
# - fgt.api.log.disk.event.vpn - VPN event logs
```

### CMDB Endpoints (Configuration)

All configuration is accessed via `fgt.api.cmdb.*`:

```python
# Firewall Address - Create new
result = fgt.api.cmdb.firewall.address.post(
    name="web-server",
    subnet="10.0.1.100/32",
    comment="Production web server"
)

# Get all addresses
addresses = fgt.api.cmdb.firewall.address.get()

# Get specific address
addr = fgt.api.cmdb.firewall.address.get(name="web-server")

# Update address (PUT)
result = fgt.api.cmdb.firewall.address.put(
    name="web-server",
    comment="Updated comment"
)

# Delete address
result = fgt.api.cmdb.firewall.address.delete(name="web-server")

# Check if exists
exists = fgt.api.cmdb.firewall.address.exists(name="web-server")
```

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

# Optimized settings based on performance testing (v0.3.17+)
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
    # Get all addresses
    addresses = fgt.api.cmdb.firewall.address.get()

    # Create (POST)
    result = fgt.api.cmdb.firewall.address.post(
        name='web-server',
        subnet='10.0.1.100/32'
    )

    # Or use payload_dict parameter
    config = {'name': 'db-server', 'subnet': '10.0.1.200/32'}
    result = fgt.api.cmdb.firewall.address.post(payload_dict=config)

    # Update (PUT)
    result = fgt.api.cmdb.firewall.address.put(
        name='web-server',
        comment='Updated'
    )

    # Delete
    result = fgt.api.cmdb.firewall.address.delete(name='web-server')

except APIError as e:
    print(f"Error: {e.message} (Code: {e.error_code})")
```

## Dictionary Payload Pattern

HFortix supports flexible payload syntax using the `payload_dict` parameter:

```python
# Pattern 1: Dictionary-based (great for templates/configs)
config = {
    'name': 'web-server',
    'subnet': '192.168.10.50/32',
    'comment': 'Production server'
}
fgt.api.cmdb.firewall.address.post(payload_dict=config)

# Pattern 2: Keyword-based (readable/interactive)
fgt.api.cmdb.firewall.address.post(
    name='web-server',
    subnet='192.168.10.50/32',
    comment='Production server'
)

# Pattern 3: Mixed (template + overrides)
base = load_template('server.json')
fgt.api.cmdb.firewall.address.post(
    payload_dict=base,
    name=f'server-{site_id}',      # Override from template
    comment=f'Site: {site_name}'    # Add site-specific info
)
```

**Available on:** All post/put methods across all endpoint categories

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
import hfortix

print(hfortix.__version__)

# Optional clients are None unless their package is installed
print(hfortix.FortiManager is not None)  # needs hfortix-fortimanager
print(hfortix.FortiCare is not None)     # needs hfortix-forticare
print(hfortix.FortiZTP is not None)      # needs hfortix-fortiztp
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

### Filtering

```python
# Get specific object by name (mkey)
addr = fgt.api.cmdb.firewall.address.get(name='web-server')

# Get all objects with filtering (FortiOS filter syntax)
addresses = fgt.api.cmdb.firewall.address.get(
    filter='name=@web'  # Contains 'web'
)

# Filter with multiple conditions
policies = fgt.api.cmdb.firewall.policy.get(
    filter=['srcintf==port1', 'action==accept']
)

# Use count/start for pagination
first_100 = fgt.api.cmdb.firewall.address.get(count=100, start=0)
next_100 = fgt.api.cmdb.firewall.address.get(count=100, start=100)
```

### Working with Special Characters

```python
# Objects with special characters in names are automatically handled
# (underscores, slashes in IP addresses, spaces, etc.)

# Create address with CIDR notation
fgt.api.cmdb.firewall.address.post(
    name='Test_NET_192.0.2.0/24',  # Slash and underscores are fine
    subnet='192.0.2.0/24'
)

# Get/update/delete - special characters handled automatically
address = fgt.api.cmdb.firewall.address.get(name='Test_NET_192.0.2.0/24')
fgt.api.cmdb.firewall.address.put(
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

See `hfortix_core.exceptions` (`FORTIOS_ERROR_CODES`) for the complete list of 387 error codes.

## Tips

✅ **DO:**

- Use API tokens (recommended; username/password works only on FortiOS ≤7.4.x)
- Handle specific exceptions
- Set `verify=True` in production
- Use pagination for large datasets
- Check error codes in exception handlers
- Use `fgt.api.*` for all endpoint access

❌ **DON'T:**

- Hardcode credentials
- Ignore SSL verification in production
- Use bare `except:` clauses
- Make too many rapid API calls (rate limiting)

## Advanced Features

### Response Object Properties

All API responses return `FortiObject` instances with useful properties:

```python
result = fgt.api.cmdb.firewall.address.get()

# Status information
result.http_status_code    # HTTP status (200, 404, etc.)
result.http_status         # 'success' or 'error'
result.fgt_revision_changed  # True if config actually changed (useful for PUT)

# Response timing
result.serial              # Device serial number
result.vdom                # VDOM name
result.build               # FortiOS build number

# Data access methods
result.dict                # Returns dict (same data)
result.json                # Returns pretty-printed JSON string
result.raw                 # Returns full response envelope with metadata
```

### FortiManager Proxy (v0.5.77+)

> **Note:** FortiManager Proxy routes FortiOS API calls through FortiManager to managed FortiGate devices.

Route FortiOS API calls through FortiManager to managed devices:

```python
from hfortix_fortios import FortiManagerProxy

# Connect to FortiManager
fmg = FortiManagerProxy(
    host="fortimanager.example.com",
    username="admin",
    password="password",
    adom="root",           # ADOM containing the device
    verify=False
)

# Get a proxied FortiOS connection to a managed device
proxied_fgt = fmg.get_device("fw01")

# Use the same API as direct FortiOS!
addresses = proxied_fgt.api.cmdb.firewall.address.get()
for addr in addresses:
    print(f"{addr.name}: {addr.subnet}")

# Create, update, delete - all work through the proxy
proxied_fgt.api.cmdb.firewall.address.post(
    name="Server-01",
    subnet="10.0.1.10/32",
    vdom="root"
)

# Clean up
fmg.logout()
```

**Key Features:**
- Same API patterns as direct FortiOS connection
- Full ADOM and device targeting
- Session-based authentication with FortiManager
- JSON-RPC protocol support

## Support

- 📖 [Full Documentation](https://github.com/hermanwjacobsen/hfortix/blob/main/README.md)
- 🐛 [Report Issues](https://github.com/hermanwjacobsen/hfortix/issues)
- 💬 [Discussions](https://github.com/hermanwjacobsen/hfortix/discussions)
