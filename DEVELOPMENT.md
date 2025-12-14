# Development Guide

This guide covers how to set up your development environment and contribute to the Fortinet Python SDK.

## � Project Status (December 14, 2025)

- **Version**: 0.2.0
- **CMDB Endpoints**: 51 endpoints across 14 categories
- **Test Coverage**: Comprehensive tests for all endpoints
- **Python Version**: 3.9+
- **Type Hints**: Full type hint support with modern syntax

## �🚀 Quick Start for Developers

### 1. Clone the Repository

```bash
git clone https://github.com/hermanwjacobsen/hfortix.git
cd hfortix
```

### 2. Set Up Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e .[dev]
```

### 3. Configure FortiGate Access

Create a `.env` file in the project root (never commit this file!):

```bash
# .env
FGT_HOST=192.168.1.99
FGT_TOKEN=your-api-token-here
FGT_VERIFY_SSL=false
```

**Security Note:** The `.env` file is in `.gitignore` to prevent accidental commits of credentials.

### 4. Test Your Setup

```python
from fortinet import FortiOS, get_available_modules

# Check available modules
print(get_available_modules())

# Create client
fgt = FortiOS(host='192.168.1.99', token='your-token', verify=False)

# Test connection
result = fgt.cmdb.system.interface.list()
print(f"Connected! Found {len(result.get('results', []))} interfaces")
```

---

## 📁 Project Structure

```
fortinet/
├── __init__.py                 # Main package entry point
├── exceptions.py               # Base exceptions (all products)
├── exceptions_forti.py         # FortiOS-specific exceptions
├── FortiOS/                    # FortiOS module
│   ├── __init__.py
│   ├── client.py              # Main FortiOS client
│   ├── exceptions.py          # Backward compatibility
│   └── api/                   # API endpoints
│       └── v2/
│           ├── cmdb/          # Configuration endpoints
│           ├── monitor/       # Monitoring endpoints (TODO)
│           ├── log/           # Log endpoints
│           └── service/       # Service endpoints
├── FortiManager/              # FortiManager module (placeholder)
│   └── __init__.py
└── FortiAnalyzer/             # FortiAnalyzer module (placeholder)
    └── __init__.py
```

---

## 🛠️ Development Workflow

### Creating a New Endpoint

#### Step 1: Check the API Documentation

Find the endpoint in the [FortiOS API documentation](https://fndn.fortinet.net):
- Note the HTTP methods supported (GET, POST, PUT, DELETE)
- Identify required and optional parameters
- Check for any special behaviors or quirks

#### Step 2: Create the Module File

Location: `/app/dev/classes/fortinet/FortiOS/api/v2/cmdb/{category}/{endpoint}.py`

```python
"""
{Endpoint description}

API Path: /api/v2/cmdb/{category}/{endpoint}
"""

class EndpointName:
    """
    {Detailed description}
    
    This endpoint manages {what it does}.
    """
    
    def __init__(self, client):
        """Initialize the endpoint with API client"""
        self._client = client
        self._path = '{category}/{endpoint}'
    
    def list(self, vdom='root', **params):
        """
        Get list of {endpoint} objects
        
        Args:
            vdom (str): Virtual domain name (default: 'root')
            **params: Additional query parameters
                - filter (str): Filter results
                - count (int): Limit number of results
                - offset (int): Start position
                
        Returns:
            dict: API response containing:
                - results (list): List of objects
                - vdom (str): Virtual domain
                - status (str): Response status
                
        Raises:
            APIError: If API request fails
            
        Example:
            >>> result = fgt.cmdb.{category}.{endpoint}.list()
            >>> for item in result['results']:
            ...     print(item['name'])
        """
        return self._client.get(f'cmdb/{self._path}', vdom=vdom, params=params)
    
    # Add get, create, update, delete methods as appropriate
```

#### Step 3: Update the Category __init__.py

Add import and initialize in `/app/dev/classes/fortinet/FortiOS/api/v2/cmdb/{category}/__init__.py`:

```python
from .endpoint_name import EndpointName

class Category:
    def __init__(self, client):
        self._client = client
        # ... other endpoints ...
        self.endpoint_name = EndpointName(client)
```

#### Step 4: Create Test File

Create a test script to verify your implementation:

```python
"""
Test script for {category}/{endpoint}

This test requires FortiGate access configured in .env file
"""

import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).resolve().parents[5]))

from init_client import fgt

def test_crud_operations():
    """Test CRUD operations for {endpoint}"""
    print("=" * 60)
    print("Testing: {category}/{endpoint}")
    print("=" * 60)
    
    # Test LIST
    print("\n1. LIST all {endpoint} objects")
    result = fgt.cmdb.{category}.{endpoint}.list()
    print(f"   Found {len(result.get('results', []))} objects")
    
    # Test CREATE
    print("\n2. CREATE new {endpoint}")
    test_data = {
        'name': 'test-object',
        # ... other required fields
    }
    result = fgt.cmdb.{category}.{endpoint}.create(test_data)
    print(f"   Created: {result}")
    
    # Test UPDATE
    print("\n3. UPDATE {endpoint}")
    update_data = {
        'comment': 'Updated by test script'
    }
    result = fgt.cmdb.{category}.{endpoint}.update('test-object', update_data)
    print(f"   Updated: {result}")
    
    # Test GET
    print("\n4. GET specific {endpoint}")
    result = fgt.cmdb.{category}.{endpoint}.get('test-object')
    print(f"   Retrieved: {result['results'][0]['name']}")
    
    # Test DELETE
    print("\n5. DELETE {endpoint}")
    result = fgt.cmdb.{category}.{endpoint}.delete('test-object')
    print(f"   Deleted: {result}")
    
    print("\n✅ All tests completed successfully!")

