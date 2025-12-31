"""
Validation helpers for system snmp_community endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_QUERY_V1_STATUS = ["enable", "disable"]
VALID_BODY_QUERY_V2C_STATUS = ["enable", "disable"]
VALID_BODY_TRAP_V1_STATUS = ["enable", "disable"]
VALID_BODY_TRAP_V2C_STATUS = ["enable", "disable"]
VALID_BODY_EVENTS = [
    "cpu-high",
    "mem-low",
    "log-full",
    "intf-ip",
    "vpn-tun-up",
    "vpn-tun-down",
    "ha-switch",
    "ha-hb-failure",
    "ips-signature",
    "ips-anomaly",
    "av-virus",
    "av-oversize",
    "av-pattern",
    "av-fragmented",
    "fm-if-change",
    "fm-conf-change",
    "bgp-established",
    "bgp-backward-transition",
    "ha-member-up",
    "ha-member-down",
    "ent-conf-change",
    "av-conserve",
    "av-bypass",
    "av-oversize-passed",
    "av-oversize-blocked",
    "ips-pkg-update",
    "ips-fail-open",
    "temperature-high",
    "voltage-alert",
    "power-supply",
    "faz-disconnect",
    "faz",
    "wc-ap-up",
    "wc-ap-down",
    "fswctl-session-up",
    "fswctl-session-down",
    "load-balance-real-server-down",
    "device-new",
    "per-cpu-high",
    "dhcp",
    "pool-usage",
    "ippool",
    "interface",
    "ospf-nbr-state-change",
    "ospf-virtnbr-state-change",
    "bfd",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_snmp_community_get(
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


def validate_snmp_community_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating snmp_community.

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
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate query-v1-status if present
    if "query-v1-status" in payload:
        value = payload.get("query-v1-status")
        if value and value not in VALID_BODY_QUERY_V1_STATUS:
            return (
                False,
                f"Invalid query-v1-status '{value}'. Must be one of: {', '.join(VALID_BODY_QUERY_V1_STATUS)}",
            )

    # Validate query-v1-port if present
    if "query-v1-port" in payload:
        value = payload.get("query-v1-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "query-v1-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"query-v1-port must be numeric, got: {value}")

    # Validate query-v2c-status if present
    if "query-v2c-status" in payload:
        value = payload.get("query-v2c-status")
        if value and value not in VALID_BODY_QUERY_V2C_STATUS:
            return (
                False,
                f"Invalid query-v2c-status '{value}'. Must be one of: {', '.join(VALID_BODY_QUERY_V2C_STATUS)}",
            )

    # Validate query-v2c-port if present
    if "query-v2c-port" in payload:
        value = payload.get("query-v2c-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "query-v2c-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"query-v2c-port must be numeric, got: {value}")

    # Validate trap-v1-status if present
    if "trap-v1-status" in payload:
        value = payload.get("trap-v1-status")
        if value and value not in VALID_BODY_TRAP_V1_STATUS:
            return (
                False,
                f"Invalid trap-v1-status '{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_V1_STATUS)}",
            )

    # Validate trap-v1-lport if present
    if "trap-v1-lport" in payload:
        value = payload.get("trap-v1-lport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "trap-v1-lport must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"trap-v1-lport must be numeric, got: {value}")

    # Validate trap-v1-rport if present
    if "trap-v1-rport" in payload:
        value = payload.get("trap-v1-rport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "trap-v1-rport must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"trap-v1-rport must be numeric, got: {value}")

    # Validate trap-v2c-status if present
    if "trap-v2c-status" in payload:
        value = payload.get("trap-v2c-status")
        if value and value not in VALID_BODY_TRAP_V2C_STATUS:
            return (
                False,
                f"Invalid trap-v2c-status '{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_V2C_STATUS)}",
            )

    # Validate trap-v2c-lport if present
    if "trap-v2c-lport" in payload:
        value = payload.get("trap-v2c-lport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "trap-v2c-lport must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"trap-v2c-lport must be numeric, got: {value}")

    # Validate trap-v2c-rport if present
    if "trap-v2c-rport" in payload:
        value = payload.get("trap-v2c-rport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "trap-v2c-rport must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"trap-v2c-rport must be numeric, got: {value}")

    # Validate events if present
    if "events" in payload:
        value = payload.get("events")
        if value and value not in VALID_BODY_EVENTS:
            return (
                False,
                f"Invalid events '{value}'. Must be one of: {', '.join(VALID_BODY_EVENTS)}",
            )

    # Validate mib-view if present
    if "mib-view" in payload:
        value = payload.get("mib-view")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "mib-view cannot exceed 32 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_snmp_community_put(
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
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate query-v1-status if present
    if "query-v1-status" in payload:
        value = payload.get("query-v1-status")
        if value and value not in VALID_BODY_QUERY_V1_STATUS:
            return (
                False,
                f"Invalid query-v1-status '{value}'. Must be one of: {', '.join(VALID_BODY_QUERY_V1_STATUS)}",
            )

    # Validate query-v1-port if present
    if "query-v1-port" in payload:
        value = payload.get("query-v1-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "query-v1-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"query-v1-port must be numeric, got: {value}")

    # Validate query-v2c-status if present
    if "query-v2c-status" in payload:
        value = payload.get("query-v2c-status")
        if value and value not in VALID_BODY_QUERY_V2C_STATUS:
            return (
                False,
                f"Invalid query-v2c-status '{value}'. Must be one of: {', '.join(VALID_BODY_QUERY_V2C_STATUS)}",
            )

    # Validate query-v2c-port if present
    if "query-v2c-port" in payload:
        value = payload.get("query-v2c-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "query-v2c-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"query-v2c-port must be numeric, got: {value}")

    # Validate trap-v1-status if present
    if "trap-v1-status" in payload:
        value = payload.get("trap-v1-status")
        if value and value not in VALID_BODY_TRAP_V1_STATUS:
            return (
                False,
                f"Invalid trap-v1-status '{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_V1_STATUS)}",
            )

    # Validate trap-v1-lport if present
    if "trap-v1-lport" in payload:
        value = payload.get("trap-v1-lport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "trap-v1-lport must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"trap-v1-lport must be numeric, got: {value}")

    # Validate trap-v1-rport if present
    if "trap-v1-rport" in payload:
        value = payload.get("trap-v1-rport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "trap-v1-rport must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"trap-v1-rport must be numeric, got: {value}")

    # Validate trap-v2c-status if present
    if "trap-v2c-status" in payload:
        value = payload.get("trap-v2c-status")
        if value and value not in VALID_BODY_TRAP_V2C_STATUS:
            return (
                False,
                f"Invalid trap-v2c-status '{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_V2C_STATUS)}",
            )

    # Validate trap-v2c-lport if present
    if "trap-v2c-lport" in payload:
        value = payload.get("trap-v2c-lport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "trap-v2c-lport must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"trap-v2c-lport must be numeric, got: {value}")

    # Validate trap-v2c-rport if present
    if "trap-v2c-rport" in payload:
        value = payload.get("trap-v2c-rport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "trap-v2c-rport must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"trap-v2c-rport must be numeric, got: {value}")

    # Validate events if present
    if "events" in payload:
        value = payload.get("events")
        if value and value not in VALID_BODY_EVENTS:
            return (
                False,
                f"Invalid events '{value}'. Must be one of: {', '.join(VALID_BODY_EVENTS)}",
            )

    # Validate mib-view if present
    if "mib-view" in payload:
        value = payload.get("mib-view")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "mib-view cannot exceed 32 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_snmp_community_delete(
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
