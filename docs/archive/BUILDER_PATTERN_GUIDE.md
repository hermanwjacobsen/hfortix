# Builder Pattern Implementation Guide

## Overview

The **Builder Pattern** in hfortix eliminates code duplication across API endpoints by centralizing common payload construction logic into reusable helper functions.

**Version:** 0.3.21  
**Status:** Phase 1 Complete (Firewall Policy Only)  
**Impact:** 454 lines removed (-13% reduction)  
**Planned:** 30+ resources to follow

---

## What is the Builder Pattern?

The Builder Pattern separates complex object construction from its representation, allowing the same construction process to create different representations.

### Benefits

✅ **Eliminates Code Duplication** - Build once, use everywhere  
✅ **Consistent Behavior** - Same logic across API and wrapper layers  
✅ **Easier Maintenance** - Fix bugs in one place  
✅ **Better Testing** - Test builders once, not every method  
✅ **Flexible Input Formats** - Support dictionaries, keywords, or mixed

---

## Architecture

### Two-Layer Design

```
User Code
   ↓
Wrapper Layer (firewallPolicy.py)
   ↓
build_policy_payload_normalized()  ← Normalizes flexible inputs
   ↓
API Layer (policy.py)
   ↓
build_policy_payload()             ← Builds raw payload
   ↓
FortiGate REST API
```

### Layer Responsibilities

**API Layer** (`policy.py`):
- Direct 1:1 mapping to FortiOS API
- No data transformation
- Accepts exact API format

**Wrapper Layer** (`firewallPolicy.py`):
- User-friendly interface
- Accepts flexible input formats
- Normalizes data before sending to API

---

## Phase 1: Firewall Policy (Complete)

### Implementation Details

**Files:**
- `hfortix/FortiOS/api/v2/cmdb/firewall/policy.py` (API layer)
- `hfortix/FortiOS/firewall/firewallPolicy.py` (Wrapper layer)
- `hfortix/FortiOS/api/v2/cmdb/firewall/_helpers/policy_helpers.py` (Builders)

**Results:**
- **policy.py:** 1796 → 1381 lines (-415 lines, -23%)
- **firewallPolicy.py:** 1703 → 1541 lines (-162 lines, -10%)
- **Total:** 454 lines removed

### Builder Functions

#### 1. `build_policy_payload()` - API Layer

**Purpose:** Construct payload dictionary from individual parameters (no normalization)

**Location:** `hfortix/FortiOS/api/v2/cmdb/firewall/_helpers/policy_helpers.py`

**Usage:**
```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers.policy_helpers import build_policy_payload

# Build payload from kwargs
payload = build_policy_payload(
    name="Allow-Web",
    srcintf=["port1"],
    dstintf=["port2"],
    srcaddr=["all"],
    dstaddr=["all"],
    action="accept",
    schedule="always",
    service=["HTTP", "HTTPS"]
)

# Result: {'name': 'Allow-Web', 'srcintf': ['port1'], ...}
```

**Signature:**
```python
def build_policy_payload(
    policyid: str | None = None,
    payload_dict: dict[str, Any] | None = None,
    **kwargs: Any
) -> dict[str, Any]:
    """
    Build policy payload dictionary.

    Args:
        policyid: Policy ID (optional)
        payload_dict: Base dictionary to start with
        **kwargs: Individual policy parameters

    Returns:
        Complete payload dictionary for API call
    """
```

#### 2. `build_policy_payload_normalized()` - Wrapper Layer

**Purpose:** Build payload with input normalization (flexible formats)

**Location:** `hfortix/FortiOS/api/v2/cmdb/firewall/_helpers/policy_helpers.py`

**Usage:**
```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers.policy_helpers import (
    build_policy_payload_normalized
)

# Accepts flexible inputs
payload = build_policy_payload_normalized(
    name="Allow-Web",
    srcintf="port1",              # String → normalized to ['port1']
    dstintf=["port2"],            # List → stays as list
    srcaddr="Office-Net",         # String → normalized to ['Office-Net']
    dstaddr=["all"],
    action="accept"
)

# Result: All interface/address fields normalized to lists
```

