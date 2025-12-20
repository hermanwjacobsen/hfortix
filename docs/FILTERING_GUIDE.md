# FortiOS API Filtering Guide

Complete guide to using filters with FortiOS API queries.

## Overview

FortiOS supports powerful filtering capabilities for GET requests, allowing you to query specific objects without retrieving the entire dataset. Filters are applied as query parameters and use FortiOS native operators.

## Basic Usage

```python
from hfortix import FortiOS

fgt = FortiOS("192.0.2.10", token="your_token_here")

# Get specific address by name
address = fgt.api.cmdb.firewall.address.get("test-host")

# Get all addresses matching a filter
addresses = fgt.api.cmdb.firewall.address.list(filter="subnet=@10.0.0")
```

## Filter Operators

FortiOS supports the following filter operators:

### 1. Equality Operators

#### `==` - Equals (Case Insensitive Match)
Matches objects where the field value equals the pattern (case-insensitive).

```python
# Get firewall address with exact name
addresses = fgt.api.cmdb.firewall.address.list(filter="name==test-host")

# Get policies with specific action
policies = fgt.api.cmdb.firewall.policy.list(filter="action==accept")

# Get interfaces with specific type
interfaces = fgt.api.cmdb.system.interface.list(filter="type==physical")
```

#### `!=` - Not Equals
Matches objects where the field value does NOT equal the pattern.

```python
# Get all addresses except a specific one
addresses = fgt.api.cmdb.firewall.address.list(filter="name!=test-host")

# Get policies that are not set to deny
policies = fgt.api.cmdb.firewall.policy.list(filter="action!=deny")

# Get non-VLAN interfaces
interfaces = fgt.api.cmdb.system.interface.list(filter="type!=vlan")
```

### 2. Contains Operators

#### `=@` - Contains
Matches objects where the field value contains the pattern (substring match).

```python
# Get all addresses containing "10.0" in subnet
addresses = fgt.api.cmdb.firewall.address.list(filter="subnet=@10.0")

# Get all policies with "web" in the name
policies = fgt.api.cmdb.firewall.policy.list(filter="name=@web")

# Get all address groups containing "servers"
groups = fgt.api.cmdb.firewall.addrgrp.list(filter="name=@servers")
```

#### `!@` - Not Contains
Matches objects where the field value does NOT contain the pattern.

```python
# Get addresses that don't contain "192.168" in subnet
addresses = fgt.api.cmdb.firewall.address.list(filter="subnet!@192.168")

# Get policies without "test" in name
policies = fgt.api.cmdb.firewall.policy.list(filter="name!@test")
```

### 3. Comparison Operators

#### `<` - Less Than
Matches objects where the field value is less than the pattern.

```python
# Get policies with ID less than 100
policies = fgt.api.cmdb.firewall.policy.list(filter="policyid<100")

# Get routes with distance less than 10
routes = fgt.api.cmdb.router.static.list(filter="distance<10")
```

#### `<=` - Less Than or Equal
Matches objects where the field value is less than or equal to the pattern.

```python
# Get policies with ID 100 or less
policies = fgt.api.cmdb.firewall.policy.list(filter="policyid<=100")

# Get routes with priority 5 or less
routes = fgt.api.cmdb.router.static.list(filter="priority<=5")
```

#### `>` - Greater Than
Matches objects where the field value is greater than the pattern.

```python
# Get policies with ID greater than 100
policies = fgt.api.cmdb.firewall.policy.list(filter="policyid>100")

# Get routes with distance greater than 10
routes = fgt.api.cmdb.router.static.list(filter="distance>10")
```

#### `>=` - Greater Than or Equal
Matches objects where the field value is greater than or equal to the pattern.

```python
# Get policies with ID 100 or greater
policies = fgt.api.cmdb.firewall.policy.list(filter="policyid>=100")

# Get routes with priority 5 or greater
routes = fgt.api.cmdb.router.static.list(filter="priority>=5")
```

## Multiple Filter Conditions

Combine multiple filter conditions using `&` (AND logic). All conditions must be true for a match.

```python
# Get policies with ID between 100 and 200
policies = fgt.api.cmdb.firewall.policy.list(filter="policyid>=100&policyid<=200")

# Get addresses in 10.0.0.0/8 range with "server" in name
addresses = fgt.api.cmdb.firewall.address.list(filter="subnet=@10.&name=@server")

# Get enabled policies with action=accept
policies = fgt.api.cmdb.firewall.policy.list(filter="status==enable&action==accept")
```

