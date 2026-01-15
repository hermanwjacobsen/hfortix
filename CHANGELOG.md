# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.75] - 2026-01-15

### Changed - **Improved Type Safety: Generic `FortiObjectList` for proper list iteration typing**

**What Changed:**
- ✅ **Made `FortiObjectList` generic**: Now `FortiObjectList[T]` where T is the specific object type
- ✅ **List iteration now properly typed**: Iterating over policy list returns `PolicyObject`, not generic `FortiObject`
- ✅ **Nested table field access now type-checked**: `policy.srcaddr` returns properly typed objects
- ✅ **Removed `raw_json` parameter from public API**: Use `.raw` property instead

**Why:**
Previously, `FortiObjectList` was typed as `list[FortiObject]`, so when iterating over a list of policies, Pylance couldn't detect invalid attribute access like `policy.nonexistent`.

**Before (no type error on list iteration):**
```python
policies = fg.api.cmdb.firewall.policy.get()
for policy in policies:
    policy.nonexistent  # No error! FortiObject accepts any attribute
```

**After (proper type error):**
```python
policies = fg.api.cmdb.firewall.policy.get()  # FortiObjectList[PolicyObject]
for policy in policies:
    policy.name         # ✅ Works - PolicyObject has 'name'
    policy.nonexistent  # ❌ Error: Cannot access attribute "nonexistent" for class "PolicyObject"

for addr in policy.srcaddr:  # list[PolicySrcaddrObject]
    addr.name           # ✅ Works
    addr.nonexistent    # ❌ Error: Attribute "nonexistent" is unknown
```

**Also in this release:**
- Removed `raw_json` parameter from `FortiOS.request()` method
- Updated all docstrings to reference `.raw` property instead of `raw_json` parameter
- Cleaned up internal `raw_json` references (internal calls still use `raw_json=True`)

---

## [0.5.74] - 2026-01-15

### Changed - **Improved Type Safety: Removed `**kwargs: Any` from type stubs**

**What Changed:**
- ✅ **Removed `**kwargs: Any` from all method signatures in `.pyi` stubs**
- ✅ **Unknown keyword arguments now properly show type errors**
- ✅ **Passing deprecated `response_mode` parameter now shows error**

**Why:**
Previously, `**kwargs: Any` acted as a catch-all that accepted any keyword argument without type checking. This meant passing invalid or deprecated parameters like `response_mode="dict"` would be silently accepted.

**Before (no type error):**
```python
# No error even though response_mode was removed in v0.5.71!
settings = fg.api.cmdb.antivirus.settings.get(response_mode="dict")
```

**After (proper type error):**
```python
settings = fg.api.cmdb.antivirus.settings.get(response_mode="dict")
# ❌ Error: Unexpected keyword argument "response_mode"
```

---

## [0.5.73] - 2026-01-15

### Changed - **Improved Type Safety: Removed `__getitem__` from FortiObject stubs**

**What Changed:**
- ✅ **Removed `__getitem__` method from all generated type stubs** (`*Object` classes)
- ✅ **Bracket access (`obj['field']`) now properly shows type errors**
- ✅ **Forces attribute access (`obj.field`) for proper type checking**
- ✅ **Invalid field access now detected by Pylance/type checkers**

**Why:**
Previously, `__getitem__(self, key: str) -> Any` allowed bracket notation but returned `Any`, defeating type checking. Invalid field access like `obj['nonexistent_field']` would not show errors.

**Before (no type error):**
```python
rule = fg.api.cmdb.authentication.rule.get(name="test")
rule['nonexistent_field']  # No error! Returns Any
```

**After (proper type error):**
```python
rule = fg.api.cmdb.authentication.rule.get(name="test")
rule['srcintf']  # ❌ Error: "__getitem__" method not defined on type "RuleObject"
rule.srcintf     # ✅ Works with full autocomplete and type checking
rule.nonexistent # ❌ Error: Cannot access attribute "nonexistent" for class "RuleObject"
```

**Migration:**
Use attribute access (`.field`) instead of bracket access (`['field']`):
```python
# ❌ OLD: rule['srcintf']
# ✅ NEW: rule.srcintf
```

---

## [0.5.72] - 2026-01-15

### Changed
- Updated `test_autocomplete.py` for unified FortiObject API
  - File is now purely for **static analysis** (Pylance/type checking validation)
  - Demonstrates autocomplete, type errors, and IDE integration
  - NOT meant to be executed - just for checking IDE behavior
  - Added comprehensive scenarios: `.dict`, `.json`, `.raw` properties, `raw_json=True`, nested tables, Literal validation

---

## [0.5.71] - 2026-01-15

### Changed - **BREAKING: Simplified API - Removed `response_mode` parameter**

**What Changed:**
- ✅ **Removed `response_mode` parameter** from `FortiOS` client initialization
- ✅ **All API methods now return `FortiObject` instances** (no more dict mode)
- ✅ **Added `.dict`, `.json`, `.raw` properties** to `FortiObject` for flexible data access
- ✅ **Simplified client architecture** - removed `FortiOSDictMode`, `FortiOSObjectMode`, `APIDictMode`, `APIObjectMode` classes
- ✅ **Massive codebase reduction** - eliminated 267,743 lines of type stub code (50.6% reduction!)

**Impact on Generated API:**
```
BEFORE (dual response_mode API):
- Directory size:  145M
- Type stub lines: 529,626 lines
- Largest .pyi:    9,135 lines (system/interface.pyi)

AFTER (unified FortiObject API):
- Directory size:  123M (-22M, -15.2%)
- Type stub lines: 261,883 lines (-267,743 lines, -50.6%)
- Largest .pyi:    4,586 lines (-50% reduction)

Generated 1,062 endpoints in 6.7 seconds
```

