# Error Handling

Comprehensive guide to error handling in HFortix.

```{note}
This content will be migrated from `docs/fortios/ERROR_HANDLING_CONFIG.md`
```

## Overview

HFortix provides configurable error handling with three modes:

- **raise** (default) - Raise exceptions
- **return** - Return error dict
- **print** - Print errors and continue

## Quick Example

```python
from hfortix import FortiOS, APIError, DuplicateEntryError

fgt = FortiOS(host='192.168.1.99', token='token')

# Default: raise exceptions
try:
    fgt.api.cmdb.firewall.address.create(name='test', subnet='10.0.0.1/32')
except DuplicateEntryError:
    print("Address already exists!")
except APIError as e:
    print(f"Error: {e.message}")

# Return error dict
result = fgt.firewall.policy.create(
    name='test',
    error_mode='return',
    ...
)
if result.get('error'):
    print(f"Error: {result['error']}")
```

## Coming Soon

Detailed documentation including:
- All exception types
- Error handling modes
- Configuring global error handling
- Per-operation error handling
- Best practices

## Temporary Reference

For now, see:
- [Exception Reference](../api-reference/exceptions.rst)
- Current docs: `docs/fortios/ERROR_HANDLING_CONFIG.md` in repository
