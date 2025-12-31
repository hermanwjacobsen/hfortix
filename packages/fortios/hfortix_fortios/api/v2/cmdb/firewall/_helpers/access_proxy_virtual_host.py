"""
Validation helpers for firewall access_proxy_virtual_host endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_HOST_TYPE = ["sub-string", "wildcard"]
VALID_BODY_EMPTY_CERT_ACTION = ["accept", "block", "accept-unmanageable"]
VALID_BODY_USER_AGENT_DETECT = ["disable", "enable"]
VALID_BODY_CLIENT_CERT = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_access_proxy_virtual_host_get(
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


def validate_access_proxy_virtual_host_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating access_proxy_virtual_host.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate host if present
    if "host" in payload:
        value = payload.get("host")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "host cannot exceed 79 characters")

    # Validate host-type if present
    if "host-type" in payload:
        value = payload.get("host-type")
        if value and value not in VALID_BODY_HOST_TYPE:
            return (
                False,
                f"Invalid host-type '{value}'. Must be one of: {', '.join(VALID_BODY_HOST_TYPE)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate empty-cert-action if present
    if "empty-cert-action" in payload:
        value = payload.get("empty-cert-action")
        if value and value not in VALID_BODY_EMPTY_CERT_ACTION:
            return (
                False,
                f"Invalid empty-cert-action '{value}'. Must be one of: {', '.join(VALID_BODY_EMPTY_CERT_ACTION)}",
            )

    # Validate user-agent-detect if present
    if "user-agent-detect" in payload:
        value = payload.get("user-agent-detect")
        if value and value not in VALID_BODY_USER_AGENT_DETECT:
            return (
                False,
                f"Invalid user-agent-detect '{value}'. Must be one of: {', '.join(VALID_BODY_USER_AGENT_DETECT)}",
            )

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and value not in VALID_BODY_CLIENT_CERT:
            return (
                False,
                f"Invalid client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_access_proxy_virtual_host_put(
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
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate host if present
    if "host" in payload:
        value = payload.get("host")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "host cannot exceed 79 characters")

    # Validate host-type if present
    if "host-type" in payload:
        value = payload.get("host-type")
        if value and value not in VALID_BODY_HOST_TYPE:
            return (
                False,
                f"Invalid host-type '{value}'. Must be one of: {', '.join(VALID_BODY_HOST_TYPE)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate empty-cert-action if present
    if "empty-cert-action" in payload:
        value = payload.get("empty-cert-action")
        if value and value not in VALID_BODY_EMPTY_CERT_ACTION:
            return (
                False,
                f"Invalid empty-cert-action '{value}'. Must be one of: {', '.join(VALID_BODY_EMPTY_CERT_ACTION)}",
            )

    # Validate user-agent-detect if present
    if "user-agent-detect" in payload:
        value = payload.get("user-agent-detect")
        if value and value not in VALID_BODY_USER_AGENT_DETECT:
            return (
                False,
                f"Invalid user-agent-detect '{value}'. Must be one of: {', '.join(VALID_BODY_USER_AGENT_DETECT)}",
            )

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and value not in VALID_BODY_CLIENT_CERT:
            return (
                False,
                f"Invalid client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_access_proxy_virtual_host_delete(
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
