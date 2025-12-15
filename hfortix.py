"""
HFortix - Python client library for Fortinet products

This package provides Python SDKs for Fortinet products:
- FortiOS: FortiGate firewall management
- FortiManager: Centralized management (coming soon)
- FortiAnalyzer: Log analysis and reporting (coming soon)

Each product module can be used independently or as part of the complete package.

Examples:
    # Recommended: Import from main package
    from hfortix import FortiOS
    
    # Also works: Import from submodule
    from hfortix.FortiOS import FortiOS
    
    # Import base exceptions
    from hfortix import FortinetError, APIError
"""

from typing import TYPE_CHECKING

# Import version from FortiOS submodule
try:
    from FortiOS import __version__, __author__
except ImportError:
    # Fallback if FortiOS not installed
    __version__ = '0.3.6'
    __author__ = 'Herman W. Jacobsen'

# Import base exceptions - always available
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

# Try to import FortiOS if available
try:
    from FortiOS import FortiOS
    _FORTIOS_AVAILABLE = True
except ImportError:
    _FORTIOS_AVAILABLE = False
    if not TYPE_CHECKING:
        # Provide a stub for runtime when FortiOS is not available
        FortiOS = None  # type: ignore

# Try to import FortiManager if available (future)
try:
    from FortiManager import FortiManager
    _FORTIMANAGER_AVAILABLE = True
except ImportError:
    _FORTIMANAGER_AVAILABLE = False
    FortiManager = None

# Try to import FortiAnalyzer if available (future)
try:
    from FortiAnalyzer import FortiAnalyzer
    _FORTIANALYZER_AVAILABLE = True
except ImportError:
    _FORTIANALYZER_AVAILABLE = False
    FortiAnalyzer = None

# Export what's available
__all__ = [
    # Version info
    '__version__',
    '__author__',
    
    # Base exceptions (always available)
    'FortinetError',
    'AuthenticationError',
    'AuthorizationError',
    'APIError',
    'ResourceNotFoundError',
    'BadRequestError',
    'MethodNotAllowedError',
    'RateLimitError',
    'ServerError',
    'get_http_status_description',
    'HTTP_STATUS_CODES',
]

# Add products to __all__ if available
if _FORTIOS_AVAILABLE:
    __all__.append('FortiOS')

if _FORTIMANAGER_AVAILABLE:
    __all__.append('FortiManager')

if _FORTIANALYZER_AVAILABLE:
    __all__.append('FortiAnalyzer')


def get_available_modules():
    """
    Get list of available Fortinet product modules.
    
    Returns:
        dict: Dictionary with module names as keys and availability as values
        
    Example:
        >>> from fortinet import get_available_modules
        >>> modules = get_available_modules()
        >>> print(modules)
        {'FortiOS': True, 'FortiManager': False, 'FortiAnalyzer': False}
    """
    return {
        'FortiOS': _FORTIOS_AVAILABLE,
        'FortiManager': _FORTIMANAGER_AVAILABLE,
        'FortiAnalyzer': _FORTIANALYZER_AVAILABLE,
    }


def get_version():
    """
    Get the current version of the Fortinet SDK.
    
    Returns:
        str: Version string
        
    Example:
        >>> from fortinet import get_version
        >>> print(get_version())
        '0.1.0'
    """
    return __version__
