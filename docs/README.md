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
- **[FIX_WINDOWS_INSTALL.md](FIX_WINDOWS_INSTALL.md)** - Troubleshooting Windows installation issues

### Feature Guides
- **[SCHEDULE_CONVENIENCE_METHODS.md](SCHEDULE_CONVENIENCE_METHODS.md)** - Schedule management convenience methods (v0.3.34)
- **[VALIDATION_GUIDE.md](VALIDATION_GUIDE.md)** - Using the validation framework (832 validators) (v0.3.21)
- **[BUILDER_PATTERN_GUIDE.md](BUILDER_PATTERN_GUIDE.md)** - Builder pattern implementation details (v0.3.21)
- **[FIREWALL_POLICY_WRAPPER.md](FIREWALL_POLICY_WRAPPER.md)** - Intuitive interface for firewall policy management (v0.3.17)
- **[ERROR_HANDLING_CONFIG.md](ERROR_HANDLING_CONFIG.md)** - Configurable error handling for convenience wrappers (v0.3.24)

### Development & Testing
- **[TESTPYPI_GUIDE.md](TESTPYPI_GUIDE.md)** - TestPyPI setup and testing releases (v0.3.34)

## API Reference

- **[ENDPOINT_METHODS.md](ENDPOINT_METHODS.md)** - Method reference for all 857 endpoints
- **[API Coverage](../API_COVERAGE.md)** - Complete API coverage status (750+ endpoints)

## Additional Resources

- **[Main README](../README.md)** - Project overview
- **[Changelog](../CHANGELOG.md)** - Complete version history
- **[Examples](../examples/)** - Working code samples

## What's New in v0.3.34

- **Schedule Convenience Methods**: Added `get_by_name()`, `rename()`, and `clone()` to all schedule types
- **IP/MAC Binding Modules**: New modules for managing IP/MAC binding settings and table entries
- **Firewall Policy Helpers**: Extracted validation utilities into reusable `_helpers.py` module
- **Pre-release Tooling**: Added bandit security scanning and pre-commit integration
- **Documentation**: Organized docs directory structure, added TestPyPI guide

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

**Documentation Status:** ✅ Complete and up-to-date (December 25, 2025)