## Field-Specific Examples

### Firewall Addresses

```python
# By name
fgt.api.cmdb.firewall.address.list(filter="name==test-host")
fgt.api.cmdb.firewall.address.list(filter="name=@web")

# By subnet
fgt.api.cmdb.firewall.address.list(filter="subnet=@10.0")
fgt.api.cmdb.firewall.address.list(filter="subnet==10.0.0.1/32")

# By type
fgt.api.cmdb.firewall.address.list(filter="type==ipmask")
fgt.api.cmdb.firewall.address.list(filter="type==iprange")

# By comment
fgt.api.cmdb.firewall.address.list(filter="comment=@production")
```

### Firewall Policies

```python
# By ID
fgt.api.cmdb.firewall.policy.list(filter="policyid==10")
fgt.api.cmdb.firewall.policy.list(filter="policyid>=100")

# By name
fgt.api.cmdb.firewall.policy.list(filter="name=@web")

# By action
fgt.api.cmdb.firewall.policy.list(filter="action==accept")
fgt.api.cmdb.firewall.policy.list(filter="action==deny")

# By status
fgt.api.cmdb.firewall.policy.list(filter="status==enable")
fgt.api.cmdb.firewall.policy.list(filter="status==disable")

# By source interface
fgt.api.cmdb.firewall.policy.list(filter="srcintf==port1")

# By destination interface
fgt.api.cmdb.firewall.policy.list(filter="dstintf==port2")
```

### System Interfaces

```python
# By name
fgt.api.cmdb.system.interface.list(filter="name==port1")
fgt.api.cmdb.system.interface.list(filter="name=@wan")

# By type
fgt.api.cmdb.system.interface.list(filter="type==physical")
fgt.api.cmdb.system.interface.list(filter="type==vlan")
fgt.api.cmdb.system.interface.list(filter="type==tunnel")

# By VDOM
fgt.api.cmdb.system.interface.list(filter="vdom==root")

# By IP address
fgt.api.cmdb.system.interface.list(filter="ip=@192.168")
```

### Router Static Routes

```python
# By destination
fgt.api.cmdb.router.static.list(filter="dst=@0.0.0.0")

# By gateway
fgt.api.cmdb.router.static.list(filter="gateway=@192.168.1")

# By distance
fgt.api.cmdb.router.static.list(filter="distance==10")
fgt.api.cmdb.router.static.list(filter="distance<20")

# By device/interface
fgt.api.cmdb.router.static.list(filter="device==port1")
```

## Advanced Filtering Patterns

### Range Queries

```python
# Get policies with IDs between 100 and 200
policies = fgt.api.cmdb.firewall.policy.list(
    filter="policyid>=100&policyid<=200"
)

# Get routes with distance 5-15
routes = fgt.api.cmdb.router.static.list(
    filter="distance>=5&distance<=15"
)
```

### Exclude Patterns

```python
# Get all addresses NOT in 192.168.0.0/16 range
addresses = fgt.api.cmdb.firewall.address.list(
    filter="subnet!@192.168"
)

# Get policies that are NOT test policies
policies = fgt.api.cmdb.firewall.policy.list(
    filter="name!@test&name!@temp"
)
```

### Combined Filters

```python
# Get enabled web server policies
policies = fgt.api.cmdb.firewall.policy.list(
    filter="status==enable&name=@web&action==accept"
)

# Get production addresses in 10.0.0.0/8
addresses = fgt.api.cmdb.firewall.address.list(
    filter="subnet=@10.&comment=@production"
)
```

## Pagination with Filters

Combine filtering with pagination for large datasets:

```python
# Get first 100 enabled policies
policies = fgt.api.cmdb.firewall.policy.list(
    filter="status==enable",
    count=100,
    start=0
)

# Get next 100
policies = fgt.api.cmdb.firewall.policy.list(
    filter="status==enable",
    count=100,
    start=100
)
```

## Tips and Best Practices

### 1. Use Specific Filters
```python
# ✅ Good - Specific filter
addresses = fgt.api.cmdb.firewall.address.list(filter="subnet=@10.0.0")

# ❌ Bad - Retrieving everything then filtering in Python
all_addresses = fgt.api.cmdb.firewall.address.list()
filtered = [a for a in all_addresses if '10.0.0' in a.get('subnet', '')]
```

