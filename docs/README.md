# HFortix Documentation

Complete reference documentation for the HFortix FortiOS Python SDK.

## Quick Start

- **[Quick Start Guide](../QUICKSTART.md)** - Get started in 5 minutes

## User Guides

### Getting Started
- **[SECURITY.md](SECURITY.md)** - Security best practices and audit results
- **[FILTERING_GUIDE.md](FILTERING_GUIDE.md)** - Complete guide to filtering API queries with 50+ examples
- **[ASYNC_GUIDE.md](ASYNC_GUIDE.md)** - Async/await support for concurrent operations
- **[PERFORMANCE_TESTING.md](PERFORMANCE_TESTING.md)** - Test your FortiGate and optimize connection settings

### Feature Guides

#### Convenience Wrappers
- **[wrappers/CONVENIENCE_WRAPPERS.md](wrappers/CONVENIENCE_WRAPPERS.md)** - **START HERE:** Overview of all convenience wrappers with common patterns and examples
- **[wrappers/FIREWALL_POLICY_WRAPPER.md](wrappers/FIREWALL_POLICY_WRAPPER.md)** - Detailed firewall policy API reference (150+ parameters) (v0.3.17)
- **[wrappers/SHAPER_WRAPPERS.md](wrappers/SHAPER_WRAPPERS.md)** - Detailed traffic shaper API reference (per-IP and traffic shapers) (v0.3.38)
- **[wrappers/SCHEDULE_WRAPPERS.md](wrappers/SCHEDULE_WRAPPERS.md)** - Schedule management reference (onetime, recurring, groups) (v0.3.34)
- **[ERROR_HANDLING_CONFIG.md](ERROR_HANDLING_CONFIG.md)** - Configurable error handling for convenience wrappers (v0.3.24)

#### Framework Features
- **[VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)** - Using the validation framework (832 validators) (v0.3.21)
- **[BUILDER_PATTERN_GUIDE.md](BUILDER_PATTERN_GUIDE.md)** - Builder pattern implementation details (v0.3.21)
- **[ASYNC_GUIDE.md](ASYNC_GUIDE.md)** - Async/await patterns and best practices
- **[FILTERING_GUIDE.md](FILTERING_GUIDE.md)** - FortiOS filtering with 50+ examples
- **[PERFORMANCE_TESTING.md](PERFORMANCE_TESTING.md)** - Performance testing and optimization

## API Reference

- **[ENDPOINT_METHODS.md](ENDPOINT_METHODS.md)** - Method reference for all 857 endpoints
- **[API Coverage](../API_COVERAGE.md)** - Complete API coverage status (750+ endpoints)

## Additional Resources

- **[Main README](../README.md)** - Project overview
- **[Changelog](../CHANGELOG.md)** - Complete version history
- **[Examples](../examples/)** - Working code samples

## What's New in v0.3.38

- **Traffic Shaper Wrappers**: Production-ready wrappers for traffic shaping
  - Per-IP shaper: Bandwidth and session limits per source IP
  - Traffic shaper: Shared pools with guaranteed/maximum bandwidth
  - Full parameter support with comprehensive validation
- **Service Wrappers**: Complete service management (v0.3.37)
  - Custom services, service categories, service groups
  - Full CRUD operations with rename and clone support
- **Consolidated Documentation**: New comprehensive convenience wrappers guide

## What's New in v0.3.34

- **Schedule Convenience Methods**: Added `get_by_name()`, `rename()`, and `clone()` to all schedule types
- **IP/MAC Binding Modules**: New modules for managing IP/MAC binding settings and table entries
- **Firewall Policy Helpers**: Extracted validation utilities into reusable `_helpers.py` module

## What's New in v0.3.24

- **Error Handling Configuration**: Configurable error handling for convenience wrappers
  - Three error modes: "raise" (default), "return", "print"
  - Three error formats: "detailed" (default), "simple", "code_only"
  - Configure at instance level or override per method call

## What's New in v0.3.21

- **Validation Framework**: 832 auto-generated validators for all API types
- **Builder Pattern**: Centralized payload construction (Phase 1: Firewall Policy)
- **Security Audit**: Comprehensive security review and best practices guide
- **Code Quality**: 100% PEP 8 compliance, type hints, and docstrings

---

**Documentation Status:** ✅ Complete and up-to-date (December 29, 2025)
