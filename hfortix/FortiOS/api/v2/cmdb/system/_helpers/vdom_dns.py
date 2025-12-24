"""
Validation helpers for system vdom_dns endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_VDOM_DNS = ["enable", "disable"]
VALID_BODY_PROTOCOL = ["cleartext", "dot", "doh"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_SERVER_SELECT_METHOD = ["least-rtt", "failover"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vdom_dns_get(
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
# PUT Validation
# ============================================================================


def validate_vdom_dns_put(
    payload: dict[str, Any] | None = None,
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate vdom-dns if present
    if "vdom-dns" in payload:
        value = payload.get("vdom-dns")
        if value and value not in VALID_BODY_VDOM_DNS:
            return (
                False,
                f"Invalid vdom-dns '{value}'. Must be one of: {', '.join(VALID_BODY_VDOM_DNS)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate ssl-certificate if present
    if "ssl-certificate" in payload:
        value = payload.get("ssl-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssl-certificate cannot exceed 35 characters")

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

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

    # Validate server-select-method if present
    if "server-select-method" in payload:
        value = payload.get("server-select-method")
        if value and value not in VALID_BODY_SERVER_SELECT_METHOD:
            return (
                False,
                f"Invalid server-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_SELECT_METHOD)}",
            )

    return (True, None)