**Signature:**
```python
def build_policy_payload_normalized(
    policyid: str | None = None,
    payload_dict: dict[str, Any] | None = None,
    **kwargs: Any
) -> dict[str, Any]:
    """
    Build policy payload with input normalization.

    Normalizes the following fields to lists:
    - srcintf, dstintf
    - srcaddr, dstaddr, srcaddr6, dstaddr6
    - service, internet-service-src-name, internet-service-name
    - poolname, groups, users

    Args:
        policyid: Policy ID (optional)
        payload_dict: Base dictionary to start with
        **kwargs: Individual policy parameters (will be normalized)

    Returns:
        Complete payload dictionary with normalized lists
    """
```

#### 3. `normalize_to_name_list()` - Helper Function

**Purpose:** Convert flexible input formats to standardized list format

**Usage:**
```python
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers.policy_helpers import (
    normalize_to_name_list
)

# String → List of dicts
result = normalize_to_name_list("port1")
# Result: [{'name': 'port1'}]

# List of strings → List of dicts
result = normalize_to_name_list(["port1", "port2"])
# Result: [{'name': 'port1'}, {'name': 'port2'}]

# Dict → List of dicts
result = normalize_to_name_list({"name": "port1"})
# Result: [{'name': 'port1'}]

# List of dicts → Unchanged
result = normalize_to_name_list([{"name": "port1"}, {"name": "port2"}])
# Result: [{'name': 'port1'}, {'name': 'port2'}]
```

---

## Usage Examples

### Example 1: API Layer (No Normalization)

```python
from hfortix import FortiOS

fgt = FortiOS("192.168.1.1", token="your_token_here")

# API layer: Exact format required
fgt.api.cmdb.firewall.policy.create(
    name="Allow-Web",
    srcintf=[{"name": "port1"}],     # Must be list of dicts
    dstintf=[{"name": "port2"}],     # Must be list of dicts
    srcaddr=[{"name": "all"}],       # Must be list of dicts
    dstaddr=[{"name": "all"}],       # Must be list of dicts
    action="accept",
    schedule="always",
    service=[{"name": "HTTP"}]       # Must be list of dicts
)
```

### Example 2: Wrapper Layer (With Normalization)

```python
from hfortix import FortiOS

fgt = FortiOS("192.168.1.1", token="your_token_here")

# Wrapper layer: Flexible formats
fgt.firewall.policy.create(
    name="Allow-Web",
    srcintf="port1",                 # ✅ String works
    dstintf=["port2"],               # ✅ List of strings works
    srcaddr="all",                   # ✅ String works
    dstaddr=["all"],                 # ✅ List works
    action="accept",
    schedule="always",
    service=["HTTP", "HTTPS"]        # ✅ List of strings works
)

# All inputs automatically normalized to API format
```

### Example 3: Mixed Dictionary and Kwargs

```python
# Start with a base configuration
base_policy = {
    "srcintf": ["port1"],
    "dstintf": ["port2"],
    "action": "accept",
    "schedule": "always"
}

# Override specific fields with kwargs
fgt.firewall.policy.create(
    payload_dict=base_policy,
    name="Custom-Policy",            # Override
    srcaddr=["Office-Net"],          # Override
    dstaddr=["all"],                 # Override
    service=["HTTP", "HTTPS"]        # Override
)
```

---

## Implementation Pattern

### Step 1: Create Helper Module

Create `_helpers/<resource>_helpers.py`:

