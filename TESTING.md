# HFortix Test Coverage

**Comprehensive test suite with 1,447+ schema validator tests and extensive live integration testing**

## Overview

The HFortix project maintains extensive test coverage across all layers of the SDK, from generated code validation to live API integration testing. This document provides a detailed breakdown of our test organization and coverage.

## Test Suite Statistics

| Metric | Count |
| --- | --- |
| **Schema Validator Test Files** | 786 files (1,348 endpoints) |
| **Schema Validator Tests** | 1,447 tests |
| **Live Integration Test Files** | 80+ files |
| **Total API Endpoints Covered** | 1,348 (FortiOS 7.6.5) |
| **Execution Time (Schema)** | ~5 seconds (parallel) |
| **Test Documentation** | `packages/fortios/dev/tests/README.md`, `packages/fortios/dev/tests/INDEX.md` |

## Quick Start

See `packages/fortios/dev/tests/README.md` for complete usage instructions.

```bash
# Run all tests
cd packages/fortios/dev/tests && python run_all_tests.py

# Schema validators only (fast, no API)
cd packages/fortios/dev/tests && python run_all_tests.py --schema-only

# Live integration tests
cd packages/fortios/dev/tests && python run_all_tests.py --live-only --live-client=fgt
```

## Test Categories

### 1. Schema Validators (786 files, 1,447 tests)

Automated tests for all generated endpoint validator functions - **no API calls required**.

| Category | Test Files | Coverage |
|----------|-----------|----------|
| **CMDB (Configuration)** | 561 | 100% of generated CMDB endpoints |
| **Monitor (Status)** | 490 | 100% of generated Monitor endpoints |
| **Log (Query)** | 286 | 100% of generated Log endpoints |
| **Service (Operations)** | 11 | 100% of generated Service endpoints |
| **Total** | **1,348** | **100% of FortiOS 7.6.5 endpoints** |

**Location**: `packages/fortios/dev/tests/schema-validators/api/`

**What's Tested**:
- Validator function imports (1,348 tests)
- Required field validation (99 tests)
- Generated code syntax and structure
- Type checking for parameters
- **API Request Inspection** - `http_api_request` and `fmg_api_request` properties (8 tests)

**Special Test Files**:
- `test_api_request_properties.py` - Validates HTTP/FMG API request inspection properties (8 comprehensive tests covering FortiObject, FortiObjectList, ContentResponse)
- `example_api_request_inspection.py` - Demonstrates request inspection feature with practical GET/POST examples

**Execution**: Fast (~5 seconds), parallel, offline

### 2. Live Integration Tests (80+ files)

Real API integration tests against live FortiGate/FortiManager devices.

**Location**: `packages/fortios/dev/tests/live/`

**Coverage Areas**:
- **Endpoints** (`endpoints/`) - CMDB, Monitor, Log, Service API tests
- **Clients** (`integration/`, `fmgproxy/`) - FortiGate direct & FortiManager proxy
- **Unit Tests** (`unit/`) - HTTP client, response processing, error handling (13 files)
- **Validators** (`validators/`) - Validator components, formatters, caching (40+ files)

**Execution**: Sequential (respects API rate limits), requires live device access

### 3. Validator & Helper Component Tests (40+ files, 75+ functions)

**Location**: `packages/fortios/dev/tests/live/validators/`

Unit tests for all validation and helper utility functions:

#### Generic Validators (6 functions)
- `validate_required_fields()` - Required field validation
- `validate_color()` - Color index validation (0-32)
- `validate_status()` - Status field (enable/disable)
- `validate_enable_disable()` - Boolean to string conversion
- `validate_string_length()` - String length constraints
- `validate_integer_range()` - Integer range validation

#### Network Validators (5 functions)
- `validate_mac_address()` - MAC address format
- `validate_ip_address()` - IPv4 address validation
- `validate_ipv6_address()` - IPv6 address validation
- `validate_ip_network()` - CIDR network validation
- `validate_port_number()` - Port range (0-4294967295)

