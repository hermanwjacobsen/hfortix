# Convenience Wrappers Guide

**Version:** 0.3.38+  
**Status:** Production Ready

High-level convenience wrappers for FortiOS configuration management with intuitive interfaces, comprehensive parameter validation, and error handling.

## Table of Contents

- [Overview](#overview)
- [Available Wrappers](#available-wrappers)
- [Common Patterns](#common-patterns)
- [Error Handling](#error-handling)
- [Examples by Category](#examples-by-category)
- [Related Documentation](#related-documentation)

---

## Overview

Convenience wrappers provide a clean, Pythonic interface to FortiOS features, eliminating the need to work with raw REST API dictionaries. All wrappers include:

- ✅ **Explicit Parameters** - Named parameters matching FortiOS terminology
- ✅ **Type Safety** - Full type hints with IDE autocomplete
- ✅ **Input Validation** - Range checking, enum validation, type checking
- ✅ **Error Handling** - Configurable error modes (raise/return/print)
- ✅ **Comprehensive Documentation** - Detailed docstrings for all methods
- ✅ **Helper Methods** - `.exists()`, `get_by_name()`, `rename()`, `clone()`

---

## Available Wrappers

### Firewall Category

All accessible via `fgt.firewall.*`:

| Wrapper | Access Path | Description | Version |
|---------|-------------|-------------|---------|
| **Policy** | `fgt.firewall.policy` | Firewall policies with 150+ parameters | v0.3.17+ |
| **Address** | `fgt.firewall.address` | Address objects and groups | v0.3.34+ |
| **Service** | `fgt.firewall.service_custom` | Custom services | v0.3.37+ |
| **Service Category** | `fgt.firewall.service_category` | Service categories | v0.3.37+ |
| **Service Group** | `fgt.firewall.service_group` | Service groups | v0.3.37+ |
| **Traffic Shaper** | `fgt.firewall.traffic_shaper` | Shared traffic shapers | v0.3.38+ |
| **Per-IP Shaper** | `fgt.firewall.shaper_per_ip` | Per-IP bandwidth limits | v0.3.38+ |
| **Schedule Onetime** | `fgt.firewall.schedule_onetime` | One-time schedules | v0.3.34+ |
| **Schedule Recurring** | `fgt.firewall.schedule_recurring` | Recurring schedules | v0.3.34+ |
| **Schedule Group** | `fgt.firewall.schedule_group` | Schedule groups | v0.3.34+ |

---

## Common Patterns

All convenience wrappers follow consistent patterns:

### Pattern 1: Create Objects

```python
from hfortix import FortiOS

fgt = FortiOS(host="fortigate.example.com", token="your_token", verify=False)

# Create with explicit parameters
result = fgt.firewall.policy.create(
    name="Allow-Web",
    srcintf=["port1"],
    dstintf=["port2"],
    srcaddr=["all"],
    dstaddr=["web-servers"],
    action="accept",
    schedule="always",
    service=["HTTP", "HTTPS"],
    logtraffic="all"
)

# Create traffic shaper
result = fgt.firewall.traffic_shaper.create(
    name="critical-apps",
    guaranteed_bandwidth=50000,
    maximum_bandwidth=100000,
    bandwidth_unit="kbps",
    priority="high"
)

# Create schedule
result = fgt.firewall.schedule_recurring.create(
    name="business-hours",
    start="08:00",
    end="17:00",
    day=["monday", "tuesday", "wednesday", "thursday", "friday"]
)
```

### Pattern 2: Update Objects

```python
# Update only specific fields
result = fgt.firewall.policy.update(
    policy_id=5,
    status="enable",
    logtraffic="all"
)

# Update shaper bandwidth
result = fgt.firewall.traffic_shaper.update(
    name="critical-apps",
    maximum_bandwidth=200000
)

# Update schedule times
result = fgt.firewall.schedule_recurring.update(
    name="business-hours",
    end="18:00"  # Extend to 6 PM
)
```

### Pattern 3: Get Objects

```python
# Get all objects
policies = fgt.firewall.policy.get()
shapers = fgt.firewall.traffic_shaper.get()
schedules = fgt.firewall.schedule_recurring.get()

# Get specific object by ID/name
policy = fgt.firewall.policy.get(policy_id=1)
shaper = fgt.firewall.traffic_shaper.get(name="critical-apps")
schedule = fgt.firewall.schedule_recurring.get(name="business-hours")

# Get with filter
policies = fgt.firewall.policy.get(filter='srcintf==port1')

# Get by name (cleaner than .get())
policy = fgt.firewall.policy.get_by_name("Allow-Web")
shaper = fgt.firewall.traffic_shaper.get_by_name("critical-apps")
schedule = fgt.firewall.schedule_recurring.get_by_name("business-hours")
```

### Pattern 4: Delete Objects

```python
# Delete by ID/name
result = fgt.firewall.policy.delete(policy_id=5)
result = fgt.firewall.traffic_shaper.delete(name="critical-apps")
result = fgt.firewall.schedule_recurring.delete(name="business-hours")
```

### Pattern 5: Check Existence

```python
# Check if object exists (no exceptions)
if fgt.firewall.policy.exists(policy_id=1):
    print("Policy exists")

if fgt.firewall.traffic_shaper.exists(name="critical-apps"):
    print("Shaper exists")

if fgt.firewall.schedule_recurring.exists(name="business-hours"):
    print("Schedule exists")
```

### Pattern 6: Rename Objects

```python
# Rename objects (where supported)
result = fgt.firewall.policy.rename(
    policy_id=5,
    new_name="Updated-Policy-Name"
)

result = fgt.firewall.schedule_recurring.rename(
    name="old-business-hours",
    new_name="new-business-hours"
)

# Note: Traffic shapers do NOT support rename (FortiOS limitation)
# fgt.firewall.traffic_shaper.rename()  # Raises NotImplementedError
```

### Pattern 7: Clone Objects

```python
# Clone with modifications
result = fgt.firewall.policy.clone(
    policy_id=1,
    new_name="Cloned-Policy",
    additional_changes={'comments': 'Cloned from policy 1'}
)

result = fgt.firewall.schedule_recurring.clone(
    name="business-hours",
    new_name="extended-hours",
    end="18:00"  # Override end time
)
```

---

## Error Handling

All convenience wrappers support configurable error handling:

### Configuration Levels

**Level 1: FortiOS Instance** (affects all wrapper calls)
```python
fgt = FortiOS(
    host="192.0.2.10",
    token="your_token",
    error_mode="raise",      # "raise" | "return" | "print"
    error_format="detailed"  # "detailed" | "simple" | "code_only"
)
```

**Level 2: Per Method Call** (overrides instance defaults)
```python
result = fgt.firewall.policy.create(
    name="MyPolicy",
    error_mode="return",     # Override for this call only
    error_format="simple"
)
```

### Error Modes

| Mode | Behavior | Use Case |
|------|----------|----------|
| **raise** (default) | Raises exception | Critical operations |
| **return** | Returns error dict | Batch operations |
| **print** | Prints to stderr, returns None | Scripts/notebooks |

### Error Formats

| Format | Detail Level | Output |
|--------|--------------|--------|
| **detailed** (default) | Full context | Endpoint, params, status, hints |
| **simple** | Basic info | Error code and message only |
| **code_only** | Minimal | Just the error code |

**Example with error_mode="return":**
```python
fgt = FortiOS(host="...", token="...", error_mode="return")

result = fgt.firewall.policy.create(name="DuplicatePolicy", ...)

if result.get("status") == "error":
    print(f"Failed: {result['error_code']} - {result['message']}")
else:
    print(f"Created: {result['mkey']}")
```

See [../ERROR_HANDLING_CONFIG.md](../ERROR_HANDLING_CONFIG.md) for complete details.

---

## Examples by Category

### Firewall Policy Management

```python
# Create comprehensive policy with security profiles
result = fgt.firewall.policy.create(
    name='Secure-Web-Access',
    srcintf=['internal'],
    dstintf=['wan1'],
    srcaddr=['internal-network'],
    dstaddr=['all'],
    action='accept',
    schedule='always',
    service=['HTTP', 'HTTPS'],
    logtraffic='all',
    nat='enable',
    ippool='enable',
    poolname=['external-pool'],
    av_profile='default',
    webfilter_profile='default',
    ips_sensor='default',
    application_list='default',
    ssl_ssh_profile='certificate-inspection'
)

# Enable/disable policy
fgt.firewall.policy.disable(policy_id=10)
fgt.firewall.policy.enable(policy_id=10)

# Move policy position
fgt.firewall.policy.move(policy_id=5, position='before', reference_id=3)
```

See [FIREWALL_POLICY_WRAPPER.md](FIREWALL_POLICY_WRAPPER.md) for 150+ available parameters.

### Traffic Shaping

```python
# Create per-IP shaper (bandwidth per user)
fgt.firewall.shaper_per_ip.create(
    name="user-limit",
    max_bandwidth=10000,
    bandwidth_unit="kbps",
    max_concurrent_session=100
)

# Create traffic shaper (shared pool)
fgt.firewall.traffic_shaper.create(
    name="critical-apps",
    guaranteed_bandwidth=50000,
    maximum_bandwidth=100000,
    bandwidth_unit="kbps",
    priority="high",
    per_policy="enable",
    dscp_marking_method="multi-stage",
    forward_dscp=["EF", "AF41"]
)

# Update shaper settings
fgt.firewall.traffic_shaper.update(
    name="critical-apps",
    maximum_bandwidth=200000
)

# Check if shaper exists
if fgt.firewall.shaper_per_ip.exists("user-limit"):
    print("Shaper is configured")
```

See [SHAPER_WRAPPERS.md](SHAPER_WRAPPERS.md) for complete details.

### Schedule Management

```python
# Create one-time schedule
fgt.firewall.schedule_onetime.create(
    name="maintenance-window",
    start="2025-12-31 22:00",
    end="2026-01-01 02:00"
)

# Create recurring schedule
fgt.firewall.schedule_recurring.create(
    name="business-hours",
    start="08:00",
    end="17:00",
    day=["monday", "tuesday", "wednesday", "thursday", "friday"]
)

# Create schedule group
fgt.firewall.schedule_group.create(
    name="all-hours",
    members=["business-hours", "after-hours"]
)

# Clone with modifications
fgt.firewall.schedule_recurring.clone(
    name="business-hours",
    new_name="extended-hours",
    end="18:00"
)

# Rename schedule
fgt.firewall.schedule_recurring.rename(
    name="old-name",
    new_name="new-name"
)

# Get by name (cleaner than .get())
schedule = fgt.firewall.schedule_recurring.get_by_name("business-hours")
if schedule:
    print(f"Start: {schedule['start']}, End: {schedule['end']}")
```

### Service Management

#### Service Custom - TCP/UDP/ICMP/IP Services

Create and manage custom firewall services with 30+ parameters:

```python
# TCP service with port range
fgt.firewall.service_custom.create(
    name="custom-app",
    protocol="TCP/UDP/SCTP",
    tcp_portrange="8080-8090",
    udp_portrange="8080-8090",
    comment="Custom application ports"
)

# ICMP service
fgt.firewall.service_custom.create(
    name="ping-custom",
    protocol="ICMP",
    icmptype=8,  # Echo request
    icmpcode=0,
    comment="Custom ping service"
)

# IP protocol service
fgt.firewall.service_custom.create(
    name="custom-gre",
    protocol="IP",
    protocol_number=47,  # GRE
    comment="Generic Routing Encapsulation"
)

# Advanced TCP service with session timeout
fgt.firewall.service_custom.create(
    name="long-running-app",
    protocol="TCP/UDP/SCTP",
    tcp_portrange="9000",
    session_ttl=3600,  # 1 hour
    tcp_halfclose_timer=120,
    tcp_halfopen_timer=30,
    comment="Long-running TCP application"
)

# Check if service exists
if fgt.firewall.service_custom.exists("custom-app"):
    # Get service by name
    service = fgt.firewall.service_custom.get_by_name("custom-app")
    print(f"Protocol: {service['protocol']}")
    
    # Update service
    fgt.firewall.service_custom.update(
        name="custom-app",
        tcp_portrange="8080-8100",  # Expand port range
        comment="Updated port range"
    )

# Rename service (updates all references)
fgt.firewall.service_custom.rename("custom-app", "custom-app-v2")

# Clone service with modifications
fgt.firewall.service_custom.clone(
    name="custom-app-v2",
    new_name="custom-app-v3",
    tcp_portrange="9080-9090"
)

# Delete service
fgt.firewall.service_custom.delete(name="custom-app-v3")
```

**Available Parameters for Service Custom:**

- **Basic**: `name`, `comment`, `protocol` (TCP/UDP/SCTP, ICMP, ICMP6, IP)
- **TCP/UDP/SCTP**: `tcp_portrange`, `udp_portrange`, `sctp_portrange`
- **ICMP**: `icmptype`, `icmpcode` (ICMP/ICMP6)
- **IP**: `protocol_number` (0-255 for IP protocol)
- **Session Timers**: `session_ttl`, `tcp_halfclose_timer`, `tcp_halfopen_timer`, `tcp_timewait_timer`
- **Advanced**: `check_reset_range`, `app_service_type`, `app_category`, `application`
- **Fabric**: `fabric_object` (enable/disable)
- **Proxy**: `proxy`, `explicit_proxy`

See method docstrings for complete parameter validation and examples.

#### Service Category - Organize Services

Group services into logical categories:

```python
# Create category
fgt.firewall.service_category.create(
    name="business-apps",
    comment="Business critical applications"
)

# Get category by name
category = fgt.firewall.service_category.get_by_name("business-apps")

# Update category
fgt.firewall.service_category.update(
    name="business-apps",
    comment="Updated: All business applications"
)

# Rename category
fgt.firewall.service_category.rename("business-apps", "enterprise-apps")

# Check existence
if fgt.firewall.service_category.exists("enterprise-apps"):
    print("Category exists")

# Delete category
fgt.firewall.service_category.delete(name="enterprise-apps")
```

**Available Parameters for Service Category:**

- `name` (required): Category name (max 63 characters)
- `comment`: Description (optional)
- `fabric_object`: Enable/disable fabric object (enable/disable)

#### Service Group - Group Multiple Services

Combine multiple services into logical groups:

```python
# Create service group
fgt.firewall.service_group.create(
    name="web-services",
    member=["HTTP", "HTTPS", "custom-app"],
    comment="All web-related services"
)

# Add member to existing group
fgt.firewall.service_group.add_member(
    name="web-services",
    member_name="FTP"
)

# Remove member from group
fgt.firewall.service_group.remove_member(
    name="web-services",
    member_name="FTP"
)

# Get group by name
group = fgt.firewall.service_group.get_by_name("web-services")
print(f"Members: {group['member']}")

# Update group (replace all members)
fgt.firewall.service_group.update(
    name="web-services",
    member=["HTTP", "HTTPS", "SSH"],
    comment="Updated member list"
)

# Rename group
fgt.firewall.service_group.rename("web-services", "web-services-v2")

# Clone group with modifications
fgt.firewall.service_group.clone(
    name="web-services-v2",
    new_name="secure-services",
    member=["HTTPS", "SSH"]  # Override members
)

# Delete group
fgt.firewall.service_group.delete(name="secure-services")
```

**Available Parameters for Service Group:**

- `name` (required): Group name (max 79 characters)
- `member` (required): List of service names to include
- `comment`: Description (optional)
- `proxy`: Proxy mode (enable/disable)
- `explicit_proxy`: Explicit proxy mode (enable/disable)
- `fabric_object`: Enable/disable fabric object (enable/disable)
- `color`: Color in GUI (0-32)

**Service Group Helper Methods:**

- `.add_member(name, member_name)` - Add single member to group
- `.remove_member(name, member_name)` - Remove single member from group
- `.get_by_name(name)` - Get group data directly
- `.rename(old_name, new_name)` - Rename group
- `.clone(name, new_name, **kwargs)` - Clone with modifications
- `.exists(name)` - Check if group exists

---

## Best Practices

### 1. Use `.exists()` Before Operations

```python
# Check before creating
if not fgt.firewall.policy.exists(policy_id=5):
    fgt.firewall.policy.create(name="NewPolicy", ...)
else:
    print("Policy already exists")

# Check before deleting
if fgt.firewall.traffic_shaper.exists(name="old-shaper"):
    fgt.firewall.traffic_shaper.delete(name="old-shaper")
```

### 2. Use `get_by_name()` for Cleaner Code

```python
# Instead of:
result = fgt.firewall.policy.get(name="Allow-Web")
if result.get('results'):
    policy = result['results'][0]

# Use:
policy = fgt.firewall.policy.get_by_name("Allow-Web")
if policy:
    print(policy['action'])
```

### 3. Use Error Modes Appropriately

```python
# Critical operations: Use "raise" (default)
fgt = FortiOS(host="...", token="...", error_mode="raise")
try:
    fgt.firewall.policy.create(name="Critical", ...)
except DuplicateEntryError:
    print("Policy exists, handling...")

# Batch operations: Use "return"
fgt = FortiOS(host="...", token="...", error_mode="return")
successes, failures = [], []
for i in range(100):
    result = fgt.firewall.policy.create(name=f"Policy{i}", ...)
    if result.get("status") == "error":
        failures.append(result)
    else:
        successes.append(result)
```

### 4. Clone Instead of Duplicate Code

```python
# Instead of creating similar objects manually:
# fgt.firewall.policy.create(name="Policy1", srcintf=["port1"], ...)
# fgt.firewall.policy.create(name="Policy2", srcintf=["port1"], ...)  # Lots of duplicate params

# Clone and modify:
fgt.firewall.policy.clone(
    policy_id=1,
    new_name="Policy2",
    additional_changes={'srcintf': ['port2']}
)
```

---

## Related Documentation

- **[FIREWALL_POLICY_WRAPPER.md](FIREWALL_POLICY_WRAPPER.md)** - Complete firewall policy reference (150+ parameters)
- **[SHAPER_WRAPPERS.md](SHAPER_WRAPPERS.md)** - Traffic shaping reference (per-IP and traffic shapers)
- **[SCHEDULE_WRAPPERS.md](SCHEDULE_WRAPPERS.md)** - Schedule management reference (onetime, recurring, groups)
- **[../ERROR_HANDLING_CONFIG.md](../ERROR_HANDLING_CONFIG.md)** - Error handling configuration guide
- **[../VALIDATION_GUIDE.md](../VALIDATION_GUIDE.md)** - Using the validation framework (832 validators)
- **[../BUILDER_PATTERN_GUIDE.md](../BUILDER_PATTERN_GUIDE.md)** - Builder pattern implementation details

---

## Summary

Convenience wrappers eliminate the complexity of raw REST API calls:

**Before (Raw API):**
```python
fgt.api.cmdb.firewall.policy.post(data={
    'name': 'Allow-Web',
    'srcintf': [{'name': 'port1'}],
    'dstintf': [{'name': 'port2'}],
    'srcaddr': [{'name': 'all'}],
    'dstaddr': [{'name': 'web-servers'}],
    'action': 'accept',
    'schedule': 'always',
    'service': [{'name': 'HTTP'}, {'name': 'HTTPS'}],
    'nat': 'enable'
})
```

**After (Convenience Wrapper):**
```python
fgt.firewall.policy.create(
    name='Allow-Web',
    srcintf=['port1'],
    dstintf=['port2'],
    srcaddr=['all'],
    dstaddr=['web-servers'],
    action='accept',
    schedule='always',
    service=['HTTP', 'HTTPS'],
    nat='enable'
)
```

**Result:** Clean, readable, maintainable code with full validation and error handling! 🎉
