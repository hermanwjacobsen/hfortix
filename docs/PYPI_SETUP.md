# PyPI Publishing Setup Guide

This document explains how to configure PyPI and TestPyPI publishing for the hfortix package.

## Current Setup

### ✅ PyPI (Production)
- **Authentication**: Trusted Publishing (OIDC) - **Already configured**
- **URL**: https://pypi.org/manage/project/hfortix/settings/publishing/
- **No token needed** - Uses GitHub Actions OIDC authentication

### ⚠️ TestPyPI (Testing)
- **Authentication**: API Token - **Needs configuration**
- **Current Status**: Using token-based authentication (fallback)
- **Required Secret**: `TEST_PYPI_API_TOKEN`

## Setup Instructions

### 1. Configure TestPyPI API Token

Since TestPyPI trusted publishing requires additional setup, we're using token-based auth:

1. **Generate TestPyPI API Token**:
   - Go to: https://test.pypi.org/manage/account/token/
   - Click "Add API token"
   - Token name: `hfortix-github-actions`
   - Scope: Select "Project: hfortix" (if available) or "Entire account"
   - Click "Add token"
   - **IMPORTANT**: Copy the token immediately (starts with `pypi-`)

2. **Add Token to GitHub Secrets**:
   - Go to: https://github.com/hermanwjacobsen/hfortix/settings/secrets/actions
   - Click "New repository secret"
   - Name: `TEST_PYPI_API_TOKEN`
   - Value: Paste the token from step 1
   - Click "Add secret"

### 2. (Optional) Enable TestPyPI Trusted Publishing

If you want to use trusted publishing for TestPyPI as well:

1. **Configure TestPyPI Publisher**:
   - Go to: https://test.pypi.org/manage/project/hfortix/settings/publishing/
   - Click "Add a new publisher"
   - Fill in:
     - **PyPI Project Name**: `hfortix`
     - **Owner**: `hermanwjacobsen`
     - **Repository name**: `hfortix`
     - **Workflow name**: `publish.yml`
     - **Environment name**: `testpypi`
   - Click "Add"

2. **Update Workflow**:
   - In `.github/workflows/publish.yml`, find the `publish-testpypi` job
   - Remove/comment out the line:
     ```yaml
     password: ${{ secrets.TEST_PYPI_API_TOKEN }}
     ```
   - The workflow will then use trusted publishing for TestPyPI too

## How It Works

### Publishing Flow

```
Tag Push (v0.3.30)
    ↓
CI Workflow Runs
    ├─ Lint & Format Check
    ├─ Type Checking
    ├─ Security Scan
    ├─ Build Package
    └─ Pre-commit Hooks
    ↓
Wait for CI (All Checks Passed)
    ↓
Publish to TestPyPI ✓
    ↓
Verify Package Works ✓
    ↓
Publish to PyPI ✓
```

### Key Safety Features

1. **CI Must Pass**: Publishing only happens if all CI checks pass
2. **TestPyPI First**: Package is tested on TestPyPI before production
3. **Validation**: Package is verified on TestPyPI before PyPI upload
4. **Version Checks**: Ensures version consistency across all files

## Troubleshooting

### Error: "Trusted publishing exchange failure"

**Symptom**: 
```
invalid-publisher: valid token, but no corresponding publisher
environment: testpypi
```

**Cause**: Trusted publishing not configured on TestPyPI

**Solution**: Either:
- Add `TEST_PYPI_API_TOKEN` secret (recommended for TestPyPI)
- Or configure trusted publishing on TestPyPI (see section 2 above)

### Error: "Invalid or non-existent authentication information"

**Symptom**: Publishing fails with authentication error

**Solution**:
1. Check that `TEST_PYPI_API_TOKEN` secret exists
2. Verify the token hasn't expired
3. Regenerate token if needed

### CI Not Triggering

**Symptom**: Publishing starts before CI completes

**Solution**:
- The workflow now waits for the "All Checks Passed" job
- Check that the CI workflow completed successfully
- Look at: https://github.com/hermanwjacobsen/hfortix/actions

## Manual Publishing

To manually trigger publishing:

1. Go to: https://github.com/hermanwjacobsen/hfortix/actions/workflows/publish.yml
2. Click "Run workflow"
3. Select environment: `pypi` or `testpypi`
4. Click "Run workflow"

**Note**: Manual publishing bypasses the CI wait step for flexibility.

## Verification

After publishing, verify the package:

### TestPyPI
```bash
pip install --index-url https://test.pypi.org/simple/ --no-deps hfortix==0.3.30
python -c "import hfortix; print(hfortix.__version__)"
```

### PyPI
```bash
pip install hfortix==0.3.30
python -c "import hfortix; print(hfortix.__version__)"
```

## References

- [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/)
- [PyPI Trusted Publishing Troubleshooting](https://docs.pypi.org/trusted-publishers/troubleshooting/)
- [GitHub Actions OIDC](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect)
- [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish)
