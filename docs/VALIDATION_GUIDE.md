# Validation Framework Guide

## Overview

hfortix includes a comprehensive validation framework with **832 auto-generated validators** covering all FortiOS 7.6.5 API endpoints across all API types (CMDB, Monitor, Log, Service).

**Version:** 0.3.21  
**Last Updated:** December 22, 2025  
**Coverage:** 77 categories, 832 validation modules

---

## What's Validated?

The validation framework provides constants for validating API parameters before making requests to FortiGate devices.

### Validation Types

✅ **Enum Validation** - Predefined allowed values  
✅ **Length Validation** - minLength/maxLength for strings  
✅ **Range Validation** - min/max for numeric values  
✅ **Pattern Validation** - regex patterns for format checking  
✅ **Type Validation** - implicit via type coercion with error handling  
⚠️ **Required Field Validation** - NOT YET IMPLEMENTED (planned for next release)

---

## Validation Constants

Validators export two types of constants:

### 1. Body Parameter Constants (`VALID_BODY_*`)

Used for validating **payload data** sent in POST/PUT requests:

```python
VALID_BODY_ACTION = ["accept", "deny", "ipsec"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_LOGTRAFFIC = ["all", "utm", "disable"]
```

### 2. Query Parameter Constants (`VALID_QUERY_*`)

Used for validating **URL parameters** sent in GET requests:

```python
VALID_QUERY_ACTION = ["schema", "default-value", "move"]
VALID_QUERY_FORMAT = ["name", "id", "syntax"]
VALID_QUERY_FILTER = ["used==0", "q_origin_key==value"]
```

---

## Quick Start Examples

### Example 1: Firewall Policy Validation

```python
from hfortix import FortiOS
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy as policy_helpers

# Connect to FortiGate
fgt = FortiOS("192.168.1.1", token="your_token_here")

# Check valid values before creating policy
print("Valid actions:", policy_helpers.VALID_BODY_ACTION)
# Output: ['accept', 'deny', 'ipsec']

print("Valid log traffic options:", policy_helpers.VALID_BODY_LOGTRAFFIC)
# Output: ['all', 'utm', 'disable']

print("Valid schedule types:", policy_helpers.VALID_BODY_SCHEDULE_TYPE)
# Output: ['recurring', 'onetime']

# Create policy with validated values
fgt.firewall.policy.create(
    name="Allow-Web",
    srcintf=["port1"],
    dstintf=["port2"],
    srcaddr=["all"],
    dstaddr=["all"],
    action="accept",  # ✅ Valid (in VALID_BODY_ACTION)
    schedule="always",
    service=["HTTP", "HTTPS"],
    logtraffic="all",  # ✅ Valid (in VALID_BODY_LOGTRAFFIC)
    status="enable"    # ✅ Valid (in VALID_BODY_STATUS)
)
```

### Example 2: Address Object Validation

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import address as addr_helpers

# Check valid address types
print("Valid address types:", addr_helpers.VALID_BODY_TYPE)
# Output: ['ipmask', 'iprange', 'fqdn', 'geography', 'wildcard', 'dynamic', 'interface-subnet', 'mac']

# Check valid visibility options
print("Valid visibility:", addr_helpers.VALID_BODY_VISIBILITY)
# Output: ['enable', 'disable']

# Create address object with validated type
fgt.api.cmdb.firewall.address.create(
    name="Office-Network",
    type="ipmask",     # ✅ Valid
    subnet="10.0.0.0/24",
    visibility="enable"  # ✅ Valid
)
```

### Example 3: Query Parameter Validation

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import address as addr_helpers

# Check valid query parameters
print("Valid query actions:", addr_helpers.VALID_QUERY_ACTION)
# Output: ['schema', 'default-value', 'move']

print("Valid query formats:", addr_helpers.VALID_QUERY_FORMAT)
# Output: ['name', 'id', 'syntax', ... ]

# Use validated query parameters
addresses = fgt.api.cmdb.firewall.address.list(
    format="name|subnet|type",  # ✅ Valid format
    filter="used==0"            # ✅ Valid filter syntax
)
```