```python
# hfortix/FortiOS/api/v2/cmdb/firewall/_helpers/address_helpers.py

from typing import Any

def build_address_payload(
    name: str | None = None,
    payload_dict: dict[str, Any] | None = None,
    **kwargs: Any
) -> dict[str, Any]:
    """
    Build address object payload dictionary.

    Args:
        name: Address object name
        payload_dict: Base dictionary to start with
        **kwargs: Additional address parameters

    Returns:
        Complete payload dictionary
    """
    # Start with payload_dict or empty dict
    payload = payload_dict.copy() if payload_dict else {}

    # Add name if provided
    if name is not None:
        payload["name"] = name

    # Add all other kwargs
    payload.update(kwargs)

    return payload
```

### Step 2: Refactor API Layer

Before:
```python
def create(
    self,
    name: str | None = None,
    subnet: str | None = None,
    type: str | None = None,
    payload_dict: dict[str, Any] | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    # Duplicate payload building logic
    params = payload_dict.copy() if payload_dict else {}
    if name is not None:
        params["name"] = name
    if subnet is not None:
        params["subnet"] = subnet
    if type is not None:
        params["type"] = type
    params.update(kwargs)

    return self._client.post("cmdb", "/firewall/address", data=params)
```

After:
```python
def create(
    self,
    name: str | None = None,
    subnet: str | None = None,
    type: str | None = None,
    payload_dict: dict[str, Any] | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    # Use builder function
    payload = build_address_payload(
        name=name,
        subnet=subnet,
        type=type,
        payload_dict=payload_dict,
        **kwargs
    )

    return self._client.post("cmdb", "/firewall/address", data=payload)
```

### Step 3: Create Wrapper Layer

```python
# hfortix/FortiOS/firewall/firewallAddress.py

class FirewallAddress:
    """Convenience wrapper for firewall address operations."""

    def __init__(self, fortios_instance):
        self._fgt = fortios_instance

    def create(
        self,
        name: str,
        subnet: str | None = None,
        type: str | None = None,
        **kwargs
    ):
        """
        Create address object with user-friendly interface.

        Args:
            name: Address name
            subnet: IP subnet (e.g., '10.0.0.0/24')
            type: Address type (default: 'ipmask')
            **kwargs: Additional parameters
        """
        return self._fgt.api.cmdb.firewall.address.create(
            name=name,
            subnet=subnet,
            type=type or "ipmask",
            **kwargs
        )
```

---

## Testing

### Unit Tests for Builders

```python
import pytest
from hfortix.FortiOS.api.v2.cmdb.firewall._helpers.policy_helpers import (
    build_policy_payload,
    build_policy_payload_normalized,
    normalize_to_name_list
)

def test_build_policy_payload():
    """Test basic payload building."""
    payload = build_policy_payload(
        name="test",
        srcintf=["port1"],
        action="accept"
    )

    assert payload["name"] == "test"
    assert payload["srcintf"] == ["port1"]
    assert payload["action"] == "accept"

def test_build_policy_payload_with_dict():
    """Test payload building with base dict."""
    base = {"srcintf": ["port1"], "dstintf": ["port2"]}
    payload = build_policy_payload(
        payload_dict=base,
        name="test"
    )

    assert payload["name"] == "test"
    assert payload["srcintf"] == ["port1"]

def test_normalize_to_name_list():
    """Test input normalization."""
    # String input
    result = normalize_to_name_list("port1")
    assert result == [{"name": "port1"}]

    # List of strings
    result = normalize_to_name_list(["port1", "port2"])
    assert result == [{"name": "port1"}, {"name": "port2"}]

    # Already normalized
    input_data = [{"name": "port1"}]
    result = normalize_to_name_list(input_data)
    assert result == input_data
```

### Integration Tests

```python
def test_policy_create_with_builder(fgt):
    """Test policy creation using builder pattern."""
    # Should work with both API and wrapper layers

    # API layer (exact format)
    fgt.api.cmdb.firewall.policy.create(
        name="test-api",
        srcintf=[{"name": "port1"}],
        dstintf=[{"name": "port2"}],
        action="accept"
    )

    # Wrapper layer (flexible format)
    fgt.firewall.policy.create(
        name="test-wrapper",
        srcintf="port1",              # Normalized automatically
        dstintf=["port2"],
        action="accept"
    )

    # Both should succeed
```

