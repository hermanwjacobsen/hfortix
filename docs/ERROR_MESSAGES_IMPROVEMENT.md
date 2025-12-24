# Error Message Improvements - v0.3.24

## Overview

We've significantly enhanced error messages in HFortix v0.3.24 to provide better debugging context and actionable hints. Error messages now include endpoint paths, HTTP methods, sanitized parameters, and helpful suggestions for common issues.

## What's New

### 1. **Rich Error Context**
All API errors now include:
- **Endpoint Path**: The exact API endpoint that failed
- **HTTP Method**: GET, POST, PUT, or DELETE
- **HTTP Status Code**: With human-readable description
- **FortiOS Error Code**: With detailed explanation
- **Request Parameters**: Sanitized (sensitive data masked)
- **Helpful Hints**: Context-aware suggestions for fixing the error

### 2. **Parameter Sanitization**
Sensitive parameters are automatically redacted:
- Passwords, API keys, tokens → `***REDACTED***`
- Long values truncated (>100 chars)
- Shows up to 5 parameters in error messages

### 3. **Context-Aware Hints**
Smart suggestions based on error type:
- **-3 (Not Found)**: "Use .exists() to check if the object exists"
- **-5 (Duplicate)**: "Use .exists() to check for duplicates before creating"
- **-23 (In Use)**: "Remove references from firewall policies before deleting"
- **400 Bad Request**: "Check required parameters and their format"
- **404 Not Found**: "Verify the object name and endpoint path"
- **429 Rate Limit**: "Implement rate limiting or increase delay between requests"

## Before & After Examples

### Example 1: Resource Not Found (404)

#### ❌ Before (v0.3.23)
```
ResourceNotFoundError: Entry not found
```

#### ✅ After (v0.3.24)
```
ResourceNotFoundError: Entry not found
  → GET /api/v2/cmdb/firewall/address
  → HTTP Status: 404 (Not Found - Resource does not exist)
  → FortiOS Error: -3 (Entry not found)
  → Parameters: filter=name==NonExistentAddress
  💡 Tip: Use .exists() to check if the object exists before accessing it.
```

---

### Example 2: Duplicate Entry Error

#### ❌ Before (v0.3.23)
```
DuplicateEntryError: A duplicate entry already exists
```

#### ✅ After (v0.3.24)
```
DuplicateEntryError: A duplicate entry already exists
  → POST /api/v2/cmdb/firewall/address
  → HTTP Status: 400 (Bad Request - Invalid request syntax or parameters)
  → FortiOS Error: -5 (A duplicate entry already exists)
  → Parameters: name=Test_Network, subnet=192.168.1.0/24
  💡 Tip: Use .exists() to check for duplicates before creating, or .update() to modify existing objects.
```

---

### Example 3: Entry In Use (Cannot Delete)

#### ❌ Before (v0.3.23)
```
EntryInUseError: Entry is in use and cannot be deleted
```

#### ✅ After (v0.3.24)
```
EntryInUseError: Entry is in use and cannot be deleted
  → DELETE /api/v2/cmdb/firewall/address
  → HTTP Status: 400 (Bad Request - Invalid request syntax or parameters)
  → FortiOS Error: -23 (Entry is used)
  → Parameters: mkey=Test_Network
  💡 Tip: Remove references from firewall policies and other configs before deleting.
```

---

### Example 4: Permission Denied

#### ❌ Before (v0.3.23)
```
PermissionDeniedError: Permission denied. Insufficient privileges.
```

#### ✅ After (v0.3.24)
```
PermissionDeniedError: Permission denied. Insufficient privileges.
  → PUT /api/v2/cmdb/system/admin
  → HTTP Status: 403 (Forbidden - Insufficient permissions)
  → FortiOS Error: -14 (Permission denied. Insufficient privileges)
  → Parameters: name=admin, password=***REDACTED***
  💡 Tip: Check VDOM access permissions and API token admin privileges.
```

---

### Example 5: Bad Request with Sensitive Data

#### ❌ Before (v0.3.23)
```
BadRequestError: Bad request
```

#### ✅ After (v0.3.24)
```
BadRequestError: Invalid value provided
  → POST /api/v2/cmdb/system/api-user
  → HTTP Status: 400 (Bad Request - Invalid request syntax or parameters)
  → FortiOS Error: -651 (Input value is invalid)
  → Parameters: name=api_user, accprofile=super_admin, api-key=***REDACTED***, vdom=root
  💡 Tip: Verify parameter format and allowed values in API documentation.
```

---

### Example 6: Rate Limit Exceeded

#### ❌ Before (v0.3.23)
```
RateLimitError: Rate limit exceeded
```

#### ✅ After (v0.3.24)
```
RateLimitError: Rate limit exceeded
  → GET /api/v2/monitor/system/status
  → HTTP Status: 429 (Too Many Requests - Rate limit exceeded)
  💡 Tip: Implement rate limiting in your code or increase delay between requests.
```

---

## Security Features

### Automatic Sanitization
The following parameter names are automatically redacted in error messages:
- `password`, `passwd`, `pwd`
- `secret`, `token`, `api_key`, `apikey`
- `key`, `private`, `credential`, `auth`
- Any parameter containing these keywords (case-insensitive)

