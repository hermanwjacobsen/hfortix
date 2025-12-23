"""
Validation helpers for system speed_test_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_speed_test_setting_get(
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


def validate_speed_test_setting_put(
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

    # Validate latency-threshold if present
    if "latency-threshold" in payload:
        value = payload.get("latency-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2000:
                    return (
                        False,
                        "latency-threshold must be between 0 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"latency-threshold must be numeric, got: {value}",
                )

    # Validate multiple-tcp-stream if present
    if "multiple-tcp-stream" in payload:
        value = payload.get("multiple-tcp-stream")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 64:
                    return (
                        False,
                        "multiple-tcp-stream must be between 1 and 64",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"multiple-tcp-stream must be numeric, got: {value}",
                )

    return (True, None)
