# IP/MAC Binding

Guide to managing IP/MAC binding settings and table entries.

## Overview

HFortix provides wrappers for IP/MAC binding:
- **IP/MAC Binding Settings** - Global binding configuration
- **IP/MAC Binding Table** - Individual binding entries

## Quick Examples

### IP/MAC Binding Table Entry

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='token')

# Create IP/MAC binding entry
binding = fgt.firewall.ipmac_binding_table.create(
    name='workstation-1',
    ip='192.168.1.100',
    mac='00:11:22:33:44:55',
    status='enable'
)

# List all bindings
bindings = fgt.firewall.ipmac_binding_table.list()

# Check if binding exists
if fgt.firewall.ipmac_binding_table.exists(name='workstation-1'):
    print("Binding exists!")
```

### IP/MAC Binding Settings

```python
# Configure global settings
settings = fgt.firewall.ipmac_binding_setting.get()
```

## Coming Soon

Detailed documentation including:
- Binding table management
- Global settings configuration
- Integration with firewall policies
- Use cases (DHCP snooping, access control)
- Best practices

## Temporary Reference

For now, see:
- [Convenience Wrappers API Reference](/fortios/api-reference/convenience-wrappers.rst)
