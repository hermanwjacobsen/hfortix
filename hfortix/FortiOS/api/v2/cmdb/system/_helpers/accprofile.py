"""
Validation helpers for system accprofile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SCOPE = ["vdom", "global"]
VALID_BODY_SECFABGRP = ["none", "read", "read-write", "custom"]
VALID_BODY_FTVIEWGRP = ["none", "read", "read-write"]
VALID_BODY_AUTHGRP = ["none", "read", "read-write"]
VALID_BODY_SYSGRP = ["none", "read", "read-write", "custom"]
VALID_BODY_NETGRP = ["none", "read", "read-write", "custom"]
VALID_BODY_LOGGRP = ["none", "read", "read-write", "custom"]
VALID_BODY_FWGRP = ["none", "read", "read-write", "custom"]
VALID_BODY_VPNGRP = ["none", "read", "read-write"]
VALID_BODY_UTMGRP = ["none", "read", "read-write", "custom"]
VALID_BODY_WIFI = ["none", "read", "read-write"]
VALID_BODY_ADMINTIMEOUT_OVERRIDE = ["enable", "disable"]
VALID_BODY_CLI_DIAGNOSE = ["enable", "disable"]
VALID_BODY_CLI_GET = ["enable", "disable"]
VALID_BODY_CLI_SHOW = ["enable", "disable"]
VALID_BODY_CLI_EXEC = ["enable", "disable"]
VALID_BODY_CLI_CONFIG = ["enable", "disable"]
VALID_BODY_SYSTEM_EXECUTE_SSH = ["enable", "disable"]
VALID_BODY_SYSTEM_EXECUTE_TELNET = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_accprofile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> # List all objects
        >>> is_valid, error = {func_name}()
    """
    # Validate query parameters if present
    if "action" in params:
        value = params.get("action")
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: {', '.join(VALID_QUERY_ACTION)}",
            )

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_accprofile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating accprofile.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate scope if present
    if "scope" in payload:
        value = payload.get("scope")
        if value and value not in VALID_BODY_SCOPE:
            return (
                False,
                f"Invalid scope '{value}'. Must be one of: {', '.join(VALID_BODY_SCOPE)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate secfabgrp if present
    if "secfabgrp" in payload:
        value = payload.get("secfabgrp")
        if value and value not in VALID_BODY_SECFABGRP:
            return (
                False,
                f"Invalid secfabgrp '{value}'. Must be one of: {', '.join(VALID_BODY_SECFABGRP)}",
            )

    # Validate ftviewgrp if present
    if "ftviewgrp" in payload:
        value = payload.get("ftviewgrp")
        if value and value not in VALID_BODY_FTVIEWGRP:
            return (
                False,
                f"Invalid ftviewgrp '{value}'. Must be one of: {', '.join(VALID_BODY_FTVIEWGRP)}",
            )

    # Validate authgrp if present
    if "authgrp" in payload:
        value = payload.get("authgrp")
        if value and value not in VALID_BODY_AUTHGRP:
            return (
                False,
                f"Invalid authgrp '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHGRP)}",
            )

    # Validate sysgrp if present
    if "sysgrp" in payload:
        value = payload.get("sysgrp")
        if value and value not in VALID_BODY_SYSGRP:
            return (
                False,
                f"Invalid sysgrp '{value}'. Must be one of: {', '.join(VALID_BODY_SYSGRP)}",
            )

    # Validate netgrp if present
    if "netgrp" in payload:
        value = payload.get("netgrp")
        if value and value not in VALID_BODY_NETGRP:
            return (
                False,
                f"Invalid netgrp '{value}'. Must be one of: {', '.join(VALID_BODY_NETGRP)}",
            )

    # Validate loggrp if present
    if "loggrp" in payload:
        value = payload.get("loggrp")
        if value and value not in VALID_BODY_LOGGRP:
            return (
                False,
                f"Invalid loggrp '{value}'. Must be one of: {', '.join(VALID_BODY_LOGGRP)}",
            )

    # Validate fwgrp if present
    if "fwgrp" in payload:
        value = payload.get("fwgrp")
        if value and value not in VALID_BODY_FWGRP:
            return (
                False,
                f"Invalid fwgrp '{value}'. Must be one of: {', '.join(VALID_BODY_FWGRP)}",
            )

    # Validate vpngrp if present
    if "vpngrp" in payload:
        value = payload.get("vpngrp")
        if value and value not in VALID_BODY_VPNGRP:
            return (
                False,
                f"Invalid vpngrp '{value}'. Must be one of: {', '.join(VALID_BODY_VPNGRP)}",
            )

    # Validate utmgrp if present
    if "utmgrp" in payload:
        value = payload.get("utmgrp")
        if value and value not in VALID_BODY_UTMGRP:
            return (
                False,
                f"Invalid utmgrp '{value}'. Must be one of: {', '.join(VALID_BODY_UTMGRP)}",
            )

    # Validate wifi if present
    if "wifi" in payload:
        value = payload.get("wifi")
        if value and value not in VALID_BODY_WIFI:
            return (
                False,
                f"Invalid wifi '{value}'. Must be one of: {', '.join(VALID_BODY_WIFI)}",
            )

    # Validate admintimeout-override if present
    if "admintimeout-override" in payload:
        value = payload.get("admintimeout-override")
        if value and value not in VALID_BODY_ADMINTIMEOUT_OVERRIDE:
            return (
                False,
                f"Invalid admintimeout-override '{value}'. Must be one of: {', '.join(VALID_BODY_ADMINTIMEOUT_OVERRIDE)}",
            )

    # Validate admintimeout if present
    if "admintimeout" in payload:
        value = payload.get("admintimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 480:
                    return (False, "admintimeout must be between 1 and 480")
            except (ValueError, TypeError):
                return (False, f"admintimeout must be numeric, got: {value}")

    # Validate cli-diagnose if present
    if "cli-diagnose" in payload:
        value = payload.get("cli-diagnose")
        if value and value not in VALID_BODY_CLI_DIAGNOSE:
            return (
                False,
                f"Invalid cli-diagnose '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_DIAGNOSE)}",
            )

    # Validate cli-get if present
    if "cli-get" in payload:
        value = payload.get("cli-get")
        if value and value not in VALID_BODY_CLI_GET:
            return (
                False,
                f"Invalid cli-get '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_GET)}",
            )

    # Validate cli-show if present
    if "cli-show" in payload:
        value = payload.get("cli-show")
        if value and value not in VALID_BODY_CLI_SHOW:
            return (
                False,
                f"Invalid cli-show '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_SHOW)}",
            )

    # Validate cli-exec if present
    if "cli-exec" in payload:
        value = payload.get("cli-exec")
        if value and value not in VALID_BODY_CLI_EXEC:
            return (
                False,
                f"Invalid cli-exec '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_EXEC)}",
            )

    # Validate cli-config if present
    if "cli-config" in payload:
        value = payload.get("cli-config")
        if value and value not in VALID_BODY_CLI_CONFIG:
            return (
                False,
                f"Invalid cli-config '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_CONFIG)}",
            )

    # Validate system-execute-ssh if present
    if "system-execute-ssh" in payload:
        value = payload.get("system-execute-ssh")
        if value and value not in VALID_BODY_SYSTEM_EXECUTE_SSH:
            return (
                False,
                f"Invalid system-execute-ssh '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_EXECUTE_SSH)}",
            )

    # Validate system-execute-telnet if present
    if "system-execute-telnet" in payload:
        value = payload.get("system-execute-telnet")
        if value and value not in VALID_BODY_SYSTEM_EXECUTE_TELNET:
            return (
                False,
                f"Invalid system-execute-telnet '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_EXECUTE_TELNET)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_accprofile_put(
    name: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        name: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # name is required for updates
    if not name:
        return (False, "name is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate scope if present
    if "scope" in payload:
        value = payload.get("scope")
        if value and value not in VALID_BODY_SCOPE:
            return (
                False,
                f"Invalid scope '{value}'. Must be one of: {', '.join(VALID_BODY_SCOPE)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate secfabgrp if present
    if "secfabgrp" in payload:
        value = payload.get("secfabgrp")
        if value and value not in VALID_BODY_SECFABGRP:
            return (
                False,
                f"Invalid secfabgrp '{value}'. Must be one of: {', '.join(VALID_BODY_SECFABGRP)}",
            )

    # Validate ftviewgrp if present
    if "ftviewgrp" in payload:
        value = payload.get("ftviewgrp")
        if value and value not in VALID_BODY_FTVIEWGRP:
            return (
                False,
                f"Invalid ftviewgrp '{value}'. Must be one of: {', '.join(VALID_BODY_FTVIEWGRP)}",
            )

    # Validate authgrp if present
    if "authgrp" in payload:
        value = payload.get("authgrp")
        if value and value not in VALID_BODY_AUTHGRP:
            return (
                False,
                f"Invalid authgrp '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHGRP)}",
            )

    # Validate sysgrp if present
    if "sysgrp" in payload:
        value = payload.get("sysgrp")
        if value and value not in VALID_BODY_SYSGRP:
            return (
                False,
                f"Invalid sysgrp '{value}'. Must be one of: {', '.join(VALID_BODY_SYSGRP)}",
            )

    # Validate netgrp if present
    if "netgrp" in payload:
        value = payload.get("netgrp")
        if value and value not in VALID_BODY_NETGRP:
            return (
                False,
                f"Invalid netgrp '{value}'. Must be one of: {', '.join(VALID_BODY_NETGRP)}",
            )

    # Validate loggrp if present
    if "loggrp" in payload:
        value = payload.get("loggrp")
        if value and value not in VALID_BODY_LOGGRP:
            return (
                False,
                f"Invalid loggrp '{value}'. Must be one of: {', '.join(VALID_BODY_LOGGRP)}",
            )

    # Validate fwgrp if present
    if "fwgrp" in payload:
        value = payload.get("fwgrp")
        if value and value not in VALID_BODY_FWGRP:
            return (
                False,
                f"Invalid fwgrp '{value}'. Must be one of: {', '.join(VALID_BODY_FWGRP)}",
            )

    # Validate vpngrp if present
    if "vpngrp" in payload:
        value = payload.get("vpngrp")
        if value and value not in VALID_BODY_VPNGRP:
            return (
                False,
                f"Invalid vpngrp '{value}'. Must be one of: {', '.join(VALID_BODY_VPNGRP)}",
            )

    # Validate utmgrp if present
    if "utmgrp" in payload:
        value = payload.get("utmgrp")
        if value and value not in VALID_BODY_UTMGRP:
            return (
                False,
                f"Invalid utmgrp '{value}'. Must be one of: {', '.join(VALID_BODY_UTMGRP)}",
            )

    # Validate wifi if present
    if "wifi" in payload:
        value = payload.get("wifi")
        if value and value not in VALID_BODY_WIFI:
            return (
                False,
                f"Invalid wifi '{value}'. Must be one of: {', '.join(VALID_BODY_WIFI)}",
            )

    # Validate admintimeout-override if present
    if "admintimeout-override" in payload:
        value = payload.get("admintimeout-override")
        if value and value not in VALID_BODY_ADMINTIMEOUT_OVERRIDE:
            return (
                False,
                f"Invalid admintimeout-override '{value}'. Must be one of: {', '.join(VALID_BODY_ADMINTIMEOUT_OVERRIDE)}",
            )

    # Validate admintimeout if present
    if "admintimeout" in payload:
        value = payload.get("admintimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 480:
                    return (False, "admintimeout must be between 1 and 480")
            except (ValueError, TypeError):
                return (False, f"admintimeout must be numeric, got: {value}")

    # Validate cli-diagnose if present
    if "cli-diagnose" in payload:
        value = payload.get("cli-diagnose")
        if value and value not in VALID_BODY_CLI_DIAGNOSE:
            return (
                False,
                f"Invalid cli-diagnose '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_DIAGNOSE)}",
            )

    # Validate cli-get if present
    if "cli-get" in payload:
        value = payload.get("cli-get")
        if value and value not in VALID_BODY_CLI_GET:
            return (
                False,
                f"Invalid cli-get '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_GET)}",
            )

    # Validate cli-show if present
    if "cli-show" in payload:
        value = payload.get("cli-show")
        if value and value not in VALID_BODY_CLI_SHOW:
            return (
                False,
                f"Invalid cli-show '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_SHOW)}",
            )

    # Validate cli-exec if present
    if "cli-exec" in payload:
        value = payload.get("cli-exec")
        if value and value not in VALID_BODY_CLI_EXEC:
            return (
                False,
                f"Invalid cli-exec '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_EXEC)}",
            )

    # Validate cli-config if present
    if "cli-config" in payload:
        value = payload.get("cli-config")
        if value and value not in VALID_BODY_CLI_CONFIG:
            return (
                False,
                f"Invalid cli-config '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_CONFIG)}",
            )

    # Validate system-execute-ssh if present
    if "system-execute-ssh" in payload:
        value = payload.get("system-execute-ssh")
        if value and value not in VALID_BODY_SYSTEM_EXECUTE_SSH:
            return (
                False,
                f"Invalid system-execute-ssh '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_EXECUTE_SSH)}",
            )

    # Validate system-execute-telnet if present
    if "system-execute-telnet" in payload:
        value = payload.get("system-execute-telnet")
        if value and value not in VALID_BODY_SYSTEM_EXECUTE_TELNET:
            return (
                False,
                f"Invalid system-execute-telnet '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_EXECUTE_TELNET)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_accprofile_delete(
    name: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        name: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not name:
        return (False, "name is required for DELETE operation")

    return (True, None)
