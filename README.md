# HFortix - Fortinet Python SDK

Python client library for Fortinet products including FortiOS, FortiManager, and FortiAnalyzer.

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Current Status

- **CMDB API**: 79 endpoints across 15 categories (52% coverage) ✅
  - **NEW:** Firewall category with 28 endpoints (11 flat + 17 nested)
- **Service API**: 21 methods across 3 modules ✅
- **Log API**: 42 methods across 5 modules (100% complete) ✅
- **Monitor API**: Not yet implemented ⏸️

**Latest Addition (v0.3.3):**
- ✅ **Unified Package Import**: `from hfortix import FortiOS` (new recommended syntax)
- ✅ **Flat Firewall Endpoints (11 endpoints):**
  - firewall/DoS-policy, DoS-policy6 (DoS protection)
  - firewall/access-proxy, access-proxy6 (Reverse proxy/WAF)
  - firewall/access-proxy-ssh-client-cert (SSH certificates)
  - firewall/access-proxy-virtual-host (Virtual hosts)
  - firewall/address, address6 (IPv4/IPv6 addresses)
  - firewall/addrgrp, addrgrp6 (IPv4/IPv6 address groups with simplified API)
  - firewall/address6-template (IPv6 address templates)
- ✅ **Firewall Sub-categories:**
  - firewall.ipmacbinding (setting, table)
  - firewall.schedule (group, onetime, recurring)
  - firewall.service (category, custom, group)
  - firewall.shaper (per-ip-shaper, traffic-shaper)
  - firewall.ssh (host-key, local-ca, local-key, setting)
  - firewall.ssl (setting)
  - firewall.wildcard-fqdn (custom, group)

## 🎯 Features

- **Unified Package**: Import all Fortinet products from a single package
- **Modular Architecture**: Each product module can be used independently
- **PyPI Installation**: `pip install hfortix` - simple and straightforward
- **Comprehensive Exception Handling**: 387+ FortiOS error codes with detailed descriptions
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
addresses = fgt.cmdb.firewall.address.list()
print(f"Found {len(addresses['results'])} addresses")

# Create a new address
result = fgt.cmdb.firewall.address.create(
    name='web-server',
    subnet='192.168.10.50/32',
    comment='Production web server'
)
```

### Exception Handling
```python
from hfortix import (
    FortiOS,
    APIError,
    ResourceNotFoundError,
    DuplicateEntryError
)

try:
    result = fgt.cmdb.firewall.address.create(
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
├── __init__.py              # Main package entry point
├── exceptions.py            # Base exceptions for all products
├── exceptions_forti.py      # FortiOS-specific error codes
├── FortiOS/                 # FortiGate management
│   ├── __init__.py
│   ├── client.py
│   ├── exceptions.py        # Backward compatibility
│   └── api/                 # API endpoints
│       └── v2/
│           ├── cmdb/        # Configuration (firewall, system, etc.)
│           ├── monitor/     # Monitoring endpoints
│           ├── log/         # Log retrieval
│           └── service/     # Services (sniffer, security rating)
├── FortiManager/            # Coming soon
│   └── __init__.py
└── FortiAnalyzer/           # Coming soon
    └── __init__.py
```

## 🔍 Module Discovery

Check which modules are available:

```python
from fortinet import get_available_modules

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
addresses = fgt.cmdb.firewall.address.list()

# Create address
result = fgt.cmdb.firewall.address.create(
    name='web-server',
    subnet='10.0.1.100/32',
    comment='Production web server'
)

# Update address
result = fgt.cmdb.firewall.address.update(
    name='web-server',
    comment='Updated comment'
)

# Delete address
result = fgt.cmdb.firewall.address.delete(name='web-server')
```

### FortiOS - DoS Protection (NEW!)
```python
# Create IPv4 DoS policy with simplified API
result = fgt.cmdb.firewall.dos_policy.create(
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
result = fgt.cmdb.firewall.dos_policy.create(
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
result = fgt.cmdb.firewall.access_proxy.create(
    name='web-proxy',
    vip='web-vip',                    # VIP must be type='access-proxy'
    auth_portal='enable',
    log_blocked_traffic='enable',
    http_supported_max_version='2.0',
    svr_pool_multiplex='enable'
)

# Create virtual host with simplified API
result = fgt.cmdb.firewall.access_proxy_virtual_host.create(
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
result = fgt.cmdb.firewall.address.create(
    name='internal-net',
    type='ipmask',
    subnet='192.168.1.0/24',
    comment='Internal network'
)

# Create IPv4 address (IP range)
result = fgt.cmdb.firewall.address.create(
    name='dhcp-range',
    type='iprange',
    start_ip='192.168.1.100',
    end_ip='192.168.1.200'
)

# Create IPv4 address (FQDN)
result = fgt.cmdb.firewall.address.create(
    name='google-dns',
    type='fqdn',
    fqdn='dns.google.com'
)

# Create IPv6 address
result = fgt.cmdb.firewall.address6.create(
    name='ipv6-internal',
    type='ipprefix',
    ip6='2001:db8::/32',
    comment='IPv6 internal network'
)

# Create address group with simplified API
result = fgt.cmdb.firewall.addrgrp.create(
    name='internal-networks',
    member=['subnet1', 'subnet2', 'subnet3'],  # Simple string list!
    comment='All internal networks'
)

# API automatically converts:
# member=['addr1', 'addr2'] → [{'name': 'addr1'}, {'name': 'addr2'}]

# Create IPv6 address group
result = fgt.cmdb.firewall.addrgrp6.create(
    name='ipv6-internal-networks',
    member=['ipv6-subnet1', 'ipv6-subnet2'],
    comment='All internal IPv6 networks'
)

# Create IPv6 address template
result = fgt.cmdb.firewall.address6_template.create(
    name='ipv6-subnet-template',
    ip6='2001:db8::/32',
    subnet_segment_count=2,
    comment='IPv6 subnet template'
)
```

### FortiOS - Schedule Management
```python
# Create recurring schedule
result = fgt.cmdb.firewall.schedule.recurring.create(
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

result = fgt.cmdb.firewall.schedule.onetime.create(
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

Each module includes comprehensive tests:

```bash
# Run FortiOS tests (requires FortiGate access)
cd FortiOS/Tests
python3 test_exceptions.py
python3 cmdb/firewall/address.py
```

## 📝 Version

Current version: **0.1.0**

```python
from fortinet import get_version
print(get_version())  # '0.1.0'
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📄 License

[Your License Here]

## 🔗 Links

- [FortiOS API Documentation](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide)
- [FortiManager API Documentation](https://docs.fortinet.com/document/fortimanager)
- [FortiAnalyzer API Documentation](https://docs.fortinet.com/document/fortianalyzer)

## 💡 Tips

- **Use API Tokens**: Only token-based authentication is supported for FortiOS REST API
- **Error Handling**: Always catch specific exceptions for better error handling
- **Verify SSL**: Set `verify=True` in production (requires valid certificates)
- **Rate Limiting**: Be aware of API rate limits (HTTP 429 errors)

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
