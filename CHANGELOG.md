# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
