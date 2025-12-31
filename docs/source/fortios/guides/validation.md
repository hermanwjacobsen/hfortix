# Validation

Guide to the HFortix validation framework with 832 auto-generated validators.

```{note}
This content will be migrated from `docs/fortios/VALIDATION_GUIDE.md`
```

## Overview

HFortix includes auto-generated validation for:
- Enum values
- Length limits (strings, arrays)
- Range checks (integers)
- Pattern matching (regex)
- Type validation

## Quick Examples

```python
from hfortix import FortiOS, ValidationError

fgt = FortiOS(host='192.168.1.99', token='token')

# Validation happens automatically
try:
    fgt.api.cmdb.firewall.address.create(
        name='a' * 100,  # Too long
        subnet='192.168.1.1/32'
    )
except ValidationError as e:
    print(f"Validation error: {e.message}")
    # Error: name length exceeds maximum of 79 characters

# Invalid enum value
try:
    fgt.firewall.policy.create(
        name='test',
        action='invalid-action',  # Must be 'accept' or 'deny'
        ...
    )
except ValidationError as e:
    print(f"Invalid action: {e.message}")
```

## Coming Soon

Detailed documentation including:
- 832 validator modules
- Validation types
- Custom validation
- Disabling validation
- Validation error handling
- Best practices

## Temporary Reference

For now, see:
- Current docs: `docs/fortios/VALIDATION_GUIDE.md` in repository
