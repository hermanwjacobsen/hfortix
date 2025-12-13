"""
Fortinet Base Exceptions
Base exception classes for all Fortinet products (FortiOS, FortiManager, FortiAnalyzer, etc.)
"""


# ============================================================================
# Base Exceptions
# ============================================================================

class FortinetError(Exception):
    """Base exception for all Fortinet API errors"""
    pass


class AuthenticationError(FortinetError):
    """Authentication failed (login, token, credentials)"""
    pass


class AuthorizationError(FortinetError):
    """Authorization failed (insufficient permissions, access denied)"""
    pass


class APIError(FortinetError):
    """
    API request failed
    
    Attributes:
        http_status (int): HTTP status code (400, 401, 403, 404, 500, etc.)
        error_code (int): Product-specific internal error code
        message (str): Error message
        response (dict): Full API response if available
    """
    
    def __init__(self, message, http_status=None, error_code=None, response=None):
        """
        Initialize API error
        
        Args:
            message (str): Error message
            http_status (int, optional): HTTP status code
            error_code (int, optional): Product-specific error code
            response (dict, optional): Full API response
        """
        self.http_status = http_status
        self.error_code = error_code
        self.response = response
        self.message = message
        
        # Build detailed error message
        error_parts = [message]
        
        if http_status:
            error_parts.append(f"HTTP {http_status}")
        
        if error_code:
            error_parts.append(f"Error {error_code}")
        
        super().__init__(" | ".join(error_parts))
    
    def __str__(self):
        """String representation with detailed error information"""
        parts = [self.message]
        
        if self.http_status:
            status_desc = HTTP_STATUS_CODES.get(self.http_status, "Unknown")
            parts.append(f"HTTP {self.http_status} ({status_desc})")
        
        if self.error_code:
            # Try to get FortiOS error description if available
            try:
                from exceptions_forti import FORTIOS_ERROR_CODES
                error_desc = FORTIOS_ERROR_CODES.get(self.error_code, "Unknown error")
                parts.append(f"Error {self.error_code}: {error_desc}")
            except ImportError:
                parts.append(f"Error {self.error_code}")
        
        return " | ".join(parts)


# ============================================================================
# HTTP-Specific Exceptions
# ============================================================================

class ResourceNotFoundError(APIError):
    """Resource not found (HTTP 404)"""
    def __init__(self, message="Resource not found", http_status=None, **kwargs):
        if http_status is None:
            http_status = 404
        super().__init__(message, http_status=http_status, **kwargs)


class BadRequestError(APIError):
    """Bad request - invalid syntax or parameters (HTTP 400)"""
    def __init__(self, message="Bad request", **kwargs):
        super().__init__(message, http_status=400, **kwargs)


class MethodNotAllowedError(APIError):
    """HTTP method not allowed for this resource (HTTP 405)"""
    def __init__(self, message="Method not allowed", **kwargs):
        super().__init__(message, http_status=405, **kwargs)


class RateLimitError(APIError):
    """Rate limit exceeded, access temporarily blocked (HTTP 429)"""
    def __init__(self, message="Access temporarily blocked: Maximum failed authentications reached", **kwargs):
        super().__init__(message, http_status=429, **kwargs)


class ServerError(APIError):
    """Internal server error (HTTP 500)"""
    def __init__(self, message="Internal server error", **kwargs):
        super().__init__(message, http_status=500, **kwargs)


# ============================================================================
# HTTP Status Codes
# ============================================================================

HTTP_STATUS_CODES = {
    200: "OK",
    400: "Bad Request: Request cannot be processed by the API",
    401: "Not Authorized: Request without successful login session",
    403: "Forbidden: Request is missing CSRF token or administrator is missing access profile permissions",
    404: "Resource Not Found: Unable to find the specified resource",
    405: "Method Not Allowed: Specified HTTP method is not allowed for this resource",
    413: "Request Entity Too Large: Request cannot be processed due to large entity",
    424: "Failed Dependency: Fail dependency can be duplicate resource, missing required parameter, missing required attribute, invalid attribute value",
    429: "Access temporarily blocked: Maximum failed authentications reached",
    500: "Internal Server Error: Internal error when processing the request",
}


def get_http_status_description(http_status):
    """
    Get human-readable description for HTTP status code
    
    Args:
        http_status (int): HTTP status code (400, 401, 403, etc.)
        
    Returns:
        str: Description of the HTTP status code, or "Unknown" if not found
    """
    return HTTP_STATUS_CODES.get(http_status, "Unknown")


# ============================================================================
# Exports
# ============================================================================

__all__ = [
    # Base exceptions
    'FortinetError',
    'AuthenticationError',
    'AuthorizationError',
    'APIError',
    
    # HTTP-specific exceptions
    'ResourceNotFoundError',
    'BadRequestError',
    'MethodNotAllowedError',
    'RateLimitError',
    'ServerError',
    
    # Helper functions
    'get_http_status_description',
    
    # Data
    'HTTP_STATUS_CODES',
]
