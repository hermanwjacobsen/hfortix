# Makefile for HFortix Development
# Provides convenient shortcuts for common development tasks

.PHONY: help install install-dev test lint format type-check security clean build publish docs pre-commit all

# Default target: show help
help:
	@echo "HFortix Development Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  make install        - Install package in editable mode"
	@echo "  make install-dev    - Install package with dev dependencies"
	@echo "  make test           - Run all tests"
	@echo "  make test-unit      - Run unit tests only"
	@echo "  make test-integration - Run integration tests only"
	@echo "  make test-coverage  - Run tests with coverage report"
	@echo "  make lint           - Run all linters (flake8, black check, isort check)"
	@echo "  make format         - Format code with black and isort"
	@echo "  make type-check     - Run mypy type checking"
	@echo "  make security       - Run security checks (bandit)"
	@echo "  make pre-commit     - Install and run pre-commit hooks"
	@echo "  make clean          - Remove build artifacts and cache files"
	@echo "  make build          - Build all distribution packages"
	@echo "  make build-core     - Build only hfortix-core"
	@echo "  make build-fortios  - Build only hfortix-fortios"
	@echo "  make build-meta     - Build only hfortix meta-package"
	@echo "  make publish        - Publish all packages to PyPI (uses automated script)"
	@echo "  make publish-core   - Publish only hfortix-core to PyPI"
	@echo "  make publish-fortios - Publish only hfortix-fortios to PyPI"
	@echo "  make publish-meta   - Publish only hfortix meta-package to PyPI"
	@echo "  make publish-package PKG=core|fortios|meta - Publish specific package"
	@echo "  make publish-test   - Publish all packages to TestPyPI"
	@echo "  make publish-test-core - Publish only hfortix-core to TestPyPI"
	@echo "  make publish-test-fortios - Publish only hfortix-fortios to TestPyPI"
	@echo "  make publish-test-meta - Publish only hfortix meta to TestPyPI"
	@echo "  make docs           - Build HTML documentation"
	@echo "  make docs-clean     - Clean documentation build artifacts"
	@echo "  make docs-live      - Start live documentation server with auto-reload"
	@echo "  make docs-generate  - Generate API documentation from code"
	@echo "  make docs-check     - Check documentation for broken links"
	@echo "  make all            - Run format, lint, type-check, and test"
	@echo "  make version-check  - Check version consistency across all packages"
	@echo "  make bump-version   - Bump version (use VERSION=x.y.z or TYPE=patch/minor/major)"
	@echo "  make check-release  - Run all pre-release validation checks"
	@echo "  make release        - Show automated release workflow instructions"
	@echo "  make pre-release    - Auto-fix issues, then run all pre-release checks"
	@echo "  make pre-release-check - Run pre-release checks only (no auto-fix)"
	@echo "  make fix            - Auto-fix formatting and import issues"
	@echo "  make fix-check      - Check what would be fixed (without making changes)"
	@echo ""
	@echo "Package-specific options:"
	@echo "  make bump-version VERSION=0.4.1 PKG=core    - Bump only hfortix-core"
	@echo "  make bump-version TYPE=patch PKG=fortios    - Patch bump hfortix-fortios"
	@echo "  make publish-package PKG=core               - Publish only hfortix-core"
	@echo ""

# Installation
install:
	@echo "Installing modular packages in editable mode..."
	pip install -e packages/core
	pip install -e packages/fortios
	pip install -e packages/meta
	@echo "✅ All packages installed!"

install-dev:
	@echo "Installing modular packages with dev dependencies..."
	pip install -e packages/core[dev]
	pip install -e packages/fortios
	pip install -e packages/meta
	pip install pre-commit bandit pytest-httpx
	@echo "✅ Dev environment ready!"

# Testing
test:
	pytest -v

test-unit:
	pytest -v -m unit

test-integration:
	pytest -v -m integration

test-coverage:
	pytest --cov=hfortix_core --cov=hfortix_fortios --cov-report=html --cov-report=term-missing

# Code Quality
lint:
	@echo "Running flake8..."
	flake8 packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix
	@echo "Checking black formatting..."
	black --check --line-length=79 packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix
	@echo "Checking isort..."
	isort --check-only --profile=black --line-length=79 packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix
	@echo "✅ All linting checks passed!"

