# Publishing Guide for HFortix Split Packages

**Version:** 0.4.0-dev1  
**Date:** December 31, 2025

## Overview

HFortix is split into three separate PyPI packages that must be published in a specific order due to dependencies.

## Package Structure

```
hfortix-core (no dependencies)
    ↑
hfortix-fortios (depends on hfortix-core)
    ↑
hfortix (meta-package, optional dependencies on fortios)
```

**Note:** The `hfortix` meta-package installs only `hfortix-core` by default. Users can install extras:
- `pip install hfortix` - Core only
- `pip install hfortix[fortios]` - Core + FortiOS
- `pip install hfortix[all]` - Everything

## Prerequisites

1. **Install build tools:**
```bash
pip install --upgrade build twine
```

2. **Configure PyPI credentials:**
   - Option A: Use `~/.pypirc` file
   - Option B: Use GitHub Actions with trusted publishing (recommended)
   - Option C: Use environment variables with API tokens

3. **Clean any previous builds:**
```bash
find packages -type d -name "dist" -exec rm -rf {} +
find packages -type d -name "*.egg-info" -exec rm -rf {} +
find packages -type d -name "build" -exec rm -rf {} +
```

## Publishing Steps

### IMPORTANT: Order Matters!

You **must** publish in this exact order:

1. ✅ **hfortix-core** (first - has no dependencies)
2. ✅ **hfortix-fortios** (second - depends on hfortix-core)
3. ✅ **hfortix** (last - optional dependency on fortios)

### Option 1: Automated Script (Recommended)

Use the provided script:

```bash
# Dry run (see what would happen)
python X/scripts/publish_split_packages.py --dry-run

# Test on TestPyPI first
python X/scripts/publish_split_packages.py --test

# Publish to production PyPI
python X/scripts/publish_split_packages.py
```

**Script features:**
- ✅ Builds all packages automatically
- ✅ Publishes in correct order
- ✅ Waits for PyPI to index each package
- ✅ Verifies installation in clean venv
- ✅ Handles errors gracefully
- ✅ Supports dry-run mode

**Script options:**
```bash
--test          # Upload to TestPyPI instead of PyPI
--skip-build    # Use existing dist/ folders
--skip-verify   # Skip installation verification
--dry-run       # Show what would be done without publishing
```

### Option 2: Manual Publishing

#### Step 1: Publish hfortix-core

```bash
cd packages/core

# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build package
python -m build

# Check the build
twine check dist/*

# Upload to TestPyPI (optional - for testing)
twine upload --repository testpypi dist/*

# Upload to PyPI (production)
twine upload dist/*

cd ../..
```

**Wait 2-3 minutes for PyPI to index the package before proceeding!**

Verify it's available:
```bash
pip index versions hfortix-core
```

#### Step 2: Publish hfortix-fortios

```bash
cd packages/fortios

# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build package
python -m build

# Check the build
twine check dist/*

# Upload to PyPI
twine upload dist/*

cd ../..
```

**Wait 2-3 minutes for PyPI to index before proceeding!**

Verify:
```bash
pip index versions hfortix-fortios
```

#### Step 3: Publish hfortix (meta-package)

```bash
cd packages/meta

# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build package
python -m build

# Check the build
twine check dist/*

# Upload to PyPI
twine upload dist/*

cd ../..
```

Verify:
```bash
pip index versions hfortix
```

## Post-Publishing Verification

### 1. Test Installation

```bash
# Create fresh virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Test installing meta-package with all extras
pip install hfortix[all]==0.4.0

# Verify all packages installed
pip list | grep hfortix
# Should show:
# hfortix         0.4.0
# hfortix-core    0.4.0
# hfortix-fortios 0.4.0

# Test imports
python -c "from hfortix import FortiOS; print(FortiOS)"
python -c "from hfortix_fortios import FortiOS; print(FortiOS)"
python -c "from hfortix_core import FortinetError; print(FortinetError)"

deactivate
rm -rf test_env
```

