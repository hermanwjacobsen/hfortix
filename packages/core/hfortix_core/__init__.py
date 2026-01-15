"""
HFortix Core - Shared foundation for Fortinet SDKs

Provides:
- Common exception hierarchy
- HTTP client framework (sync and async)
- Shared utilities and type definitions
"""

from . import fmt
from .cache import (
    TTLCache,
    readonly_cache,
)
from .debug import (
    DebugSession,
    debug_timer,
    format_connection_stats,
    format_request_info,
    print_debug_info,
)
from .deprecation import (
    check_deprecated_fields,
    warn_deprecated_field,
)
from .http import HTTPClientFMG
from .exceptions import (
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
    ValidationError,
    VDOMError,
)
from .logging import (
    RequestLogger,
    StructuredFormatter,
    TextFormatter,
    log_operation,
)
from .types import (
    APIResponse,
    CircuitBreakerState,
    ConnectionStats,
    ErrorResponse,
    ListResponse,
    ObjectResponse,
    RequestInfo,
)

__version__ = "0.5.76"

__all__ = [
    # Cache utilities
    "TTLCache",
    "readonly_cache",
    # Deprecation utilities
    "check_deprecated_fields",
    "warn_deprecated_field",
    # Formatting utilities
    "fmt",
    # Exceptions
    "FortinetError",
    "APIError",
    "AuthenticationError",
    "AuthorizationError",
    "ValidationError",
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
    # Type definitions
    "APIResponse",
    "ListResponse",
    "ObjectResponse",
    "ErrorResponse",
    "ConnectionStats",
    "RequestInfo",
    "CircuitBreakerState",
    # Logging utilities
    "RequestLogger",
    "log_operation",
    "StructuredFormatter",
    "TextFormatter",
    # Debug utilities
    "DebugSession",
    "debug_timer",
    "format_connection_stats",
    "format_request_info",
    "print_debug_info",
    # HTTP clients
    "HTTPClientFMG",
]
