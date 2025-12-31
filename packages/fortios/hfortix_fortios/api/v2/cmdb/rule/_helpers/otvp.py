"""
Validation helpers for rule otvp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_LOG = ["disable", "enable"]
VALID_BODY_LOG_PACKET = ["disable", "enable"]
VALID_BODY_ACTION = ["pass", "block"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_otvp_get(
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


def validate_otvp_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating otvp.

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

    # Validate group if present
    if "group" in payload:
        value = payload.get("group")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "group cannot exceed 63 characters")

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

    # Validate rev if present
    if "rev" in payload:
        value = payload.get("rev")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "rev must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"rev must be numeric, got: {value}")

    # Validate date if present
    if "date" in payload:
        value = payload.get("date")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "date must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"date must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_otvp_put(
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

    # Validate group if present
    if "group" in payload:
        value = payload.get("group")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "group cannot exceed 63 characters")

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

    # Validate rev if present
    if "rev" in payload:
        value = payload.get("rev")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "rev must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"rev must be numeric, got: {value}")

    # Validate date if present
    if "date" in payload:
        value = payload.get("date")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "date must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"date must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_otvp_delete(name: str | None = None) -> tuple[bool, str | None]:
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