---

## Coverage by API Type

### CMDB API (37 categories, 548 validators)

**Categories:**
- `alertemail`, `antivirus`, `application`, `authentication`, `automation`
- `casb`, `certificate`, `diameter-filter`, `dlp`, `dnsfilter`
- `emailfilter`, `endpoint-control`, `ethernet-oam`, `extension-controller`
- `file-filter`, `firewall`, `ftp-proxy`, `icap`, `ips`
- `log`, `monitoring`, `report`, `router`, `rule`
- `sctp-filter`, `switch-controller`, `system`, `user`
- `videofilter`, `virtual-patch`, `voip`, `vpn`
- `waf`, `web-proxy`, `webfilter`, `wireless-controller`, `ztna`

**Example Usage:**
```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy, address, service_custom
from hfortix.FortiOS.api.v2.cmdb.system._helpers import interface, admin
from hfortix.FortiOS.api.v2.cmdb.router._helpers import static, bgp
from hfortix.FortiOS.api.v2.cmdb.vpn.ipsec._helpers import phase1_interface

# All contain VALID_BODY_* and VALID_QUERY_* constants
```

### Monitor API (32 categories, 276 validators)

**Categories:**
- `firewall`, `system`, `vpn`, `router`, `user`
- `wifi`, `switch-controller`, `log`, `webfilter`
- `ips`, `waf`, `antivirus`, `dlp`, `dnsfilter`
- `spamfilter`, `webproxy`, `casb`, `emailfilter`
- `videofilter`, `virtual-patch`, `gtp`, `certificate`
- `network`, `nsx`, `endpoint-control`, `extension-controller`
- `license`, `utm`, `utmProxy`, `fortiview`

**Example Usage:**
```python
from hfortix.FortiOS.api.v2.monitor.firewall._helpers import policy, session
from hfortix.FortiOS.api.v2.monitor.system._helpers import status, interface

# Monitor endpoints often have query parameter validation
print(status.VALID_QUERY_SCOPE)  # ['global', 'vdom']
```

### Log API (5 categories, 5 validators)

**Categories:**
- `disk`, `memory`, `fortianalyzer`, `forticloud`, `syslogd`

**Example Usage:**
```python
from hfortix.FortiOS.api.v2.log.memory._helpers import setting as log_setting

print(log_setting.VALID_BODY_STATUS)  # ['enable', 'disable']
```

### Service API (3 categories, 3 validators)

**Categories:**
- `sniffer`, `security-rating`, `system`

**Example Usage:**
```python
from hfortix.FortiOS.api.v2.service.system._helpers import fortiguard

print(fortiguard.VALID_BODY_PROTOCOL)  # ['udp', 'http', 'https']
```

---

## Finding Validators

### Method 1: Import from Helper Modules

```python
# Import specific validators
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import (
    policy,      # Firewall policies
    address,     # Address objects
    addrgrp,     # Address groups
    service_custom,  # Custom services
    ippool,      # IP pools
    vip          # Virtual IPs
)

# Use constants
print(policy.VALID_BODY_ACTION)
print(address.VALID_BODY_TYPE)
print(service_custom.VALID_BODY_PROTOCOL)
```

### Method 2: Direct Path Access

```python
# Full path for any validator
from hfortix.FortiOS.api.v2.cmdb.system._helpers import interface
from hfortix.FortiOS.api.v2.cmdb.router._helpers import static
from hfortix.FortiOS.api.v2.cmdb.user._helpers import local

print(interface.VALID_BODY_TYPE)
print(static.VALID_BODY_DEVICE)
print(local.VALID_BODY_TYPE)
```

### Method 3: Discover Available Constants

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy

# List all available constants
constants = [attr for attr in dir(policy) if attr.startswith('VALID_')]
print("Available validators:", constants)