**Impact on Test Suite:**
```
Test Generation Summary:
- ✅ Generated:  1,066 test files
- ⏭️  Skipped:   282 endpoints (category containers, unsupported)
- ❌ Errors:     0
- 📝 Total:      1,348 schemas processed

All tests updated to use new unified API:
- Removed all response_mode="dict" parameter calls
- Tests now use .dict property: endpoint.get().dict
- 100% test compatibility with v0.6.0+ API
```

**Migration Guide:**

```python
# ❌ OLD (v0.5.x):
fgt = FortiOS(host="...", token="...", response_mode="dict")  # Dict mode
addresses = fgt.api.cmdb.firewall.address.get()
for addr in addresses:
    print(addr["name"])  # Dictionary access

fgt = FortiOS(host="...", token="...", response_mode="object")  # Object mode  
addresses = fgt.api.cmdb.firewall.address.get()
for addr in addresses:
    print(addr.name)  # Attribute access

# ✅ NEW (v0.6.0+):
fgt = FortiOS(host="...", token="...")  # No response_mode parameter!
addresses = fgt.api.cmdb.firewall.address.get()
for addr in addresses:
    # Attribute access (recommended)
    print(addr.name)
    print(addr.subnet)
    
    # Dictionary access still works!
    print(addr["name"])
    
    # Convert to dict when needed
    addr_dict = addr.dict  # or addr.json or addr.raw
    print(addr_dict)  # {'name': 'MyAddress', 'subnet': '10.0.0.1/32', ...}
```

**Why This Change:**
- 🎯 **Simpler API** - One obvious way to do things (Pythonic!)
- 🚀 **Better UX** - Choose output format when you need it, not upfront
- 🧹 **Cleaner codebase** - Eliminated 50% of duplicate classes and type stubs
- ✨ **More flexible** - Access as object OR dict, convert when needed
- 📦 **Smaller package** - 22MB smaller distribution size

**Benefits:**
- ✅ Always get `FortiObject` with full IDE autocomplete
- ✅ Use `.dict`, `.json`, or `.raw` properties when you need a dictionary
- ✅ Both `obj.field` and `obj["field"]` work on the same object
- ✅ No need to choose mode upfront - decide at access time!
- ✅ 50% reduction in generated code complexity

### Added
- **Added `pydantic>=2.0` as dependency** - Required for 1,062 generated Pydantic models used for request validation

## [0.5.70] - 2026-01-15

### Changed
- **BREAKING: Removed `**kwargs` from all endpoint methods**
  - All query parameters are now explicitly typed in method signatures
  - Query parameters use `q_` prefix to avoid conflicts with body field parameters (e.g., `q_action`, `q_format`)
  - Special exclusions: `vdom`, `filter`, `count`, `start` (no `q_` prefix as they never conflict)
  - Improved IDE autocomplete and type safety
  - Example: `endpoint.get(q_format="name|id", q_action="move")` instead of `endpoint.get(format="name|id", action="move")`

- **BREAKING: Changed default `response_mode` from `"dict"` to `"object"`**
  - All GET/PUT/POST/DELETE methods now return `FortiObject` instances by default
  - For dictionary responses, explicitly pass `response_mode="dict"`
  - Provides better attribute access: `result.name` instead of `result["name"]`

- **Added `error_mode` and `error_format` parameters to all CRUD methods**
  - Optional per-call overrides for error handling behavior
  - Example: `endpoint.get(error_mode="raise", error_format="detailed")`

### Fixed
- **Eliminated `datetime.utcnow()` deprecation warnings in audit logging**
  - `SyslogFormatter` now uses timezone-aware UTC timestamps (`datetime.now(timezone.utc)` → `...Z`).
  - Matches ISO 8601 output while avoiding Python 3.12 deprecation warnings.
- **Generator metadata now UTC-aware**
  - Schema downloader uses the same timezone-aware helper for `downloaded_at` and summaries.
  - Regenerated schemas will embed compliant `...Z` timestamps without deprecation warnings.
- **Fixed circular imports in monitor/service categories**
  - Removed duplicate `schema/7.6.5/monitor/monitor/` directory causing circular imports
  - Generator no longer creates same-name subdirectories (e.g., `monitor/monitor`, `service/service`)

## [0.5.57] - 2026-01-14

### Added (Docs)
- **Expanded test suite with 8 new test files (~78 new tests)**
  - `test_readonly_cache.py` - 9 tests for module-level cache functions (`hfortix_core.readonly_cache`)
  - `test_debug_session.py` - 6 tests for `DebugSession` class (request tracking)
  - `test_configure_logging.py` - 9 tests for `configure_logging()` function
  - `test_request_logger.py` - 7 tests for `RequestLogger` class
  - `test_http_client_advanced.py` - 10 tests for HTTPClient/FortiOS advanced methods
  - `test_syslog_handler.py` - 6 tests for `SyslogHandler` audit logging
  - `test_core_types.py` - 15 tests for `hfortix_core` TypedDicts (`ConnectionStats`, `RequestInfo`, `APIResponse`, etc.)
  - `test_fortios_types.py` - 16 tests for `hfortix_fortios` response types and Literal types (`ActionType`, `StatusType`, etc.)

### Fixed
- **Generator: Fixed `NotRequired` import for Python <3.11 compatibility**
  - Changed `from typing import NotRequired` to `from typing_extensions import NotRequired`
  - `NotRequired` was added to `typing` in Python 3.11, but hfortix supports Python 3.10+
  - Updated templates: `endpoint_class.pyi.j2`, `validator.py.j2`
  - Updated manual files: `types.py`, `types.pyi`
  - Fixes Pylance error: `"NotRequired" is unknown import symbol`

- **Generator: Fixed Monitor/Service class names in stub files**
  - Template `toplevel_init.pyi.j2` was generating `MONITOR`/`SERVICE` class names
  - But Python classes use `Monitor`/`Service` (matching `regenerate_init_files.py`)
  - Added class name mapping: `{'cmdb': 'CMDB', 'monitor': 'Monitor', 'log': 'Log', 'service': 'Service'}`
  - Fixes Pylance import errors for `.monitor` and `.service` in stub files

