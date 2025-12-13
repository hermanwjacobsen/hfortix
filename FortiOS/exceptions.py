"""
FortiOS Exceptions
Backward compatibility wrapper - imports from base exceptions and FortiOS-specific modules
"""

# Import base exceptions
from exceptions import (
    FortinetError,
    AuthenticationError,
    AuthorizationError,
    APIError,
    ResourceNotFoundError,
    BadRequestError,
    MethodNotAllowedError,
    RateLimitError,
    ServerError,
    get_http_status_description,
    HTTP_STATUS_CODES,
)

# Import FortiOS-specific exceptions and helpers
from exceptions_forti import (
    DuplicateEntryError,
    EntryInUseError,
    InvalidValueError,
    PermissionDeniedError,
    get_error_description,
    raise_for_status,
    FORTIOS_ERROR_CODES,
)

# Backward compatibility aliases
FortiOSError = FortinetError
LoginError = AuthenticationError

__all__ = [
    # Base exceptions
    'FortinetError',
    'FortiOSError',
    'AuthenticationError',
    'LoginError',
    'AuthorizationError',
    'APIError',
    
    # Specific exceptions
    'ResourceNotFoundError',
    'BadRequestError',
    'MethodNotAllowedError',
    'RateLimitError',
    'ServerError',
    'DuplicateEntryError',
    'EntryInUseError',
    'InvalidValueError',
    'PermissionDeniedError',
    
    # Helper functions
    'get_error_description',
    'get_http_status_description',
    'raise_for_status',
    
    # Data
    'HTTP_STATUS_CODES',
    'FORTIOS_ERROR_CODES',
]