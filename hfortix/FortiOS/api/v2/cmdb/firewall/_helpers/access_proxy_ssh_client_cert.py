"""
Validation helpers for firewall access_proxy_ssh_client_cert endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SOURCE_ADDRESS = ["enable", "disable"]
VALID_BODY_PERMIT_X11_FORWARDING = ["enable", "disable"]
VALID_BODY_PERMIT_AGENT_FORWARDING = ["enable", "disable"]
VALID_BODY_PERMIT_PORT_FORWARDING = ["enable", "disable"]
VALID_BODY_PERMIT_PTY = ["enable", "disable"]
VALID_BODY_PERMIT_USER_RC = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_access_proxy_ssh_client_cert_get(
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


def validate_access_proxy_ssh_client_cert_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating access_proxy_ssh_client_cert.

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

    # Validate source-address if present
    if "source-address" in payload:
        value = payload.get("source-address")
        if value and value not in VALID_BODY_SOURCE_ADDRESS:
            return (
                False,
                f"Invalid source-address '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE_ADDRESS)}",
            )

    # Validate permit-x11-forwarding if present
    if "permit-x11-forwarding" in payload:
        value = payload.get("permit-x11-forwarding")
        if value and value not in VALID_BODY_PERMIT_X11_FORWARDING:
            return (
                False,
                f"Invalid permit-x11-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_X11_FORWARDING)}",
            )

    # Validate permit-agent-forwarding if present
    if "permit-agent-forwarding" in payload:
        value = payload.get("permit-agent-forwarding")
        if value and value not in VALID_BODY_PERMIT_AGENT_FORWARDING:
            return (
                False,
                f"Invalid permit-agent-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_AGENT_FORWARDING)}",
            )

    # Validate permit-port-forwarding if present
    if "permit-port-forwarding" in payload:
        value = payload.get("permit-port-forwarding")
        if value and value not in VALID_BODY_PERMIT_PORT_FORWARDING:
            return (
                False,
                f"Invalid permit-port-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PORT_FORWARDING)}",
            )

    # Validate permit-pty if present
    if "permit-pty" in payload:
        value = payload.get("permit-pty")
        if value and value not in VALID_BODY_PERMIT_PTY:
            return (
                False,
                f"Invalid permit-pty '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PTY)}",
            )

    # Validate permit-user-rc if present
    if "permit-user-rc" in payload:
        value = payload.get("permit-user-rc")
        if value and value not in VALID_BODY_PERMIT_USER_RC:
            return (
                False,
                f"Invalid permit-user-rc '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_USER_RC)}",
            )

    # Validate auth-ca if present
    if "auth-ca" in payload:
        value = payload.get("auth-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "auth-ca cannot exceed 79 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_access_proxy_ssh_client_cert_put(
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

    # Validate source-address if present
    if "source-address" in payload:
        value = payload.get("source-address")
        if value and value not in VALID_BODY_SOURCE_ADDRESS:
            return (
                False,
                f"Invalid source-address '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE_ADDRESS)}",
            )

    # Validate permit-x11-forwarding if present
    if "permit-x11-forwarding" in payload:
        value = payload.get("permit-x11-forwarding")
        if value and value not in VALID_BODY_PERMIT_X11_FORWARDING:
            return (
                False,
                f"Invalid permit-x11-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_X11_FORWARDING)}",
            )

    # Validate permit-agent-forwarding if present
    if "permit-agent-forwarding" in payload:
        value = payload.get("permit-agent-forwarding")
        if value and value not in VALID_BODY_PERMIT_AGENT_FORWARDING:
            return (
                False,
                f"Invalid permit-agent-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_AGENT_FORWARDING)}",
            )

    # Validate permit-port-forwarding if present
    if "permit-port-forwarding" in payload:
        value = payload.get("permit-port-forwarding")
        if value and value not in VALID_BODY_PERMIT_PORT_FORWARDING:
            return (
                False,
                f"Invalid permit-port-forwarding '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PORT_FORWARDING)}",
            )

    # Validate permit-pty if present
    if "permit-pty" in payload:
        value = payload.get("permit-pty")
        if value and value not in VALID_BODY_PERMIT_PTY:
            return (
                False,
                f"Invalid permit-pty '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_PTY)}",
            )

    # Validate permit-user-rc if present
    if "permit-user-rc" in payload:
        value = payload.get("permit-user-rc")
        if value and value not in VALID_BODY_PERMIT_USER_RC:
            return (
                False,
                f"Invalid permit-user-rc '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_USER_RC)}",
            )

    # Validate auth-ca if present
    if "auth-ca" in payload:
        value = payload.get("auth-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "auth-ca cannot exceed 79 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_access_proxy_ssh_client_cert_delete(
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