- **Stub files: Fixed import chain for Monitor/Service/Log categories**
  - `api/__init__.pyi`: Now imports `Monitor`, `MonitorDictMode`, etc. directly
  - `api/v2/__init__.pyi`: Exports proper class names
  - `api/v2/monitor/__init__.pyi`: Uses `Monitor`, `MonitorDictMode`, `MonitorObjectMode`

- **Generator: Fixed auto-generated tests using kebab-case keys for response dictionary access**
  - Test template `test_basic.py.j2` was using `{{ schema.mkey }}` (kebab-case) for dict access
  - But API responses are normalized to snake_case by `normalize_keys()` in HTTPClient
  - Changed dictionary key access to use `{{ schema.mkey|kebab_to_snake }}` filter
  - Fixes 21 test failures like: `assert "ems-id" in item` → `assert "ems_id" in item`
  - `api/v2/service/__init__.pyi`: Uses `Service`, `ServiceDictMode`, `ServiceObjectMode`

- **Bug #21: CompositeHandler.error_summary now tracks handler errors** (`hfortix_core/audit/handlers.py`)
  - Added `propagate_errors` parameter to `CallbackHandler` (default: `False`)
  - When `True`, exceptions from callback are re-raised, enabling CompositeHandler error tracking
  - Previously, `CallbackHandler` swallowed exceptions, so `error_summary['total_errors']` stayed at 0
  - Set `propagate_errors=True` when using `CallbackHandler` inside `CompositeHandler`

- **Bug #22: process_response no longer crashes on list of non-dicts** (`hfortix_fortios/models.py`)
  - `process_response()` with `response_mode='object'` now handles lists of strings/integers
  - Previously crashed with `AttributeError: 'str' object has no attribute 'get'`
  - Now only wraps dict items in `FortiObject`; non-dict items pass through unchanged

- **Bug #23: make_exists_method returns False for error responses** (`hfortix_core/http/client.py`)
  - `HTTPClient.make_exists_method()` now checks for API error responses
  - Returns `False` when response has `status='error'` or `http_status=404`
  - Previously returned `True` for all non-exception responses, including errors

- **Bug #24: Utils.performance_test() now works correctly** (`hfortix_fortios/api/__init__.py`)
  - Fixed `AttributeError: 'FortiOS' object has no attribute '_url'`
  - `API` class now unwraps `ResponseProcessingClient` to get underlying `HTTPClient`
  - `Utils` now receives the actual `HTTPClient` with access to `_url` and other internals

- **Bug #26: Fixed log_operation stub signature** (`hfortix_core/__init__.pyi`)
  - Stub incorrectly defined `log_operation` as a decorator returning `Callable`
  - Actual function signature: `log_operation(logger_name, operation, level='INFO', **kwargs) -> None`
  - Fixes Pylance error: `Expected 1 positional argument` when calling with multiple args

## [0.5.56] - 2026-01-13

### Fixed
- **BUG #18: Added `hfortix_core/__init__.pyi` type stubs** (`hfortix_core/__init__.pyi`)
  - Created comprehensive type stubs for hfortix_core package
  - Fixes Pylance errors for `format_connection_stats`, `format_request_info`, `print_debug_info`
  - These functions were exported at runtime but Pylance couldn't resolve them from hfortix_core
  - Added type stubs for all exceptions, debug utilities, cache, logging, and type definitions
  - Updated `__version__` in `hfortix_fortios/__init__.py` to match package version

## [0.5.55] - 2026-01-13

### Fixed
- **BUG #17: Fixed monitor/service/log categories showing as Unknown types** (`api/__init__.pyi`)
  - `APIDictMode.monitor` was typed as `Monitor` instead of `MONITORDictMode`
  - `APIObjectMode.monitor` was typed as `Monitor` instead of `MONITORObjectMode`
  - `APIDictMode.service` was typed as `Service` instead of `SERVICEDictMode`
  - `APIObjectMode.service` was typed as `Service` instead of `SERVICEObjectMode`
  - Fixed imports to use proper DictMode/ObjectMode variants for all categories
  - Fixes `fgt.api.monitor.system.status` and similar paths showing as Unknown in Pylance

## [0.5.54] - 2026-01-13

### Fixed
- **BUG #15: Added `utils.pyi` type stub for direct Utils instantiation** (`api/utils.pyi`)
  - Created new type stub file for `Utils` class
  - Type hint now accepts `FortiOS | FortiOSDictMode | FortiOSObjectMode | HTTPClient | IHTTPClient`
  - Fixes Pylance errors when instantiating `Utils(fgt)` directly with FortiOS clients
  - Added type stubs for `PerformanceTestResults` class

- **BUG #16: Added `_validate_credentials` static method to FortiOS type stubs** (`client.pyi`)
  - Added `@staticmethod _validate_credentials(token, username, password) -> None`
  - Fixes "Cannot access attribute '_validate_credentials'" Pylance errors
  - Enables type checking when calling `FortiOS._validate_credentials()` directly

## [0.5.53] - 2026-01-12

### Fixed
- **BUG #11: Fixed `Utils.__init__` type hint rejecting FortiOS client** (`api/utils.py`)
  - Type hint was `HTTPClient` but `Utils` is initialized with `FortiOS._client`
  - Changed to `Union[HTTPClient, IHTTPClient]` to accept any HTTP client interface
  - Fixes Pylance type mismatch errors when using `fgt.api.utils`

- **BUG #12: Added missing async context manager methods to FortiOS type stubs** (`client.pyi`)
  - Added `__aenter__`, `__aexit__`, `aclose` to `FortiOS`, `FortiOSDictMode`, `FortiOSObjectMode`
  - Enables proper type checking for `async with FortiOS(..., mode="async") as fgt:`
  - Fixes "Cannot access attribute" Pylance errors when using async context manager

