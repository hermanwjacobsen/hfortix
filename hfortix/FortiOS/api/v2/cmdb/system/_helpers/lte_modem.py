"""
Validation helpers for system lte_modem endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_PDPTYPE = ["IPv4"]
VALID_BODY_AUTHTYPE = ["none", "pap", "chap"]
VALID_BODY_MODE = ["standalone", "redundant"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_lte_modem_get(
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


def validate_lte_modem_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate extra-init if present
    if "extra-init" in payload:
        value = payload.get("extra-init")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "extra-init cannot exceed 127 characters")

    # Validate pdptype if present
    if "pdptype" in payload:
        value = payload.get("pdptype")
        if value and value not in VALID_BODY_PDPTYPE:
            return (
                False,
                f"Invalid pdptype '{value}'. Must be one of: {', '.join(VALID_BODY_PDPTYPE)}",
            )

    # Validate authtype if present
    if "authtype" in payload:
        value = payload.get("authtype")
        if value and value not in VALID_BODY_AUTHTYPE:
            return (
                False,
                f"Invalid authtype '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHTYPE)}",
            )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "username cannot exceed 63 characters")

    # Validate apn if present
    if "apn" in payload:
        value = payload.get("apn")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "apn cannot exceed 127 characters")

    # Validate modem-port if present
    if "modem-port" in payload:
        value = payload.get("modem-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 20:
                    return (False, "modem-port must be between 0 and 20")
            except (ValueError, TypeError):
                return (False, f"modem-port must be numeric, got: {value}")

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate holddown-timer if present
    if "holddown-timer" in payload:
        value = payload.get("holddown-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 60:
                    return (False, "holddown-timer must be between 10 and 60")
            except (ValueError, TypeError):
                return (False, f"holddown-timer must be numeric, got: {value}")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "interface cannot exceed 63 characters")

    return (True, None)