# Output:
# ['VALID_BODY_ACTION', 'VALID_BODY_STATUS', 'VALID_BODY_LOGTRAFFIC', 
#  'VALID_BODY_NAT', 'VALID_QUERY_ACTION', 'VALID_QUERY_FORMAT', ...]
```

---

## Common Validation Patterns

### Pattern 1: Pre-Validation Helper Function

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy as policy_helpers

def validate_policy_params(action, status, logtraffic):
    """Validate policy parameters before API call."""
    errors = []
    
    if action not in policy_helpers.VALID_BODY_ACTION:
        errors.append(f"Invalid action '{action}'. "
                      f"Must be one of: {policy_helpers.VALID_BODY_ACTION}")
    
    if status not in policy_helpers.VALID_BODY_STATUS:
        errors.append(f"Invalid status '{status}'. "
                      f"Must be one of: {policy_helpers.VALID_BODY_STATUS}")
    
    if logtraffic not in policy_helpers.VALID_BODY_LOGTRAFFIC:
        errors.append(f"Invalid logtraffic '{logtraffic}'. "
                      f"Must be one of: {policy_helpers.VALID_BODY_LOGTRAFFIC}")
    
    if errors:
        raise ValueError("\\n".join(errors))
    
    return True

# Use in your code
try:
    validate_policy_params(
        action="allow",  # ❌ Invalid - should be "accept"
        status="enabled",  # ❌ Invalid - should be "enable"
        logtraffic="all"  # ✅ Valid
    )
except ValueError as e:
    print(f"Validation failed:\\n{e}")
```

### Pattern 2: Decorator for Automatic Validation

```python
from functools import wraps
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy as policy_helpers

def validate_firewall_action(func):
    """Decorator to validate firewall policy action parameter."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        action = kwargs.get('action')
        if action and action not in policy_helpers.VALID_BODY_ACTION:
            raise ValueError(
                f"Invalid action '{action}'. "
                f"Valid options: {policy_helpers.VALID_BODY_ACTION}"
            )
        return func(*args, **kwargs)
    return wrapper

@validate_firewall_action
def create_policy(name, action, **kwargs):
    """Create firewall policy with validated action."""
    # action is already validated by decorator
    return fgt.firewall.policy.create(name=name, action=action, **kwargs)

# Usage
create_policy("test", action="accept")  # ✅ Valid
create_policy("test", action="allow")   # ❌ Raises ValueError
```

### Pattern 3: Dynamic Validation Class

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy as policy_helpers

class PolicyValidator:
    """Validator for firewall policy parameters."""
    
    def __init__(self):
        self.validators = {
            'action': policy_helpers.VALID_BODY_ACTION,
            'status': policy_helpers.VALID_BODY_STATUS,
            'logtraffic': policy_helpers.VALID_BODY_LOGTRAFFIC,
            'nat': policy_helpers.VALID_BODY_NAT,
        }
    
    def validate(self, **params):
        """Validate multiple parameters at once."""
        errors = []
        
        for key, value in params.items():
            if key in self.validators:
                if value not in self.validators[key]:
                    errors.append(
                        f"Invalid {key} '{value}'. "
                        f"Valid options: {self.validators[key]}"
                    )
        
        if errors:
            raise ValueError("\\n".join(errors))
        
        return True

# Usage
validator = PolicyValidator()
validator.validate(
    action="accept",
    status="enable",
    logtraffic="all",
    nat="enable"
)
```

---

## Advanced Usage

### Combining Multiple Validators

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import (
    policy,
    address,
    service_custom
)

# Create a comprehensive firewall configuration validator
class FirewallConfigValidator:
    """Validate complete firewall configurations."""
    
    @staticmethod
    def validate_policy(data):
        """Validate policy data."""
        if 'action' in data and data['action'] not in policy.VALID_BODY_ACTION:
            raise ValueError(f"Invalid policy action: {data['action']}")
        
        if 'status' in data and data['status'] not in policy.VALID_BODY_STATUS:
            raise ValueError(f"Invalid policy status: {data['status']}")
        
        return True
    
    @staticmethod
    def validate_address(data):
        """Validate address data."""
        if 'type' in data and data['type'] not in address.VALID_BODY_TYPE:
            raise ValueError(f"Invalid address type: {data['type']}")
        
        return True
    
    @staticmethod
    def validate_service(data):
        """Validate service data."""
        if 'protocol' in data and data['protocol'] not in service_custom.VALID_BODY_PROTOCOL:
            raise ValueError(f"Invalid service protocol: {data['protocol']}")
        
        return True

# Use the validator
validator = FirewallConfigValidator()

policy_data = {
    'name': 'Allow-Web',
    'action': 'accept',
    'status': 'enable'
}

address_data = {
    'name': 'Office-Net',
    'type': 'ipmask',
    'subnet': '10.0.0.0/24'
}

validator.validate_policy(policy_data)
validator.validate_address(address_data)
```

