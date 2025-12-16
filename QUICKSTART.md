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
    token='your-api-token',
    verify=True  # Recommended: Verify SSL certificates
)

# Development/Testing - with self-signed certificate
fgt_dev = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False  # Only for dev/test with self-signed certs
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

**Available on:** 43 methods across 13 categories (100% coverage)

See [Full Documentation](X/docs/migration/DUAL_PATTERN_MIGRATION.md) for complete details.

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
    verify=os.getenv('FGT_VERIFY_SSL', 'false') == 'true'
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
|------|---------|
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

❌ **DON'T:**
- Hardcode credentials
- Ignore SSL verification in production
- Use bare `except:` clauses
- Make too many rapid API calls (rate limiting)

## Support

- 📖 [Full Documentation](README.md)
- 🐛 [Report Issues](issues)
- 💬 [Discussions](discussions)
