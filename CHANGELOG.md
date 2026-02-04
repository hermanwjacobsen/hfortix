# Changelog

> **Note**: All HFortix packages (hfortix-fortios, hfortix-core, hfortix) maintain synchronized versioning.
> This changelog is identical across the root repository and all public package repositories.

## [0.5.154] - 2026-02-02

### Improved

- **Enhanced PyPI Metadata**: Improved package discoverability and classification
  - **Keywords**: Added comprehensive search terms including `network-automation`, `network-administration`, `network-as-code`, `devops`, `netops`, `network-security`, `infrastructure-as-code`, `configuration-management`
  - **Classifiers**: Added audience and topic classifications
    - Audience: `Information Technology`, `Telecommunications Industry`
    - Topics: `Networking :: Monitoring`, `Systems Administration`
    - Language: `Natural Language :: English`
    - Compatibility: `Programming Language :: Python :: 3 :: Only`, `Operating System :: OS Independent`
    - Frameworks: `AsyncIO`, `Pydantic`, `Typed`
    - License: `Other/Proprietary License`
  - **Project URLs**: Added direct links to documentation, bug tracker, changelog, and source code
  - **Maintainer**: Added maintainer field for better package management
  - **Descriptions**: Enhanced package descriptions to highlight key features (type safety, async support, endpoint coverage)
  - **Impact**: Better search results on PyPI, clearer package purpose, easier navigation to resources
  - **Packages Updated**: All packages (hfortix-core, hfortix-fortios, hfortix) bumped to 0.5.154

# [0.5.153] - 2026-02-02

### Fixed

- **Type Stubs (.pyi) for Transaction Feature**: Added complete type hints for IDE support
  - Added `transaction.pyi` with full `Transaction` class signatures
  - Updated `client.pyi` with `transaction()`, `transactional()`, and `list_transactions()` method signatures
  - Updated `__init__.pyi` to export `Transaction` and `TransactionError` classes
  - **Impact**: Fixes IDE autocomplete, type checking, and IntelliSense for transaction feature
  - **Resolves**: "FortiOS has no attribute 'transaction'" type errors in VS Code, PyCharm, and mypy
  - **Packages Updated**: All packages (hfortix-core, hfortix-fortios, hfortix) bumped to 0.5.153 for consistency

# [0.5.152] - 2026-02-02

### Added

- **FortiOS Batch Transactions**: Atomic configuration changes with commit/rollback support (FortiOS 6.4.0+)
  - **Feature**: Group multiple API operations into a single atomic transaction
  - **Patterns**:
    - **Context Manager**: `with fgt.transaction() as txn:` - auto-commit on success, auto-abort on exception
    - **Decorator**: `@fgt.transactional()` - wrap entire functions in transactions
    - **Manual Control**: `txn.start()`, `txn.commit()`, `txn.abort()` for fine-grained control
  - **Methods**:
    - `fgt.transaction(timeout=60, auto_commit=True, auto_abort=True)` - Create transaction context manager
    - `fgt.transactional(timeout=60)` - Decorator for transactional functions
    - `fgt.list_transactions()` - List active transactions (FortiOS 7.4.1+)
    - `txn.show()` - Preview cached commands before commit (FortiOS 7.4.1+)
    - `txn.commit()` - Apply all changes atomically
    - `txn.abort()` / `txn.rollback()` - Discard all pending changes
  - **Properties**: `txn.transaction_id`, `txn.is_active`, `txn.is_committed`, `txn.is_aborted`
  - **Use Cases**:
    - **Atomic configuration**: All changes succeed or fail together
    - **Safe rollback**: Undo complex multi-step changes on error
    - **Bulk operations**: Create/update/delete many objects efficiently
    - **Migration**: Move configuration between VDOMs or devices safely
  - **Example - Context Manager**:
    ```python
    with fgt.transaction() as txn:
        fgt.api.cmdb.system.interface.post({...})
        fgt.api.cmdb.firewall.address.post({...})
        fgt.api.cmdb.firewall.policy.post({...})
    # Auto-commits on success, auto-aborts on exception
    ```
  - **Example - Decorator**:
    ```python
    @fgt.transactional(timeout=120)
    def setup_infrastructure():
        fgt.api.cmdb.system.interface.post({...})
        fgt.api.cmdb.firewall.address.post({...})
        return {"status": "success"}
    
    setup_infrastructure()  # Runs in transaction
    ```
  - **Example - Manual Control**:
    ```python
    with fgt.transaction(auto_commit=False) as txn:
        fgt.api.cmdb.firewall.policy.post({...})
        if validation_passes():
            txn.commit()
        else:
            txn.abort()
    ```
  - **Error Handling**: Raises `TransactionError` for nested transactions or invalid operations
  - **Limitations**: One transaction per connection, scoped to single VDOM, timeout enforced
  - **Documentation**: See `docs/fortios/TRANSACTIONS.md` for complete guide with patterns and best practices
  - **Tests**: Comprehensive test suite in `.tests/live/txn/test_transactions.py` (10 tests, all passing)
  - **Files Added**: 
    - `packages/fortios/hfortix_fortios/transaction.py` (459 lines)
    - HTTP client modified for automatic X-TRANSACTION-ID header injection
    - FortiOS client extended with transaction methods

- **HTTP API Request Inspection**: New `http_api_request` and `fmg_api_request` properties on all response objects
  - **Feature**: All `FortiObject`, `FortiObjectList`, and `ContentResponse` instances now include complete HTTP request details
  - **Access via**: 
    - `result.http_api_request` - Returns dictionary with method, url, endpoint, params, data, and timestamp
    - `result.fmg_api_request` - Alias for FortiManager proxy connections (same data, clearer naming)
  - **Use cases**:
    - **Debugging**: See exactly what request was sent to FortiGate/FortiManager (URL, params, data)
    - **Audit logging**: Include full request context in application logs
    - **Troubleshooting**: Verify filters, parameters were constructed correctly
    - **Documentation**: Generate API examples from actual requests
    - **Testing**: Validate request construction in unit tests
  - **Works with**: All API operations (GET, POST, PUT, DELETE), both direct FortiGate and FortiManager proxy clients
  - **Example - Direct FortiGate**:
    ```python
    result = fgt.api.cmdb.firewall.policy.get(filter='srcaddr==internal')
    print(result.http_api_request)
    # {'method': 'GET', 'url': 'https://...', 'params': {...}, ...}
    ```
  - **Example - FortiManager Proxy**:
    ```python
    result = fmg.devices['FGT-01'].api.cmdb.firewall.policy.get()
    print(result.fmg_api_request)  # Clearer naming for FMG proxy
    # {'method': 'POST', 'url': 'https://fmg.../jsonrpc', 'data': {...}, ...}
    ```
  - **Documentation**: See `docs/fortios/HTTP_API_REQUEST.md` for complete guide and examples
  - **Tests **: Comprehensive test suite in `.tests/schema-validators/test_api_request_properties.py`

### Fixed

- **Generator: FIELD_TYPES Comment Escaping**: Fixed syntax errors in generated validator files caused by improper help text truncation
  - **Issue**: Generator template was truncating field help text to 60 characters inside Python comments without escaping special characters
  - **Symptoms**: Syntax errors in 16 validator files (e.g., `enable:Enable setti` broken mid-sentence, unescaped quotes/colons)
  - **Root Cause**: Template `.dev/generator/templates/validator.py.j2` used `field.help[:60]` before escaping, causing invalid Python syntax when truncation split words or exposed special characters
  - **Solution**: 
    - Properly escape special characters BEFORE truncating: `|replace('\r', '')|replace('\n', ' ')|replace('\\', '\\\\')|replace('"', '\\"')`
    - Increased comment length limit from 60 to 80 characters for better readability
    - Applied same escaping pattern already used in `FIELD_DESCRIPTIONS` section
  - **Impact**: ✅ All 1,447 schema validator tests now passing (was 16 failures)
  - **Files Regenerated**: 7 validator helper files in `cmdb/monitoring/` and `cmdb/system/` categories

# [0.5.151] - 2026-02-02

### Added

- **Comprehensive Test Suite**: Complete test infrastructure with schema validators and live integration tests
  - **1,447 schema validator tests** across 786 files covering 100% of 1,348 generated endpoints
  - **80+ live integration test files** for real API testing with FortiGate/FortiManager
  - **Unified test runner** (`.tests/run_all_tests.py`) supporting both offline and live testing
  - **Fast execution**: Schema validators run in ~5 seconds with parallel execution (no API calls)
  - **Complete documentation**: `.tests/README.md`, `.tests/INDEX.md`, `.tests/TESTCOVERAGE.md`
  - **CI/CD ready**: Offline tests for every commit, full integration tests for releases
  - **Coverage breakdown**: CMDB (561), Monitor (490), Log (286), Service (11) endpoint validators
  - See `TESTING.md` and `.tests/` directory for complete test coverage details

### Changed

- **Documentation Updates**: Enhanced beta status messaging and stability guarantees
  - Updated README with clearer beta status explanation
  - Added recommendation to stay on version 0.5.150+
  - Clarified breaking change policy (possible before v1.0.0, but not expected after v0.5.150)
  - Updated ReadTheDocs with latest endpoint counts (1,348 total) and test coverage
  - Created comprehensive TESTING.md document with detailed test coverage information

### Fixed

- **Meta Package: py.typed Marker**: Added `py.typed` marker file to meta package to fix mypy import-untyped warning
  - **Issue**: `from hfortix import FortiOS` showed "module is installed, but missing library stubs or py.typed marker"
  - **Root Cause**: Meta package (`hfortix`) was missing the `py.typed` marker file
  - **Solution**: 
    - Created empty `py.typed` file in `packages/meta/hfortix/`
    - Added explicit package-data configuration in `packages/meta/pyproject.toml`
  - **Impact**: ✅ Mypy now recognizes the package as typed, no more import warnings

# [0.5.150] - 2026-02-02

### Fixed

- **Core: SSL Certificate Error Retry Logic**: Fixed retry mechanism to immediately fail on SSL/certificate errors instead of retrying 3 times
  - **Root Cause**: `_should_retry()` in `HTTPClientBase` only checked for network/timeout/HTTP errors, treating all `ConnectError` instances as transient failures
  - **Solution**: Added SSL error detection before retry logic - checks error message for SSL/certificate indicators and returns `False` immediately
  - **Impact**: ✅ No more wasteful retry attempts on permanent SSL failures (certificate validation, hostname mismatch, handshake errors)
  - **Location**: `hfortix_core/http/base.py` - `_should_retry()` method
  - **User Benefit**: Faster error feedback and clearer error logs when SSL configuration is incorrect

- **FortiOS: Legacy Endpoint Cleanup**: Fixed outdated `user/tacacs_plus.py` endpoint to match current code patterns
  - **Issues Fixed**:
    - `exists()` method accessing private `_wrapped_client` attribute → Changed to use public `self.get()` API
    - `get_schema()` passing `action` as parameter → Changed to `payload_dict={"action": format}`
    - `move()` method using non-existent `request()` → Changed to `put()` with params
    - `clone()` method using non-existent `request()` → Changed to `post()` with data
  - **Root Cause**: Readonly endpoint with manually maintained code predating v0.5.149 template fixes
  - **Impact**: ✅ All 2,327+ endpoints now use consistent, correct patterns
  - **Location**: `hfortix_fortios/api/v2/cmdb/user/tacacs_plus.py`

### Changed

- **Core: Improved Error Messages**: SSL/certificate errors now log at ERROR level with clearer message: "SSL/Certificate error (not retrying)"
  - Makes it immediately obvious that the error is permanent and won't be retried
  - Helps users quickly identify and fix SSL configuration issues

# [0.5.149] - 2026-02-02

### Fixed

- **Generator: Type System Cleanup**: Resolved all type checker errors in generated endpoint files through comprehensive template updates
  
  **Issue 1 - Response Processing Wrapper Pattern**: Fixed type mismatch between `IHTTPClient` protocol (returns `dict[str, Any]`) and actual endpoint return types (returns `FortiObject`/`FortiObjectList`)
  - **Root Cause**: `ResponseProcessingClient` wrapper transforms `dict` → `FortiObject` at runtime, but type checkers see protocol signature
  - **Solution**: Added `# type: ignore[return-value]` to all HTTP client method calls (GET, PUT, POST, DELETE)
  - **Rationale**: Intentional design - wrapper pattern provides enhanced response objects while maintaining clean protocol interface
  - **Impact**: ✅ Eliminated 2,327+ type errors across all endpoint files
  
  **Issue 2 - Action Methods Using Wrong HTTP Interface**: Fixed `move()` and `clone()` methods attempting to call non-existent `request()` method
  - **Root Cause**: `IHTTPClient` protocol only defines `get()`, `post()`, `put()`, `delete()` - no generic `request()` method
  - **Solution**: 
    - `move()`: Changed from `request(method="PUT")` → `put()` with params
    - `clone()`: Changed from `request(method="POST")` → `post()` with params
  - **Impact**: ✅ Fixed action methods in all 2,327+ endpoint files with move/clone support
  
  **Issue 3 - Invalid Internal Attribute Access**: Fixed `exists()` method attempting to access private `_wrapped_client` attribute
  - **Root Cause**: Protocol interface doesn't expose internal wrapper implementation details
  - **Solution**: Changed from `self._client._wrapped_client.get()` → `self.get()` with proper error handling
  - **Rationale**: Use public API instead of reaching into private implementation
  - **Impact**: ✅ Fixed exists() method in all endpoints that support creation
  
  **Issue 4 - Incorrect Parameter Passing**: Fixed `get_schema()` passing `action` as function parameter instead of URL query parameter
  - **Root Cause**: User insight - "isn't action a URL parameter and not body/payload?"
  - **Solution**: Changed from `self.get(action=format)` → `self.get(payload_dict={"action": format})`
  - **Rationale**: `payload_dict` in `get()` is copied to `params` dict for URL query parameters
  - **Impact**: ✅ Fixed schema retrieval in all 2,327+ endpoints
  
  **Issue 5 - Async/Sync Return Type Mismatch**: Fixed `exists()` method return type not supporting both synchronous and asynchronous clients
  - **Root Cause**: Return type declared as `bool` but method returns `Coroutine[Any, Any, bool]` for async clients
  - **Solution**: Changed return type to `Union[bool, Coroutine[Any, Any, bool]]`
  - **Impact**: ✅ Proper dual-mode support for sync and async clients
  
  **Issue 6 - Type Narrowing Limitations**: Added type ignore comments for unavoidable Python type system limitations
  - **Root Cause**: Type checkers cannot narrow `Union[T, Coroutine[T]]` types inside conditional blocks
  - **Solution**: Added `# type: ignore[misc]` and `# type: ignore[union-attr]` with explanatory comments
  - **Rationale**: Fundamental Python type system limitation - code is correct at runtime
  - **Impact**: ✅ Documented expected type checker behavior
  
  **Issue 7 - Protocol Signature Incompatibility**: Added type ignore for protocol method signature mismatches
  - **Root Cause**: Protocols use minimal `**kwargs` signature, implementations add field-specific parameters for autocomplete
  - **Solution**: Added `# type: ignore[override]` to GET/POST/PUT/DELETE methods with explanatory comments
  - **Rationale**: Intentional design - implementations extend protocol for better developer experience
  - **Impact**: ✅ Documented design pattern, suppressed false-positive errors
  
  **Issue 8 - Invalid exists() Methods**: Removed `exists()` method from endpoints that don't support object creation
  - **Root Cause**: Generator was creating `exists()` for all GET endpoints, but it's only useful for POST endpoints
  - **Solution**: Updated template condition from `'GET' in http_methods` → `'POST' in http_methods and 'GET' in http_methods`
  - **Rationale**: `exists()` is used to check before creation - meaningless for read-only/update-only endpoints
  - **Impact**: ✅ Removed unnecessary exists() methods from ~800 non-creatable endpoints
  
  **Issue 9 - get_schema() Return Type Too Narrow**: Fixed return type not accounting for potential list responses
  - **Root Cause**: `get_schema()` calls `self.get()` which can return `FortiObjectList`, but return type only declared `FortiObject`
  - **Solution**: Changed return type to `Union[FortiObject, FortiObjectList, Coroutine[Any, Any, Union[FortiObject, FortiObjectList]]]`
  - **Impact**: ✅ Accurate return type for schema retrieval across all endpoints
  
  **Files Changed**:
  - `.dev/generator/templates/endpoint_class.py.j2`: 
    - Added `# type: ignore[return-value]` to GET/PUT/POST/DELETE method calls
    - Added `# type: ignore[override]` to method signatures with explanatory comments
    - Added `# type: ignore[misc]` and `# type: ignore[union-attr]` to exists() with comments
    - Fixed move() and clone() to use put()/post() instead of request()
    - Fixed exists() to use self.get() instead of _wrapped_client access
    - Fixed get_schema() to use payload_dict parameter
    - Updated exists() return type to Union[bool, Coroutine[Any, Any, bool]]
    - Updated get_schema() return type to include FortiObjectList
    - Restricted exists() generation to POST-supporting endpoints only
  
  **Regenerations**: All 2,327+ endpoint files regenerated 8 times during troubleshooting process
  
  **Final Result**: Zero type errors across entire codebase ✅

