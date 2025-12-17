# HFortix - Fortinet Python SDK

Python client library for Fortinet products including FortiOS, FortiManager, and FortiAnalyzer.

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)

## 🎯 Current Status

**⚠️ BETA STATUS**: All implementations are functional but in beta. APIs work correctly but may have incomplete parameter coverage or undiscovered edge cases.

**FortiOS 7.6.5 Coverage (December 17, 2025):**

- **CMDB API**: 23 of 40 categories (57.5% coverage) - 200+ endpoints 🔷 Beta
- **Monitor API**: 6 of 33 categories (18% coverage) - 50+ endpoints 🔷 Beta
- **Log API**: 5 of 5 categories (100% coverage) - Log reading functionality 🔷 Beta
- **Service API**: 3 of 3 categories (100% coverage) - 21 methods 🔷 Beta
- **Overall**: 37 of 77 categories (48% coverage) - 250+ API methods

**Note:** All implementations remain in beta until version 1.0.0 with comprehensive unit test coverage.

**🔥 Recent Highlights:**
- ✨ **Enhanced Reliability** (v0.3.11+): Automatic retry logic with exponential backoff, HTTP/2 support, connection pooling
- ✨ **Monitor API** (v0.3.11): 6 categories with 50+ monitoring endpoints (firewall stats, sessions, EMS, etc.)
- ✨ **Log Configuration** (v0.3.11): 56 endpoints for comprehensive logging setup
- ✨ **Firewall Expansion** (v0.3.11): FTP proxy, ICAP, IPS, DoS policies, access-proxy (WAF)
- ✨ **Configurable Timeouts** (v0.3.10): Customize connection and read timeouts for slow networks
- ✨ **URL Encoding** (v0.3.10): Automatic handling of special characters in object names
- ✨ **Full Response Access** (v0.3.9): `raw_json=True` parameter on all 250+ API methods
- ✨ **Advanced Logging** (v0.3.9): Global and per-instance logging with automatic data sanitization

**📖 Full release notes:** See [CHANGELOG.md](CHANGELOG.md) for complete version history.

**Latest Features (v0.3.11):**
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
- **Enhanced IDE Support**: Full type hints with PEP 561 compliance for excellent autocomplete
- **Modular Architecture**: Each product module can be used independently
- **PyPI Installation**: `pip install hfortix` - simple and straightforward
- **Comprehensive Exception Handling**: 387+ FortiOS error codes with detailed descriptions
- **Automatic Retry Logic**: Built-in retry mechanism with exponential backoff for transient failures
- **HTTP/2 Support**: Modern HTTP client with connection multiplexing for improved performance
- **Type-Safe**: Proper exception hierarchy and error handling
- **Simplified APIs**: Auto-conversion for common patterns (e.g., address group members)
- **Well-Documented**: Extensive API documentation and examples
- **Modern Python**: Type hints, PEP 585 compliance, Python 3.8+

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

Current version: **0.3.11** (See [CHANGELOG.md](CHANGELOG.md) for release notes)

```python
from hfortix import get_version
print(get_version())
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

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
  - [x] Base client architecture
  - [🔷] CMDB endpoints (Beta - partial coverage)
    - Firewall (address, policy, service, etc.)
    - System (interface, admin, global, etc.)
    - Router (static, policy, etc.)
    - VPN (IPsec, SSL, etc.)
  - [🔷] Service endpoints (Beta)
    - Sniffer, Security Rating, etc.
  - [🔷] Log endpoints (Beta)
    - Traffic, Event, Virus, etc.
  - [ ] Monitor endpoints (Not Started)
  - [ ] Complete API coverage
- [x] Modular package architecture
- [ ] FortiManager module (Not Started)
- [ ] FortiAnalyzer module (Not Started)
- [ ] PyPI package publication
- [ ] Async support
- [ ] CLI tool

---

## 👤 Author

**Herman W. Jacobsen**
- Email: herman@wjacobsen.fo
- LinkedIn: [linkedin.com/in/hermanwjacobsen](https://www.linkedin.com/in/hermanwjacobsen/)
- GitHub: [@hermanwjacobsen](https://github.com/hermanwjacobsen)

---

**Built with ❤️ for the Fortinet community**