- **BUG #13: Added missing FortiOS methods to type stubs** (`client.pyi`)
  - Added `get_health_metrics()`, `get_retry_stats()`, `get_operations()`
  - Added `get_circuit_breaker_state()`, `export_audit_logs()`, `request()`
  - Fixes "Cannot access attribute" Pylance errors when using these methods

## [0.5.52] - 2026-01-12

### Added
- **Expanded test suite with 27 new test files (400+ new tests)**
  - **Unit tests** (9 files):
    - `test_api_utils.py` - `api.utils.Utils` class tests
    - `test_async_client.py` - Async FortiOS client (`mode="async"`)
    - `test_encode_path.py` - `encode_path_component()` URL encoding
    - `test_format_utils.py` - `format_connection_stats()`, `format_request_info()`
    - `test_http_client_utils.py` - HTTPClient utility methods
    - `test_log_operation.py` - `log_operation` decorator
    - `test_print_debug.py` - `print_debug_info()` debug output
    - `test_process_response.py` - `process_response()` function
    - `test_response_types.py` - Response type handling
  - **Integration tests** (3 files):
    - `test_fortios_client.py` - FortiOS client integration
    - `test_hooks.py` - Hook system tests
    - `test_http_client_stats.py` - HTTP client statistics
  - **Validator tests** (14 files):
    - `test_audit_formatters.py` - Audit log formatters
    - `test_audit_handlers.py` - Audit handlers
    - `test_credential_validation.py` - Credential validation
    - `test_debug_formatters.py` - Debug formatters
    - `test_debug_timer.py` - `debug_timer` decorator
    - `test_exceptions.py` - Exception classes
    - `test_fmt.py` - String formatting utilities
    - `test_forti_object.py` - `FortiObject` class
    - `test_fortios_formatting.py` - FortiOS formatting
    - `test_helpers.py` - Helper functions
    - `test_logging_formatters.py` - Logging formatters
    - `test_normalize_keys.py` - Key normalization
    - `test_ttl_cache.py` - TTL cache
    - `test_validators.py` - Validation functions

### Fixed
- **BUG #8: Fixed `normalize_*` type hints rejecting homogeneous lists** (`normalizers.py`)
  - Type hints now accept `List[str]`, `List[Dict]`, and mixed lists separately
  - Added separate Union options: `List[str] | List[Dict[str, Any]] | List[str | Dict[str, Any]]`
  - Fixes Pylance errors when passing homogeneous lists like `["port1", "port2"]`

- **BUG #9: Added missing static methods to HTTPClient `.pyi` stub** (`http/client.pyi`)
  - Added `validate_mkey`, `validate_required_params`, `validate_range`
  - Added `validate_choice`, `build_params`, `make_exists_method`
  - Fixes "Cannot access attribute" Pylance errors when using these static methods

- **BUG #10: Fixed `Utils.performance_test()` referencing missing module** (`api/utils.py`)
  - Import path was `.performance_test` (looking in `api/` directory)
  - Changed to `..performance_test` to correctly import from `hfortix_fortios/performance_test.py`
  - Fixes `ModuleNotFoundError: No module named 'hfortix_fortios.api.performance_test'`

## [0.5.51] - 2026-01-12

### Fixed
- **BUG #5: Fixed `to_xml()` producing invalid XML with special characters** (`formatting.py`, `fmt.py`)
  - Special characters (`<`, `>`, `&`, `"`, `'`) were not escaped, causing XML parse errors
  - Added `_escape_xml()` helper function that properly escapes all XML special characters
  - Fixed in both `hfortix_fortios/formatting.py` and `hfortix_core/fmt.py`

- **BUG #6: Fixed `validate_port_number` allowing invalid port range** (`validators.py`)
  - Was incorrectly allowing ports 0-4294967295 (32-bit range)
  - Fixed to validate TCP/UDP port range 0-65535 (16-bit range)
  - Updated docstring to clarify this is for TCP/UDP ports
  - For FortiOS 32-bit integer fields, use `validate_integer_range()` directly

- **BUG #7: Fixed `normalize_to_name_list` corrupting mixed lists** (`normalizers.py`)
  - Mixed lists like `["port1", {"name": "port2"}]` were corrupted
  - The dict would become `{"name": "{'name': 'port2'}"}` (stringified)
  - Now processes each item individually based on its actual type
  - Correctly handles any mix of strings and dicts in the same list
  - **Also fixed `normalize_table_field`** with the same mixed-list bug

- **Type hint fixes for better IDE support** (`converters.py`, `normalizers.py`)
  - `convert_boolean_to_str`: Added `int` to type hint (was `bool|str|None`, now `bool|str|int|None`)
  - `normalize_to_name_list`, `normalize_member_list`, `normalize_table_field`: Changed type hints to allow mixed lists (`List[str|Dict]` instead of `List[str]|List[Dict]`)
  - Fixes false Pylance/type checker errors when using valid inputs

## [0.5.50] - 2026-01-12

### Added
- **Expanded unit test suite to 366 tests across 22 test files**
  - New `hfortix_core` tests (88 tests in 7 files):
    - `test_fmt.py` (14 tests) - Data formatting functions
    - `test_audit_formatters.py` (14 tests) - JSONFormatter, SyslogFormatter, CEFFormatter
    - `test_audit_handlers.py` (18 tests) - NullHandler, StreamHandler, FileHandler, CompositeHandler
    - `test_logging_formatters.py` (13 tests) - StructuredFormatter, TextFormatter
    - `test_normalize_keys.py` (10 tests) - Key normalization utilities
    - `test_debug_timer.py` (8 tests) - Timing context manager
    - `test_exceptions.py` (11 tests) - Full exception hierarchy

### Fixed
- **Fixed `CEFFormatter` crash when `user_context=None`** (`hfortix_core/audit/formatters.py`)
  - `operation.get("user_context", {}).get("username")` crashes if `user_context` is explicitly `None`
  - Changed to `(operation.get("user_context") or {}).get("username")` to handle `None` values