### Changed

- **Generator: Enhanced Type Annotations**: All generated endpoint methods now include comprehensive explanatory comments
  - Protocol signature mismatches documented with reason and design rationale
  - Type narrowing limitations documented as Python type system constraints
  - Wrapper pattern architecture explained inline for future maintainers

# [0.5.148] - 2026-01-31

### Documentation

- **ReadTheDocs: Comprehensive Documentation Audit**: Fixed inconsistencies across all documentation
  - Corrected authentication parameter: `api_key` → `token` throughout all docs
  - Fixed exception class names: `HTTPError`/`NotFoundError` → `APIError`/`ResourceNotFoundError`
  - Fixed method names: `.create()`/`.update()`/`.list()` → `.post()`/`.put()`/`.get()`
  - Fixed result property: `result.status_code` → `result.http_status_code`
  - Fixed exception attribute: `e.status_code` → `e.http_status`
  - Updated list field examples to show both formats: `['HTTP', 'HTTPS']` (recommended) and `[{"name": "HTTP"}]`

- **Removed Deprecated Documentation**: Cleaned up outdated convenience wrapper documentation
  - Removed `docs/source/fortios/api-reference/convenience-wrappers.rst`
  - Removed `docs/source/fortios/convenience-wrappers/` directory
  - Updated all references that pointed to deprecated convenience methods

- **Updated Example Files**: All code examples now use correct API patterns
  - `custom-wrappers.md`: Fixed error handling with `ResourceNotFoundError`
  - `fmg-proxy.md`: Fixed error handling with `APIError`
  - `endpoint-methods.md`: Fixed result property access
  - Multiple guide files updated with correct exception handling

### Changed

- **Version Bumped**: All packages updated to 0.5.148
  - `hfortix-core`: 0.5.147 → 0.5.148
  - `hfortix-fortios`: 0.5.147 → 0.5.148
  - `hfortix` (meta): 0.5.147 → 0.5.148
  - Updated root pyproject.toml from 0.5.141 → 0.5.148

# [0.5.147] - 2026-01-28

### Documentation

- **README: Major Simplification**: Drastically shortened README from 2,337 lines to ~360 lines (85% reduction)
  - Removed extensive version history (available in CHANGELOG.md)
  - Removed detailed feature descriptions (available on ReadTheDocs)
  - Focused on essential quick start, installation, and examples
  - Added prominent ReadTheDocs links throughout
  - Better GitHub presentation for new users

- **README: Enhanced Content**: Added missing important features while keeping it concise
  - **Beta status warning** with version and status information
  - **FortiObject response access patterns** showing attribute vs dictionary access, single object returns, nested support
  - **Authentication options** with 3 methods: API key, username/password, environment variables
  - **Advanced features section** with Pydantic models, action methods (move/clone/exists), read-only mode, operation tracking
  - **Enhanced documentation links** including QUICKSTART.md, ASYNC_GUIDE.md, PERFORMANCE_TESTING.md, SECURITY.md
  - **Installation options** showing meta-package alternatives (`hfortix[fortios]`, `hfortix[all]`)
  - **Expanded Key Capabilities** listing 9 specific advanced features with Pydantic model count

- **README: API Coverage Clarity**: Improved table to distinguish endpoint coverage from response field types
  - Added "Endpoint Coverage" column showing 100% across all categories
  - Renamed "Type Coverage" to "Response Field Types" for clarity
  - Clear explanation that all 1,348 endpoints are functional
  - Autocomplete availability clearly indicated per category

- **README: Code Examples**: All examples now use synchronous code (no async)
  - Simpler for beginners to understand
  - Async support mentioned in features but not demonstrated
  - Authentication examples with environment variables
  - FortiManager proxy example updated to synchronous

- **TODO.md Updates**:
  - Updated version references from v0.5.130 to v0.5.146+
  - Added recent improvements section (v0.5.146, v0.5.145, v0.5.130)
  - Added FortiManager Batch Operations planning section
  - FortiManager multi-device batch API design documented (~3 weeks effort)

### Changed

- **Version Bumped**: All packages updated to 0.5.147
  - `hfortix-core`: 0.5.146 → 0.5.147
  - `hfortix-fortios`: 0.5.146 → 0.5.147
  - `hfortix` (meta): 0.5.146 → 0.5.147
  - Updated all internal dependencies to reference 0.5.147

# [0.5.146] - 2026-01-24

### Fixed

- **Generator: Module Alias Resolution in Type Stubs**: Fixed critical bug where module aliases in category `__init__.py` files were not being resolved correctly when generating `.pyi` type stub files.
  
  **The Problem**: When a category imports a module with an alias (e.g., `from . import client as client_ns`), the generator was capturing the alias name instead of the actual module name, resulting in broken imports like `from .client_ns import Client` (module doesn't exist).
  
  **The Solution**: Enhanced generator to:
  - Parse both `from . import module` and `from . import module as alias` patterns
  - Build `module_aliases` dict to map aliases to actual module names
  - Resolve aliases back to actual module names when generating imports
  
  **Impact**:
  - ✅ WiFi client autocomplete now works correctly (`client.mac`, `client.ip`, etc.)
  - ✅ Type checking properly shows errors for non-existent fields (`client.nonexistent_field`)
  - ✅ Fixed for all categories with aliased imports (338 .pyi files regenerated)
  
  **Files Changed**:
  - `.dev/generator/generate.py`: Added alias resolution logic
  - All category `__init__.pyi` files: Regenerated with correct import paths

### Improved

- **Schema: Major Response Fields Enhancement**: Significant improvements to response field coverage and accuracy across all endpoint categories:
  
  **Log Archives**: 12/12 endpoints now have detailed response fields (was 0)
  - All log archive endpoints (`app_ctrl.archive`, `dlp.archive`, etc.) now include 7-8 response fields
  - Fields include: `filename`, `filesize`, `download_available`, timestamps, etc.
  
  **Monitor Endpoints**: Enhanced response field definitions
  - Integer enum values now properly handled (previously caused generation failures)
  - 490 monitor endpoints regenerate successfully with accurate type hints
  
  **Overall Coverage**:
  - CMDB: 560/561 endpoints (99.8%)
  - Monitor: 230/490 endpoints with response fields (46.9%)
  - Service: 8/11 endpoints (72.7%)
  - Log: 12/12 endpoints with response fields (100%)
  
  **Impact**:
  - Better IDE autocomplete for API responses
  - More accurate type hints for response data
  - Improved documentation and field descriptions

# [0.5.145] - 2026-01-24

### Changed

- **FortiManager Login/Logout Now Return FortiObject**: Updated `login()` and `logout()` methods to return `FortiObject` instances instead of plain dicts, providing access to status codes, messages, session information, and FMG metadata properties.
  
  **Breaking Change**: 
  - `fmg.login()` now returns `FortiObject` (was `dict[str, Any]`)
  - `fmg.logout()` now returns `FortiObject` (was `dict[str, Any]`)
  
  **Usage**:
  ```python
  # Login response (FortiObject with FMG properties)
  login_response = fmg.login()
  print(login_response["result"][0]["status"]["code"])  # 0 = success
  print(login_response["session"])  # Session token
  print(login_response.fmg_raw)  # Full raw response
  
  # Logout response (FortiObject with FMG properties)
  logout_response = fmg.logout()
  print(logout_response["status"]["code"])  # 0 = success
  print(logout_response["status"]["message"])  # Status message
  print(logout_response.fmg_raw)  # Full raw response
  
  # FMG metadata properties available:
  # - .fmg_raw - Full JSON-RPC response
  # - .fmg_status_code - Status code from response
  # - .fmg_status_message - Status message
  # - .json - JSON serializable dict
  # - .dict - Dictionary representation
  ```
  
  **Benefits**:
  - Consistent API - all FMG operations return FortiObject instances
  - Access to all FMG metadata properties (.fmg_raw, etc.)
  - Access to status codes and error messages
  - Better error handling and debugging
  - Type hints updated in stub files (.pyi)

### Technical Details

- Modified `FortiManagerProxy.login()` and `FortiManagerProxy.logout()` to wrap responses in FortiObject
- Core library `HTTPClientFMG.login()` and `HTTPClientFMG.logout()` still return plain dicts
- FortiObject wrapper provides FMG metadata properties (.fmg_raw, .fmg_status_code, etc.)
- Updated type stubs to reflect new return types (FortiObject instead of dict[str, Any])
- Maintains backward compatibility for dict-style access (response["key"])
- Adds attribute-style access for FMG properties (response.fmg_raw)

# [0.5.144] - 2026-01-24

### Changed

- **FortiManager Login/Logout Now Return FortiObject**: Updated `login()` and `logout()` methods to return `FortiObject` instances instead of `None`, providing access to status codes, messages, session information, and FMG metadata properties.
  
  **Breaking Change**: 
  - `fmg.login()` now returns `FortiObject` (was `None`)
  - `fmg.logout()` now returns `FortiObject` (was `None`)
  
  **Usage**:
  ```python
  # Login response (FortiObject with FMG properties)
  login_response = fmg.login()
  print(login_response["result"][0]["status"]["code"])  # 0 = success
  print(login_response["session"])  # Session token
  print(login_response.fmg_raw)  # Full raw response
  
  # Logout response (FortiObject with FMG properties)
  logout_response = fmg.logout()
  print(logout_response["status"]["code"])  # 0 = success
  print(logout_response["status"]["message"])  # Status message
  print(logout_response.fmg_raw)  # Full raw response
  
  # FMG metadata properties available:
  # - .fmg_raw - Full JSON-RPC response
  # - .fmg_status_code - Status code from response
  # - .fmg_status_message - Status message
  # - .json - JSON serializable dict
  # - .dict - Dictionary representation
  ```
  
  **Benefits**:
  - Consistent API - all FMG operations return FortiObject instances
  - Access to all FMG metadata properties (.fmg_raw, etc.)
  - Access to status codes and error messages
  - Better error handling and debugging
  - Type hints updated in stub files (.pyi)

### Technical Details

- Modified `FortiManagerProxy.login()` and `FortiManagerProxy.logout()` to wrap responses in FortiObject
- Core library `HTTPClientFMG.login()` and `HTTPClientFMG.logout()` still return plain dicts
- FortiObject wrapper provides FMG metadata properties (.fmg_raw, .fmg_status_code, etc.)
- Updated type stubs to reflect new return types (FortiObject instead of dict[str, Any])
- Maintains backward compatibility for dict-style access (response["key"])
- Adds attribute-style access for FMG properties (response.fmg_raw)

# [0.5.143] - 2026-01-23

### Fixed

- **Type Safety for CMDB Response Objects**: Restored proper type checking for undefined attributes on CMDB response objects (SettingObject, AddressObject, etc.). Previously, `__getattr__` was accidentally added to the FortiObject stub file during this session, which made Pylance treat all undefined attributes as `Any` instead of showing errors.

  **Solution**: 
  - Removed `__getattr__` from `models.pyi` stub file (restored to last commit state)
  - Runtime `models.py` still has `__getattr__` for dynamic access at runtime
  - Stub omission forces Pylance to validate attributes against typed subclasses
  
  **Behavior**:
  - ✅ Defined fields (e.g., `status.username`, `status.mailto1`) → proper types with autocomplete
  - ❌ Undefined fields (e.g., `status.nonexistent`) → Pylance error: "Attribute is unknown"
  - ✅ Runtime still works with dynamic fields via `models.py` implementation

### Technical Details

- The intentional omission of `__getattr__` from stub files is a documented pattern for achieving type safety with dynamic attribute access. This was the original design (see commit 4d49b9cdb) and has been restored.

# [0.5.142] - 2026-01-23

### Fixed

- **Circular Reference in FMG Proxy Responses**: Fixed `ValueError: Circular reference detected` error when calling `.json` property on FortiObject instances created from FortiManager proxy responses. The issue was caused by adding `fmg_raw` (which contains the full response) to the `results` dict, creating an infinite loop: `results['fmg_raw']['response']['results']['fmg_raw']...`
  
  **Solution**: 
  - Modified FMG proxy client to NOT add `fmg_raw` to the `results` dict (prevents circular reference at source)
  - `fmg_raw` remains accessible via `.fmg_raw` property on FortiObject instances
  - All other FMG metadata (status codes, target, URL, etc.) still available in `results`
  - Added defensive circular reference detection in `FortiObject.json` and `FortiObjectList.json` properties as a safety net

- **JSON Serialization Safety**: Enhanced `FortiObject.json` and `FortiObjectList.json` properties with circular reference detection. Any circular references (from any source) are now replaced with `"<circular reference>"` placeholder instead of crashing.

### Changed

- **FMG Proxy Response Structure**: Cleaner data structure without circular references. `fmg_raw` is now only at the envelope level (accessible via property), not embedded in `results` dict. This improves memory efficiency and prevents JSON serialization issues.

# [0.5.141] - 2026-01-22

### Fixed

- **FortiManager HTTP Status**: Fixed missing `http_status` field in FortiManager proxy responses. FMG proxy responses now synthesize `http_status` (200 for success, 400 for error) based on the response status since FMG's JSON-RPC protocol doesn't provide HTTP status codes.
- **FortiObject Attribute Access**: Fixed critical bug where `__getattr__` method was accidentally deleted, breaking all dynamic attribute access on `FortiObject` instances. All endpoint-specific fields (e.g., `mailto1`, `name`, etc.) now work correctly again.
- **FMG Properties on FortiObject**: Added FMG metadata properties to the base `FortiObject` class (not just `FMGFortiObject`) to ensure they're accessible on all responses from FMG proxy requests. Properties check both `_raw_envelope` and `_data` for maximum compatibility.

### Changed

- **FMG Proxy Client**: Updated to add synthesized `http_status` field to responses when not present, ensuring consistent behavior between direct FortiOS connections and FMG proxy connections.

# [0.5.140] - 2026-01-22

### Fixed

- **DeviceResult AttributeError**: Fixed `AttributeError: 'DeviceResult' object has no attribute '_data'` that occurred when checking `if proxy_response.first`. Removed `FMGFortiObject` inheritance from `DeviceResult` and `ProxyResponse` dataclasses since they don't need dict-wrapping behavior.
- **FMG Metadata Accessibility**: Added FMG metadata properties (`fmg_proxy_status_code`, `fmg_proxy_status_message`, `fmg_proxy_target`, `fmg_proxy_url`, `fmg_url`, `fmg_status_code`, `fmg_status_message`, `fmg_id`, `fmg_raw`) to both `FortiObject` and `FortiObjectList` classes. These properties are now accessible on all responses from FMG proxy requests with full IDE autocomplete support via updated type stubs.
- **FMG Proxy Response Processing**: Updated FMG proxy client to merge metadata into both top-level response envelope and `results` dict, ensuring metadata is preserved when responses are processed into `FortiObject` or `FortiObjectList` instances.

### Changed

- **Type Stub Updates**: Updated `.pyi` stub files for `FortiObject` and `FortiObjectList` to include FMG metadata properties for full Pylance/IDE autocomplete support.

# [0.5.139] - 2026-01-22

### Fixed

- **Version Alignment & PyPI Fix**: All packages (`hfortix-core`, `hfortix-fortios`, `hfortix`) bumped to 0.5.139 to resolve PyPI version propagation issues and ensure all dependencies are aligned. This fixes installation errors due to missing or mismatched meta-package versions on PyPI.

# [0.5.137] - 2026-01-22

### Changed

- **FMG Field Scoping Refactor**: FMG proxy/status fields (`fmg_proxy_status_code`, `fmg_proxy_status_message`, `fmg_proxy_target`, `fmg_proxy_url`, `fmg_url`, `fmg_status_code`, `fmg_status_message`, `fmg_id`, `fmg_raw`) are now only present on `FMGFortiObject`, which is used by FMGProxy models (`DeviceResult`, `ProxyResponse`). The base `FortiObject` is unchanged for all other usage. This resolves type and attribute errors and ensures correct field scoping for FMG-specific data.

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).



## [0.5.135] - 2026-01-22

### Added

- **FMG Proxy/Status/Raw Fields**: `DeviceResult` and `ProxyResponse` now include:
  - `.fmg_proxy_status_code`, `.fmg_proxy_status_message`, `.fmg_proxy_target`, `.fmg_proxy_url`, `.fmg_url`, `.fmg_status_code`, `.fmg_status_message`, `.fmg_id`, `.fmg_raw`
  - These fields provide direct access to FortiManager proxy status, target, URLs, and the full raw FMG JSON-RPC response for both the top-level proxy and each device result.
- **Type Stub Support**: All new fields are included in `.pyi` stubs for full IDE/Pylance autocomplete and type checking.

### Changed

- **Dependencies**: Installing `hfortix-fortios` now also installs `hfortix` and `hfortix-core` (all >=0.5.135). All inter-package dependencies updated to `>=0.5.135`.

