"""
Validation helpers for firewall internet_service_append endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ADDR_MODE = ["ipv4", "ipv6", "both"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_internet_service_append_get(
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


def validate_internet_service_append_put(
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

    # Validate addr-mode if present
    if "addr-mode" in payload:
        value = payload.get("addr-mode")
        if value and value not in VALID_BODY_ADDR_MODE:
            return (
                False,
                f"Invalid addr-mode '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_MODE)}",
            )

    # Validate match-port if present
    if "match-port" in payload:
        value = payload.get("match-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "match-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"match-port must be numeric, got: {value}")

    # Validate append-port if present
    if "append-port" in payload:
        value = payload.get("append-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "append-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"append-port must be numeric, got: {value}")

    return (True, None)
