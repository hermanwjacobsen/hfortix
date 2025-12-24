"""FortiOS exception exports.

This module exports all FortiOS exceptions and error handling utilities.
All exception classes are defined in exceptions_forti.py.
"""

from .exceptions_forti import (  # Base exceptions; HTTP status exceptions; FortiOS-specific exceptions; Helper functions; Data  # noqa: E501
    FORTIOS_ERROR_CODES,
    HTTP_STATUS_CODES,
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
    get_error_description,
    get_http_status_description,
    get_retry_delay,
    is_retryable_error,
    raise_for_status,
)

__all__ = [
    # Base exceptions
    "FortinetError",
    "APIError",
    "AuthenticationError",
    "AuthorizationError",
    # Retry hierarchy
    "RetryableError",
    "NonRetryableError",
    # Client-side exceptions
    "ConfigurationError",
    "VDOMError",
    "OperationNotSupportedError",
    "ReadOnlyModeError",
    # HTTP status exceptions
    "BadRequestError",
    "ResourceNotFoundError",
    "MethodNotAllowedError",
    "RateLimitError",
    "ServerError",
    "ServiceUnavailableError",
    "CircuitBreakerOpenError",
    "TimeoutError",
    # FortiOS-specific exceptions
    "DuplicateEntryError",
    "EntryInUseError",
    "InvalidValueError",
    "PermissionDeniedError",
    # Helper functions
    "get_error_description",
    "get_http_status_description",
    "raise_for_status",
    "is_retryable_error",
    "get_retry_delay",
    # Data
    "HTTP_STATUS_CODES",
    "FORTIOS_ERROR_CODES",
]
