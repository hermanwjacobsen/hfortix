# Contributing to Fortinet Python SDK

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## 🎯 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the behavior
- **Expected vs actual behavior**
- **FortiOS version** you're testing against
- **Python version** and OS
- **Code samples** if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **List any alternative solutions** you've considered

### Adding New Endpoints

We welcome contributions for new FortiOS API endpoints! Here's the process:

1. **Check the API documentation** - Reference the official Fortinet API docs
2. **Follow the existing pattern** - Look at similar endpoints for structure
3. **Include docstrings** - Document all parameters and return values
4. **Add examples** - Test your implementation thoroughly
5. **Update API_COVERAGE.md** - Mark the endpoint as implemented

#### Endpoint Implementation Template

```python
"""
Module for {endpoint_name} configuration
"""

class EndpointName:
    """
    {Brief description of what this endpoint manages}
    
    API Path: /api/v2/cmdb/{path}/{endpoint}
    """
    
    def __init__(self, client):
        self._client = client
        self._path = '{path}/{endpoint}'
    
    def list(self, vdom='root', **params):
        """
        Get list of {endpoint_name} objects
        
        Args:
            vdom: Virtual domain name (default: 'root')
            **params: Additional query parameters
                - filter: Filter results
                - count: Limit number of results
                - offset: Start position
                
        Returns:
            dict: API response with results
            
        Example:
            >>> result = fgt.cmdb.{path}.{endpoint}.list()
            >>> for item in result['results']:
            ...     print(item['name'])
        """
        return self._client.get(f'cmdb/{self._path}', vdom=vdom, params=params)
    
    def get(self, name, vdom='root', **params):
        """
        Get specific {endpoint_name} object by name
        
        Args:
            name: Object name/identifier
            vdom: Virtual domain name (default: 'root')
            **params: Additional query parameters
            
        Returns:
            dict: API response with object details
        """
        return self._client.get(f'cmdb/{self._path}/{name}', vdom=vdom, params=params)
    
    def create(self, data, vdom='root', **params):
        """
        Create new {endpoint_name} object
        
        Args:
            data: Object configuration (dict)
            vdom: Virtual domain name (default: 'root')
            **params: Additional parameters
            
        Returns:
            dict: API response
            
        Example:
            >>> result = fgt.cmdb.{path}.{endpoint}.create({
            ...     'name': 'example',
            ...     'param1': 'value1'
            ... })
        """
        return self._client.post(f'cmdb/{self._path}', json=data, vdom=vdom, params=params)
    
    def update(self, name, data, vdom='root', **params):
        """
        Update existing {endpoint_name} object
        
        Args:
            name: Object name/identifier
            data: Updated configuration (dict)
            vdom: Virtual domain name (default: 'root')
            **params: Additional parameters
            
        Returns:
            dict: API response
        """
        return self._client.put(f'cmdb/{self._path}/{name}', json=data, vdom=vdom, params=params)
    
    def delete(self, name, vdom='root', **params):
        """
        Delete {endpoint_name} object
        
        Args:
            name: Object name/identifier
            vdom: Virtual domain name (default: 'root')
            **params: Additional parameters
            
        Returns:
            dict: API response
        """
        return self._client.delete(f'cmdb/{self._path}/{name}', vdom=vdom, params=params)
```

### Pull Request Process

1. **Fork the repository** and create your branch from `main`
2. **Follow the code style** - Use existing code as reference
3. **Add tests** if applicable
4. **Update documentation** - README, API_COVERAGE, etc.
5. **Update CHANGELOG.md** - Add your changes under [Unreleased]
6. **Commit messages** - Use clear, descriptive commit messages
7. **Submit PR** with description of changes

## 📝 Code Style Guidelines

### Python Style

- Follow **PEP 8** style guide
- Use **4 spaces** for indentation (no tabs)
- Maximum **line length of 100 characters**
- Use **type hints** where appropriate
- Write **clear docstrings** for all public methods

### Naming Conventions

- **Classes**: PascalCase (`FirewallAddress`)
- **Functions/Methods**: snake_case (`get_address_list`)
- **Variables**: snake_case (`address_name`)
- **Constants**: UPPER_SNAKE_CASE (`DEFAULT_VDOM`)
- **Private methods**: prefix with underscore (`_internal_method`)

### Documentation

- Use **Google-style docstrings**
- Include **examples** for complex operations
- Document **all parameters** and return values
- Note any **quirks or special behavior**

Example:
```python
def create(self, data, vdom='root', **params):
    """
    Create a new firewall address object
    
    Args:
        data (dict): Address object configuration containing:
            - name (str): Address object name
            - subnet (str): IP address with subnet mask (e.g., '10.0.0.0/24')
            - comment (str, optional): Description
        vdom (str, optional): Virtual domain name. Defaults to 'root'.
        **params: Additional API parameters
        
    Returns:
        dict: API response with creation status
        
    Raises:
        DuplicateEntryError: If address with same name already exists
        InvalidValueError: If subnet format is invalid
        
    Example:
        >>> result = fgt.cmdb.firewall.address.create({
        ...     'name': 'web-server',
        ...     'subnet': '10.0.1.100/32',
        ...     'comment': 'Production web server'
        ... })
    """
```

## 🧪 Testing

### Integration Tests

- Tests require actual FortiGate access
- Use `.env` file for credentials (never commit credentials!)
- Follow existing test file patterns

### Test File Structure

```python
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from init_client import fgt

def test_endpoint():
    """Test description"""
    print("=" * 60)
    print("Testing: {endpoint_name}")
    print("=" * 60)
    
    # Test operations
    # ...
    
if __name__ == '__main__':
    test_endpoint()
```

## 🐛 Debugging Tips

- Use `print()` for quick debugging in test files
- Check FortiOS logs for API errors
- Verify VDOM settings if commands fail
- Test on non-production FortiGate first
- Check API version compatibility

## 📚 Resources

- [FortiOS API Documentation](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide)
- [FortiOS REST API Reference](https://fndn.fortinet.net)
- [Python PEP 8 Style Guide](https://pep8.org/)
- [Semantic Versioning](https://semver.org/)

## 🤝 Community Guidelines

- **Be respectful** and constructive
- **Help others** learn and contribute
- **Ask questions** when unclear
- **Share knowledge** and best practices
- **Give credit** where due

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Your contributions help make this project better for everyone. Thank you for taking the time to contribute!

---

**Questions?** Feel free to open an issue for discussion.
