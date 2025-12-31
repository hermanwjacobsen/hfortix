# Traffic Shaper Convenience Wrappers

**Version:** 0.3.38+  
**Status:** Production Ready

Convenience wrappers for FortiOS traffic shaping configuration with comprehensive parameter validation and intuitive interfaces.

## Table of Contents

- [Overview](#overview)
- [Available Wrappers](#available-wrappers)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
- [Important Limitations](#important-limitations)
- [Examples](#examples)
- [Related Documentation](#related-documentation)

---

## Overview

The traffic shaper wrappers provide a clean, Pythonic interface to FortiOS traffic shaping features with:

- ✅ **Full parameter support** - All FortiOS parameters with validation
- ✅ **Type safety** - Literal types for enum values
- ✅ **Input validation** - Range checking and type validation
- ✅ **Comprehensive documentation** - Detailed docstrings for all methods
- ⚠️ **Known limitations** - Rename operations not supported (FortiOS API limitation)

## Available Wrappers

### 1. Per-IP Shaper (`ShaperPerIp`)

Controls bandwidth and session limits per source IP address.

**Access:** `fgt.firewall.shaper_per_ip`

**Use Cases:**
- Limit bandwidth per user/device
- Control concurrent sessions per IP
- Apply different limits for upload/download (via DiffServ)

### 2. Traffic Shaper (`TrafficShaper`)

Shared traffic shaper with guaranteed/maximum bandwidth and priority.

**Access:** `fgt.firewall.traffic_shaper`

**Use Cases:**
- Guarantee bandwidth for critical applications
- Set maximum bandwidth caps
- Prioritize traffic classes
- Apply QoS markings (DSCP, CoS)

---

## Quick Start

```python
from hfortix import FortiOS

# Initialize connection
fgt = FortiOS(
    host="fortigate.example.com",
    token="your-api-token",
    verify=False
)

# Create a per-IP shaper
fgt.firewall.shaper_per_ip.create(
    name="user-limit",
    max_bandwidth=5000,
    bandwidth_unit="kbps",
    max_concurrent_session=100
)

# Create a traffic shaper
fgt.firewall.traffic_shaper.create(
    name="critical-apps",
    guaranteed_bandwidth=10000,
    maximum_bandwidth=50000,
    bandwidth_unit="mbps",
    priority="high"
)

# Update shaper settings
fgt.firewall.traffic_shaper.update(
    name="critical-apps",
    maximum_bandwidth=100000
)

# Check if shaper exists
if fgt.firewall.shaper_per_ip.exists("user-limit"):
    print("Shaper exists!")

# Delete a shaper
fgt.firewall.shaper_per_ip.delete(name="user-limit")
```

---

## API Reference

### ShaperPerIp Methods

#### `create()`
Create a new per-IP traffic shaper.

```python
fgt.firewall.shaper_per_ip.create(
    name: str,                                    # Required
    max_bandwidth: int = None,                     # 0-80000000
    bandwidth_unit: Literal["kbps", "mbps", "gbps"] = None,
    max_concurrent_session: int = None,            # 0-2097000
    max_concurrent_tcp_session: int = None,        # 0-2097000
    max_concurrent_udp_session: int = None,        # 0-2097000
    diffserv_forward: Literal["enable", "disable"] = None,
    diffserv_reverse: Literal["enable", "disable"] = None,
    diffservcode_forward: str = None,              # 6-bit binary
    diffservcode_rev: str = None,                  # 6-bit binary
    vdom: str = None
)
```

**Parameters:**
- `name`: Shaper name (max 35 characters)
- `max_bandwidth`: Upper bandwidth limit (0-80000000)
- `bandwidth_unit`: Unit of measurement (kbps/mbps/gbps)
- `max_concurrent_session`: Maximum concurrent sessions (0-2097000)
- `max_concurrent_tcp_session`: Maximum TCP sessions (0-2097000)
- `max_concurrent_udp_session`: Maximum UDP sessions (0-2097000)
- `diffserv_forward`: Enable/disable forward DiffServ
- `diffserv_reverse`: Enable/disable reverse DiffServ
- `diffservcode_forward`: Forward DiffServ code (6-bit binary)
- `diffservcode_rev`: Reverse DiffServ code (6-bit binary)

#### `get()`
Retrieve per-IP shaper configuration.

```python
# Get all shapers
all_shapers = fgt.firewall.shaper_per_ip.get()

# Get specific shaper
shaper = fgt.firewall.shaper_per_ip.get(name="user-limit")
```

#### `update()`
Update an existing per-IP shaper (same parameters as `create()`).

```python
fgt.firewall.shaper_per_ip.update(
    name="user-limit",
    max_bandwidth=10000,
    bandwidth_unit="kbps"
)
```

#### `delete()`
Delete a per-IP shaper.

```python
fgt.firewall.shaper_per_ip.delete(name="user-limit")
```

#### `exists()`
Check if a per-IP shaper exists.

```python
exists = fgt.firewall.shaper_per_ip.exists("user-limit")
```

#### `rename()` ⚠️ NOT SUPPORTED
```python
# This will raise NotImplementedError
fgt.firewall.shaper_per_ip.rename("old-name", "new-name")
# NotImplementedError: FortiOS does not support renaming per-IP shapers
```

---

### TrafficShaper Methods

#### `create()`
Create a new traffic shaper.

```python
fgt.firewall.traffic_shaper.create(
    name: str,                                    # Required
    guaranteed_bandwidth: int = None,              # 0-80000000
    maximum_bandwidth: int = None,                 # 0-80000000
    bandwidth_unit: Literal["kbps", "mbps", "gbps"] = None,
    priority: Literal["low", "medium", "high"] = None,
    per_policy: Literal["enable", "disable"] = None,
    diffserv: Literal["enable", "disable"] = None,
    diffservcode: str = None,                      # 6-bit binary
    dscp_marking_method: Literal["multi-stage", "static"] = None,
    exceed_bandwidth: int = None,                  # 0-80000000
    exceed_dscp: str = None,                       # 6-bit binary
    maximum_dscp: str = None,                      # 6-bit binary
    cos_marking: Literal["enable", "disable"] = None,
    cos_marking_method: Literal["multi-stage", "static"] = None,
    cos: str = None,                               # 3-bit binary
    exceed_cos: str = None,                        # 3-bit binary
    maximum_cos: str = None,                       # 3-bit binary
    overhead: int = None,                          # 0-100
    exceed_class_id: int = None,                   # 0-4294967295
    vdom: str = None
)
```

**Key Parameters:**
- `name`: Shaper name (max 35 characters)
- `guaranteed_bandwidth`: Minimum guaranteed bandwidth
- `maximum_bandwidth`: Maximum allowed bandwidth
- `bandwidth_unit`: Unit of measurement (kbps/mbps/gbps)
- `priority`: Traffic priority (low/medium/high)
- `per_policy`: Apply per policy
- `diffserv`: Enable DiffServ marking
- `dscp_marking_method`: DSCP marking method
- `cos_marking`: Enable CoS marking (requires VLAN)
- `overhead`: Overhead percentage (0-100)

#### `get()`, `update()`, `delete()`, `exists()`
Same usage as `ShaperPerIp` methods.

#### `rename()` ⚠️ NOT SUPPORTED
```python
# This will raise NotImplementedError
fgt.firewall.traffic_shaper.rename("old-name", "new-name")
# NotImplementedError: FortiOS does not support renaming traffic shapers
```

---

## Important Limitations

### ⚠️ Rename Operations Not Supported

FortiOS uses the `name` field as the **immutable primary key** for shaper objects. Unlike shaping policies which use numeric IDs, shapers cannot be renamed after creation.

**Why?**
- Shaper endpoints use name-based URLs: `/firewall.shaper/traffic-shaper/{name}`
- The name in the URL is the primary key
- FortiOS API silently ignores rename attempts

**What happens if I try?**
```python
fgt.firewall.traffic_shaper.rename("old-name", "new-name")
# Raises: NotImplementedError with explanation
```

**Workaround:**
To rename a shaper:
1. Create a new shaper with the desired name
2. Update all policies/rules that reference the old shaper
3. Delete the old shaper

⚠️ **Warning:** This will break any policies referencing the old shaper name until updated.

**Comparison:**

| Endpoint Type | Primary Key | Rename Support |
|--------------|-------------|----------------|
| Per-IP Shaper | `name` (string) | ❌ Not supported |
| Traffic Shaper | `name` (string) | ❌ Not supported |
| **Shaping Policy** | `id` (integer) | ✅ **Supported** |

---

## Examples

### Example 1: Basic Bandwidth Limiting

```python
# Limit users to 10 Mbps
fgt.firewall.shaper_per_ip.create(
    name="standard-user-10mbps",
    max_bandwidth=10,
    bandwidth_unit="mbps"
)

# Create shared shaper for guest network
fgt.firewall.traffic_shaper.create(
    name="guest-network-limit",
    guaranteed_bandwidth=5,
    maximum_bandwidth=20,
    bandwidth_unit="mbps",
    priority="low"
)
```

### Example 2: Session Limiting

```python
# Limit concurrent sessions per IP
fgt.firewall.shaper_per_ip.create(
    name="session-limited-user",
    max_concurrent_session=200,      # Total sessions
    max_concurrent_tcp_session=150,  # TCP sessions
    max_concurrent_udp_session=50    # UDP sessions
)
```

### Example 3: Priority-Based Traffic Shaping

```python
# High priority for critical apps
fgt.firewall.traffic_shaper.create(
    name="critical-apps-high",
    guaranteed_bandwidth=50,
    maximum_bandwidth=200,
    bandwidth_unit="mbps",
    priority="high",
    diffserv="enable",
    dscp_marking_method="static"
)

# Medium priority for business apps
fgt.firewall.traffic_shaper.create(
    name="business-apps-medium",
    guaranteed_bandwidth=20,
    maximum_bandwidth=100,
    bandwidth_unit="mbps",
    priority="medium"
)

# Low priority for bulk traffic
fgt.firewall.traffic_shaper.create(
    name="bulk-traffic-low",
    guaranteed_bandwidth=5,
    maximum_bandwidth=50,
    bandwidth_unit="mbps",
    priority="low"
)
```

### Example 4: DiffServ Marking

```python
# Forward DiffServ marking
fgt.firewall.shaper_per_ip.create(
    name="dscp-marked-traffic",
    max_bandwidth=100,
    bandwidth_unit="mbps",
    diffserv_forward="enable",
    diffservcode_forward="101110",  # EF (Expedited Forwarding)
    diffserv_reverse="enable",
    diffservcode_rev="000000"       # Best effort
)
```

### Example 5: Bulk Operations

```python
# Create multiple shapers for different user tiers
tiers = {
    "bronze": {"max_bw": 10, "sessions": 50},
    "silver": {"max_bw": 25, "sessions": 100},
    "gold": {"max_bw": 50, "sessions": 200},
    "platinum": {"max_bw": 100, "sessions": 500}
}

for tier, limits in tiers.items():
    fgt.firewall.shaper_per_ip.create(
        name=f"user-tier-{tier}",
        max_bandwidth=limits["max_bw"],
        bandwidth_unit="mbps",
        max_concurrent_session=limits["sessions"]
    )
    print(f"Created shaper for {tier} tier")
```

### Example 6: Checking and Updating

```python
# Check if shaper exists before creating
shaper_name = "my-shaper"

if not fgt.firewall.traffic_shaper.exists(shaper_name):
    # Create new shaper
    fgt.firewall.traffic_shaper.create(
        name=shaper_name,
        guaranteed_bandwidth=10,
        maximum_bandwidth=50,
        bandwidth_unit="mbps"
    )
else:
    # Update existing shaper
    fgt.firewall.traffic_shaper.update(
        name=shaper_name,
        maximum_bandwidth=100  # Increase limit
    )
```

### Example 7: Error Handling

```python
try:
    fgt.firewall.shaper_per_ip.create(
        name="invalid-shaper",
        max_bandwidth=100000000,  # Too high!
        bandwidth_unit="kbps"
    )
except ValueError as e:
    print(f"Validation error: {e}")
    # Output: max_bandwidth must be between 0 and 80000000

try:
    fgt.firewall.traffic_shaper.rename("old", "new")
except NotImplementedError as e:
    print(f"Operation not supported: {e}")
    # Output: FortiOS does not support renaming traffic shapers
```

---

## Validation Rules

### Name Validation
- **Max length:** 35 characters
- **Pattern:** Alphanumeric, hyphens, underscores
- **Case sensitive**

### Bandwidth Validation
- **Range:** 0-80,000,000
- **Units:** kbps, mbps, gbps
- **Integer values only**

### Session Limits
- **Range:** 0-2,097,000
- **Applies to:** max_concurrent_session, max_concurrent_tcp_session, max_concurrent_udp_session

### Priority Values
- **Valid:** "low", "medium", "high"
- **Case sensitive**

### Enable/Disable Values
- **Valid:** "enable", "disable"
- **Case sensitive**

### DiffServ Codes
- **Format:** 6-bit binary string
- **Example:** "101110" (EF - Expedited Forwarding)
- **Common values:**
  - `000000` - Best Effort (BE)
  - `001000` - Class Selector 1 (CS1)
  - `010000` - Class Selector 2 (CS2)
  - `011000` - Class Selector 3 (CS3)
  - `100000` - Class Selector 4 (CS4)
  - `101000` - Class Selector 5 (CS5)
  - `101110` - Expedited Forwarding (EF)
  - `001010` - Assured Forwarding 11 (AF11)

### CoS (Class of Service)
- **Format:** 3-bit binary string
- **Example:** "011" (Priority 3)
- **Range:** "000" to "111" (0-7)
- **Note:** Requires VLAN configuration

### Overhead
- **Range:** 0-100 (percentage)
- **Use:** Account for protocol overhead

### Class ID
- **Range:** 0-4,294,967,295
- **Use:** Traffic class identification

---

## Related Documentation

- **[FIREWALL_POLICY_WRAPPER.md](FIREWALL_POLICY_WRAPPER.md)** - Using shapers in firewall policies
- **[API_COVERAGE.md](API_COVERAGE.md)** - Complete API endpoint coverage
- **[ERROR_HANDLING_CONFIG.md](ERROR_HANDLING_CONFIG.md)** - Error handling configuration
- **[VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)** - Input validation details

---

## Troubleshooting

### Issue: Rename Not Working

**Problem:** Trying to rename a shaper doesn't change the name.

**Solution:** This is expected behavior. FortiOS does not support renaming shapers. See [Important Limitations](#important-limitations) above.

### Issue: CoS Marking Not Working

**Problem:** CoS parameters have no effect.

**Solution:** CoS marking requires VLAN configuration. Ensure:
1. Traffic is tagged with VLAN
2. Interface supports 802.1Q
3. CoS marking is enabled on the interface

### Issue: Shaper Not Applied

**Problem:** Created shaper but traffic not shaped.

**Solution:** Shapers must be referenced in:
- Firewall policies (via `traffic_shaper`, `per_ip_shaper` parameters)
- Interface settings
- Shaping policies

Example:
```python
# Create shaper
fgt.firewall.traffic_shaper.create(
    name="limit-100mbps",
    maximum_bandwidth=100,
    bandwidth_unit="mbps"
)

# Apply in firewall policy
fgt.firewall.policy.create(
    name="shaped-policy",
    srcintf=["port1"],
    dstintf=["port2"],
    srcaddr=["all"],
    dstaddr=["all"],
    service=["ALL"],
    traffic_shaper="limit-100mbps",  # Reference the shaper
    action="accept"
)
```

---

## Version History

- **v0.3.38** - Initial release of shaper convenience wrappers
  - Full parameter support for per-IP shaper and traffic shaper
  - Comprehensive validation
  - Documented rename limitation
  - Complete test coverage (20 tests passing)

---

## Contributing

Found a bug or have a feature request? Please open an issue on GitHub.

For questions about FortiOS traffic shaping configuration, see the official Fortinet documentation.