- **Fixed `StreamHandler` crash with `StringIO` objects** (`hfortix_core/audit/handlers.py`)
  - `StringIO` objects don't have a `.name` attribute, causing `AttributeError`
  - Changed `self.stream.name` to `getattr(self.stream, "name", "<unnamed>")` (3 occurrences)

## [0.5.49] - 2026-01-10

### Added
- **Comprehensive unit test suite (200+ tests across 16 test files)**
  - Validators: generic, network, firewall, schedule, SSH/SSL validators
  - Helpers: normalizers, converters, builders, response helpers, metadata
  - Core modules: formatting (69 tests), models (31 tests), cache, deprecation, exceptions
  - Full coverage of `hfortix_fortios._helpers` and `hfortix_core` utility modules
  - Test documentation in `docs/fortios/TESTING.md`

### Fixed
- **Fixed type stubs for Pylance compatibility**
  - Added `__all__` export list to `formatting.pyi` for all 13 formatting functions
  - Resolves "unknown import symbol" errors for `to_list`, `to_table`, `to_json`, etc.
  - Added fallback overload to `process_response` in `models.pyi` for non-dict/list types
  - Allows passing strings, None, or other types without Pylance overload mismatch errors

### Tested
- **hfortix_fortios validators** (`_helpers/validators.py`)
  - `validate_required_fields`, `validate_color`, `validate_status`, `validate_enable_disable`
  - `validate_mac_address`, `validate_ip_address`, `validate_ipv6_address`, `validate_ip_network`
  - `validate_policy_id`, `validate_address_pairs`, `validate_seq_num`
  - `validate_schedule_name`, `validate_time_format`, `validate_day_names`
  - `validate_ssh_host_key_*`, `validate_ssl_dh_bits`, `validate_ssl_cipher_action`
- **hfortix_fortios helpers**
  - `normalizers.py`: `normalize_to_name_list`, `normalize_member_list`, `normalize_table_field`
  - `converters.py`: `convert_boolean_to_str`, `filter_empty_values`
  - `builders.py`: `build_cmdb_payload`, `build_cmdb_payload_normalized`, `build_api_payload`
  - `response.py`: `get_name`, `get_mkey`, `get_results`, `is_success`
  - `metadata.py`: `get_field_*` functions, `validate_field_value`
- **hfortix_fortios top-level**
  - `formatting.py`: all 13 output formatters (`to_json`, `to_csv`, `to_table`, `to_yaml`, etc.)
  - `models.py`: `FortiObject` class (all methods), `process_response`
- **hfortix_core utilities**
  - `cache.py`: `TTLCache`, `CacheEntry` classes
  - `deprecation.py`: `warn_deprecated_field`, `check_deprecated_fields`
  - `exceptions.py`: `raise_for_status`, `is_retryable_error`, `get_retry_delay`, full exception hierarchy

## [0.5.48] - 2026-01-10

### Fixed
- **Fixed `.pyi` stub class name generation for multi-word categories**
  - Categories like `file_filter`, `endpoint_control`, `diameter_filter` now generate correct PascalCase
  - Before: `class Filefilter:` (incorrect) → After: `class FileFilter:` (correct)
  - Added `to_class_name` filter to pyi_generator for proper snake_case → PascalCase conversion
  - Updated `category_init.pyi.j2` template to use new filter
  - Regenerated all 1,064 endpoint stubs with correct class names
  - Affected categories: diameter_filter, endpoint_control, ethernet_oam, extension_controller,
    file_filter, ftp_proxy, sctp_filter, switch_controller, virtual_patch, web_proxy, wireless_controller

### Changed
- **Test fixes for snake_case API response keys**
  - Fixed remaining test assertions expecting hyphenated keys (`ems-id`) to use snake_case (`ems_id`)
  - All 3,486 tests now passing

### Tested
- **Comprehensive CMDB API endpoint testing (~115+ methods across 11 modules)**
  - Alert Email: `setting.get()`, `setting.put()`
  - Antivirus: `settings`, `quarantine`, `profile`, `exempt_list` (full CRUD)
  - Application: `list`, `custom`, `group` (full CRUD)
  - Authentication: `setting`, `scheme`, `rule` (full CRUD)
  - Automation: `setting.get()`, `setting.put()`
  - CASB: `saas_application`, `user_activity`, `profile` (POST/PUT)
  - Certificate: `hsm_local`, `ca`, `crl`, `local`, `remote` (GET)
  - Diameter Filter: `profile` (GET/POST)
  - DLP: `settings`, `sensor`, `dictionary`, `filepattern`, `exact_data_match`, `data_type` (full CRUD)
  - Firewall: `address` (full CRUD with filtering)
  - All HTTP methods covered: GET, POST, PUT, DELETE, SET
  - Special features: filtering, nested resources, ID-based and name-based operations

## [0.5.47] - 2026-01-09

### Changed
- **Code quality improvements**
  - Removed commented-out legacy convenience wrapper imports from `__init__.py`
  - Fixed docstring examples: `.list()` → `.get()` (8 occurrences in client.py)
  - Fixed endpoint count in README: 1,351 → 1,348 (accurate count)
  - Archived CHANGELOG entries v0.5.29 and earlier to `.dev/archive/CHANGELOG_ARCHIVE.md`
  - Added `Literal["exponential", "linear"]` type for `retry_strategy` parameter
  - Added `AuditHandler` Protocol type for `audit_handler` parameter (was `Any`)

### Fixed
- **Linting configuration and code fixes**
  - Configured flake8, black, and isort to exclude auto-generated `api/` folder
  - Fixed unused imports: `Literal` in models.py, `Coroutine` in _protocols.py
  - Fixed f-strings without placeholders in help.py (4 occurrences)
  - Added `normalize_table_field` to `_helpers/__all__` export list
  - All manual code now passes flake8, black, and isort checks

## [0.5.46] - 2026-01-09

