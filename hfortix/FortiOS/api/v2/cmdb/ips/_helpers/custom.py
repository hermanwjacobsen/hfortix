"""
Validation helpers for ips custom endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["disable", "enable"]
VALID_BODY_LOG = ["disable", "enable"]
VALID_BODY_LOG_PACKET = ["disable", "enable"]
VALID_BODY_ACTION = ["pass", "block"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_custom_get(
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


def validate_custom_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating custom.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate tag if present
    if "tag" in payload:
        value = payload.get("tag")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "tag cannot exceed 63 characters")

    # Validate signature if present
    if "signature" in payload:
        value = payload.get("signature")
        if value and isinstance(value, str) and len(value) > 4095:
            return (False, "signature cannot exceed 4095 characters")

    # Validate rule-id if present
    if "rule-id" in payload:
        value = payload.get("rule-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "rule-id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"rule-id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate log if present
    if "log" in payload:
        value = payload.get("log")
        if value and value not in VALID_BODY_LOG:
            return (
                False,
                f"Invalid log '{value}'. Must be one of: {', '.join(VALID_BODY_LOG)}",
            )

    # Validate log-packet if present
    if "log-packet" in payload:
        value = payload.get("log-packet")
        if value and value not in VALID_BODY_LOG_PACKET:
            return (
                False,
                f"Invalid log-packet '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_PACKET)}",
            )

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    return (True, None)
