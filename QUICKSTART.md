# Fortinet SDK - Quick Reference

## Installation Methods

### Full Package
```bash
git clone <repo-url>
cd fortinet
pip install -e .
```

### Standalone FortiOS
```bash
git clone <repo-url>
cd fortinet/FortiOS
# Use as standalone module
```

## Import Patterns

### Pattern 1: Full Package Import
```python
from fortinet import FortiOS, FortinetError
```

### Pattern 2: Standalone Import
```python
from FortiOS import FortiOS
```

### Pattern 3: Exception Import
```python
from fortinet.exceptions import APIError, ResourceNotFoundError
```

### Pattern 4: Product-Specific Import
```python
from fortinet.FortiOS import FortiOS
```

## Quick Start

```python
from fortinet import FortiOS, APIError

# Initialize
fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False
)

# Basic operations
try:
    # List
    addresses = fgt.cmdb.firewall.address.list()
    
    # Create
    result = fgt.cmdb.firewall.address.create(
        name='web-server',
        subnet='10.0.1.100/32'
    )
    
    # Update
    result = fgt.cmdb.firewall.address.update(
        name='web-server',
        comment='Updated'
    )
    
    # Delete
    result = fgt.cmdb.firewall.address.delete(name='web-server')
    
except APIError as e:
    print(f"Error: {e.message} (Code: {e.error_code})")
```

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

## Module Discovery

```python
from fortinet import get_available_modules, get_version

print(get_version())  # '0.1.0'
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
all_addresses = fgt.cmdb.firewall.address.list()

# Manual pagination
page1 = fgt.cmdb.firewall.address.list(start=0, count=100)
page2 = fgt.cmdb.firewall.address.list(start=100, count=100)
```

### Filtering
```python
# Filter by name
result = fgt.cmdb.firewall.address.get(name='web-server')

# Filter in list (FortiOS filter syntax)
addresses = fgt.cmdb.firewall.address.list(
    filter='name==web-*'
)
```

## API Structure

### CMDB (Configuration Management Database)
```python
fgt.cmdb.firewall.address.*        # Firewall addresses
fgt.cmdb.firewall.policy.*         # Firewall policies
fgt.cmdb.firewall.service.*        # Services
fgt.cmdb.system.interface.*        # Interfaces
fgt.cmdb.system.global_.*          # Global settings
fgt.cmdb.router.static.*           # Static routes
fgt.cmdb.vpn.ipsec.*              # IPSec VPN
```

### Monitor
```python
fgt.monitor.system.interface.*     # Interface stats
fgt.monitor.firewall.session.*     # Session table
fgt.monitor.system.resource.*      # Resource usage
```

### Log
```python
fgt.log.disk.traffic.*             # Traffic logs
fgt.log.disk.event.*               # Event logs
fgt.log.disk.virus.*               # Antivirus logs
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
