"""
HFortix - Python SDK for Fortinet Products

Meta-package providing convenient access to all Fortinet SDKs.

Install individual packages for smaller footprint:
  pip install hfortix-core
  pip install hfortix-fortios
  pip install hfortix-forticare
  pip install hfortix-fortiztp
"""

# Re-export from core
from hfortix_core import (
    APIError,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    CircuitBreakerOpenError,
    ConfigurationError,
    DuplicateEntryError,
    EntryInUseError,
    FortinetError,
    InvalidValueError,
    MethodNotAllowedError,
    NonRetryableError,
    OperationNotSupportedError,
    PermissionDeniedError,
    RateLimitError,
    ReadOnlyModeError,
    ResourceNotFoundError,
    RetryableError,
    ServerError,
    ServiceUnavailableError,
    TimeoutError,
    VDOMError,
    fmt,
)

# Re-export from fortios
from hfortix_fortios import FortiOS

# Optional imports - only available if extra packages are installed
try:
    from hfortix_fortimanager import FortiManager
    _has_fortimanager = True
except ImportError:
    _has_fortimanager = False
    FortiManager = None  # type: ignore

try:
    from hfortix_fortianalyzer import FortiAnalyzer
    _has_fortianalyzer = True
except ImportError:
    _has_fortianalyzer = False
    FortiAnalyzer = None  # type: ignore

try:
    from hfortix_forticare import FortiCare
    _has_forticare = True
except ImportError:
    _has_forticare = False
    FortiCare = None  # type: ignore

try:
    from hfortix_fortiztp import FortiZTP
    _has_fortiztp = True
except ImportError:
    _has_fortiztp = False
    FortiZTP = None  # type: ignore

__version__ = "0.5.161"
__author__ = "Herman W. Jacobsen"

__all__ = [
    # FortiOS
    "FortiOS",
    # FortiManager (optional)
    "FortiManager",
    # FortiAnalyzer (optional)
    "FortiAnalyzer",
    # FortiCare (optional)
    "FortiCare",
    # FortiZTP (optional)
    "FortiZTP",
    # Formatting utilities
    "fmt",
    # Exceptions
    "FortinetError",
    "APIError",
    "AuthenticationError",
    "AuthorizationError",
    "RetryableError",
    "NonRetryableError",
    "ConfigurationError",
    "VDOMError",
    "OperationNotSupportedError",
    "ReadOnlyModeError",
    "BadRequestError",
    "ResourceNotFoundError",
    "MethodNotAllowedError",
    "RateLimitError",
    "ServerError",
    "ServiceUnavailableError",
    "CircuitBreakerOpenError",
    "TimeoutError",
    "DuplicateEntryError",
    "EntryInUseError",
    "InvalidValueError",
    "PermissionDeniedError",
]
