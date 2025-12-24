"""
Validation helpers for switch-controller qos_dot1p_map endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_EGRESS_PRI_TAGGING = ["disable", "enable"]
VALID_BODY_PRIORITY_0 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_1 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_2 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_3 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_4 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_5 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_6 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_BODY_PRIORITY_7 = [
    "queue-0",
    "queue-1",
    "queue-2",
    "queue-3",
    "queue-4",
    "queue-5",
    "queue-6",
    "queue-7",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_qos_dot1p_map_get(
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


def validate_qos_dot1p_map_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating qos_dot1p_map.

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

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate egress-pri-tagging if present
    if "egress-pri-tagging" in payload:
        value = payload.get("egress-pri-tagging")
        if value and value not in VALID_BODY_EGRESS_PRI_TAGGING:
            return (
                False,
                f"Invalid egress-pri-tagging '{value}'. Must be one of: {', '.join(VALID_BODY_EGRESS_PRI_TAGGING)}",
            )

    # Validate priority-0 if present
    if "priority-0" in payload:
        value = payload.get("priority-0")
        if value and value not in VALID_BODY_PRIORITY_0:
            return (
                False,
                f"Invalid priority-0 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_0)}",
            )

    # Validate priority-1 if present
    if "priority-1" in payload:
        value = payload.get("priority-1")
        if value and value not in VALID_BODY_PRIORITY_1:
            return (
                False,
                f"Invalid priority-1 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_1)}",
            )

    # Validate priority-2 if present
    if "priority-2" in payload:
        value = payload.get("priority-2")
        if value and value not in VALID_BODY_PRIORITY_2:
            return (
                False,
                f"Invalid priority-2 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_2)}",
            )

    # Validate priority-3 if present
    if "priority-3" in payload:
        value = payload.get("priority-3")
        if value and value not in VALID_BODY_PRIORITY_3:
            return (
                False,
                f"Invalid priority-3 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_3)}",
            )

    # Validate priority-4 if present
    if "priority-4" in payload:
        value = payload.get("priority-4")
        if value and value not in VALID_BODY_PRIORITY_4:
            return (
                False,
                f"Invalid priority-4 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_4)}",
            )

    # Validate priority-5 if present
    if "priority-5" in payload:
        value = payload.get("priority-5")
        if value and value not in VALID_BODY_PRIORITY_5:
            return (
                False,
                f"Invalid priority-5 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_5)}",
            )

    # Validate priority-6 if present
    if "priority-6" in payload:
        value = payload.get("priority-6")
        if value and value not in VALID_BODY_PRIORITY_6:
            return (
                False,
                f"Invalid priority-6 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_6)}",
            )

    # Validate priority-7 if present
    if "priority-7" in payload:
        value = payload.get("priority-7")
        if value and value not in VALID_BODY_PRIORITY_7:
            return (
                False,
                f"Invalid priority-7 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_7)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_qos_dot1p_map_put(
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

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate egress-pri-tagging if present
    if "egress-pri-tagging" in payload:
        value = payload.get("egress-pri-tagging")
        if value and value not in VALID_BODY_EGRESS_PRI_TAGGING:
            return (
                False,
                f"Invalid egress-pri-tagging '{value}'. Must be one of: {', '.join(VALID_BODY_EGRESS_PRI_TAGGING)}",
            )

    # Validate priority-0 if present
    if "priority-0" in payload:
        value = payload.get("priority-0")
        if value and value not in VALID_BODY_PRIORITY_0:
            return (
                False,
                f"Invalid priority-0 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_0)}",
            )

    # Validate priority-1 if present
    if "priority-1" in payload:
        value = payload.get("priority-1")
        if value and value not in VALID_BODY_PRIORITY_1:
            return (
                False,
                f"Invalid priority-1 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_1)}",
            )

    # Validate priority-2 if present
    if "priority-2" in payload:
        value = payload.get("priority-2")
        if value and value not in VALID_BODY_PRIORITY_2:
            return (
                False,
                f"Invalid priority-2 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_2)}",
            )

    # Validate priority-3 if present
    if "priority-3" in payload:
        value = payload.get("priority-3")
        if value and value not in VALID_BODY_PRIORITY_3:
            return (
                False,
                f"Invalid priority-3 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_3)}",
            )

    # Validate priority-4 if present
    if "priority-4" in payload:
        value = payload.get("priority-4")
        if value and value not in VALID_BODY_PRIORITY_4:
            return (
                False,
                f"Invalid priority-4 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_4)}",
            )

    # Validate priority-5 if present
    if "priority-5" in payload:
        value = payload.get("priority-5")
        if value and value not in VALID_BODY_PRIORITY_5:
            return (
                False,
                f"Invalid priority-5 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_5)}",
            )

    # Validate priority-6 if present
    if "priority-6" in payload:
        value = payload.get("priority-6")
        if value and value not in VALID_BODY_PRIORITY_6:
            return (
                False,
                f"Invalid priority-6 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_6)}",
            )

    # Validate priority-7 if present
    if "priority-7" in payload:
        value = payload.get("priority-7")
        if value and value not in VALID_BODY_PRIORITY_7:
            return (
                False,
                f"Invalid priority-7 '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_7)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_qos_dot1p_map_delete(
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
