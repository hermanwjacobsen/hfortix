"""
Validation helpers for log fortiguard_override_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_OVERRIDE = ["enable", "disable"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_UPLOAD_OPTION = [
    "store-and-upload",
    "realtime",
    "1-minute",
    "5-minute",
]
VALID_BODY_UPLOAD_INTERVAL = ["daily", "weekly", "monthly"]
VALID_BODY_PRIORITY = ["default", "low"]
VALID_BODY_ACCESS_CONFIG = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortiguard_override_setting_get(
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


def validate_fortiguard_override_setting_put(
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

    # Validate override if present
    if "override" in payload:
        value = payload.get("override")
        if value and value not in VALID_BODY_OVERRIDE:
            return (
                False,
                f"Invalid override '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate upload-option if present
    if "upload-option" in payload:
        value = payload.get("upload-option")
        if value and value not in VALID_BODY_UPLOAD_OPTION:
            return (
                False,
                f"Invalid upload-option '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_OPTION)}",
            )

    # Validate upload-interval if present
    if "upload-interval" in payload:
        value = payload.get("upload-interval")
        if value and value not in VALID_BODY_UPLOAD_INTERVAL:
            return (
                False,
                f"Invalid upload-interval '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_INTERVAL)}",
            )

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value and value not in VALID_BODY_PRIORITY:
            return (
                False,
                f"Invalid priority '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY)}",
            )

    # Validate max-log-rate if present
    if "max-log-rate" in payload:
        value = payload.get("max-log-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100000:
                    return (
                        False,
                        "max-log-rate must be between 0 and 100000",
                    )
            except (ValueError, TypeError):
                return (False, f"max-log-rate must be numeric, got: {value}")

    # Validate access-config if present
    if "access-config" in payload:
        value = payload.get("access-config")
        if value and value not in VALID_BODY_ACCESS_CONFIG:
            return (
                False,
                f"Invalid access-config '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_CONFIG)}",
            )

    return (True, None)