### Changed
- **Documentation cleanup and consolidation**
  - Fixed markdown lint warnings across README.md, QUICKSTART.md, and package docs
  - Improved table formatting, list indentation, and code block consistency
  - Synced version numbers across all documentation files

## [0.5.45] - 2026-01-09

### Fixed
- **Improved type annotations for `fmt.to_dict()` function**
  - Changed return type from `dict[str, Any] | dict[int, Any]` to `dict`
  - Removes false Pylance errors when using `.get()` with string keys
  - Function behavior unchanged - still supports polymorphic dict conversions
  - Better reflects the dynamic nature of the function's return type

## [0.5.44] - 2026-01-09

### Added
- **Moved formatting utilities to core package as `fmt` module**
  - Renamed `hfortix_fortios.formatting` to `hfortix_core.fmt` for better accessibility
  - Simpler import: `from hfortix_core import fmt` instead of `from hfortix_fortios.formatting import ...`
  - Shorter module name: `fmt` instead of `formatting` (follows Python conventions)
  - All 13 formatting functions now available in core package
  - Usage: `fmt.to_list("80 443")`, `fmt.to_json(data)`, etc.
  - Original `formatting` module in hfortix_fortios still available for backward compatibility

## [0.5.43] - 2026-01-09

### Added
- **Enhanced formatting utilities module with 13 comprehensive functions**
  - Added `to_list()` with auto-split for space-delimited strings like `tcp_portrange`
    - Handles `"80 443 8080"` → `['80', '443', '8080']`
    - Preserves range notation: `"7000-7009"` → `['7000-7009']`
    - Supports custom delimiters: `to_list("a,b,c", delimiter=',')`
  - Added `to_dictlist()` for columnar to row format transformation
    - Converts `{'name': ['p1', 'p2'], 'action': ['accept', 'deny']}`
    - To `[{'name': 'p1', 'action': 'accept'}, {'name': 'p2', 'action': 'deny'}]`
  - Added `to_listdict()` for row to columnar format transformation
    - Inverse of `to_dictlist()` for data reshaping
  - Added `to_table()` for ASCII table formatting
  - Added `to_yaml()` for YAML-like output (no external dependencies)
  - Added `to_xml()` for simple XML formatting (no external dependencies)
  - Added `to_key_value()` for config file format output
  - Added `to_markdown_table()` for Markdown table generation
  - All functions are zero-dependency and handle edge cases gracefully
  - Perfect for handling FortiOS `tcp_portrange`, `udp_portrange` fields
  - Module location: `hfortix_fortios.formatting`

### Fixed
- **Fixed `tcp_portrange` display in test_autocomplete.py**
  - Removed incorrect iteration over `tcp_portrange` field
  - Field is a string (e.g., `"80 443"` or `"7000-7009"`), not a list
  - Now displays correctly without attempting to loop over characters
  - Use `to_list(service.tcp_portrange)` to split into individual ports

## [0.5.42] - 2026-01-09

### Fixed
- **Fixed hyphenated API response keys not matching TypedDict stubs**
  - Added automatic key normalization to convert hyphens to underscores in API responses
  - FortiOS returns keys like `tcp-portrange`, `cache-ttl`, `uuid-idx` with hyphens
  - Python TypedDict and attribute access require underscores: `tcp_portrange`, `cache_ttl`, `uuid_idx`
  - Normalization now happens automatically in HTTP client response processing
  - Fixes autocomplete and type checking for all fields with hyphens in their names
  - Example: `service['tcp_portrange']` now works (previously only `service['tcp-portrange']` worked)
  - Example: `addr.cache_ttl` now works in object mode
  - Added `normalize_keys()` utility function in `hfortix_core.utils`
  - Applied to both sync (`HTTPClient`) and async (`AsyncHTTPClient`) response processing

### Changed
- **Optimized helper file code generation using functools.partial**
  - Replaced ~200 lines of wrapper function definitions with ~10 lines of partial bindings in generated helper files
  - Reduced helper file size by ~50-80 lines per file without affecting functionality
  - Changed from pattern: `def get_field_type(field_name: str): return _get_field_type(FIELD_TYPES, field_name)`
  - To pattern: `get_field_type = partial(get_field_type, FIELD_TYPES)`
  - Saves ~2-3MB across 1,200+ generated helper files
  - IDE autocomplete, type hints, and introspection remain fully functional
  - Generator backup created in `.dev/generator/archive/pre-deduplication-20260109_113603/`
  - Updated validator template: `.dev/generator/templates/validator.py.j2`

- **Reduced helper module docstring verbosity**
  - Removed verbose docstring examples from helper utility modules
  - Kept concise descriptions for all public functions
  - Affected modules: `_helpers/builders.py`, `_helpers/converters.py`, `_helpers/normalizers.py`, `_helpers/response.py`, `_helpers/validation.py`
  - Reduced internal documentation overhead while maintaining clarity

## [0.5.41] - 2026-01-09

### Fixed
- **Fixed missing helper methods in DictMode and ObjectMode classes**
  - Added helper method signatures to mode-specific classes: `exists()`, `set()`, `defaults()`, `schema()`, `help()`, `fields()`, `field_info()`, `validate_field()`, `required_fields()`
  - Fixed "Attribute is unknown" errors when calling helper methods on mode-specific clients
  - Example: `fg.api.cmdb.authentication.rule.defaults()` now works correctly
  - Example: `fgt_object.api.cmdb.firewall.service.group.exists(name="test")` now works correctly
  - Helper methods were previously only available in base class, not in DictMode/ObjectMode
  - Regenerated all 1,064 endpoint `.pyi` stub files

## [0.5.40] - 2026-01-09