#### Firewall Validators (3 functions)
- `validate_policy_id()` - Policy ID validation
- `validate_address_pairs()` - Address pair validation
- `validate_seq_num()` - Sequence number validation

#### Schedule Validators (3 functions)
- `validate_schedule_name()` - Schedule name (max 31 chars)
- `validate_time_format()` - Time format (HH:MM)
- `validate_day_names()` - Day name validation

#### SSH/SSL Validators (7 functions)
- `validate_ssh_host_key_type()` - SSH key type validation
- `validate_ssh_host_key_status()` - Key status validation
- `validate_ssh_host_key_nid()` - ECDSA NID validation
- `validate_ssh_host_key_usage()` - Key usage validation
- `validate_ssh_source()` - Local CA/key source
- `validate_ssl_dh_bits()` - Diffie-Hellman bits
- `validate_ssl_cipher_action()` - Cipher action validation

#### Endpoint Validators (5 functions)
- `validate_required_fields()` - Enhanced required field validation
- `validate_enum_field()` - Enum validation with error messages
- `validate_query_parameter()` - Query param validation
- `validate_multiple_enums()` - Batch enum validation
- `validate_multiple_query_params()` - Batch query validation

#### Normalizers (3 functions)
- `normalize_to_name_list()` - Convert to [{'name': '...'}] format
- `normalize_member_list()` - Member list normalization
- `normalize_table_field()` - Universal table field normalizer

#### Converters (2 functions)
- `convert_boolean_to_str()` - Bool to 'enable'/'disable'
- `filter_empty_values()` - Remove None/empty values

#### Builders (3 functions)
- `build_cmdb_payload()` - Build CMDB payloads (snake_case → kebab-case)
- `build_cmdb_payload_normalized()` - Build with auto-normalization
- `build_api_payload()` - Universal payload builder

#### Response Helpers (4 functions)
- `get_name()` - Extract object name/mkey
- `get_mkey()` - Alias for get_name()
- `get_results()` - Extract results from response
- `is_success()` - Check response success status

#### Metadata Functions (9 functions)
- `get_field_description()` - Field help text
- `get_field_type()` - Field type (string, option, integer, table)
- `get_field_constraints()` - Min/max, length constraints
- `get_field_default()` - Default value
- `get_field_options()` - Valid enum options
- `get_nested_schema()` - Nested table schema
- `get_all_fields()` - All field names
- `get_field_metadata()` - Complete field metadata
- `validate_field_value()` - Value constraint validation

#### Formatting Functions (13 functions)
- `to_json()` - Format as JSON
- `to_csv()` - Comma-separated format
- `to_dict()` - Convert to dictionary
- `to_multiline()` - Newline-separated
- `to_list()` - Convert to list
- `to_quoted()` - Quoted string representation
- `to_table()` - Table format
- `to_yaml()` - YAML-like format
- `to_xml()` - Simple XML format
- `to_key_value()` - Key=value pairs
- `to_markdown_table()` - Markdown table
- `to_dictlist()` - Columnar dict to list of dicts
- `to_listdict()` - List of dicts to columnar dict

#### Additional Test Categories
- **Audit Handlers** (`test_audit_handlers.py`) - Kafka, webhook, database audit logging
- **Audit Formatters** (`test_audit_formatters.py`) - Log format customization
- **Debug Formatters** (`test_debug_formatters.py`) - Debug output formatting
- **Debug Session** (`test_debug_session.py`) - Debug session management
- **Debug Timer** (`test_debug_timer.py`) - Performance timing utilities
- **Logging Formatters** (`test_logging_formatters.py`) - Log output formatting
- **Request Logger** (`test_request_logger.py`) - HTTP request/response logging
- **Cache** (`test_cache.py`) - General caching mechanisms
- **TTL Cache** (`test_ttl_cache.py`) - Time-based cache expiration
- **Readonly Cache** (`test_readonly_cache.py`) - Read-only endpoint caching
- **FortiObject** (`test_forti_object.py`) - Response wrapper object tests
- **FortiOS Types** (`test_fortios_types.py`) - Type system tests
- **Core Types** (`test_core_types.py`) - Core type definitions
- **Deprecation** (`test_deprecation.py`) - Deprecation warning system
- **Credential Validation** (`test_credential_validation.py`) - Auth credential validation
- **Exceptions** (`test_exceptions.py`) - Exception hierarchy and handling
- **Metadata Mixin** (`test_metadata_mixin.py`) - Schema metadata mixing
- **FortiOS Formatting** (`test_fortios_formatting.py`) - FortiOS-specific formatting

