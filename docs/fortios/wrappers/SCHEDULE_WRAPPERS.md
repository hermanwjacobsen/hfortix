# Schedule Convenience Methods - Enhancement Summary

## Overview

Added missing convenience methods to all schedule modules to match the `firewallPolicy` pattern, making schedule management more user-friendly and consistent across the API.

## Changes Made

### 1. New Convenience Methods (All 3 Schedule Types)

#### ✅ `get_by_name(name, vdom=None)` 
**Returns schedule data directly instead of full API response**

```python
# OLD WAY (messy):
result = fgt.firewall.schedule_onetime.get(name="maintenance-window")
if result.get('status') == 'success' and result.get('results'):
    schedule = result['results'][0]
    print(f"Start: {schedule['start']}")

# NEW WAY (clean):
schedule = fgt.firewall.schedule_onetime.get_by_name("maintenance-window")
if schedule:
    print(f"Start: {schedule['start']}")
else:
    print("Schedule not found")
```

**Key Features:**
- Returns `None` if schedule not found (no exception)
- Handles both `raw_json=False` and `raw_json=True` responses
- Works with list or dict responses
- Validates schedule name

#### ✅ `rename(name, new_name, vdom=None)`
**Rename a schedule in one call**

```python
# Rename schedule
result = fgt.firewall.schedule_recurring.rename(
    name="old-business-hours",
    new_name="new-business-hours"
)
print(f"Renamed to: {result.get('mkey', new_name)}")
```

**Key Features:**
- Validates both old and new names
- Checks if source schedule exists before renaming
- Cleaner than: `update(name=name, **{'name': new_name})`

#### ✅ `clone(name, new_name, [overrides], vdom=None)`
**Clone a schedule with optional modifications**

```python
# Clone onetime schedule with modifications
result = fgt.firewall.schedule_onetime.clone(
    name="maintenance-window",
    new_name="extended-maintenance",
    end="20:00 2026/01/15",  # Override end time
    color=10  # Override color
)

# Clone recurring schedule
result = fgt.firewall.schedule_recurring.clone(
    name="business-hours",
    new_name="extended-hours",
    end="18:00"  # Extend to 6 PM
)

# Clone schedule group with different members
result = fgt.firewall.schedule_group.clone(
    name="all-hours",
    new_name="backup-group",
    members=["schedule1", "schedule2"]  # Override members
)
```

**Key Features:**
- Clones all settings from original schedule
- Allows selective override of any field
- Validates all override values
- Great for creating similar schedules

### 2. Response Helper Functions

Added to `hfortix.FortiOS.api._helpers`:

#### ✅ `get_mkey(response)`
**Extract the created object's name from response**

```python
from hfortix.FortiOS.api._helpers import get_mkey

# OLD WAY (ugly):
result = fgt.firewall.schedule_onetime.create(name='test', ...)
print(f"Created: {result.get('mkey')}")  # Yuck!

# NEW WAY (clean):
result = fgt.firewall.schedule_onetime.create(name='test', ...)
print(f"Created: {get_mkey(result)}")  # Much better!
```

#### ✅ `is_success(response)`
**Check if operation succeeded**

```python
from hfortix.FortiOS.api._helpers import is_success

result = fgt.firewall.schedule_onetime.create(...)
if is_success(result):
    print(f"✅ Created: {get_mkey(result)}")
else:
    print("❌ Failed!")
```

#### ✅ `get_results(response)`
**Extract results from response**

```python
from hfortix.FortiOS.api._helpers import get_results

response = fgt.firewall.schedule_onetime.get()
schedules = get_results(response)
for schedule in schedules:
    print(schedule['name'])
```

## Implementation Details

### Response Format Handling

The methods correctly handle both API response formats:

**`raw_json=False` (default):**
- Returns `response.get("results", response)`
- Direct list or simplified data
- Example: `[{schedule1}, {schedule2}]` or `{schedule1}`

**`raw_json=True`:**
- Returns full API response
- Dict with 'status', 'results', 'mkey', etc.
- Example: `{"status": "success", "results": [{...}], "mkey": "name"}`

```python
def get_by_name(self, name, vdom=None):
    result = self.get(name=name, vdom=vdom)
    
    # Handle both response formats
    if isinstance(result, dict):
        if 'results' in result:  # raw_json=True
            results = result['results']
        else:  # Single object returned directly
            return result
    elif isinstance(result, list):  # raw_json=False (list)
        results = result
    else:
        return None
    
    return results[0] if results else None
```

## Module Coverage

### ✅ scheduleOnetime.py
- `get_by_name()`
- `rename()`
- `clone()` - with start, end, color, expiration_days overrides

### ✅ scheduleRecurring.py  
- `get_by_name()`
- `rename()`
- `clone()` - with start, end, day, color overrides

### ✅ scheduleGroup.py
- `get_by_name()`
- `rename()`
- `clone()` - with members, color overrides

## Not Implemented (Not Applicable)

### ❌ `enable()` / `disable()`
**Reason:** Schedules don't have a status field in FortiOS API
- Schedules are active when created
- They're removed when deleted
- No enable/disable functionality exists

### ❌ `move()`
**Reason:** Schedules don't have ordering/position
- Only firewall policies have sequence numbers
- Schedules are referenced by name, not position

## Migration Guide

### Before (Manual Approach)
```python
# Get schedule data
result = fgt.firewall.schedule_onetime.get(name="test")
if result.get('status') == 'success' and result.get('results'):
    schedule = result['results'][0] if isinstance(result['results'], list) else result['results']
    print(schedule['start'])

# Rename (messy)
fgt.firewall.schedule_onetime.update(name="old", **{"name": "new"})

# Clone manually
original = fgt.firewall.schedule_onetime.get(name="source")
clone_data = {k: v for k, v in original['results'][0].items() if k not in ('name', 'q_origin_key')}
clone_data['name'] = "new-name"
fgt.firewall.schedule_onetime.create(**clone_data)
```

### After (New Convenience Methods)
```python
# Get schedule data
schedule = fgt.firewall.schedule_onetime.get_by_name("test")
if schedule:
    print(schedule['start'])

# Rename (clean)
fgt.firewall.schedule_onetime.rename(name="old", new_name="new")

# Clone (easy)
fgt.firewall.schedule_onetime.clone(name="source", new_name="new-name")
```

## Examples

See `/examples/schedule_convenience_demo.py` for comprehensive demonstrations.

## Testing

The methods handle edge cases:
- ✅ Non-existent schedules (return None, no exception)
- ✅ Both `raw_json=False` and `raw_json=True` responses
- ✅ List and dict response formats
- ✅ Missing optional fields in original objects
- ✅ Validation of all input parameters

## Benefits

1. **Consistency**: Matches `firewallPolicy` convenience method pattern
2. **Simplicity**: Less code, cleaner syntax
3. **Safety**: Built-in validation and error handling
4. **Flexibility**: Works with all response formats
5. **Discoverability**: IDE autocomplete shows all available methods
6. **User-Friendly**: No more dealing with `result.get('mkey')` or `result['results'][0]`

## Backward Compatibility

✅ **100% backward compatible**
- All existing methods unchanged
- New methods are additions only
- No breaking changes to existing code
