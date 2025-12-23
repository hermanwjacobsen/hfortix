"""
Validation helpers for system object_tagging endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ADDRESS = ["disable", "mandatory", "optional"]
VALID_BODY_DEVICE = ["disable", "mandatory", "optional"]
VALID_BODY_INTERFACE = ["disable", "mandatory", "optional"]
VALID_BODY_MULTIPLE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_object_tagging_get(
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


def validate_object_tagging_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating object_tagging.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "category cannot exceed 63 characters")

    # Validate address if present
    if "address" in payload:
        value = payload.get("address")
        if value and value not in VALID_BODY_ADDRESS:
            return (
                False,
                f"Invalid address '{value}'. Must be one of: {', '.join(VALID_BODY_ADDRESS)}",
            )

    # Validate device if present
    if "device" in payload:
        value = payload.get("device")
        if value and value not in VALID_BODY_DEVICE:
            return (
                False,
                f"Invalid device '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and value not in VALID_BODY_INTERFACE:
            return (
                False,
                f"Invalid interface '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE)}",
            )

    # Validate multiple if present
    if "multiple" in payload:
        value = payload.get("multiple")
        if value and value not in VALID_BODY_MULTIPLE:
            return (
                False,
                f"Invalid multiple '{value}'. Must be one of: {', '.join(VALID_BODY_MULTIPLE)}",
            )

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    return (True, None)
