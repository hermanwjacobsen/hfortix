"""
Pytest configuration for FortiOS API tests.

This conftest.py ensures that tests use the local development version
of the hfortix_fortios package instead of any pip-installed version.
"""

import sys
from pathlib import Path

# Add local package to sys.path FIRST (highest priority)
# This ensures we import from local development code, not pip-installed package
# Path: .tests/conftest.py -> resolve to absolute -> parent (workspace root) -> packages/fortios
workspace_root = Path(__file__).resolve().parent.parent  # Go up to workspace root
local_package_dir = workspace_root / "packages" / "fortios"
sys.path.insert(0, str(local_package_dir))

# Add .tests directory to path for __client__ import (where __client__.py is located)
tests_dir = Path(__file__).parent
sys.path.insert(0, str(tests_dir))

print(f"✓ Using local package from: {local_package_dir}")
print(f"✓ Tests directory (.tests): {tests_dir}")
