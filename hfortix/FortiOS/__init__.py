"""
FortiOS Python SDK

Python client for interacting with Fortinet FortiGate firewalls via REST API.
Supports configuration management (CMDB), monitoring, logging, and services.

Main Classes:
    FortiOS: Main API client class

API Categories:
    - cmdb: Configuration Management Database
    - monitor: Real-time monitoring and status
    - log: Log queries and analysis
    - service: System services

Exceptions:
    FortinetError: Base exception for FortiOS-specific errors
    AuthenticationError: Authentication failure
    APIError: API request/response errors
"""

# Version information
__version__ = "0.3.38"
__author__ = "Herman W. Jacobsen"
__license__ = "Proprietary"
__email__ = "herman@wjacobsen.fo"
__url__ = "https://github.com/hermanwjacobsen/hfortix"

# Version info tuple for programmatic access
# Handle dev/rc/alpha/beta versions by stripping them for the tuple
_version_base = (
    __version__.split("-dev")[0]
    .split("-rc")[0]
    .split("-alpha")[0]
    .split("-beta")[0]
    .split(".dev")[0]
    .split(".rc")[0]
    .split(".alpha")[0]
    .split(".beta")[0]
)
VERSION = tuple(map(int, _version_base.split(".")))

from .exceptions import (  # noqa: E402
    APIError,
    AuthenticationError,
    FortinetError,
)

# Public API
from .fortios import FortiOS  # noqa: E402
from .performance_test import quick_test, run_performance_test  # noqa: E402

__all__ = [
    # Main client
    "FortiOS",
    # Exceptions
    "FortinetError",
    "AuthenticationError",
    "APIError",
    # Performance testing
    "run_performance_test",
    "quick_test",
    # Version info
    "__version__",
    "__author__",
    "__license__",
    "__email__",
    "__url__",
    "VERSION",
]
