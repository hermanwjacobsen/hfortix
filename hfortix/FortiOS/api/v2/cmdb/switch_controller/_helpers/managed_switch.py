"""
Validation helpers for switch-controller managed_switch endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PURDUE_LEVEL = ["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
VALID_BODY_FSW_WAN1_ADMIN = ["discovered", "disable", "enable"]
VALID_BODY_POE_PRE_STANDARD_DETECTION = ["enable", "disable"]
VALID_BODY_DHCP_SERVER_ACCESS_LIST = ["global", "enable", "disable"]
VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE = ["enable", "disable"]
VALID_BODY_PTP_STATUS = ["disable", "enable"]
VALID_BODY_RADIUS_NAS_IP_OVERRIDE = ["disable", "enable"]
VALID_BODY_ROUTE_OFFLOAD = ["disable", "enable"]
VALID_BODY_ROUTE_OFFLOAD_MCLAG = ["disable", "enable"]
VALID_BODY_TYPE = ["virtual", "physical"]
VALID_BODY_FIRMWARE_PROVISION = ["enable", "disable"]
VALID_BODY_FIRMWARE_PROVISION_LATEST = ["disable", "once"]
VALID_BODY_OVERRIDE_SNMP_SYSINFO = ["disable", "enable"]
VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD = ["enable", "disable"]
VALID_BODY_OVERRIDE_SNMP_COMMUNITY = ["enable", "disable"]
VALID_BODY_OVERRIDE_SNMP_USER = ["enable", "disable"]
VALID_BODY_QOS_DROP_POLICY = ["taildrop", "random-early-detection"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_managed_switch_get(
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


def validate_managed_switch_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating managed_switch.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate switch-id if present
    if "switch-id" in payload:
        value = payload.get("switch-id")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "switch-id cannot exceed 35 characters")

    # Validate sn if present
    if "sn" in payload:
        value = payload.get("sn")
        if value and isinstance(value, str) and len(value) > 16:
            return (False, "sn cannot exceed 16 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "description cannot exceed 63 characters")

    # Validate switch-profile if present
    if "switch-profile" in payload:
        value = payload.get("switch-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "switch-profile cannot exceed 35 characters")

    # Validate access-profile if present
    if "access-profile" in payload:
        value = payload.get("access-profile")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "access-profile cannot exceed 31 characters")

    # Validate purdue-level if present
    if "purdue-level" in payload:
        value = payload.get("purdue-level")
        if value and value not in VALID_BODY_PURDUE_LEVEL:
            return (
                False,
                f"Invalid purdue-level '{value}'. Must be one of: {', '.join(VALID_BODY_PURDUE_LEVEL)}",
            )

    # Validate fsw-wan1-peer if present
    if "fsw-wan1-peer" in payload:
        value = payload.get("fsw-wan1-peer")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fsw-wan1-peer cannot exceed 35 characters")

    # Validate fsw-wan1-admin if present
    if "fsw-wan1-admin" in payload:
        value = payload.get("fsw-wan1-admin")
        if value and value not in VALID_BODY_FSW_WAN1_ADMIN:
            return (
                False,
                f"Invalid fsw-wan1-admin '{value}'. Must be one of: {', '.join(VALID_BODY_FSW_WAN1_ADMIN)}",
            )

    # Validate poe-pre-standard-detection if present
    if "poe-pre-standard-detection" in payload:
        value = payload.get("poe-pre-standard-detection")
        if value and value not in VALID_BODY_POE_PRE_STANDARD_DETECTION:
            return (
                False,
                f"Invalid poe-pre-standard-detection '{value}'. Must be one of: {', '.join(VALID_BODY_POE_PRE_STANDARD_DETECTION)}",
            )

    # Validate dhcp-server-access-list if present
    if "dhcp-server-access-list" in payload:
        value = payload.get("dhcp-server-access-list")
        if value and value not in VALID_BODY_DHCP_SERVER_ACCESS_LIST:
            return (
                False,
                f"Invalid dhcp-server-access-list '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SERVER_ACCESS_LIST)}",
            )

    # Validate poe-detection-type if present
    if "poe-detection-type" in payload:
        value = payload.get("poe-detection-type")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "poe-detection-type must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"poe-detection-type must be numeric, got: {value}",
                )

    # Validate max-poe-budget if present
    if "max-poe-budget" in payload:
        value = payload.get("max-poe-budget")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "max-poe-budget must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"max-poe-budget must be numeric, got: {value}")

    # Validate directly-connected if present
    if "directly-connected" in payload:
        value = payload.get("directly-connected")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1:
                    return (
                        False,
                        "directly-connected must be between 0 and 1",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"directly-connected must be numeric, got: {value}",
                )

    # Validate version if present
    if "version" in payload:
        value = payload.get("version")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "version must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"version must be numeric, got: {value}")

    # Validate max-allowed-trunk-members if present
    if "max-allowed-trunk-members" in payload:
        value = payload.get("max-allowed-trunk-members")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "max-allowed-trunk-members must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-allowed-trunk-members must be numeric, got: {value}",
                )

    # Validate pre-provisioned if present
    if "pre-provisioned" in payload:
        value = payload.get("pre-provisioned")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "pre-provisioned must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pre-provisioned must be numeric, got: {value}",
                )

    # Validate l3-discovered if present
    if "l3-discovered" in payload:
        value = payload.get("l3-discovered")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1:
                    return (False, "l3-discovered must be between 0 and 1")
            except (ValueError, TypeError):
                return (False, f"l3-discovered must be numeric, got: {value}")

    # Validate mgmt-mode if present
    if "mgmt-mode" in payload:
        value = payload.get("mgmt-mode")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "mgmt-mode must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"mgmt-mode must be numeric, got: {value}")

    # Validate tunnel-discovered if present
    if "tunnel-discovered" in payload:
        value = payload.get("tunnel-discovered")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1:
                    return (
                        False,
                        "tunnel-discovered must be between 0 and 1",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tunnel-discovered must be numeric, got: {value}",
                )

    # Validate tdr-supported if present
    if "tdr-supported" in payload:
        value = payload.get("tdr-supported")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "tdr-supported cannot exceed 31 characters")

    # Validate switch-device-tag if present
    if "switch-device-tag" in payload:
        value = payload.get("switch-device-tag")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "switch-device-tag cannot exceed 32 characters")

    # Validate switch-dhcp_opt43_key if present
    if "switch-dhcp_opt43_key" in payload:
        value = payload.get("switch-dhcp_opt43_key")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "switch-dhcp_opt43_key cannot exceed 63 characters",
            )

    # Validate mclag-igmp-snooping-aware if present
    if "mclag-igmp-snooping-aware" in payload:
        value = payload.get("mclag-igmp-snooping-aware")
        if value and value not in VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE:
            return (
                False,
                f"Invalid mclag-igmp-snooping-aware '{value}'. Must be one of: {', '.join(VALID_BODY_MCLAG_IGMP_SNOOPING_AWARE)}",
            )

    # Validate dynamically-discovered if present
    if "dynamically-discovered" in payload:
        value = payload.get("dynamically-discovered")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1:
                    return (
                        False,
                        "dynamically-discovered must be between 0 and 1",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dynamically-discovered must be numeric, got: {value}",
                )

    # Validate ptp-status if present
    if "ptp-status" in payload:
        value = payload.get("ptp-status")
        if value and value not in VALID_BODY_PTP_STATUS:
            return (
                False,
                f"Invalid ptp-status '{value}'. Must be one of: {', '.join(VALID_BODY_PTP_STATUS)}",
            )

    # Validate ptp-profile if present
    if "ptp-profile" in payload:
        value = payload.get("ptp-profile")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ptp-profile cannot exceed 63 characters")

    # Validate radius-nas-ip-override if present
    if "radius-nas-ip-override" in payload:
        value = payload.get("radius-nas-ip-override")
        if value and value not in VALID_BODY_RADIUS_NAS_IP_OVERRIDE:
            return (
                False,
                f"Invalid radius-nas-ip-override '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_NAS_IP_OVERRIDE)}",
            )

    # Validate route-offload if present
    if "route-offload" in payload:
        value = payload.get("route-offload")
        if value and value not in VALID_BODY_ROUTE_OFFLOAD:
            return (
                False,
                f"Invalid route-offload '{value}'. Must be one of: {', '.join(VALID_BODY_ROUTE_OFFLOAD)}",
            )

    # Validate route-offload-mclag if present
    if "route-offload-mclag" in payload:
        value = payload.get("route-offload-mclag")
        if value and value not in VALID_BODY_ROUTE_OFFLOAD_MCLAG:
            return (
                False,
                f"Invalid route-offload-mclag '{value}'. Must be one of: {', '.join(VALID_BODY_ROUTE_OFFLOAD_MCLAG)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate owner-vdom if present
    if "owner-vdom" in payload:
        value = payload.get("owner-vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "owner-vdom cannot exceed 31 characters")

    # Validate staged-image-version if present
    if "staged-image-version" in payload:
        value = payload.get("staged-image-version")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "staged-image-version cannot exceed 127 characters",
            )

    # Validate delayed-restart-trigger if present
    if "delayed-restart-trigger" in payload:
        value = payload.get("delayed-restart-trigger")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "delayed-restart-trigger must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"delayed-restart-trigger must be numeric, got: {value}",
                )

    # Validate firmware-provision if present
    if "firmware-provision" in payload:
        value = payload.get("firmware-provision")
        if value and value not in VALID_BODY_FIRMWARE_PROVISION:
            return (
                False,
                f"Invalid firmware-provision '{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION)}",
            )

    # Validate firmware-provision-version if present
    if "firmware-provision-version" in payload:
        value = payload.get("firmware-provision-version")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "firmware-provision-version cannot exceed 35 characters",
            )

    # Validate firmware-provision-latest if present
    if "firmware-provision-latest" in payload:
        value = payload.get("firmware-provision-latest")
        if value and value not in VALID_BODY_FIRMWARE_PROVISION_LATEST:
            return (
                False,
                f"Invalid firmware-provision-latest '{value}'. Must be one of: {', '.join(VALID_BODY_FIRMWARE_PROVISION_LATEST)}",
            )

    # Validate override-snmp-sysinfo if present
    if "override-snmp-sysinfo" in payload:
        value = payload.get("override-snmp-sysinfo")
        if value and value not in VALID_BODY_OVERRIDE_SNMP_SYSINFO:
            return (
                False,
                f"Invalid override-snmp-sysinfo '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SNMP_SYSINFO)}",
            )

    # Validate override-snmp-trap-threshold if present
    if "override-snmp-trap-threshold" in payload:
        value = payload.get("override-snmp-trap-threshold")
        if value and value not in VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD:
            return (
                False,
                f"Invalid override-snmp-trap-threshold '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SNMP_TRAP_THRESHOLD)}",
            )

    # Validate override-snmp-community if present
    if "override-snmp-community" in payload:
        value = payload.get("override-snmp-community")
        if value and value not in VALID_BODY_OVERRIDE_SNMP_COMMUNITY:
            return (
                False,
                f"Invalid override-snmp-community '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SNMP_COMMUNITY)}",
            )

    # Validate override-snmp-user if present
    if "override-snmp-user" in payload:
        value = payload.get("override-snmp-user")
        if value and value not in VALID_BODY_OVERRIDE_SNMP_USER:
            return (
                False,
                f"Invalid override-snmp-user '{value}'. Must be one of: {', '.join(VALID_BODY_OVERRIDE_SNMP_USER)}",
            )

    # Validate qos-drop-policy if present
    if "qos-drop-policy" in payload:
        value = payload.get("qos-drop-policy")
        if value and value not in VALID_BODY_QOS_DROP_POLICY:
            return (
                False,
                f"Invalid qos-drop-policy '{value}'. Must be one of: {', '.join(VALID_BODY_QOS_DROP_POLICY)}",
            )

    # Validate qos-red-probability if present
    if "qos-red-probability" in payload:
        value = payload.get("qos-red-probability")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "qos-red-probability must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"qos-red-probability must be numeric, got: {value}",
                )

    return (True, None)
