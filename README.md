# HFortix - Fortinet Python SDK

Python client library for Fortinet products including FortiOS, FortiManager, and FortiAnalyzer.

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)
[![Typing: Typed](https://img.shields.io/badge/typing-typed-green.svg)](https://peps.python.org/pep-0561/)

## 🎯 Current Status

**⚠️ BETA STATUS**: All implementations are functional but in beta. APIs work correctly but may have incomplete parameter coverage or undiscovered edge cases.

**FortiOS 7.6.5 Coverage (December 19, 2025):**

- **CMDB API**: 37 of 37 categories (100% coverage) - 500+ endpoints 🔷 Beta
- **Monitor API**: 32 of 32 categories (100% coverage) - 200+ endpoints 🔷 Beta
- **Log API**: 5 of 5 categories (100% coverage) - Log reading functionality 🔷 Beta
- **Service API**: 3 of 3 categories (100% coverage) - 21 methods 🔷 Beta
- **Overall**: 77 of 77 categories (100% coverage) - 750+ API methods 🎉

**Test Coverage:** 226 test files (145 CMDB, 81 Monitor) with 75%+ pass rate (~50% of generated endpoints tested)

**Note:** All implementations remain in beta until version 1.0.0 with comprehensive unit test coverage.

**🔥 Recent Highlights (December 2025):**
- 🎉 **100% API COVERAGE**: Complete implementation of ALL documented FortiOS 7.6.5 API categories!
- 🚀 **MASSIVE EXPANSION**: Generated 500+ new endpoints across 37 CMDB + 32 Monitor categories
- 🔄 **API Refactoring**: All endpoints refactored with RESTful methods (.list(), .get(), .create(), .update(), .delete())
- ⚡ **Dual-Pattern Interface**: Flexible syntax supporting both dictionary and keyword arguments
- 🏗️ **Repository Organization**: Clean structure with all dev tools
- ⚡ **Unified Module Generator**: Single tool handles all edge cases (digit-prefixed names, certificates, nested resources)
- ✨ **Monitor API** (v0.3.11): 6 categories with 50+ monitoring endpoints (firewall stats, sessions, EMS, etc.)
- ✨ **Log Configuration** (v0.3.11): 56 endpoints for comprehensive logging setup
- ✨ **Firewall Expansion** (v0.3.11): FTP proxy, ICAP, IPS, DoS policies, access-proxy (WAF)

**📖 Documentation:**
- **User Guide**: [QUICKSTART.md](https://github.com/hermanwjacobsen/hfortix/blob/main/QUICKSTART.md) - Getting started guide
- **Async Guide**: [ASYNC_GUIDE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ASYNC_GUIDE.md) - Async/await support documentation
- **API Method Reference**: [ENDPOINT_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/ENDPOINT_METHODS.md) - All 857 endpoints with available methods
- **Helper Methods Guide**: [HELPER_METHODS.md](https://github.com/hermanwjacobsen/hfortix/blob/main/HELPER_METHODS.md) - Safe existence checking and best practices
- **API Coverage**: [API_COVERAGE.md](https://github.com/hermanwjacobsen/hfortix/blob/main/API_COVERAGE.md) - Implementation status by category
- **Full Changelog**: [CHANGELOG.md](https://github.com/hermanwjacobsen/hfortix/blob/main/CHANGELOG.md) - Complete version history

**Latest Features (v0.3.15):**
- ✨ **Async/Await Support**: Full dual-mode support for async operations (NEW!)
  - Single `FortiOS` class works in both sync and async modes
  - All 750+ API methods support async with `mode="async"` parameter
  - All helper methods (`.exists()`) work transparently in both modes
  - Async context manager support with `async with`
  - Zero breaking changes - existing sync code continues to work
- ✨ **288 Endpoints Updated**: All `.exists()` helper methods now async-aware
- 🏗️ **Refactored Architecture**: Improved code quality and maintainability
  - Protocol-based HTTP client interface (`IHTTPClient`) for extensibility
  - Eliminated 744 lines of duplicated code (35% reduction)
  - Shared base class (`BaseHTTPClient`) for sync and async clients
  - Enhanced testability and consistency across sync/async modes
  - Users can now provide custom HTTP client implementations

**Also in v0.3.15:**
- ✨ **Request ID / Correlation Tracking**: Auto-generated or custom request IDs for distributed tracing
- ✨ **Circuit Breaker Pattern**: Automatic fail-fast to prevent cascading failures (opens after 5 failures, auto-recovers)
- ✨ **Connection Pool Metrics**: Monitor HTTP client health with `get_connection_stats()` method
- ✨ **Per-Endpoint Timeouts**: Configure custom timeouts per endpoint with wildcard pattern support
- ✨ **Structured Logging**: Machine-readable logs with extra fields (request_id, endpoint, method, status_code, duration)
- ✨ **100% Backwards Compatible**: All existing code works unchanged


**Previous Release (v0.3.12):**
- ✨ **HTTP/2 Support**: Modern httpx library with connection multiplexing for improved performance
- ✨ **Automatic Retry Logic**: Exponential backoff (1s, 2s, 4s, 8s, 30s max) for transient failures
- ✨ **Enhanced Reliability**: Retries on connection errors, timeouts, rate limits (429), server errors (500-504)
- ✨ **Context Manager Support**: Use `with HTTPClient(...) as client:` for automatic cleanup
- ✨ **Retry Statistics**: Track retry attempts by reason and endpoint
- ✨ **Better Error Handling**: Graceful fallback for non-JSON responses, improved logging

**Previous Release (v0.3.11):**
- ✨ **FTP Proxy Category**: FTP proxy configuration (1 endpoint)
  - **explicit**: FTP proxy explicit configuration with SSL/TLS support
  - FTPS support, SSL certificate management, custom encryption
  - 10 parameters: status, ports, IPs, security actions, SSL settings
  - Test coverage: 5 test sections with comprehensive validation
- ✨ **Monitor API Categories**: 6 categories implemented (18% coverage)
  - **firewall/**: 39 endpoints for firewall monitoring
  - Policy statistics, session monitoring, ACL counters
  - Address objects, traffic shapers, GTP stats
  - Special endpoints: policy-lookup (callable), clearpass-address (actions)
  - **endpoint-control/**: 7 endpoints for FortiClient EMS monitoring
  - **azure/, casb/, extender-controller/, extension-controller/**: Additional monitoring
  - Test coverage: 39 firewall tests with 100% pass rate
  - All endpoints support explicit parameters (no **kwargs)
- ✨ **Log Configuration Category**: 56 endpoints for comprehensive logging setup
  - Nested object pattern: `fgt.api.cmdb.log.disk.filter.get()`
  - Multiple FortiAnalyzer, syslog, TACACS+ server support
  - Custom fields, event filters, threat weights
- ✨ **ICAP Category**: Complete ICAP integration (3 endpoints, 30+ parameters)
- ✨ **IPS Category**: Full IPS management (8 endpoints)
  - Custom signatures, sensors, decoders, rules
- ✨ **Monitoring & Report Categories**: NPU-HPE monitoring, report layouts
- ✨ **Firewall Category Expansion**: 29 endpoints with nested objects
  - DoS policies, access-proxy (reverse proxy/WAF)
  - Schedule, service, shaper, SSH/SSL configurations
  
**Previous Release (v0.3.10):**
- ✨ **Configurable Timeouts**: Customize connection and read timeouts
  - `connect_timeout`: Connection establishment timeout (default: 10.0s)
  - `read_timeout`: Response read timeout (default: 300.0s)
  - Example: `FortiOS(host='...', token='...', connect_timeout=30.0, read_timeout=600.0)`
- ✨ **URL Encoding for Special Characters**: Automatic encoding of special characters in object names
  - Handles `/`, `@`, `:`, spaces, and other special characters
  - Works with objects like `Test_NET_192.0.2.0/24` (IP addresses with CIDR notation)
  - Applied to all 145 CMDB endpoint files automatically
- ✅ **Bug Fix**: Fixed 404 errors when object names contain special characters

**Previous Release (v0.3.9):**
- ✨ **raw_json Parameter**: All 200+ API methods now support `raw_json=True` for full response access
- ✨ **Logging System**: Global and per-instance logging control
- ✅ **Code Quality**: 100% PEP 8 compliance (black + isort + flake8)
- ✅ **Comprehensive Tests**: 200+ test files covering all endpoints

**Previous Releases:**
- v0.3.8: Dual-pattern interface for all create/update methods
- v0.3.7: Packaging and layout improvements
- v0.3.6: Hidden internal CRUD methods for cleaner autocomplete
- v0.3.5: Enhanced IDE autocomplete with PEP 561 type hints
- v0.3.4: Unified import syntax documentation
- v0.3.0: Firewall endpoints expansion

## 🎯 Features

- **Unified Package**: Import all Fortinet products from a single package
- **Type-Safe & Type-Checked**: Full PEP 561 compliance with mypy/pyright support for IDE autocomplete
- **Async/Await Support**: Full dual-mode operation - works with both sync and async code
- **Modular Architecture**: Each product module can be used independently
- **PyPI Installation**: `pip install hfortix` - simple and straightforward
- **Comprehensive Exception Handling**: 387+ FortiOS error codes with detailed descriptions
- **Automatic Retry Logic**: Built-in retry mechanism with exponential backoff for transient failures
- **HTTP/2 Support**: Modern HTTP client with connection multiplexing for improved performance
- **Circuit Breaker**: Prevents cascade failures with automatic recovery
- **Simplified APIs**: Auto-conversion for common patterns (e.g., address group members)
- **Well-Documented**: Extensive API documentation and examples
- **Modern Python**: Type hints, PEP 585 compliance, Python 3.10+

## 📦 Available Modules

| Module | Status | Description |
|--------|--------|-------------|
| **FortiOS** | ✅ Active | FortiGate firewall management API |
| **FortiManager** | ⏸️ Planned | Centralized management for FortiGate devices |
| **FortiAnalyzer** | ⏸️ Planned | Log analysis and reporting platform |

## 🚀 Installation

### From PyPI (Recommended)
```bash
pip install hfortix
```

## 📖 Quick Start

### Basic Usage
```python
from hfortix import FortiOS

# Initialize with API token (recommended)
fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False  # Use True in production with valid SSL cert
)

# List firewall addresses
addresses = fgt.api.cmdb.firewall.address.list()
print(f"Found {len(addresses['results'])} addresses")

# Create a new address
result = fgt.api.cmdb.firewall.address.create(
    name='web-server',
    subnet='192.168.10.50/32',
    comment='Production web server'
)
```

### Raw JSON Response ✨

All API methods support `raw_json` parameter for full response access:

```python
# Default behavior - returns just the results
addresses = fgt.api.cmdb.firewall.address.list()
print(addresses)  # ['obj1', 'obj2', 'obj3']

# With raw_json=True - returns complete API response
response = fgt.api.cmdb.firewall.address.list(raw_json=True)
print(response['http_status'])  # 200
print(response['status'])       # 'success'
print(response['results'])      # ['obj1', 'obj2', 'obj3']
print(response['serial'])       # 'FGT60FTK19000001'
print(response['version'])      # 'v7.6.5'

# Useful for error checking
result = fgt.api.cmdb.firewall.address.get('web-server', raw_json=True)
if result['http_status'] == 200:
    print(f"Object found: {result['results']}")
else:
    print(f"Error: {result.get('error', 'Unknown error')}")
```

**Available on:** All 45+ API methods (100% coverage)

### Logging Control ✨

Control logging output globally or per-instance:

```python
import hfortix
from hfortix import FortiOS

# Enable detailed logging globally for all instances
hfortix.set_log_level('DEBUG')  # Very verbose - all requests/responses
hfortix.set_log_level('INFO')   # Normal - request summaries
hfortix.set_log_level('WARNING') # Quiet - only warnings (default)
hfortix.set_log_level('ERROR')   # Silent - only errors
hfortix.set_log_level('OFF')     # No logging output

# Or enable logging for a specific instance
fgt = FortiOS('192.168.1.99', token='your-token', debug='info')

# Automatic sensitive data sanitization
# Tokens, passwords, and API keys are automatically masked in logs
```

**Features:**
- 5 log levels (DEBUG, INFO, WARNING, ERROR, OFF)
- Automatic sensitive data sanitization
- Request/response logging with timing
- Hierarchical loggers for fine-grained control

### Advanced HTTP Features ✨ NEW in v0.3.15

Enterprise-grade reliability and observability features:

```python
from hfortix import FortiOS

fgt = FortiOS('192.168.1.99', token='your-token', verify=False)

# 1. Request correlation tracking (auto-generated or custom)
result = fgt._client.request(
    "GET", "monitor", "system/status",
    request_id="batch-update-2025-12-17"
)

# 2. Monitor connection pool health
stats = fgt._client.get_connection_stats()
print(f"Circuit breaker: {stats['circuit_breaker_state']}")
print(f"HTTP/2 enabled: {stats['http2_enabled']}")

# 3. Circuit breaker pattern (automatic fail-fast)
# Opens after 5 consecutive failures, auto-recovers after 60s
try:
    result = fgt.api.monitor.system.status.get()
except RuntimeError as e:
    if "Circuit breaker is OPEN" in str(e):
        print("Service is down - failing fast")
        fgt._client.reset_circuit_breaker()  # Manual reset

# 4. Per-endpoint timeouts (custom timeouts for slow endpoints)
fgt._client.configure_endpoint_timeout('monitor/*', read=10.0)
fgt._client.configure_endpoint_timeout('cmdb/firewall/policy', read=600.0)

# 5. Structured logging (machine-readable logs with extra fields)
# All logs include: request_id, endpoint, method, status_code, duration
# Compatible with Elasticsearch, Splunk, CloudWatch
```

**Benefits:**
- **Request Tracking**: Trace requests across distributed systems
- **Circuit Breaker**: Prevent cascading failures during outages
- **Metrics**: Monitor connection pool health and performance
- **Fine-tuned Timeouts**: Different timeouts for fast/slow endpoints
- **Structured Logs**: Machine-readable for log aggregation tools

📖 **Full documentation**: [docs/ADVANCED_HTTP_FEATURES.md](docs/ADVANCED_HTTP_FEATURES.md)

### Dual-Pattern Interface ✨

HFortix supports **flexible dual-pattern syntax** - use dictionaries, keywords, or mix both:

```python
# Pattern 1: Dictionary-based (great for templates)
config = {
    'name': 'web-server',
    'subnet': '192.168.10.50/32',
    'comment': 'Production web server'
}
fgt.api.cmdb.firewall.address.create(data_dict=config)

# Pattern 2: Keyword-based (great for readability)
fgt.api.cmdb.firewall.address.create(
    name='web-server',
    subnet='192.168.10.50/32',
    comment='Production web server'
)

# Pattern 3: Mixed (template + overrides)
base_config = load_template('address_template.json')
fgt.api.cmdb.firewall.address.create(
    data_dict=base_config,
    name=f'server-{site_id}',  # Override name
    comment=f'Site: {site_name}'
)
```

**Available on:** 43 methods across 13 categories (100% coverage)
- All CMDB create/update operations (38 endpoints)
- Service operations (5 methods)

### Exception Handling
```python
from hfortix import (
    FortiOS,
    APIError,
    ResourceNotFoundError,
    DuplicateEntryError
)

try:
    result = fgt.api.cmdb.firewall.address.create(
        name='test-address',
        subnet='10.0.0.0/24'
    )
except DuplicateEntryError as e:
    print(f"Address already exists: {e}")
except ResourceNotFoundError as e:
    print(f"Resource not found: {e}")
except APIError as e:
    print(f"API Error: {e.message}")
    print(f"HTTP Status: {e.http_status}")
    print(f"Error Code: {e.error_code}")
```

## 🏗️ Project Structure

```
fortinet/
├── hfortix/                  # Main package
│   ├── __init__.py           # Public API exports
│   ├── exceptions.py         # Base exceptions
│   ├── exceptions_forti.py   # FortiOS-specific error codes/helpers
│   ├── py.typed              # PEP 561 marker
│   └── FortiOS/
│       ├── __init__.py
│       ├── fortios.py        # FortiOS client
│       ├── http_client.py    # Internal HTTP client
│       ├── exceptions.py     # FortiOS re-exports
│       └── api/
│           └── v2/
│               ├── cmdb/     # Configuration endpoints
│               ├── log/      # Log reading endpoints
│               ├── service/  # Service operations
│               └── monitor/  # Monitoring endpoints
├── setup.py                  # Package configuration
├── pyproject.toml            # Build system config
├── README.md                 # This file
├── QUICKSTART.md             # Quick reference guide
├── API_COVERAGE.md           # API implementation status
└── CHANGELOG.md              # Version history
```

## 🔍 Module Discovery

Check which modules are available:

```python
from hfortix import get_available_modules

modules = get_available_modules()
print(modules)
# {'FortiOS': True, 'FortiManager': False, 'FortiAnalyzer': False}
```

## 🎓 Examples

### FortiOS - Firewall Address Management
```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='your-token', verify=False)

# List addresses
addresses = fgt.api.cmdb.firewall.address.list()

# Create address
result = fgt.api.cmdb.firewall.address.create(
    name='web-server',
    subnet='10.0.1.100/32',
    comment='Production web server'
)

# Update address
result = fgt.api.cmdb.firewall.address.update(
    name='web-server',
    comment='Updated comment'
)

# Delete address
result = fgt.api.cmdb.firewall.address.delete(name='web-server')
```

### FortiOS - DoS Protection (NEW!)
```python
# Create IPv4 DoS policy with simplified API
result = fgt.api.cmdb.firewall.dos_policy.create(
    policyid=1,
    name='protect-web-servers',
    interface='port3',              # Simple string format
    srcaddr=['all'],                # Simple list format
    dstaddr=['web-servers'],
    service=['HTTP', 'HTTPS'],
    status='enable',
    comments='Protect web farm from DoS attacks'
)

# API automatically converts to FortiGate format:
# interface='port3' → {'q_origin_key': 'port3'}
# service=['HTTP'] → [{'name': 'HTTP'}]

# Custom anomaly detection thresholds
result = fgt.api.cmdb.firewall.dos_policy.create(
    policyid=2,
    name='strict-dos-policy',
    interface='wan1',
    srcaddr=['all'],
    dstaddr=['all'],
    service=['ALL'],
    anomaly=[
        {'name': 'tcp_syn_flood', 'threshold': 500, 'action': 'block'},
        {'name': 'udp_flood', 'threshold': 1000, 'action': 'block'}
    ]
)
```

### FortiOS - Reverse Proxy/WAF (NEW!)
```python
# Create access proxy (requires VIP with type='access-proxy')
result = fgt.api.cmdb.firewall.access_proxy.create(
    name='web-proxy',
    vip='web-vip',                    # VIP must be type='access-proxy'
    auth_portal='enable',
    log_blocked_traffic='enable',
    http_supported_max_version='2.0',
    svr_pool_multiplex='enable'
)

# Create virtual host with simplified API
result = fgt.api.cmdb.firewall.access_proxy_virtual_host.create(
    name='api-vhost',
    host='*.api.example.com',
    host_type='wildcard',
    ssl_certificate='Fortinet_Factory'  # String auto-converts to list
)

# API automatically converts:
# ssl_certificate='cert' → [{'name': 'cert'}]
```

### FortiOS - Address & Address Group Management (NEW!)
```python
# Create IPv4 address (subnet)
result = fgt.api.cmdb.firewall.address.create(
    name='internal-net',
    type='ipmask',
    subnet='192.168.1.0/24',
    comment='Internal network'
)

# Create IPv4 address (IP range)
result = fgt.api.cmdb.firewall.address.create(
    name='dhcp-range',
    type='iprange',
    start_ip='192.168.1.100',
    end_ip='192.168.1.200'
)

# Create IPv4 address (FQDN)
result = fgt.api.cmdb.firewall.address.create(
    name='google-dns',
    type='fqdn',
    fqdn='dns.google.com'
)

# Create IPv6 address
result = fgt.api.cmdb.firewall.address6.create(
    name='ipv6-internal',
    type='ipprefix',
    ip6='2001:db8::/32',
    comment='IPv6 internal network'
)

# Create address group with simplified API
result = fgt.api.cmdb.firewall.addrgrp.create(
    name='internal-networks',
    member=['subnet1', 'subnet2', 'subnet3'],  # Simple string list!
    comment='All internal networks'
)

# API automatically converts:
# member=['addr1', 'addr2'] → [{'name': 'addr1'}, {'name': 'addr2'}]

# Create IPv6 address group
result = fgt.api.cmdb.firewall.addrgrp6.create(
    name='ipv6-internal-networks',
    member=['ipv6-subnet1', 'ipv6-subnet2'],
    comment='All internal IPv6 networks'
)

# Create IPv6 address template
result = fgt.api.cmdb.firewall.address6_template.create(
    name='ipv6-subnet-template',
    ip6='2001:db8::/32',
    subnet_segment_count=2,
    comment='IPv6 subnet template'
)
```

### FortiOS - Schedule Management
```python
# Create recurring schedule
result = fgt.api.cmdb.firewall.schedule.recurring.create(
    name='business-hours',
    day=['monday', 'tuesday', 'wednesday', 'thursday', 'friday'],
    start='08:00',
    end='18:00'
)

# Create one-time schedule
from datetime import datetime, timedelta
tomorrow = datetime.now() + timedelta(days=1)
start = f"09:00 {tomorrow.strftime('%Y/%m/%d')}"
end = f"17:00 {tomorrow.strftime('%Y/%m/%d')}"

result = fgt.api.cmdb.firewall.schedule.onetime.create(
    name='maintenance-window',
    start=start,
    end=end,
    color=5
)
```

### FortiOS - Routing Protocols (Singleton Endpoints) ⚠️

**Important:** Routing protocol configurations use a different pattern than collection endpoints.

**Collection Endpoints** (addresses, policies, etc.) support standard CRUD:
```python
# Standard CRUD - simple and intuitive
fgt.api.cmdb.firewall.address.create(name='test', subnet='192.168.1.0/24')
fgt.api.cmdb.firewall.address.update(name='test', comment='updated')
fgt.api.cmdb.firewall.address.delete('test')
```

**Singleton Endpoints** (BGP, OSPF, RIP, ISIS, etc.) require GET→Modify→PUT pattern:
```python
# BGP Neighbor Management - requires full config update
# Step 1: Get current BGP configuration
result = fgt.api.cmdb.router.bgp.get()

# Step 2: Extract config (handles different response formats)
if isinstance(result, list):
    config = result[0] if result else {}
elif isinstance(result, dict) and 'results' in result:
    config = result['results']
    if isinstance(config, list):
        config = config[0] if config else {}
else:
    config = result

# Step 3: Modify nested objects (neighbors, networks, etc.)
neighbors = config.get('neighbor', [])
neighbors.append({
    'ip': '10.0.0.1',
    'remote-as': 65001,
    'description': 'New BGP neighbor',
    'shutdown': 'enable'  # Disabled for safety
})
config['neighbor'] = neighbors

# Step 4: Send entire config back
result = fgt.api.cmdb.router.bgp.update(data_dict=config)

# Verify
config = fgt.api.cmdb.router.bgp.get()
# Extract config again (same as step 2)
neighbors = config.get('neighbor', []) if isinstance(config, dict) else []
print(f"BGP now has {len(neighbors)} neighbors")
```

```python
# OSPF Network Management - same pattern
config = fgt.api.cmdb.router.ospf.get()
# Extract config (same pattern as BGP)
if isinstance(config, list):
    config = config[0] if config else {}

networks = config.get('network', [])
networks.append({
    'id': 9999,
    'prefix': '192.168.1.0 255.255.255.0'
})
config['network'] = networks
fgt.api.cmdb.router.ospf.update(data_dict=config)
```

```python
# RIP Network Management
config = fgt.api.cmdb.router.rip.get()
if isinstance(config, list):
    config = config[0]

networks = config.get('network', [])
networks.append({'id': 1, 'prefix': '10.0.0.0 255.0.0.0'})
config['network'] = networks
fgt.api.cmdb.router.rip.update(data_dict=config)
```

**Why This Pattern?**
- FortiOS API design: Routing protocols are singleton objects (only one BGP/OSPF/RIP config per VDOM)
- Nested objects (neighbors, networks, areas) are managed as lists within the main config
- The API requires sending the entire configuration on updates to maintain consistency

**Future Enhancement:**
Helper methods are planned to simplify this pattern:
```python
# Planned for future release (not yet available)
fgt.api.cmdb.router.bgp.add_neighbor(ip='10.0.0.1', remote_as=65001)
fgt.api.cmdb.router.bgp.remove_neighbor('10.0.0.1')
fgt.api.cmdb.router.bgp.list_neighbors()
```

**Affected Endpoints:**
- `router/bgp` - BGP neighbors, networks, aggregate addresses, VRFs
- `router/ospf` - OSPF areas, interfaces, networks, neighbors
- `router/ospf6` - OSPFv3 areas, interfaces
- `router/rip` - RIP networks, neighbors, interfaces
- `router/ripng` - RIPng networks, neighbors
- `router/isis` - IS-IS NETs, interfaces
- `router/bfd` - BFD neighbors (IPv4)
- `router/bfd6` - BFD neighbors (IPv6)

See the test files in the development workspace for complete working examples.
```

### Helper Methods - Safe Existence Checking ✨

The `.exists()` helper method provides safe existence checking on 288 CMDB endpoints without raising exceptions:

```python
from hfortix import FortiOS

fgt = FortiOS(host='192.168.1.99', token='your-token', verify=False)

# Check if object exists before operations
if fgt.api.cmdb.firewall.address.exists('web-server'):
    print("Address already exists")
    fgt.api.cmdb.firewall.address.update('web-server', comment='Updated')
else:
    print("Creating new address")
    fgt.api.cmdb.firewall.address.create(
        name='web-server',
        subnet='10.0.1.100/32'
    )

# Safe deletion pattern
if fgt.api.cmdb.user.local.exists('testuser'):
    fgt.api.cmdb.user.local.delete('testuser')

# Conditional processing
users = ['alice', 'bob', 'charlie']
for user in users:
    if not fgt.api.cmdb.user.local.exists(user):
        fgt.api.cmdb.user.local.create(
            name=user,
            type='password',
            passwd='SecureP@ss123'
        )
```

**Available on:** 288 endpoints with full CRUD operations (firewall addresses, policies, users, VPN configs, etc.)

**📚 Complete Documentation:**
- See [HELPER_METHODS.md](HELPER_METHODS.md) for detailed guide with examples
- See [ENDPOINT_METHODS.md](ENDPOINT_METHODS.md) for complete API method reference

### Exception Hierarchy
```
Exception
└── FortinetError (base)
    ├── AuthenticationError
    ├── AuthorizationError
    └── APIError
        ├── ResourceNotFoundError (404)
        ├── BadRequestError (400)
        ├── MethodNotAllowedError (405)
        ├── RateLimitError (429)
        ├── ServerError (500)
        ├── DuplicateEntryError (-5, -15, -100)
        ├── EntryInUseError (-23, -94, -95)
        ├── InvalidValueError (-651, -1, -50)
        └── PermissionDeniedError (-14, -37)
```

## 🧪 Testing

**Note:** This SDK is currently in beta (v0.3.x). All endpoints are functional but will remain in beta status until version 1.0.0 with comprehensive unit test coverage.

**Current Status:**
- All implemented endpoints are tested against live FortiGate devices
- Integration testing performed during development
- Unit test framework planned for v1.0.0 release

## 📝 Version

Current version: **0.3.12** (See [CHANGELOG.md](CHANGELOG.md) for release notes)

```python
from hfortix import get_version
print(get_version())
```

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests

For code contributions:
1. Fork the repository
2. Create a feature branch
3. Make your changes with proper tests
4. Submit a pull request with clear description

## 📄 License

Proprietary License - Free for personal, educational, and business use.

**You may:**
- Use for personal projects and learning
- Use in your business operations
- Deploy in client environments
- Use in managed services and technical support

**You may not:**
- Sell the software itself as a standalone product
- Redistribute as your own product

See [CHANGELOG.md](CHANGELOG.md) v0.2.0 for details.

## 🔗 Links

- [FortiOS API Documentation](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide)
- [FortiManager API Documentation](https://docs.fortinet.com/document/fortimanager)
- [FortiAnalyzer API Documentation](https://docs.fortinet.com/document/fortianalyzer)

## 💡 Tips

- **Use API Tokens**: Only token-based authentication is supported for FortiOS REST API
- **Error Handling**: Always catch specific exceptions for better error handling
- **Verify SSL**: Set `verify=True` in production (requires valid certificates)
- **Automatic Retries**: Built-in retry logic handles transient failures (429, 500, 502, 503, 504)
- **Connection Pooling**: HTTP/2 support with connection multiplexing for better performance
- **Timeout Configuration**: Customize `connect_timeout` and `read_timeout` for your environment
- **Logging**: Use `hfortix.set_log_level('INFO')` for request/response debugging

## ⚙️ Configuration

### Environment Variables
```bash
export FGT_HOST="192.168.1.99"
export FGT_TOKEN="your-api-token"
export FGT_VERIFY_SSL="false"
```

### Using .env File
```python
from dotenv import load_dotenv
import os

load_dotenv()

fgt = FortiOS(
    host=os.getenv('FGT_HOST'),
    token=os.getenv('FGT_TOKEN'),
    verify=os.getenv('FGT_VERIFY_SSL', 'false').lower() == 'true'
)
```

## 🎯 Roadmap

- [🚧] FortiOS API implementation (In Development)
  - [x] Exception handling system (387 error codes)
  - [x] Base client architecture with HTTP/2, retry logic, circuit breaker
  - [🔷] CMDB endpoints (Beta - 57.5% coverage, 23/40 categories)
    - [🔷] Firewall (address, policy, service, DoS, ICAP, IPS, etc.) - Beta
    - [🔷] System (interface, admin, global, etc.) - Beta
    - [🔷] Router (static, bgp, ospf, rip, isis, etc.) - **NEW** Beta ⚠️ See note below
    - [🔷] VPN (IPsec, SSL, etc.) - Beta
    - [🔷] Log (disk, syslog, fortianalyzer, etc.) - Beta
    - [🔷] Wireless Controller, User, Web Filter, Application - Beta
    - [ ] Remaining 17 categories (Switch Controller, WAD, etc.)
  - [🔷] Monitor endpoints (Beta - 18% coverage, 6/33 categories)
    - [🔷] Firewall, Endpoint Control, Azure, CASB, Extender - Beta
    - [ ] Remaining 27 categories
  - [🔷] Service endpoints (Beta - 100% coverage, 3/3 categories)
    - Sniffer, Security Rating, etc.
  - [🔷] Log endpoints (Beta - 100% coverage, 5/5 categories)
    - Traffic, Event, Virus, etc.
- [x] Modular package architecture
- [x] PyPI package publication (hfortix on PyPI)
- [ ] FortiManager module (Not Started)
- [ ] FortiAnalyzer module (Not Started)
- [ ] Helper methods for singleton routing endpoints (Planned)
- [x] Async/await support (Implemented in v0.3.15)
- [ ] CLI tool (Planned)

### ⚠️ Important Note: Singleton Routing Endpoints (Beta)

**Routing protocol configurations (BGP, OSPF, RIP, ISIS, etc.) use a different pattern than collection endpoints:**

- **Collection Endpoints** (addresses, policies, etc.): Use standard CRUD operations
  ```python
  # Simple add/remove pattern
  fgt.api.cmdb.firewall.address.create(name='test', subnet='192.168.1.0/24')
  fgt.api.cmdb.firewall.address.delete('test')
  ```

- **Singleton Endpoints** (bgp, ospf, rip, isis, etc.): Require GET→Modify→PUT pattern
  ```python
  # Must get entire config, modify, and send back
  config = fgt.api.cmdb.router.bgp.get()
  config['neighbor'].append({'ip': '10.0.0.1', 'remote-as': 65001})
  fgt.api.cmdb.router.bgp.update(data_dict=config)
  ```

**Why?** This is a FortiOS API design - routing protocols are singleton objects with nested lists (neighbors, networks, areas). The API requires sending the entire configuration on updates.

**Future Enhancement:** Helper methods like `add_neighbor()`, `remove_neighbor()`, `list_neighbors()` are planned to simplify this pattern.

**Affected Endpoints:**
- `router/bgp` - BGP neighbors, networks, VRFs
- `router/ospf` - OSPF areas, interfaces, networks
- `router/ospf6` - OSPFv3 configuration
- `router/rip` - RIP networks, neighbors
- `router/ripng` - RIPng configuration
- `router/isis` - IS-IS NETs, interfaces
- `router/bfd` - BFD neighbors (IPv4)
- `router/bfd6` - BFD neighbors (IPv6)

**All implementations remain in BETA until version 1.0.0 with comprehensive unit test coverage.**

---

## 👤 Author

**Herman W. Jacobsen**
- Email: herman@wjacobsen.fo
- LinkedIn: [linkedin.com/in/hermanwjacobsen](https://www.linkedin.com/in/hermanwjacobsen/)
- GitHub: [@hermanwjacobsen](https://github.com/hermanwjacobsen)

---

**Built with ❤️ for the Fortinet community**