### Fixed
- **Fixed overload matching for mode-specific clients with keyword arguments**
  - Added explicit default `@overload` decorators for ObjectMode mutation methods (POST/PUT/DELETE)
  - Fixed "No overloads match" error when calling mutations with keyword args but no `response_mode`
  - ObjectMode methods now correctly infer return types without requiring explicit `response_mode="object"`
  - Example: `fgt_object.api.cmdb.firewall.policy.post(name="test", action="accept")` → `PolicyObject`
  - Previously required keyword-only `response_mode` parameter due to `*,` separator
  - DictMode already had proper default overloads; fixed ObjectMode to match
  - Regenerated all 1,064 endpoint `.pyi` stub files

## [0.5.39] - 2026-01-09

### Fixed
- **Fixed POST/PUT/DELETE type inference for mutation operations**
  - Added explicit `@overload` decorators for default case (no `response_mode` parameter)
  - Fixed "No overloads match" Pylance errors when calling mutations without `response_mode`
  - Removed `response_mode` parameter from final `def` implementation signatures
  - Made all mode override overloads keyword-only using `*,` separator
  - Pylance now correctly infers `MutationResponse` for default calls
  - Example: `delete(name="test")` → `MutationResponse`, not `RuleObject`
  - Fixed for both DictMode (default) and ObjectMode classes
  - Regenerated all 1,064 endpoint `.pyi` stub files

## [0.5.38] - 2026-01-09

### Fixed
- **Fixed Literal type validation in Payload TypedDict dict literals**
  - Removed `NotRequired` wrapper from Literal fields in Payload TypedDict stubs
  - Pylance now validates Literal values when assigning dict literals to Payload types
  - Example: `policy: PolicyPayload = {"action": "invalid"}` now shows type error
  - Previously, `NotRequired[Literal[...]]` prevented Pylance from validating inner Literal
  - Fields are still optional via `total=False` on the TypedDict class
  - All 1,064 endpoints regenerated with this fix

- **Fixed test template expecting list instead of dict for mkey queries**
  - Since v0.5.33, querying by mkey returns single dict, not list of one item
  - Updated test template to expect `dict` instead of `list` for `get(mkey=value)`
  - Regenerated all 936 auto-generated test files

## [0.5.37] - 2026-01-09

### Fixed
- **Fixed Pylance overload matching for default response mode**
  - Reordered stub file overloads: DEFAULT mode (no `response_mode`) now comes FIRST
  - Pylance matches overloads top-to-bottom; previous order caused `response_mode: Literal["object"] = ...` to match calls without `response_mode`
  - Fixed "Never is not iterable" error when iterating over table fields without explicit `response_mode`
  - Example: `for intf in rule["srcintf"]` now works without needing `response_mode="dict"`
  - Accessing nonexistent fields like `rule["nonexistent_field"]` now correctly shows TypedDict key error
  - Fixed in generator template and regenerated all 1,064 endpoints
  - Also fixed `post()`, `put()`, and `delete()` method overloads for consistency

### Added
- **Added `MutationResponse` TypedDict for POST/PUT/DELETE operations**
  - New `MutationResponse` type in `hfortix_core.types` with `status` and `http_status` fields
  - POST/PUT/DELETE now return `MutationResponse` instead of `dict[str, Any]`
  - Enables type checking for mutation responses: `result["nonexistent"]` now shows error
  - Example: `post_result["status"]` works, `post_result["nonexistent"]` shows error

- **Added `RawAPIResponse` TypedDict for `raw_json=True` mode**
  - New `RawAPIResponse` type for full FortiOS API envelope responses
  - Fields: `http_method`, `http_status`, `status`, `vdom`, `results`, `path`, `name`, `mkey`, `revision`, `serial`, `version`, `build`
  - All fields marked as required to provide autocomplete without warnings
  - Primary purpose: catch typos - `response["nonexistent"]` shows error
  - Use `.get()` for fields that may not be present in specific response types

- **Added validation hints to type stub comments**
  - Field comments now include: `Default: value`, `Min: value`, `Max: value`, `MaxLen: value`
  - Example: `cache_ttl: int  # Defines the minimal TTL... | Default: 0 | Min: 0 | Max: 86400`
  - Example: `name: str  # Address name. | MaxLen: 79`
  - Validation hints shown in Payload TypedDict, Response TypedDict, and Object classes
  - Also shown in nested TypedDict items for table field children
  - Helps developers understand field constraints without consulting documentation

## [0.5.36] - 2026-01-08

### Changed
- **Regenerated all 1,064 endpoints with enhanced TypedDict autocomplete**
  - Applied nested TypedDict fixes to all endpoints
  - Ensured all table field items have proper type hints
  - All endpoints now provide full autocomplete for nested table field items

## [0.5.35] - 2026-01-08

### Added
- **Nested TypedDict autocomplete for table field items in dict mode**
  - Generated TypedDict classes for all table field children (e.g., `RuleSrcintfItem`)
  - Full IDE autocomplete when iterating over table fields: `for intf in rule["srcintf"]: intf["name"]`
  - Type checking for nested items: `intf["nonexistent_field"]` now shows error
  - Fields are required (not `NotRequired`) since they're always present in API responses
  - Applies to all endpoints with table fields

### Fixed
- **Fixed type inference for default response mode**
  - Removed overly restrictive `raw_json: Literal[False]` constraint from default mode overloads
  - Pylance now correctly infers types when `response_mode` is not specified
  - Fixed `"Never" is not iterable` error when iterating over table fields
  - Response type inference now works regardless of client-level or request-level `response_mode` setting

## [0.5.34] - 2026-01-08

### Improved
- **Enhanced type stub overloads for better IDE autocomplete without explicit type annotations**
  - Added specific overloads for default mode (when `response_mode` is not specified)
  - Pylance now correctly infers `RuleResponse` type when querying by mkey without `response_mode`
  - Example: `rule = fgt.api.cmdb.authentication.rule.get(name="test")` now properly typed as `RuleResponse`
  - No longer need explicit type annotations like `rule: RuleResponse = ...`
  - Applies to all 1,064 endpoints
  - Improved overload ordering for better type inference

## [0.5.33] - 2026-01-08

