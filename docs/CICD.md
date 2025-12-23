# CI/CD Pipeline Documentation

**Version:** 0.3.22  
**Last Updated:** December 23, 2025

---

## Overview

HFortix uses GitHub Actions for continuous integration and deployment. Our CI/CD pipeline ensures code quality, security, and automated releases.

---

## Workflows

### 1. **CI Workflow** (`ci.yml`)

**Trigger:** Push to `main`/`develop`, Pull Requests  
**Purpose:** Validate code quality before merge

#### Jobs:

1. **Lint & Format Check**
   - Black formatting check (79 char line length)
   - isort import sorting check
   - flake8 linting
   - **Status Badge:** [![CI](https://github.com/hermanwjacobsen/hfortix/workflows/CI/badge.svg)](https://github.com/hermanwjacobsen/hfortix/actions/workflows/ci.yml)

2. **Type Checking**
   - mypy type validation
   - Ensures 100% type hint coverage compliance

3. **Security Scan**
   - Bandit security analysis
   - Generates JSON report (available as artifact)
   - Scans for common vulnerabilities

4. **Test Suite** (Python 3.10, 3.11, 3.12)
   - **Current Status:** ⏳ Placeholder (unit tests not yet implemented)
   - **Future:** pytest with coverage reporting, Codecov integration

5. **Build Package**
   - Builds wheel and sdist
   - Validates with twine
   - Uploads artifacts

6. **Pre-commit Hooks**
   - Runs all pre-commit hooks
   - Ensures consistent code quality

7. **All Checks Passed**
   - Gate job that requires all checks to pass
   - Blocks merge if any job fails

---

### 2. **Publish to PyPI** (`publish.yml`)

**Trigger:** 
- Automatic: Git tag push (`v*.*.*`)
- Manual: Workflow dispatch (choose PyPI or TestPyPI)

**Purpose:** Automated package publishing

#### Jobs:

1. **Validate Version**
   - Ensures version consistency across:
     - `pyproject.toml`
     - `setup.py`
     - `hfortix/FortiOS/__init__.py`
     - Git tag
   - Fails if any mismatch detected

2. **Build Distribution**
   - Creates wheel and source distribution
   - Validates package integrity
   - Stores artifacts for 30 days

3. **Publish to TestPyPI** (Manual only)
   - Test publishing before production
   - URL: https://test.pypi.org/project/hfortix/

4. **Publish to PyPI** (Automatic on tag push)
   - Production release
   - Uses trusted publishing (no API token needed)
   - URL: https://pypi.org/project/hfortix/

5. **Create GitHub Release**
   - Extracts changelog for version
   - Creates release with notes
   - Auto-generates release notes

6. **Notify Success**
   - Outputs success message with links

#### Usage:

**Automatic Release:**
```bash
# Update version in all files
vim pyproject.toml setup.py hfortix/FortiOS/__init__.py

# Commit and tag
git add .
git commit -m "release: version 0.3.22"
git tag v0.3.22
git push origin main --tags
```

**Manual Release (TestPyPI):**
1. Go to Actions → Publish to PyPI
2. Click "Run workflow"
3. Select "testpypi"
4. Click "Run workflow"

---

### 3. **CodeQL Security Analysis** (`codeql.yml`)

**Trigger:** 
- Push to `main`
- Pull Requests
- Weekly schedule (Monday 9:00 AM UTC)

**Purpose:** Advanced security vulnerability detection

#### Features:
- GitHub Advanced Security scanning
- Detects SQL injection, XSS, command injection, etc.
- Security alerts in repository Security tab

---

### 4. **Dependency Review** (`dependency-review.yml`)

**Trigger:** Pull Requests

**Purpose:** Review dependency changes

#### Features:
- Detects new dependencies in PRs
- Fails on moderate+ severity vulnerabilities
- Blocks GPL-2.0/GPL-3.0 licenses
- Comments summary in PR

---

### 5. **Auto-label PRs** (`label-pr.yml`)

**Trigger:** PR opened/edited/synchronized

**Purpose:** Automatically label PRs based on changed files

#### Labels:
- `documentation` - Docs or markdown changes
- `dependencies` - requirements.txt, pyproject.toml changes
- `ci/cd` - GitHub Actions, pre-commit changes
- `tests` - Test file changes
- `api` - API endpoint changes
- `examples` - Example file changes
- `core` - Core client changes
- `security` - Exception or security doc changes

---

## Required Secrets

### For Trusted Publishing (Recommended):

No secrets needed! Configure trusted publishing on PyPI:
1. Go to https://pypi.org/manage/account/publishing/
2. Add publisher: `hermanwjacobsen/hfortix`
3. Workflow: `publish.yml`
4. Environment: `pypi`

### Alternative: API Tokens

If not using trusted publishing, add these secrets:

```
PYPI_API_TOKEN       - PyPI API token for production
TEST_PYPI_API_TOKEN  - TestPyPI API token for testing
```

Add in: Repository → Settings → Secrets and variables → Actions

---

## Branch Protection Rules

**Recommended for `main` branch:**

1. **Require pull request before merging**
   - Require 1 approval
   - Dismiss stale reviews

2. **Require status checks to pass**
   - `Lint & Format Check`
   - `Type Checking`
   - `Security Scan`
   - `Build Package`
   - `Pre-commit Hooks`

3. **Require conversation resolution**

4. **Require signed commits** (optional)

5. **Require linear history** (optional)

---

## Local Development

### Run CI checks locally:

```bash
# All checks
make all

# Individual checks
make format      # Auto-fix formatting
make lint        # Check code quality
make type-check  # Type validation
make security    # Security scan
make test        # Run tests (when available)
```

### Pre-commit hooks:

```bash
# Install hooks
make pre-commit

# Run manually
pre-commit run --all-files
```

---

## CI/CD Best Practices

### Before Pushing:

1. ✅ Run `make all` locally
2. ✅ Ensure all files formatted (Black, isort)
3. ✅ No type errors (mypy)
4. ✅ No security issues (bandit)
5. ✅ Tests pass (when available)

### Before Releasing:

1. ✅ Update CHANGELOG.md
2. ✅ Bump version in all 3 files:
   - `pyproject.toml`
   - `setup.py`
   - `hfortix/FortiOS/__init__.py`
3. ✅ Test locally: `make build`
4. ✅ Optional: Test on TestPyPI first
5. ✅ Create and push tag

### Version Numbering:

Follow semantic versioning:
- **Major (X.0.0):** Breaking changes
- **Minor (0.X.0):** New features, backward compatible
- **Patch (0.0.X):** Bug fixes

---

## Troubleshooting

### CI Failures

**Lint failures:**
```bash
make format  # Auto-fix most issues
```

**Type check failures:**
```bash
mypy hfortix --ignore-missing-imports
# Add type ignores if necessary
```

**Security scan failures:**
Review bandit report in artifacts, add exclusions to `pyproject.toml` if false positive.

**Build failures:**
```bash
make clean
make build
twine check dist/*
```

### Publish Failures

**Version mismatch:**
```bash
# Check all version strings
grep -r "0.3.21" pyproject.toml setup.py hfortix/FortiOS/__init__.py
```

**PyPI authentication:**
- Verify trusted publishing is configured
- Or check API token is valid

**Package already exists:**
- You cannot republish the same version
- Bump version and retry

---

## Monitoring

### GitHub Actions Dashboard

View all workflow runs:
- Repository → Actions tab

### Security Alerts

View security findings:
- Repository → Security tab → Code scanning alerts

### Dependency Alerts

View dependency vulnerabilities:
- Repository → Security tab → Dependabot alerts

---

## Future Enhancements

- [ ] Add unit test coverage reporting to Codecov
- [ ] Add integration test workflow (requires FortiGate)
- [ ] Add performance benchmark tracking
- [ ] Add changelog auto-generation
- [ ] Add automatic version bumping
- [ ] Add Slack/Discord notifications
- [ ] Add Docker image publishing

---

## Support

**Issues:** https://github.com/hermanwjacobsen/hfortix/issues  
**Discussions:** https://github.com/hermanwjacobsen/hfortix/discussions