if __name__ == '__main__':
    try:
        test_crud_operations()
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
```

#### Step 5: Run Tests

Test your implementation with your FortiGate environment.

#### Step 6: Update Documentation

- Add endpoint to `API_COVERAGE.md`
- Update `CHANGELOG.md` under [Unreleased]
- Add examples to README if significant

---

## 🧪 Testing

### Integration Tests

Integration tests require actual FortiGate access. Test your implementations with your own FortiGate environment.

### Unit Tests (Future)

We plan to add unit tests with mocking:

```bash
pytest tests/unit/
pytest tests/unit/ --cov=fortinet --cov-report=html
```

---

## 🎨 Code Style

### Use Black for Formatting

```bash
# Format all Python files
black fortinet/

# Check without modifying
black --check fortinet/
```

### Use Flake8 for Linting

```bash
# Run linter
flake8 fortinet/

# With configuration
flake8 --max-line-length=100 --extend-ignore=E203,W503 fortinet/
```

### Use MyPy for Type Checking

```bash
# Check types
mypy fortinet/
```

---

## 🐛 Debugging Tips

### Enable Verbose Logging

```python
import logging

# Enable debug logging for requests
logging.basicConfig(level=logging.DEBUG)
```

### Inspect API Responses

```python
import json

result = fgt.cmdb.firewall.address.list()
print(json.dumps(result, indent=2))
```

### Check FortiOS Logs

```bash
# On FortiGate CLI
diagnose debug application httpsd 5
diagnose debug enable

# Make API request

diagnose debug disable
```

### Common Issues

**Import Errors:**
```bash
# Make sure you're in the right directory
cd /app/dev/classes/fortinet
python3 -m fortinet
```

**Authentication Failures:**
```bash
# Check token validity
curl -k -H "Authorization: Bearer YOUR_TOKEN" \
  https://fortigate-ip/api/v2/cmdb/system/interface
```

**VDOM Issues:**
```python
# Specify VDOM explicitly
result = fgt.cmdb.firewall.address.list(vdom='root')
```

---

## 📦 Building the Package

### Install Build Tools

```bash
pip install build twine
```

### Build Distribution

```bash
# Build source and wheel distributions
python3 -m build

# Outputs to dist/:
# - hfortix-0.1.0.tar.gz
# - hfortix-0.1.0-py3-none-any.whl
```

### Test Installation

```bash
# Install from local build
pip install dist/hfortix-0.1.0-py3-none-any.whl

# Test import
python3 -c "from FortiOS import FortiOS; print('Success!')"
```

### Upload to PyPI (when ready)

```bash
# Test PyPI first
twine upload --repository testpypi dist/*

# Production PyPI
twine upload dist/*
```

---

## 🔄 Git Workflow

### Branch Strategy

```bash
# Create feature branch
git checkout -b feature/add-firewall-policy

# Make changes, commit
git add .
git commit -m "feat: add firewall policy endpoint"

# Push to remote
git push origin feature/add-firewall-policy
```

### Commit Message Format

Follow conventional commits:

```
feat: add new feature
fix: bug fix
docs: documentation changes
style: formatting, missing semicolons, etc
refactor: code restructuring
test: adding tests
chore: maintenance tasks
```

Examples:
```
feat: add firewall.policy endpoint with full CRUD
fix: handle empty results in address.list()
docs: update API_COVERAGE with new endpoints
refactor: extract common CRUD methods to base class
```

---

## 📚 Resources

### Official Documentation
- [FortiOS Administration Guide](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide)
- [FortiOS REST API Reference](https://fndn.fortinet.net)
- [Fortinet Developer Network](https://fndn.fortinet.net)

### Python Resources
- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 8 Style Guide](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

### Tools
- [Black Code Formatter](https://black.readthedocs.io/)
- [Flake8 Linter](https://flake8.pycqa.org/)
- [MyPy Type Checker](http://mypy-lang.org/)
- [pytest Testing Framework](https://pytest.org/)

---

## 🆘 Getting Help

- **Issues:** [GitHub Issues](https://github.com/hermanwjacobsen/hfortix/issues)
- **Discussions:** [GitHub Discussions](https://github.com/hermanwjacobsen/hfortix/discussions)
- **Email:** herman@wjacobsen.fo
- **LinkedIn:** [Herman W. Jacobsen](https://www.linkedin.com/in/hermanwjacobsen/)

---

## ✅ Pre-Commit Checklist

Before submitting a PR:

- [ ] Code follows style guidelines (Black, Flake8)
- [ ] All tests pass
- [ ] Documentation updated (README, API_COVERAGE, CHANGELOG)
- [ ] Commit messages follow conventions
- [ ] No credentials or sensitive data in commits
- [ ] `.gitignore` patterns respected

---

Happy coding! 🎉