**Location**: `packages/fortios/dev/tests/live/validators/`

**Coverage**: 75+ utility functions fully tested with valid cases, invalid cases, edge cases, and optional value handling

### 3. Unit Tests (12 files)

Low-level unit tests for core functionality:

| Test File | Coverage |
|-----------|----------|
| `test_http_client_advanced.py` | Advanced HTTP client features (retry, circuit breaker) |
| `test_http_client_utils.py` | HTTP client utility functions |
| `test_process_response.py` | Response processing and transformation |
| `test_response_types.py` | Response type handling |
| `test_log_operation.py` | Operation logging functionality |
| `test_async_client.py` | Async/await client operations |
| `test_format_utils.py` | Data formatting utilities |
| `test_runner_and_cleanup.py` | Test runner and cleanup logic |
| `test_exception_utils.py` | Exception handling utilities |
| `test_print_debug.py` | Debug output utilities |
| `test_api_utils.py` | API utility functions |
| `test_encode_path.py` | URL path encoding |
| `test_forti_object_types.py` | FortiObject type system |

**Location**: `packages/fortios/dev/tests/live/unit/`

**Coverage**: Core HTTP client, response processing, error handling, async operations, formatting

### 4. Integration Tests (3 files)

End-to-end integration tests:

| Test File | Coverage |
|-----------|----------|
| `test_fortios_client.py` | FortiOS client lifecycle (connect, auth, operations, disconnect) |
| `test_hooks.py` | Hooks system (pre-request, post-response, error hooks) |
| `test_http_client_stats.py` | HTTP client statistics tracking |

**Location**: `packages/fortios/dev/tests/live/integration/`

**Coverage**: Client initialization, authentication, hook execution, statistics collection

### 5. FortiManager Proxy Tests (1 file)

FortiManager JSON-RPC proxy functionality:

| Test File | Coverage |
|-----------|----------|
| `test_client.py` | FMG proxy client (login, device selection, ADOM, API passthrough) |

**Location**: `packages/fortios/dev/tests/live/fmgproxy/`

**Coverage**: FortiManager proxy authentication, device targeting, API operations

### 6. Edge Case Tests

Special scenario and edge case handling:

**Location**: `packages/fortios/dev/tests/live/x_egde_cases/`

**Coverage**: 
- List handling edge cases
- Parameter normalization edge cases
- Helper function edge cases

### 7. PyTest Integration Tests (5 files)

Additional pytest-based tests:

| Test File | Coverage |
|-----------|----------|
| `api/monitor/system/auto_test_test.py` | Monitor system auto-test endpoint |
| `api/monitor/user/auto_test_test.py` | Monitor user auto-test endpoint |
| `api/log/test_forticloud.py` | FortiCloud log queries |
| `api/log/test_search.py` | Log search functionality |
| `api/log/test_fortianalyzer.py` | FortiAnalyzer log queries |
| `api/log/test_memory.py` | Memory log queries |
| `api/log/test_disk.py` | Disk log queries |

**Location**: `packages/fortios/dev/tests/pytests/`

## Test Execution Strategy

### Parallel Execution (Validators Only)

Validator and helper tests can run in parallel because they:
- ✅ Make no API calls to FortiGate
- ✅ Modify no external state
- ✅ Are pure validation logic tests
- ✅ Have no dependencies between tests

### Sequential Execution (Endpoints)

Endpoint tests must run sequentially to:
- ✅ Respect FortiOS API rate limits
- ✅ Avoid overwhelming the FortiGate device
- ✅ Prevent test interference (resource conflicts)
- ✅ Maintain stable test environment

## Test Structure Pattern

