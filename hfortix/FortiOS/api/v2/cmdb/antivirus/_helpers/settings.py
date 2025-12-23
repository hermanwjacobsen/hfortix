"""
Validation helpers for antivirus settings endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MACHINE_LEARNING_DETECTION = ["enable", "monitor", "disable"]
VALID_BODY_USE_EXTREME_DB = ["enable", "disable"]
VALID_BODY_GRAYWARE = ["enable", "disable"]
VALID_BODY_CACHE_INFECTED_RESULT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_settings_get(
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


def validate_settings_put(
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

    # Validate machine-learning-detection if present
    if "machine-learning-detection" in payload:
        value = payload.get("machine-learning-detection")
        if value and value not in VALID_BODY_MACHINE_LEARNING_DETECTION:
            return (
                False,
                f"Invalid machine-learning-detection '{value}'. Must be one of: {', '.join(VALID_BODY_MACHINE_LEARNING_DETECTION)}",
            )

    # Validate use-extreme-db if present
    if "use-extreme-db" in payload:
        value = payload.get("use-extreme-db")
        if value and value not in VALID_BODY_USE_EXTREME_DB:
            return (
                False,
                f"Invalid use-extreme-db '{value}'. Must be one of: {', '.join(VALID_BODY_USE_EXTREME_DB)}",
            )

    # Validate grayware if present
    if "grayware" in payload:
        value = payload.get("grayware")
        if value and value not in VALID_BODY_GRAYWARE:
            return (
                False,
                f"Invalid grayware '{value}'. Must be one of: {', '.join(VALID_BODY_GRAYWARE)}",
            )

    # Validate override-timeout if present
    if "override-timeout" in payload:
        value = payload.get("override-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 3600:
                    return (
                        False,
                        "override-timeout must be between 30 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"override-timeout must be numeric, got: {value}",
                )

    # Validate cache-infected-result if present
    if "cache-infected-result" in payload:
        value = payload.get("cache-infected-result")
        if value and value not in VALID_BODY_CACHE_INFECTED_RESULT:
            return (
                False,
                f"Invalid cache-infected-result '{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_INFECTED_RESULT)}",
            )

    return (True, None)
