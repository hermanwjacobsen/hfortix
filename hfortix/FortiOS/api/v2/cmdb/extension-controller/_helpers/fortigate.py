"""
Validation helpers for extension-controller fortigate endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_AUTHORIZED = ["discovered", "disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortigate_get(
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


def validate_fortigate_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating fortigate.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "name cannot exceed 19 characters")

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "id cannot exceed 19 characters")

    # Validate authorized if present
    if "authorized" in payload:
        value = payload.get("authorized")
        if value and value not in VALID_BODY_AUTHORIZED:
            return (
                False,
                f"Invalid authorized '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZED)}",
            )

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "hostname cannot exceed 31 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "vdom must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"vdom must be numeric, got: {value}")

    # Validate device-id if present
    if "device-id" in payload:
        value = payload.get("device-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "device-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"device-id must be numeric, got: {value}")

    # Validate profile if present
    if "profile" in payload:
        value = payload.get("profile")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "profile cannot exceed 31 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_fortigate_put(
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
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "name cannot exceed 19 characters")

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "id cannot exceed 19 characters")

    # Validate authorized if present
    if "authorized" in payload:
        value = payload.get("authorized")
        if value and value not in VALID_BODY_AUTHORIZED:
            return (
                False,
                f"Invalid authorized '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHORIZED)}",
            )

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "hostname cannot exceed 31 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "vdom must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"vdom must be numeric, got: {value}")

    # Validate device-id if present
    if "device-id" in payload:
        value = payload.get("device-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "device-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"device-id must be numeric, got: {value}")

    # Validate profile if present
    if "profile" in payload:
        value = payload.get("profile")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "profile cannot exceed 31 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_fortigate_delete(
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
