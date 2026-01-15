"""
HFortix FortiOS - Python SDK for FortiGate

Provides comprehensive API client for FortiOS with:
- Full CRUD operations
- Firewall policy management
- Schedule, service, and shaper configuration
- Async support
"""

from __future__ import annotations

import logging
import sys
from typing import Any, Literal

# Import commonly used exceptions
# Import debug utilities from core for convenience
from hfortix_core import (
    APIError,
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    CircuitBreakerOpenError,
    ConfigurationError,
    DebugSession,
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
    debug_timer,
    format_connection_stats,
    format_request_info,
    print_debug_info,
)

from .client import FortiOS
from .formatting import to_csv, to_dict, to_json, to_multiline, to_quoted
from .help import help
from .models import FortiObject, FortiObjectList

# Import type definitions for IDE support
from .types import (
    ActionType,
    FortiOSErrorResponse,
    FortiOSResponse,
    FortiOSSuccessResponse,
    FortiOSListResponse,
    FortiOSDictResponse,
    LogSeverity,
    ProtocolType,
    ScheduleType,
    StatusType,
)

__version__ = "0.5.75"

__all__ = [
    # Main client
    "FortiOS",
    "FortiObject",
    "FortiObjectList",
    "configure_logging",
    # Formatting utilities
    "to_json",
    "to_csv",
    "to_dict",
    "to_multiline",
    "to_quoted",
    # Help system
    "help",
    # Type definitions for IDE support
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
    # Convenience wrappers - commented out, using generated API
    # "FirewallPolicy",
    # "IPMACBindingSetting",
    # "IPMACBindingTable",
    # "ScheduleGroup",
    # "ScheduleOnetime",
    # "ScheduleRecurring",
    # "ServiceCategory",
    # "ServiceCustom",
    # "ServiceGroup",
    # "ShaperPerIp",
    # "TrafficShaper",
    # Debug utilities
    "DebugSession",
    "debug_timer",
    "format_connection_stats",
    "format_request_info",
    "print_debug_info",
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
    level: str | int = "INFO",
    format: Literal["json", "text"] = "text",
    handler: logging.Handler | None = None,
    use_color: bool = False,
    include_trace: bool = False,
    output_file: str | None = None,
    structured: bool = False,
) -> None:
    """
    Configure logging for HFortix library

    Provides a convenient way to set up structured logging for all
    HFortix loggers. Useful for enterprise observability with log
    aggregation systems (ELK, Splunk, CloudWatch).

    Args:
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL) or numeric value  # noqa: E501
        format: Output format - "json" for structured logs or "text" for human-readable  # noqa: E501
        handler: Custom logging handler (optional, default: StreamHandler to stdout)  # noqa: E501
        use_color: Use ANSI color codes in text format (default: False)
        include_trace: Include request/trace IDs in all logs (default: False)
        output_file: Path to log file (logs to both file and console if provided)  # noqa: E501
        structured: Force structured logging with extra fields (default: False)

    Examples:
        Basic text logging:

        >>> from hfortix_fortios import configure_logging, FortiOS
        >>> configure_logging(level="INFO", format="text")
        >>> fgt = FortiOS("192.168.1.99", token="token")

        Structured JSON logging for ELK/Splunk:

        >>> configure_logging(level="INFO", format="json")
        >>> # All logs now output as JSON

        Debug logging with colors:

        >>> configure_logging(level="DEBUG", format="text", use_color=True)
        >>> # Debug logs with ANSI colors

        Log to file:

        >>> configure_logging(level="INFO", format="json", output_file="/var/log/hfortix.log")  # noqa: E501
        >>> # Logs to both console and file

        With request tracing:

        >>> configure_logging(level="INFO", format="json", include_trace=True)
        >>> # All logs include request_id for correlation

    Note:
        This configures all loggers under the "hfortix" namespace:
        - hfortix.http (HTTP client operations)
        - hfortix.audit (Audit logging)
        - hfortix.core (Core utilities)
    """
    # Import formatters from logging package
    from hfortix_core.logging import StructuredFormatter, TextFormatter

    # Get root hfortix logger
    logger = logging.getLogger("hfortix")

    # Convert level string to logging constant
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)

    logger.setLevel(level)

    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()

    # Choose formatter based on format type or structured flag
    if format == "json" or structured:
        formatter: logging.Formatter = StructuredFormatter()
    else:
        formatter = TextFormatter(use_color=use_color)

    # Create console handler if not provided
    if handler is None:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    else:
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Add file handler if output_file is specified
    if output_file:
        file_handler = logging.FileHandler(output_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info(f"Logging to file: {output_file}")

    # Prevent propagation to root logger to avoid duplicate logs
    logger.propagate = False

    # Log configuration
    extra: dict[str, Any] = {
        "format": format,
        "level": logging.getLevelName(level),
    }
    if include_trace:
        extra["trace_enabled"] = "true"
    if output_file:
        extra["output_file"] = output_file

    logger.debug(
        f"Logging configured: level={logging.getLevelName(level)}, format={format}",  # noqa: E501
        extra=extra,
    )
