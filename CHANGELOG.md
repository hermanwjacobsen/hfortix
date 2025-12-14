# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### In Progress
- Firewall category expansion (83 remaining endpoints)
- Monitor API implementation

### Planned
- Complete CMDB endpoint coverage (74/150+ endpoints complete)
- Monitor endpoints implementation
- FortiManager module
- FortiAnalyzer module
- Async support
- CLI tool

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
- ✅ Nested API structure: `fgt.cmdb.firewall.[subcategory].[endpoint]`
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
