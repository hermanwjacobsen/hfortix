"""
Validation helpers for extension-controller extender_vap endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = ["local-vap", "lan-ext-vap"]
VALID_BODY_BROADCAST_SSID = ["disable", "enable"]
VALID_BODY_SECURITY = [
    "OPEN",
    "WPA2-Personal",
    "WPA-WPA2-Personal",
    "WPA3-SAE",
    "WPA3-SAE-Transition",
    "WPA2-Enterprise",
    "WPA3-Enterprise-only",
    "WPA3-Enterprise-transition",
    "WPA3-Enterprise-192-bit",
]
VALID_BODY_PMF = ["disabled", "optional", "required"]
VALID_BODY_TARGET_WAKE_TIME = ["disable", "enable"]
VALID_BODY_BSS_COLOR_PARTIAL = ["disable", "enable"]
VALID_BODY_MU_MIMO = ["disable", "enable"]
VALID_BODY_ALLOWACCESS = ["ping", "telnet", "http", "https", "ssh", "snmp"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_extender_vap_get(
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


def validate_extender_vap_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating extender_vap.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate ssid if present
    if "ssid" in payload:
        value = payload.get("ssid")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "ssid cannot exceed 32 characters")

    # Validate max-clients if present
    if "max-clients" in payload:
        value = payload.get("max-clients")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 512:
                    return (False, "max-clients must be between 0 and 512")
            except (ValueError, TypeError):
                return (False, f"max-clients must be numeric, got: {value}")

    # Validate broadcast-ssid if present
    if "broadcast-ssid" in payload:
        value = payload.get("broadcast-ssid")
        if value and value not in VALID_BODY_BROADCAST_SSID:
            return (
                False,
                f"Invalid broadcast-ssid '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SSID)}",
            )

    # Validate security if present
    if "security" in payload:
        value = payload.get("security")
        if value and value not in VALID_BODY_SECURITY:
            return (
                False,
                f"Invalid security '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY)}",
            )

    # Validate dtim if present
    if "dtim" in payload:
        value = payload.get("dtim")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "dtim must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"dtim must be numeric, got: {value}")

    # Validate rts-threshold if present
    if "rts-threshold" in payload:
        value = payload.get("rts-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 256 or int_val > 2347:
                    return (
                        False,
                        "rts-threshold must be between 256 and 2347",
                    )
            except (ValueError, TypeError):
                return (False, f"rts-threshold must be numeric, got: {value}")

    # Validate pmf if present
    if "pm" in payload:
        value = payload.get("pm")
        if value and value not in VALID_BODY_PMF:
            return (
                False,
                f"Invalid pmf '{value}'. Must be one of: {', '.join(VALID_BODY_PMF)}",
            )

    # Validate target-wake-time if present
    if "target-wake-time" in payload:
        value = payload.get("target-wake-time")
        if value and value not in VALID_BODY_TARGET_WAKE_TIME:
            return (
                False,
                f"Invalid target-wake-time '{value}'. Must be one of: {', '.join(VALID_BODY_TARGET_WAKE_TIME)}",
            )

    # Validate bss-color-partial if present
    if "bss-color-partial" in payload:
        value = payload.get("bss-color-partial")
        if value and value not in VALID_BODY_BSS_COLOR_PARTIAL:
            return (
                False,
                f"Invalid bss-color-partial '{value}'. Must be one of: {', '.join(VALID_BODY_BSS_COLOR_PARTIAL)}",
            )

    # Validate mu-mimo if present
    if "mu-mimo" in payload:
        value = payload.get("mu-mimo")
        if value and value not in VALID_BODY_MU_MIMO:
            return (
                False,
                f"Invalid mu-mimo '{value}'. Must be one of: {', '.join(VALID_BODY_MU_MIMO)}",
            )

    # Validate auth-server-address if present
    if "auth-server-address" in payload:
        value = payload.get("auth-server-address")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auth-server-address cannot exceed 63 characters")

    # Validate auth-server-port if present
    if "auth-server-port" in payload:
        value = payload.get("auth-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "auth-server-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-server-port must be numeric, got: {value}",
                )

    # Validate auth-server-secret if present
    if "auth-server-secret" in payload:
        value = payload.get("auth-server-secret")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auth-server-secret cannot exceed 63 characters")

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_extender_vap_put(
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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate ssid if present
    if "ssid" in payload:
        value = payload.get("ssid")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "ssid cannot exceed 32 characters")

    # Validate max-clients if present
    if "max-clients" in payload:
        value = payload.get("max-clients")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 512:
                    return (False, "max-clients must be between 0 and 512")
            except (ValueError, TypeError):
                return (False, f"max-clients must be numeric, got: {value}")

    # Validate broadcast-ssid if present
    if "broadcast-ssid" in payload:
        value = payload.get("broadcast-ssid")
        if value and value not in VALID_BODY_BROADCAST_SSID:
            return (
                False,
                f"Invalid broadcast-ssid '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SSID)}",
            )

    # Validate security if present
    if "security" in payload:
        value = payload.get("security")
        if value and value not in VALID_BODY_SECURITY:
            return (
                False,
                f"Invalid security '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY)}",
            )

    # Validate dtim if present
    if "dtim" in payload:
        value = payload.get("dtim")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "dtim must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"dtim must be numeric, got: {value}")

    # Validate rts-threshold if present
    if "rts-threshold" in payload:
        value = payload.get("rts-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 256 or int_val > 2347:
                    return (
                        False,
                        "rts-threshold must be between 256 and 2347",
                    )
            except (ValueError, TypeError):
                return (False, f"rts-threshold must be numeric, got: {value}")

    # Validate pmf if present
    if "pm" in payload:
        value = payload.get("pm")
        if value and value not in VALID_BODY_PMF:
            return (
                False,
                f"Invalid pmf '{value}'. Must be one of: {', '.join(VALID_BODY_PMF)}",
            )

    # Validate target-wake-time if present
    if "target-wake-time" in payload:
        value = payload.get("target-wake-time")
        if value and value not in VALID_BODY_TARGET_WAKE_TIME:
            return (
                False,
                f"Invalid target-wake-time '{value}'. Must be one of: {', '.join(VALID_BODY_TARGET_WAKE_TIME)}",
            )

    # Validate bss-color-partial if present
    if "bss-color-partial" in payload:
        value = payload.get("bss-color-partial")
        if value and value not in VALID_BODY_BSS_COLOR_PARTIAL:
            return (
                False,
                f"Invalid bss-color-partial '{value}'. Must be one of: {', '.join(VALID_BODY_BSS_COLOR_PARTIAL)}",
            )

    # Validate mu-mimo if present
    if "mu-mimo" in payload:
        value = payload.get("mu-mimo")
        if value and value not in VALID_BODY_MU_MIMO:
            return (
                False,
                f"Invalid mu-mimo '{value}'. Must be one of: {', '.join(VALID_BODY_MU_MIMO)}",
            )

    # Validate auth-server-address if present
    if "auth-server-address" in payload:
        value = payload.get("auth-server-address")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auth-server-address cannot exceed 63 characters")

    # Validate auth-server-port if present
    if "auth-server-port" in payload:
        value = payload.get("auth-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "auth-server-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-server-port must be numeric, got: {value}",
                )

    # Validate auth-server-secret if present
    if "auth-server-secret" in payload:
        value = payload.get("auth-server-secret")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auth-server-secret cannot exceed 63 characters")

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_extender_vap_delete(
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