### Fixed
- **Dict mode query by name now returns single dict instead of list**
  - When querying by name/mkey with `response_mode="dict"` (or default), now correctly returns single dict instead of list
  - Aligns dict mode behavior with object mode for consistency
  - Example: `group = fgt.api.cmdb.firewall.service.group.get(name="test")` returns `dict` not `list[dict]`
  - Both modes now have identical unwrapping behavior when querying by identifier
  - **Breaking Change**: Tests expecting list for single-item queries need to be updated
  - Fixed 936 auto-generated test files to expect dict instead of list

## [0.5.32] - 2025-01-24

### Fixed
- **Object mode query by name now returns single object instead of list**
  - When querying by name/mkey with `response_mode="object"`, now correctly returns single `FortiObject` instead of list
  - Added `unwrap_single=True` parameter to old API endpoints when querying by identifier
  - Example: `group = fgt.api.cmdb.firewall.service.group.get(name="test")` returns `FortiObject` not `list[FortiObject]`
  - Aligns old API behavior with new v2 API which already had this feature

- **FortiObject now wraps nested table field items instead of flattening to strings**
  - Table field members (lists of dicts) now wrapped in `FortiObject` for attribute access
  - Example: `group.member[0].name` now works (was: `AttributeError: 'str' object has no attribute 'name'`)
  - Changed from auto-flattening `[{"name": "test"}]` → `["test"]` to wrapping in `FortiObject`
  - Enables clean attribute access while maintaining compatibility

- **Clean string representation for simple FortiObject members**
  - Simple objects (containing only `name` and optionally `q_origin_key`) now show clean repr
  - Example: `['port3', 'port4']` instead of `[FortiObject(port3), FortiObject(port4)]`
  - Added `__str__` method for user-friendly output
  - Improves readability when printing lists of members

### Improved
- **Type annotations for FortiOS client attributes**
  - Added explicit type annotation `self._api: API = API(wrapped_client)` for better IDE support
  - Added type annotations to test helper modules (`fgt: FortiOS`, `fgt_ResponseModeObject: FortiOS`)
  - Improved Pylance autocomplete reliability after sys.path manipulation
  - Better type inference for `fgt.api`, `fgt.api.cmdb`, etc.

## [0.5.31] - 2026-01-08

### Added
- **Nested typed classes for table field children**
  - Generated specific typed classes for table field items (e.g., `GroupMemberObject`)
  - Each table field now has its own typed class with proper attribute definitions
  - Example: `member: list[GroupMemberObject]` instead of generic `list[FortiObject]`
  - Enables full IDE autocomplete for nested table attributes like `.name`, `.id`, etc.
  - Pylance now validates attribute access and shows errors for non-existent fields

- **Keyword argument support for mkey parameters**
  - Added overloads to support both positional and keyword mkey arguments
  - Both `get("name")` and `get(name="name")` now correctly infer single object return type
  - Proper overload ordering ensures Pylance matches the most specific signature
  - Works for both `response_mode="object"` and `response_mode="dict"`

### Improved
- **IDE autocomplete for table field members in object mode**
  - Table fields now return typed objects instead of generic `FortiObject`
  - Example: `group.member[0].name` shows autocomplete with proper type validation
  - Response objects in `response_mode="object"` provide full attribute autocomplete
  - Template generates nested classes for all table fields with children metadata

- **Whitespace stripping in table field normalization**
  - All string values automatically stripped of leading/trailing whitespace
  - Prevents "Entry not found" errors from accidental spaces in member names
  - Example: `" test_service1 "` → `"test_service1"` automatically
  - Applied to all normalizers: `normalize_table_field()`, `normalize_string_list()`, `normalize_source_destination_list()`

### Added
- **Enhanced parameter documentation with schema descriptions**
  - All POST and PUT method parameters now show field descriptions from FortiOS schema in IDE tooltips
  - Example: Hovering over function shows full Args section with descriptions for every parameter
  - Improved developer experience with rich, schema-driven documentation

- **Accurate type hints for table fields vs multi-value option fields**
  - Table fields: `str | list[str] | list[dict[str, Any]]` (supports flexible normalization)
  - Multi-value option fields: `Literal[...] | list[str]` (string list only, no dict support)
  - Single-value fields: Just their base type (`str`, `int`, `Literal[...]`)
  - Removes confusing `list[dict[str, Any]]` from option fields like `method`, `digest_algo`

- **Universal table field normalization with schema awareness**
  - Added `normalize_table_field()` helper that supports ANY mkey (not just "name")
  - Handles custom mkeys: `interface-name`, `id`, `index`, `seq-num`, `priority`, etc.
  - Auto-detects single-field (flexible) vs multi-field (strict) validation from schema
  - Generates intelligent examples based on field types (ip→192.168.1.10, id→1, cipher→TLS-AES-128-GCM-SHA256)
  - Shows format documentation for ALL table fields (removed 10-field limit)

### Fixed
- **Fixed table field documentation not showing for all fields**
  - Issue: Only 5 of 11 table fields were documented in complex endpoints like `firewall.vip`
  - Root cause: Schema parser used kebab-case keys, template expected snake_case keys
  - Solution: Convert field names to snake_case in `extract_table_fields_metadata()`
  - Result: All table fields now show complete format documentation in IDE tooltips

## [0.5.30] - 2026-01-08

### Fixed
- **Fixed stub generator comment truncation causing syntax errors**
  - Added `sanitize_comment` filter to properly truncate help text in `.pyi` stubs
  - Prevents broken comments like `# Sample one packet every configured number of packets (1 -`
  - Comments now safely truncate without breaking parentheses or special characters
  - Fixes Pylance failing to parse endpoints like `system.interface` due to syntax errors


---

**📦 Older versions (0.5.29 and earlier) archived to [`.dev/archive/CHANGELOG_ARCHIVE.md`](.dev/archive/CHANGELOG_ARCHIVE.md)**
