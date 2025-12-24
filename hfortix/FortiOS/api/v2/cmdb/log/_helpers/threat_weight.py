"""
Validation helpers for log threat_weight endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_BLOCKED_CONNECTION = [
    "disable",
    "low",
    "medium",
    "high",
    "critical",
]
VALID_BODY_FAILED_CONNECTION = ["disable", "low", "medium", "high", "critical"]
VALID_BODY_URL_BLOCK_DETECTED = [
    "disable",
    "low",
    "medium",
    "high",
    "critical",
]
VALID_BODY_BOTNET_CONNECTION_DETECTED = [
    "disable",
    "low",
    "medium",
    "high",
    "critical",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_threat_weight_get(
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


def validate_threat_weight_put(
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

    # Validate blocked-connection if present
    if "blocked-connection" in payload:
        value = payload.get("blocked-connection")
        if value and value not in VALID_BODY_BLOCKED_CONNECTION:
            return (
                False,
                f"Invalid blocked-connection '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCKED_CONNECTION)}",
            )

    # Validate failed-connection if present
    if "failed-connection" in payload:
        value = payload.get("failed-connection")
        if value and value not in VALID_BODY_FAILED_CONNECTION:
            return (
                False,
                f"Invalid failed-connection '{value}'. Must be one of: {', '.join(VALID_BODY_FAILED_CONNECTION)}",
            )

    # Validate url-block-detected if present
    if "url-block-detected" in payload:
        value = payload.get("url-block-detected")
        if value and value not in VALID_BODY_URL_BLOCK_DETECTED:
            return (
                False,
                f"Invalid url-block-detected '{value}'. Must be one of: {', '.join(VALID_BODY_URL_BLOCK_DETECTED)}",
            )

    # Validate botnet-connection-detected if present
    if "botnet-connection-detected" in payload:
        value = payload.get("botnet-connection-detected")
        if value and value not in VALID_BODY_BOTNET_CONNECTION_DETECTED:
            return (
                False,
                f"Invalid botnet-connection-detected '{value}'. Must be one of: {', '.join(VALID_BODY_BOTNET_CONNECTION_DETECTED)}",
            )

    return (True, None)