### Generating User-Friendly Error Messages

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy as policy_helpers

def create_policy_with_validation(fgt, **kwargs):
    """Create policy with comprehensive validation and helpful error messages."""
    
    # Validate action
    action = kwargs.get('action')
    if not action:
        raise ValueError("'action' is required")
    
    if action not in policy_helpers.VALID_BODY_ACTION:
        valid_options = ", ".join(policy_helpers.VALID_BODY_ACTION)
        raise ValueError(
            f"Invalid action '{action}'.\\n"
            f"Valid options are: {valid_options}\\n"
            f"Did you mean 'accept' instead of 'allow'?"
        )
    
    # Validate status
    status = kwargs.get('status', 'enable')
    if status not in policy_helpers.VALID_BODY_STATUS:
        raise ValueError(
            f"Invalid status '{status}'. "
            f"Use 'enable' or 'disable' (not 'enabled' or 'disabled')"
        )
    
    # All validations passed - create policy
    return fgt.firewall.policy.create(**kwargs)
```

---

## Best Practices

### 1. ✅ Always Validate User Input

```python
# Good: Validate before sending to FortiGate
def create_address_from_user_input(name, addr_type, value):
    if addr_type not in address_helpers.VALID_BODY_TYPE:
        raise ValueError(f"Invalid type. Choose from: {address_helpers.VALID_BODY_TYPE}")
    
    fgt.api.cmdb.firewall.address.create(name=name, type=addr_type, subnet=value)

# Bad: No validation
def create_address_from_user_input(name, addr_type, value):
    fgt.api.cmdb.firewall.address.create(name=name, type=addr_type, subnet=value)
```

### 2. ✅ Provide Helpful Error Messages

```python
# Good: Clear, actionable error
if action not in VALID_BODY_ACTION:
    raise ValueError(
        f"Invalid action '{action}'. "
        f"Valid options: {', '.join(VALID_BODY_ACTION)}"
    )

# Bad: Generic error
if action not in VALID_BODY_ACTION:
    raise ValueError("Invalid action")
```

### 3. ✅ Cache Validators for Performance

```python
# Good: Cache validator lookups
class PolicyManager:
    def __init__(self):
        from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy
        self.valid_actions = policy.VALID_BODY_ACTION
        self.valid_status = policy.VALID_BODY_STATUS
    
    def validate_action(self, action):
        return action in self.valid_actions

# Bad: Repeated imports
def validate_action(action):
    from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy
    return action in policy.VALID_BODY_ACTION
```

### 4. ✅ Document Validation Requirements

```python
def create_policy(name: str, action: str, **kwargs):
    """
    Create firewall policy.
    
    Args:
        name: Policy name
        action: Policy action. Valid values: 'accept', 'deny', 'ipsec'
        **kwargs: Additional policy parameters
    
    Raises:
        ValueError: If action is not valid
    
    Valid actions can be found in:
        hfortix.FortiOS.api.v2.cmdb.firewall._helpers.policy.VALID_BODY_ACTION
    """
    if action not in VALID_BODY_ACTION:
        raise ValueError(f"Invalid action. See docstring for valid values.")
    
    # ... rest of implementation
