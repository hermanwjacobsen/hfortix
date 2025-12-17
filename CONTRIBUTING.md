# Contributing to hfortix

Thank you for your interest in contributing to hfortix! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Code Style](#code-style)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Issue Guidelines](#issue-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)

## Code of Conduct

By participating in this project, you are expected to uphold a professional and respectful environment. Be kind, constructive, and considerate in all interactions.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/hfortix.git
   cd hfortix
   ```
3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/hermanwjacobsen/hfortix.git
   ```

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- git

### Install Dependencies

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the package in development mode with dev dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

This will install:
- `httpx[http2]` - HTTP client with HTTP/2 support
- `pytest` - Testing framework
- `pytest-cov` - Code coverage plugin
- `black` - Code formatter
- `flake8` - Linter
- `mypy` - Type checker
- `python-dotenv` - Environment variable management

## Making Changes

1. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Make your changes** following the code style guidelines

3. **Test your changes** thoroughly

4. **Commit your changes** with clear, descriptive commit messages:
   ```bash
   git commit -m "Add feature: description of what you added"
   # or
   git commit -m "Fix: description of what you fixed"
   ```

## Code Style

This project follows standard Python conventions and uses several tools to maintain code quality:

### Black (Code Formatter)

All code must be formatted with Black:
```bash
black .
```

Check formatting without making changes:
```bash
black --check .
```

### Flake8 (Linter)

Code must pass flake8 linting:
```bash
flake8 hfortix tests
```

### Mypy (Type Checker)

Type hints are required for all public APIs:
```bash
mypy hfortix --ignore-missing-imports
```

### General Guidelines

- Use type hints for function parameters and return values
- Write docstrings for all public classes and functions (Google style)
- Keep line length to 127 characters maximum
- Use descriptive variable and function names
- Follow PEP 8 conventions
- Add comments for complex logic

### Example

```python
from typing import Optional, Dict, Any


def get_firewall_policy(
    policy_id: str,
    vdom: str = "root"
) -> Optional[Dict[str, Any]]:
    """Get a specific firewall policy by ID.
    
    Args:
        policy_id: The policy ID to retrieve.
        vdom: Virtual domain name. Defaults to "root".
    
    Returns:
        Dictionary containing the policy data, or None if not found.
    
    Raises:
        APIError: If the API request fails.
    """
    # Implementation here
    pass
```

## Testing

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=hfortix --cov-report=term --cov-report=html
```

Run specific test file:
```bash
pytest tests/test_specific.py
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files as `test_*.py`
- Name test functions as `test_*`
- Use descriptive test names that explain what is being tested
- Include both positive and negative test cases
- Mock external API calls
- Aim for high test coverage

### Example Test

```python
import pytest
from hfortix import FortiOSClient


def test_client_initialization():
    """Test that FortiOS client initializes correctly."""
    client = FortiOSClient(
        host="192.168.1.99",
        api_key="test-key"
    )
    assert client.host == "192.168.1.99"
    assert client.api_key == "test-key"


def test_client_missing_credentials():
    """Test that client raises error with missing credentials."""
    with pytest.raises(ValueError):
        FortiOSClient(host="192.168.1.99")
```

## Submitting Changes

1. **Push your changes** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub:
   - Go to the original hfortix repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template completely
   - Link any related issues

3. **Wait for review**:
   - Address any feedback from maintainers
   - Keep your PR updated with the main branch
   - Be responsive to comments and questions

## Issue Guidelines

### Before Creating an Issue

- Search existing issues to avoid duplicates
- Check the documentation and README
- Verify you're using the latest version

### Creating an Issue

Use the appropriate issue template:

- **Bug Report**: For reporting bugs or unexpected behavior
- **Feature Request**: For suggesting new features or improvements
- **Question**: For asking questions or starting discussions

Provide as much detail as possible:
- Clear description of the issue/request
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Environment details (Python version, OS, FortiOS version)
- Error messages and stack traces
- Code samples when relevant

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows the project style guidelines
- [ ] All tests pass locally
- [ ] New tests added for new functionality
- [ ] Documentation updated if needed
- [ ] Commits are clear and descriptive
- [ ] Branch is up to date with main

### PR Requirements

- Fill out the PR template completely
- Link related issues
- Include a clear description of changes
- Add tests for new functionality
- Update documentation as needed
- Ensure CI checks pass

### Review Process

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, your PR will be merged
4. Your contribution will be included in the next release

## Development Tips

### Working with FortiOS API

- Always test against a development/test FortiGate device
- Never commit API keys or credentials
- Use environment variables for sensitive data (python-dotenv)
- Reference the [FortiOS REST API documentation](https://docs.fortinet.com/document/fortigate/latest/rest-api-reference)

### Adding New Endpoints

When adding support for new FortiOS API endpoints:

1. Follow the existing package structure (`hfortix/FortiOS/api/v2/cmdb/...`)
2. Use consistent naming conventions
3. Add comprehensive docstrings
4. Include type hints
5. Add error handling
6. Write tests
7. Update documentation

### Environment Variables

For testing, create a `.env` file (not committed):
```
FORTIOS_HOST=192.168.1.99
FORTIOS_API_KEY=your-api-key-here
FORTIOS_VERIFY_SSL=false
```

## Getting Help

- Check the [README](README.md) for basic usage
- Review existing [issues](https://github.com/hermanwjacobsen/hfortix/issues)
- Create a [question issue](https://github.com/hermanwjacobsen/hfortix/issues/new/choose)
- Visit the [Fortinet Community Forums](https://community.fortinet.com/)

## License

By contributing to hfortix, you agree that your contributions will be licensed under the MIT License.

## Thank You!

Your contributions help make hfortix better for everyone. We appreciate your time and effort!