---

## Phase 2: Planned Resources

### High Priority (Next Sprint)

1. **Firewall Address** - Most commonly used
2. **Service Custom** - Second most common
3. **Address Group** - Group management
4. **Service Group** - Service groups
5. **IPPool** - NAT pools
6. **VIP** - Virtual IPs

### Implementation Checklist Per Resource

- [ ] Create `_helpers/<resource>_helpers.py`
- [ ] Implement `build_<resource>_payload()`
- [ ] Implement `build_<resource>_payload_normalized()` (if needed)
- [ ] Refactor API layer methods (create, update)
- [ ] Create convenience wrapper class
- [ ] Add wrapper to main FortiOS class
- [ ] Write unit tests for builders
- [ ] Write integration tests
- [ ] Update documentation

---

## Benefits Summary

### Code Reduction

**Phase 1 (Firewall Policy):**
- 454 lines removed
- 13% reduction

**Projected Phase 2 (6 resources):**
- ~1,500 lines estimated reduction
- ~15% average reduction

### Maintenance Benefits

**Before:**
- Bug fix requires changes in 2 places (create + update)
- Different behavior between methods
- Hard to test comprehensively

**After:**
- Bug fix in one place (builder function)
- Consistent behavior guaranteed
- Easy unit testing of builders

### User Experience

**Before:**
```python
# Must use exact API format
fgt.api.cmdb.firewall.policy.create(
    srcintf=[{"name": "port1"}],  # Tedious
    dstintf=[{"name": "port2"}]
)
```

**After:**
```python
# Natural, Pythonic interface
fgt.firewall.policy.create(
    srcintf="port1",     # ✅ Much easier!
    dstintf="port2"
)
```

---

## Best Practices

### 1. ✅ Keep Builders Simple

```python
# Good: Simple, focused builder
def build_address_payload(name=None, subnet=None, **kwargs):
    payload = {}
    if name:
        payload["name"] = name
    if subnet:
        payload["subnet"] = subnet
    payload.update(kwargs)
    return payload

# Bad: Too complex, business logic in builder
def build_address_payload(name=None, subnet=None, **kwargs):
    # Validation, transformation, API calls - too much!
    if not validate_subnet(subnet):
        raise ValueError("Invalid subnet")
    resolved_name = lookup_name_in_database(name)
    # ... more complexity
```

### 2. ✅ Separate API and Wrapper Concerns

**API Layer:**
- No normalization
- Exact API format
- Minimal logic

**Wrapper Layer:**
- Normalize inputs
- Provide defaults
- User-friendly interface

### 3. ✅ Test Builders Independently

```python
# Test builders without API calls
def test_builder():
    payload = build_policy_payload(name="test", action="accept")
    assert payload == {"name": "test", "action": "accept"}

# Test integration separately
def test_api_integration(fgt):
    result = fgt.api.cmdb.firewall.policy.create(name="test")
    assert result["status"] == "success"
```

---

## Migration Guide

### For Users

**No Breaking Changes!** Both interfaces work:

```python
# Old way still works
fgt.api.cmdb.firewall.policy.create(
    payload_dict={"name": "test", "action": "accept"}
)

# New way also works
fgt.firewall.policy.create(
    name="test",
    action="accept"
)
```

### For Developers

When adding new resources:

1. Create helper module first
2. Implement builders with tests
3. Refactor API layer to use builders
4. Create wrapper layer
5. Update documentation

---

## Additional Resources

- **[Code Examples](../examples/firewall_policy_examples.py)** - Firewall policy examples
- **[API Reference](ENDPOINT_METHODS.md)** - Complete endpoint documentation
- **[Firewall Policy Wrapper Guide](FIREWALL_POLICY_WRAPPER.md)** - High-level wrapper documentation

---

**Questions?** Open an issue on GitHub: https://github.com/hermanwjacobsen/hfortix/issues