### Fixed

- Dataclass field order and indentation issues in `models.py` resolved for compatibility with Python and Pylance.

## [0.5.131] - 2026-01-21

Readme and other docs updated


## [0.5.136] - 2026-01-22

### Changed

- Removed debug print of full FMG JSON-RPC response in FMG proxy client; output is now normal.
- FMG proxy/status fields (`fmg_status_code`, `fmg_proxy_status_code`, etc.) are now available on all `FortiObject` instances for universal autocomplete and compatibility.

### Note

FMG fields are now only present on `FMGFortiObject`, which is used by FMGProxy models (`DeviceResult`, `ProxyResponse`). The base `FortiObject` is unchanged for all other usage.

### Added

- **FortiManagerProxy Enhancements**: Added `get_devices()`, `get_adoms()`, and `get_device()` methods for device and ADOM queries via FortiManager.
- **Type Stub Updates**: Updated `.pyi` files to provide IDE/Pylance support for new proxy methods.

### Fixed

- **Pylance Attribute Errors**: Resolved unknown attribute errors in IDE by updating type stubs for new methods.

### Changed

- **Version Bump and PyPI Release**: Bumped all package versions to `0.5.134` and published to PyPI.

## [0.5.133] - 2026-01-22

### Changed

- Bumped package versions to `0.5.133` for PyPI release.

## [0.5.132] - 2026-01-22

### Changed

- Bumped package versions to `0.5.132` for PyPI release.

### Fixed

- **Array Type in TypedDict Payloads**: Fixed array fields in .pyi stub files causing type variance errors
  - **Issue**: Array fields in TypedDict payloads typed as `int | str | list[int | str]` caused variance errors
  - **Example Bug**: `url: int | str | list[int | str]` rejected `list[str]` due to list invariance
  - **Root Cause**: Template added union types for "convenience" but Python's `list` is invariant
  - **Solution**: Changed array fields to `list[str]` in .pyi stub files
  - **Impact**: Array parameters now accept lists without type variance errors
    - ✅ `select.post(url=["https://..."])` → no type error
    - ✅ TypedDict payloads properly typed for type checkers

- **Array Type Parameters**: Fixed array-type request fields being typed as `Any` instead of `list[str]`
  - **Issue**: Generator's type mapping didn't include `"array"` type, causing fallback to `Any`
  - **Example Bug**: `url: Any | None` instead of `url: list[str] | None` for utm/rating-lookup/select
  - **Solution**: Added `"array": "list[str]"` mapping to `_to_python_type()` function
  - **Impact**: All array-type request fields now correctly typed as `list[str]`
    - ✅ `monitor.utm.rating_lookup.select.post(url=["..."])` → correctly typed as `list[str] | None`
    - ✅ Type checker no longer shows variance errors for list parameters

- **Literal Types for Array Parameters**: Fixed incorrect Literal type extraction for array-type parameters
  - **Issue**: Schema parser was extracting enum values from array parameter descriptions and applying them to the array parameter itself
  - **Example Bug**: `filters: Literal["exact", "contains", ...]` instead of `filters: list[str]`
  - **Root Cause**: Description text like "Op: filter operator [exact|contains|...]" was being parsed as Literal values for the `filters` array parameter
  - **Solution**: Modified schema parser to skip Literal type extraction for parameters with `type: "array"`
  - **Impact**: Array parameters now correctly typed as `list[str]` while preserving Literal types for actual enum parameters
    - ✅ `monitor.user.device.query.get(filters=["..."])` → correctly typed as `list[str] | None`
    - ✅ `monitor.user.device.query.get(query_type="latest")` → still has `Literal["latest", "unified_latest", "unified_history"]`

### Tests

- **UTM Rating Lookup Endpoints** (1 file, 3 tests):
  - `utm/rating-lookup/select` (3 tests): URL rating lookup, language parameter support, multiple URL batch queries
  - Test coverage for FortiGuard web filtering rating queries

## [0.5.130] - 2026-01-20

### Fixed

- **CRITICAL: Context-Aware Field Name Conversion**: Fixed `ems_id` and other fields used across multiple API types
  - **Root Cause**: Fields like `ems_id` appear in both CMDB and Monitor endpoints but need different handling:
    - CMDB endpoints: `ems_id` → `ems-id` (convert to kebab-case)
    - Monitor endpoints: `ems_id` → `ems_id` (preserve underscore)
  - **Previous Issue**: `build_api_payload()` checked ALL underscore preservation lists, causing CMDB endpoints to incorrectly preserve underscores
  - **Example Bug**: `cmdb.endpoint_control.fctems.put(ems_id=3)` sent `{"ems_id": 3}` but API expects `{"ems-id": 3}` → HTTP 500
  - **Solution**: Added `api_type` parameter to `build_api_payload()` for context-specific behavior
    - CMDB endpoints: Only check `CMDB_BODY_FIELD_NO_HYPHEN` (4 fields)
    - Monitor endpoints: Only check `MONITOR_BODY_FIELD_NO_HYPHEN` (200 fields)
    - Log endpoints: Only check `LOG_BODY_FIELD_NO_HYPHEN` (0 fields)
    - Service endpoints: Auto-detect based on context
  - **Impact**: Context-sensitive fields now work correctly in all API types
    - ✅ `cmdb.endpoint_control.fctems.put(ems_id=3)` → `{"ems-id": 3}` (CMDB: converts to hyphen)
    - ✅ `monitor.endpoint_control.ems.status.get(ems_id=5)` → `{"ems_id": 5}` (Monitor: preserves underscore)
    - ✅ All 1,064 endpoints regenerated with proper `api_type` context

### Changed

- **Generator Template**: Updated `endpoint_class.py.j2` to emit `api_type="{{ schema.category }}"` in all `build_api_payload()` calls
- **Payload Builders**: Enhanced `build_api_payload()` with context-aware field name conversion
  - New parameter: `api_type: Literal["cmdb", "monitor", "log", "service"] | None`
  - Context-specific underscore preservation based on API type
  - Legacy behavior preserved when `api_type=None` (checks all lists)
- **All Endpoints**: Regenerated 1,064 endpoints with proper API type context

### Documentation

- Updated builder function docstrings with `api_type` parameter documentation

### Tests

- **System Monitor Endpoints**: Added comprehensive testing for FortiGate system monitoring endpoints (11 files, 22 tests)
  - **Configuration Management** (2 files, 7 tests):
    - `system/config-script` (4 tests): Script execution history, upload/execute, delete
    - `system/config-revision` (3 tests): List revisions, save revision, update comments
  - **Admin & Session Monitoring** (2 files, 2 tests):
    - `system/current-admins` (1 test): Active admin sessions
    - `system/interface-connected-admins-info` (1 test): Admin sessions by interface
  - **System Resources & Status** (4 files, 4 tests):
    - `system/vdom-resource` (1 test): VDOM resource usage statistics
    - `system/global-resources` (1 test): Global system resource allocation
    - `system/vdom-link` (1 test): VDOM link configuration and status
    - `system/ntp-status` (1 test): NTP synchronization status
  - **Time Management** (1 file, 2 tests):
    - `system/time` (2 tests): Get/set system time with Unix timestamp and component-based formats
  - **DHCP Management** (1 file, 2 tests):
    - `system/dhcp` (2 tests): Active DHCP lease monitoring, lease revocation by IP
  - **Security Fabric** (1 file, 2 tests):
    - `system/csf` (2 tests): Fabric topology, pending device authorizations
  - **System Upgrade** (1 file, 3 tests):
    - `system/upgrade/report` (3 tests): Saved reports, report existence check, current report
  - **Test Environment**: FortiGate v7.6.5 build 3651, VDOM: test, hfortix-fortios v0.5.130
  - **Test Results**: 214 total monitor tests passed, 1 skipped

## [0.5.129] - 2026-01-20

### Fixed

- **CRITICAL: Schema-Driven Field Preservation**: Auto-generated comprehensive lists of fields with underscores
  - **Root Cause**: FortiOS API inconsistently uses both underscores AND hyphens in field names
    - CMDB endpoints: Mostly kebab-case (`ems-id`, `source-ip`)
    - Monitor endpoints: Mix of both (`id_list`, `file_content` with underscores, others with hyphens)
    - Same parameter differs by context: `ems-id` in CMDB vs `ems_id` in Monitor
  - **Previous Issue**: Only 2 Monitor fields preserved (file_content, key_file_content), but API has 200+ underscore fields!
  - **Solution**: Created automated schema scanner that found ALL fields with underscores
    - Scanned 1,350+ schema files
    - Found 204 total fields where API expects underscores (not hyphens)
  - **New Field Lists** (auto-generated from schemas):
    - `CMDB_BODY_FIELD_NO_HYPHEN`: 4 fields (block_ack_flood, block_ack_flood_thresh, block_ack_flood_time, switch_dhcp_opt43_key)
    - `MONITOR_BODY_FIELD_NO_HYPHEN`: 200 fields (id_list, file_content, ems_id, account_id, ip_address, mac_address, etc.)
    - `LOG_BODY_FIELD_NO_HYPHEN`: 0 fields
    - `SERVICE_BODY_FIELD_NO_HYPHEN`: 0 fields
  - **Impact**: All underscore fields now work correctly
    - ✅ `monitor.system.config_script.delete.post(id_list=[...])` → `{"id_list": [...]}` (was `{"id-list": [...]}` → HTTP 400)
    - ✅ `monitor.system.config_script.upload.post(file_content="...")` → `{"file_content": "..."}`
    - ✅ `monitor.endpoint_control.ems.status.get(ems_id=5)` → params with `ems_id=5`
    - ✅ `monitor.registration.forticare.login.post(account_id="user@example.com")` → `{"account_id": "..."}`
    - ✅ All 200+ Monitor underscore fields now preserved correctly

### Added

- **Generator Tools** (`generator/` directory):
  - `scan_underscore_fields.py` - Scans all schemas to find fields with underscores
  - `update_field_overrides.py` - Auto-updates field_overrides.py from schemas
  - `example_generator_integration.py` - Integration example for generator workflow
  - `README.md` - Documentation for generator tools
  - **Integration**: Can be called during code generation to keep field lists in sync with schemas

### Changed

- **Field Override Lists**: Now auto-generated from schemas (was manually maintained)
  - `CMDB_BODY_FIELD_NO_HYPHEN`: 0 → 4 fields
  - `MONITOR_BODY_FIELD_NO_HYPHEN`: 2 → 200 fields
  - Ensures field conversion always matches actual API expectations

### Documentation

- `docs/fortios/UNDERSCORE_HYPHEN_INCONSISTENCY.md` - Comprehensive guide to the API inconsistency
- `UNDERSCORE_HYPHEN_FIX_SUMMARY.md` - Fix summary and impact analysis
- `generator/README.md` - Generator tools documentation

### Tests

- `test_underscore_preservation.py` - Unit tests for underscore field preservation
- `test_id_list_bug_fix.py` - Integration test for original user bug report

## [0.5.128] - 2026-01-20

### Fixed

- **CRITICAL: Context-Aware Parameter Conversion System**: Implemented proper separation of query parameter vs body field handling
  - **Root Cause**: Previous whitelist didn't distinguish between query params (keep underscore) and body fields (convert to hyphen)
  - **Solution**: Split into context-specific lists for each API type
    - `*_QUERY_PARAM_NO_HYPHEN` - Query/path parameters that preserve underscores
    - `*_BODY_FIELD_NO_HYPHEN` - Body fields that exceptionally preserve underscores (rare!)
  - **New Architecture**:
    - CMDB: 7 query params, 0 body field exceptions
    - Monitor: 104 query params, 0 body field exceptions
    - Log: 7 query params, 0 body field exceptions
    - Service: 0 query params, 0 body field exceptions
  - **Impact**: Body fields now correctly convert to hyphen format
    - ✅ `icap/server.post(ip_address="192.168.1.1")` → `{"ip-address": "192.168.1.1"}` (was HTTP 500)
    - ✅ `user/banned/check.post(ip_address="10.0.0.1")` → `{"ip-address": "10.0.0.1"}`
    - ✅ `router/charts.post(ip_mask="255.255.255.0")` → `{"ip-mask": "255.255.255.0"}`
    - ✅ `fortiview.post(ip_version=4)` → `{"ip-version": 4}`
    - ✅ `user/device/query.post(filter_logic="and")` → `{"filter-logic": "and"}`
    - ✅ All 102 dual-context parameters now work correctly in both contexts
  - **Files Updated**:
    - `_helpers/field_overrides.py` - New context-specific lists
    - `_helpers/builders.py` - Use `*_BODY_FIELD_NO_HYPHEN` for body conversion

### Added

- **Context-Specific Parameter Lists**: Eight new lists for fine-grained control
  - `CMDB_QUERY_PARAM_NO_HYPHEN` - 7 params (datasource_format, find_all_references, primary_keys, skip_to, unfiltered_count, with_contents_hash, with_meta)
  - `CMDB_BODY_FIELD_NO_HYPHEN` - 0 params (empty - all CMDB body fields use hyphens)
  - `MONITOR_QUERY_PARAM_NO_HYPHEN` - 104 params (ip_address, ip_mask, ip_version, filter_logic, timestamp_from, etc.)
  - `MONITOR_BODY_FIELD_NO_HYPHEN` - 0 params (empty - all Monitor body fields use hyphens)
  - `LOG_QUERY_PARAM_NO_HYPHEN` - 7 params (filter_logic, is_ha_member, keep_session_alive, serial_no, session_id, timestamp_from, timestamp_to)
  - `LOG_BODY_FIELD_NO_HYPHEN` - 0 params (empty - all Log body fields use hyphens)
  - `SERVICE_QUERY_PARAM_NO_HYPHEN` - 0 params (empty)
  - `SERVICE_BODY_FIELD_NO_HYPHEN` - 0 params (empty)

### Changed

- **Payload Builders**: Updated to use context-specific body field lists
  - `build_cmdb_payload()` - Uses `CMDB_BODY_FIELD_NO_HYPHEN` (currently empty)
  - `build_cmdb_payload_normalized()` - Uses `CMDB_BODY_FIELD_NO_HYPHEN`
  - `build_api_payload()` - Uses `MONITOR_BODY_FIELD_NO_HYPHEN` (for Monitor/Service)
  - All body fields now default to kebab-case conversion unless explicitly whitelisted

### Deprecated

- **Legacy Unified Lists**: `NO_HYPHEN_PARAMETERS_*` lists maintained for backward compatibility
  - These are computed as union of query + body lists for each API type
  - New code should use context-specific `*_QUERY_PARAM_NO_HYPHEN` or `*_BODY_FIELD_NO_HYPHEN` lists

### Technical Details

- **Dual-Context Parameters**: 102 parameters used in BOTH query and body contexts
  - Examples: ip_address, ip_version, filter_logic, timestamp_from, mac_address
  - Now properly handled: underscore in queries, hyphen in body
- **Body Field Exceptions**: Currently 0 across all API types
  - All known "exceptions" were actually query parameters
  - Future exceptions can be added to `*_BODY_FIELD_NO_HYPHEN` as discovered

## [0.5.127] - 2026-01-20

### Fixed

- **Critical Bug Fix: CMDB endpoint-control.fctems**: Fixed `fctems.put(ems_id=4)` failing with "ems-id is required for PUT"
  - **Root Cause**: `ems_id` was incorrectly in `NO_HYPHEN_PARAMETERS`, preventing conversion to API field name `ems-id`
  - **Impact**: All CMDB endpoints using `ems_id` as body field (e.g., PUT/POST operations) now work correctly
  - **Note**: Monitor endpoints using `ems_id` as query parameter are unaffected (query params handled separately)

### Changed

- **NO_HYPHEN_PARAMETERS Cleanup**: Removed 97 incorrect entries, reducing from 211 to 113 parameters
  - **Analysis**: Comprehensive schema scan revealed many parameters in the list don't actually exist in schemas
  - **Verification**: All 113 remaining parameters confirmed to exist across 2,591+ schema files
  - **Categories**: CMDB (8), Monitor (104), Log (4), Service (0)
  - **Breaking**: No user-facing impact - only internal whitelist cleanup

### Added

- **API-Type-Specific Parameter Lists**: Split `NO_HYPHEN_PARAMETERS` by API type for better maintainability
  - `NO_HYPHEN_PARAMETERS_CMDB`: 8 parameters (query/path params for CMDB endpoints)
  - `NO_HYPHEN_PARAMETERS_MONITOR`: 104 parameters (query/path params for Monitor endpoints)
  - `NO_HYPHEN_PARAMETERS_LOG`: 4 parameters (query/path params for Log endpoints)
  - `NO_HYPHEN_PARAMETERS_SERVICE`: 0 parameters (empty set, reserved for future)
  - **Backward Compatibility**: Unified `NO_HYPHEN_PARAMETERS` maintained as union of all sets

## [0.5.126] - 2026-01-20

### Changed

- **Upload to PyPI**: Published hfortix-fortios, hfortix-core, and hfortix meta-packages

