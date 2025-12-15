"""
FortiOS Exceptions
Backward compatibility wrapper - imports from base exceptions and FortiOS-specific modules
"""

# Import base exceptions from parent package
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from exceptions import (
        HTTP_STATUS_CODES,
        APIError,
        AuthenticationError,
        AuthorizationError,
        BadRequestError,
        FortinetError,
        MethodNotAllowedError,
        RateLimitError,
        ResourceNotFoundError,
        ServerError,
        get_http_status_description,
    )
except ImportError:
    # Fallback: define minimal exceptions if base module not found
    class FortinetError(Exception):
        """Base exception for all Fortinet SDK errors"""
        pass
    
    class APIError(FortinetError):
        """API request failed"""
        pass
    
    class AuthenticationError(APIError):
        """Authentication failed"""
        pass
    
    class AuthorizationError(APIError):
        """Authorization failed - insufficient permissions"""
        pass
    
    class BadRequestError(APIError):
        """Bad request - invalid parameters"""
        pass
    
    class ResourceNotFoundError(APIError):
        """Requested resource not found"""
        pass
    
    class MethodNotAllowedError(APIError):
        """HTTP method not allowed"""
        pass
    
    class RateLimitError(APIError):
        """Rate limit exceeded"""
        pass
    
    class ServerError(APIError):
        """Server error occurred"""
        pass
    
    HTTP_STATUS_CODES = {}
    
    def get_http_status_description(code):
        return f"HTTP {code}"

# Import FortiOS-specific exceptions and helpers
from exceptions_forti import (
    FORTIOS_ERROR_CODES,
    DuplicateEntryError,
    EntryInUseError,
    InvalidValueError,
    PermissionDeniedError,
    get_error_description,
    raise_for_status,
)

__all__ = [
    # Base exceptions
    'FortinetError',
    'AuthenticationError',
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