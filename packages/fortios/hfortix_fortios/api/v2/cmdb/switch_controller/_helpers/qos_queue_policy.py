"""
Validation helpers for switch-controller qos_queue_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SCHEDULE = ["strict", "round-robin", "weighted"]
VALID_BODY_RATE_BY = ["kbps", "percent"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_qos_queue_policy_get(
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


def validate_qos_queue_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating qos_queue_policy.

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

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and value not in VALID_BODY_SCHEDULE:
            return (
                False,
                f"Invalid schedule '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE)}",
            )

    # Validate rate-by if present
    if "rate-by" in payload:
        value = payload.get("rate-by")
        if value and value not in VALID_BODY_RATE_BY:
            return (
                False,
                f"Invalid rate-by '{value}'. Must be one of: {', '.join(VALID_BODY_RATE_BY)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_qos_queue_policy_put(
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

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and value not in VALID_BODY_SCHEDULE:
            return (
                False,
                f"Invalid schedule '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE)}",
            )

    # Validate rate-by if present
    if "rate-by" in payload:
        value = payload.get("rate-by")
        if value and value not in VALID_BODY_RATE_BY:
            return (
                False,
                f"Invalid rate-by '{value}'. Must be one of: {', '.join(VALID_BODY_RATE_BY)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_qos_queue_policy_delete(
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