## [0.5.125] - 2026-01-20

### Changed

- **Comprehensive NO_HYPHEN_PARAMETERS Update**: Expanded parameter whitelist from 3 to 162 parameters to prevent incorrect conversion:
  - **Analysis**: Scanned 2,591+ schema files across FortiOS 7.4.8 and 7.6.5
  - **Previous**: Only `file_content`, `key_file_content`, `id_list` (3 parameters)
  - **Updated**: All 162 request parameters containing underscores now preserved
  - **Verification**: Confirmed zero format conflicts (no param exists in both formats)
  - **Impact**: Eliminates entire class of potential parameter conversion bugs
  - **Categories Covered**:
    - File operations (36+ endpoints): `file_content`, `key_file_content`, `file_id`
    - Network/IP params (32+ endpoints): `ip_version`, `ip_address`, `ip_mask`, etc.
    - Authentication (20+): `account_id`, `old_password`, `new_password`, `is_government`
    - Certificates/PKI (15+): `acme_*`, `scep_*`, `common_name`, `subject_alt_name`
    - Queries (20+): `query_id`, `filter_logic`, `timestamp_from`, `timestamp_to`
    - WiFi/Wireless (15+): `wtp_id`, `radio_id`, `image_id`, `region_name`
    - HA/Clustering (10+): `serial_no`, `vcluster_id`, `parent_peer1`
    - And 85+ more across all categories
  - **Documentation**: New `docs/fortios/NO_HYPHEN_PARAMETERS.md` with complete reference
  - **Files Updated**: `packages/fortios/hfortix_fortios/_helpers/field_overrides.py`

### Added

- **Documentation**: `docs/fortios/NO_HYPHEN_PARAMETERS.md` - Comprehensive reference for all 162 parameters
- **Documentation**: `docs/fortios/NO_HYPHEN_PARAMETERS_ANALYSIS.md` - Detailed analysis report with statistics

## [0.5.124] - 2026-01-20

### Fixed

- **Generator Bug: Array type handling in .pyi stub files**: Fixed critical bug where generator incorrectly converted `"type": "array"` from JSON schemas to `str` instead of `list[Any]` in type stub files:
  - **Issue**: Array fields like `id_list` were typed as `str` causing type checking errors
  - **Root Causes**:
    1. `_to_python_type()` function in `pyi_generator.py` had no mapping for `'array'` type
    2. Template `endpoint_class.pyi.j2` had no conditional check for `field.type == 'array'`
  - **Fix Applied in TWO locations**:
    1. **Generator** (`.dev/generator/generators/pyi_generator.py`):
       - Added `'array': 'list[Any]'` to type mapping in `_to_python_type()`
    2. **Template** (`.dev/generator/templates/endpoint_class.pyi.j2`):
       - Added `{% elif field.type == 'array' %}` checks in 6 locations:
         - Payload TypedDict (line ~193)
         - Response TypedDict (line ~226)
         - Object Class (line ~394)
         - POST method signature (line ~648)
         - PUT method signature (line ~704)
         - SET method signature (line ~788)
  - **Impact**: All endpoints with array fields now have correct type hints
  - **Example Fix** (`monitor/system/config-script/delete`):
    ```python
    # Before (WRONG):
    id_list: str | None = ...
    
    # After (CORRECT):
    id_list: list[Any] | None = ...
    ```

- **Parameter Name Conversion: Added `id_list` to NO_HYPHEN_PARAMETERS**: Fixed bug where `id_list` parameter was incorrectly converted to `id-list` when sending to API:
  - **Issue**: Same category of bug as `file_content` - library converting underscores to hyphens when API expects underscores
  - **Root Cause**: `id_list` not in `NO_HYPHEN_PARAMETERS` whitelist
  - **Fix**: Added `"id_list"` to `NO_HYPHEN_PARAMETERS` set in `_helpers/field_overrides.py`
  - **Affected Endpoint**: `monitor/system/config-script/delete`
  - **Files Updated**: `packages/fortios/hfortix_fortios/_helpers/field_overrides.py`

## [0.5.123] - 2026-01-20

### Fixed

- **File Upload Endpoints: Complete fix for parameter transformation bug**: Fixed critical bug where `file_content` and `key_file_content` parameters were being incorrectly transformed in TWO locations, causing HTTP 400 errors on all file upload/import endpoints:
  - **Issue**: v0.5.122 only fixed ONE of two conversion points - the bug persisted
  - **Root Cause**: Library converts parameter names in two separate locations:
    1. ✅ Payload builders (`_helpers/builders.py`) - FIXED in v0.5.122
    2. ❌ Client wrapper (`client.py` line 740) - STILL BROKEN in v0.5.122
  - **Complete Fix**: Added `NO_HYPHEN_PARAMETERS` whitelist to BOTH locations:
    - `build_api_payload()` in `_helpers/builders.py` ✅
    - `build_cmdb_payload()` in `_helpers/builders.py` ✅
    - `build_cmdb_payload_normalized()` in `_helpers/builders.py` ✅
    - `convert_field_names()` in `client.py` ✅ NEW in v0.5.123
  - **Centralized Configuration**: Created `_helpers/field_overrides.py` for single source of truth:
    - `NO_HYPHEN_PARAMETERS` - Parameters that must keep underscores
    - `PYTHON_KEYWORD_TO_API_FIELD` - Python keyword mappings (also moved here)
  - **Files Updated**:
    - `packages/fortios/hfortix_fortios/client.py` - Fixed `convert_field_names()`
    - `packages/fortios/hfortix_fortios/_helpers/field_overrides.py` - NEW centralized config
    - `packages/fortios/hfortix_fortios/_helpers/builders.py` - Import from central config
  - **Impact**: All 15+ file upload endpoints now work correctly
  - **Example**:
    ```python
    # Now works correctly end-to-end:
    result = fgt.api.monitor.system.config_script.upload.post(
        filename="test.conf",
        file_content=base64_content  # ✅ Preserved through entire pipeline
    )
    ```

## [0.5.122] - 2026-01-20

### Fixed

- **File Upload Endpoints: Incorrect parameter transformation** (INCOMPLETE FIX - see v0.5.123): Fixed critical bug where `file_content` and `key_file_content` parameters were incorrectly transformed from underscore to hyphen format, causing HTTP 400 errors on all file upload/import endpoints:
  - **Issue**: Library converted `file_content="data"` → `{"file-content": "data"}` but FortiOS API expects `{"file_content": "data"}` (underscore, not hyphen)
  - **Root Cause**: `build_api_payload()` unconditionally converted ALL snake_case parameters to kebab-case, but these file parameters are exceptions
  - **Affected Endpoints** (15+):
    - `monitor/system/config-script/upload` - Upload and run config script
    - `monitor/system/config/restore` - Restore configuration from file
    - `monitor/system/firmware/upgrade` - Upload firmware image
    - `monitor/vpn-certificate/ca/import` - Import CA certificate
    - `monitor/vpn-certificate/local/import` - Import local certificate (also has `key_file_content`)
    - `monitor/wifi/firmware/upload` - Upload WiFi firmware
    - `monitor/switch-controller/fsw-firmware/upload` - Upload FortiSwitch firmware
    - `monitor/extender-controller/extender/upgrade` - Upload FortiExtender firmware
    - `monitor/license/database/upgrade` - Upload license database
    - `monitor/web-ui/language/import` - Import language file
    - `monitor/wifi/region-image/upload` - Upload WiFi region image
    - And 5+ more firmware/certificate/config endpoints
  - **Fix**: Added `NO_HYPHEN_PARAMETERS` whitelist in `_helpers/builders.py`:
    ```python
    NO_HYPHEN_PARAMETERS = {
        "file_content",      # File upload endpoints
        "key_file_content",  # Certificate import endpoints
    }
    ```
  - **Implementation**: Updated conversion logic in all 3 payload builders:
    - `build_cmdb_payload()` - CMDB API endpoints
    - `build_cmdb_payload_normalized()` - CMDB with auto-normalization
    - `build_api_payload()` - Monitor/Service endpoints
  - **Impact**: All file upload endpoints now work correctly
  - **Example**:
    ```python
    # Before (v0.5.121 and earlier): HTTP 400 error
    result = fgt.api.monitor.system.config_script.upload.post(
        filename="test.conf",
        file_content=base64_content  # ❌ Sent as "file-content"
    )
    
    # After (v0.5.122+): Works correctly
    result = fgt.api.monitor.system.config_script.upload.post(
        filename="test.conf",
        file_content=base64_content  # ✅ Sent as "file_content"
    )
    ```
  - **Schema Verification**: Confirmed all affected schemas define `"file_content"` with underscore in 7.4.8 and 7.6.5 schema files
  - **Files Updated**: `packages/fortios/hfortix_fortios/_helpers/builders.py`

## [0.5.121] - 2026-01-20

### Added

- **Schema Override System**: Implemented flexible JSON-based override system for schema metadata corrections
  - **Purpose**: Fix schema metadata issues that cannot be auto-detected from FortiOS API documentation
  - **Location**: `.dev/generator/schema_management/schema_overrides.json`
  - **Capabilities**:
    - `scope` - Override endpoint scope (global/vdom/unknown)
    - `scope_options` - Set valid scope options (e.g., ['global'] for global-only endpoints)
    - `readonly` - Mark endpoints as read-only
    - `capabilities` - Deep merge capabilities metadata (CRUD flags, features, limits)
    - `response_fields` - Add response field definitions for monitor/service endpoints
    - `query_params` - Add or override query parameters by HTTP method
  - **Implementation**: 
    - `SchemaParser.load_overrides()` - Loads overrides from JSON (cached)
    - `SchemaParser.apply_overrides()` - Deep merges overrides into parsed schemas
    - Automatic application during schema parsing
  - **Documentation**: 
    - `SCHEMA_OVERRIDES.md` - Comprehensive usage guide with examples
    - JSON file includes inline documentation and examples
  - **Files Added**:
    - `.dev/generator/schema_management/schema_overrides.json`
    - `.dev/generator/schema_management/SCHEMA_OVERRIDES.md`
  - **Files Updated**:
    - `.dev/generator/schema_management/schema_parser.py` (added override methods)

### Fixed

- **Monitor Endpoints: Config-Script Scope Correction**: Fixed incorrect scope for system config-script endpoints
  - **Issue**: All 4 config-script endpoints incorrectly marked as `scope="unknown"` instead of `"global"`
  - **Affected Endpoints**:
    - `monitor/system/config-script` - List/retrieve config scripts
    - `monitor/system/config-script/run` - Execute config script
    - `monitor/system/config-script/delete` - Delete config script history
    - `monitor/system/config-script/upload` - Upload and run config script
  - **Fix**: Applied schema overrides setting `scope="global"` and `scope_options=["global"]`
  - **Impact**: Generated endpoints now correctly:
    - Omit `vdom` parameter from method signatures (global-only)
    - Hardcode `vdom=False` in API calls
    - Operate at global scope only (affects entire FortiGate system)
  - **Technical**: Override system enables permanent fixes without manual schema edits
  - **Files Updated**: All regenerated monitor/system/config_script* endpoints

## [0.5.120] - 2026-01-19

### Fixed

- **Type System: Protocol Interface Updates**: Enhanced `IHTTPClient` protocol to match actual implementation
  - **Issue**: Pylance showing stale type errors in some endpoint files after `models.pyi` changes from `dict[str, Any]` to `Mapping[str, Any]`
  - **Root Cause**: `IHTTPClient` protocol was missing parameters that `ResponseProcessingClient` wrapper actually provides
  - **Fix**: Added missing parameters to `IHTTPClient.get()` method signature:
    - `unwrap_single: bool = False` - Auto-unwrap single-item lists to single object
    - `action: Optional[str] = None` - Special action parameter (e.g., 'schema', 'default')
  - **Impact**: Resolves type checking errors while maintaining backward compatibility
  - **Files Updated**: `packages/core/hfortix_core/http/interface.py` (protocol definition)
  - **Note**: All endpoint files are generated from same template - apparent errors were Pylance cache artifacts

### Changed

- **Type Safety: FortiObject Generic Bound**: Changed TypeVar bound from `dict[str, Any]` to `Mapping[str, Any]`
  - **Location**: `packages/fortios/hfortix_fortios/models.pyi` line 11
  - **Reason**: TypedDict types are compatible with `Mapping` but not with `dict` in Python's type system
  - **Impact**: Allows generated TypedDict types to work seamlessly with `FortiObject[T]` generic wrapper
  - **Related**: This change triggered Pylance cache issues that surfaced the `IHTTPClient` protocol incompleteness

## [0.5.119] - 2026-01-19

### Added

- **Tests: Switch Controller Monitor Endpoints**: Added 11 test files for FortiLink device detection and policy matching:
  - **switch_controller_detected_device.py** (3 tests): GET - Retrieve a list of devices detected on all switches (Access Group: wifi)
    - Test: 12 physical devices detected on switch ports
  - **switch_controller_matched_devices.py** (5 tests): GET - Return a list of devices that match NAC and/or dynamic port policies (Access Group: wifi)
    - Test: NAC policy matching (0 devices, 1 test skips)
  - **switch_controller_isl_lockdown_status.py** (3 tests): GET - Get current status of ISL lockdown (Access Group: wifi)
    - Test: ISL lockdown status = "enable"

- **Environment Variable Support**: Added `FORTIOS_PORT` environment variable support with automatic type conversion
  - **Use Case**: Simplifies port configuration when using environment variables
  - **Behavior**: Reads `FORTIOS_PORT` from environment and converts string to integer automatically
  - **Priority**: Explicit `port` parameter > `FORTIOS_PORT` environment variable > default (443)
  - **Example**: `export FORTIOS_PORT=8443` then `FortiOS()` - automatically uses port 8443
  - **Documentation**: Updated docstring with example and added port parameter description explaining automatic conversion

### Fixed

- **Type Flexibility**: Port parameter now accepts both `int` and `str` types with automatic conversion
  - **Issue**: Users passing environment variable values like `port=os.getenv("FORTIOS_PORT", "443")` got type errors because `os.getenv()` returns strings
  - **Common Pattern**: Many users load configuration from environment: `port=FORTIGATE_PORT` where `FORTIGATE_PORT = os.getenv("FORTIOS_PORT", "443")`
  - **Fix**: 
    - Updated type hints in both `client.py` and `client.pyi` to `Union[int, str, None]`
    - Added automatic string-to-int conversion in `__init__` for both direct parameters and environment variables
    - Updated both sync and async overload signatures
  - **Impact**: No more `int()` wrapper needed - can pass environment variable strings directly to port parameter
  - **Example**: Both `port=8443` and `port="8443"` now work identically
  - **Files Updated**: `client.py` (implementation + type hints), `client.pyi` (type stubs)

### Documentation

- **Schema Improvement Suggestions**: Updated `docs/fortios/SCHEMA_IMPROVEMENT_SUGGESTIONS.md` with OpenAPI vs FortiOS schema gap analysis
  - **New Section**: "OpenAPI vs FortiOS Schema" explaining the difference between documentation and SDK schema requirements
  - **Partial Schema Issue**: Documented endpoints with incomplete OpenAPI schemas (e.g., `dhcp-snooping` with undefined array items)
  - **Example**: Shows how `dhcp-snooping` has `snooping_entries` defined as array but lacks item properties
  - **Clarification**: OpenAPI specs exist but don't automatically provide type safety - FortiOS schema files need complete `response_fields`
  - **Priority Updates**: Added notation for endpoints with partial OpenAPI documentation

## [0.5.118] - 2026-01-19

### Added

- **Tests: Switch Controller Managed Switch Monitor Endpoints**: Added 7 test files for FortiSwitch monitoring:
  - **switch_controller_managed_switch_faceplate_xml.py**: GET - Retrieve XML for rendering FortiSwitch faceplate widget (Access Group: wifi)
  - **switch_controller_managed_switch_factory_reset.py**: POST - Send 'Factory Reset' command to a given FortiSwitch (Access Group: wifi)
  - **switch_controller_managed_switch_dhcp_snooping.py**: GET - Retrieve DHCP servers monitored by FortiSwitches (Access Group: wifi)
  - **switch_controller_managed_switch_transceivers.py**: GET - Get a list of transceivers being used by managed FortiSwitches (Access Group: any)
  - **switch_controller_managed_switch_bios.py**: GET - Get a list of BIOS info by managed FortiSwitches (Access Group: any)
  - **switch_controller_managed_switch_health_status.py**: GET - Retrieve health-check statistics for managed FortiSwitches (Access Group: wifi)
  - **switch_controller_managed_switch_port_health.py**: GET - Retrieve port health statistics for managed FortiSwitches (Access Group: wifi)

### Documentation