### Example:
```python
# Request parameters
params = {
    "name": "admin",
    "password": "SuperSecret123!",
    "api-key": "abc123xyz789",
    "vdom": "root"
}

# Error message shows:
# → Parameters: name=admin, password=***REDACTED***, api-key=***REDACTED***, vdom=root
```

---

## Implementation Details

### Enhanced Exception Base Class
```python
class APIError(FortinetError):
    """Generic API error with optional metadata"""
    
    def __init__(
        self,
        message,
        http_status=None,
        error_code=None,
        response=None,
        endpoint=None,      # NEW
        method=None,        # NEW
        params=None,        # NEW (sanitized)
        hint=None,          # NEW
    ):
        # ...
```

### Rich String Formatting
All exceptions now have a custom `__str__()` method that formats errors with full context:
- Endpoint path and HTTP method
- HTTP status code with description
- FortiOS error code with explanation
- Request parameters (sanitized)
- Helpful hint/suggestion

### Backward Compatibility
- All existing exception types still work
- No breaking changes to exception handling
- Additional context is optional
- Errors can still be caught and handled as before

---

## Usage Examples

### Catching Specific Errors with Context
```python
from hfortix import FortiOS
from hfortix.FortiOS.exceptions import ResourceNotFoundError, DuplicateEntryError

fgt = FortiOS(host="192.168.1.99", api_token="your-token")

try:
    address = fgt.api.cmdb.firewall.address.get(mkey="NonExistent")
except ResourceNotFoundError as e:
    # New rich error message
    print(str(e))
    
    # Access individual fields
    print(f"Endpoint: {e.endpoint}")
    print(f"Method: {e.method}")
    print(f"HTTP Status: {e.http_status}")
    print(f"Error Code: {e.error_code}")
    print(f"Hint: {e.hint}")
```

### Logging with Context
```python
import logging

logger = logging.getLogger(__name__)

try:
    fgt.api.cmdb.firewall.policy.create(
        name="Test Policy",
        srcintf="port1",
        dstintf="port2",
        # ... more params
    )
except DuplicateEntryError as e:
    # Log the full formatted error
    logger.error(f"Failed to create policy: {e}")
    
    # Or log specific fields
    logger.error(
        "Duplicate policy",
        extra={
            "endpoint": e.endpoint,
            "method": e.method,
            "error_code": e.error_code,
            "params": e.params  # Already sanitized!
        }
    )
```

---

## Benefits

1. **Faster Debugging**
   - See exactly which endpoint and method failed
   - Understand what parameters were sent
   - Get actionable hints immediately

2. **Better Security**
   - Sensitive data automatically redacted
   - Safe to log errors without exposing credentials
   - Truncation prevents log bloat

3. **Improved Developer Experience**
   - Clear, actionable error messages
   - No need to dig through FortiOS documentation
   - Common fixes suggested automatically

4. **Production Ready**
   - Rich context for monitoring and alerting
   - Structured error data for log aggregation
   - Easy to parse for automated error handling

---

## Future Enhancements

Planned for upcoming versions:
- Typo detection with "Did you mean?" suggestions
- Differentiate between endpoint vs object 404 errors
- Timeout messages with endpoint-specific suggestions
- Deprecated endpoint warnings with alternatives
- Error recovery suggestions with code examples

---

## Testing

To test the new error messages:

```python
from hfortix import FortiOS
from hfortix.FortiOS.exceptions import ResourceNotFoundError

fgt = FortiOS(host="192.168.1.99", api_token="your-token")

# Test 1: Not Found
try:
    fgt.api.cmdb.firewall.address.get(mkey="DoesNotExist")
except ResourceNotFoundError as e:
    print("NOT FOUND ERROR:")
    print(e)
    print()

# Test 2: Duplicate
try:
    fgt.api.cmdb.firewall.address.create(
        name="ExistingAddress",
        subnet="192.168.1.0/24"
    )
except DuplicateEntryError as e:
    print("DUPLICATE ERROR:")
    print(e)
    print()

# Test 3: Sensitive Data Masking
try:
    fgt.api.cmdb.system.api_user.create(
        name="test_user",
        accprofile="super_admin",
        api_key="this-should-be-redacted",
        password="also-redacted"
    )
except Exception as e:
    print("SANITIZED ERROR:")
    print(e)
    # Verify that api_key and password show as ***REDACTED***
```

---

## Migration Guide

No code changes required! The improvements are automatic and backward compatible.

### Before
```python
try:
    fgt.api.cmdb.firewall.address.get(mkey="test")
except ResourceNotFoundError as e:
    print(e)  # "Entry not found"
```

### After  
```python
try:
    fgt.api.cmdb.firewall.address.get(mkey="test")
except ResourceNotFoundError as e:
    print(e)  # Full rich error message with context!
```

That's it! Just upgrade to v0.3.24 and enjoy better error messages automatically.

---

**Version:** 0.3.24  
**Last Updated:** December 24, 2025  
**Author:** HFortix Development Team