format:
	@echo "Formatting with black..."
	black --line-length=79 packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix examples
	@echo "Sorting imports with isort..."
	isort --profile=black --line-length=79 packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix examples
	@echo "✅ Code formatted!"

type-check:
	@echo "Running mypy type checking..."
	mypy packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix --ignore-missing-imports
	@echo "✅ Type checking complete!"

security:
	@echo "Running bandit security checks..."
	bandit -r packages/core/hfortix_core packages/fortios/hfortix_fortios packages/meta/hfortix -c pyproject.toml
	@echo "✅ Security checks passed!"

# Pre-commit
pre-commit:
	@echo "Installing pre-commit hooks..."
	pre-commit install
	@echo "Running pre-commit on all files..."
	pre-commit run --all-files
	@echo "✅ Pre-commit setup complete!"

# Cleanup
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf packages/core/build/
	rm -rf packages/core/dist/
	rm -rf packages/core/*.egg-info
	rm -rf packages/fortios/build/
	rm -rf packages/fortios/dist/
	rm -rf packages/fortios/*.egg-info
	rm -rf packages/meta/build/
	rm -rf packages/meta/dist/
	rm -rf packages/meta/*.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "✅ Cleanup complete!"

# Building and Publishing
# Individual package build targets
build-core:
	@echo "Building hfortix-core..."
	cd packages/core && rm -rf dist/ build/ *.egg-info && python -m build
	@echo "✅ hfortix-core built!"

build-fortios:
	@echo "Building hfortix-fortios..."
	cd packages/fortios && rm -rf dist/ build/ *.egg-info && python -m build
	@echo "✅ hfortix-fortios built!"

build-meta:
	@echo "Building hfortix (meta-package)..."
	cd packages/meta && rm -rf dist/ build/ *.egg-info && python -m build
	@echo "✅ hfortix (meta) built!"

# Build all packages
build: clean
	@echo "Building all modular packages..."
	@make build-core
	@make build-fortios
	@make build-meta
	@echo "Copying all dist files to root dist/..."
	mkdir -p dist
	cp packages/core/dist/* dist/ 2>/dev/null || true
	cp packages/fortios/dist/* dist/ 2>/dev/null || true
	cp packages/meta/dist/* dist/ 2>/dev/null || true
	@echo "✅ Build complete! All packages in dist/"

# Individual package publish targets (PyPI)
publish-core: build-core
	@echo "Publishing hfortix-core to PyPI..."
	cd packages/core && python -m twine upload dist/*
	@echo "✅ hfortix-core published to PyPI!"

publish-fortios: build-fortios
	@echo "Publishing hfortix-fortios to PyPI..."
	@echo "⚠️  NOTE: Ensure hfortix-core is already published!"
	cd packages/fortios && python -m twine upload dist/*
	@echo "✅ hfortix-fortios published to PyPI!"

publish-meta: build-meta
	@echo "Publishing hfortix (meta-package) to PyPI..."
	@echo "⚠️  NOTE: Ensure hfortix-core is already published!"
	cd packages/meta && python -m twine upload dist/*
	@echo "✅ hfortix (meta) published to PyPI!"

# Selective package publishing
publish-package:
	@if [ -z "$(PKG)" ]; then \
		echo "❌ Error: PKG not specified"; \
		echo "Usage: make publish-package PKG=core|fortios|meta"; \
		echo "Example: make publish-package PKG=core"; \
		exit 1; \
	fi
	@make publish-$(PKG)

# Publish all packages (automated with proper ordering)
publish: build
	@echo "Publishing to PyPI using automated script..."
	@echo "⚠️  Publishing in order: core → fortios → meta"
	@python .dev/scripts/publish_split_packages.py
	@echo "✅ All packages published to PyPI!"

# Individual package publish targets (TestPyPI)
publish-test-core: build-core
	@echo "Publishing hfortix-core to TestPyPI..."
	cd packages/core && python -m twine upload --repository testpypi dist/*
	@echo "✅ hfortix-core published to TestPyPI!"

publish-test-fortios: build-fortios
	@echo "Publishing hfortix-fortios to TestPyPI..."
	cd packages/fortios && python -m twine upload --repository testpypi dist/*
	@echo "✅ hfortix-fortios published to TestPyPI!"

publish-test-meta: build-meta
	@echo "Publishing hfortix (meta-package) to TestPyPI..."
	cd packages/meta && python -m twine upload --repository testpypi dist/*
	@echo "✅ hfortix (meta) published to TestPyPI!"

# Publish all packages to TestPyPI (automated)
publish-test: build
	@echo "Publishing to TestPyPI using automated script..."
	@echo "⚠️  Publishing in order: core → fortios → meta"
	@python .dev/scripts/publish_split_packages.py --test
	@echo "✅ All packages published to TestPyPI!"

# Documentation (placeholder for future)
docs:
	@echo "📚 Building documentation..."
	@cd docs && $(MAKE) html
	@echo "✅ Documentation built! Open docs/build/html/index.html"

docs-clean:
	@echo "🧹 Cleaning documentation build..."
	@cd docs && $(MAKE) clean
	@echo "✅ Documentation build cleaned!"

docs-live:
	@echo "📚 Starting live documentation server..."
	@cd docs && $(MAKE) livehtml

docs-generate:
	@echo "🔧 Generating API documentation..."
	@python .dev/scripts/generate_docs.py
	@echo "✅ API documentation generated!"

docs-check:
	@echo "🔍 Checking documentation..."
	@cd docs && $(MAKE) linkcheck
	@echo "✅ Documentation check complete!"

# Comprehensive check
all: format lint type-check test
	@echo "✅ All checks passed! Ready to commit."

# Version management
version-check:
	@echo "Checking version consistency across all packages..."
	@python3 .dev/scripts/check_version_consistency_split.py

bump-version:
	@if [ -n "$(VERSION)" ]; then \
		if [ -n "$(PKG)" ]; then \
			python3 .dev/scripts/bump_version.py $(VERSION) --packages $(PKG); \
		else \
			python3 .dev/scripts/bump_version.py $(VERSION); \
		fi; \
	elif [ -n "$(TYPE)" ]; then \
		if [ -n "$(PKG)" ]; then \
			python3 .dev/scripts/bump_version.py --$(TYPE) --packages $(PKG); \
		else \
			python3 .dev/scripts/bump_version.py --$(TYPE); \
		fi; \
	else \
		echo "Usage: make bump-version VERSION=0.4.1 [PKG=core|fortios|meta]"; \
		echo "   or: make bump-version TYPE=patch|minor|major [PKG=core|fortios|meta]"; \
		echo ""; \
		echo "Examples:"; \
		echo "  make bump-version VERSION=0.4.1              # Update all packages"; \
		echo "  make bump-version VERSION=0.4.1 PKG=core    # Update only core"; \
		echo "  make bump-version TYPE=patch                 # Patch all packages"; \
		echo "  make bump-version TYPE=minor PKG=fortios    # Minor bump fortios only"; \
		exit 1; \
	fi

pre-release: fix
	@echo "Running pre-release checks after auto-fix..."
	@echo "⚠️  Note: This runs legacy checks. For split packages, use:"
	@echo "   make version-check  # Check package versions"
	@echo "   make lint           # Linting"
	@echo "   make type-check     # Type checking"
	@echo "   make test-coverage  # Tests with coverage"
	@if [ -f .venv/bin/python ]; then \
		.venv/bin/python .dev/scripts/pre_release_check.py; \
	else \
		python3 .dev/scripts/pre_release_check.py || echo "⚠️  Pre-release check script not found"; \
	fi

pre-release-check:
	@echo "Running pre-release checks only (no auto-fix)..."
	@if [ -f .venv/bin/python ]; then \
		.venv/bin/python .dev/scripts/pre_release_check.py; \
	else \
		python3 .dev/scripts/pre_release_check.py || echo "⚠️  Pre-release check script not found"; \
	fi

# Auto-fix code issues
fix:
	@echo "Auto-fixing code issues..."
	@.venv/bin/python .dev/scripts/pre_release_fix.py

fix-check:
	@echo "Checking what would be fixed..."
	@.venv/bin/python .dev/scripts/pre_release_fix.py --check-only

# Version bump helpers (legacy - use bump-version instead)
bump-patch:
	@echo "Current version: $$(grep '^version' pyproject.toml | cut -d'"' -f2)"
	@echo "Use: make bump-version TYPE=patch"

bump-minor:
	@echo "Current version: $$(grep '^version' pyproject.toml | cut -d'"' -f2)"
	@echo "Use: make bump-version TYPE=minor PKG=<package>"

bump-major:
	@echo "Current version: $$(grep '^version' pyproject.toml | cut -d'"' -f2)"
	@echo "Use: make bump-version TYPE=major PKG=<package>"

# Show project stats
stats:
	@echo "📊 Project Statistics"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Python files:    $$(find hfortix -name '*.py' | wc -l)"
	@echo "Lines of code:   $$(find hfortix -name '*.py' -exec cat {} \; | wc -l)"
	@echo "Test files:      $$(find .dev/tests -name '*.py' 2>/dev/null | wc -l || echo 0)"
	@echo "Documentation:   $$(find docs -name '*.md' | wc -l) markdown files"
	@echo "Examples:        $$(find examples -name '*.py' | wc -l) example files"
	@echo "Version:         $$(grep '^version' pyproject.toml | cut -d'"' -f2)"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Automated release process
release:
	@echo "════════════════════════════════════════════════════════════════════════"
	@echo "  HFortix Multi-Package Release Process"
	@echo "════════════════════════════════════════════════════════════════════════"
	@echo ""
	@echo "⚠️  IMPORTANT: This is an automated release workflow."
	@echo ""
	@echo "For multi-package releases (0.4.0+), use the following workflow instead:"
	@echo ""
	@echo "1. Update versions:"
	@echo "   make bump-version VERSION=0.4.1              # All packages"
	@echo "   make bump-version VERSION=0.4.1 PKG=core    # Specific package"
	@echo ""
	@echo "2. Verify versions:"
	@echo "   make version-check"
	@echo ""
	@echo "3. Run pre-release checks:"
	@echo "   make all          # format, lint, type-check, test"
	@echo ""
	@echo "4. Update CHANGELOG.md manually"
	@echo ""
	@echo "5. Commit and tag:"
	@echo "   git add packages/*/pyproject.toml CHANGELOG.md"
	@echo "   git commit -m 'chore: release v0.4.1'"
	@echo "   git tag v0.4.1                    # Unified release (all packages)"
	@echo "   git tag v-core-0.4.1              # Or package-specific tag"
	@echo ""
	@echo "6. Push (triggers GitHub Actions):"
	@echo "   git push origin main"
	@echo "   git push origin v0.4.1"
	@echo ""
	@echo "7. Monitor workflow:"
	@echo "   https://github.com/hermanwjacobsen/hfortix/actions"
	@echo ""
	@echo "════════════════════════════════════════════════════════════════════════"
	@echo ""
	@echo "For detailed instructions, see: .dev/docs/AUTOMATED_PUBLISHING.md"
	@echo "Quick reference: .dev/docs/RELEASE_QUICK_REFERENCE.md"
	@echo ""
	@if [ -n "$(FORCE)" ]; then \
		echo "⚠️  FORCE=1 detected - skipping safety check"; \
		if [ -n "$(VERSION)" ]; then \
			echo "Running automated release for version $(VERSION)"; \
		else \
			echo "ERROR: VERSION not specified"; \
			echo "Usage: make release VERSION=0.4.1 FORCE=1"; \
			exit 1; \
		fi; \
	else \
		echo "To proceed anyway, run: make release VERSION=x.y.z FORCE=1"; \
		exit 1; \
	fi

# Quick pre-release validation
check-release:
	@echo "════════════════════════════════════════════════════════════════════════"
	@echo "  Pre-Release Validation"
	@echo "════════════════════════════════════════════════════════════════════════"
	@echo ""
	@echo "📦 Checking package versions..."
	@python3 .dev/scripts/check_version_consistency_split.py
	@echo ""
	@echo "🧪 Running linters..."
	@make lint
	@echo ""
	@echo "📝 Running type checks..."
	@make type-check
	@echo ""
	@echo "🔒 Running security checks..."
	@make security
	@echo ""
	@echo "════════════════════════════════════════════════════════════════════════"
	@echo "✅ All pre-release checks passed!"
	@echo "════════════════════════════════════════════════════════════════════════"
	@echo ""
	@echo "Next steps:"
	@echo "1. Update CHANGELOG.md"
	@echo "2. Commit: git commit -am 'chore: prepare release'"
	@echo "3. Tag: git tag v\$$(python3 -c \"import re; print(re.search(r'version = \"([^\"]+)\"', open('packages/meta/pyproject.toml').read()).group(1))\")"
	@echo "4. Push: git push origin main --tags"
	@echo ""
