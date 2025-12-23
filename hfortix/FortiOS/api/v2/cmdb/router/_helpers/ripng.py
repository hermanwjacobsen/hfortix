"""
Validation helpers for router ripng endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_DEFAULT_INFORMATION_ORIGINATE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ripng_get(
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


def validate_ripng_put(
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

    # Validate default-information-originate if present
    if "default-information-originate" in payload:
        value = payload.get("default-information-originate")
        if value and value not in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE:
            return (
                False,
                f"Invalid default-information-originate '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_INFORMATION_ORIGINATE)}",
            )

    # Validate default-metric if present
    if "default-metric" in payload:
        value = payload.get("default-metric")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16:
                    return (False, "default-metric must be between 1 and 16")
            except (ValueError, TypeError):
                return (False, f"default-metric must be numeric, got: {value}")

    # Validate max-out-metric if present
    if "max-out-metric" in payload:
        value = payload.get("max-out-metric")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 15:
                    return (False, "max-out-metric must be between 0 and 15")
            except (ValueError, TypeError):
                return (False, f"max-out-metric must be numeric, got: {value}")

    # Validate update-timer if present
    if "update-timer" in payload:
        value = payload.get("update-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 2147483647:
                    return (
                        False,
                        "update-timer must be between 5 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"update-timer must be numeric, got: {value}")

    # Validate timeout-timer if present
    if "timeout-timer" in payload:
        value = payload.get("timeout-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 2147483647:
                    return (
                        False,
                        "timeout-timer must be between 5 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"timeout-timer must be numeric, got: {value}")

    # Validate garbage-timer if present
    if "garbage-timer" in payload:
        value = payload.get("garbage-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 2147483647:
                    return (
                        False,
                        "garbage-timer must be between 5 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"garbage-timer must be numeric, got: {value}")

    return (True, None)
