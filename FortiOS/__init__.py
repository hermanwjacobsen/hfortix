"""
FortiOS Python SDK

Python client for interacting with Fortinet FortiGate firewalls via REST API.
Supports configuration management (CMDB), monitoring, logging, and services.

Main Classes:
    FortiOS: Main API client class
    
API Categories:
    - cmdb: Configuration Management Database
    - monitor: Real-time monitoring and status
    - log: Log queries and analysis
    - service: System services

Exceptions:
    FortiOSError: Base exception for FortiOS-specific errors
    LoginError: Authentication failure
    APIError: API request/response errors
"""

# Version information
__version__ = "0.3.6"
__author__ = "Herman W. Jacobsen"
__license__ = "MIT"
__email__ = "herman@wjacobsen.fo"
__url__ = "https://github.com/hermanwjacobsen/hfortix"

# Version info tuple for programmatic access
VERSION = tuple(map(int, __version__.split('.')))

# Public API
from .fortios import FortiOS
from .exceptions import APIError, FortiOSError, LoginError

__all__ = [
    # Main client
    'FortiOS',
    
    # Exceptions
    'FortiOSError',
    'LoginError', 
    'APIError',
    
    # Version info
    '__version__',
    '__author__',
    '__license__',
    '__email__',
    '__url__',
    'VERSION',
]
