# Error Handling Configuration Guide

## Overview

The convenience wrappers (e.g., `fgt.firewall.policy.create()`) now support configurable error handling with two independent settings:

1. **error_mode**: Controls whether the program stops or continues when errors occur
2. **error_format**: Controls how much detail is included in error messages

## Configuration Levels

### Level 1: FortiOS Instance (affects all wrapper calls)

```python
fgt = FortiOS(
    host="192.0.2.10",
    token="your-token-here",
    error_mode="raise",      # "raise" | "return" | "log"
    error_format="detailed"  # "detailed" | "simple" | "code_only"
)
```

### Level 2: Per Method Call (overrides instance defaults)

```python
result = fgt.firewall.policy.create(
    name="MyPolicy",
    srcintf="port1",
    dstintf="port2",
    srcaddr="all",
    dstaddr="all",
    action="accept",
    error_mode="return",     # Override for this call only
    error_format="simple"    # Override for this call only
)
```

## Error Modes

### Mode: "raise" (DEFAULT)

**Behavior**: Raises exception when error occurs

**Program flow**: STOPS (unless you use try/except)

**Use when**: Errors are critical and must be handled immediately

```python
fgt = FortiOS(host="...", token="...", error_mode="raise")

# ❌ WITHOUT try/except - Program CRASHES
fgt.firewall.policy.create(name="DuplicatePolicy", ...)
print("This never executes")  # DEAD CODE

# ✅ WITH try/except - Program CONTINUES
try:
    fgt.firewall.policy.create(name="DuplicatePolicy", ...)
except DuplicateEntryError:
    print("Policy exists, handling...")
print("This executes")  # RUNS
```

### Mode: "return"

**Behavior**: Returns error dictionary instead of raising

**Program flow**: NEVER stops (always continues)

**Use when**: Batch operations where you want to try everything and collect results

```python
fgt = FortiOS(host="...", token="...", error_mode="return")

# Program ALWAYS continues
result = fgt.firewall.policy.create(name="DuplicatePolicy", ...)

# Check if it worked
if result.get("status") == "error":
    print(f"Failed: {result['error_code']}")
else:
    print("Success!")

# Try multiple operations - ALL execute
for i in range(100):
    result = fgt.firewall.policy.create(name=f"Policy{i}", ...)
    if result.get("status") == "error":
        failures.append(i)
    else:
        successes.append(i)

print(f"Created {len(successes)}, Failed {len(failures)}")
```

### Mode: "log"

**Behavior**: Logs error and returns None

**Program flow**: NEVER stops (always continues)

**Use when**: Fire-and-forget operations or centralized logging

```python
fgt = FortiOS(host="...", token="...", error_mode="log")

# Logs error automatically, returns None
result = fgt.firewall.policy.create(name="DuplicatePolicy", ...)

if result is None:
    print("Failed - check logs")
else:
    print("Success!")
```

## Error Formats

### Format: "detailed" (DEFAULT)

Full context with endpoint, parameters, HTTP status, error code, and helpful hints

```python
error_dict = {
    "status": "error",
    "error": "Object already exists (-5)\n  → POST /api/v2/cmdb/firewall/policy\n  → HTTP Status: 424 (Failed Dependency)\n  → FortiOS Error: -5 (Object already exists)\n  → Parameters: name=MyPolicy, action=accept\n  💡 Tip: Use .exists() to check for duplicates...",
    "exception_type": "DuplicateEntryError",
    "http_status": 424,
    "error_code": -5,
    "endpoint": "/api/v2/cmdb/firewall/policy",
    "method": "POST"
}
```

### Format: "simple"

Just exception type, message, and error code

```python
error_dict = {
    "status": "error",
    "error": "Object already exists",
    "exception_type": "DuplicateEntryError",
    "error_code": -5
}
```

### Format: "code_only"

Just the error code number

```python
error_dict = {
    "status": "error",
    "error": "...",
    "error_code": -5
}
```

## Decision Guide

### When to use each mode:

| Scenario | Mode | Reason |
|----------|------|--------|
| Creating ONE critical policy | `raise` | Must know immediately if it fails |
| Creating 100 policies from CSV | `return` | Want to create as many as possible |
| Background sync job | `log` | Runs automatically, review logs later |
| Interactive script | `raise` | User needs immediate feedback |
| Testing/validation | `return` | Collect all errors for review |

## Examples

### Example 1: Critical operation with immediate failure

```python
fgt = FortiOS(host="...", token="...", error_mode="raise")

try:
    fgt.firewall.policy.create(
        name="CriticalFirewallRule",
        srcintf="wan1",
        dstintf="internal",
        srcaddr="all",
        dstaddr="all",
        action="deny"
    )
    print("✅ Critical rule created")
except Exception as e:
    print(f"❌ CRITICAL FAILURE: {e}")
    send_alert_to_admin()
    sys.exit(1)
```

### Example 2: Batch import with error collection

```python
fgt = FortiOS(host="...", token="...", error_mode="return", error_format="simple")

successes = []
failures = []

for policy in load_policies_from_csv():
    result = fgt.firewall.policy.create(**policy)
    
    if result.get("status") == "error":
        failures.append({
            "name": policy["name"],
            "error_code": result.get("error_code"),
            "message": result.get("error")
        })
    else:
        successes.append(policy["name"])

# Generate report
print(f"✅ Created: {len(successes)}")
print(f"❌ Failed: {len(failures)}")
save_failures_to_csv(failures)
```

### Example 3: Mixed modes in same script

```python
# Default to "raise" for most operations
fgt = FortiOS(host="...", token="...", error_mode="raise")

# Critical rule - uses default "raise"
try:
    fgt.firewall.policy.create(name="CriticalRule", ...)
except Exception as e:
    handle_critical_failure(e)

# Optional rule - override to "return" for this call
optional_result = fgt.firewall.policy.create(
    name="OptionalRule",
    ...,
    error_mode="return"  # Override just for this call
)

if optional_result.get("status") == "error":
    print("Optional rule failed, continuing...")
```

## Implementation Status

Currently implemented for:
- ✅ `FirewallPolicy.create()`

TODO: Apply to all convenience wrapper methods:
- `FirewallPolicy.update()`
- `FirewallPolicy.delete()`
- `FirewallPolicy.get()`
- Other convenience wrappers as they are created

## Important Notes

1. **Only affects convenience wrappers**: Direct API calls (e.g., `fgt.api.cmdb.firewall.policy.post()`) are not affected by these settings
2. **Backward compatible**: Default is `error_mode="raise"` which matches current behavior
3. **Per-call override**: Can always override the instance default for specific calls
4. **Type safety**: Return type includes both success dict and error dict when using `error_mode="return"`

## Common Error Codes

| Code | Meaning | Suggested Mode |
|------|---------|----------------|
| -3 | Object not found | `return` (check existence) |
| -5 | Object already exists | `return` (handle duplicates) |
| -14 | Permission denied | `raise` (critical auth issue) |
| -23 | Object in use | `return` (might be expected) |
| 401 | Authentication failed | `raise` (critical) |
| 404 | Not found | `return` (might be expected) |
