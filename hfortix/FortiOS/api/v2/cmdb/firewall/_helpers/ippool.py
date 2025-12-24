"""
Validation helpers for firewall ippool endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "overload",
    "one-to-one",
    "fixed-port-range",
    "port-block-allocation",
]
VALID_BODY_PERMIT_ANY_HOST = ["disable", "enable"]
VALID_BODY_ARP_REPLY = ["disable", "enable"]
VALID_BODY_NAT64 = ["disable", "enable"]
VALID_BODY_ADD_NAT64_ROUTE = ["disable", "enable"]
VALID_BODY_PRIVILEGED_PORT_USE_PBA = ["disable", "enable"]
VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL = ["disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ippool_get(
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


def validate_ippool_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ippool.

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

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate startport if present
    if "startport" in payload:
        value = payload.get("startport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1024 or int_val > 65535:
                    return (False, "startport must be between 1024 and 65535")
            except (ValueError, TypeError):
                return (False, f"startport must be numeric, got: {value}")

    # Validate endport if present
    if "endport" in payload:
        value = payload.get("endport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1024 or int_val > 65535:
                    return (False, "endport must be between 1024 and 65535")
            except (ValueError, TypeError):
                return (False, f"endport must be numeric, got: {value}")

    # Validate block-size if present
    if "block-size" in payload:
        value = payload.get("block-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 64 or int_val > 4096:
                    return (False, "block-size must be between 64 and 4096")
            except (ValueError, TypeError):
                return (False, f"block-size must be numeric, got: {value}")

    # Validate port-per-user if present
    if "port-per-user" in payload:
        value = payload.get("port-per-user")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 32 or int_val > 60417:
                    return (
                        False,
                        "port-per-user must be between 32 and 60417",
                    )
            except (ValueError, TypeError):
                return (False, f"port-per-user must be numeric, got: {value}")

    # Validate num-blocks-per-user if present
    if "num-blocks-per-user" in payload:
        value = payload.get("num-blocks-per-user")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 128:
                    return (
                        False,
                        "num-blocks-per-user must be between 1 and 128",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"num-blocks-per-user must be numeric, got: {value}",
                )

    # Validate pba-timeout if present
    if "pba-timeout" in payload:
        value = payload.get("pba-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 86400:
                    return (False, "pba-timeout must be between 3 and 86400")
            except (ValueError, TypeError):
                return (False, f"pba-timeout must be numeric, got: {value}")

    # Validate pba-interim-log if present
    if "pba-interim-log" in payload:
        value = payload.get("pba-interim-log")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 600 or int_val > 86400:
                    return (
                        False,
                        "pba-interim-log must be between 600 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pba-interim-log must be numeric, got: {value}",
                )

    # Validate permit-any-host if present
    if "permit-any-host" in payload:
        value = payload.get("permit-any-host")
        if value and value not in VALID_BODY_PERMIT_ANY_HOST:
            return (
                False,
                f"Invalid permit-any-host '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_ANY_HOST)}",
            )

    # Validate arp-reply if present
    if "arp-reply" in payload:
        value = payload.get("arp-reply")
        if value and value not in VALID_BODY_ARP_REPLY:
            return (
                False,
                f"Invalid arp-reply '{value}'. Must be one of: {', '.join(VALID_BODY_ARP_REPLY)}",
            )

    # Validate arp-intf if present
    if "arp-int" in payload:
        value = payload.get("arp-int")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "arp-intf cannot exceed 15 characters")

    # Validate associated-interface if present
    if "associated-interface" in payload:
        value = payload.get("associated-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "associated-interface cannot exceed 15 characters")

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate nat64 if present
    if "nat64" in payload:
        value = payload.get("nat64")
        if value and value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid nat64 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )

    # Validate add-nat64-route if present
    if "add-nat64-route" in payload:
        value = payload.get("add-nat64-route")
        if value and value not in VALID_BODY_ADD_NAT64_ROUTE:
            return (
                False,
                f"Invalid add-nat64-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT64_ROUTE)}",
            )

    # Validate client-prefix-length if present
    if "client-prefix-length" in payload:
        value = payload.get("client-prefix-length")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 128:
                    return (
                        False,
                        "client-prefix-length must be between 1 and 128",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-prefix-length must be numeric, got: {value}",
                )

    # Validate tcp-session-quota if present
    if "tcp-session-quota" in payload:
        value = payload.get("tcp-session-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "tcp-session-quota must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-session-quota must be numeric, got: {value}",
                )

    # Validate udp-session-quota if present
    if "udp-session-quota" in payload:
        value = payload.get("udp-session-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "udp-session-quota must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"udp-session-quota must be numeric, got: {value}",
                )

    # Validate icmp-session-quota if present
    if "icmp-session-quota" in payload:
        value = payload.get("icmp-session-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "icmp-session-quota must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"icmp-session-quota must be numeric, got: {value}",
                )

    # Validate privileged-port-use-pba if present
    if "privileged-port-use-pba" in payload:
        value = payload.get("privileged-port-use-pba")
        if value and value not in VALID_BODY_PRIVILEGED_PORT_USE_PBA:
            return (
                False,
                f"Invalid privileged-port-use-pba '{value}'. Must be one of: {', '.join(VALID_BODY_PRIVILEGED_PORT_USE_PBA)}",
            )

    # Validate subnet-broadcast-in-ippool if present
    if "subnet-broadcast-in-ippool" in payload:
        value = payload.get("subnet-broadcast-in-ippool")
        if value and value not in VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL:
            return (
                False,
                f"Invalid subnet-broadcast-in-ippool '{value}'. Must be one of: {', '.join(VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ippool_put(
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

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate startport if present
    if "startport" in payload:
        value = payload.get("startport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1024 or int_val > 65535:
                    return (False, "startport must be between 1024 and 65535")
            except (ValueError, TypeError):
                return (False, f"startport must be numeric, got: {value}")

    # Validate endport if present
    if "endport" in payload:
        value = payload.get("endport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1024 or int_val > 65535:
                    return (False, "endport must be between 1024 and 65535")
            except (ValueError, TypeError):
                return (False, f"endport must be numeric, got: {value}")

    # Validate block-size if present
    if "block-size" in payload:
        value = payload.get("block-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 64 or int_val > 4096:
                    return (False, "block-size must be between 64 and 4096")
            except (ValueError, TypeError):
                return (False, f"block-size must be numeric, got: {value}")

    # Validate port-per-user if present
    if "port-per-user" in payload:
        value = payload.get("port-per-user")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 32 or int_val > 60417:
                    return (
                        False,
                        "port-per-user must be between 32 and 60417",
                    )
            except (ValueError, TypeError):
                return (False, f"port-per-user must be numeric, got: {value}")

    # Validate num-blocks-per-user if present
    if "num-blocks-per-user" in payload:
        value = payload.get("num-blocks-per-user")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 128:
                    return (
                        False,
                        "num-blocks-per-user must be between 1 and 128",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"num-blocks-per-user must be numeric, got: {value}",
                )

    # Validate pba-timeout if present
    if "pba-timeout" in payload:
        value = payload.get("pba-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 86400:
                    return (False, "pba-timeout must be between 3 and 86400")
            except (ValueError, TypeError):
                return (False, f"pba-timeout must be numeric, got: {value}")

    # Validate pba-interim-log if present
    if "pba-interim-log" in payload:
        value = payload.get("pba-interim-log")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 600 or int_val > 86400:
                    return (
                        False,
                        "pba-interim-log must be between 600 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pba-interim-log must be numeric, got: {value}",
                )

    # Validate permit-any-host if present
    if "permit-any-host" in payload:
        value = payload.get("permit-any-host")
        if value and value not in VALID_BODY_PERMIT_ANY_HOST:
            return (
                False,
                f"Invalid permit-any-host '{value}'. Must be one of: {', '.join(VALID_BODY_PERMIT_ANY_HOST)}",
            )

    # Validate arp-reply if present
    if "arp-reply" in payload:
        value = payload.get("arp-reply")
        if value and value not in VALID_BODY_ARP_REPLY:
            return (
                False,
                f"Invalid arp-reply '{value}'. Must be one of: {', '.join(VALID_BODY_ARP_REPLY)}",
            )

    # Validate arp-intf if present
    if "arp-int" in payload:
        value = payload.get("arp-int")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "arp-intf cannot exceed 15 characters")

    # Validate associated-interface if present
    if "associated-interface" in payload:
        value = payload.get("associated-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "associated-interface cannot exceed 15 characters")

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate nat64 if present
    if "nat64" in payload:
        value = payload.get("nat64")
        if value and value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid nat64 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )

    # Validate add-nat64-route if present
    if "add-nat64-route" in payload:
        value = payload.get("add-nat64-route")
        if value and value not in VALID_BODY_ADD_NAT64_ROUTE:
            return (
                False,
                f"Invalid add-nat64-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT64_ROUTE)}",
            )

    # Validate client-prefix-length if present
    if "client-prefix-length" in payload:
        value = payload.get("client-prefix-length")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 128:
                    return (
                        False,
                        "client-prefix-length must be between 1 and 128",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-prefix-length must be numeric, got: {value}",
                )

    # Validate tcp-session-quota if present
    if "tcp-session-quota" in payload:
        value = payload.get("tcp-session-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "tcp-session-quota must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-session-quota must be numeric, got: {value}",
                )

    # Validate udp-session-quota if present
    if "udp-session-quota" in payload:
        value = payload.get("udp-session-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "udp-session-quota must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"udp-session-quota must be numeric, got: {value}",
                )

    # Validate icmp-session-quota if present
    if "icmp-session-quota" in payload:
        value = payload.get("icmp-session-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "icmp-session-quota must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"icmp-session-quota must be numeric, got: {value}",
                )

    # Validate privileged-port-use-pba if present
    if "privileged-port-use-pba" in payload:
        value = payload.get("privileged-port-use-pba")
        if value and value not in VALID_BODY_PRIVILEGED_PORT_USE_PBA:
            return (
                False,
                f"Invalid privileged-port-use-pba '{value}'. Must be one of: {', '.join(VALID_BODY_PRIVILEGED_PORT_USE_PBA)}",
            )

    # Validate subnet-broadcast-in-ippool if present
    if "subnet-broadcast-in-ippool" in payload:
        value = payload.get("subnet-broadcast-in-ippool")
        if value and value not in VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL:
            return (
                False,
                f"Invalid subnet-broadcast-in-ippool '{value}'. Must be one of: {', '.join(VALID_BODY_SUBNET_BROADCAST_IN_IPPOOL)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ippool_delete(name: str | None = None) -> tuple[bool, str | None]:
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
