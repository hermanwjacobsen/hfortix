"""
Validation helpers for user fsso endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = ["default", "fortinac"]
VALID_BODY_LDAP_POLL = ["enable", "disable"]
VALID_BODY_SSL = ["enable", "disable"]
VALID_BODY_SSL_SERVER_HOST_IP_CHECK = ["enable", "disable"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fsso_get(
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


def validate_fsso_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating fsso.

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

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate server2 if present
    if "server2" in payload:
        value = payload.get("server2")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server2 cannot exceed 63 characters")

    # Validate port2 if present
    if "port2" in payload:
        value = payload.get("port2")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port2 must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port2 must be numeric, got: {value}")

    # Validate server3 if present
    if "server3" in payload:
        value = payload.get("server3")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server3 cannot exceed 63 characters")

    # Validate port3 if present
    if "port3" in payload:
        value = payload.get("port3")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port3 must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port3 must be numeric, got: {value}")

    # Validate server4 if present
    if "server4" in payload:
        value = payload.get("server4")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server4 cannot exceed 63 characters")

    # Validate port4 if present
    if "port4" in payload:
        value = payload.get("port4")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port4 must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port4 must be numeric, got: {value}")

    # Validate server5 if present
    if "server5" in payload:
        value = payload.get("server5")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server5 cannot exceed 63 characters")

    # Validate port5 if present
    if "port5" in payload:
        value = payload.get("port5")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port5 must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port5 must be numeric, got: {value}")

    # Validate logon-timeout if present
    if "logon-timeout" in payload:
        value = payload.get("logon-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2880:
                    return (False, "logon-timeout must be between 1 and 2880")
            except (ValueError, TypeError):
                return (False, f"logon-timeout must be numeric, got: {value}")

    # Validate ldap-server if present
    if "ldap-server" in payload:
        value = payload.get("ldap-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ldap-server cannot exceed 35 characters")

    # Validate group-poll-interval if present
    if "group-poll-interval" in payload:
        value = payload.get("group-poll-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2880:
                    return (
                        False,
                        "group-poll-interval must be between 1 and 2880",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"group-poll-interval must be numeric, got: {value}",
                )

    # Validate ldap-poll if present
    if "ldap-poll" in payload:
        value = payload.get("ldap-poll")
        if value and value not in VALID_BODY_LDAP_POLL:
            return (
                False,
                f"Invalid ldap-poll '{value}'. Must be one of: {', '.join(VALID_BODY_LDAP_POLL)}",
            )

    # Validate ldap-poll-interval if present
    if "ldap-poll-interval" in payload:
        value = payload.get("ldap-poll-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2880:
                    return (
                        False,
                        "ldap-poll-interval must be between 1 and 2880",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ldap-poll-interval must be numeric, got: {value}",
                )

    # Validate ldap-poll-filter if present
    if "ldap-poll-filter" in payload:
        value = payload.get("ldap-poll-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "ldap-poll-filter cannot exceed 2047 characters")

    # Validate user-info-server if present
    if "user-info-server" in payload:
        value = payload.get("user-info-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "user-info-server cannot exceed 35 characters")

    # Validate ssl if present
    if "ssl" in payload:
        value = payload.get("ssl")
        if value and value not in VALID_BODY_SSL:
            return (
                False,
                f"Invalid ssl '{value}'. Must be one of: {', '.join(VALID_BODY_SSL)}",
            )

    # Validate sni if present
    if "sni" in payload:
        value = payload.get("sni")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "sni cannot exceed 255 characters")

    # Validate ssl-server-host-ip-check if present
    if "ssl-server-host-ip-check" in payload:
        value = payload.get("ssl-server-host-ip-check")
        if value and value not in VALID_BODY_SSL_SERVER_HOST_IP_CHECK:
            return (
                False,
                f"Invalid ssl-server-host-ip-check '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_HOST_IP_CHECK)}",
            )

    # Validate ssl-trusted-cert if present
    if "ssl-trusted-cert" in payload:
        value = payload.get("ssl-trusted-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ssl-trusted-cert cannot exceed 79 characters")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_fsso_put(
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

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate server2 if present
    if "server2" in payload:
        value = payload.get("server2")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server2 cannot exceed 63 characters")

    # Validate port2 if present
    if "port2" in payload:
        value = payload.get("port2")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port2 must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port2 must be numeric, got: {value}")

    # Validate server3 if present
    if "server3" in payload:
        value = payload.get("server3")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server3 cannot exceed 63 characters")

    # Validate port3 if present
    if "port3" in payload:
        value = payload.get("port3")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port3 must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port3 must be numeric, got: {value}")

    # Validate server4 if present
    if "server4" in payload:
        value = payload.get("server4")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server4 cannot exceed 63 characters")

    # Validate port4 if present
    if "port4" in payload:
        value = payload.get("port4")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port4 must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port4 must be numeric, got: {value}")

    # Validate server5 if present
    if "server5" in payload:
        value = payload.get("server5")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server5 cannot exceed 63 characters")

    # Validate port5 if present
    if "port5" in payload:
        value = payload.get("port5")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port5 must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port5 must be numeric, got: {value}")

    # Validate logon-timeout if present
    if "logon-timeout" in payload:
        value = payload.get("logon-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2880:
                    return (False, "logon-timeout must be between 1 and 2880")
            except (ValueError, TypeError):
                return (False, f"logon-timeout must be numeric, got: {value}")

    # Validate ldap-server if present
    if "ldap-server" in payload:
        value = payload.get("ldap-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ldap-server cannot exceed 35 characters")

    # Validate group-poll-interval if present
    if "group-poll-interval" in payload:
        value = payload.get("group-poll-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2880:
                    return (
                        False,
                        "group-poll-interval must be between 1 and 2880",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"group-poll-interval must be numeric, got: {value}",
                )

    # Validate ldap-poll if present
    if "ldap-poll" in payload:
        value = payload.get("ldap-poll")
        if value and value not in VALID_BODY_LDAP_POLL:
            return (
                False,
                f"Invalid ldap-poll '{value}'. Must be one of: {', '.join(VALID_BODY_LDAP_POLL)}",
            )

    # Validate ldap-poll-interval if present
    if "ldap-poll-interval" in payload:
        value = payload.get("ldap-poll-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2880:
                    return (
                        False,
                        "ldap-poll-interval must be between 1 and 2880",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ldap-poll-interval must be numeric, got: {value}",
                )

    # Validate ldap-poll-filter if present
    if "ldap-poll-filter" in payload:
        value = payload.get("ldap-poll-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "ldap-poll-filter cannot exceed 2047 characters")

    # Validate user-info-server if present
    if "user-info-server" in payload:
        value = payload.get("user-info-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "user-info-server cannot exceed 35 characters")

    # Validate ssl if present
    if "ssl" in payload:
        value = payload.get("ssl")
        if value and value not in VALID_BODY_SSL:
            return (
                False,
                f"Invalid ssl '{value}'. Must be one of: {', '.join(VALID_BODY_SSL)}",
            )

    # Validate sni if present
    if "sni" in payload:
        value = payload.get("sni")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "sni cannot exceed 255 characters")

    # Validate ssl-server-host-ip-check if present
    if "ssl-server-host-ip-check" in payload:
        value = payload.get("ssl-server-host-ip-check")
        if value and value not in VALID_BODY_SSL_SERVER_HOST_IP_CHECK:
            return (
                False,
                f"Invalid ssl-server-host-ip-check '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_HOST_IP_CHECK)}",
            )

    # Validate ssl-trusted-cert if present
    if "ssl-trusted-cert" in payload:
        value = payload.get("ssl-trusted-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ssl-trusted-cert cannot exceed 79 characters")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_fsso_delete(name: str | None = None) -> tuple[bool, str | None]:
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
