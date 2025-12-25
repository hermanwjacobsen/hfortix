# Fix for Windows Installation Issue - SOLVED! ✅

## Problem
The error `ModuleNotFoundError: No module named 'hfortix.FortiOS.api.v2.cmdb.system.password_policy'` occurred because:

**Version 0.3.32 on PyPI was missing the `password_policy.py` file!** The `__init__.py` tries to import it, but the file wasn't included in that release.

## Solution - Install Version 0.3.33

**Version 0.3.33 has been published to PyPI with the missing file included!**

Run these commands in your Windows PowerShell or Command Prompt:

```powershell
# 1. Activate your virtual environment
.\.venv\Scripts\activate

# 2. Upgrade to version 0.3.33 (includes the fix)
pip install --upgrade hfortix

# 3. Verify the installation
python -c "from hfortix.FortiOS.api.v2.cmdb.system.password_policy import PasswordPolicy; print('Success!')"
```

### If you still have issues (stale cache):

```powershell
# Complete reinstall with cache clearing:
pip uninstall hfortix -y
pip cache purge
pip install hfortix==0.3.33
```

## Alternative: Install Latest from Source

If the PyPI version still has issues, install directly from the latest wheel:

```powershell
# Download the latest wheel from the repository
# Then install it directly:
pip uninstall hfortix -y
pip install --force-reinstall hfortix-0.3.33-py3-none-any.whl
```

## For Package Maintainer

To fix this permanently, ensure the new version is properly uploaded to PyPI:

```bash
# On Linux development machine:
cd /app/dev/classes/fortinet
source .venv/bin/activate

# Clean old builds
rm -rf dist/ build/ *.egg-info

# Update version number in setup.py (already done: 0.3.33)

# Build fresh packages
python -m build

# Upload to PyPI
python -m twine upload dist/*
```
