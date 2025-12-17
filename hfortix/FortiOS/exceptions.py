"""FortiOS exception exports.

This module exports all FortiOS exceptions and error handling utilities.
All exception classes are defined in exceptions_forti.py.
"""

from .exceptions_forti import (  # Base exceptions; HTTP status exceptions; FortiOS-specific exceptions; Helper functions; Data
    FORTIOS_ERROR_CODES, HTTP_STATUS_CODES, APIError, AuthenticationError,
    AuthorizationError, BadRequestError, CircuitBreakerOpenError,
    DuplicateEntryError, EntryInUseError, FortinetError, InvalidValueError,
    MethodNotAllowedError, PermissionDeniedError, RateLimitError,
    ResourceNotFoundError, ServerError, ServiceUnavailableError, TimeoutError,
    get_error_description, get_http_status_description, raise_for_status)

__all__ = [
    # Base exceptions
    "FortinetError",
    "AuthenticationError",
    "AuthorizationError",
    "APIError",
    # Specific exceptions
    "ResourceNotFoundError",
    "BadRequestError",
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
    # Helper functions
    "get_error_description",
    "get_http_status_description",
    "raise_for_status",
    # Data
    "HTTP_STATUS_CODES",
    "FORTIOS_ERROR_CODES",
]
