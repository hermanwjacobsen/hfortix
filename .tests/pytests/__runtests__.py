#!/usr/bin/env python3
"""
HFortix Test Runner - v0.5.0

Runs all auto-generated tests for FortiOS API endpoints.

Usage:
    python __runtests__.py              # Run all tests
    python __runtests__.py --cmdb       # Run only CMDB tests
    python __runtests__.py --monitor    # Run only Monitor tests
    python __runtests__.py --log        # Run only Log tests
    python __runtests__.py --verbose    # Verbose output
    python __runtests__.py --fast       # Skip slow tests
    python __runtests__.py --failed     # Re-run only failed tests

Test Coverage:
    - CMDB API: 886 auto-generated endpoint tests
    - Monitor API: 295 auto-generated endpoint tests  
    - Log API: 5 manual structure tests
    
Total: 1,200+ test files
"""

import sys
import subprocess
import argparse
from pathlib import Path


def get_venv_python() -> str:
    """
    Get the path to the virtual environment Python executable.
    
    Returns:
        Path to venv Python, or sys.executable if not found
    """
    # Look for .venv in project root (2 levels up from this file)
    project_root = Path(__file__).parent.parent.parent
    venv_python = project_root / ".venv" / "bin" / "python"
    
    if venv_python.exists():
        return str(venv_python)
    
    # Fallback to current Python
    return sys.executable


def run_pytest(args: list[str]) -> int:
    """
    Run pytest with the given arguments.
    
    Args:
        args: List of pytest arguments
        
    Returns:
        Exit code from pytest
    """
    # Use venv python -m pytest to ensure we use the correct environment
    python_exe = get_venv_python()
    cmd = [python_exe, "-m", "pytest"] + args
    print(f"\n🧪 Running: {' '.join(cmd)}\n")
    result = subprocess.run(cmd)
    return result.returncode


def main():
    """Main test runner."""
    parser = argparse.ArgumentParser(
        description="HFortix Test Runner - Run all FortiOS API tests"
    )
    
    # Test selection
    parser.add_argument(
        "--cmdb",
        action="store_true",
        help="Run only CMDB (configuration) tests"
    )
    parser.add_argument(
        "--monitor",
        action="store_true",
        help="Run only Monitor (status/stats) tests"
    )
    parser.add_argument(
        "--log",
        action="store_true",
        help="Run only Log query tests"
    )
    parser.add_argument(
        "--category",
        type=str,
        help="Run tests for specific category (e.g., 'firewall', 'system')"
    )
    
    # Test behavior
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output (show all test names)"
    )
    parser.add_argument(
        "-vv", "--very-verbose",
        action="store_true",
        help="Very verbose output (show detailed test output)"
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Skip slow tests (marked with @pytest.mark.slow)"
    )
    parser.add_argument(
        "--failed",
        action="store_true",
        help="Re-run only failed tests from last run"
    )
    parser.add_argument(
        "--exitfirst", "-x",
        action="store_true",
        help="Exit on first test failure"
    )
    
    # Output options
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Quiet output (minimal)"
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Show only test summary (no individual results)"
    )
    parser.add_argument(
        "--html",
        type=str,
        metavar="FILE",
        help="Generate HTML test report (requires pytest-html)"
    )
    
    # Coverage
    parser.add_argument(
        "--cov",
        action="store_true",
        help="Run with coverage report (requires pytest-cov)"
    )
    
    # Additional pytest args
    parser.add_argument(
        "pytest_args",
        nargs="*",
        help="Additional arguments to pass to pytest"
    )
    
    args = parser.parse_args()
    
    # Build pytest arguments
    pytest_args = []
    
    # Test directory selection
    test_base = Path(__file__).parent / "api"
    
    if args.cmdb:
        pytest_args.append(str(test_base / "cmdb"))
    elif args.monitor:
        pytest_args.append(str(test_base / "monitor"))
    elif args.log:
        pytest_args.append(str(test_base / "log"))
    elif args.category:
        # Try to find category in cmdb or monitor
        cmdb_path = test_base / "cmdb" / args.category
        monitor_path = test_base / "monitor" / args.category
        
        if cmdb_path.exists():
            pytest_args.append(str(cmdb_path))
        elif monitor_path.exists():
            pytest_args.append(str(monitor_path))
        else:
            print(f"❌ Category '{args.category}' not found in cmdb or monitor")
            return 1
    else:
        # Run all tests
        pytest_args.append(str(test_base))
    
    # Verbosity
    if args.very_verbose:
        pytest_args.append("-vv")
    elif args.verbose:
        pytest_args.append("-v")
    elif args.quiet:
        pytest_args.append("-q")
    elif args.summary:
        pytest_args.append("--tb=no")
        pytest_args.append("-q")
    
    # Test behavior
    if args.fast:
        pytest_args.extend(["-m", "not slow"])
    
    if args.failed:
        pytest_args.append("--lf")  # Last failed
    
    if args.exitfirst:
        pytest_args.append("-x")
    
    # Coverage
    if args.cov:
        pytest_args.extend([
            "--cov=hfortix_fortios",
            "--cov-report=term-missing",
            "--cov-report=html"
        ])
    
    # HTML report
    if args.html:
        pytest_args.extend(["--html", args.html, "--self-contained-html"])
    
    # Add parallel execution (pytest-xdist)
    pytest_args.extend(["-n", "8", "-q"])
    
    # Add user-specified pytest args
    if args.pytest_args:
        pytest_args.extend(args.pytest_args)
    
    # Show test info
    print("=" * 80)
    print("🧪 HFortix Test Runner - v0.5.0")
    print("=" * 80)
    print(f"Test Directory: {test_base}")
    print(f"Test Selection: ", end="")
    
    if args.cmdb:
        print("CMDB only (~886 tests)")
    elif args.monitor:
        print("Monitor only (~295 tests)")
    elif args.log:
        print("Log only (~5 tests)")
    elif args.category:
        print(f"Category '{args.category}'")
    else:
        print("All tests (~1,200 tests)")
    
    print("=" * 80)
    
    # Run tests
    exit_code = run_pytest(pytest_args)
    
    # Summary
    print("\n" + "=" * 80)
    if exit_code == 0:
        print("✅ All tests passed!")
    else:
        print(f"❌ Tests failed with exit code {exit_code}")
    print("=" * 80)
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
