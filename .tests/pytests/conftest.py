"""
Pytest configuration for HFortix tests.

Implements smart parallelization:
- Validator tests run in parallel (no API calls, CPU-bound)
- API call tests run serially (one at a time to avoid overwhelming FortiGate)
"""
import pytest
import warnings


def pytest_collection_modifyitems(config, items):
    """
    Modify test items to control parallelization.
    
    When running with pytest-xdist (-n flag):
    - Tests marked with 'api_call' all get the same group name
    - This forces them to run one at a time in the same worker
    - Validator tests run in parallel across all workers
    """
    for item in items:
        # Check if test makes API calls
        if 'api_call' in item.keywords:
            # Force sequential execution for ALL API calls by grouping them
            # All tests with same group run sequentially in same worker
            item.add_marker(pytest.mark.xdist_group('serial_api_calls'))


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers",
        "xdist_group(name): group tests to run sequentially within pytest-xdist"
    )
    
    # Filter out pytest-xdist teardown warnings (known issue with pytest-xdist)
    warnings.filterwarnings(
        "ignore",
        category=pytest.PytestUnraisableExceptionWarning,
        message=".*pytest_sessionfinish.*"
    )
    warnings.filterwarnings(
        "ignore", 
        category=DeprecationWarning,
        message=".*PluggyTeardownRaisedWarning.*"
    )


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """
    Clean session finish hook to prevent teardown warnings.
    
    This hook runs before the default hooks and helps prevent
    the "already closed" warnings from pytest-xdist workers.
    """
    try:
        # Clean any remaining resources
        pass
    except Exception:
        # Silently ignore any teardown errors
        pass
