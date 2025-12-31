"""
Validation helpers for system link_monitor endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ADDR_MODE = ["ipv4", "ipv6"]
VALID_BODY_SERVER_CONFIG = ["default", "individual"]
VALID_BODY_SERVER_TYPE = ["static", "dynamic"]
VALID_BODY_PROTOCOL = [
    "ping",
    "tcp-echo",
    "udp-echo",
    "http",
    "https",
    "twamp",
]
VALID_BODY_SECURITY_MODE = ["none", "authentication"]
VALID_BODY_UPDATE_CASCADE_INTERFACE = ["enable", "disable"]
VALID_BODY_UPDATE_STATIC_ROUTE = ["enable", "disable"]
VALID_BODY_UPDATE_POLICY_ROUTE = ["enable", "disable"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_SERVICE_DETECTION = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_link_monitor_get(
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


def validate_link_monitor_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating link_monitor.

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

    # Validate addr-mode if present
    if "addr-mode" in payload:
        value = payload.get("addr-mode")
        if value and value not in VALID_BODY_ADDR_MODE:
            return (
                False,
                f"Invalid addr-mode '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_MODE)}",
            )

    # Validate srcintf if present
    if "srcint" in payload:
        value = payload.get("srcint")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "srcintf cannot exceed 15 characters")

    # Validate server-config if present
    if "server-config" in payload:
        value = payload.get("server-config")
        if value and value not in VALID_BODY_SERVER_CONFIG:
            return (
                False,
                f"Invalid server-config '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_CONFIG)}",
            )

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

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

    # Validate http-get if present
    if "http-get" in payload:
        value = payload.get("http-get")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "http-get cannot exceed 1024 characters")

    # Validate http-agent if present
    if "http-agent" in payload:
        value = payload.get("http-agent")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "http-agent cannot exceed 1024 characters")

    # Validate http-match if present
    if "http-match" in payload:
        value = payload.get("http-match")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "http-match cannot exceed 1024 characters")

    # Validate interval if present
    if "interval" in payload:
        value = payload.get("interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 20 or int_val > 3600000:
                    return (False, "interval must be between 20 and 3600000")
            except (ValueError, TypeError):
                return (False, f"interval must be numeric, got: {value}")

    # Validate probe-timeout if present
    if "probe-timeout" in payload:
        value = payload.get("probe-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 20 or int_val > 5000:
                    return (
                        False,
                        "probe-timeout must be between 20 and 5000",
                    )
            except (ValueError, TypeError):
                return (False, f"probe-timeout must be numeric, got: {value}")

    # Validate failtime if present
    if "failtime" in payload:
        value = payload.get("failtime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (False, "failtime must be between 1 and 3600")
            except (ValueError, TypeError):
                return (False, f"failtime must be numeric, got: {value}")

    # Validate recoverytime if present
    if "recoverytime" in payload:
        value = payload.get("recoverytime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (False, "recoverytime must be between 1 and 3600")
            except (ValueError, TypeError):
                return (False, f"recoverytime must be numeric, got: {value}")

    # Validate probe-count if present
    if "probe-count" in payload:
        value = payload.get("probe-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 30:
                    return (False, "probe-count must be between 5 and 30")
            except (ValueError, TypeError):
                return (False, f"probe-count must be numeric, got: {value}")

    # Validate security-mode if present
    if "security-mode" in payload:
        value = payload.get("security-mode")
        if value and value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid security-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
            )

    # Validate packet-size if present
    if "packet-size" in payload:
        value = payload.get("packet-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "packet-size must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"packet-size must be numeric, got: {value}")

    # Validate ha-priority if present
    if "ha-priority" in payload:
        value = payload.get("ha-priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 50:
                    return (False, "ha-priority must be between 1 and 50")
            except (ValueError, TypeError):
                return (False, f"ha-priority must be numeric, got: {value}")

    # Validate fail-weight if present
    if "fail-weight" in payload:
        value = payload.get("fail-weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "fail-weight must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"fail-weight must be numeric, got: {value}")

    # Validate update-cascade-interface if present
    if "update-cascade-interface" in payload:
        value = payload.get("update-cascade-interface")
        if value and value not in VALID_BODY_UPDATE_CASCADE_INTERFACE:
            return (
                False,
                f"Invalid update-cascade-interface '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_CASCADE_INTERFACE)}",
            )

    # Validate update-static-route if present
    if "update-static-route" in payload:
        value = payload.get("update-static-route")
        if value and value not in VALID_BODY_UPDATE_STATIC_ROUTE:
            return (
                False,
                f"Invalid update-static-route '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_STATIC_ROUTE)}",
            )

    # Validate update-policy-route if present
    if "update-policy-route" in payload:
        value = payload.get("update-policy-route")
        if value and value not in VALID_BODY_UPDATE_POLICY_ROUTE:
            return (
                False,
                f"Invalid update-policy-route '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_POLICY_ROUTE)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate class-id if present
    if "class-id" in payload:
        value = payload.get("class-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "class-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"class-id must be numeric, got: {value}")

    # Validate service-detection if present
    if "service-detection" in payload:
        value = payload.get("service-detection")
        if value and value not in VALID_BODY_SERVICE_DETECTION:
            return (
                False,
                f"Invalid service-detection '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_DETECTION)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_link_monitor_put(
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

    # Validate addr-mode if present
    if "addr-mode" in payload:
        value = payload.get("addr-mode")
        if value and value not in VALID_BODY_ADDR_MODE:
            return (
                False,
                f"Invalid addr-mode '{value}'. Must be one of: {', '.join(VALID_BODY_ADDR_MODE)}",
            )

    # Validate srcintf if present
    if "srcint" in payload:
        value = payload.get("srcint")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "srcintf cannot exceed 15 characters")

    # Validate server-config if present
    if "server-config" in payload:
        value = payload.get("server-config")
        if value and value not in VALID_BODY_SERVER_CONFIG:
            return (
                False,
                f"Invalid server-config '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_CONFIG)}",
            )

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

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

    # Validate http-get if present
    if "http-get" in payload:
        value = payload.get("http-get")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "http-get cannot exceed 1024 characters")

    # Validate http-agent if present
    if "http-agent" in payload:
        value = payload.get("http-agent")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "http-agent cannot exceed 1024 characters")

    # Validate http-match if present
    if "http-match" in payload:
        value = payload.get("http-match")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "http-match cannot exceed 1024 characters")

    # Validate interval if present
    if "interval" in payload:
        value = payload.get("interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 20 or int_val > 3600000:
                    return (False, "interval must be between 20 and 3600000")
            except (ValueError, TypeError):
                return (False, f"interval must be numeric, got: {value}")

    # Validate probe-timeout if present
    if "probe-timeout" in payload:
        value = payload.get("probe-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 20 or int_val > 5000:
                    return (
                        False,
                        "probe-timeout must be between 20 and 5000",
                    )
            except (ValueError, TypeError):
                return (False, f"probe-timeout must be numeric, got: {value}")

    # Validate failtime if present
    if "failtime" in payload:
        value = payload.get("failtime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (False, "failtime must be between 1 and 3600")
            except (ValueError, TypeError):
                return (False, f"failtime must be numeric, got: {value}")

    # Validate recoverytime if present
    if "recoverytime" in payload:
        value = payload.get("recoverytime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (False, "recoverytime must be between 1 and 3600")
            except (ValueError, TypeError):
                return (False, f"recoverytime must be numeric, got: {value}")

    # Validate probe-count if present
    if "probe-count" in payload:
        value = payload.get("probe-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 30:
                    return (False, "probe-count must be between 5 and 30")
            except (ValueError, TypeError):
                return (False, f"probe-count must be numeric, got: {value}")

    # Validate security-mode if present
    if "security-mode" in payload:
        value = payload.get("security-mode")
        if value and value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid security-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
            )

    # Validate packet-size if present
    if "packet-size" in payload:
        value = payload.get("packet-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "packet-size must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"packet-size must be numeric, got: {value}")

    # Validate ha-priority if present
    if "ha-priority" in payload:
        value = payload.get("ha-priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 50:
                    return (False, "ha-priority must be between 1 and 50")
            except (ValueError, TypeError):
                return (False, f"ha-priority must be numeric, got: {value}")

    # Validate fail-weight if present
    if "fail-weight" in payload:
        value = payload.get("fail-weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "fail-weight must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"fail-weight must be numeric, got: {value}")

    # Validate update-cascade-interface if present
    if "update-cascade-interface" in payload:
        value = payload.get("update-cascade-interface")
        if value and value not in VALID_BODY_UPDATE_CASCADE_INTERFACE:
            return (
                False,
                f"Invalid update-cascade-interface '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_CASCADE_INTERFACE)}",
            )

    # Validate update-static-route if present
    if "update-static-route" in payload:
        value = payload.get("update-static-route")
        if value and value not in VALID_BODY_UPDATE_STATIC_ROUTE:
            return (
                False,
                f"Invalid update-static-route '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_STATIC_ROUTE)}",
            )

    # Validate update-policy-route if present
    if "update-policy-route" in payload:
        value = payload.get("update-policy-route")
        if value and value not in VALID_BODY_UPDATE_POLICY_ROUTE:
            return (
                False,
                f"Invalid update-policy-route '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_POLICY_ROUTE)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate class-id if present
    if "class-id" in payload:
        value = payload.get("class-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "class-id must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"class-id must be numeric, got: {value}")

    # Validate service-detection if present
    if "service-detection" in payload:
        value = payload.get("service-detection")
        if value and value not in VALID_BODY_SERVICE_DETECTION:
            return (
                False,
                f"Invalid service-detection '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_DETECTION)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_link_monitor_delete(
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
