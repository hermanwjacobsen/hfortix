"""Type stubs for FortiOS API v2."""

from typing import Literal
import logging

from .client import FortiOS as FortiOS
from .models import FortiObject as FortiObject
from .models import FortiObjectList as FortiObjectList

# FortiManager proxy support
from .fmg_proxy import FortiManagerProxy as FortiManagerProxy
from .fmg_proxy import ProxyResponse as ProxyResponse
from .fmg_proxy import DeviceResult as DeviceResult

# API categories (accessed via FortiOS instance, not imported directly)
# These are exposed in __all__ for documentation but accessed as client.cmdb, client.log, etc.
from .api import CMDB as CMDB
from .api import Log as Log
from .api import Monitor as Monitor
from .api import Service as Service
from .formatting import to_csv as to_csv
from .formatting import to_dict as to_dict
from .formatting import to_json as to_json
from .formatting import to_multiline as to_multiline
from .formatting import to_quoted as to_quoted
from .help import help as help
from .types import (
    ActionType as ActionType,
    FortiOSErrorResponse as FortiOSErrorResponse,
    FortiOSResponse as FortiOSResponse,
    FortiOSSuccessResponse as FortiOSSuccessResponse,
    FortiOSListResponse as FortiOSListResponse,
    FortiOSDictResponse as FortiOSDictResponse,
    LogSeverity as LogSeverity,
    ProtocolType as ProtocolType,
    ScheduleType as ScheduleType,
    StatusType as StatusType,
)

# Re-exported from hfortix_core
from hfortix_core import (
    APIError as APIError,
    AuthenticationError as AuthenticationError,
    AuthorizationError as AuthorizationError,
    BadRequestError as BadRequestError,
    CircuitBreakerOpenError as CircuitBreakerOpenError,
    ConfigurationError as ConfigurationError,
    DebugSession as DebugSession,
    DuplicateEntryError as DuplicateEntryError,
    EntryInUseError as EntryInUseError,
    FortinetError as FortinetError,
    InvalidValueError as InvalidValueError,
    MethodNotAllowedError as MethodNotAllowedError,
    NonRetryableError as NonRetryableError,
    OperationNotSupportedError as OperationNotSupportedError,
    PermissionDeniedError as PermissionDeniedError,
    RateLimitError as RateLimitError,
    ReadOnlyModeError as ReadOnlyModeError,
    ResourceNotFoundError as ResourceNotFoundError,
    RetryableError as RetryableError,
    ServerError as ServerError,
    ServiceUnavailableError as ServiceUnavailableError,
    TimeoutError as TimeoutError,
    VDOMError as VDOMError,
    debug_timer as debug_timer,
    format_connection_stats as format_connection_stats,
    format_request_info as format_request_info,
    print_debug_info as print_debug_info,
)

__version__: str

__all__ = [
    # Main client
    "FortiOS",
    "FortiObject",
    "FortiObjectList",
    "configure_logging",
    # FortiManager proxy
    "FortiManagerProxy",
    "ProxyResponse",
    "DeviceResult",
    # Formatting utilities
    "to_json",
    "to_csv",
    "to_dict",
    "to_multiline",
    "to_quoted",
    # Help system
    "help",
    # Type definitions
    "FortiOSSuccessResponse",
    "FortiOSListResponse",
    "FortiOSDictResponse",
    "FortiOSErrorResponse",
    "FortiOSResponse",
    "ActionType",
    "StatusType",
    "LogSeverity",
    "ScheduleType",
    "ProtocolType",
    # Debug utilities
    "DebugSession",
    "debug_timer",
    "format_connection_stats",
    "format_request_info",
    "print_debug_info",
    # Categories (legacy)
    "CMDB",
    "Monitor",
    "Service",
    "Log",
    # Exceptions
    "FortinetError",
    "APIError",
    "AuthenticationError",
    "AuthorizationError",
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
]


def configure_logging(
    level: str | int = ...,
    format: Literal["json", "text"] = ...,
    handler: logging.Handler | None = ...,
    use_color: bool = ...,
    include_trace: bool = ...,
    output_file: str | None = ...,
    structured: bool = ...,
) -> None:
    """Configure logging for HFortix library."""
    ...
