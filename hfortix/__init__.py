"""
HFortix - Python client library for Fortinet products

This package provides Python SDKs for Fortinet products:
- FortiOS: FortiGate firewall management
- FortiManager: Centralized management (coming soon)
- FortiAnalyzer: Log analysis and reporting (coming soon)

Each product module can be used independently or as part of the complete
package.

Examples:
    # Recommended: Import from main package
    from hfortix import FortiOS

    # Also works: Import from submodule
    from hfortix.FortiOS import FortiOS

    # Import base exceptions
    from hfortix import FortinetError, APIError
"""

from __future__ import annotations

import logging

from .FortiOS import (  # noqa: F401
    FortiOS,
    __author__,
    __version__,
)
from .FortiOS.exceptions import (
    FORTIOS_ERROR_CODES,
    HTTP_STATUS_CODES,
    APIError,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    CircuitBreakerOpenError,
    DuplicateEntryError,
    EntryInUseError,
    FortinetError,
    InvalidValueError,
    MethodNotAllowedError,
    PermissionDeniedError,
    RateLimitError,
    ResourceNotFoundError,
    ServerError,
    ServiceUnavailableError,
    TimeoutError,
    get_error_description,
    get_http_status_description,
    raise_for_status,
)

# Canonical public API for the hfortix package.
#
# Backward compatibility shims are intentionally not provided here.


# Export what's available
__all__ = [
    # Version info
    "__version__",
    "__author__",
    # Base exceptions (always available)
    "FortinetError",
    "AuthenticationError",
    "AuthorizationError",
    "APIError",
    # HTTP status exceptions
    "ResourceNotFoundError",
    "BadRequestError",
    "MethodNotAllowedError",
    "RateLimitError",
    "ServerError",
    "ServiceUnavailableError",
    # Connection and reliability exceptions
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
    # Data
    "HTTP_STATUS_CODES",
    "FORTIOS_ERROR_CODES",
    # Utility functions
    "get_available_modules",
    "get_version",
    "set_log_level",
]

__all__.append("FortiOS")


def get_available_modules():
    """
    Get list of available Fortinet product modules.

    Returns:
        dict: Dictionary with module names as keys and availability as values

    Example:
    >>> from hfortix import get_available_modules
        >>> modules = get_available_modules()
        >>> print(modules)
        {'FortiOS': True, 'FortiManager': False, 'FortiAnalyzer': False}
    """
    return {
        "FortiOS": True,
        "FortiManager": False,
        "FortiAnalyzer": False,
    }


def get_version():
    """
    Get the current version of the Fortinet SDK.

    Returns:
        str: Version string

    Example:
    >>> from hfortix import get_version
        >>> print(get_version())
        '0.1.0'
    """
    return __version__


def set_log_level(level: str = "WARNING") -> None:
    """
    Set logging level for hfortix SDK globally

    Controls the verbosity of logging output across all hfortix instances.
    By default, logging is minimal (WARNING level).
    Use this function to enable detailed logging for debugging or monitoring.

    Args:
        level: Log level as string. Options:
            - 'DEBUG': Very verbose - all requests, parameters, responses,
            timing
            - 'INFO': Normal - request summaries and timings
            - 'WARNING': Quiet - only warnings and errors (default)
            - 'ERROR': Silent - only errors
            - 'OFF': Completely silent - no logging output

    Examples:
        >>> import hfortix
        >>>
        >>> # Enable detailed debugging
        >>> hfortix.set_log_level('DEBUG')
        >>> fgt = hfortix.FortiOS("192.168.1.99", token="...")
        >>> fgt.api.cmdb.firewall.address.list()
        # Shows: Request details, parameters, response, timing

        >>> # Normal operation logging
        >>> hfortix.set_log_level('INFO')
        >>> fgt.api.cmdb.firewall.address.create(name='test',
        subnet='10.0.0.1/32')
        # Shows: POST firewall/address → 200 (0.23s)

        >>> # Completely silent
        >>> hfortix.set_log_level('OFF')
        >>> fgt.api.cmdb.firewall.address.list()
        # No output

    Note:
        - This sets the global log level for all hfortix instances
        - Can be called multiple times to change level dynamically
        - Use debug='info' parameter in FortiOS() for per-instance control
        - Sensitive data (passwords, tokens) is automatically sanitized

    See Also:
        FortiOS.__init__() - Use debug parameter for per-instance logging
    """
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "OFF": logging.CRITICAL + 10,  # Above CRITICAL = effectively disabled
    }

    log_level = level_map.get(level.upper(), logging.WARNING)
    logger = logging.getLogger("hfortix")
    logger.setLevel(log_level)

    # Configure basic logging if not already configured
    if not logging.getLogger().handlers:
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
