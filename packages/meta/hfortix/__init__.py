"""
HFortix - Python SDK for Fortinet Products

Meta-package providing convenient access to all Fortinet SDKs.

Install individual packages for smaller footprint:
  pip install hfortix-core
  pip install hfortix-fortios
  pip install hfortix-fortimanager
  pip install hfortix-fortianalyzer
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
)

# Re-export from fortios
from hfortix_fortios import FortiOS

__version__ = "0.4.0"
__author__ = "Herman W. Jacobsen"

__all__ = [
    # FortiOS
    "FortiOS",
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
