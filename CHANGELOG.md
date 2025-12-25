# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.34] - 2025-12-25

### Added

- **Schedule Convenience Methods**: Added comprehensive convenience methods to all schedule types
  - **New Methods** (available for `schedule_onetime`, `schedule_recurring`, `schedule_group`):
    - `get_by_name(name, vdom=None)`: Returns schedule data directly (not full API response)
    - `rename(name, new_name, vdom=None)`: Rename a schedule in one call
    - `clone(name, new_name, **overrides, vdom=None)`: Clone schedule with optional modifications
  - **Response Helpers** (added to `hfortix.FortiOS.api._helpers`):
    - `get_mkey(response)`: Extract created object's name from response
    - `is_success(response)`: Check if operation succeeded
    - `get_results(response)`: Extract results from response
  - Matches the convenience method pattern from `firewallPolicy`
  - Makes schedule management more user-friendly and consistent
  - See `SCHEDULE_CONVENIENCE_METHODS.md` for full documentation
  - See `examples/schedule_convenience_demo.py` for usage examples

- **IP/MAC Binding Convenience Wrapper**: New helper class for firewall IP/MAC binding management
  - Located at `hfortix.FortiOS.api.v2.cmdb.firewall._helpers.ipmacbinding_table`
  - **Core Methods**:
    - `create(seq_num, ip, mac, name=None, status='enable', vdom=None)`: Create new binding
    - `update(seq_num, **kwargs, vdom=None)`: Update existing binding
    - `delete(seq_num, vdom=None)`: Delete binding
    - `get(seq_num=None, vdom=None)`: Get binding(s) by sequence number
    - `get_all(vdom=None)`: Get all bindings
  - **Convenience Methods**:
    - `exists(seq_num, vdom=None)`: Check if binding exists
    - `enable(seq_num, vdom=None)`: Enable a binding
    - `disable(seq_num, vdom=None)`: Disable a binding
  - **Validation**: IP addresses, MAC addresses, status values, name length
  - Comprehensive test suite: `examples/ipmacbinding_test_suite.py` (19 pytest tests)

- **Circuit Breaker Auto-Retry**: Optional automatic retry when circuit breaker opens
  - New parameters:
    - `circuit_breaker_auto_retry` (bool, default=False) - Enable/disable auto-retry
    - `circuit_breaker_max_retries` (int, default=3) - Maximum retry attempts
    - `circuit_breaker_retry_delay` (float, default=5.0) - Delay in seconds between retries
  - When enabled, client automatically waits and retries when circuit breaker opens instead of failing immediately
  - Useful for production scripts that need resilience against temporary service degradation
  - **IMPORTANT**: Retry delay is configurable and separate from circuit_breaker_timeout
    - `circuit_breaker_retry_delay`: How long to wait between retry attempts (default: 5s)
    - `circuit_breaker_timeout`: How long circuit stays open before transitioning to half-open (default: 30s)
  - **WARNING**: Not recommended for test environments - may cause long delays
  - Fail-fast behavior is preserved by default (auto-retry disabled)
  - Available in both sync (`HTTPClient`) and async (`AsyncHTTPClient`) clients
  - Examples:

    ```python
    # Fail-fast (default) - raises CircuitBreakerOpenError immediately
    fgt = FortiOS(host="192.0.2.10", token="api_token")

    # Auto-retry - waits 5 seconds between retries (up to 3 attempts)
    fgt = FortiOS(
        host="192.0.2.10",
        token="api_token",
        circuit_breaker_auto_retry=True,
        circuit_breaker_max_retries=3,
        circuit_breaker_retry_delay=5.0  # Wait 5s between retries
    )

    # Custom retry delay for slower recovery scenarios
    fgt = FortiOS(
        host="192.0.2.10",
        token="api_token",
        circuit_breaker_auto_retry=True,
        circuit_breaker_max_retries=5,
        circuit_breaker_retry_delay=10.0  # Wait 10s between retries
    )
    ```

- **Pytest Test Suites**: Comprehensive test coverage for convenience wrapper classes
  - `examples/ipmacbinding_test_suite.py`: 19 tests covering IP/MAC binding CRUD operations
    - Tests: create, read, update, delete operations
    - Validation: IP addresses, MAC addresses, status values, name length
    - Convenience methods: enable(), disable(), exists()
    - Error handling: duplicate entries, non-existent resources
    - List operations and cleanup fixtures
  - `examples/circuit_breaker_test.py`: Circuit breaker behavior demonstration
    - Fail-fast vs auto-retry comparison
    - Circuit breaker state transitions
    - Recovery scenarios with valid endpoints
  - All tests use pytest framework with fixtures for cleanup
  - Tests validate both convenience wrappers and direct API access

### Changed

- **Circuit Breaker Defaults**: Adjusted thresholds for better testing and general use
  - `circuit_breaker_threshold`: 5 → 10 consecutive failures (more tolerant)
  - `circuit_breaker_timeout`: 60.0s → 30.0s (faster recovery)
  - **Rationale**: Previous settings (5 failures, 60s timeout) were too aggressive for:
    - Testing environments where some failures are expected
    - Development workflows with frequent code changes
    - Networks with occasional transient issues
  - New settings still provide circuit breaker protection while being more practical
  - Users can override via `circuit_breaker_threshold` and `circuit_breaker_timeout` parameters if needed

- **FirewallPolicy.exists()**: Enhanced to support lookup by name or policy ID
  - Added optional `name` parameter for checking policy existence by name
  - `policy_id` parameter is now optional (either `policy_id` or `name` required)
  - Maintains backward compatibility - existing code using `policy_id` continues to work
  - **Performance Note**: Using `name` performs a recursive lookup (slower), while `policy_id` uses direct API call (faster)
  - Improves API consistency with schedule wrapper methods
  - Examples:
    ```python
    # Direct lookup by ID (recommended for performance)
    exists = fgt.firewall.policy.exists(policy_id=5)

    # Lookup by name (convenient but slower)
    exists = fgt.firewall.policy.exists(name="Allow-Web-Traffic")
    ```

## [0.3.33] - 2025-12-25

### Fixed

- **Package Distribution**: Fixed missing `password_policy.py` module in PyPI package
  - Version 0.3.32 was missing the `hfortix.FortiOS.api.v2.cmdb.system.password_policy` module
  - This caused `ModuleNotFoundError` when initializing FortiOS instance
  - Updated version in both `setup.py` and `pyproject.toml` to ensure consistency
  - Rebuilt and republished package with all required modules included
  - Users experiencing the import error should upgrade: `pip install --upgrade hfortix`

## [0.3.32] - 2025-12-24

### Fixed

- **CI/CD Pipeline**: Publishing now properly blocked if CI fails
  - Removed `if: always()` from wait-for-ci job
  - Job now fails if CI checks don't pass, preventing publishing
  - Fixed trailing whitespace in workflow file

## [0.3.31] - 2025-12-24

### Fixed

- **CI/CD Pipeline**: Fixed wait-for-ci job to properly wait for CI completion
  - Switched to `fountainhead/action-wait-for-check` for better reliability
  - Added 30-minute timeout with 10-second polling interval
  - Prevents race condition where publishing started before CI completed
  - Job now always runs but conditionally waits based on trigger type

## [0.3.30] - 2025-12-24

### Changed

- **CI/CD Pipeline**: Publishing workflow now waits for CI checks to pass
  - Added `wait-for-ci` job to ensure all quality checks pass before publishing
  - Configured trusted publishing for TestPyPI (no API token needed)
  - Publishing flow: CI passes → TestPyPI → verify → PyPI production
  - Added comprehensive PyPI setup documentation (`docs/PYPI_SETUP.md`)

## [0.3.29] - 2025-12-24

### Changed

- **CI/CD Pipeline**: Enhanced PyPI publication workflow
  - Now publishes to TestPyPI first for validation
  - Only publishes to production PyPI after successful TestPyPI verification
  - Added package availability verification steps
  - Prevents publishing broken packages to production

## [0.3.28] - 2025-12-24

### Fixed

- **Critical Syntax Errors**: Fixed 512 broken f-strings in CMDB _helpers files
  - Black formatter had incorrectly reformatted multi-line f-strings
  - Caused 511 E999 syntax errors across all _helpers files
  - Used regex pattern to rejoin broken f-string expressions
  - All files now pass flake8 validation

### Changed

- **Pre-commit Configuration**: Enhanced Black exclusion documentation
  - Added critical warning comment about _helpers exclusion
  - Documented why exclusion must be maintained (prevents 500+ syntax errors)
  - Prevents accidental removal of necessary exclusion pattern

## [0.3.27] - 2025-12-24

### Changed

- **Import Refactoring**: Refactored monitor API imports for better code quality
  - `hfortix/FortiOS/api/v2/monitor/firewall/__init__.py` now uses direct class imports
  - Eliminated confusing module alias pattern (e.g., `sessions as sessions_module`)
  - Imports are now alphabetically sorted and properly formatted
  - Cleaner, more maintainable code that passes isort/black checks

### Fixed

- **Pre-commit Configuration**: Removed monitor API from exclusions
  - Monitor API files now included in black, isort, flake8, and mypy checks
  - Fixed yamllint errors (trailing blank lines in YAML files)
  - All pre-commit hooks now pass successfully

## [0.3.26] - 2025-12-24

### Fixed

- **Syntax Errors**: Fixed 32 files with broken f-strings (E999 errors)
  - f-strings now properly formatted on single lines
  - All files pass flake8 syntax validation
  - Pre-release workflow now catches syntax errors immediately

### Changed

- **Directory Naming**: Renamed hyphenated directories to follow Python conventions
  - `wireless-controller` → `wireless_controller`
  - `switch-controller` → `switch_controller`
  - `extension-controller` → `extension_controller`
  - `endpoint-control` → `endpoint_control`
  - `web-proxy` → `web_proxy`
  - **BREAKING CHANGE**: Import paths updated, users must update their code
  - Mypy can now properly validate all API modules

### Added

- `X/scripts/fix_fstrings.py` - Utility to fix broken f-strings in generated code
- `X/scripts/rename_hyphenated_dirs.py` - Utility for directory renaming

## [0.3.25] - 2025-12-24

### Added

- **Pre-Release Workflow**: Comprehensive code quality automation
  - `make pre-release` - Auto-fix and validate code before release
  - `make fix` - Auto-fix formatting and import issues
  - `make fix-check` - Dry-run to see what would be fixed
  - `X/scripts/pre_release_fix.py` - Auto-fix script with Black and isort
  - `X/scripts/pre_release_check.py` - Validation script with all quality checks

### Changed

- **Code Quality Configuration**: Centralized and consistent settings
  - Created `.flake8` config file with PEP 8 standards (79 char line length)
  - API folders excluded from E501 line-length checks (auto-generated code)
  - Updated `.pre-commit-config.yaml` to use `.flake8` config
  - Updated GitHub Actions CI to use `.flake8` config
  - All tools (Makefile, scripts, pre-commit, CI) now use same configuration

- **Pre-commit Hooks**: Improved configuration
  - Excluded `X/` directory from all checks (development tools, not package code)
  - Consistent exclude patterns across all hooks
  - Pre-commit check added to pre-release workflow (warning only)

### Fixed

- **Test Execution**: Tests excluded from pre-release workflow
  - Pre-release checks no longer run tests (run separately with `make test`)
  - Focus on code quality, formatting, and linting only

### Documentation

