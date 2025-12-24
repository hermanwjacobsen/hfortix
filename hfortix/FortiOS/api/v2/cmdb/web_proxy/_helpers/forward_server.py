"""
Validation helpers for web-proxy forward_server endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ADDR_TYPE = ["ip", "ipv6", "fqdn"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["sdwan", "specify"]
VALID_BODY_MASQUERADE = ["enable", "disable"]
VALID_BODY_HEALTHCHECK = ["disable", "enable"]
VALID_BODY_SERVER_DOWN_OPTION = ["block", "pass"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_forward_server_get(
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


def validate_forward_server_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating forward_server.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate addr-type if present
    if "addr-type" in payload:
        value = payload.get("addr-type")
        if value and value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )

    # Validate fqdn if present
    if "fqdn" in payload:
        value = payload.get("fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fqdn cannot exceed 255 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate masquerade if present
    if "masquerade" in payload:
        value = payload.get("masquerade")
        if value and value not in VALID_BODY_MASQUERADE:
            return (
                False,
                f"Invalid masquerade '{value}'. Must be one of: {', '.join(VALID_BODY_MASQUERADE)}",
            )

    # Validate healthcheck if present
    if "healthcheck" in payload:
        value = payload.get("healthcheck")
        if value and value not in VALID_BODY_HEALTHCHECK:
            return (
                False,
                f"Invalid healthcheck '{value}'. Must be one of: {', '.join(VALID_BODY_HEALTHCHECK)}",
            )

    # Validate monitor if present
    if "monitor" in payload:
        value = payload.get("monitor")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "monitor cannot exceed 255 characters")

    # Validate server-down-option if present
    if "server-down-option" in payload:
        value = payload.get("server-down-option")
        if value and value not in VALID_BODY_SERVER_DOWN_OPTION:
            return (
                False,
                f"Invalid server-down-option '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_DOWN_OPTION)}",
            )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_forward_server_put(
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate addr-type if present
    if "addr-type" in payload:
        value = payload.get("addr-type")
        if value and value not in VALID_BODY_ADDR_TYPE:
            return (
                False,
                f"Invalid addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_TYPE)}",
            )

    # Validate fqdn if present
    if "fqdn" in payload:
        value = payload.get("fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fqdn cannot exceed 255 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate masquerade if present
    if "masquerade" in payload:
        value = payload.get("masquerade")
        if value and value not in VALID_BODY_MASQUERADE:
            return (
                False,
                f"Invalid masquerade '{value}'. Must be one of: {', '.join(VALID_BODY_MASQUERADE)}",
            )

    # Validate healthcheck if present
    if "healthcheck" in payload:
        value = payload.get("healthcheck")
        if value and value not in VALID_BODY_HEALTHCHECK:
            return (
                False,
                f"Invalid healthcheck '{value}'. Must be one of: {', '.join(VALID_BODY_HEALTHCHECK)}",
            )

    # Validate monitor if present
    if "monitor" in payload:
        value = payload.get("monitor")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "monitor cannot exceed 255 characters")

    # Validate server-down-option if present
    if "server-down-option" in payload:
        value = payload.get("server-down-option")
        if value and value not in VALID_BODY_SERVER_DOWN_OPTION:
            return (
                False,
                f"Invalid server-down-option '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_DOWN_OPTION)}",
            )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_forward_server_delete(
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