- **Schema Improvement Suggestions for Fortinet**: Created `docs/fortios/SCHEMA_IMPROVEMENT_SUGGESTIONS.md` documenting missing response field definitions in monitor endpoints
  - **Issue**: 100+ monitor endpoints lack response field schemas, causing `FortiObject[Any]` instead of typed responses
  - **Impact**: No IDE autocomplete, no type checking, poor developer experience for monitor endpoints
  - **Request**: Add `response_fields` to schema files with proper field types, categories, and options
  - **Priority endpoints**: Switch controller (17 endpoints), system status (15 endpoints), VPN (12 endpoints), firewall sessions (8 endpoints)
  - **Example**: Shows before/after comparison for dhcp-snooping endpoint with full field definitions

- **README: Known Limitations**: Added section documenting monitor endpoint schema limitations in `packages/fortios/README.md`
  - **Explanation**: Why monitor endpoints return `FortiObject[Any]` (missing field schemas)
  - **Affected categories**: Switch controller, system status, VPN, firewall sessions, network diagnostics, routing, WiFi
  - **Workarounds**: Dynamic attribute access, iteration support (v0.5.118+), `.dict`/`.json` properties
  - **Reference**: Links to schema improvement suggestions document

### Fixed

- **Type Safety: FortiObject iteration support**: Added `__iter__` method to `FortiObject` class to enable iteration over list-based responses:
  - **Issue**: Monitor endpoints returning lists caused Pylance error: `"FortiObject[Unknown]" is not iterable - "__iter__" method not defined`
  - **Root Cause**: Type stubs (`.pyi`) didn't declare `__iter__`, so type checkers couldn't recognize FortiObject as iterable
  - **Fix**: Added `__iter__` method to both `models.pyi` stub and `models.py` runtime implementation
  - **Implementation**: Checks if `_data` contains a `results` list (monitor endpoints) or is itself a list, then yields FortiObject instances
  - **Impact**: Can now iterate over monitor endpoint responses without type checker warnings
  - **Example**: 
    ```python
    result = fgt.api.monitor.switch_controller.managed_switch.dhcp_snooping.get()
    for entry in result:  # ✅ No more type error
        print(entry.switch_id)
    ```

- **Type Safety: Explicit Any type for untyped endpoints**: Changed generator template to use `FortiObject[Any]` instead of bare `FortiObject`:
  - **Issue**: Endpoints without field definitions showed `FortiObject[Unknown]` type, implying incomplete type information
  - **Root Cause**: Generic `FortiObject` defaults to `Unknown` type parameter when not specified
  - **Fix**: Updated `.dev/generator/templates/endpoint_class.pyi.j2` to explicitly use `FortiObject[Any]` for endpoints lacking field definitions
  - **Affected endpoints**: Monitor endpoints, service endpoints, and other endpoints without response field schemas
  - **Impact**: Better semantics - `Any` means "can be any dict structure" vs `Unknown` which implies missing type information
  - **Locations updated** (11 total):
    - Monitor/service endpoint GET returns (singleton and list)
    - CMDB endpoint GET returns (with/without mkey)
    - POST method returns
    - PUT method returns
    - DELETE method returns
    - Helper method returns (`field_info`, `defaults`, `schema`)
  - **Example**: Type now shows `FortiObject[Any]` instead of `FortiObject[Unknown]`

### Documentation

- **Schema Improvement Suggestions**: Created comprehensive document for Fortinet detailing missing response field definitions in monitor endpoints
  - **File**: `docs/fortios/SCHEMA_IMPROVEMENT_SUGGESTIONS.md`
  - **Content**: Documents 100+ monitor endpoints lacking response field schemas, impact on developer experience, recommended schema structure
  - **Examples**: Detailed before/after comparisons showing how field definitions enable type safety and IDE autocomplete
  - **Priority list**: Switch controller, system status, VPN, firewall session, and network diagnostics endpoints

- **README: Known Limitations section**: Added documentation about monitor endpoint schema limitations
  - **Location**: `packages/fortios/README.md`
  - **Content**: Explains why monitor endpoints return `FortiObject[Any]`, lists affected endpoint categories, provides workarounds
  - **Workarounds**: Dynamic attribute access, iteration support (v0.5.118+), references schema improvement suggestions document

## [0.5.117] - 2026-01-19

### Added

- **Tests: Switch Controller Managed Switch Test Suite**: Added 5 test files with 14 tests for FortiSwitch management:
  - **switch_controller_managed_switch_status.py** (1 test): GET managed switch status
  - **switch_controller_managed_switch_port_stats.py** (3 tests): GET all FortiSwitch port statistics, verify port statistics structure, GET with mkey filter
  - **switch_controller_managed_switch_port_stats_reset.py** (3 tests): POST to reset all port statistics, POST to reset specific ports, verify reset operation
  - **switch_controller_managed_switch_poe_reset.py** (3 tests): POST to reset PoE on safe port (down + PoE-capable), verify safe port selection, list and categorize all ports
  - **switch_controller_managed_switch_port_bounce.py** (4 tests): POST to bounce a port (1 second duration), POST with different durations (2 seconds, default), POST to start and stop a bounce (5 second bounce interrupted), list safe ports and bounce one

- **Tests: SCTP Filter Test**: Added test for SCTP filter endpoint
  - **sctp-filter**: SCTP filter configuration and CRUD operations

### Fixed

