"""
Validation helpers for system snmp_user endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_TRAP_STATUS = ["enable", "disable"]
VALID_BODY_QUERIES = ["enable", "disable"]
VALID_BODY_HA_DIRECT = ["enable", "disable"]
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
VALID_BODY_SECURITY_LEVEL = ["no-auth-no-priv", "auth-no-priv", "auth-priv"]
VALID_BODY_AUTH_PROTO = ["md5", "sha", "sha224", "sha256", "sha384", "sha512"]
VALID_BODY_PRIV_PROTO = ["aes", "des", "aes256", "aes256cisco"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_snmp_user_get(
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


def validate_snmp_user_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating snmp_user.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "name cannot exceed 32 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate trap-status if present
    if "trap-status" in payload:
        value = payload.get("trap-status")
        if value and value not in VALID_BODY_TRAP_STATUS:
            return (
                False,
                f"Invalid trap-status '{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_STATUS)}",
            )

    # Validate trap-lport if present
    if "trap-lport" in payload:
        value = payload.get("trap-lport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "trap-lport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"trap-lport must be numeric, got: {value}")

    # Validate trap-rport if present
    if "trap-rport" in payload:
        value = payload.get("trap-rport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "trap-rport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"trap-rport must be numeric, got: {value}")

    # Validate queries if present
    if "queries" in payload:
        value = payload.get("queries")
        if value and value not in VALID_BODY_QUERIES:
            return (
                False,
                f"Invalid queries '{value}'. Must be one of: {', '.join(VALID_BODY_QUERIES)}",
            )

    # Validate query-port if present
    if "query-port" in payload:
        value = payload.get("query-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "query-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"query-port must be numeric, got: {value}")

    # Validate ha-direct if present
    if "ha-direct" in payload:
        value = payload.get("ha-direct")
        if value and value not in VALID_BODY_HA_DIRECT:
            return (
                False,
                f"Invalid ha-direct '{value}'. Must be one of: {', '.join(VALID_BODY_HA_DIRECT)}",
            )

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

    # Validate security-level if present
    if "security-level" in payload:
        value = payload.get("security-level")
        if value and value not in VALID_BODY_SECURITY_LEVEL:
            return (
                False,
                f"Invalid security-level '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_LEVEL)}",
            )

    # Validate auth-proto if present
    if "auth-proto" in payload:
        value = payload.get("auth-proto")
        if value and value not in VALID_BODY_AUTH_PROTO:
            return (
                False,
                f"Invalid auth-proto '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PROTO)}",
            )

    # Validate priv-proto if present
    if "priv-proto" in payload:
        value = payload.get("priv-proto")
        if value and value not in VALID_BODY_PRIV_PROTO:
            return (
                False,
                f"Invalid priv-proto '{value}'. Must be one of: {', '.join(VALID_BODY_PRIV_PROTO)}",
            )

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


def validate_snmp_user_put(
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
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "name cannot exceed 32 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate trap-status if present
    if "trap-status" in payload:
        value = payload.get("trap-status")
        if value and value not in VALID_BODY_TRAP_STATUS:
            return (
                False,
                f"Invalid trap-status '{value}'. Must be one of: {', '.join(VALID_BODY_TRAP_STATUS)}",
            )

    # Validate trap-lport if present
    if "trap-lport" in payload:
        value = payload.get("trap-lport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "trap-lport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"trap-lport must be numeric, got: {value}")

    # Validate trap-rport if present
    if "trap-rport" in payload:
        value = payload.get("trap-rport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "trap-rport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"trap-rport must be numeric, got: {value}")

    # Validate queries if present
    if "queries" in payload:
        value = payload.get("queries")
        if value and value not in VALID_BODY_QUERIES:
            return (
                False,
                f"Invalid queries '{value}'. Must be one of: {', '.join(VALID_BODY_QUERIES)}",
            )

    # Validate query-port if present
    if "query-port" in payload:
        value = payload.get("query-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "query-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"query-port must be numeric, got: {value}")

    # Validate ha-direct if present
    if "ha-direct" in payload:
        value = payload.get("ha-direct")
        if value and value not in VALID_BODY_HA_DIRECT:
            return (
                False,
                f"Invalid ha-direct '{value}'. Must be one of: {', '.join(VALID_BODY_HA_DIRECT)}",
            )

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

    # Validate security-level if present
    if "security-level" in payload:
        value = payload.get("security-level")
        if value and value not in VALID_BODY_SECURITY_LEVEL:
            return (
                False,
                f"Invalid security-level '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_LEVEL)}",
            )

    # Validate auth-proto if present
    if "auth-proto" in payload:
        value = payload.get("auth-proto")
        if value and value not in VALID_BODY_AUTH_PROTO:
            return (
                False,
                f"Invalid auth-proto '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_PROTO)}",
            )

    # Validate priv-proto if present
    if "priv-proto" in payload:
        value = payload.get("priv-proto")
        if value and value not in VALID_BODY_PRIV_PROTO:
            return (
                False,
                f"Invalid priv-proto '{value}'. Must be one of: {', '.join(VALID_BODY_PRIV_PROTO)}",
            )

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


def validate_snmp_user_delete(
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
