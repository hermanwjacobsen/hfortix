"""
Audit Log Formatters

Provides different formatting options for audit logs to support
various compliance and logging standards.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Protocol, runtime_checkable

__all__ = [
    "AuditFormatter",
    "JSONFormatter",
    "SyslogFormatter",
    "CEFFormatter",
]


def _utc_timestamp() -> str:
    """Return an ISO 8601 UTC timestamp with a trailing Z."""
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


@runtime_checkable
class AuditFormatter(Protocol):
    """Protocol for audit log formatters"""

    def format(self, operation: dict[str, Any]) -> str:
        """
        Format an operation dict as a string

        Args:
            operation: Operation data dictionary

        Returns:
            Formatted string ready for output
        """
        ...


class JSONFormatter:
    """
    Format audit logs as JSON (default)

    Outputs compact JSON on a single line, suitable for log aggregation
    systems like ELK, Splunk, or cloud logging services.

    Example output:
        {"timestamp":"2026-01-02T14:23:45Z","method":"POST",...}
    """

    def __init__(self, pretty: bool = False, indent: int = 2):
        """
        Initialize JSON formatter

        Args:
            pretty: If True, format with indentation for readability
            indent: Number of spaces for indentation (when pretty=True)
        """
        self.pretty = pretty
        self.indent = indent if pretty else None

    def format(self, operation: dict[str, Any]) -> str:
        """Format as JSON string"""
        if self.pretty:
            return json.dumps(operation, indent=self.indent, sort_keys=True)
        return json.dumps(operation, separators=(",", ":"))


class SyslogFormatter:
    """
    Format audit logs for Syslog (RFC 5424)

    Outputs Syslog-formatted messages with proper priority, timestamp,
    and structured data.

    Format:
        <PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID STRUCTURED-DATA MSG  # noqa: E501

    Example output:
        <134>1 2026-01-02T14:23:45Z 192.168.1.99 hfortix - - - {"method":"POST",...}  # noqa: E501
    """

    # Syslog facilities
    FACILITIES = {
        "KERN": 0,
        "USER": 1,
        "MAIL": 2,
        "DAEMON": 3,
        "AUTH": 4,
        "SYSLOG": 5,
        "LPR": 6,
        "NEWS": 7,
        "UUCP": 8,
        "CRON": 9,
        "AUTHPRIV": 10,
        "FTP": 11,
        "LOCAL0": 16,
        "LOCAL1": 17,
        "LOCAL2": 18,
        "LOCAL3": 19,
        "LOCAL4": 20,
        "LOCAL5": 21,
        "LOCAL6": 22,
        "LOCAL7": 23,
    }

    # Syslog severities
    SEVERITIES = {
        "EMERG": 0,
        "ALERT": 1,
        "CRIT": 2,
        "ERR": 3,
        "WARNING": 4,
        "NOTICE": 5,
        "INFO": 6,
        "DEBUG": 7,
    }

    def __init__(
        self,
        facility: str = "LOCAL0",
        severity: str = "INFO",
        app_name: str = "hfortix",
        hostname: str | None = None,
    ):
        """
        Initialize Syslog formatter

        Args:
            facility: Syslog facility (LOCAL0-LOCAL7, USER, etc.)
            severity: Syslog severity (INFO, WARNING, ERR, etc.)
            app_name: Application name for syslog
            hostname: Hostname to use (None = use from operation data)
        """
        self.facility = self.FACILITIES.get(
            facility.upper(), 16
        )  # Default LOCAL0
        self.severity = self.SEVERITIES.get(
            severity.upper(), 6
        )  # Default INFO
        self.app_name = app_name
        self.hostname = hostname

    def format(self, operation: dict[str, Any]) -> str:
        """
        Format as RFC 5424 syslog message

        Priority is calculated as: (facility * 8) + severity
        """
        # Calculate priority
        pri = (self.facility * 8) + self.severity

        # Get hostname from operation or use configured
        hostname = self.hostname or operation.get("host", "-")

        # Get timestamp (use operation timestamp or current time)
        timestamp = operation.get("timestamp", _utc_timestamp())

        # Message is the full operation as JSON
        message = json.dumps(operation, separators=(",", ":"))

        # RFC 5424 format
        # <PRI>VERSION TIMESTAMP HOSTNAME APP-NAME PROCID MSGID STRUCTURED-DATA MSG  # noqa: E501
        return (
            f"<{pri}>1 {timestamp} {hostname} {self.app_name} - - - {message}"
        )


class CEFFormatter:
    """
    Format audit logs as Common Event Format (CEF)

    CEF is widely used by SIEM systems like ArcSight, Splunk, QRadar.

    Format:
        CEF:Version|Device Vendor|Device Product|Device Version|Signature ID|Name|Severity|Extension  # noqa: E501

    Example output:
        CEF:0|Fortinet|FortiGate|7.0|API_OPERATION|FortiGate API Operation|5|
        act=POST dst=192.168.1.99 suser=api-token outcome=success ...
    """

    # CEF severity mapping
    SEVERITY_MAP = {
        "GET": 2,  # Low - read operations
        "POST": 5,  # Medium - create operations
        "PUT": 5,  # Medium - update operations
        "DELETE": 7,  # High - delete operations
    }

    def __init__(
        self,
        device_vendor: str = "Fortinet",
        device_product: str = "FortiGate",
        device_version: str = "7.0",
    ):
        """
        Initialize CEF formatter

        Args:
            device_vendor: Vendor name
            device_product: Product name
            device_version: Product version
        """
        self.device_vendor = device_vendor
        self.device_product = device_product
        self.device_version = device_version

    def format(self, operation: dict[str, Any]) -> str:
        """Format as CEF string"""
        method = operation.get("method", "UNKNOWN")
        # endpoint and success available for future use
        # endpoint = operation.get("endpoint", "")
        # success = operation.get("success", False)

        # CEF header
        severity = self.SEVERITY_MAP.get(method, 5)
        signature_id = "API_OPERATION"
        name = f"FortiGate API {method} Operation"

        header = (
            f"CEF:0|{self.device_vendor}|{self.device_product}|"
            f"{self.device_version}|{signature_id}|{name}|{severity}|"
        )

        # CEF extensions (key-value pairs)
        extensions = []

        # Map operation fields to CEF fields
        if "method" in operation:
            extensions.append(f"act={self._escape(operation['method'])}")

        if "host" in operation:
            extensions.append(f"dst={self._escape(operation['host'])}")

        if "endpoint" in operation:
            extensions.append(f"request={self._escape(operation['endpoint'])}")

        if "success" in operation:
            outcome = "success" if operation["success"] else "failure"
            extensions.append(f"outcome={outcome}")

        if "status_code" in operation:
            extensions.append(
                f"requestClientApplication={operation['status_code']}"
            )

        if "request_id" in operation:
            extensions.append(
                f"requestContext={self._escape(operation['request_id'])}"
            )

        if "vdom" in operation and operation["vdom"]:
            extensions.append(f"dvchost={self._escape(operation['vdom'])}")

        if "duration_ms" in operation:
            extensions.append(f"rt={operation['duration_ms']}")

        if "object_type" in operation:
            extensions.append(
                f"deviceCustomString1={self._escape(operation['object_type'])}"
            )
            extensions.append("deviceCustomString1Label=ObjectType")

        if "object_name" in operation and operation["object_name"]:
            extensions.append(
                f"deviceCustomString2={self._escape(operation['object_name'])}"
            )
            extensions.append("deviceCustomString2Label=ObjectName")

        # Add username (from user_context if available)
        user = "api-token"
        user_context = operation.get("user_context") or {}
        if user_context.get("username"):
            user = user_context["username"]
        extensions.append(f"suser={self._escape(user)}")

        return header + " ".join(extensions)

    @staticmethod
    def _escape(value: str) -> str:
        """Escape special characters for CEF format"""
        if not isinstance(value, str):
            value = str(value)
        # Escape backslash, pipe, equals, and newlines
        return (
            value.replace("\\", "\\\\")
            .replace("|", "\\|")
            .replace("=", "\\=")
            .replace("\n", "\\n")
            .replace("\r", "\\r")
        )