- **Generator: Boolean field types in all templates**: Fixed `.pyi` stub generator to properly type boolean fields across all contexts:
  - **Issue**: Boolean fields (e.g., `stop` in `switch-controller/managed-switch/bounce-port`) were incorrectly typed as `str` instead of `bool`
  - **Root Cause**: Template only checked for `options` (Literal) and `integer` types, defaulting everything else to `str`
  - **Fix**: Added `{% elif field.type == 'boolean' %}` checks before `str` fallback in 11 template locations:
    - TypedDict Payload definitions (for user input construction)
    - TypedDict Response definitions (for API response typing)
    - FortiObject class field definitions (for attribute access)
    - POST method parameter signatures
    - PUT method parameter signatures
    - Nested complex field TypedDicts
    - Nested table field TypedDicts
    - Nested complex field Object classes
    - Nested table field Object classes
  - **Impact**: All boolean fields across all 1064 endpoints now correctly typed as `bool`, enabling proper type checking for values like `True`/`False`
  - **Example**: `fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(stop=True)` now passes type checking (was showing error: "Literal[True] cannot be assigned to parameter of type str | None")
  - **Templates verified**: `endpoint_class.pyi.j2` (all other templates don't generate field-level type annotations)

## [0.5.116] - 2026-01-19

### Added

- **Tests: Rule Endpoint Test Suite**: Added tests for read-only CMDB rule endpoints (reference data):
  - **rule/fmwp**: Show FMWP signatures
  - **rule/iotd**: Show IOT detection signatures
  - **rule/otdt**: Show OT detection signatures
  - **rule/otvp**: Show OT patch signatures
  - All rule endpoints are read-only (GET operations only) and provide reference data for security signatures

### Fixed

- **Generator: Type stubs for read-only endpoints**: Fixed `.pyi` stub generator to respect `readonly` flag:
  - **Issue**: Type stub files (`.pyi`) were generating POST/PUT/DELETE method signatures for read-only endpoints, causing IDE autocomplete to show non-existent methods
  - **Root Cause**: Template `endpoint_class.pyi.j2` only checked `capabilities.crud.{create,update,delete}` flags without checking `schema.readonly` flag
  - **Fix**: Added `not schema.readonly` check to all CRUD method generation in `.pyi` template:
    - Line 505: POST method now requires `{% if not schema.readonly and schema.capabilities.crud.create %}`
    - Line 557: PUT method now requires `{% if not schema.readonly and schema.capabilities.crud.update %}`
    - Line 609: DELETE method now requires `{% if not schema.readonly and schema.capabilities.crud.delete %}`
  - **Impact**: Read-only endpoints (e.g., `rule/fmwp`, `rule/iotd`, system reference tables) no longer show POST/PUT/DELETE in IDE autocomplete
  - **Consistency**: `.pyi` template now matches Python template logic which already had readonly checks for `SUPPORTS_CREATE/UPDATE/DELETE` flags

- **Generator: Boolean field types**: Fixed `.pyi` stub generator to properly type boolean fields:
  - **Issue**: Boolean fields (e.g., `stop` in `switch-controller/managed-switch/bounce-port`) were incorrectly typed as `str` instead of `bool`
  - **Root Cause**: Template only checked for `options` (Literal) and `integer` types, defaulting everything else to `str`
  - **Fix**: Added `{% elif field.type == 'boolean' %}` checks before `str` fallback in 11 template locations:
    - TypedDict Payload definitions (for user input)
    - TypedDict Response definitions (for API responses)
    - FortiObject class definitions (for attribute access)
    - POST/PUT method parameter signatures
    - Nested complex/table field definitions
  - **Impact**: All boolean fields across all endpoints now correctly typed as `bool`, enabling proper type checking for values like `True`/`False`
  - **Example**: `fgt.api.monitor.switch_controller.managed_switch.bounce_port.post(stop=True)` now passes type checking

## [0.5.115] - 2026-01-19

### Added

- **Tests: Comprehensive Router Protocol Test Suite**: Added 163 tests across 12 test files covering all major router endpoints:
  - **router/setting** (9 tests): Singleton endpoint - hostname, kernel-route-distance, boundary values (min 0, max 255), multi-field updates
  - **router/static** (17 tests): IPv4 static routes - distance/weight/priority, blackhole, source prefix, disabled routes, tags, BFD, CRUD operations
  - **router/static6** (17 tests): IPv6 static routes - link-local gateways (fe80::), distance/weight/priority, blackhole, tags, BFD, CRUD operations
  - **router/prefix-list** (14 tests): IPv4 prefix filtering - permit/deny rules, GE/LE prefix matching, multiple rules, CRUD operations
  - **router/prefix-list6** (14 tests): IPv6 prefix filtering - GE/LE matching, CRUD operations
  - **router/policy** (14 tests): IPv4 policy routing - source/destination matching, ports, TOS, input/output devices, deny rules, CRUD operations
  - **router/policy6** (15 tests): IPv6 policy routing - addr6 field, ports, TOS, input/output devices, CRUD operations (known limitation: combining src+dst in same rule causes error)
  - **router/rip** (13 tests): RIPv2 configuration - networks, interfaces with authentication, neighbors, redistribution, timers, distances
  - **router/ripng** (14 tests): RIPng for IPv6 - link-local networks (fe80::/10), aggregate addresses, neighbors, redistribution, timers (key discovery: network field requires link-local IPv6 addresses)
  - **router/route-map** (19 tests): Route map rules - match/set conditions (metric, tag, origin, local-preference, weight), metric-type ("external-type1/2"), multiple rules
  - **router/ospf** (13 tests): OSPF configuration - areas (backbone, stub, NSSA), interfaces, networks, redistribution, graceful restart, timers
  - **router/ospf6** (13 tests): OSPFv3 for IPv6 - areas, stub/NSSA types, IPv6 interfaces, summary addresses, redistribution
  - All tests include comprehensive cleanup functions and dynamic configuration discovery
  - All tests passing in both direct execution and pytest

### Fixed

- **Generator: Complex fields nested in table items**: Fixed code generator to properly handle complex fields nested within table items (e.g., `router.multicast.interface.igmp`):
  - **Type Stubs (.pyi)**: Now generates proper TypedDict for nested complex fields instead of typing them as `str`
    - Before: `igmp: str` ❌
    - After: `igmp: MulticastInterfaceIgmpDict` ✅ (with all nested fields properly typed)
  - **Pydantic Models**: Fixed to generate single object type for complex fields instead of list
    - Before: `igmp: list[MulticastInterfaceIgmp] = Field(default_factory=list, ...)` ❌
    - After: `igmp: MulticastInterfaceIgmp | None = Field(default=None, ...)` ✅
  - **Template Changes**:
    - Updated `endpoint_class.pyi.j2`: Added two-pass generation to create nested TypedDicts before parent types
    - Updated `model_generator.py`: Added category check (`'complex'` vs `'table'`) to determine if field is single object or list
  - **Impact**: Fixes type errors for all endpoints with nested complex fields (e.g., `firewall.profile-protocol-options`, `ssl-ssh-profile`, etc.)

## [0.5.114] - 2026-01-18

### Added

- **Tests: Comprehensive Router Protocol Tests**: Added 11 new tests across 3 files for CMDB router endpoints:
  - **BGP Tests** (`bgp.py` - 7 tests): Complete BGP configuration workflow including AS number, router ID, neighbors (with preservation of existing neighbors), neighbor groups, and neighbor ranges
  - **BFD IPv4 Tests** (`router_bfd.py` - 2 tests): Bidirectional Forwarding Detection for IPv4 with dynamic interface discovery
  - **BFD IPv6 Tests** (`router_bfd6.py` - 2 tests): Bidirectional Forwarding Detection for IPv6 with /128 subnet handling and automatic IP calculation
  - All tests include comprehensive cleanup functions and dynamic configuration discovery
  - Tests validate nested object access patterns and FortiObjectList functionality

### Added

- **Tests: Comprehensive CMDB Endpoint Test Suite**: Added 592 tests across 141 test files covering firewall, router, IPS, logging, and other CMDB endpoints:
  - **Firewall (77 files, 289 tests)**: Complete coverage of addresses, policies, VIPs, schedules, shapers, services, SSL settings, and internet service objects
  - **Log (42 files, 193 tests)**: FortiAnalyzer, syslog, disk, memory, TACACS+, threat weight, and custom field configurations
  - **IPS (8 files, 33 tests)**: Custom signatures, decoders, sensors, rules, and global settings
  - **Router (6 files, 24 tests)**: Access lists (IPv4/IPv6), AS-path lists, auth paths, BFD (IPv4/IPv6), and BGP (7 comprehensive tests)
  - **Other (8 files, 53 tests)**: Endpoint control, file filter, FTP proxy, ICAP profiles/servers, report settings
  - All tests include GET/POST/PUT/DELETE operations with comprehensive cleanup functions
  - Tests validate nested object access, FortiObjectList functionality, and dynamic configuration discovery

### Fixed

- **Runtime: Empty list handling for table fields**: Updated `FortiObject.__getattr__()` to always wrap list-type fields in `FortiObjectList`, even when empty. This ensures the `.dict` property is always available:
  - **Before**: Empty lists returned as plain Python `list`, causing `AttributeError` when accessing `.dict`
  - **After**: Empty lists wrapped in `FortiObjectList([])`, providing consistent `.dict` access
  - **Example**: `config.neighbor_group.dict` now works even when `neighbor_group` is empty
  - Fixes cleanup operations: `fgt.api.cmdb.router.bgp.put(neighbor_group=[])` followed by `.get().neighbor_group.dict`
  
- **Type Stubs: Simplified table field annotations**: Removed `| list` union type since runtime now always returns `FortiObjectList`

- **Documentation: BGP Field Access Issue Identified**: Documented workaround for BGP "as" field - API returns `"as": "65001"` but library attribute access via `.asn` returns `None`. Workaround: use `result.raw.get('results', {}).get('as', '')` until keyword mapping is fixed

- **Documentation: BFD6 Field Name Mismatch**: Identified type stub inconsistency - stubs use `ip6_address` (underscore) but API expects `"ip6-address"` (hyphen) at runtime

## [0.5.113] - 2026-01-18

### Added

- **Type Stubs: Empty list type annotation**: Initial attempt to handle empty lists by adding `| list` union type (superseded by runtime fix in v0.5.114)

## [0.5.112] - 2026-01-18

### Added

- **Type Checking: Full type inference for table/list field items**: Generated typed object classes for all table field items to enable complete type checking support in IDEs. Each table item now has explicit property definitions for all fields:
  - **Example**: `BgpNeighborItemObject` class with typed properties (`ip: str`, `remote_as: str`, etc.)
  - **Before**: `neighbor.ip` showed as `Unknown` in Pylance (worked at runtime but no type checking)
  - **After**: `neighbor.ip` shows as `str` with full autocomplete and type validation
  - Applies to all 1000+ endpoints with table/list fields (firewall policies, BGP neighbors, addresses, etc.)
  - Type inference now works for: `for item in config.field: print(item.property)`
  - Compatible with all access patterns: attribute access, dict access, and list .dict property

- **Type Checking: Enhanced FortiObject generic typing**: Updated `FortiObject.dict` property to return the generic type parameter instead of `dict[str, Any]`:
  - Enables typed dict access: `neighbor.dict` returns `BgpNeighborItem` (TypedDict)
  - Supports both runtime convenience and static type checking

### Changed

- **Generator: Template updated to generate ItemObject classes**: Modified `endpoint_class.pyi.j2` template to generate both TypedDict definitions (for dict-style access) and Object classes (for attribute access) for all table fields
  - Field type changed from `FortiObjectList[FortiObject[TypedDict]]` to `FortiObjectList[ItemObject]`
  - ItemObject classes inherit from `FortiObject[TypedDict]` and define all properties explicitly

### Fixed

- **Type Stubs: Added `__getitem__` method to FortiObject stub**: Previously intentionally omitted, now added to support both attribute and dict-style access patterns in type checking

## [0.5.111] - 2026-01-18

### Fixed

- **API Responses: Reverse keyword mapping for Python keyword fields**: Added bidirectional keyword mapping to support API responses containing Python keyword fields. The `FortiObject` class now correctly maps API keyword fields to safe Python attribute names when receiving responses:
  - **Inbound (NEW)**: API `{"as": "65001"}` → Python `result.asn` returns `"65001"`
  - **Outbound (v0.5.110)**: Python `asn="65000"` → API `{"as": "65000"}`
  - Fixes: `result.asn` now works correctly for BGP configurations, `class_` for RADIUS, `type_` for firewall pools
  - Updated `FortiObject.__getattr__()` and `FortiObject.get_full()` methods
  - Completes the keyword handling feature from v0.5.110 with full bidirectional support

## [0.5.110] - 2026-01-18

### Fixed

- **API Field Names: Python keyword conflict resolution**: Added automatic mapping for Python keywords that were renamed to avoid conflicts. The payload builders now correctly convert these renamed parameters back to their original API field names:
  - **BGP AS number**: `asn="65000"` → `{"as": "65000"}` (was incorrectly sent as `"asn"`)
  - **RADIUS class field**: `class_=[{"name": "test"}]` → `{"class": [{"name": "test"}]}` (was sent as `"class-"`)
  - **Firewall type field**: `type_="overload"` → `{"type": "overload"}` (was sent as `"type-"`)
  - **Other keywords**: `from_` → `"from"`, `import_` → `"import"`, `global_` → `"global"`
  - Generator uses trailing underscores (`class_`, `type_`) or alternate names (`asn`) to avoid Python syntax errors
  - Updated `build_cmdb_payload()`, `build_cmdb_payload_normalized()`, and `build_api_payload()` functions
  - Fixes: BGP configuration, RADIUS class attributes, firewall IP pools, and all other keyword-conflicted fields

## [0.5.109] - 2026-01-18

### Fixed

- **API Field Names: Automatic conversion from snake_case to hyphenated format**: Added automatic field name conversion in `POST` and `PUT` requests to convert Python's snake_case field names (e.g., `ip6_address`) to FortiOS API's hyphenated format (e.g., `ip6-address`). This allows using Pythonic field names while maintaining API compatibility:
  - **Before**: Required using hyphenated names: `{"ip6-address": "2001:db8::1"}` (causes Pylance errors)
  - **After**: Use Python conventions: `{"ip6_address": "2001:db8::1"}` (auto-converted to `ip6-address`)
  - Recursive conversion handles nested objects and lists
  - IDE autocomplete now works perfectly with no typing errors
  - Example: `fgt.api.cmdb.router.bfd6.put(neighbor=[{"ip6_address": "::1", "interface": "port1"}])`

## [0.5.108] - 2026-01-18

### Fixed

- **Runtime: Nested object fields now return FortiObject instances**: Updated `FortiObject.__getattr__()` to automatically wrap nested dict fields in `FortiObject` instances. This completes the nested object attribute access feature started in v0.5.107:
  - **Before**: `intf.ipv6` returned plain dict (AttributeError on `intf.ipv6.ip6_address`)
  - **After**: `intf.ipv6` returns `FortiObject` (enables `intf.ipv6.ip6_address` at runtime)
  - Works for all nested configuration objects: `ipv6`, `http`, `smtp`, `ftp`, etc.
  - Both IDE autocomplete (v0.5.107 type stubs) and runtime behavior now fully support attribute access

## [0.5.107] - 2026-01-18

### Fixed

- **Type Stubs: Nested object fields now support attribute access**: Changed nested complex field types (like `ipv6`, `http`, `smtp`, etc.) from `TypedDict` to `FortiObject` subclasses in .pyi stub files. This enables full attribute access with autocomplete for nested configuration objects:
  - **Before**: `intf.ipv6["ip6_address"]` (dict access only, no autocomplete)
  - **After**: `intf.ipv6.ip6_address` (attribute access with full IDE autocomplete!)
  - IDE now provides autocomplete, type validation, and Literal value checking for all nested object fields
  - Affects fields like: `ipv6` in system/interface, `http`/`ftp`/`smtp` in profile-protocol-options, and many others
- **Example**: `intf.ipv6.ip6_mode` now shows autocomplete for Literal values: "static", "dhcp", "pppoe", "delegated"

## [0.5.106] - 2026-01-18

### Fixed

- **Type Stubs: Table field items now use TypedDict for IDE validation**: Changed table field nested item types from plain classes to TypedDict in .pyi stub files. This enables full IDE type checking and autocomplete for nested table fields (like `rule` in access-list, `srcintf` in policies, etc.). IDE now validates:
  - Dictionary keys (catches typos and unknown fields)
  - Literal values (shows errors for invalid enum values)
  - Required fields (highlights missing required fields)
- **Type Stubs: Removed untyped dict from table field signatures**: Removed `list[dict[str, Any]]` from table field type signatures in .pyi files to force strict type checking. Table fields now only accept:
  - `str` (for single-value auto-normalization)
  - `list[str]` (for multi-value auto-normalization)
  - `list[TypedDictItem]` (for full IDE validation)
- **Example**: Before this fix, `rule=[{"action": "accept", "typo": "value"}]` would pass type checking. After this fix, IDE shows errors for invalid Literal values and unknown fields.

## [0.5.105] - 2026-01-18

### Fixed

- **Generator: Plus symbol (+) naming convention**: Fixed generator to correctly convert plus symbols in API paths to `_plus_` with underscore separators on both sides. Now `tacacs+accounting` → `tacacs_plus_accounting` (not `tacacs_plusaccounting`). This affects:
  - **Path-to-module conversion**: `log.tacacs+accounting` → `log/tacacs_plus_accounting/` directory structure
  - **Class names**: `TacacsPlusAccounting` (PascalCase with underscore preserved)
  - **Attribute names**: `fgt.api.cmdb.log.tacacs_plus_accounting` (snake_case with underscore separator)
  - **All generated code**: Endpoint files, stubs (.pyi), helpers, models, and __init__.py files
- **Affected endpoints**: `log.tacacs+accounting`, `log.tacacs+accounting2`, `log.tacacs+accounting3`, `user.tacacs+` now all use correct naming convention
- **Generator components updated**: 
  - `utils/naming.py`: `kebab_to_snake()` function
  - `schema_management/schema_parser.py`: `file_name`, `class_name`, `normalize_path()` methods
  - `generators/model_generator.py`: Endpoint path and field name conversions

## [0.5.104] - 2026-01-18

### Fixed

- **Schema: Read-only flag now included for all endpoints**: Updated schema files to include the `readonly` flag for all read-only reference data endpoints (e.g., `ips/decoder`, internet services, geographic data). The schema generator now properly extracts and preserves the `readonly: true` flag from FortiOS API responses.
- **Generator: Read-only endpoints no longer generate mutation methods**: Fixed endpoint generator to check `schema.readonly` flag and skip generating POST/PUT/DELETE/move/clone methods for read-only endpoints. Capabilities flags (SUPPORTS_CREATE, SUPPORTS_UPDATE, SUPPORTS_DELETE, SUPPORTS_MOVE, SUPPORTS_CLONE) are now correctly set to False for read-only endpoints, regardless of what the schema capabilities section contains.

## [0.5.103] - 2026-01-18

### Changed

- **Version bump**: Released v0.5.103 to PyPI.

## [0.5.102] - 2026-01-18

### Changed

- **Generator: Literal type extraction from parameter descriptions**: The endpoint generator now automatically extracts enumerated values from parameter descriptions in schema files and generates proper `Literal` type hints. When a parameter description contains options in the format `[option1 | option2 | option3]`, the generator creates `Literal["option1", "option2", "option3"]` types for both `.py` implementations and `.pyi` stub files, providing IDE autocomplete and type checking for valid parameter values.

### Fixed

- **Generator: Strip leading asterisks from parameter option values**: Fixed schema parser to remove asterisks (`*`) from both the beginning and end of parameter option values when extracting Literal types from descriptions. Previously, options like `[*vdom|global]` would generate `Literal["*vdom", "global"]` instead of the correct `Literal["vdom", "global"]`. Examples affected: `scope` parameter in `monitor.network.lldp.ports`, `ip_version` parameter in `monitor.router.bgp.neighbors_statistics`.

### Tests

- **85 new Monitor API endpoint tests** across 8 test files covering comprehensive monitoring functionality:
  - **router.py** (50 tests): Routing tables (IPv4/IPv6), BGP (neighbors, paths, statistics, soft reset), OSPF neighbors, SD-WAN routes, route lookup (IPv4/IPv6, policy routes), policy routes
  - **network.py** (13 tests): ARP table, LLDP (neighbors, ports with VDOM/global scope), DNS latency, DDNS (servers, lookup), reverse IP lookup, debug flow trace
  - **registration.py** (3 tests): FortiCloud status, FortiCare account, FortiCare resellers
  - **license.py** (4 tests): License status, FortiAnalyzer license, FortiCare organization list, FortiCare resellers
  - **ips.py** (5 tests): Rate-based statistics, metadata, anomaly detection, hold signatures, session performance
  - **fortiview.py** (3 tests): Realtime statistics, historical statistics, realtime proxy statistics
  - **fortiguard.py** (4 tests): Redirect portal, service communication statistics (with filtering), answers endpoint
  - **firmware.py** (3 tests): Extension device firmware info for FortiSwitch, FortiAP, FortiExtender
- **Test quality improvements**: All tests include proper exception handling for 404/424/500 errors, use realistic test data (google.dk, 8.8.8.8, port3/port4), and document disabled tests with reasons

## [0.5.101] - 2026-01-18

### Changed

- **BREAKING: FortiObject property renaming**: Renamed FortiGate-specific metadata properties with `fgt_` prefix to clearly distinguish API metadata from object fields and prevent naming conflicts:
  - `vdom` → `fgt_vdom` - FortiGate virtual domain name
  - `mkey` → `fgt_mkey` - FortiGate primary key of created/modified object
  - `revision` → `fgt_revision` - Configuration revision number
  - `serial` → `fgt_serial` - Device serial number
  - `version` → `fgt_version` - FortiOS version string
  - `build` → `fgt_build` - FortiOS firmware build number
- **New properties**:
  - `fgt_revision_changed` - Boolean flag indicating whether config was modified
  - `fgt_old_revision` - Previous configuration revision number (before this change)
  - `fgt_api_path` - API path segment (e.g., 'firewall', 'system', 'user')
  - `fgt_api_name` - API endpoint name (e.g., 'address', 'policy', 'interface')
  - `fgt_response_size` - Number of objects returned in the response (for list operations)
  - `fgt_action` - API action performed (appears in some response types)
  - `fgt_limit_reached` - Boolean indicating pagination limit was reached
  - `fgt_matched_count` - Number of objects matching the query criteria
  - `fgt_next_idx` - Index for the next page in paginated results
- **Rationale**: The `fgt_` prefix makes it immediately clear these are FortiGate API metadata properties, not fields from the actual FortiOS object being managed. This prevents potential conflicts when object schemas include fields like "version", "serial", "name", "path", "size", etc.

### Fixed

- **HTTP Client: Missing http_status in API responses**: Fixed issue where `FortiObject.http_status_code` returned `None` because FortiOS API responses don't always include the HTTP status code in the JSON body. The HTTP client now injects `http_status` from the actual HTTP response (`response.status_code`) if not present in the JSON response.
- **Impact**: `result.http_status_code` now correctly returns HTTP status codes (200, 404, 500, etc.) for all endpoints, and `result.http_stats` includes accurate status code information.
- **Affected code**: Both sync (`hfortix_core.http.client`) and async (`hfortix_core.http.async_client`) HTTP clients updated.

### Tests

- **Test file fixes**: Corrected validator function name checks in `system.global` and `web_proxy.global` test files (changed from double underscore `validate_*__post` to single underscore `validate_*_post` to match actual generated function names).

## [0.5.100] - 2026-01-17

### Tests

- **45 new CMDB endpoint test files** covering comprehensive firewall configuration testing:
  - **Address & Address Groups**: `firewall_address.py` (6 tests), `firewall_address6.py` (6 tests), `firewall_addrgrp.py` (6 tests), `firewall_addrgrp6.py` (6 tests)
  - **Internet Services**: `firewall_internet_service.py` (1 test, GET-only), `firewall_internet_service_addition.py` (6 tests), `firewall_internet_service_custom.py` (6 tests), `firewall_internet_service_custom_group.py` (6 tests), `firewall_internet_service_definition.py` (1 test, GET-only), `firewall_internet_service_extension.py` (1 test, GET-only), `firewall_internet_service_fortiguard.py` (1 test, GET-only), `firewall_internet_service_group.py` (6 tests), `firewall_internet_service_list.py` (1 test, GET-only), `firewall_internet_service_name.py` (6 tests)
  - **IP Pools & NAT**: `firewall_ip_translation.py` (6 tests), `firewall_ippool.py` (6 tests), `firewall_ippool6.py` (6 tests)
  - **Load Balancing**: `firewall_ldb_monitor.py` (6 tests)
  - **Local-In Policies**: `firewall_local_in_policy.py` (6 tests), `firewall_local_in_policy6.py` (6 tests)
  - **Multicast**: `firewall_multicast_address.py` (6 tests), `firewall_multicast_address6.py` (6 tests), `firewall_multicast_policy.py` (6 tests), `firewall_multicast_policy6.py` (6 tests)
  - **Network Services**: `firewall_network_service_dynamic.py` (1 test, GET-only)
  - **Packet Sniffers**: `firewall_on_demand_sniffer.py` (6 tests), `firewall_sniffer.py` (1 test, GET-only)
  - **Policies**: `firewall_policy.py` (9 tests), `firewall_policy6.py` (9 tests), `firewall_proxy_policy.py` (9 tests), `firewall_shaping_policy.py` (6 tests)
  - **Security Profiles**: `firewall_profile_group.py` (6 tests), `firewall_profile_protocol_options.py` (6 tests), `firewall_ssl_ssh_profile.py` (6 tests)
  - **Proxy Objects**: `firewall_proxy_address.py` (6 tests), `firewall_proxy_addrgrp.py` (6 tests)
  - **Geographic & Reference Data**: `firewall_region.py` (1 test, GET-only), `firewall_vendor_mac.py` (1 test, GET-only), `firewall_vendor_mac_summary.py` (1 test, GET-only)
  - **Traffic Shaping**: `firewall_shaping_profile.py` (1 test, GET-only)
  - **SSL/TLS**: `firewall_ssl_server.py` (6 tests)
  - **Virtual IPs**: `firewall_vip.py` (6 tests), `firewall_vip6.py` (6 tests), `firewall_vipgrp.py` (6 tests), `firewall_vipgrp6.py` (6 tests)



### Changed

- **Generator: Readonly endpoint detection**: Updated endpoint generator to detect readonly reference data endpoints (marked with `"readonly": true` in schema) and only generate GET methods. Prevents generation of POST/PUT/DELETE methods for endpoints that provide read-only FortiGuard-managed data.
- **38 readonly endpoints updated**: Internet service variants, geographic data, IPS signatures, vendor MAC addresses, system replacement messages, and timezone data endpoints now only expose `get()` and `get_schema()` methods.

### Added

- **Generator: Complex field TypedDict support**: Added full support for complex nested object fields (schema `category="complex"` with `children`). Generator now creates dedicated TypedDict classes for nested objects, enabling proper type checking and IDE autocomplete for complex configurations.
- **Complex field examples**: Endpoints like `firewall.profile-protocol-options` with nested fields (`http`, `ftp`, `smtp`, etc.) now have full type safety:
  ```python
  # Before: complex fields were simple strings - type errors when passing dicts
  http: str | None = ...  # ❌
  
  # After: proper TypedDict with nested field validation
  http: ProfileProtocolOptionsHttpDict | None = ...  # ✅
  class ProfileProtocolOptionsHttpDict(TypedDict, total=False):
      ports: int | list[int]
      status: Literal["enable", "disable"]
      inspect_all: Literal["enable", "disable"]
      # ... all nested fields with proper types
  ```
- **Documentation: READONLY_ENDPOINTS.md**: New documentation listing all 38 readonly endpoints with descriptions, primary keys, and usage examples. Located at `docs/fortios/READONLY_ENDPOINTS.md`.
- **Readonly endpoint categories**:
  - **Internet Services**: internet-service, internet-service-botnet, internet-service-custom, internet-service-custom-group, internet-service-extension, internet-service-group, internet-service-list, internet-service-name, internet-service-negate, internet-service-owner, internet-service-reputation, internet-service-sld
  - **Geographic Data**: country, city, region, geoip-country
  - **IPS Data**: decoder, rule, rule-settings, view-map
  - **System Data**: vendor-mac, replacement-message groups, timezone
  - **Application Data**: application categories and lists

### Technical Details

- Modified `endpoint_generator.py` `_extract_http_methods()` to check `schema.readonly` flag and return `['GET']` for readonly endpoints
- Updated `endpoint_class.pyi.j2` template to handle `category == 'complex'` fields:
  - Generate TypedDict classes for complex nested objects (not just table lists)
  - Updated Payload, Response, and Object type sections to use complex field TypedDicts
  - Updated POST, PUT, SET method parameters to accept complex TypedDict types
- Created `scripts/generate_readonly_list.py` to scan schema files and generate readonly endpoint documentation
- Readonly endpoints now include special documentation header explaining read-only nature and unsupported operations

## [0.5.99] - 2026-01-17

### Fixed

- **Generator: Unitary field auto-normalize conflict**: Fixed bug where fields like `interface` in `firewall.DoS-policy` were incorrectly auto-normalized to list format `[{"name": "..."}]` when they should remain as simple strings. The generator now detects unitary fields that conflict with `COMMON_LIST_FIELDS` and sets `auto_normalize=False` in `build_api_payload()` calls.
- **Affected endpoints**: `firewall/DoS_policy`, `firewall/DoS_policy6`, `firewall/interface_policy`, and ~20 other endpoints with unitary `interface`, `srcintf`, `dstintf`, or `member` fields that were being incorrectly converted.

### Technical Details

- Added `get_unitary_list_field_conflicts()` function to `schema_parser.py` to detect schema fields that are in `COMMON_LIST_FIELDS` but have `category="unitary"`
- Updated `endpoint_generator.py` to pass `has_unitary_list_conflicts` flag to template context
- Modified `endpoint_class.py.j2` template to conditionally set `auto_normalize=False` with explanatory comment when conflicts exist

## [0.5.98] - 2025-05-23

### Fixed

- **Stub generator `status` field**: Removed `status` from `reserved_fields` list - base class has `http_status` (for API response status), but `status` (enable/disable) is a valid object field that should be generated in child class stubs
- **Stub template multi-value option fields**: Fixed `endpoint_class.pyi.j2` template for fields with `options` + `is_list=True` (e.g., `firewall.schedule/recurring.day`). FortiOS returns space-separated strings like `"monday tuesday wednesday"`, not lists. Response/Object types now use `str`, Payload accepts `str | list[str]` for convenience
- **Stub method parameters for multi-value fields**: Fixed `post()`, `put()`, and `set()` method signatures in `.pyi` stubs to use `str | list[str]` instead of `Literal[...] | list[str]` for space-separated multi-value option fields

### Added

- **`normalize_day_field()` helper**: New normalizer in `_helpers/normalizers.py` for schedule day fields. Accepts `str`, `list[str]`, or comma-separated string and normalizes to space-separated format for FortiOS API. Includes validation of day names.
- **Generator: auto-normalize multi-value option fields**: Added `extract_multivalue_option_fields()` to schema parser and integrated into `endpoint_class.py.j2` template. Endpoints with `day` fields (like `firewall.schedule/recurring`) now automatically normalize input via `normalize_day_field()` in `post()`, `put()`, and `set()` methods.

### Tests

- **53 new CMDB endpoint tests** covering 11 firewall-related endpoints:
  | File | Tests | Endpoint |
  |------|-------|----------|
  | `firewall_ipmacbinding.py` | 3 | `firewall.ipmacbinding/setting` |
  | `firewall_ipmacbinding_table.py` | 5 | `firewall.ipmacbinding/table` |
  | `firewall_schedule_group.py` | 5 | `firewall.schedule/group` |
  | `firewall_schedule_onetime.py` | 5 | `firewall.schedule/onetime` |
  | `firewall_schedule_recurring.py` | 5 | `firewall.schedule/recurring` |
  | `firewall_service_category.py` | 5 | `firewall.service/category` |
  | `firewall_service_custom.py` | 5 | `firewall.service/custom` |
  | `firewall_service_group.py` | 5 | `firewall.service/group` |
  | `firewall_shaper_per_ip_shaper.py` | 5 | `firewall.shaper/per-ip-shaper` |
  | `firewall_shaper_traffic_shaper.py` | 5 | `firewall.shaper/traffic-shaper` |
  | `filefilter.py` | 5 | `file-filter/profile` |

### Improved

- **Test infrastructure**: Dynamic xdist grouping using `Path(__file__).stem`
- **Deletion verification**: Cleaner pattern using get-all + check not in list

## [0.5.97] - 2026-01-17

### Fixed - **Pydantic Model Generator & Stub Type Fixes**

#### Pydantic Model Generator Fixes (`generators/model_generator.py`)
- ✅ **Duplicate enum members**: Schema may contain duplicate enum options - generator now deduplicates while preserving order
- ✅ **String defaults for int fields**: Fields typed as `int` but with string defaults like `"unspecified"` now use `None` instead
- ✅ **Type tracking**: Added `python_type` to field_info for proper type checking during default value generation

#### Core Stubs (`models.pyi`)
- ✅ **`dict` shadowing fix**: Added `import builtins` and use `builtins.dict` for `raw` property return types
- ✅ **Overload implementations removed**: Removed non-stub implementation signatures from `process_response` and `__getitem__`
- ✅ **`__getitem__` signature**: Use `SupportsIndex` parameter to match base `list` class signature

#### Stub Template (`endpoint_class.pyi.j2`)
- ✅ **Reserved field names**: Skip generating fields that conflict with `FortiObject` base class properties (`vdom`, `serial`, `version`, `revision`, `status`, `list`, etc.)
- ✅ **`__init__` method**: Added missing `__init__(self, client: Any) -> None` to all generated endpoint class stubs

#### Other Stub Fixes
- ✅ **`api/utils.pyi`**: Removed obsolete `FortiOSDictMode`, `FortiOSObjectMode` imports (classes were removed in previous version)
- ✅ **`fmg_proxy/client.pyi`**: Use `TypeAlias` for `FMGSession` type alias
- ✅ **`monitor/system/time/__init__.pyi`**: Renamed `set` to `set_` to avoid conflict with inherited `set()` method
- ✅ **`performance_test.py`**: Added type ignore for `asyncio.gather` call

#### Test Generator & Pydantic Model Enum Formatting
- ✅ **Test generator global-scope fix**: Tests no longer generate `auto_test_get_with_vdom` for global-scope endpoints that don't support `vdom` parameter
- ✅ **Pydantic model enum fix**: Fixed template to generate enum values on separate lines instead of single line (was causing syntax errors)
- ✅ **All tests regenerated**: 1066 test files regenerated with global-scope awareness

### Added

- 📄 **ENDPOINT_SCOPE_REFERENCE.md**: New documentation listing all global-only, read-only, and combined endpoints

### Improved

- 🎯 **IDE Autocompletion**: Significantly improved Pylance/mypy type inference for all endpoint classes
  - All endpoint stubs now have proper `__init__` signatures
  - Reserved field names no longer conflict with `FortiObject` base class
  - Clean type checking with zero mypy errors across 3465 source files

### Result
- **All 1062 endpoints regenerated**
- **mypy passes**: `Success: no issues found in 3465 source files`
- **Pylance**: No more `Expected 0 positional arguments` errors on `super().__init__(client)`

## [0.5.96] - 2026-01-17

### Fixed - **Regenerated All Endpoints with Integer Parameter Types**

- ✅ **Full regeneration**: All monitor/service endpoints regenerated with correct integer query parameter types
- ✅ **config_revision.info.get()**: Now accepts `config_id: int` instead of `str`
- ✅ **All integer params fixed**: Any endpoint with integer query parameters now has correct types in stubs

## [0.5.95] - 2026-01-17

### Fixed - **ContentResponse Stub & Query Parameter Types**

- ✅ **ContentResponse return type**: Generator now uses `CONTENT_ENDPOINTS` registry to return `ContentResponse` instead of `FortiObject` for file/download endpoints
- ✅ **Query parameter types**: Fixed stub generation to use correct types (`int` vs `str`) based on schema `type` field
- ✅ **config_id parameter**: `config_revision.file.get(config_id=45)` now accepts `int` instead of requiring `str`

**Fixed Pylance errors:**
```python
# Before: Pylance error - expected str, got int
result = fgt.api.monitor.system.config_revision.file.get(config_id=45)  # ❌

# After: Works correctly with int
result = fgt.api.monitor.system.config_revision.file.get(config_id=45)  # ✅
result.content  # ✅ bytes - autocomplete works
result.text     # ✅ str - autocomplete works
```

## [0.5.94] - 2026-01-17

### Added - **ContentResponse for Binary/File Download Endpoints**

- ✅ **New `ContentResponse` class**: Wraps responses from endpoints that return binary/text content (config files, certificates, logs, etc.)
- ✅ **Consistent API**: Same properties as `FortiObject` (`.http_status_code`, `.vdom`, `.raw`, etc.) plus content-specific properties
- ✅ **Content properties**: `.content` (bytes), `.content_type` (MIME type), `.text` (decoded string)
- ✅ **Convenience methods**: `.to_text()`, `.to_dict()`, `.to_json()`, `.save(path)`
- ✅ **FortiOS config parser**: `parse_fortios_config()` function parses FortiOS config format to nested dict
- ✅ **Endpoint registry**: `CONTENT_ENDPOINTS` dict to track which endpoints return content (add as discovered)

**New exports from `hfortix_fortios`:**
- `ContentResponse` - Response class for content endpoints
- `CONTENT_ENDPOINTS` - Registry of content-returning endpoints
- `is_content_endpoint(path)` - Check if endpoint returns content
- `parse_fortios_config(text)` - Parse FortiOS config to dict

**Example usage:**
```python
# Download config revision
result = fgt.api.monitor.system.config_revision.file.get(config_id=45)

# Access content
result.content       # Raw bytes
result.text          # As UTF-8 string
result.content_type  # 'text/plain'

# Standard API fields still available
result.http_status_code  # 200
result.vdom              # 'root'
result.raw               # Full API envelope

# Parse FortiOS config format
config = result.to_dict()
config['system global']['hostname']  # 'my-firewall'

# Save to file
result.save('/tmp/backup.conf')
```

## [0.5.93] - 2026-01-17

### Fixed - **Generator: Remove `vdom` Parameter from Global-Only Endpoints**

- ✅ **Improved API ergonomics**: Global-only endpoints no longer expose confusing `vdom` parameter to users
- ✅ **Schema parsing updated**: Added `scope`, `scope_options`, and `is_global_only` properties to `EndpointSchema`
- ✅ **Template conditionals**: `.py` and `.pyi` templates conditionally exclude `vdom` parameter based on `is_global_only`
- ✅ **Internal handling**: Global-only endpoints internally pass `vdom=False` to HTTP client (skips sending vdom param)
- ✅ **V1.7 schema support**: Fixed `_parse_v1_7()` function to extract and pass scope/scope_options

### Global-Only Endpoints (147 total)

These endpoints operate at global scope only and no longer accept a `vdom` parameter:

<details>
<summary><strong>Certificate (5)</strong></summary>

- `certificate.ca`
- `certificate.crl`
- `certificate.hsm-local`
- `certificate.local`
- `certificate.remote`
</details>

<details>
<summary><strong>Endpoint Control (1)</strong></summary>

- `endpoint-control.fctems`
</details>

<details>
<summary><strong>Firewall (16)</strong></summary>

- `firewall.city`
- `firewall.country`
- `firewall.global`
- `firewall.internet-service`
- `firewall.internet-service-addition`
- `firewall.internet-service-append`
- `firewall.internet-service-botnet`
- `firewall.internet-service-definition`
- `firewall.internet-service-fortiguard`
- `firewall.internet-service-ipbl-reason`
- `firewall.internet-service-ipbl-vendor`
- `firewall.internet-service-list`
- `firewall.internet-service-owner`
- `firewall.internet-service-reputation`
- `firewall.internet-service-sld`
- `firewall.internet-service-subapp`
- `firewall.region`
- `firewall.ssl.setting`
- `firewall.vendor-mac`
- `firewall.vendor-mac-summary`
</details>

<details>
<summary><strong>IPS (3)</strong></summary>

- `ips.decoder`
- `ips.global`
- `ips.rule`
</details>

<details>
<summary><strong>Log (24)</strong></summary>

- `log.fortianalyzer.filter`
- `log.fortianalyzer.setting`
- `log.fortianalyzer-cloud.filter`
- `log.fortianalyzer-cloud.setting`
- `log.fortianalyzer2.filter`
- `log.fortianalyzer2.setting`
- `log.fortianalyzer3.filter`
- `log.fortianalyzer3.setting`
- `log.fortiguard.filter`
- `log.fortiguard.setting`
- `log.memory.global-setting`
- `log.syslogd.filter`
- `log.syslogd.setting`
- `log.syslogd2.filter`
- `log.syslogd2.setting`
- `log.syslogd3.filter`
- `log.syslogd3.setting`
- `log.syslogd4.filter`
- `log.syslogd4.setting`
- `log.webtrends.filter`
- `log.webtrends.setting`
</details>

<details>
<summary><strong>Rule (4)</strong></summary>

- `rule.fmwp`
- `rule.iotd`
- `rule.otdt`
- `rule.otvp`
</details>

<details>
<summary><strong>System (72)</strong></summary>

- `system.accprofile`
- `system.acme`
- `system.affinity-interrupt`
- `system.affinity-packet-redistribution`
- `system.alias`
- `system.auto-install`
- `system.auto-script`
- `system.automation-action`
- `system.automation-condition`
- `system.automation-destination`
- `system.automation-stitch`
- `system.automation-trigger`
- `system.autoupdate.schedule`
- `system.central-management`
- `system.cloud-service`
- `system.console`
- `system.csf`
- `system.custom-language`
- `system.ddns`
- `system.dedicated-mgmt`
- `system.device-upgrade-exemptions`
- `system.dns`
- `system.dscp-based-priority`
- `system.email-server`
- `system.fabric-vpn`
- `system.federated-upgrade`
- `system.fips-cc`
- `system.fortiguard`
- `system.fortisandbox`
- `system.fsso-polling`
- `system.ftm-push`
- `system.geoip-country`
- `system.geoip-override`
- `system.global`
- `system.ha`
- `system.ha-monitor`
- `system.health-check-fortiguard`
- `system.ike`
- `system.ipam`
- `system.ips-urlfilter-dns`
- `system.ips-urlfilter-dns6`
- `system.netflow`
- `system.ntp`
- `system.password-policy`
- `system.password-policy-guest-admin`
- `system.probe-response`
- `system.ptp`
- `system.replacemsg-image`
- `system.replacemsg.admin`
- `system.replacemsg.alertmail`
- `system.replacemsg.auth`
- `system.replacemsg.automation`
- `system.replacemsg.fortiguard-wf`
- `system.replacemsg.http`
- `system.replacemsg.mail`
- `system.replacemsg.nac-quar`
- `system.replacemsg.spam`
- `system.replacemsg.sslvpn`
- `system.replacemsg.traffic-quota`
- `system.replacemsg.utm`
- `system.resource-limits`
- `system.saml`
- `system.sdn-connector`
- `system.sdn-proxy`
- `system.sdn-vpn`
- `system.security-rating.controls`
- `system.security-rating.settings`
- `system.session-helper`
- `system.sflow`
- `system.sms-server`
- `system.snmp.community`
- `system.snmp.mib-view`
- `system.snmp.rmon-stat`
- `system.snmp.sysinfo`
- `system.snmp.user`
- `system.sov-sase`
- `system.speed-test-setting`
- `system.ssh-config`
- `system.standalone-cluster`
- `system.storage`
- `system.timezone`
- `system.tos-based-priority`
- `system.vdom`
- `system.vdom-exception`
- `system.vdom-link`
- `system.vdom-property`
- `system.vdom-radius-server`
</details>

<details>
<summary><strong>Other (22)</strong></summary>

- `application.name`
- `automation.setting`
- `dlp.settings`
- `emailfilter.fortishield`
- `emailfilter.options`
- `switch-controller.system`
- `waf.main-class`
- `waf.signature`
- `webfilter.fortiguard`
- `webfilter.ips-urlfilter-cache-setting`
- `wireless-controller.global`
- `wireless-controller.inter-controller`
- `wireless-controller.timers`
</details>

### Example

```python
# Before: Global-only endpoints showed confusing vdom parameter
fgt.api.cmdb.system.global.get(vdom="root")  # vdom was ignored anyway!

# After: Clean API without vdom parameter
fgt.api.cmdb.system.global.get()  # ✅ No vdom parameter

# VDOM-scoped endpoints still have vdom parameter
fgt.api.cmdb.firewall.policy.get(vdom="engineering")  # ✅ vdom works here
```

---

## [0.5.90] - 2026-01-16

### Fixed - **Generator: Invalid LOG Module File Names**

- ✅ **Fixed LOG module syntax error**: Removed incorrectly generated `FortiOS 7.py` and `FortiOS 7.pyi` files with spaces in names
- ✅ **Regenerated LOG endpoints**: All log endpoints regenerated from correct schema files (disk, memory, fortianalyzer, forticloud, search)
- ✅ **Import error resolved**: `SyntaxError: invalid syntax` from `from .FortiOS 7 import Fortios 7` now fixed
- ✅ **Schema source corrected**: LOG generator now correctly uses `schema/7.6.5/log/` instead of swagger files with spaces in names

### Fixed - **Stub Types: Accept `list[str]` for Table Fields**

- ✅ **Pylance errors resolved**: Table field parameters now accept `list[str]` in addition to `list[TypedDict]`
- ✅ **Flexible input support**: Parameters like `member`, `srcintf`, `entries` now accept all formats:
  - Single string: `"value"`
  - List of strings: `["val1", "val2"]` ← **NEW: No longer causes Pylance error**
  - List of dicts: `[{"name": "val1"}]` ← Still works with autocomplete
- ✅ **Template fix**: Updated `endpoint_class.pyi.j2` to generate `str | list[str] | list[TypedDictItem]` union types
- ✅ **All 1062 endpoints regenerated**: Every stub file updated with the fix

### Example

```python
# Before (Pylance error: list[str] not assignable to list[GroupMemberItem])
fgt.api.cmdb.firewall.service.group.post(
    name="my_group",
    member=["HTTP", "HTTPS"]  # ❌ Error
)

# After (works correctly)
fgt.api.cmdb.firewall.service.group.post(
    name="my_group", 
    member=["HTTP", "HTTPS"]  # ✅ No error
)

# Dict format still works with autocomplete
fgt.api.cmdb.firewall.service.group.post(
    name="my_group",
    member=[{"name": "HTTP"}]  # ✅ Autocomplete shows 'name' field
)
```

---

## [0.5.89] - 2026-01-16

### Fixed - **Generator: Response Properties on Nested Child Objects**

- ✅ **Added missing response properties to nested child objects**: All nested table field object stubs now include `http_status_code`, `http_method`, and `http_response_time`
- ✅ **Pylance support for nested objects**: Properties like `policy.srcintf[0].http_status_code` now recognized
- ✅ **Template fix**: Updated `endpoint_class.pyi.j2` to add response properties to nested child object classes (e.g., `PolicySrcintfObject`, `AddressTaggingObject`)
- ✅ **Consistency**: Both main endpoint objects and nested child objects now have identical response property signatures

### Added - **New Fully Tested Endpoints**

**Service API** (12 tests total):
- ✅ **`service/security_rating.py`** - 4 tests for security rating recommendations and reports
- ✅ **`service/system.py`** - 2 tests for fabric admin lockout and time sync checks

**Monitor API** (4 tests total):
- ✅ **`monitor/casb.py`** - 1 test for CASB SaaS application monitoring
- ✅ **`monitor/firewall_policy.py`** - 3 tests for firewall policy monitoring and hit count

**CMDB Email Filter** (36 tests total):
- ✅ **`cmdb/emailfilter/block_allow_list.py`** - Block/allow list management
- ✅ **`cmdb/emailfilter/bword.py`** - Banned word filtering
- ✅ **`cmdb/emailfilter/dnsbl.py`** - DNS block list configuration
- ✅ **`cmdb/emailfilter/fortishield.py`** - FortiGuard email filtering
- ✅ **`cmdb/emailfilter/iptrust.py`** - IP trust list management
- ✅ **`cmdb/emailfilter/mheader.py`** - Email header filtering
- ✅ **`cmdb/emailfilter/options.py`** - Email filter options
- ✅ **`cmdb/emailfilter/profile.py`** - Email filter profiles

**Total new tests**: 52 comprehensive endpoint tests added

---

## [0.5.88] - 2026-01-16

### Fixed - **Generator: Stub File Response Properties**

- ✅ **Added missing response properties**: Endpoint object stubs now include `http_status_code`, `http_method`, and `http_response_time`
- ✅ **Pylance support**: `result.http_status_code` now recognized on all endpoint objects


---

## [0.5.87] - 2026-01-16

### Fixed - **Generator: Stub Files and Pydantic Models**

- ✅ **Helper stub exports**: Added `DEPRECATED_FIELDS` and `REQUIRED_FIELDS` to validator stub template
- ✅ **Core stub signature**: Fixed `check_deprecated_fields()` signature in `hfortix_core/__init__.pyi` to match implementation
- ✅ **Pydantic model return type**: Fixed `from_fortios_response()` return type from empty string to correct class name

### Fixed - **Test Generator: HTTP Methods and Parameters**

- ✅ **HTTP methods extraction**: Test generator now correctly reads `http_methods` from schema top-level (was looking in `_metadata`)
- ✅ **POST-only endpoints**: Endpoints like `system/os/reboot` that only support POST no longer generate GET tests
- ✅ **Removed unsupported `format` parameter**: Test template was using `format` parameter directly, but endpoint implementations only accept it via `payload_dict`
- ✅ **Regenerated all 1066 tests**: Test files now use only supported parameters and correct HTTP methods

### Fixed - **Generator: exists() Method API Path**

- ✅ **API path fix**: `exists()` method now uses `schema.api_path` (with hyphens) instead of `schema.path` (with underscores)
- ✅ **Example**: `/firewall/ssl-ssh-profile` instead of `/firewall/ssl_ssh_profile`
- ✅ **Impact**: All `exists()` calls now correctly query the FortiOS API

---

## [0.5.86] - 2026-01-16

### Fixed - **Generator: Response Fields and Integer Types for Service/Monitor Endpoints**

- ✅ **Added `response_fields` support**: Schema parser now extracts `response_fields` from service/monitor endpoint schemas
- ✅ **Correct response types**: Object classes now use `response_fields` for type hints (falling back to `fields` for CMDB)
- ✅ **Boolean type support**: Added `boolean` type mapping in templates (was defaulting to `str`)
- ✅ **Integer type support**: Added `int` type alongside `integer` (monitor/service schemas use `int`, CMDB uses `integer`)
- ✅ **Example fix**: `FabricTimeInSyncObject.synchronized` now correctly typed as `bool` instead of `str`
- ✅ **Example fix**: `clear_counters.post(policy=1)` now accepts `int` instead of `str`

### Technical Details

| Category    | Request Fields   | Response Fields   |
| ----------- | ---------------- | ----------------- |
| **CMDB**    | `fields`         | `fields` (same)   |
| **Monitor** | `request_fields` | `response_fields` |
| **Service** | `request_fields` | `response_fields` |

**Type mappings fixed:**
- `boolean` → `bool`
- `int` → `int` (monitor/service schemas)
- `integer` → `int` (CMDB schemas)

### Example

```python
# Before (missing attribute or wrong type)
result = fgt.api.service.system.fabric_time_in_sync.get()
print(result.synchronized)  # AttributeError or typed as str

# After (correct type)
result = fgt.api.service.system.fabric_time_in_sync.get()
print(result.synchronized)  # True/False (typed as bool)

# Before (type error)
fgt.api.monitor.firewall.policy.clear_counters.post(policy=1)  # Pylance error: expected str

# After (correct type)
fgt.api.monitor.firewall.policy.clear_counters.post(policy=1)  # Works correctly (int)
```

---

## [0.5.85] - 2026-01-16

### Fixed - **URL Encoding for Special Characters in mkey Values**

- ✅ **Proper URL encoding**: Object names containing `/` (like `CGNAT_100.64.0.0/10`) are now properly URL-encoded
- ✅ **New helper function**: Added `quote_path_param()` to `_helpers` module for consistent path parameter encoding
- ✅ **All methods fixed**: GET, PUT, DELETE, and `exists()` all now use proper encoding

### Example

```python
# Before (failed with 404)
addr = fgt.api.cmdb.firewall.address.get(name="CGNAT_100.64.0.0/10")
# Request: GET /api/v2/cmdb/firewall/address/CGNAT_100.64.0.0/10  (interpreted as path)

# After (works correctly)
addr = fgt.api.cmdb.firewall.address.get(name="CGNAT_100.64.0.0/10")
# Request: GET /api/v2/cmdb/firewall/address/CGNAT_100.64.0.0%2F10  (properly encoded)
```

---

## [0.5.84] - 2026-01-16

### Fixed - **FMG Proxy HTML Error Handling**

- ✅ **Graceful HTML error handling**: When a FortiGate returns an HTML error page via FMG proxy, it's now converted to a proper error response
- ✅ **No more raw strings**: Previously, HTML error pages were returned as raw strings causing `AttributeError: 'str' object has no attribute 'raw'`
- ✅ **Proper error info**: Error responses include `http_status: 404`, clear error message, and the raw HTML for debugging

### Example

```python
# Before (crashed with AttributeError)
psirt = fgt.api.service.security_rating.report.get(type="psirt")
print(psirt.raw)  # AttributeError: 'str' object has no attribute 'raw'

# After (proper error handling)
psirt = fgt.api.service.security_rating.report.get(type="psirt")
print(psirt.http_status_code)  # 404
print(psirt.raw["error"])      # "Endpoint not found"
print(psirt.raw["message"])    # "The FortiGate returned an HTML error page..."
```

---

## [0.5.83] - 2026-01-16

### Fixed - **Consistent `.json` Property Return Type**

- ✅ **Fixed inconsistency**: Both `FortiObject.json` and `FortiObjectList.json` now return a formatted JSON string
- ✅ **Unified API**: No more confusion - `.json` always returns a string, `.dict` returns a dict

### Migration

```python
# Before (inconsistent behavior)
obj.json    # FortiObject returned dict
list.json   # FortiObjectList returned str

# After (consistent behavior)
obj.json    # Returns formatted JSON string
list.json   # Returns formatted JSON string
obj.dict    # Returns dict (use this for dict access)
obj.raw     # Returns raw API response dict
```

---

## [0.5.82] - 2026-01-16

### Added - **Literal Type Autocomplete for Query Parameters**

- ✅ **Literal types for allowed values**: Query parameters with known values now use `Literal` types for IDE autocomplete
- ✅ **Extracted from descriptions**: Values are automatically parsed from descriptions like `['psirt', 'insight']` or `[global | vdom*]`

### Examples

```python
# Before (no autocomplete for values)
psirt = fgt.api.service.security_rating.report.get(type="psirt")  # No hints

# After (full autocomplete with Literal types)
psirt = fgt.api.service.security_rating.report.get(type="psirt")  # ✓ Suggests: "psirt", "insight"
psirt = fgt.api.service.security_rating.report.get(scope="global")  # ✓ Suggests: "global", "vdom"
```

---

## [0.5.81] - 2026-01-16

### Fixed - **Service Endpoint Type Hints**

- ✅ **Reverted `name` to `mkey`**: Service endpoints now use `mkey` parameter to match stub files
- ✅ **Type hint alignment**: Generated `.py` files now match `.pyi` stub files for proper Pylance support

### Changed - **Service Endpoint API**

Service POST endpoints now use `mkey` parameter (matching stub files):

```python
# Service endpoints with mkey parameter
fgt.api.service.sniffer.start.post(mkey="capture1", vdom="test")
fgt.api.service.sniffer.stop.post(mkey="capture1", vdom="test")
```

---

## [0.5.79] - 2026-01-16

### Added - **Full Log, Monitor, and Service API Support**

- ✅ **Log endpoints**: Full support for `fgt.api.log.*` endpoints (disk, memory, fortianalyzer, etc.)
- ✅ **Monitor endpoints**: Full support for `fgt.api.monitor.*` endpoints with proper POST method generation
- ✅ **Service endpoints**: Full support for `fgt.api.service.*` endpoints with `name` parameter

### Fixed - **Code Generator Improvements**

- ✅ **POST method generation**: Fixed schema parser to read `http_methods` from schema JSON instead of hardcoding GET
- ✅ **Monitor action endpoints**: Endpoints like `monitor.firewall.policy.reset.post()` now work correctly
- ✅ **Service POST endpoints**: Service endpoints now use intuitive `name` parameter instead of `mkey`
- ✅ **Request fields parsing**: Schema parser now reads `request_fields` for service/monitor schemas
- ✅ **Log generator fix**: Fixed log generator to use correct schema directory path

### Changed - **Service Endpoint API**

Service POST endpoints now use `name` parameter which maps to `mkey` internally:

```python
# Before (confusing)
fgt.api.service.sniffer.start.post(payload_dict={"mkey": "sniffer1"}, vdom="test")

# After (intuitive)
fgt.api.service.sniffer.start.post(name="sniffer1", vdom="test")
```

### Examples

```python
# Log endpoints
logs = fgt.api.log.disk.traffic.forward.get(rows=15)

# Monitor endpoints (including POST actions)
stats = fgt.api.monitor.firewall.policy.get()
reset = fgt.api.monitor.firewall.policy.reset.post()

# Service endpoints with name parameter
fgt.api.service.sniffer.start.post(name="capture1", vdom="test")
fgt.api.service.sniffer.stop.post(name="capture1", vdom="test")
pcap = fgt.api.service.sniffer.download.post(name="capture1", vdom="test")
# pcap.raw['content'] contains binary PCAP data
```

---

## [0.5.78] - 2026-01-16

### Fixed
- ✅ **Envelope-only responses (DELETE, some POST/PUT)**: Fixed property collision where `.status` returned `"success"` instead of `None` for responses without `results` key

### Tested
- ✅ **dnsfilter**: Fully tested endpoint category

---

## [0.5.77] - 2026-01-15

### Changed - **Renamed envelope properties to avoid collision**

- ✅ **`status` → `http_status`**: API response status ("success"/"error") now accessed via `http_status`
- ✅ **`http_status` → `http_status_code`**: HTTP status code (200, 404, etc.) now accessed via `http_status_code`
- ✅ **Updated `http_stats` dict**: Keys now use `http_` prefix consistently

**Why:**
The previous `.status` property on `FortiObject` shadowed the actual object field `status` that many FortiOS objects use (e.g., `status: "enable"` on firewall policies). This caused:
- `policy.status` → returned `"success"` (API envelope) instead of `"enable"` (object field)
- `policy["status"]` → returned `"enable"` (correct, but inconsistent)

**Migration:**
```python
# Before (0.5.76)
result.status           # API status ("success"/"error")
result.http_status      # HTTP code (200, 404)

# After (0.5.77)
result.http_status      # API status ("success"/"error")
result.http_status_code # HTTP code (200, 404)

# Object fields now accessible directly
policy.status           # "enable" or "disable" (actual object field)
```

---

## [0.5.76] - 2026-01-15

### Added - **FortiManager Proxy Support**

- ✅ **FortiManagerProxy client**: Route FortiOS API calls through FortiManager to managed devices
- ✅ **HTTPClientFMG**: New HTTP client for FortiManager JSON-RPC API (in `hfortix_core`)
- ✅ **Same FortiOS API**: Use the exact same `fgt.api.cmdb.*` and `fgt.api.monitor.*` patterns
- ✅ **Full retry/circuit-breaker support**: Shares infrastructure with FortiOS HTTPClient

**Usage:**
```python
from hfortix_fortios import FortiManagerProxy

# Connect to FortiManager
fmg = FortiManagerProxy(
    host="fmg.example.com",
    username="admin",
    password="password",
    adom="production",
)

# Get a proxied FortiOS client for a specific device
fgt = fmg.proxy(device="firewall-01")

# Use the exact same FortiOS API!
addresses = fgt.api.cmdb.firewall.address.get()
for addr in addresses:
    print(f"{addr.name}: {addr.subnet}")
```

### Added - **Response Timing & Envelope Properties**

- ✅ **Response timing**: `response_time` (seconds), `response_time_ms` (milliseconds), `http_stats` property
- ✅ **Explicit envelope properties**: `http_method`, `http_status`, `status`, `vdom`, `mkey`, `revision`, `serial`, `version`, `build`
- ✅ **FortiObjectList support**: Same properties available on list responses

```python
result = fgt.api.cmdb.firewall.address.get()
print(f"Query took {result.response_time_ms:.1f}ms")
print(result.http_stats)  # {'http_response_time': 206.4}
```

### Fixed - **Silent 404 for exists() Method**

- ✅ **Silent 404 handling**: `exists()` no longer logs "Request failed: HTTP 404" messages
- ✅ **Clean set() workflow**: No noisy 404 logs when checking existence before create/update

### Fixed - **Mutation Methods Return FortiObject**

- ✅ **Type stubs updated**: `post()`, `put()`, `delete()`, and `set()` now return `FortiObject` with full autocomplete
- ✅ **Consistent API**: All endpoint methods return properly typed `FortiObject` instances

### Fixed - **FortiObject.raw Property**

- ✅ **Fixed `.raw` property**: Now returns the full API response envelope (with `status`, `http_status`, `vdom`, etc.)
- ✅ **Fixed `exists()` method**: Properly detects existing objects
- ✅ **Fixed `set()` method**: Now correctly uses `put()` for updates and `post()` for creates

### Fixed - **Performance Test Utility and Client Type Stubs**

- ✅ **Fixed `performance_test.py`**: Proper endpoint navigation including `monitor`/`cmdb` namespace
- ✅ **Updated `client.pyi`**: Added all missing constructor parameters with proper `@overload`

### Fixed - **Singleton Endpoint Response Handling**

- ✅ **Fixed singleton endpoints**: Endpoints returning dict (not list) in `results` now wrap correctly
- ✅ **Direct attribute access**: `result.mailto1` works for singleton endpoints

---

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