- `X/scripts/README.md` - Pre-release workflow guide
- `X/CODE_QUALITY_CONFIG.md` - Comprehensive configuration documentation

## [0.3.24] - 2025-12-24

### Added

- **Exception Hierarchy**: Comprehensive retry logic support
  - `RetryableError` base class for transient errors (rate limits, timeouts, service unavailable)
  - `NonRetryableError` base class for permanent errors (bad request, duplicate entry, not found)
  - All existing exceptions updated to inherit from appropriate base class
  - Enables intelligent retry strategies: `if isinstance(error, RetryableError)`

- **New Exception Types**: Client-side and specialized errors
  - `ConfigurationError` - FortiOS instance misconfiguration (replaces generic ValueError)
  - `VDOMError` - VDOM-specific errors with vdom attribute
  - `OperationNotSupportedError` - Unsupported operations on endpoints
  - `ReadOnlyModeError` - Already existed, now properly documented

- **Enhanced Exception Metadata**: Better debugging and error tracking
  - `request_id` - Unique UUID for each request (auto-generated)
  - `timestamp` - ISO 8601 timestamp when error occurred
  - Enhanced `__str__()` - Human-readable with emoji hints (💡)
  - Added `__repr__()` - Developer-friendly representation for debugging
  - All APIError exceptions now capture full context automatically

- **Recovery Suggestions**: Built-in error recovery guidance
  - `DuplicateEntryError.suggest_recovery()` - Suggests using PUT or checking existing
  - `EntryInUseError.suggest_recovery()` - Suggests removing references first
  - `ResourceNotFoundError.suggest_recovery()` - Suggests using POST or listing available
  - Helps developers understand how to handle common error scenarios

- **Helper Utility Functions**: Simplify retry logic implementation
  - `is_retryable_error(error)` - Check if error should be retried
  - `get_retry_delay(error, attempt, base_delay, max_delay)` - Calculate backoff delay
    - Exponential backoff for `RateLimitError`
    - Linear backoff for `ServiceUnavailableError`
    - Moderate backoff for `TimeoutError`
  - Makes implementing retry logic simple and consistent

- **Comprehensive Tests**: Full test coverage for new functionality
  - Exception hierarchy tests (RetryableError vs NonRetryableError)
  - Metadata capture tests (request_id, timestamp)
  - String representation tests (__str__ and __repr__)
  - Recovery suggestion tests
  - Helper function tests (is_retryable_error, get_retry_delay)
  - Client-side exception tests
  - All tests passing ✅

### Changed

- **Exception Inheritance**: Updated all HTTP status exceptions
  - `BadRequestError` now inherits from `NonRetryableError` (was APIError)
  - `ResourceNotFoundError` now inherits from `NonRetryableError` (was APIError)
  - `RateLimitError` now inherits from `RetryableError` (was APIError)
  - `ServerError` now inherits from `RetryableError` (was APIError)
  - `ServiceUnavailableError` now inherits from `RetryableError` (was APIError)
  - `TimeoutError` now inherits from `RetryableError` (was APIError)
  - `CircuitBreakerOpenError` now inherits from `RetryableError` (was APIError)

- **FortiOS-Specific Exceptions**: Updated inheritance
  - `DuplicateEntryError` now inherits from `NonRetryableError` (was APIError)
  - `EntryInUseError` now inherits from `NonRetryableError` (was APIError)
  - `InvalidValueError` now inherits from `NonRetryableError` (was APIError)
  - `PermissionDeniedError` now inherits from `NonRetryableError` (was APIError)

- **Error Hints**: Enhanced with emoji for better visibility
  - All hints now prefixed with 💡 emoji in __str__ output
  - Makes hints stand out in error messages and logs

### Documentation

- Updated `docs/ERROR_HANDLING_CONFIG.md` with retry examples
- Added exception hierarchy diagram in inline documentation
- Enhanced docstrings for all new exception classes
- Added comprehensive examples for helper functions

### Migration Guide

**No Breaking Changes**: All existing code continues to work. The changes are additive:

```python
# Old code still works
try:
    fgt.api.cmdb.firewall.policy.post(data=...)
except DuplicateEntryError as e:
    print(f"Error: {e}")

# New capabilities available
try:
    fgt.api.cmdb.firewall.policy.post(data=...)
except DuplicateEntryError as e:
    print(f"Request ID: {e.request_id}")
    print(f"Timestamp: {e.timestamp}")
    print(e.suggest_recovery())

# Intelligent retry logic
try:
    result = fgt.api.cmdb.firewall.policy.get()
except Exception as e:
    if is_retryable_error(e):
        delay = get_retry_delay(e, attempt=1)
        time.sleep(delay)
        # retry...
```

## [0.3.23] - 2025-12-23

### Added

- **API Endpoints**: Added missing monitor API endpoints
  - `check_addrgrp_exclude_mac_member` - Firewall address group MAC exclusion checking
  - `check_port_availability` - System port availability checking
  - Helper modules for both endpoints with validation support

### Fixed

- **CI/CD Pipeline**: Resolved issues blocking automated builds
  - All pre-commit hooks now pass consistently
  - Fixed recurring formatting issues that caused CI failures
  - Mypy type checking passes without errors
  - Ready for automated PyPI publishing via GitHub Actions
- **Code Quality**: Resolved persistent pre-commit formatting issues
  - Fixed black formatting instability with inline comments in `http_client.py` and `http_client_base.py`
  - Moved inline type annotation comments to separate lines for stable formatting
  - Added missing `__all__` exports to resolve mypy module attribute errors
  - Prevents format/check/format loops in CI pipeline
- **Git Configuration**: Fixed `.gitignore` pattern blocking legitimate API files
  - Changed `check_*.py` to `/check_*.py` to only ignore root-level temporary scripts
  - Prevents accidental exclusion of API endpoint modules with `check_` prefix
  - Previously ignored files now properly tracked and versioned
- **Module Imports**: Removed unnecessary imports causing mypy errors
  - Cleaned up redundant module-level imports in `firewall/__init__.py`
  - Fixed "Module has no attribute" errors in type checking

### Changed

- **Code Formatting**: Applied black/isort formatting to all newly tracked files
  - Consistent quote style (double quotes) across all API modules
  - Proper import ordering and grouping per PEP 8
  - Standardized blank line placement
  - All 1596 source files pass mypy type checking

## [0.3.22] - 2025-12-23

### Added

- **CI/CD Pipeline**: Complete GitHub Actions workflow automation
  - **CI Workflow** (`ci.yml`): Automated code quality checks on every push/PR
    - Lint & format checking (Black, isort, flake8)
    - Type checking with mypy
    - Security scanning with Bandit (JSON reports as artifacts)
    - Build validation with twine
    - Pre-commit hook enforcement
    - Multi-Python version testing (3.10, 3.11, 3.12)
    - All checks gate job (blocks merge if any fail)
  - **Publish Workflow** (`publish.yml`): Automated PyPI publishing
    - Automatic publishing on git tag push (`v*.*.*`)
    - Manual workflow dispatch for TestPyPI testing
    - Version consistency validation across pyproject.toml, setup.py, __init__.py
    - Trusted publishing support (no API tokens needed)
    - Automatic GitHub release creation with changelog extraction
  - **CodeQL Analysis** (`codeql.yml`): Advanced security scanning
    - Runs on push to main, PRs, and weekly schedule
    - GitHub Advanced Security vulnerability detection
  - **Dependency Review** (`dependency-review.yml`): PR dependency checking
    - Detects new dependencies and vulnerabilities
    - Blocks moderate+ severity issues and GPL licenses
  - **Auto-label PRs** (`label-pr.yml`): Automatic PR categorization
    - Labels based on changed files (docs, tests, api, core, etc.)
  - **Documentation**: Complete CI/CD guide in `docs/CICD.md`
    - Workflow explanations and usage examples
    - Local development integration
    - Troubleshooting guide

### Changed

- **Code Quality**: Applied comprehensive PEP 8 compliance
  - Reformatted 796 files with Black (line-length=79)
  - Fixed 1000+ flake8 lint errors for strict PEP 8 compliance
  - Standardized on 79-character line limit (PEP 8 standard)
  - Only ignoring E203 (Black slice spacing) and W503 (modern line break style)
  - All auto-generated API v2 files excluded from linting
- **Import Cleanup**: Removed unused imports across core modules
  - Fixed F401 (unused imports) warnings
  - Added proper noqa comments for intentional exceptions

### Fixed

- **Empty F-Strings**: Fixed F541 errors (f-strings without placeholders)
  - Converted empty f-strings to regular strings in performance_test.py
  - Proper string formatting in all print statements
- **Unused Variables**: Fixed F841 warnings in test functions
  - Added explicit ignore markers for intentionally unused variables
- **Long Lines**: Systematic fixing of E501 errors
  - Wrapped docstrings to 79 characters
  - Split long log messages across lines
  - Added strategic noqa comments for unavoidable long lines

### Removed

## [0.3.21] - 2025-12-22

### Fixed

- **Type Errors in Core Modules**: Fixed multiple type checking errors across the codebase
  - **fortios.py line 472**: Fixed `Operator "in" not supported for types "Literal[' ']" and "str | None"`
    - Added None check before using `in` operator for token validation
    - Changed from `if has_token:` to `if has_token and token is not None:`
  - **firewallPolicy.py**: Fixed return type mismatches for API method calls (5 locations)
    - Added `Coroutine` to type imports for proper type hint support
    - Added `# type: ignore[return-value]` comments at lines 733, 777, 1220, 1246, 1455
    - Issue: API methods return `Union[dict, Coroutine]` for async/sync compatibility
    - Wrapper methods declare strict `Dict` return types for better IDE autocomplete
  - **performance_test.py**: Fixed dynamic attribute access errors
    - Line 323: Added `hasattr` check before calling dynamic `get()` method
    - Line 359: Replaced non-existent `logout()` method with `close()` method
  - All reported type errors now resolved while maintaining full functionality

- **Type Annotation Runtime Error**: Fixed `NameError: name 'Coroutine' is not defined` error
  - Added `from __future__ import annotations` to 832 files across the entire API codebase
  - Issue: `Coroutine` type was imported in `TYPE_CHECKING` blocks (False at runtime) but used in runtime type annotations
  - Solution: Deferred evaluation of all type annotations using PEP 563 (`__future__.annotations`)
  - Enables proper type checking while avoiding runtime evaluation errors
  - Affected files: All API endpoint modules (cmdb, log, monitor, service)
  - Created automated fix script (`fix_coroutine_imports.py`) for systematic resolution
  - All tests now pass without runtime type annotation errors

### Added

