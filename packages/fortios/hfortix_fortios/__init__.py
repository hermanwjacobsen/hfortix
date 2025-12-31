"""
HFortix FortiOS - Python SDK for FortiGate

Provides comprehensive API client for FortiOS with:
- Full CRUD operations
- Firewall policy management
- Schedule, service, and shaper configuration
- Async support
"""

from .client import FortiOS

__version__ = "0.4.0"
__all__ = ["FortiOS"]