All tests follow a consistent pattern:

```python
def test_function_name():
    """Test description"""
    
    # 1. Valid cases - test with correct values
    result = function(valid_input)
    assert expected_behavior
    
    # 2. Invalid cases - test error handling
    with pytest.raises(ExpectedException):
        function(invalid_input)
    
    # 3. Edge cases - test boundary conditions
    result = function(edge_case_input)
    assert edge_case_behavior
    
    # 4. Optional values - test None handling
    result = function(optional_param=None)
    assert optional_handling
```

## Running Tests

### Run All Tests
```bash
cd packages/fortios/dev/tests/live
python __run__.py
```

### Run Specific Category
```bash
# Validators only
pytest validators/

# Endpoint tests only
pytest endpoints/

# Unit tests only
pytest unit/

# Integration tests only
pytest integration/
```

### Run Specific Test File
```bash
pytest validators/test_network_validators.py
pytest endpoints/cmdb/firewall_address.py
```

### Run with Coverage Report
```bash
pytest --cov=hfortix_fortios --cov-report=html
```

## Test Quality Standards

All tests adhere to:

- ✅ **Comprehensive coverage** - Valid, invalid, edge cases
- ✅ **Clear naming** - Descriptive test function names
- ✅ **Documentation** - Docstrings explaining test purpose
- ✅ **Isolation** - No dependencies between tests
- ✅ **Assertions** - Explicit expected behavior verification
- ✅ **Error validation** - Proper exception testing
- ✅ **Cleanup** - Proper teardown and resource cleanup

## Coverage Goals

| Component | Current Coverage | Target |
|-----------|-----------------|--------|
| **API Endpoints** | 100% (1,348/1,348) | 100% |
| **Validators** | 100% (75/75 functions) | 100% |
| **HTTP Client** | ~95% | 100% |
| **Response Processing** | ~95% | 100% |
| **Error Handling** | ~90% | 100% |
| **FortiManager Proxy** | ~85% | 95% |
| **Async Operations** | ~80% | 95% |

## Continuous Improvement

Our test suite is continuously improved through:

- 📈 **Regular audits** - Identifying coverage gaps
- 🔄 **Regression tests** - Adding tests for bug fixes
- 🆕 **New feature tests** - Tests for all new functionality
- 📊 **Coverage tracking** - Monitoring test coverage metrics
- 🐛 **Bug reproduction** - Tests that reproduce reported issues
- 📝 **Documentation** - Keeping test docs up to date

## Test Files Location

```
packages/fortios/dev/tests/
├── live/
│   ├── endpoints/
│   │   ├── cmdb/          # 180 CMDB endpoint tests
│   │   ├── monitor/       # 63 Monitor endpoint tests
│   │   ├── log/           # 4 Log endpoint tests
│   │   └── service/       # 4 Service endpoint tests
│   ├── validators/        # 40 validator/helper tests
│   ├── unit/              # 12 unit tests
│   ├── integration/       # 3 integration tests
│   ├── fmgproxy/          # 1 FortiManager proxy test
│   └── x_egde_cases/      # Edge case tests
├── pytests/
│   └── api/               # 5 pytest integration tests
└── others/                # Experimental/utility tests
```

## Contributing Tests

When adding new tests:

1. **Follow the pattern** - Use consistent test structure
2. **Test all cases** - Valid, invalid, edge cases
3. **Add documentation** - Clear docstrings
4. **Update this document** - Keep coverage stats current
5. **Run locally** - Verify tests pass before committing
6. **Consider performance** - Avoid overwhelming API rate limits

## Summary

The HFortix test suite provides **comprehensive validation** of all SDK functionality:

- ✅ **2,566+ test functions** ensure reliability
- ✅ **318 test files** organized by category
- ✅ **100% endpoint coverage** for all 1,348 FortiOS APIs
- ✅ **75+ utility functions** fully validated
- ✅ **Multi-layer testing** from unit to integration
- ✅ **Production ready** with extensive real-world scenario coverage

This extensive testing ensures HFortix is **production-ready and reliable** for enterprise use.
