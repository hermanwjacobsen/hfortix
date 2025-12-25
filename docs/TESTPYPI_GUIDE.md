# Using PyPI Test Server

## Overview
TestPyPI is a separate instance of PyPI for testing package uploads before publishing to the real PyPI.

## Quick Start (Recommended)

### 1. Set Up Token in .env File
```bash
# Copy the example file
cd X/
cp .env.example .env

# Edit .env and add your TestPyPI token
# Get token from: https://test.pypi.org/manage/account/token/
```

Your `X/.env` file should contain:
```bash
TESTPYPI_TOKEN="pypi-AgENdGVzdC5weXBpLm9yZw..."
```

### 2. Run the Upload Script
```bash
# From the repository root
./upload_to_testpypi.sh 0.3.34.dev1
```

The script will automatically use the token from `X/.env`, so no need to type it each time!

## Manual Setup (Alternative)

### 1. Create TestPyPI Account
- Go to https://test.pypi.org/
- Register for a new account (separate from your PyPI account)
- Verify your email
- Generate an API token at https://test.pypi.org/manage/account/token/

### 2. Configure `.pypirc` for TestPyPI

Create/edit `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-<your-production-token>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-<your-testpypi-token>
```

## Uploading to TestPyPI

### Build the Package
```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build the package
python -m build
```

### Upload to TestPyPI
```bash
# Upload using twine
python -m twine upload --repository testpypi dist/*

# Or specify explicitly
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

### Upload Specific Version
```bash
# Upload only wheel
python -m twine upload --repository testpypi dist/hfortix-0.3.33-py3-none-any.whl

# Upload only source distribution
python -m twine upload --repository testpypi dist/hfortix-0.3.33.tar.gz
```

## Installing from TestPyPI

### On Another System

```bash
# Install from TestPyPI (basic)
pip install --index-url https://test.pypi.org/simple/ hfortix

# Install specific version
pip install --index-url https://test.pypi.org/simple/ hfortix==0.3.33

# Install with dependencies from regular PyPI
# (TestPyPI doesn't have all packages, so dependencies come from PyPI)
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hfortix
```

### In a Virtual Environment (Recommended)

```bash
# Create fresh virtual environment
python -m venv test-env
source test-env/bin/activate  # On Windows: test-env\Scripts\activate

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hfortix

# Test the installation
python -c "import hfortix; print(hfortix.__version__)"
```

## Complete Workflow Example

### On Development System (Upload)

```bash
# 1. Update version in setup.py and pyproject.toml
# For example: 0.3.34-test1

# 2. Clean and build
rm -rf dist/ build/ *.egg-info
python -m build

# 3. Upload to TestPyPI
python -m twine upload --repository testpypi dist/*
```

### On Test System (Install)

```bash
# 1. Create isolated environment
python -m venv test-install
source test-install/bin/activate

# 2. Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hfortix==0.3.34-test1

# 3. Test imports
python -c "from hfortix import FortiOS; print('Success!')"

# 4. Run your tests
python your_test_script.py

# 5. Cleanup
deactivate
rm -rf test-install
```

## Important Notes

### Version Numbers
- TestPyPI and PyPI share the same version namespace
- Once you upload version `0.3.33` to TestPyPI, you can't upload it again
- Use test suffixes for TestPyPI: `0.3.33-test1`, `0.3.33-test2`, etc.
- Or use development versions: `0.3.34.dev1`, `0.3.34.dev2`, etc.

### Dependencies
- TestPyPI doesn't have all packages that regular PyPI has
- Always use `--extra-index-url https://pypi.org/simple/` to install dependencies from regular PyPI
- Your package will be from TestPyPI, but dependencies will come from regular PyPI

### Limitations
- TestPyPI is periodically cleaned (old packages may be deleted)
- Not suitable for long-term hosting
- Only for testing package distribution

## Best Practices

### 1. Test Version Naming
```python
# setup.py - for testing
version="0.3.34.dev1"  # Development version

# OR
version="0.3.34rc1"  # Release candidate

# OR
version="0.3.34a1"  # Alpha version
```

### 2. Full Test Workflow
```bash
#!/bin/bash
# test_pypi_upload.sh

# Set version
VERSION="0.3.34.dev1"

# Clean
echo "Cleaning old builds..."
rm -rf dist/ build/ *.egg-info

# Build
echo "Building package..."
python -m build

# Upload to TestPyPI
echo "Uploading to TestPyPI..."
python -m twine upload --repository testpypi dist/*

# Create test environment
echo "Creating test environment..."
python -m venv /tmp/test-hfortix
source /tmp/test-hfortix/bin/activate

# Install from TestPyPI
echo "Installing from TestPyPI..."
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hfortix==$VERSION

# Test
echo "Testing installation..."
python -c "import hfortix; print(f'Installed version: {hfortix.__version__}')"
python -c "from hfortix import FortiOS; print('FortiOS import: OK')"

# Cleanup
deactivate
rm -rf /tmp/test-hfortix

echo "Test complete!"
```

### 3. Windows Testing
```batch
REM test_pypi_install.bat

REM Create test environment
python -m venv test-env
call test-env\Scripts\activate.bat

REM Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hfortix==0.3.34.dev1

REM Test
python -c "import hfortix; print('Success!')"

REM Cleanup
deactivate
rmdir /s /q test-env
```

## Verification

### Check Package on TestPyPI
- Visit: https://test.pypi.org/project/hfortix/
- Verify version, description, and metadata
- Check that all files uploaded correctly

### Common Issues

**Issue:** "File already exists"
**Solution:** You can't re-upload the same version. Increment version number.

**Issue:** Dependencies not found
**Solution:** Add `--extra-index-url https://pypi.org/simple/`

**Issue:** "Invalid credentials"
**Solution:** Make sure you're using the TestPyPI token, not your PyPI token

## Moving to Production

Once tested on TestPyPI:

```bash
# 1. Update version to release number (no dev/test suffix)
# setup.py: version="0.3.34"

# 2. Rebuild
rm -rf dist/ build/ *.egg-info
python -m build

# 3. Upload to REAL PyPI
python -m twine upload dist/*

# 4. Install from real PyPI
pip install --upgrade hfortix
```

## Quick Commands Reference

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Install from TestPyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hfortix

# Upgrade from TestPyPI
pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ hfortix

# Uninstall
pip uninstall hfortix
```
