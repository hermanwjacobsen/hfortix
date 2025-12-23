"""
Validation helpers for switch-controller ip_source_guard_log endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_LOG_VIOLATIONS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ip_source_guard_log_get(
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


def validate_ip_source_guard_log_put(
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

    # Validate log-violations if present
    if "log-violations" in payload:
        value = payload.get("log-violations")
        if value and value not in VALID_BODY_LOG_VIOLATIONS:
            return (
                False,
                f"Invalid log-violations '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_VIOLATIONS)}",
            )

    # Validate violation-timer if present
    if "violation-timer" in payload:
        value = payload.get("violation-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1500:
                    return (
                        False,
                        "violation-timer must be between 0 and 1500",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"violation-timer must be numeric, got: {value}",
                )

    return (True, None)
