"""Type stubs for hfortix meta package."""
from typing import Optional

# Core exceptions and utilities
from hfortix_core import (
    APIError as APIError,
    AuthenticationError as AuthenticationError,
    AuthorizationError as AuthorizationError,
    BadRequestError as BadRequestError,
    CircuitBreakerOpenError as CircuitBreakerOpenError,
    ConfigurationError as ConfigurationError,
    DuplicateEntryError as DuplicateEntryError,
    EntryInUseError as EntryInUseError,
    FortinetError as FortinetError,
    InvalidValueError as InvalidValueError,
    MethodNotAllowedError as MethodNotAllowedError,
    NonRetryableError as NonRetryableError,
    OperationNotSupportedError as OperationNotSupportedError,
    PermissionDeniedError as PermissionDeniedError,
    RateLimitError as RateLimitError,
    ReadOnlyModeError as ReadOnlyModeError,
    ResourceNotFoundError as ResourceNotFoundError,
    RetryableError as RetryableError,
    ServerError as ServerError,
    ServiceUnavailableError as ServiceUnavailableError,
    TimeoutError as TimeoutError,
    VDOMError as VDOMError,
    fmt as fmt,
)

# FortiOS (always available)
from hfortix_fortios import FortiOS as FortiOS

# FortiManager (optional - available with hfortix[fortimanager] or hfortix[all])
try:
    from hfortix_fortimanager import FortiManager as FortiManager
except ImportError:
    FortiManager: Optional[type] = None  # type: ignore

# FortiAnalyzer (optional - available with hfortix[fortianalyzer] or hfortix[all])
try:
    from hfortix_fortianalyzer import FortiAnalyzer as FortiAnalyzer
except ImportError:
    FortiAnalyzer: Optional[type] = None  # type: ignore

# FortiCare (optional - available with hfortix[forticare] or hfortix[all])
try:
    from hfortix_forticare import FortiCare as FortiCare
except ImportError:
    FortiCare: Optional[type] = None  # type: ignore

# FortiZTP (optional - available with hfortix[fortiztp] or hfortix[all])
try:
    from hfortix_fortiztp import FortiZTP as FortiZTP
except ImportError:
    FortiZTP: Optional[type] = None  # type: ignore

__version__: str
__author__: str

__all__: list[str]
