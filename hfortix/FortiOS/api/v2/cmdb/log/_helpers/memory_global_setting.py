"""
Validation helpers for log memory_global_setting endpoint.

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


def validate_memory_global_setting_get(
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


def validate_memory_global_setting_put(
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

    # Validate max-size if present
    if "max-size" in payload:
        value = payload.get("max-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-size must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-size must be numeric, got: {value}")

    # Validate full-first-warning-threshold if present
    if "full-first-warning-threshold" in payload:
        value = payload.get("full-first-warning-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 98:
                    return (
                        False,
                        "full-first-warning-threshold must be between 1 and 98",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"full-first-warning-threshold must be numeric, got: {value}",
                )

    # Validate full-second-warning-threshold if present
    if "full-second-warning-threshold" in payload:
        value = payload.get("full-second-warning-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 99:
                    return (
                        False,
                        "full-second-warning-threshold must be between 2 and 99",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"full-second-warning-threshold must be numeric, got: {value}",
                )

    # Validate full-final-warning-threshold if present
    if "full-final-warning-threshold" in payload:
        value = payload.get("full-final-warning-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 100:
                    return (
                        False,
                        "full-final-warning-threshold must be between 3 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"full-final-warning-threshold must be numeric, got: {value}",
                )

    return (True, None)
