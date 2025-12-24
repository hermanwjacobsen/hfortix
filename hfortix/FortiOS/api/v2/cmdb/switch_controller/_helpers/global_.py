"""
Validation helpers for switch-controller global_ endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_HTTPS_IMAGE_PUSH = ["enable", "disable"]
VALID_BODY_VLAN_ALL_MODE = ["all", "defined"]
VALID_BODY_VLAN_OPTIMIZATION = ["prune", "configured", "none"]
VALID_BODY_VLAN_IDENTITY = ["description", "name"]
VALID_BODY_DHCP_SERVER_ACCESS_LIST = ["enable", "disable"]
VALID_BODY_DHCP_OPTION82_FORMAT = ["ascii", "legacy"]
VALID_BODY_DHCP_OPTION82_CIRCUIT_ID = [
    "intfname",
    "vlan",
    "hostname",
    "mode",
    "description",
]
VALID_BODY_DHCP_OPTION82_REMOTE_ID = ["mac", "hostname", "ip"]
VALID_BODY_DHCP_SNOOP_CLIENT_REQ = ["drop-untrusted", "forward-untrusted"]
VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS = ["enable", "disable"]
VALID_BODY_SN_DNS_RESOLUTION = ["enable", "disable"]
VALID_BODY_MAC_EVENT_LOGGING = ["enable", "disable"]
VALID_BODY_BOUNCE_QUARANTINED_LINK = ["disable", "enable"]
VALID_BODY_QUARANTINE_MODE = ["by-vlan", "by-redirect"]
VALID_BODY_UPDATE_USER_DEVICE = [
    "mac-cache",
    "lldp",
    "dhcp-snooping",
    "l2-db",
    "l3-db",
]
VALID_BODY_FIPS_ENFORCE = ["disable", "enable"]
VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION = ["enable", "disable"]
VALID_BODY_SWITCH_ON_DEAUTH = ["no-op", "factory-reset"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_global__get(
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
# PUT Validation
# ============================================================================


def validate_global__put(
    payload: dict[str, Any] | None = None,
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate mac-aging-interval if present
    if "mac-aging-interval" in payload:
        value = payload.get("mac-aging-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 1000000:
                    return (
                        False,
                        "mac-aging-interval must be between 10 and 1000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"mac-aging-interval must be numeric, got: {value}",
                )

    # Validate https-image-push if present
    if "https-image-push" in payload:
        value = payload.get("https-image-push")
        if value and value not in VALID_BODY_HTTPS_IMAGE_PUSH:
            return (
                False,
                f"Invalid https-image-push '{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_IMAGE_PUSH)}",
            )

    # Validate vlan-all-mode if present
    if "vlan-all-mode" in payload:
        value = payload.get("vlan-all-mode")
        if value and value not in VALID_BODY_VLAN_ALL_MODE:
            return (
                False,
                f"Invalid vlan-all-mode '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_ALL_MODE)}",
            )

    # Validate vlan-optimization if present
    if "vlan-optimization" in payload:
        value = payload.get("vlan-optimization")
        if value and value not in VALID_BODY_VLAN_OPTIMIZATION:
            return (
                False,
                f"Invalid vlan-optimization '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_OPTIMIZATION)}",
            )

    # Validate vlan-identity if present
    if "vlan-identity" in payload:
        value = payload.get("vlan-identity")
        if value and value not in VALID_BODY_VLAN_IDENTITY:
            return (
                False,
                f"Invalid vlan-identity '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_IDENTITY)}",
            )

    # Validate mac-retention-period if present
    if "mac-retention-period" in payload:
        value = payload.get("mac-retention-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 168:
                    return (
                        False,
                        "mac-retention-period must be between 0 and 168",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"mac-retention-period must be numeric, got: {value}",
                )

    # Validate default-virtual-switch-vlan if present
    if "default-virtual-switch-vlan" in payload:
        value = payload.get("default-virtual-switch-vlan")
        if value and isinstance(value, str) and len(value) > 15:
            return (
                False,
                "default-virtual-switch-vlan cannot exceed 15 characters",
            )

    # Validate dhcp-server-access-list if present
    if "dhcp-server-access-list" in payload:
        value = payload.get("dhcp-server-access-list")
        if value and value not in VALID_BODY_DHCP_SERVER_ACCESS_LIST:
            return (
                False,
                f"Invalid dhcp-server-access-list '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SERVER_ACCESS_LIST)}",
            )

    # Validate dhcp-option82-format if present
    if "dhcp-option82-format" in payload:
        value = payload.get("dhcp-option82-format")
        if value and value not in VALID_BODY_DHCP_OPTION82_FORMAT:
            return (
                False,
                f"Invalid dhcp-option82-format '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_FORMAT)}",
            )

    # Validate dhcp-option82-circuit-id if present
    if "dhcp-option82-circuit-id" in payload:
        value = payload.get("dhcp-option82-circuit-id")
        if value and value not in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID:
            return (
                False,
                f"Invalid dhcp-option82-circuit-id '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_CIRCUIT_ID)}",
            )

    # Validate dhcp-option82-remote-id if present
    if "dhcp-option82-remote-id" in payload:
        value = payload.get("dhcp-option82-remote-id")
        if value and value not in VALID_BODY_DHCP_OPTION82_REMOTE_ID:
            return (
                False,
                f"Invalid dhcp-option82-remote-id '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_REMOTE_ID)}",
            )

    # Validate dhcp-snoop-client-req if present
    if "dhcp-snoop-client-req" in payload:
        value = payload.get("dhcp-snoop-client-req")
        if value and value not in VALID_BODY_DHCP_SNOOP_CLIENT_REQ:
            return (
                False,
                f"Invalid dhcp-snoop-client-req '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SNOOP_CLIENT_REQ)}",
            )

    # Validate dhcp-snoop-client-db-exp if present
    if "dhcp-snoop-client-db-exp" in payload:
        value = payload.get("dhcp-snoop-client-db-exp")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 259200:
                    return (
                        False,
                        "dhcp-snoop-client-db-exp must be between 300 and 259200",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-snoop-client-db-exp must be numeric, got: {value}",
                )

    # Validate dhcp-snoop-db-per-port-learn-limit if present
    if "dhcp-snoop-db-per-port-learn-limit" in payload:
        value = payload.get("dhcp-snoop-db-per-port-learn-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2048:
                    return (
                        False,
                        "dhcp-snoop-db-per-port-learn-limit must be between 0 and 2048",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-snoop-db-per-port-learn-limit must be numeric, got: {value}",
                )

    # Validate log-mac-limit-violations if present
    if "log-mac-limit-violations" in payload:
        value = payload.get("log-mac-limit-violations")
        if value and value not in VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS:
            return (
                False,
                f"Invalid log-mac-limit-violations '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_MAC_LIMIT_VIOLATIONS)}",
            )

    # Validate mac-violation-timer if present
    if "mac-violation-timer" in payload:
        value = payload.get("mac-violation-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "mac-violation-timer must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"mac-violation-timer must be numeric, got: {value}",
                )

    # Validate sn-dns-resolution if present
    if "sn-dns-resolution" in payload:
        value = payload.get("sn-dns-resolution")
        if value and value not in VALID_BODY_SN_DNS_RESOLUTION:
            return (
                False,
                f"Invalid sn-dns-resolution '{value}'. Must be one of: {', '.join(VALID_BODY_SN_DNS_RESOLUTION)}",
            )

    # Validate mac-event-logging if present
    if "mac-event-logging" in payload:
        value = payload.get("mac-event-logging")
        if value and value not in VALID_BODY_MAC_EVENT_LOGGING:
            return (
                False,
                f"Invalid mac-event-logging '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_EVENT_LOGGING)}",
            )

    # Validate bounce-quarantined-link if present
    if "bounce-quarantined-link" in payload:
        value = payload.get("bounce-quarantined-link")
        if value and value not in VALID_BODY_BOUNCE_QUARANTINED_LINK:
            return (
                False,
                f"Invalid bounce-quarantined-link '{value}'. Must be one of: {', '.join(VALID_BODY_BOUNCE_QUARANTINED_LINK)}",
            )

    # Validate quarantine-mode if present
    if "quarantine-mode" in payload:
        value = payload.get("quarantine-mode")
        if value and value not in VALID_BODY_QUARANTINE_MODE:
            return (
                False,
                f"Invalid quarantine-mode '{value}'. Must be one of: {', '.join(VALID_BODY_QUARANTINE_MODE)}",
            )

    # Validate update-user-device if present
    if "update-user-device" in payload:
        value = payload.get("update-user-device")
        if value and value not in VALID_BODY_UPDATE_USER_DEVICE:
            return (
                False,
                f"Invalid update-user-device '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_USER_DEVICE)}",
            )

    # Validate fips-enforce if present
    if "fips-enforce" in payload:
        value = payload.get("fips-enforce")
        if value and value not in VALID_BODY_FIPS_ENFORCE:
            return (
                False,
                f"Invalid fips-enforce '{value}'. Must be one of: {', '.join(VALID_BODY_FIPS_ENFORCE)}",
            )

    # Validate firmware-provision-on-authorization if present
    if "firmware-provision-on-authorization" in payload:
        value = payload.get("firmware-provision-on-authorization")
        if (
            value
            and value not in VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION
        ):
            return (
                False,
                f"Invalid firmware-provision-on-authorization '{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION)}",
            )

    # Validate switch-on-deauth if present
    if "switch-on-deauth" in payload:
        value = payload.get("switch-on-deauth")
        if value and value not in VALID_BODY_SWITCH_ON_DEAUTH:
            return (
                False,
                f"Invalid switch-on-deauth '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_ON_DEAUTH)}",
            )

    # Validate firewall-auth-user-hold-period if present
    if "firewall-auth-user-hold-period" in payload:
        value = payload.get("firewall-auth-user-hold-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 1440:
                    return (
                        False,
                        "firewall-auth-user-hold-period must be between 5 and 1440",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"firewall-auth-user-hold-period must be numeric, got: {value}",
                )

    return (True, None)
