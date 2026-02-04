# Git Workflow - Multi-Repo Development

## Repository Architecture

This project uses a **multi-repository structure** where each package is an independent git repository:

### 🔒 Private Development Repo: `hfortix-dev`
**URL:** https://github.com/hermanwjacobsen/hfortix-dev

**Tracks:**
- `packages/*/dev/` - Tests, schemas, generators, internal docs
- `scripts/` - Development tools
- `.github/` - CI/CD, AI context

**Does NOT track:**
- `packages/*/src/` - These are separate git repos (excluded via `.gitignore`)

### 📦 Public Package Repos (Independent)

| Package | URL | Local Path |
| --- | --- | --- |
| **hfortix-fortios** | [github.com/hermanwjacobsen/hfortix-fortios](https://github.com/hermanwjacobsen/hfortix-fortios) | `packages/fortios/src/` |
| **hfortix-core** | [github.com/hermanwjacobsen/hfortix-core](https://github.com/hermanwjacobsen/hfortix-core) | `packages/core/src/` |
| **hfortix** | [github.com/hermanwjacobsen/hfortix](https://github.com/hermanwjacobsen/hfortix) | `packages/meta/src/` |

Each `packages/*/src/` directory is a **complete git repository** with its own `.git/` directory.

---

## Initial Setup

```bash
# 1. Clone the private development repo
git clone https://github.com/hermanwjacobsen/hfortix-dev.git
cd hfortix-dev

# 2. Clone each public repo into packages/*/src/
cd packages/fortios
git clone https://github.com/hermanwjacobsen/hfortix-fortios.git src

cd ../core
git clone https://github.com/hermanwjacobsen/hfortix-core.git src

cd ../meta
git clone https://github.com/hermanwjacobsen/hfortix.git src

cd ../..

# 3. Install packages in editable mode
pip install -e packages/core/src
pip install -e packages/fortios/src
pip install -e packages/meta/src
```

---

## Development Workflows

### Working on Source Code (packages/*/src/)

Each `packages/*/src/` is a **separate git repository**. Push changes directly:

```bash
# Example: Work on FortiOS source code
cd packages/fortios/src

# Make changes
vim hfortix_fortios/client.py

# Standard git workflow
git add .
git commit -m "Add new feature"
git push  # ✅ Pushes to github.com/hermanwjacobsen/hfortix-fortios

# Same pattern for other packages:
# cd packages/core/src && git push      → hfortix-core
# cd packages/meta/src && git push      → hfortix
```

### Working on Development Assets (packages/*/dev/)

Development assets are tracked in **hfortix-dev**:

```bash
# Navigate to hfortix-dev root
cd /app/dev/classes/fortinet

# Make changes to tests, schemas, generators
vim packages/fortios/dev/tests/test_client.py
vim packages/fortios/dev/schema/7.6.5/firewall.policy.json

# Standard git workflow for hfortix-dev
git add packages/fortios/dev/
git commit -m "Add new tests and update schema"
git push  # ✅ Pushes to github.com/hermanwjacobsen/hfortix-dev
```

### Working on Documentation

**Public Documentation** (ReadTheDocs):
```bash
# Public docs live in packages/*/src/docs/ (part of public repos)
cd packages/fortios/src

vim docs/source/guides/quickstart.rst
git add docs/
git commit -m "Update quickstart guide"
git push  # ✅ Pushes to hfortix-fortios

# Trigger ReadTheDocs build automatically
```

**Internal Documentation:**
```bash
# Internal docs live in hfortix-dev
cd /app/dev/classes/fortinet

vim packages/fortios/dev/internal-docs/architecture.md
git add packages/fortios/dev/internal-docs/
git commit -m "Update architecture docs"
git push  # ✅ Pushes to hfortix-dev
```

---

## Common Tasks

### Check Status Across All Repos

```bash
# Check hfortix-dev (private)
cd /app/dev/classes/fortinet && git status

# Check public repos
cd packages/fortios/src && git status  # hfortix-fortios
cd packages/core/src && git status     # hfortix-core  
cd packages/meta/src && git status     # hfortix (meta)
```

### Pull Latest Changes

```bash
# Pull from hfortix-dev
cd /app/dev/classes/fortinet && git pull

# Pull from public repos
cd packages/fortios/src && git pull
cd packages/core/src && git pull
cd packages/meta/src && git pull
```

### Create a New Feature

```bash
# 1. Create feature branch in public repo
cd packages/fortios/src
git checkout -b feature/new-endpoint
vim hfortix_fortios/api/v2/cmdb/system/admin.py
git commit -m "Add system admin endpoint"
git push -u origin feature/new-endpoint

# 2. Add tests in hfortix-dev
cd /app/dev/classes/fortinet
vim packages/fortios/dev/tests/live/cmdb/test_system_admin.py
git add packages/fortios/dev/tests/
git commit -m "Add tests for system admin endpoint"
git push

# 3. Merge feature branch via GitHub PR (in public repo)
# 4. Pull merged changes locally
cd packages/fortios/src && git checkout main && git pull
```

### Release a New Version

```bash
# 1. Update version in public repo
cd packages/fortios/src
vim pyproject.toml  # Bump version to 0.5.155
git commit -m "Bump version to 0.5.155"
git tag v0.5.155
git push && git push --tags

# 2. Build and publish to PyPI (if applicable)
python -m build
python -m twine upload dist/*

# 3. Update changelog in hfortix-dev
cd /app/dev/classes/fortinet
vim CHANGELOG.md
git commit -m "Update changelog for v0.5.155"
git push
```

---

## File Location Quick Reference

| Content Type | Location | Git Repo | Push Command |
| --- | --- | --- | --- |
| Source code | `packages/*/src/hfortix_*/` | Public (separate .git/) | `cd packages/*/src && git push` |
| Public docs | `packages/*/src/docs/` | Public (same as source) | `cd packages/*/src && git push` |
| Tests | `packages/*/dev/tests/` | hfortix-dev | `git push` (from root) |
| Schemas | `packages/*/dev/schema/` | hfortix-dev | `git push` (from root) |
| Generators | `packages/*/dev/generator/` | hfortix-dev | `git push` (from root) |
| Internal docs | `packages/*/dev/internal-docs/` | hfortix-dev | `git push` (from root) |

---

## Important Notes

1. **No Sync Script**: The old `scripts/push_src_to_public_repos.sh` and `scripts/sync_to_public.sh` scripts have been **removed**. Each `packages/*/src/` is now a full git repository - push directly from those directories.

2. **Separate Git Histories**: Each public repo maintains its own git history. The hfortix-dev repo only tracks development assets.

3. **Editable Installs**: With `pip install -e packages/*/src`, Python imports resolve to your local source code automatically.

4. **ReadTheDocs**: Builds trigger automatically when you push to public repos. Documentation is optimized with parallel processing and no PDF/ePub generation.

5. **Testing**: Run tests from `packages/*/dev/tests/` - they will use your local editable-installed source code.

---

## Troubleshooting

**Q: I accidentally committed packages/*/src/ to hfortix-dev!**
```bash
# Remove from git tracking (keeps files locally)
git rm -r --cached packages/fortios/src/
git commit -m "Remove src/ from tracking"
git push
```

**Q: How do I know which repo I'm in?**
```bash
# Check current repo's remote URL
git remote -v

# From hfortix-dev root: origin → hfortix-dev.git
# From packages/fortios/src: origin → hfortix-fortios.git
```

**Q: I want to work on multiple packages simultaneously**
```bash
# Make changes to multiple packages
cd packages/fortios/src
vim hfortix_fortios/client.py
git commit -m "Update fortios client"
git push

cd ../core/src
vim hfortix_core/http.py
git commit -m "Update core HTTP client"
git push

# Push to hfortix-dev for test changes
cd /app/dev/classes/fortinet
git commit -m "Update tests for both packages"
git push
```

---

**Made with ❤️ for efficient multi-repo development**
