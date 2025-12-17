# hfortix

[![PyPI version](https://badge.fury.io/py/hfortix.svg)](https://pypi.org/project/hfortix/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/hermanwjacobsen/hfortix/workflows/CI/badge.svg)](https://github.com/hermanwjacobsen/hfortix/actions/workflows/ci.yml)
[![Codecov](https://codecov.io/gh/hermanwjacobsen/hfortix/branch/main/graph/badge.svg)](https://codecov.io/gh/hermanwjacobsen/hfortix)

Python SDK for Fortinet FortiOS API automation. **BETA status** - functional but incomplete coverage.

## Features

- 🔐 HTTP client with authentication and circuit breaker
- 📦 31+ CMDB categories (router, rule, sctp-filter)
- 📝 Comprehensive type hints and docstrings
- 🚀 Published on PyPI
- 🐍 Python 3.8+ support

## Installation

```bash
pip install hfortix
```

## Quick Start

```python
from hfortix import FortiOSClient

# Initialize client
client = FortiOSClient(
    host="192.168.1.99",
    api_key="your-api-key-here"
)

# Example: Get firewall policies
policies = client.cmdb.firewall.policy.get()
```

## Documentation

For detailed usage instructions and API reference, visit:
- [PyPI Package](https://pypi.org/project/hfortix/)
- [Issue Tracker](https://github.com/hermanwjacobsen/hfortix/issues)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:
- Development setup
- Code style guidelines
- Testing requirements
- Pull request process

### Quick Start for Contributors

```bash
# Clone the repository
git clone https://github.com/hermanwjacobsen/hfortix.git
cd hfortix

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .

# Lint code
flake8 hfortix tests
```

## Support

- 🐛 [Report a bug](https://github.com/hermanwjacobsen/hfortix/issues/new?template=bug_report.yml)
- 💡 [Request a feature](https://github.com/hermanwjacobsen/hfortix/issues/new?template=feature_request.yml)
- ❓ [Ask a question](https://github.com/hermanwjacobsen/hfortix/issues/new?template=question.yml)

## Target Audience

Network engineers automating FortiGate configurations.

## Status

Current version: **0.3.13** (BETA)
- ✅ Functional with HTTP client, auth, and circuit breaker
- ⚠️ Incomplete API coverage
- 🚧 Active development

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Author

Herman W. Jacobsen
- Email: herman@wjacobsen.fo
- GitHub: [@hermanwjacobsen](https://github.com/hermanwjacobsen)

## Acknowledgments

This project automates Fortinet FortiOS configurations through the REST API. For official documentation, visit [Fortinet Documentation](https://docs.fortinet.com/).