```

---

## Limitations and Future Enhancements

### Current Limitations

⚠️ **Required Field Validation NOT Implemented**
- Validators don't currently check for required fields
- Planned for next release (v0.3.22)
- Example: Policy requires name, srcintf, dstintf, srcaddr, dstaddr, action

⚠️ **Relationship Validation NOT Implemented**
- Cross-field validation not available
- Example: NAT enabled should require poolname/natip
- Planned for future release

⚠️ **No Automatic Validation in API Methods**
- Current validators are constants only
- You must manually validate before API calls
- Auto-validation in convenience wrappers planned

### Planned Enhancements (v0.3.22+)

📋 **Required Field Validation**
```python
# Planned for next release
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy

# Check required fields
missing = policy.validate_required_fields({
    'name': 'test',
    'srcintf': ['port1']
    # Missing: dstintf, srcaddr, dstaddr, action, schedule, service
})

if missing:
    raise ValueError(f"Missing required fields: {', '.join(missing)}")
```

📋 **Relationship Validation**
```python
# Planned for future release
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy

# Validate cross-field dependencies
errors = policy.validate_relationships({
    'nat': 'enable',  # NAT is enabled
    # Missing poolname - should error
})
```

📋 **Automatic Validation in Wrappers**
```python
# Planned for future release
# Validation happens automatically
fgt.firewall.policy.create(
    name="test",
    action="invalid"  # Raises ValidationError automatically
)
```

---

## Troubleshooting

### Issue: Can't Find Validator

**Problem:** Import error when trying to access validator

```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import nonexistent
# ImportError: cannot import name 'nonexistent'
```

**Solution:** Check the endpoint path in the API

```python
# Correct paths:
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers import policy  # /firewall/policy
from hfortix.FortiOS.api.v2.cmdb.firewall.service._helpers import custom  # /firewall/service/custom
from hfortix.FortiOS.api.v2.cmdb.system._helpers import interface  # /system/interface
```

### Issue: Constants are Empty

**Problem:** Validator constant exists but is empty

```python
print(policy.VALID_BODY_UNKNOWN)  # []
```

**Solution:** Not all parameters have enum validation. Check the OpenAPI spec or FortiOS documentation for that parameter.

### Issue: Value Seems Valid but Not in List

**Problem:** Value works in FortiGate GUI but not in validator

```python
# "allow" works in GUI but not in API
policy.VALID_BODY_ACTION  # ['accept', 'deny', 'ipsec']
```

**Solution:** FortiOS API and GUI sometimes use different values. Use API values:
- GUI: "allow" → API: "accept"
- GUI: "enabled" → API: "enable"
- GUI: "disabled" → API: "disable"

---

## Reference

### All 77 Categories with Validators

**CMDB (37):** alertemail, antivirus, application, authentication, automation, casb, certificate, diameter-filter, dlp, dnsfilter, emailfilter, endpoint-control, ethernet-oam, extension-controller, file-filter, firewall, ftp-proxy, icap, ips, log, monitoring, report, router, rule, sctp-filter, switch-controller, system, user, videofilter, virtual-patch, voip, vpn, waf, web-proxy, webfilter, wireless-controller, ztna

**Monitor (32):** firewall, system, vpn, router, user, wifi, switch-controller, log, webfilter, ips, waf, antivirus, dlp, dnsfilter, spamfilter, webproxy, casb, emailfilter, videofilter, virtual-patch, gtp, certificate, network, nsx, endpoint-control, extension-controller, license, utm, utmProxy, fortiview, ...

**Log (5):** disk, memory, fortianalyzer, forticloud, syslogd

**Service (3):** sniffer, security-rating, system

---

## Additional Resources

- **[API Coverage](../API_COVERAGE.md)** - Complete API implementation status
- **[Quick Start Guide](../QUICKSTART.md)** - Getting started with hfortix
- **[Examples Directory](../examples/)** - Working code samples
- **[FortiOS API Docs](https://docs.fortinet.com/)** - Official Fortinet documentation

---

**Questions?** Open an issue on GitHub: https://github.com/hermanwjacobsen/hfortix/issues