### 2. Test Minimal Installation

```bash
python -m venv test_env2
source test_env2/bin/activate

# Test installing core only (default)
pip install hfortix==0.4.0

# Should only install hfortix-core
pip list | grep hfortix
# Should show:
# hfortix      0.4.0
# hfortix-core 0.4.0

python -c "from hfortix_core import FortinetError; print('Success!')"

deactivate
rm -rf test_env2
```

### 3. Test FortiOS Extra

```bash
python -m venv test_env3
source test_env3/bin/activate

# Test installing with fortios extra
pip install hfortix[fortios]==0.4.0

# Should install core + fortios
pip list | grep hfortix
# Should show:
# hfortix         0.4.0
# hfortix-core    0.4.0
# hfortix-fortios 0.4.0

python -c "from hfortix_fortios import FortiOS; print('Success!')"

deactivate
rm -rf test_env3
```

## Troubleshooting

### Problem: "Could not find a version that satisfies the requirement hfortix-core>=0.4.0"

**Cause:** You tried to publish hfortix-fortios or hfortix before hfortix-core was indexed by PyPI.

**Solution:**
1. Wait 2-3 minutes after publishing each package
2. Verify package is available: `pip index versions hfortix-core`
3. Try publishing the next package again

### Problem: "File already exists"

**Cause:** You're trying to re-upload the same version.

**Solution:**
1. You cannot re-upload the same version to PyPI
2. Bump the version number (e.g., 0.4.0 → 0.4.1)
3. Update all three packages to the new version
4. Rebuild and re-publish all three

### Problem: Build artifacts from previous version

**Cause:** Old dist/ folders contain previous builds.

**Solution:**
```bash
# Clean all build artifacts
find packages -type d -name "dist" -exec rm -rf {} +
find packages -type d -name "*.egg-info" -exec rm -rf {} +
find packages -type d -name "build" -exec rm -rf {} +
```

## GitHub Actions (Optional)

For automated publishing via GitHub Actions, see `.github/workflows/publish.yml`.

The workflow:
1. Triggers on release tags (e.g., `v0.4.0`)
2. Builds all packages
3. Publishes in correct order with delays
4. Uses trusted publishing (no API tokens needed)

## Version Bumping

When releasing a new version, update these files:

1. `packages/core/pyproject.toml` - version
2. `packages/core/hfortix_core/__init__.py` - __version__
3. `packages/fortios/pyproject.toml` - version and dependency version
4. `packages/fortios/hfortix_fortios/__init__.py` - __version__
5. `packages/meta/pyproject.toml` - version and dependency versions
6. `packages/meta/hfortix/__init__.py` - __version__
7. `CHANGELOG.md` - add new version entry
8. `README.md` - update "Latest Features" section

Or use: `make release VERSION=0.4.1` (if updated to support split packages)

## Support

- GitHub Issues: https://github.com/hermanwjacobsen/hfortix/issues
- Documentation: https://github.com/hermanwjacobsen/hfortix

## Checklist

Before publishing:

- [ ] All version numbers updated to 0.4.0
- [ ] CHANGELOG.md updated
- [ ] README files updated
- [ ] All tests passing
- [ ] Git committed and tagged
- [ ] Clean build directories
- [ ] Build tools installed (build, twine)
- [ ] PyPI credentials configured

Publishing order:

- [ ] Published hfortix-core==0.4.0
- [ ] Waited 2-3 minutes
- [ ] Verified hfortix-core on PyPI
- [ ] Published hfortix-fortios==0.4.0
- [ ] Waited 2-3 minutes
- [ ] Verified hfortix-fortios on PyPI
- [ ] Published hfortix==0.4.0
- [ ] Verified hfortix on PyPI

Post-publishing:

- [ ] Tested meta-package installation
- [ ] Tested minimal installation
- [ ] Tested imports work
- [ ] Created GitHub release
- [ ] Updated documentation website (if applicable)