### 2. Combine Multiple Conditions
```python
# ✅ Good - Filter on FortiGate
policies = fgt.api.cmdb.firewall.policy.list(
    filter="status==enable&action==accept"
)

# ❌ Bad - Multiple API calls
enabled = fgt.api.cmdb.firewall.policy.list(filter="status==enable")
result = [p for p in enabled if p.get('action') == 'accept']
```

### 3. Test Filters First
```python
# Test your filter with a small dataset first
test_result = fgt.api.cmdb.firewall.address.list(
    filter="subnet=@10.0",
    count=5
)
print(f"Found {len(test_result)} addresses")

# If results look good, get all
all_results = fgt.api.cmdb.firewall.address.list(filter="subnet=@10.0")
```

### 4. Handle Empty Results
```python
# Filters may return empty list
addresses = fgt.api.cmdb.firewall.address.list(filter="name==nonexistent")
if not addresses:
    print("No addresses found matching filter")
```

### 5. Case Sensitivity
```python
# Operators are case-sensitive
addresses = fgt.api.cmdb.firewall.address.list(filter="name==TEST")  # Matches "TEST", "test", "Test"

# Pattern matching is case-insensitive for ==
policies = fgt.api.cmdb.firewall.policy.list(filter="action==ACCEPT")  # Matches "accept"
```

## Filter Operator Reference Table

| Operator | Description | Example | Use Case |
|----------|-------------|---------|----------|
| `==` | Equals (case-insensitive) | `name==test` | Exact match |
| `!=` | Not equals | `action!=deny` | Exclusion |
| `=@` | Contains (substring) | `subnet=@10.0` | Partial match |
| `!@` | Not contains | `name!@temp` | Exclude pattern |
| `<` | Less than | `policyid<100` | Numeric comparison |
| `<=` | Less than or equal | `policyid<=100` | Numeric range |
| `>` | Greater than | `distance>10` | Numeric comparison |
| `>=` | Greater than or equal | `priority>=5` | Numeric range |
| `&` | AND (combine filters) | `status==enable&action==accept` | Multiple conditions |

## Common Filter Examples

### Security Auditing

```python
# Find all accept policies
accept_policies = fgt.api.cmdb.firewall.policy.list(filter="action==accept")

# Find disabled policies
disabled = fgt.api.cmdb.firewall.policy.list(filter="status==disable")

# Find policies without logging
no_log = fgt.api.cmdb.firewall.policy.list(filter="logtraffic==disable")
```

### Network Planning

```python
# Find all RFC1918 addresses
rfc1918_10 = fgt.api.cmdb.firewall.address.list(filter="subnet=@10.")
rfc1918_172 = fgt.api.cmdb.firewall.address.list(filter="subnet=@172.")
rfc1918_192 = fgt.api.cmdb.firewall.address.list(filter="subnet=@192.168")

# Find VLAN interfaces
vlans = fgt.api.cmdb.system.interface.list(filter="type==vlan")

# Find default routes
defaults = fgt.api.cmdb.router.static.list(filter="dst==0.0.0.0/0")
```

### Cleanup Operations

```python
# Find test/temporary objects
test_addresses = fgt.api.cmdb.firewall.address.list(filter="name=@test")
temp_policies = fgt.api.cmdb.firewall.policy.list(filter="name=@temp")

# Find unused objects (requires additional logic)
# Note: Finding truly unused objects requires checking references
```

## Troubleshooting

### Filter Not Working?

1. **Check field name**: Use correct field names from FortiOS API documentation
2. **Check value format**: Some fields expect specific formats (e.g., IP addresses)
3. **Use simple filter first**: Test with `==` before complex filters
4. **Check API version**: Some fields may not support filtering in older FortiOS versions

### Performance Considerations

- Filters are processed on FortiGate, not client-side
- More specific filters = faster responses
- Use pagination for large result sets
- Avoid overly broad contains (`=@`) filters when possible

## Related Topics

- [FortiOS API Reference](https://docs.fortinet.com/document/fortigate/latest/rest-api-reference)
- [Operation Tracking](../README.md#operation-tracking) - Track all filtered queries
- [Read-Only Mode](../README.md#read-only-mode) - Test filters safely

## See Also

- **hfortix Documentation**: [README.md](../README.md)
- **Examples**: [examples/filtering_examples.py](../examples/filtering_examples.py)
- **FortiOS Documentation**: https://docs.fortinet.com/
