# Fortinet Python SDK

Python client library for Fortinet products including FortiOS, FortiManager, and FortiAnalyzer.

## 🎯 Features

- **Modular Architecture**: Each product module can be used independently or together
- **Flexible Installation**: Clone individual modules or the complete package
- **Comprehensive Exception Handling**: 387+ FortiOS error codes with detailed descriptions
- **Type-Safe**: Proper exception hierarchy and error handling
- **Well-Documented**: Extensive API documentation and examples

## 📦 Available Modules

| Module | Status | Description |
|--------|--------|-------------|
| **FortiOS** | 🚧 In Development | FortiGate firewall management API |
| **FortiManager** | ⏸️ Not Started | Centralized management for FortiGate devices |
| **FortiAnalyzer** | ⏸️ Not Started | Log analysis and reporting platform |

## 🚀 Installation Options

### Option 1: Complete Package (All Modules)
```bash
git clone https://github.com/your-org/fortinet-sdk.git
cd fortinet-sdk
pip install -e .
```

### Option 2: FortiOS Only (Standalone)
```bash
git clone https://github.com/your-org/fortinet-sdk.git
cd fortinet-sdk/FortiOS
# Use FortiOS as standalone module
```

## 📖 Usage

### Import from Complete Package
```python
from fortinet import FortiOS, FortinetError, APIError

# Initialize client
fgt = FortiOS(
    host='192.168.1.99',
    token='your-api-token',
    verify=False
)

# Use the API
result = fgt.cmdb.firewall.address.list()
```

### Import as Standalone Module
```python
from FortiOS import FortiOS

# Same usage as above
fgt = FortiOS(host='192.168.1.99', token='your-api-token')
```

### Exception Handling
```python
from fortinet import (
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
from fortinet import FortiOS

fgt = FortiOS(host='192.168.1.99', token='your-token')

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

**Built with ❤️ for the Fortinet community**
