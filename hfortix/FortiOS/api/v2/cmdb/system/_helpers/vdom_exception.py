"""
Validation helpers for system vdom_exception endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_OBJECT = [
    "log.fortianalyzer.setting",
    "log.fortianalyzer.override-setting",
    "log.fortianalyzer2.setting",
    "log.fortianalyzer2.override-setting",
    "log.fortianalyzer3.setting",
    "log.fortianalyzer3.override-setting",
    "log.fortianalyzer-cloud.setting",
    "log.fortianalyzer-cloud.override-setting",
    "log.syslogd.setting",
    "log.syslogd.override-setting",
    "log.syslogd2.setting",
    "log.syslogd2.override-setting",
    "log.syslogd3.setting",
    "log.syslogd3.override-setting",
    "log.syslogd4.setting",
    "log.syslogd4.override-setting",
    "system.gre-tunnel",
    "system.central-management",
    "system.cs",
    "user.radius",
    "system.interface",
    "log.syslogd.setting",
    "log.syslogd.override-setting",
    "firewall.address",
]
VALID_BODY_SCOPE = ["all", "inclusive", "exclusive"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vdom_exception_get(
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


def validate_vdom_exception_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating vdom_exception.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4096:
                    return (False, "id must be between 1 and 4096")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate object if present
    if "object" in payload:
        value = payload.get("object")
        if value and value not in VALID_BODY_OBJECT:
            return (
                False,
                f"Invalid object '{value}'. Must be one of: {', '.join(VALID_BODY_OBJECT)}",
            )

    # Validate scope if present
    if "scope" in payload:
        value = payload.get("scope")
        if value and value not in VALID_BODY_SCOPE:
            return (
                False,
                f"Invalid scope '{value}'. Must be one of: {', '.join(VALID_BODY_SCOPE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vdom_exception_put(
    id: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        id: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # id is required for updates
    if not id:
        return (False, "id is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4096:
                    return (False, "id must be between 1 and 4096")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate object if present
    if "object" in payload:
        value = payload.get("object")
        if value and value not in VALID_BODY_OBJECT:
            return (
                False,
                f"Invalid object '{value}'. Must be one of: {', '.join(VALID_BODY_OBJECT)}",
            )

    # Validate scope if present
    if "scope" in payload:
        value = payload.get("scope")
        if value and value not in VALID_BODY_SCOPE:
            return (
                False,
                f"Invalid scope '{value}'. Must be one of: {', '.join(VALID_BODY_SCOPE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_vdom_exception_delete(
    id: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        id: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not id:
        return (False, "id is required for DELETE operation")

    return (True, None)
