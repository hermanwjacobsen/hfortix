"""
Validation helpers for report layout endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_OPTIONS = [
    "include-table-of-content",
    "auto-numbering-heading",
    "view-chart-as-heading",
    "show-html-navbar-before-heading",
    "dummy-option",
]
VALID_BODY_FORMAT = ["pd"]
VALID_BODY_SCHEDULE_TYPE = ["demand", "daily", "weekly"]
VALID_BODY_DAY = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
VALID_BODY_CUTOFF_OPTION = ["run-time", "custom"]
VALID_BODY_EMAIL_SEND = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_layout_get(
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


def validate_layout_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating layout.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate title if present
    if "title" in payload:
        value = payload.get("title")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "title cannot exceed 127 characters")

    # Validate subtitle if present
    if "subtitle" in payload:
        value = payload.get("subtitle")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "subtitle cannot exceed 127 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "description cannot exceed 127 characters")

    # Validate style-theme if present
    if "style-theme" in payload:
        value = payload.get("style-theme")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "style-theme cannot exceed 35 characters")

    # Validate options if present
    if "options" in payload:
        value = payload.get("options")
        if value and value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid options '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )

    # Validate format if present
    if "format" in payload:
        value = payload.get("format")
        if value and value not in VALID_BODY_FORMAT:
            return (
                False,
                f"Invalid format '{value}'. Must be one of: {', '.join(VALID_BODY_FORMAT)}",
            )

    # Validate schedule-type if present
    if "schedule-type" in payload:
        value = payload.get("schedule-type")
        if value and value not in VALID_BODY_SCHEDULE_TYPE:
            return (
                False,
                f"Invalid schedule-type '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_TYPE)}",
            )

    # Validate day if present
    if "day" in payload:
        value = payload.get("day")
        if value and value not in VALID_BODY_DAY:
            return (
                False,
                f"Invalid day '{value}'. Must be one of: {', '.join(VALID_BODY_DAY)}",
            )

    # Validate cutoff-option if present
    if "cutoff-option" in payload:
        value = payload.get("cutoff-option")
        if value and value not in VALID_BODY_CUTOFF_OPTION:
            return (
                False,
                f"Invalid cutoff-option '{value}'. Must be one of: {', '.join(VALID_BODY_CUTOFF_OPTION)}",
            )

    # Validate email-send if present
    if "email-send" in payload:
        value = payload.get("email-send")
        if value and value not in VALID_BODY_EMAIL_SEND:
            return (
                False,
                f"Invalid email-send '{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL_SEND)}",
            )

    # Validate email-recipients if present
    if "email-recipients" in payload:
        value = payload.get("email-recipients")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "email-recipients cannot exceed 511 characters")

    # Validate max-pdf-report if present
    if "max-pdf-report" in payload:
        value = payload.get("max-pdf-report")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 365:
                    return (False, "max-pdf-report must be between 1 and 365")
            except (ValueError, TypeError):
                return (False, f"max-pdf-report must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_layout_put(
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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate title if present
    if "title" in payload:
        value = payload.get("title")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "title cannot exceed 127 characters")

    # Validate subtitle if present
    if "subtitle" in payload:
        value = payload.get("subtitle")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "subtitle cannot exceed 127 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "description cannot exceed 127 characters")

    # Validate style-theme if present
    if "style-theme" in payload:
        value = payload.get("style-theme")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "style-theme cannot exceed 35 characters")

    # Validate options if present
    if "options" in payload:
        value = payload.get("options")
        if value and value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid options '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )

    # Validate format if present
    if "format" in payload:
        value = payload.get("format")
        if value and value not in VALID_BODY_FORMAT:
            return (
                False,
                f"Invalid format '{value}'. Must be one of: {', '.join(VALID_BODY_FORMAT)}",
            )

    # Validate schedule-type if present
    if "schedule-type" in payload:
        value = payload.get("schedule-type")
        if value and value not in VALID_BODY_SCHEDULE_TYPE:
            return (
                False,
                f"Invalid schedule-type '{value}'. Must be one of: {', '.join(VALID_BODY_SCHEDULE_TYPE)}",
            )

    # Validate day if present
    if "day" in payload:
        value = payload.get("day")
        if value and value not in VALID_BODY_DAY:
            return (
                False,
                f"Invalid day '{value}'. Must be one of: {', '.join(VALID_BODY_DAY)}",
            )

    # Validate cutoff-option if present
    if "cutoff-option" in payload:
        value = payload.get("cutoff-option")
        if value and value not in VALID_BODY_CUTOFF_OPTION:
            return (
                False,
                f"Invalid cutoff-option '{value}'. Must be one of: {', '.join(VALID_BODY_CUTOFF_OPTION)}",
            )

    # Validate email-send if present
    if "email-send" in payload:
        value = payload.get("email-send")
        if value and value not in VALID_BODY_EMAIL_SEND:
            return (
                False,
                f"Invalid email-send '{value}'. Must be one of: {', '.join(VALID_BODY_EMAIL_SEND)}",
            )

    # Validate email-recipients if present
    if "email-recipients" in payload:
        value = payload.get("email-recipients")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "email-recipients cannot exceed 511 characters")

    # Validate max-pdf-report if present
    if "max-pdf-report" in payload:
        value = payload.get("max-pdf-report")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 365:
                    return (False, "max-pdf-report must be between 1 and 365")
            except (ValueError, TypeError):
                return (False, f"max-pdf-report must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_layout_delete(name: str | None = None) -> tuple[bool, str | None]:
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
