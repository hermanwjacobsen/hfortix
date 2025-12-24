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
	@echo "  make build          - Build distribution packages"
	@echo "  make publish        - Publish to PyPI (requires credentials)"
	@echo "  make publish-test   - Publish to TestPyPI"
	@echo "  make docs           - Generate documentation (future)"
	@echo "  make all            - Run format, lint, type-check, and test"
	@echo "  make version-check  - Check version consistency across files"
	@echo "  make bump-version   - Bump version (use VERSION=0.3.25 or TYPE=patch/minor/major)"
	@echo "  make pre-release    - Auto-fix issues, then run all pre-release checks"
	@echo "  make pre-release-check - Run pre-release checks only (no auto-fix)"
	@echo "  make fix            - Auto-fix formatting and import issues"
	@echo "  make fix-check      - Check what would be fixed (without making changes)"
	@echo ""

# Installation
install:
	pip install -e .

install-dev:
	pip install -e .[dev]
	pip install pre-commit bandit pytest-httpx

# Testing
test:
	pytest -v

test-unit:
	pytest -v -m unit

test-integration:
	pytest -v -m integration

test-coverage:
	pytest --cov=hfortix --cov-report=html --cov-report=term-missing

# Code Quality
lint:
	@echo "Running flake8..."
	flake8 hfortix
	@echo "Checking black formatting..."
	black --check --line-length=79 hfortix
	@echo "Checking isort..."
	isort --check-only --profile=black --line-length=79 hfortix
	@echo "✅ All linting checks passed!"

format:
	@echo "Formatting with black..."
	black --line-length=79 hfortix examples
	@echo "Sorting imports with isort..."
	isort --profile=black --line-length=79 hfortix examples
	@echo "✅ Code formatted!"

type-check:
	@echo "Running mypy type checking..."
	mypy hfortix --ignore-missing-imports
	@echo "✅ Type checking complete!"

security:
	@echo "Running bandit security checks..."
	bandit -r hfortix -c pyproject.toml
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
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "✅ Cleanup complete!"

# Building and Publishing
build: clean
	@echo "Building distribution packages..."
	python -m build
	@echo "✅ Build complete! Packages in dist/"

publish: build
	@echo "Publishing to PyPI..."
	@echo "⚠️  Make sure you have set up your PyPI credentials!"
	python -m twine upload dist/*
	@echo "✅ Published to PyPI!"

publish-test: build
	@echo "Publishing to TestPyPI..."
	python -m twine upload --repository testpypi dist/*
	@echo "✅ Published to TestPyPI!"

# Documentation (placeholder for future)
docs:
	@echo "📚 Documentation generation not yet configured"
	@echo "Future: Will use Sphinx or MkDocs"

# Comprehensive check
all: format lint type-check test
	@echo "✅ All checks passed! Ready to commit."

# Version management
version-check:
	@echo "Checking version consistency..."
	@python3 X/scripts/check-version-consistency.py

bump-version:
	@if [ -n "$(VERSION)" ]; then \
		python3 X/scripts/bump_version.py $(VERSION); \
	elif [ -n "$(TYPE)" ]; then \
		python3 X/scripts/bump_version.py --$(TYPE); \
	else \
		echo "Usage: make bump-version VERSION=0.3.25"; \
		echo "   or: make bump-version TYPE=patch|minor|major"; \
		exit 1; \
	fi

pre-release: fix
	@echo "Running pre-release checks after auto-fix..."
	@.venv/bin/python X/scripts/pre_release_check.py

pre-release-check:
	@echo "Running pre-release checks only (no auto-fix)..."
	@.venv/bin/python X/scripts/pre_release_check.py

# Auto-fix code issues
fix:
	@echo "Auto-fixing code issues..."
	@.venv/bin/python X/scripts/pre_release_fix.py

fix-check:
	@echo "Checking what would be fixed..."
	@.venv/bin/python X/scripts/pre_release_fix.py --check-only

# Version bump helpers (legacy - use bump-version instead)
bump-patch:
	@echo "Current version: $$(grep '^version' pyproject.toml | cut -d'"' -f2)"
	@echo "Use: make bump-version TYPE=patch"

bump-minor:
	@echo "Current version: $$(grep '^version' pyproject.toml | cut -d'"' -f2)"
	@echo "To bump version, edit pyproject.toml, setup.py, and hfortix/FortiOS/__init__.py"

bump-major:
	@echo "Current version: $$(grep '^version' pyproject.toml | cut -d'"' -f2)"
	@echo "To bump version, edit pyproject.toml, setup.py, and hfortix/FortiOS/__init__.py"

# Show project stats
stats:
	@echo "📊 Project Statistics"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Python files:    $$(find hfortix -name '*.py' | wc -l)"
	@echo "Lines of code:   $$(find hfortix -name '*.py' -exec cat {} \; | wc -l)"
	@echo "Test files:      $$(find X/tests -name '*.py' 2>/dev/null | wc -l || echo 0)"
	@echo "Documentation:   $$(find docs -name '*.md' | wc -l) markdown files"
	@echo "Examples:        $$(find examples -name '*.py' | wc -l) example files"
	@echo "Version:         $$(grep '^version' pyproject.toml | cut -d'"' -f2)"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
