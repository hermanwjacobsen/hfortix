"""
Validation helpers for system ptp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_MODE = ["multicast", "hybrid"]
VALID_BODY_DELAY_MECHANISM = ["E2E", "P2P"]
VALID_BODY_SERVER_MODE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ptp_get(
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


def validate_ptp_put(
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

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate delay-mechanism if present
    if "delay-mechanism" in payload:
        value = payload.get("delay-mechanism")
        if value and value not in VALID_BODY_DELAY_MECHANISM:
            return (
                False,
                f"Invalid delay-mechanism '{value}'. Must be one of: {', '.join(VALID_BODY_DELAY_MECHANISM)}",
            )

    # Validate request-interval if present
    if "request-interval" in payload:
        value = payload.get("request-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 6:
                    return (False, "request-interval must be between 1 and 6")
            except (ValueError, TypeError):
                return (
                    False,
                    f"request-interval must be numeric, got: {value}",
                )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate server-mode if present
    if "server-mode" in payload:
        value = payload.get("server-mode")
        if value and value not in VALID_BODY_SERVER_MODE:
            return (
                False,
                f"Invalid server-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_MODE)}",
            )

    return (True, None)
