# Installation

Install HFortix packages for Fortinet product automation.

## Overview

HFortix is a modular Python SDK for Fortinet products:

- **hfortix-core** - Core HTTP client and exception framework
- **hfortix-fortios** - FortiOS/FortiGate API client (750+ endpoints)
- **hfortix-fortimanager** - FortiManager API client (coming soon)
- **hfortix-fortianalyzer** - FortiAnalyzer API client (coming soon)

## Requirements

- Python 3.10 or higher
- Access to your Fortinet device(s)
- API credentials (token or username/password)

## Installing Packages

### Meta Package (All Products)

Install everything:

```bash
pip install hfortix
```

This installs `hfortix-core` and all available product packages.

### Individual Packages

Install only what you need:

```bash
# Core package only
pip install hfortix-core

# FortiOS/FortiGate
pip install hfortix-fortios

# FortiManager (coming soon)
pip install hfortix-fortimanager

# FortiAnalyzer (coming soon)
pip install hfortix-fortianalyzer
```

### With Optional Dependencies

```bash
# FortiOS with all extras
pip install hfortix[fortios]

# Development dependencies
pip install hfortix[dev]
```

## Development Installation

Clone and install from source:

```bash
git clone https://github.com/hermanwjacobsen/hfortix.git
cd hfortix
pip install -e ".[dev]"
```

## Verifying Installation

```python
import hfortix
print(hfortix.__version__)

# Check specific packages
from hfortix_fortios import FortiOS
from hfortix_core import FortinetError
```

## Next Steps

Choose your product to get started:

- **[FortiOS/FortiGate](../fortios/getting-started/quickstart.md)** - Firewall automation
- **[FortiManager](../fortimanager/index.rst)** - Centralized management (coming soon)
- **[FortiAnalyzer](../fortianalyzer/index.rst)** - Analytics platform (coming soon)

## Upgrading

```bash
# Upgrade all packages
pip install --upgrade hfortix

# Upgrade specific package
pip install --upgrade hfortix-fortios
```

## Uninstalling

```bash
# Remove all HFortix packages
pip uninstall hfortix hfortix-core hfortix-fortios
```

## Next Steps

- [Quickstart Guide](quickstart.md) - Get started in 5 minutes
- [Authentication](authentication.md) - Set up API access
- [User Guide](../user-guide/fortios-overview.md) - Comprehensive documentation