- **API Validators - Complete Coverage**: Generated validation helpers for all FortiOS API types
  - Generated 832 validation helper modules across 77 categories (4 API types)
  - **CMDB API**: 37 categories, 548 validators
  - **LOG API**: 5 categories, 5 validators
  - **MONITOR API**: 32 categories, 276 validators
  - **SERVICE API**: 3 categories, 3 validators
  - Extended validator generator to support all API types (cmdb, log, monitor, service)
  - Implemented API-type-specific path matching (CMDB uses `/cmdb/` prefix, others don't)
  - Enhanced fuzzy path matching for complex endpoint structures (0 endpoints skipped)
  - Consistent `VALID_BODY_*` and `VALID_QUERY_*` naming convention for parameter constants
  - Body parameter validation: Payload field validation with `VALID_BODY_ACTION`, `VALID_BODY_STATUS`, etc.
  - Query parameter validation: URL parameter validation with `VALID_QUERY_ACTION`, etc.
  - Handles parameter name collisions (e.g., `action` in both body and query contexts)
  - **Validation coverage**:
    - ✅ Enum validation (predefined allowed values)
    - ✅ Length validation (minLength/maxLength for strings)
    - ✅ Range validation (min/max for numeric values)
    - ✅ Pattern validation (regex patterns)
    - ✅ Type validation (implicit via type coercion with error handling)
    - ⚠️ **Required field validation NOT YET IMPLEMENTED** - needs to be added
  - All validators auto-generated from FortiOS 7.6.5 OpenAPI specifications
  - CMDB Categories: alertemail, antivirus, application, authentication, automation, casb, certificate,
    diameter-filter, dlp, dnsfilter, emailfilter, endpoint-control, ethernet-oam, extension-controller,
    file-filter, firewall, ftp-proxy, icap, ips, log, monitoring, report, router, rule, sctp-filter,
    switch-controller, system, user, videofilter, virtual-patch, voip, vpn, waf, web-proxy, webfilter,
    wireless-controller, ztna

- **Builder Pattern Refactoring (Phase 1)**: Eliminated code duplication in firewall policy endpoints
  - Created `hfortix/FortiOS/api/v2/cmdb/firewall/_helpers/policy_helpers.py` (123 lines)
  - Implemented `build_policy_payload()` - API layer function (no normalization)
  - Implemented `build_policy_payload_normalized()` - Wrapper layer function (with normalization)
  - Implemented `normalize_to_name_list()` - Format converter for flexible inputs
  - Refactored `policy.py`: 1796 → 1381 lines (-415 lines, -23% reduction)
  - Refactored `firewallPolicy.py`: 1703 → 1541 lines (-162 lines, -10% reduction)
  - Total: 454 lines removed, 13% reduction across both files
  - All 226 integration tests passing - Zero breaking changes
  - Proper architectural separation: API layer (no normalization) vs Wrapper layer (with normalization)

- **Code Quality Improvements**: Comprehensive codebase quality audit and improvements
  - **Code Formatting**: Applied `isort` and `black` to all 823 files in `hfortix/`
    - Fixed syntax error in `lldp_profile.py` (renamed variables with dots to underscores)
    - All files now follow consistent PEP 8 formatting standards
    - Consistent import ordering across entire codebase
  - **Type Hints**: Added missing type hints to 7 functions
    - `performance_test.py`: Added return types to `print_summary()`, `quick_test()`
    - `exceptions_forti.py`: Added type hints to 5 functions (error handling utilities)
    - `api/__init__.py`: Added return type to `__dir__()`
    - Added `Optional` import where needed
  - **Docstring Audit**: Verified Google-style docstrings across all public APIs
    - Core classes: `FortiOS`, `AsyncHTTPClient`, `HTTPClient`, `BaseHTTPClient` - all comprehensive
    - Exception classes: All have proper descriptions, args, and examples
    - API endpoint classes: All have complete method documentation
    - Helper functions: All utility functions properly documented
  - **Legacy Code Review**: Scanned for deprecated patterns and legacy implementations
    - No actual legacy code found (only config options with "legacy" in names)
    - Codebase is clean and modern

### Changed

- **Documentation Updates**: Updated roadmap and project status documentation
  - Updated `ROADMAP.md` with comprehensive feature history from v0.3.14-v0.3.21
  - Added detailed v0.3.18 features (custom HTTP clients, environment variables, credential validation)
  - Added v0.3.10-0.3.13 features (circuit breaker, connection pool, request tracking, structured logging)
  - Changed builder pattern status from ✅ to ⏳ (only 1 of 30+ resources completed)
  - Updated version tracking: v0.3.20 released, v0.3.21 in development
  - Created `REFACTORING_SUMMARY.md` documenting builder pattern implementation

### Fixed

- **Firewall Policy Wrapper**: Improved parameter handling and code consistency
  - Fixed `get()` method to properly construct API parameters dictionary
  - Fixed `move()` method to use consistent parameter passing pattern
  - Simplified implementation to match other wrapper methods
  - All parameters now passed correctly to underlying API layer

- **Validator Generator**: Fixed parameter type handling and naming consistency
  - Fixed undefined constant bug where query parameters referenced non-existent body constants
  - Separated validation logic: body parameters (payload) vs query parameters (URL)
  - Implemented consistent naming: `VALID_BODY_*` for payload, `VALID_QUERY_*` for URL params
  - Prevents parameter name collision issues (e.g., `action` can exist in both contexts)
  - Examples: `firewall/policy.py` (VALID_BODY_ACTION), `log/syslogd_setting.py` (both types)

## [0.3.20] - 2025-12-21

### Fixed

- **Firewall Policy Wrapper**: Fixed critical bugs in policy management wrapper
  - Fixed `move()` method "top" and "bottom" positions now work correctly
    - Properly queries all policies to find first/last policy IDs
    - Excludes the policy being moved from consideration
    - Uses query parameters instead of data payload for move action
    - Bypasses generated API layer to call HTTP client directly with `params`
  - Fixed `get_by_name()` return type - now returns single dict or None (not a list)
  - Fixed `get(policy_id=X)` response handling - properly extracts policy from list response
  - Fixed parameter names in all methods: `mkey` → `policyid` for consistency
  - Added `raw_json` parameter support to `create()`, `get()`, `update()`, `delete()`, `move()`
  - All 10 wrapper methods now fully tested and working with live FortiGate

### Tested

- **Integration Testing**: Verified all firewall policy wrapper functions against live FortiGate
  - ✅ `create()` - Create policies with all parameters
  - ✅ `get()` - Get all policies or specific policy by ID  
  - ✅ `get_by_name()` - Get policy by exact name match
  - ✅ `update()` - Partial policy updates
  - ✅ `delete()` - Delete policies
  - ✅ `exists()` - Check policy existence
  - ✅ `move()` - Reorder policies (before/after/top/bottom)
  - ✅ `clone()` - Duplicate policies with modifications
  - ✅ `enable()` / `disable()` - Toggle policy status

### Documentation

- **Filtering Guide**: Confirmed filter operators for policy searches
  - `==` - Exact match (case insensitive)
  - `=@` - Contains (substring match)
  - `!=` - Not equals
  - `!@` - Does not contain
  - Multiple conditions with `&` (AND logic)
  - Examples: `filter="name=@API_TEST"` returns all policies containing "API_TEST"

## [0.3.19] - 2025-12-21

### Changed

- **Type Checking Configuration**: Cleaned up mypy configuration in pyproject.toml
  - Removed unnecessary `httpx.*` mypy override (httpx v0.28.1 has built-in type hints)
  - Removed obsolete `requests.*` mypy override (library migrated to httpx in v0.3.12)
  - Enables better IDE autocomplete and type checking for HTTP client usage
  - Verified: Zero new mypy errors after cleanup

### Improved

- **Build Configuration**: Updated .gitignore to exclude GitHub templates
  - Excludes `.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`
  - Prevents inclusion of work-in-progress templates in releases

## [0.3.18] - 2025-12-21

### Fixed

- **Test File Naming**: Fixed critical circular import issues caused by test files shadowing Python stdlib modules
  - Renamed all 354 test files to use `test_` prefix (e.g., `statistics.py` → `test_statistics.py`)
  - Prevents shadowing of Python stdlib modules: `statistics`, `ssl`, `os`, `time`, `profile`, `resource`, `test`
  - Fixes "cannot import name 'fgt' from partially initialized module" errors
  - All monitor, vpn, wifi, router, and system tests now execute correctly
  - Follows Python testing best practices and PEP 8 conventions
  - Created automated `rename_tests.py` script for systematic renaming

### Added

- **Extensibility: Custom HTTP Clients**: Library now supports custom HTTP client implementations
  - `IHTTPClient` Protocol interface (PEP 544) for type-safe extensibility
  - All 750+ endpoint files use TYPE_CHECKING pattern for protocol imports
  - `FortiOS.__init__()` accepts custom clients via `client` parameter
  - Enables audit logging, response caching, fake clients for testing, custom authentication
  - Complete example file: `examples/custom_http_client_example.py`
  - Three production-ready examples: AuditLoggingHTTPClient, CachingHTTPClient, FakeHTTPClient
  - Documentation in README.md "Extensibility" section
  - Use cases: SOX/HIPAA/PCI-DSS compliance, CI/CD testing, performance optimization

- **Environment Variables Support**: Load credentials from environment variables
  - Support for `FORTIOS_HOST`, `FORTIOS_TOKEN`, `FORTIOS_USERNAME`, `FORTIOS_PASSWORD`
  - Explicit parameters take priority over environment variables
  - Enables clean separation of credentials from code
  - Perfect for CI/CD pipelines, Docker containers, and security best practices
  - Example: `export FORTIOS_TOKEN="..." && python script.py`
  - No hardcoded credentials needed in scripts
  - Comprehensive documentation in README.md and QUICKSTART.md

- **Credential Validation**: Comprehensive validation for authentication credentials
  - Validates token format (25+ characters minimum, alphanumeric with hyphens/underscores)
  - Catches common copy-paste errors: spaces in tokens, invalid special characters
  - Detects placeholder tokens: "your_token_here", "xxx", "api_token", "your-api-token", etc.
  - Version-agnostic: works with all FortiOS versions (31-32 chars in older, 40+ chars in newer)
  - Enforces username+password pairing (both must be provided together)
  - Provides actionable error messages with clear examples
  - Prevents authentication failures before making API calls
  - Added comprehensive inline documentation

- **Protocol Method Stubs**: Enhanced IHTTPClient protocol interface
  - Added `get_operations()` method stub for operation tracking
  - Added `get_write_operations()` method stub for write operation filtering
  - Added `get_health_metrics()` method stub for connection health monitoring
  - All methods marked as optional with comprehensive docstrings
  - Enables type-safe access to optional features without suppressions

### Improved

- **Documentation**: Updated authentication documentation
  - Added detailed token requirements section in README.md
  - Documented 25-character minimum and version variability
  - Updated QUICKSTART.md with credential validation examples
  - Added error handling examples for common mistakes
  - Documented username/password validation requirements
  - Added best practices for token format

- **Documentation Links**: Fixed PyPI compatibility for all documentation
  - Updated all doc links to use full GitHub URLs (works on PyPI)
  - Removed broken HELPER_METHODS.md references (file doesn't exist)
  - Consolidated helper method docs in ENDPOINT_METHODS.md
  - Renamed DOCS_INDEX.md → INDEX.md for clarity
  - All cross-references verified and working

- **Code Quality**: Fixed type checking errors
  - Added PerformanceTestResults to TYPE_CHECKING imports in utils.py
  - Fixed "not defined" error on line 55
  - Updated .gitignore to include .mypy_cache/

### Changed

- **Token Validation Logic**: Improved from length-based to format-based validation
  - Removed strict 20-character minimum (too restrictive)
  - Changed to flexible 25-character minimum (catches invalid tokens, allows all FortiOS versions)
  - Treats tokens as opaque strings per Fortinet best practices
  - No maximum length restriction (supports all current and future FortiOS versions)
  - Enhanced alphanumeric validation with hyphen/underscore support
  - Expanded placeholder detection list for better error catching

## [0.3.17] - 2025-12-20

### Added
  - New `fgt.api.utils.performance_test()` method for integrated testing
  - Validates connection pool settings automatically
  - Tests real-world API endpoints (status, policies, addresses, interfaces, resources)
  - Identifies device performance profile (high-performance, fast-lan, remote-wan)
  - Provides device-specific recommendations for optimal settings
  - Accessible via `fgt.api.utils` namespace
  - Standalone functions also available: `quick_test()`, `run_performance_test()`
  - Command-line interface: `python -m hfortix.FortiOS.performance_test`
  - Comprehensive documentation in `docs/PERFORMANCE_TESTING.md`

- **Read-Only Mode**: Protect production environments by blocking write operations
  - Add `read_only=True` flag to FortiOS constructor
  - Blocks all POST, PUT, and DELETE requests with `ReadOnlyModeError`
  - GET requests execute normally for queries and monitoring
  - Perfect for testing, CI/CD pipelines, dry-run previews, and training
  - Works with both sync and async modes

- **Operation Tracking**: Complete audit log of all API operations
  - Add `track_operations=True` flag to enable operation logging
  - Records timestamp, method, URL, request data, response status, and VDOM
  - Access via `get_operations()` or `get_write_operations()`
  - Tracks both successful operations and those blocked by read-only mode
  - Perfect for debugging, auditing, change logs, and documentation
  - Works with both sync and async modes

- **Extended Filter Documentation**: Comprehensive guide to FortiOS filtering
  - New `docs/FILTERING_GUIDE.md` with complete operator documentation
  - Covers all FortiOS native filter operators: `==`, `!=`, `=@`, `!@`, `<`, `<=`, `>`, `>=`
  - 50+ practical examples for common use cases
  - Field-specific examples for addresses, policies, interfaces, routes
  - Advanced patterns: range queries, combined filters, exclusions

- **Username/Password Authentication**: Alternative to API token authentication
  - Session-based authentication using username and password
  - Automatic session management and renewal
  - Useful when API tokens are not available or for temporary access
  - Example: `FortiOS(host='...', username='admin', password='...')`

### Improved

- **Type Safety**: Reduced type ignores from 4 to 1 in core fortios.py
  - Added protocol method stubs to IHTTPClient interface
  - Eliminated type: ignore[attr-defined] suppressions
  - Only architectural async type ignore remains
  - Better IDE support and type inference- **Firewall Policy Convenience Wrapper**: Intuitive interface for policy management
  - Access via `fgt.firewall.policy` namespace
  - Methods: `create()`, `update()`, `get()`, `delete()`, `exists()`, `enable()`, `disable()`, `move()`, `clone()`
  - 150+ explicit parameters matching FortiOS terminology
  - Comprehensive documentation in `docs/FIREWALL_POLICY_WRAPPER.md`

### Changed

- **Connection Pool Defaults Optimized**: Based on multi-device performance testing
  - `max_connections`: Reduced from 100 → 30 → **10** (conservative default)
  - `max_keepalive_connections`: Reduced from 20 → 15 → **5** (conservative default)
  - Defaults set 50% below lowest-performing device tested
  - Tested across 3 FortiGate models with varying performance characteristics
  - Use `fgt.api.utils.performance_test()` to get device-specific recommendations
  - Performance testing shows most FortiGates serialize API requests internally
  - Sequential requests recommended for most deployments

### Fixed

- **Connection Pool Validation**: Auto-adjust instead of error
  - Changed from hard error to auto-adjust when `max_keepalive_connections > max_connections`
  - Logs warning and adjusts `max_keepalive_connections` to match `max_connections`
  - Allows testing different concurrency levels without configuration errors

## [0.3.16] - 2025-12-20

### Added

- **Read-Only Mode**: Protect production environments by blocking write operations
  - Add `read_only=True` flag to FortiOS constructor to prevent accidental changes
  - Blocks all POST, PUT, and DELETE requests with `ReadOnlyModeError` exception
  - GET requests execute normally for queries and monitoring
  - Perfect for testing automation scripts, CI/CD pipelines, dry-run previews, and training environments
  - Works with both sync and async modes
  - Examples:
    ```python
    # Enable read-only mode for safe testing
    fgt = FortiOS("192.0.2.10", token="...", read_only=True)

    # GET requests work normally
    addresses = fgt.api.cmdb.firewall.address.get()  # ✓ Works

    # Write operations are blocked
    try:
        fgt.api.cmdb.firewall.address.post(data={"name": "test"})
    except ReadOnlyModeError as e:
        print(f"Blocked: {e}")  # ✗ Raises ReadOnlyModeError

    # Combine with operation tracking for audit trail
    fgt = FortiOS("fw", token="...", read_only=True, track_operations=True)
    # ... make API calls ...
    for op in fgt.get_operations():
        if op.get('blocked_by_read_only'):
            print(f"BLOCKED: {op['method']} {op['path']}")
    ```

- **Operation Tracking**: Complete audit log of all API operations
  - Add `track_operations=True` flag to enable operation logging
  - Records timestamp, method, URL, request data, response status, and VDOM for every API call
  - Access via `get_operations()` (all operations) or `get_write_operations()` (POST/PUT/DELETE only)
  - Tracks both successful operations and those blocked by read-only mode
  - Perfect for debugging, auditing, generating change logs, and documentation
  - Works with both sync and async modes
  - Examples:
    ```python
    # Enable operation tracking
    fgt = FortiOS("192.0.2.10", token="...", track_operations=True)

    # Make various API calls
    fgt.api.monitor.system.status.get()
    fgt.api.cmdb.firewall.address.post(data={"name": "test", "subnet": "10.0.0.1/32"})
    fgt.api.cmdb.firewall.policy.put("10", data={"action": "deny"})

    # Get all operations
    all_ops = fgt.get_operations()
    for op in all_ops:
        print(f"{op['timestamp']} {op['method']} {op['path']}")
    # Output:
    # 2024-12-20T10:30:15Z GET /system/status
    # 2024-12-20T10:30:16Z POST /firewall/address
    # 2024-12-20T10:30:17Z PUT /firewall/policy/10

    # Get only write operations (POST/PUT/DELETE)
    write_ops = fgt.get_write_operations()
    for op in write_ops:
        print(f"{op['method']} {op['path']}")
        if op['data']:
            print(f"  Data: {op['data']}")
    # Output:
    # POST /firewall/address
    #   Data: {'data': {'name': 'test', 'subnet': '10.0.0.1/32'}}
    # PUT /firewall/policy/10
    #   Data: {'name': '10', 'data': {'action': 'deny'}}
    ```

- **Extended Filter Documentation**: Comprehensive guide to FortiOS filter operators
  - New `FILTERING_GUIDE.md` with complete documentation of all FortiOS native filter operators
  - Covers all 8 operators: `==`, `!=`, `=@`, `!@`, `<`, `<=`, `>`, `>=`
  - 50+ practical examples for firewall addresses, policies, interfaces, and routes
  - Advanced patterns: range queries, exclusions, combined filters, pagination
  - Tips and best practices for efficient filtering
  - Examples:
    ```python
    # Equality
    fgt.api.cmdb.firewall.address.get(filter="name==test-host")

    # Contains (substring match)
    fgt.api.cmdb.firewall.address.get(filter="subnet=@10.0")

    # Range query
    fgt.api.cmdb.firewall.policy.get(filter="policyid>=100&policyid<=200")

    # Multiple conditions (AND logic)
    fgt.api.cmdb.firewall.policy.get(filter="status==enable&action==accept")

    # Not contains (exclusion)
    fgt.api.cmdb.firewall.address.get(filter="subnet!@192.168")
    ```

- **Username/Password Authentication**: Alternative authentication method for FortiOS devices
  - Session-based authentication using username and password (alternative to API tokens)
  - Automatic login on initialization, automatic logout on context manager exit
  - Context manager support for automatic session cleanup: `with FortiOS(username="admin", password="***") as fgt:`
  - Proactive session refresh to prevent idle timeout expiration
  - Configurable session idle timeout (default: 5 minutes, matching FortiGate defaults)
  - Automatic re-authentication on 401 errors if session expires
  - Session tracking with last activity timestamps
  - **⚠️ Deprecation Notice**: Username/password authentication **still works in FortiOS 7.4.x** but is **removed in FortiOS 7.6.x and later**. Fortinet recommends using API token authentication for all new deployments. See [FortiOS 7.4 Release Notes](https://docs.fortinet.com/document/fortigate/7.4.0/fortios-release-notes).
  - **Important**: Proactive re-authentication only works with context manager (`with` statement). Without context manager, you must manually manage login/logout.
  - **Note**: The idle timer resets on each API request. Proactive re-auth triggers when time since *last request* exceeds the threshold (not time since login).
  - Examples:
    ```python
    # Recommended: Context manager (automatic login/logout + proactive re-auth)
    with FortiOS(host="fw", username="admin", password="***") as fgt:
        addresses = fgt.api.cmdb.firewall.address.get()
        # Session automatically refreshed if approaching timeout
        # Auto-logout on exit

    # Custom timeout (match your FortiGate's remoteauthtimeout setting)
    with FortiOS(host="fw", username="admin", password="***",
                 session_idle_timeout=120) as fgt:  # 2 minutes
        # Proactive re-auth at 96 seconds (80% of 120s)
        status = fgt.api.monitor.system.status.get()

    # Disable proactive re-authentication
    with FortiOS(host="fw", username="admin", password="***",
                 session_idle_timeout=None) as fgt:
        # Will only re-auth on 401 errors
        addresses = fgt.api.cmdb.firewall.address.get()
    ```
  - Implementation details:
    - Login via POST to `/logincheck` with `secretkey` parameter (FortiOS convention)
    - CSRF token extracted from `ccsrftoken` cookie
    - Session cookies managed automatically by httpx client
    - Logout via POST to `/logout` (clears session, sets cookies to expire in 1976)
    - Proactive re-auth triggered at 80% of idle timeout (before expiration)
    - Fallback re-auth on 401 Unauthorized responses
    - Session timestamps: `_session_created_at`, `_session_last_activity`

- **Firewall Policy Convenience Wrapper**: Intuitive, GUI-like interface for managing firewall policies
  - Access via `fgt.firewall.policy` namespace with explicit parameter names
  - Simplified syntax: `fgt.firewall.policy.create(name='MyPolicy', srcintf=['port1'], ...)` instead of complex REST API calls
  - Auto-normalizes inputs: accepts strings or lists, converts to FortiOS format automatically
  - Full CRUD operations: `.create()`, `.update()`, `.get()`, `.delete()`, `.exists()`
  - Convenience methods: `.enable()`, `.disable()`, `.move()`, `.clone()`
  - Supports all 100+ firewall policy parameters from FortiOS 7.6.5 API
  - Works with both sync and async modes
  - Examples:
    ```python
    # Create policy with intuitive syntax
    fgt.firewall.policy.create(
        name='Allow-Web',
        srcintf=['port1'],
        dstintf=['port2'],
        srcaddr=['internal-net'],
        dstaddr=['all'],
        service=['HTTP', 'HTTPS'],
        action='accept',
        nat='enable'
    )

    # Enable/disable policies
    fgt.firewall.policy.disable(policy_id=10)
    fgt.firewall.policy.enable(policy_id=10)

    # Move policy
    fgt.firewall.policy.move(policy_id=5, position='before', reference_id=3)

    # Clone policy with modifications
    fgt.firewall.policy.clone(policy_id=1, new_name='Cloned-Policy')
    ```

## [0.3.15] - 2025-12-20

### Added

- **Async/Await Support**: Full dual-mode support for asynchronous operations
  - Single `FortiOS` class now supports both sync and async modes via `mode` parameter
  - All 750+ API methods work transparently in async mode with `await`
  - All 288 `.exists()` helper methods are async-aware
  - Async context manager support with `async with`
  - Zero breaking changes - existing sync code continues to work
  - Implementation:
    - New `AsyncHTTPClient` class mirroring sync `HTTPClient` with async/await
    - `mode="async"` parameter on `FortiOS.__init__()`
    - Automatic coroutine detection using `inspect.iscoroutine()`
    - Type hints with `@overload` decorators for IDE support
  - Performance: Enables concurrent operations with `asyncio.gather()` for 3x+ speedup
  - See [ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ASYNC_GUIDE.md) for complete documentation

- **Helper Methods**: Added `.exists()` helper method to 288 CMDB endpoints
  - Provides safe existence checking without raising exceptions
  - Returns `True` if object exists, `False` if not found
  - Works transparently in both sync and async modes
  - Available on all endpoints that support full CRUD operations
  - Example (sync): `if fgt.api.cmdb.firewall.address.exists("test-host"): ...`
  - Example (async): `if await fgt.api.cmdb.firewall.address.exists("test-host"): ...`
  - See [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md) for complete API reference

### Changed

- **Code Refactoring**: Eliminated code duplication in HTTP client implementation
  - Created `BaseHTTPClient` base class with shared logic for sync and async clients
  - `HTTPClient` and `AsyncHTTPClient` now inherit from `BaseHTTPClient`
  - Removed 744 lines of duplicated code (35% reduction in HTTP client code)
  - Zero duplication between sync and async implementations
  - Improved maintainability: bug fixes now apply to both sync and async modes automatically
  - Better consistency: retry logic, circuit breaker, and validation identical across modes
  - Enhanced testability: shared logic tested once in base class
  - Implementation:
    - `BaseHTTPClient`: Parameter validation, URL building, retry logic, circuit breaker, statistics
    - `HTTPClient`: Sync-specific HTTP operations (httpx.Client)
    - `AsyncHTTPClient`: Async-specific HTTP operations (httpx.AsyncClient)
  - Created `IHTTPClient` Protocol interface for extensibility
  - Updated 863 endpoint files to use Protocol-based type hints
  - Enables users to provide custom HTTP client implementations

### Fixed

- **Test Fixes**: Fixed certificate/local test helper methods to properly filter by source
  - Updated `test_get_factory_helper()` and `test_get_user_helper()` to use correct filters
  - Added `filter='source==factory'` and `filter='source==user'` parameters
  - All 9 certificate/local tests now pass correctly

### Documentation

- **Async Guide**: Created comprehensive [ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ASYNC_GUIDE.md) documentation
  - Complete async/await usage guide with examples
  - Common patterns: concurrent requests, bulk operations, error handling
  - Migration guide from sync to async
  - Performance comparisons and best practices
  - Advanced usage: rate limiting, timeouts, multiple FortiGates
  - Troubleshooting common async errors
- **API Reference**: Created comprehensive [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md) documentation
  - Complete listing of all 857 FortiOS API endpoints
  - Shows available methods (`.get()`, `.post()`, `.put()`, `.delete()`, `.exists()`) for each endpoint
  - Organized by API category (CMDB, LOG, MONITOR, SERVICE)
  - Quick navigation with anchor links to all subcategories
  - Coverage: 561 CMDB endpoints, 19 LOG endpoints, 274 MONITOR endpoints, 3 SERVICE endpoints
- **Helper Methods**: Added `.exists()` helper method documentation in [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md)
  - In-depth guide to the `.exists()` helper method
  - Practical usage examples for common scenarios (idempotent operations, safe deletion, batch processing)
  - Reference table of identifier types for all 288 endpoints with `.exists()`
  - Organized by category with example code snippets
- **README Updates**: Improved documentation organization
  - Updated documentation links to use GitHub URLs for PyPI compatibility
  - Added [docs/ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ASYNC_GUIDE.md) and [docs/ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/docs/ENDPOINT_METHODS.md) to main documentation section
  - Updated roadmap to mark async support as completed (v0.3.15)
  - Added async/await to features list
  - Improved discoverability for PyPI users
- **QUICKSTART Updates**: Added async/await section
  - Quick example of async mode usage
  - Link to comprehensive ASYNC_GUIDE.md
  - Updated tips section to mention async for concurrent operations
- **Project Cleanup**: Cleaned up root folder and updated documentation
  - Moved refactoring documentation to internal development workspace
  - Removed `update_endpoints.py` (one-time migration script)
  - Updated `CHANGELOG.md` with comprehensive refactoring details
  - Updated `README.md` to highlight refactored architecture

## [0.3.14] - 2025-12-19

### Fixed

- **Critical**: Fixed httpx dependency in requirements.txt (was incorrectly listing requests/urllib3)
  - Package now correctly declares httpx[http2]>=0.27.0 as dependency
  - Resolves installation issues where wrong HTTP library was installed
- **Build**: Updated MANIFEST.in to reflect moved development docs
  - Commented out CONTRIBUTING.md and DEVELOPMENT.md (moved to development workspace)
  - Prevents build warnings about missing files
- **Type Checking**: Fixed mypy configuration for Python 3.10+ syntax
  - Updated pyproject.toml: python_version = "3.10" (was "3.8")
  - Added httpx module ignore for missing type stubs
  - Fixes compatibility with modern union syntax (str | None)

### Added

- **PEP 561 Compliance**: Full type checker support for hfortix package
  - ✅ `py.typed` marker file included in package
  - ✅ All public APIs have complete type hints
  - ✅ mypy/pyright can now validate user code using hfortix
  - ✅ IDE autocomplete with full type information
  - Benefits: Catch type errors at development time, better developer experience
  - Example: Type checkers now understand `fgt.api.cmdb.firewall.address.get()` returns `dict[str, Any]`
- **Public API**: Added `get_connection_stats()` method to FortiOS class
  - Monitor HTTP connection pool health and performance
  - Track retry statistics by reason and endpoint
  - Access circuit breaker state and failure counts
  - Example: `stats = fgt.get_connection_stats()`
- **Exception Exports**: Exported all 16 exception classes from main hfortix package
  - Complete exception hierarchy now available: `from hfortix import CircuitBreakerOpenError, ...`
  - Added 10 new exception exports: ServiceUnavailableError, CircuitBreakerOpenError, TimeoutError, DuplicateEntryError, EntryInUseError, InvalidValueError, PermissionDeniedError
  - Exported helper functions: get_error_description(), raise_for_status()
  - Exported data structures: FORTIOS_ERROR_CODES, HTTP_STATUS_CODES

### Changed

- **Python Version Requirement**: Updated minimum Python version from 3.8 to 3.10
  - Code uses Python 3.10+ syntax (str | None union types)
  - Updated pyproject.toml: requires-python = ">=3.10"
  - Removed Python 3.8, 3.9 from classifiers
  - Added "Typing :: Typed" classifier for PEP 561 compliance
- **Development Status**: Updated from Alpha (3) to Beta (4)
  - Package metadata now consistently declares Beta status
  - Updated in setup.py, pyproject.toml classifiers
  - Reflects maturity of codebase and API stability
- **Documentation**: Updated API_COVERAGE.md to reflect 100% coverage achievement
  - Changed from "38/77 (49%)" to "77/77 (100%)"
  - Added celebration section for milestone achievement
  - Updated test coverage statistics (226 test files)
- **Documentation**: Removed broken internal development references from README.md
  - Cleaned up references to development workspace content

### Notes

- Version synchronized across setup.py (0.3.14), pyproject.toml (0.3.14), and hfortix/FortiOS/__init__.py (0.3.14)
- All changes are backward compatible
- PEP 561 compliance makes hfortix a first-class typed Python package
- This release prepares the package for broader beta testing

## [Unreleased]

### Added

- **🎉 100% API COVERAGE ACHIEVED** (December 2025) - **Complete FortiOS 7.6.5 implementation!**
  - **CMDB API**: All 37 documented categories (100% coverage)
    - **Refactored**: alertemail, antivirus, application, authentication, automation, casb, certificate, dlp, dnsfilter, emailfilter, firewall, icap, ips, log, monitoring, report, router, rule, system (19 categories)
    - Complete categories: diameter-filter, endpoint-control, ethernet-oam, extension-controller, file-filter, ftp-proxy, sctp-filter, switch-controller, user, videofilter, virtual-patch, voip, vpn, waf, web-proxy, webfilter, wireless-controller, ztna (18 categories)
    - Note: ssh-filter, telemetry-controller, wanopt, extender-controller not yet documented on FNDN
  - **Monitor API**: All 32 documented categories (100% coverage)
    - **Previously implemented**: azure, casb, endpoint-control, extender-controller, extension-controller, firewall (6 categories)
    - **Added in this session**: firmware, fortiguard, fortiview, geoip, ips, license, log, network, registration, router, sdwan, service, switch-controller, system, user, utm, videofilter, virtual-wan, vpn, vpn-certificate, wanopt, web-ui, webcache, webfilter, webproxy, wifi (26 categories)
  - **Log API**: 5 categories (100% coverage) - disk, fortianalyzer, memory, forticloud, search
  - **Service API**: 3 categories (100% coverage) - sniffer, security-rating, system
  - **Total**: 77 of 77 documented categories with 750+ API methods
  - **Generated via unified module generator** with automatic edge case handling
  - **Status**: All endpoints generated, ~50% tested with live FortiGate
  - **Quality**: All follow standardized dual-pattern interface with full type hints

- **Router CMDB Category** - Complete routing protocol configuration support (BETA)
  - Implemented all 26 router endpoints with full CRUD operations
  - Collection endpoints: static, static6, access-list, access-list6, prefix-list, prefix-list6, route-map, policy, policy6, aspath-list, community-list, extcommunity-list, key-chain, auth-path, multicast, multicast6, multicast-flow
  - Singleton endpoints: bgp, ospf, ospf6, rip, ripng, isis, bfd, bfd6, setting
  - Comprehensive test coverage: 22/26 endpoints tested (85%), 100% pass rate
  - **Note:** Singleton endpoints (BGP, OSPF, RIP, etc.) require GET→Modify→PUT pattern for nested objects

### Changed

- **🔄 MAJOR API REFACTORING** (December 2025) - **All 500+ endpoints refactored**
  - **Breaking Change**: Standardized method names across all endpoints
  - **Old API**: `create()`, `update()`, `delete()` - required manual `mkey` parameter handling
  - **New API**: `list()`, `get()`, `create()`, `update()`, `delete()` - RESTful and intuitive
  - **Dual-Pattern Interface**: All `create()` and `update()` methods now support:
    - Dictionary pattern: `create(data_dict={'name': 'x', 'subnet': '10.0.0.0/24'})`
    - Keyword pattern: `create(name='x', subnet='10.0.0.0/24')`
    - Mixed pattern: `create(data_dict=base_config, name='override')`
  - **Benefits**: Cleaner code, better IDE autocomplete, template-friendly, more Pythonic
  - **Migration**: Old code will break - update `create(data)` → `create(data_dict=data)`
  - **Scope**: All 37 CMDB categories + 32 Monitor categories refactored with unified generator
  - **Scope**: 200+ endpoints across 24 CMDB categories refactored
  - **Status**: ~85% complete, router endpoints verified with comprehensive tests

- **Repository Organization** (December 19, 2025)
  - Moved development tools (CONTRIBUTING.md, DEVELOPMENT.md) to development workspace
  - Cleaned up public documentation to focus on user-facing content
  - Simplified README.md contributing section
  - Updated all documentation cross-references

- **Module Naming Improvements** (December 19, 2025)
  - Fixed invalid Python identifiers: renamed `3g_modem` → `modem_3g`, `5g_modem` → `modem_5g`
  - Module classes: `Modem3g`, `Modem5g` with proper attribute access
  - Test files updated to match new naming convention
  - All modem tests now passing

- **Development Workflow** (December 19, 2025)
  - Created unified module generator handling all edge cases automatically
  - Auto-detects digit-prefixed names and sanitizes to valid Python identifiers
  - Auto-adds certificate helper methods for certificate endpoints
  - Generates nested resource classes for complex endpoints
  - Detects read-only endpoints and generates appropriate methods
  - Consolidated all generation tools into single location
  - All new modules follow standardized dual-pattern interface

- **Singleton Endpoint Pattern** - Important behavioral note for routing protocols
  - Routing protocol endpoints (BGP, OSPF, RIP, ISIS, etc.) work differently than other endpoints
  - Unlike firewall addresses or policies, you cannot add/remove individual neighbors or networks
  - Instead, you must retrieve the entire configuration, make changes, and send it back
  - This requires more code than typical CRUD operations (see README examples)
  - **Why?** FortiOS API design - routing configs are single objects with nested lists
  - **Future:** Helper methods like `add_neighbor()`, `remove_neighbor()` are planned to simplify this

## [0.3.13] - 2025-12-17

### Added

- **Custom User-Agent Header** - Identify applications in FortiGate logs
  - Configure via `user_agent` parameter in `FortiOS()` constructor
  - Default: `hfortix/{version}` if not specified
  - Useful for multi-team environments and troubleshooting
  - Shows up in FortiGate admin logs for better visibility
  - Example: `FortiOS(host='...', token='...', user_agent='BackupScript/2.1.0')`

- **New Exception Classes** - Better error handling and type safety
  - `ServiceUnavailableError` - HTTP 503 service unavailable
  - `CircuitBreakerOpenError` - Circuit breaker is open (replaces generic RuntimeError)
  - `TimeoutError` - Request timeout errors
  - More specific exceptions for better error handling

- **Configurable Circuit Breaker** - Customize circuit breaker behavior
  - `circuit_breaker_threshold` - Number of failures before opening (default: 5)
  - `circuit_breaker_timeout` - Seconds before transitioning to half-open (default: 60.0)
  - Configure per FortiGate size/environment
  - Example: `FortiOS(host='...', circuit_breaker_threshold=10, circuit_breaker_timeout=120.0)`

- **Configurable Connection Pool** - Tune connection limits
  - `max_connections` - Maximum connections in pool (default: 100)
  - `max_keepalive_connections` - Maximum keepalive connections (default: 20)
  - Adjust for small embedded FortiGates or large enterprise models
  - Example: `FortiOS(host='...', max_connections=50, max_keepalive_connections=10)`

- **Enhanced Retry Statistics** - More detailed metrics
  - `total_requests` - Total number of requests made
  - `successful_requests` - Number of successful requests
  - `failed_requests` - Number of failed requests
  - `last_retry_time` - Timestamp of last retry
  - `success_rate` - Percentage of successful requests (0-100)
  - Better visibility into client performance

- **Advanced Wildcard Matching** - fnmatch support for endpoint timeouts
  - Supports shell-style patterns: `monitor/*`, `*/status`, `monitor/*/interface`
  - More flexible than simple prefix matching
  - Exact match still takes priority over patterns

### Changed

- **Enhanced Parameter Sanitization** - Security improvement
  - Now sanitizes query parameters in addition to request data
  - Prevents leaking API keys, tokens, passwords in logs
  - Added more sensitive key patterns: `api_key`, `api-key`, `apikey`, `auth`, `authorization`
  - Improves security for production logging

- **Parameter Validation** - Fail fast with clear errors
  - Validates `max_retries` (must be >= 0, warns if > 100)
  - Validates `connect_timeout` and `read_timeout` (must be > 0)
  - Validates `circuit_breaker_threshold` (must be > 0)
  - Validates `max_connections` and `max_keepalive_connections` (must be > 0)
  - Validates `host` parameter is required (no longer accepts None)
  - Better error messages for invalid configurations

- **Code Quality Improvements**
  - Reduced code duplication with `_normalize_path()` helper method
  - Improved type hints for `__exit__()` method
  - Enhanced docstrings with examples
  - Better logging consistency

### Fixed

- **Integer ID Path Encoding** - Fixed URL encoding for numeric IDs
  - `dos_policy.get()`, `dos_policy.update()`, `dos_policy.delete()` - Convert policyid to string before encoding
  - `dos_policy6.get()`, `dos_policy6.update()`, `dos_policy6.delete()` - Convert policyid to string before encoding
  - `ipmacbinding.table.get()`, `ipmacbinding.table.update()`, `ipmacbinding.table.delete()` - Convert seq_num to string before encoding
  - Resolves `TypeError: quote_from_bytes() expected bytes` when using numeric IDs
  - All numeric identifiers are now properly converted to strings for URL path encoding

- **Type Safety** - Fixed type checking errors
  - `host` parameter properly validated (no longer Optional in practice)
  - Better type hints for exception handling
  - Cleaner type checking for HTTPClient initialization

### Technical Details

- **100% backwards compatible** - all existing code works unchanged
- Test coverage: 28 tests (all passing)
- Zero breaking changes - all improvements are additive or internal

## [0.3.13] - 2025-12-17 (if releasing the v0.3.13 from earlier)

### Added

- **Request ID / Correlation Tracking** - Track requests across logs for better debugging
  - Auto-generates short 8-character UUID if not provided
  - Support for custom correlation IDs via `request_id` parameter
  - Request ID appears in all log entries for full traceability
  - Enables distributed tracing across multiple systems

- **Connection Pool Metrics** - Monitor HTTP client health and performance
  - `get_connection_stats()` method returns pool health metrics
  - Track: HTTP/2 status, max connections, circuit breaker state, failures
  - Enable proactive monitoring and alerting
  - Zero performance overhead

- **Circuit Breaker Pattern** - Prevent cascading failures with automatic fail-fast
  - Opens after 5 consecutive failures (configurable)
  - Automatically enters half-open state after 60s timeout
  - Manual reset via `reset_circuit_breaker()` method
  - Clear error messages with time-until-retry
  - Protects downstream services from overload

- **Per-Endpoint Timeout Configuration** - Fine-grained timeout control
  - `configure_endpoint_timeout(pattern, timeout)` for custom timeouts
  - Supports wildcard patterns: `monitor/*`, `log/*/report`
  - Exact match takes priority over wildcard
  - Ideal for slow endpoints (reports, large policy lists)
  - Zero overhead if not configured

- **Structured Logging** - Machine-readable logs with extra fields
  - All log entries include: request_id, method, endpoint, status_code, duration, vdom
  - Compatible with JSON log formatters (Elasticsearch, Splunk, CloudWatch)
  - Enables log aggregation and analysis
  - Better troubleshooting with correlation
  - Same performance as string logging

### Technical Details

- All features are **100% backwards compatible** - no breaking changes
- Comprehensive test coverage: 13 new tests in `test_advanced_features.py`
- Total test suite: 24 tests (4 retry + 7 improvements + 13 advanced)
- Performance: Minimal overhead (~0.001ms per request for circuit breaker)

## [0.3.12] - 2025-12-17

### Changed

- **BREAKING: Migrated from requests to httpx** - Complete HTTP client library migration
  - Replaced `requests` library with modern `httpx` library
  - **HTTP/2 Support Enabled** - Improved performance with connection multiplexing
  - More explicit timeout configuration using `httpx.Timeout` object
  - Connection pooling: 100 max connections, 20 keepalive connections
  - Updated exception handling:
    * `ConnectionError` → `httpx.ConnectError, httpx.NetworkError`
    * `Timeout` → `httpx.ReadTimeout, httpx.WriteTimeout, httpx.PoolTimeout, httpx.ConnectTimeout`
    * `requests.HTTPError` → `httpx.HTTPStatusError`
  - Response API changes: `response.ok` → `response.is_success`
  - Requires: `httpx[http2]>=0.27.0` (previously `requests>=2.31.0`)
  - **No API Changes**: All 644 endpoint methods work unchanged
  - Better foundation for future async support

### Added

- **Automatic Retry Logic** - HTTPClient now automatically retries failed requests with exponential backoff
  - Retries on transient failures: connection errors, timeouts, rate limits (429), server errors (500, 502, 503, 504)
  - Configurable via `max_retries` parameter (default: 3 attempts)
  - Exponential backoff: 1s, 2s, 4s, 8s (capped at 30s)
  - Respects `Retry-After` header for rate limit responses
  - Detailed retry logging at INFO level
  - Improves reliability in unstable network conditions

- **Context Manager Support** - HTTPClient can now be used with `with` statement
  - Automatically closes client on exit: `with HTTPClient(...) as client:`
  - Ensures proper resource cleanup
  - Implements `__enter__` and `__exit__` methods

- **Enhanced Documentation**
  - Query parameter encoding behavior documented in class docstring
  - Timeout configuration explained with detailed examples
  - Path encoding strategy documented (safe='/%' prevents double-encoding)
  - Binary error response handling documented

### Fixed

- **URL Normalization** - Base URL now has trailing slashes stripped during initialization
  - Prevents potential double-slash issues like `https://host//api/v2/...`
  - Ensures consistent URL construction across all requests

- **HTTP Client Path Normalization** - Fixed 404 errors when endpoint methods pass paths with leading slashes
  - HTTPClient now strips leading slashes from paths before URL construction
  - Prevents double-slash URLs (e.g., `/api/v2/monitor//firewall/acl`)
  - Backwards compatible: works with both `"firewall/acl"` and `"/firewall/acl"` path formats
  - Affects `request()` and `get_binary()` methods
  - Resolves `ResourceNotFoundError` for monitor endpoints like `firewall.acl.list()`

- **Path Encoding Implementation** - Paths are now properly URL-encoded
  - Special characters in paths are encoded (e.g., spaces → `%20`, `@` → `%40`)
  - Safe characters: `/` (path separator) and `%` (already-encoded marker)
  - Prevents double-encoding of pre-encoded components
  - Example: `"user@domain"` → `"user%40domain"`

- **Binary Response Error Handling** - Improved error handling for non-JSON responses
  - Added try/except around JSON parsing in `_handle_response_errors()`
  - Falls back to standard HTTP error for binary/HTML error pages
  - Logs response size for debugging
  - Handles proxy/firewall error pages gracefully

- **Rate Limit Handling** - HTTP 429 responses now properly handled with retry logic
  - Respects `Retry-After` header from server
  - Falls back to exponential backoff if header not present
  - Prevents overwhelming servers during rate limiting

## [0.3.11] - 2025-12-17

### Added - December 17, 2025

- **FTP Proxy Category** - FTP proxy configuration (1 endpoint):
  - **explicit** - FTP proxy explicit configuration (GET, PUT)
  - Parameters: status, incoming_port, incoming_ip, outgoing_ip, sec_default_action, server_data_mode
  - SSL/TLS support: ssl, ssl_cert, ssl_dh_bits, ssl_algorithm
  - Singleton endpoint pattern (no POST/DELETE operations)
  - Test coverage: 5 test sections with comprehensive parameter validation

- **Monitor API Categories** - 6 categories implemented (18% coverage):
  - **azure/** - Azure application list monitoring (1 endpoint)
  - **casb/** - SaaS application statistics (1 endpoint)
  - **endpoint-control/** - FortiClient EMS monitoring (7 endpoints):
    - ems-status, ems-status-summary, installer, profile-xml
    - record-list, registration-password, summary
  - **extender-controller/** - FortiExtender status monitoring (1 endpoint)
  - **extension-controller/** - Extension controller status (2 endpoints):
    - extender, fortigate
  - **firewall/** - Firewall monitoring (39 endpoints):
    - Policy statistics (policy, policy6, proxy-policy, security-policy, etc.)
    - Session monitoring with 20+ filter parameters
    - ACL counters (acl, acl6) with clear operations
    - Address objects (address, address6, address-dynamic, address-fqdn)
    - Traffic shapers (per-ip-shaper, shaper, multi-class-shaper)
    - Special endpoints (policy-lookup callable, clearpass-address actions)
    - GTP statistics, health monitoring, load balancing
    - Internet service matching and reputation
    - VIP overlap detection, UUID objects
  - Test coverage: 39 firewall tests with 100% pass rate
  - All endpoints support explicit parameters (no **kwargs)

- **Log Configuration Category** - Complete logging configuration (56 endpoints):
  - Nested object pattern: `fgt.api.cmdb.log.disk.filter.get()`
  - **disk/** - Disk logging (filter, setting)
  - **memory/** - Memory logging (filter, global-setting, setting)
  - **fortianalyzer-cloud/** - FortiAnalyzer Cloud (4 endpoints)
  - **fortianalyzer/** - FortiAnalyzer 1/2/3 servers (12 endpoints total)
  - **fortiguard/** - FortiGuard logging (4 endpoints)
  - **null-device/** - Null device logging (filter, setting)
  - **syslogd/** - Syslog servers 1/2/3/4 (16 endpoints total)
  - **tacacs+accounting/** - TACACS+ accounting 1/2/3 (6 endpoints total)
  - **webtrends/** - WebTrends logging (filter, setting)
  - **Singleton endpoints** - custom-field (CRUD), eventfilter, gui-display, setting, threat-weight
  - Test coverage: 12 test files, 47 test cases (100% pass rate)

- **ICAP Category** - Internet Content Adaptation Protocol (3 endpoints):
  - **profile** - ICAP profiles (30+ parameters)
  - **server** - ICAP server configuration with SSL/TLS support
  - **server-group** - ICAP server groups for load balancing

- **IPS Category** - Intrusion Prevention System (8 endpoints):
  - **custom** - Custom IPS signatures (CRUD)
  - **decoder** - Protocol decoders (CRUD)
  - **global** - Global IPS settings (singleton)
  - **rule** - IPS rules (CRUD)
  - **rule-settings** - IPS rule settings (CRUD)
  - **sensor** - IPS sensors/profiles (CRUD)
  - **settings** - VDOM IPS settings (singleton)
  - **view-map** - IPS view-map configuration (CRUD)

- **Monitoring Category** - System monitoring configuration (1 endpoint):
  - **npu-hpe** - NPU-HPE performance monitoring (3 parameters)

- **Report Category** - Report configuration (2 endpoints):
  - **layout** - Report layouts with CRUD (17 parameters)
  - **setting** - Report settings (5 parameters)

### Changed
- **Module Creation Prompt** - Added nested object pattern documentation
  - Complete examples of intermediate classes
  - Property decorators with lazy loading
  - Usage patterns for nested vs flat endpoints

### Improved
- **API Coverage** - Now at 48% overall (37 of 77 categories):
  - CMDB: 23 of 40 categories (57.5% - all beta)
  - Monitor: 6 of 33 categories (18% - all beta)
  - Log: 5 of 5 categories (100% - all beta)
  - Service: 3 of 3 categories (100% - all beta)
  - Total: 200+ endpoints, 250+ API methods
  - **Note:** All implementations remain in beta until v1.0.0

### Status
- **Beta Release** - All implementations are in beta status:
  - Functional and tested with real FortiGate devices
  - May have incomplete parameter coverage or undiscovered edge cases
  - Production-ready status (v1.0.0) requires comprehensive unit test coverage

### Planned
- Complete CMDB endpoint coverage (23 of 40 categories implemented)
- Monitor endpoints implementation (6 of 33 categories)
- Remaining Monitor categories: system, user, router, vpn, network, etc.
- FortiManager module
- FortiAnalyzer module
- Async support
- CLI tool
- Version 1.0.0: Comprehensive unit tests and production-ready status

## [0.3.10] - 2025-12-16

### Added
- **Configurable Timeouts** - HTTP timeout values are now customizable:
  - `connect_timeout`: Time to wait for connection establishment (default: 10.0 seconds)
  - `read_timeout`: Time to wait for response data (default: 300.0 seconds)
  - Configurable via `FortiOS()` constructor parameters
  - Useful for slow networks, international connections, or large operations
  - `max_retries`: Parameter added for future retry mechanism (default: 3)
- **URL Encoding Helper** - Centralized URL encoding for special characters:
  - New `encode_path_component()` function in `http_client.py`
  - Automatically encodes special characters in object names: `/`, `@`, `:`, spaces, etc.
  - Applied to all 145 CMDB endpoint files (84 path variables encoded)
  - Prevents URL parsing errors when object names contain special characters

### Fixed
- **URL Encoding for Special Characters** - Object names with special characters now work correctly:
  - Fixed issue where objects with `/` in names (e.g., `Test_NET_192.0.2.0/24`) caused 404 errors
  - Special characters are now properly encoded: `/` → `%2F`, `@` → `%40`, `:` → `%3A`, space → `%20`
  - Applies to all API operations: get, create, update, delete
  - Implemented as reusable helper function to avoid code duplication
  - Covers all path variables: `name`, `mkey`, `policyid`, `seq_num`, `member`

## [0.3.9] - 2025-12-16

### Added
- **raw_json Parameter** (100% Coverage) - All API methods now support raw_json parameter:
  - Default behavior: Returns just the results data
  - With `raw_json=True`: Returns complete API response with status codes, metadata
  - Coverage: 45+ methods across all CMDB, Log, and Service endpoints
  - Enables access to `http_status`, `status`, `serial`, `version`, `build` fields

- **Logging System** (Complete) - Comprehensive logging framework:
  - Global control: `hfortix.set_log_level('DEBUG'|'INFO'|'WARNING'|'ERROR'|'OFF')`
  - Per-instance control: `FortiOS(debug='info')`
  - 5 log levels with automatic sensitive data sanitization
  - Hierarchical loggers (`hfortix.http`, `hfortix.client`)
  - Request/response logging with timing information
  - Replaced all print() statements with proper logging

### Changed
- **Code Quality** - Applied comprehensive formatting and linting:
  - Black formatter applied to all 195 files (100% PEP 8 compliance)
  - isort applied to organize imports (86 files updated)
  - flake8 checks passed with max-complexity=10
  - All type hints verified
  - Removed all print() statements in production code (replaced with logging)

### Fixed
- **Bug Fixes** - Fixed multiple undefined variable errors:
  - `antivirus/profile.py`: Fixed 2 instances of undefined 'data' variable (lines 265, 451)
  - `certificate` helpers: Added raw_json parameter to import_p12() and other helper methods
  - `DoS Policy`: Fixed interface_data variable bugs in dos_policy.py and dos_policy6.py
  - `firewall` access-proxy: Fixed raw_json parameter placement in 6 files
  - Multiple service/shaper/ssh files: Fixed data→payload_dict variable name consistency

- **Test Fixes** - Updated test files to use raw_json=True where needed:
  - Fixed 159 test files to properly check API responses
  - Updated payload structures in multiple test files
  - Fixed syntax errors in certificate and firewall tests

## [0.3.8] - 2025-12-16

### Added
- **Dual-Pattern Interface** (100% Complete) - All 43 create/update methods now support:
  - Dictionary pattern: `create(data_dict={'name': 'x', 'param': 'y'})`
  - Keyword pattern: `create(name='x', param='y')`
  - Mixed pattern: `create(data_dict=base, name='override')`
  - Coverage: 38 CMDB endpoints + 5 Service methods

### Changed
- **Documentation**: Updated all docs with dual-pattern examples
  - README.md, QUICKSTART.md with usage examples

### Fixed
- `extension_controller`: Fixed fortigate_profile registration
- `firewall.ssl_setting`: Added missing typing imports
- `firewall.vendor_mac_summary`: Added get() method for singleton endpoint
- Test fixes for alertemail and proxy_addrgrp

## [0.3.7] - 2025-12-16

### Improved
- Packaging/layout cleanup to align with the canonical `hfortix/` package structure
- Additional FortiOS v2 endpoint modules (log/service/cmdb expansions)

## [0.3.6] - 2025-12-15

### Improved - IDE Autocomplete Experience 🎯

**Note:** This is an alpha release with internal refactoring for better developer experience.

#### Hidden Internal Methods for Cleaner Autocomplete
- **Generic CRUD methods renamed** - Methods moved to underscore prefix:
  - `cmdb.get()` → `cmdb._get()` (escape hatch for unmapped endpoints)
  - `cmdb.post()` → `cmdb._post()`
  - `cmdb.put()` → `cmdb._put()`
  - `cmdb.delete()` → `cmdb._delete()`
  - Similar changes for log, monitor, service modules
- **Benefit:** IDE now shows only endpoint-specific methods (create, update, list, etc.)
- **Migration:** If you use generic methods directly, add underscore prefix

#### Hidden Internal Client Attributes
- **Client internals renamed** - FortiOS client implementation details:
  - `fgt.session` → `fgt._session`
  - `fgt.url` → `fgt._url`
  - `fgt.verify` → `fgt._verify`
- **Public attributes unchanged:** `host`, `port`, `vdom`, `cmdb`, `monitor`, `log`, `service`
- **Benefit:** Cleaner autocomplete showing only user-facing API

#### Hidden Lazy-Loaded Property Cache
- **Firewall lazy loading internals** - Changed cache naming to double underscore
- **Affects:** 11 firewall endpoints (dos_policy, address, addrgrp, access_proxy, etc.)
- **Benefit:** IDE no longer shows internal cached attributes

### Added
- **`__all__` exports** - Explicit control over public API in all modules
- Better documentation and import suggestions

### Technical Details
- 79+ endpoint files updated to use underscore methods internally
- Follows Python naming conventions (single _ = internal, double __ = private)
- All endpoint-specific methods work as before (no breaking changes)
- All tests passing (8/8 for address, access_proxy)

## [0.3.5] - 2025-12-15

### Improved - IDE Autocomplete & Type Hints ✨

#### Developer Experience Enhancements
- **Added PEP 561 support** - Created `FortiOS/py.typed` marker file for better IDE type checking
- **Enhanced type hints** - Added explicit type annotations to all API helper classes
  - `self.cmdb: CMDB` - Full autocomplete for CMDB endpoints
  - `self.firewall: Firewall` - Full autocomplete for firewall endpoints
  - All 16 CMDB categories now have proper type hints
- **Improved `__all__` exports** - Better module discovery and import suggestions
- **Updated setup.py** - Added `package_data` for py.typed and "Typing :: Typed" classifier
- **Fixed duplicate assignments** - Removed redundant initialization in CMDB `__init__.py`

#### Documentation Improvements
- Added comprehensive docstrings explaining API helper class attributes
- Clarified purpose of generic methods (advanced/fallback usage)
- Better examples in class docstrings

### Technical Details
- Type hints now work correctly in VS Code, PyCharm, and other PEP 561-compliant IDEs
- Autocomplete shows all available endpoints when typing `fgt.api.cmdb.firewall.`
- Method signatures display parameter types and return types
- No breaking changes - fully backward compatible

## [0.3.4] - 2025-12-15

### Documentation - Unified Import Syntax 📚

#### Updated All Documentation
- **README.md** - Changed all examples to use `from hfortix import FortiOS`
- **QUICKSTART.md** - Updated import patterns and all code examples
- **Added PyPI badges** - Version, Python 3.8+, MIT license
- **Status updates** - FortiOS "✅ Active", FortiManager/FortiAnalyzer "⏸️ Planned"

### Technical Details
- All documentation now reflects the unified package import structure
- Installation instructions prioritize PyPI method
- 190 insertions, 78 deletions across documentation files

## [0.3.3] - 2025-12-15

### Added - Unified Package Import Structure 📦

#### Package Restructuring
- **Created `hfortix.py`** - Main module for unified imports
- **Enable `from hfortix import FortiOS`** - Clean import syntax
- **Backward compatible** - Old imports still work
- **Updated `__init__.py`** - Changed from relative to absolute imports

### Technical Details
- Added `py_modules=['hfortix', 'exceptions', 'exceptions_forti']` to setup.py
- Package now supports both import styles:
  - Recommended: `from hfortix import FortiOS`
  - Also works: `from FortiOS import FortiOS`

## [0.3.2] - 2025-12-15

### Fixed - Package Distribution 🔧

#### Resolved Import Errors
- **Fixed ModuleNotFoundError** - Added root-level modules to package
- **Updated setup.py** - Added `py_modules` configuration
- **Included exceptions modules** - Both `exceptions.py` and `exceptions_forti.py` now in package

### Technical Details
- Root-level Python modules now properly included in wheel and sdist
- No code changes needed - pure packaging fix

## [0.3.1] - 2025-12-15

### Fixed - Import Error Handling 🛠️

#### Exception Module Imports
- **Added fallback imports** - Better handling for missing exception modules
- **Enhanced FortiOS/exceptions.py** - Try/except blocks for imports
- **Fallback exceptions defined** - Basic exception classes if imports fail

### Technical Details
- Partial fix for import issues (fully resolved in 0.3.2)

## [0.3.0] - 2025-12-14

### Added - Firewall Flat Endpoints + Sub-categories! 🎉

#### New Flat Firewall Endpoints (6 endpoints)
Implemented DoS protection and access proxy endpoints with simplified API:

- **firewall/DoS-policy** - IPv4 DoS protection policies
  - Full CRUD operations with automatic type conversion
  - Comprehensive anomaly detection (18 types with default thresholds)
  - Simplified API: `interface='port3'` → `{'q_origin_key': 'port3'}`
  - Test coverage: 8/8 tests passing (100%)

- **firewall/DoS-policy6** - IPv6 DoS protection policies
  - Same features as DoS-policy for IPv6
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy** - IPv4 reverse proxy/WAF
  - Full CRUD with 16+ configuration parameters
  - VIP integration (requires type="access-proxy")
  - Server pool multiplexing support
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy6** - IPv6 reverse proxy/WAF
  - Same features as access-proxy for IPv6
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy-ssh-client-cert** - SSH client certificates
  - Certificate-based SSH authentication
  - Permit controls (agent forwarding, port forwarding, PTY, X11, user RC)
  - Test coverage: 8/8 tests passing (100%)

- **firewall/access-proxy-virtual-host** - Virtual host configuration
  - Domain/wildcard/regex host matching
  - SSL certificate management with automatic list conversion
  - Test coverage: 8/8 tests passing (100%)

**Total Test Coverage:** 48/48 tests (100% pass rate)

**Key Features:**
- **Simplified API** - Automatic type conversion for better UX
  - String → dict: `'port3'` → `{'q_origin_key': 'port3'}`
  - String list → dict list: `['HTTP']` → `[{'name': 'HTTP'}]`
  - Certificate string → list: `'cert'` → `[{'name': 'cert'}]`
- **Comprehensive Documentation** - Anomaly detection types with thresholds
- **Prerequisites Documented** - VIP types, certificates, CAs
- **Lazy Loading** - @property pattern for optimal performance

#### CMDB Category: Firewall Sub-categories (17 endpoints, 7 sub-categories)
Implemented nested/hierarchical structure for firewall endpoints with lazy-loading pattern:

- **firewall.ipmacbinding** (2 endpoints)
  - `setting` - IP/MAC binding global settings
  - `table` - IP/MAC binding table entries

- **firewall.schedule** (3 endpoints)
  - `group` - Schedule groups
  - `onetime` - One-time schedules
  - `recurring` - Recurring schedules

- **firewall.service** (3 endpoints)
  - `category` - Service categories
  - `custom` - Custom service definitions
  - `group` - Service groups

- **firewall.shaper** (2 endpoints)
  - `per-ip-shaper` - Per-IP traffic shaping
  - `traffic-shaper` - Shared traffic shaping

- **firewall.ssh** (4 endpoints)
  - `host-key` - SSH proxy host public keys
  - `local-ca` - SSH proxy local CA
  - `local-key` - SSH proxy local keys (with PEM format support)
  - `setting` - SSH proxy settings

- **firewall.ssl** (1 endpoint)
  - `setting` - SSL proxy settings (timeout, DH bits, caching)

- **firewall.wildcard-fqdn** (2 endpoints)
  - `custom` - Wildcard FQDN addresses (e.g., *.example.com)
  - `group` - Wildcard FQDN groups

### Technical Improvements
- ✅ Nested API structure: `fgt.api.cmdb.firewall.[subcategory].[endpoint]`
- ✅ Lazy-loading with @property methods
- ✅ Singleton pattern for settings endpoints (results as dict)
- ✅ Collection pattern for list endpoints (results as list)
- ✅ exists() methods with try/except for 404 handling
- ✅ Real SSH key generation for testing (PEM format)
- ✅ Member management for group endpoints
- ✅ 138 comprehensive tests (100% pass rate)

### Documentation
- ✅ Complete module creation guide (1,900+ lines)
- ✅ Documentation generation prompt
- ✅ Comprehensive docstrings with examples for all methods
- ✅ Type hints on all parameters

## [0.2.0] - 2025-12-14

### Added - Major Expansion! 🎉

#### New CMDB Categories (7 categories, 30 endpoints)
- **DLP (Data Loss Prevention)** - 8 endpoints
  - `data-type` - Predefined data type patterns
  - `dictionary` - Custom DLP dictionaries
  - `exact-data-match` - Fingerprinting for exact data matching
  - `filepattern` - File type and pattern matching
  - `label` - Classification labels
  - `profile` - DLP policy profiles
  - `sensor` - DLP sensor configuration
  - `settings` - Global DLP settings

- **DNS Filter** - 2 endpoints
  - `domain-filter` - Custom domain filtering lists
  - `profile` - DNS filtering profiles

- **Email Filter** - 8 endpoints
  - `block-allow-list` - Email sender block/allow lists
  - `bword` - Banned word filtering
  - `dnsbl` - DNS-based blacklist checking
  - `fortishield` - FortiShield spam filtering
  - `iptrust` - Trusted IP addresses
  - `mheader` - Email header filtering rules
  - `options` - Global email filter options
  - `profile` - Email filtering profiles

- **Endpoint Control** - 3 endpoints
  - `fctems` - FortiClient EMS integration
  - `fctems-override` - EMS override configurations
  - `settings` - Endpoint control settings

- **Ethernet OAM** - 1 endpoint
  - `cfm` - Connectivity Fault Management (requires physical hardware)

- **Extension Controller** - 6 endpoints
  - `dataplan` - FortiExtender data plan configuration
  - `extender` - FortiExtender controller settings
  - `extender-profile` - FortiExtender profiles
  - `extender-vap` - FortiExtender WiFi VAP
  - `fortigate` - FortiGate controller configuration
  - `fortigate-profile` - FortiGate connector profiles

- **File Filter** - 1 endpoint
  - `profile` - File content filtering profiles

### Changed
- **License**: Changed from MIT to Proprietary License with free use
  - Free for personal, educational, and business use
  - Companies can use for internal operations and client services
  - Tech support and MSPs can use in their service offerings
  - **Cannot sell the software itself as a standalone product**
  - Simple rule: Use it freely for your work, just don't sell the software

### Improved
- **CMDB Coverage**: 21 → 51 endpoints (+143% growth!)
- **CMDB Categories**: 7 → 14 categories (+100% growth!)
- All modules follow consistent patterns:
  - `from __future__ import annotations` for modern type hints
  - Comprehensive docstrings with examples
  - Snake_case to hyphen-case parameter conversion
  - Full CRUD operations where applicable
  - **kwargs for flexibility

### Fixed
- Directory naming issues (hyphens → underscores for Python imports)
- Graceful error handling for hardware-dependent features
- Improved test patterns for pre-allocated resource slots
- Better handling of list/dict API responses

### Documentation
- Updated PROJECT_STATUS.md with all new modules
- Updated README with current statistics
- Updated CHANGELOG with detailed release notes
- All modules include comprehensive test files

## [0.1.0] - 2025-12-13

### Added
- Initial release of Fortinet Python SDK
- Modular package architecture supporting FortiOS, FortiManager, FortiAnalyzer
- FortiOS client with token-based authentication
- Comprehensive exception handling system (387 FortiOS error codes)
- CMDB endpoints (Beta - partial coverage):
  - `alertemail` - Email alert settings
  - `antivirus` - Antivirus profiles and settings
  - `application` - Application control (custom, list, group, name)
  - `authentication` - Authentication rules, schemes, and settings
  - `automation` - Automation settings
  - `casb` - CASB (Cloud Access Security Broker) profiles
  - `certificate` - Certificate management (CA, CRL, local, remote, HSM)
  - `diameter_filter` - Diameter filter profiles
- Service endpoints (Beta):
  - `sniffer` - Packet capture and analysis
  - `security_rating` - Security Fabric rating
  - `system` - System information and operations
- Log endpoints (Beta):
  - `disk` - Disk-based logging
  - `fortianalyzer` - FortiAnalyzer logging
  - `forticloud` - FortiCloud logging
  - `memory` - Memory-based logging
  - `search` - Log search functionality
- Base exception classes for all Fortinet products
- FortiOS-specific exception classes with detailed error code mapping
- Support for both full package and standalone module installation
- Module availability detection (`get_available_modules()`)
- Version information (`get_version()`)

### Documentation
- Comprehensive README with installation and usage examples
- QUICKSTART guide for rapid onboarding
- Exception hierarchy documentation
- API structure overview
- Common usage patterns and examples

### Infrastructure
- Package distribution setup (setup.py, MANIFEST.in)
- Requirements management (requirements.txt)
- Git ignore configuration
- MIT License

## [0.0.1] - 2025-11-XX

### Added
- Initial project structure
- Basic FortiOS client implementation
- Core exception handling

---

## Version Numbering

- **Major version (X.0.0)**: Incompatible API changes
- **Minor version (0.X.0)**: New features, backward compatible
- **Patch version (0.0.X)**: Bug fixes, backward compatible

## Categories

- **Added**: New features
- **Changed**: Changes in existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes
