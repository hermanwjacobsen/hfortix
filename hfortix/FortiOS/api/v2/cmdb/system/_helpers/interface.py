"""
Validation helpers for system interface endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FORTILINK = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP = ["outbound", "fixed"]
VALID_BODY_MODE = ["static", "dhcp", "pppoe"]
VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_DHCP_BROADCAST_FLAG = ["disable", "enable"]
VALID_BODY_DHCP_RELAY_SERVICE = ["disable", "enable"]
VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER = ["disable", "enable"]
VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION = ["disable", "enable"]
VALID_BODY_DHCP_RELAY_TYPE = ["regular", "ipsec"]
VALID_BODY_DHCP_SMART_RELAY = ["disable", "enable"]
VALID_BODY_DHCP_RELAY_AGENT_OPTION = ["enable", "disable"]
VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION = ["enable", "disable"]
VALID_BODY_ALLOWACCESS = [
    "ping",
    "https",
    "ssh",
    "snmp",
    "http",
    "telnet",
    "fgfm",
    "radius-acct",
    "probe-response",
    "fabric",
    "ftm",
    "speed-test",
    "scim",
]
VALID_BODY_GWDETECT = ["enable", "disable"]
VALID_BODY_DETECTPROTOCOL = ["ping", "tcp-echo", "udp-echo"]
VALID_BODY_FAIL_DETECT = ["enable", "disable"]
VALID_BODY_FAIL_DETECT_OPTION = ["detectserver", "link-down"]
VALID_BODY_FAIL_ALERT_METHOD = ["link-failed-signal", "link-down"]
VALID_BODY_FAIL_ACTION_ON_EXTENDER = ["soft-restart", "hard-restart", "reboot"]
VALID_BODY_PPPOE_EGRESS_COS = [
    "cos0",
    "cos1",
    "cos2",
    "cos3",
    "cos4",
    "cos5",
    "cos6",
    "cos7",
]
VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE = ["enable", "disable"]
VALID_BODY_MULTILINK = ["enable", "disable"]
VALID_BODY_DEFAULTGW = ["enable", "disable"]
VALID_BODY_DNS_SERVER_OVERRIDE = ["enable", "disable"]
VALID_BODY_DNS_SERVER_PROTOCOL = ["cleartext", "dot", "doh"]
VALID_BODY_AUTH_TYPE = ["auto", "pap", "chap", "mschapv1", "mschapv2"]
VALID_BODY_PPTP_CLIENT = ["enable", "disable"]
VALID_BODY_PPTP_AUTH_TYPE = ["auto", "pap", "chap", "mschapv1", "mschapv2"]
VALID_BODY_ARPFORWARD = ["enable", "disable"]
VALID_BODY_NDISCFORWARD = ["enable", "disable"]
VALID_BODY_BROADCAST_FORWARD = ["enable", "disable"]
VALID_BODY_BFD = ["global", "enable", "disable"]
VALID_BODY_L2FORWARD = ["enable", "disable"]
VALID_BODY_ICMP_SEND_REDIRECT = ["enable", "disable"]
VALID_BODY_ICMP_ACCEPT_REDIRECT = ["enable", "disable"]
VALID_BODY_VLANFORWARD = ["enable", "disable"]
VALID_BODY_STPFORWARD = ["enable", "disable"]
VALID_BODY_STPFORWARD_MODE = [
    "rpl-all-ext-id",
    "rpl-bridge-ext-id",
    "rpl-nothing",
]
VALID_BODY_IPS_SNIFFER_MODE = ["enable", "disable"]
VALID_BODY_IDENT_ACCEPT = ["enable", "disable"]
VALID_BODY_IPMAC = ["enable", "disable"]
VALID_BODY_SUBST = ["enable", "disable"]
VALID_BODY_SPEED = [
    "auto",
    "10full",
    "10hal",
    "100full",
    "100hal",
    "100auto",
    "1000full",
    "1000auto",
]
VALID_BODY_STATUS = ["up", "down"]
VALID_BODY_NETBIOS_FORWARD = ["disable", "enable"]
VALID_BODY_TYPE = [
    "physical",
    "vlan",
    "aggregate",
    "redundant",
    "tunnel",
    "vdom-link",
    "loopback",
    "switch",
    "hard-switch",
    "vap-switch",
    "wl-mesh",
    "fext-wan",
    "vxlan",
    "geneve",
    "switch-vlan",
    "emac-vlan",
    "lan-extension",
]
VALID_BODY_DEDICATED_TO = ["none", "management"]
VALID_BODY_WCCP = ["enable", "disable"]
VALID_BODY_NETFLOW_SAMPLER = ["disable", "tx", "rx", "both"]
VALID_BODY_SFLOW_SAMPLER = ["enable", "disable"]
VALID_BODY_DROP_FRAGMENT = ["enable", "disable"]
VALID_BODY_SRC_CHECK = ["enable", "disable"]
VALID_BODY_SAMPLE_DIRECTION = ["tx", "rx", "both"]
VALID_BODY_EXPLICIT_WEB_PROXY = ["enable", "disable"]
VALID_BODY_EXPLICIT_FTP_PROXY = ["enable", "disable"]
VALID_BODY_PROXY_CAPTIVE_PORTAL = ["enable", "disable"]
VALID_BODY_EXTERNAL = ["enable", "disable"]
VALID_BODY_MTU_OVERRIDE = ["enable", "disable"]
VALID_BODY_VLAN_PROTOCOL = ["8021q", "8021ad"]
VALID_BODY_TRUNK = ["enable", "disable"]
VALID_BODY_LACP_MODE = ["static", "passive", "active"]
VALID_BODY_LACP_HA_SECONDARY = ["enable", "disable"]
VALID_BODY_SYSTEM_ID_TYPE = ["auto", "user"]
VALID_BODY_LACP_SPEED = ["slow", "fast"]
VALID_BODY_MIN_LINKS_DOWN = ["operational", "administrative"]
VALID_BODY_ALGORITHM = ["L2", "L3", "L4", "NPU-GRE", "Source-MAC"]
VALID_BODY_AGGREGATE_TYPE = ["physical", "vxlan"]
VALID_BODY_PRIORITY_OVERRIDE = ["enable", "disable"]
VALID_BODY_L2TP_CLIENT = ["enable", "disable"]
VALID_BODY_SECURITY_MODE = ["none", "captive-portal", "802.1X"]
VALID_BODY_SECURITY_MAC_AUTH_BYPASS = ["mac-auth-only", "enable", "disable"]
VALID_BODY_SECURITY_IP_AUTH_BYPASS = ["enable", "disable"]
VALID_BODY_SECURITY_8021X_MODE = [
    "default",
    "dynamic-vlan",
    "fallback",
    "slave",
]
VALID_BODY_SECURITY_8021X_MEMBER_MODE = ["switch", "disable"]
VALID_BODY_STP = ["disable", "enable"]
VALID_BODY_STP_HA_SECONDARY = ["disable", "enable", "priority-adjust"]
VALID_BODY_STP_EDGE = ["disable", "enable"]
VALID_BODY_DEVICE_IDENTIFICATION = ["enable", "disable"]
VALID_BODY_EXCLUDE_SIGNATURES = ["iot", "ot"]
VALID_BODY_DEVICE_USER_IDENTIFICATION = ["enable", "disable"]
VALID_BODY_LLDP_RECEPTION = ["enable", "disable", "vdom"]
VALID_BODY_LLDP_TRANSMISSION = ["enable", "disable", "vdom"]
VALID_BODY_MONITOR_BANDWIDTH = ["enable", "disable"]
VALID_BODY_VRRP_VIRTUAL_MAC = ["enable", "disable"]
VALID_BODY_ROLE = ["lan", "wan", "dmz", "undefined"]
VALID_BODY_SECONDARY_IP = ["enable", "disable"]
VALID_BODY_PRESERVE_SESSION_ROUTE = ["enable", "disable"]
VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE = ["enable", "disable"]
VALID_BODY_AP_DISCOVER = ["enable", "disable"]
VALID_BODY_FORTILINK_NEIGHBOR_DETECT = ["lldp", "fortilink"]
VALID_BODY_IP_MANAGED_BY_FORTIIPAM = ["inherit-global", "enable", "disable"]
VALID_BODY_MANAGED_SUBNETWORK_SIZE = [
    "4",
    "8",
    "16",
    "32",
    "64",
    "128",
    "256",
    "512",
    "1024",
    "2048",
    "4096",
    "8192",
    "16384",
    "32768",
    "65536",
    "131072",
    "262144",
    "524288",
    "1048576",
    "2097152",
    "4194304",
    "8388608",
    "16777216",
]
VALID_BODY_FORTILINK_SPLIT_INTERFACE = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE = ["disable", "enable"]
VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT = ["disable", "enable"]
VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82 = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION = ["enable", "disable", "monitor"]
VALID_BODY_SWITCH_CONTROLLER_FEATURE = [
    "none",
    "default-vlan",
    "quarantine",
    "rspan",
    "voice",
    "video",
    "nac",
    "nac-segment",
]
VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_OFFLOAD = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW = ["enable", "disable"]
VALID_BODY_EAP_SUPPLICANT = ["enable", "disable"]
VALID_BODY_EAP_METHOD = ["tls", "peap"]
VALID_BODY_DEFAULT_PURDUE_LEVEL = [
    "1",
    "1.5",
    "2",
    "2.5",
    "3",
    "3.5",
    "4",
    "5",
    "5.5",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_interface_get(
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


def validate_interface_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating interface.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate vrf if present
    if "vr" in payload:
        value = payload.get("vr")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf must be numeric, got: {value}")

    # Validate cli-conn-status if present
    if "cli-conn-status" in payload:
        value = payload.get("cli-conn-status")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "cli-conn-status must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cli-conn-status must be numeric, got: {value}",
                )

    # Validate fortilink if present
    if "fortilink" in payload:
        value = payload.get("fortilink")
        if value and value not in VALID_BODY_FORTILINK:
            return (
                False,
                f"Invalid fortilink '{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK)}",
            )

    # Validate switch-controller-source-ip if present
    if "switch-controller-source-ip" in payload:
        value = payload.get("switch-controller-source-ip")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP:
            return (
                False,
                f"Invalid switch-controller-source-ip '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP)}",
            )

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate distance if present
    if "distance" in payload:
        value = payload.get("distance")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "distance must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"distance must be numeric, got: {value}")

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "priority must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"priority must be numeric, got: {value}")

    # Validate dhcp-relay-interface-select-method if present
    if "dhcp-relay-interface-select-method" in payload:
        value = payload.get("dhcp-relay-interface-select-method")
        if (
            value
            and value not in VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD
        ):
            return (
                False,
                f"Invalid dhcp-relay-interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate dhcp-relay-interface if present
    if "dhcp-relay-interface" in payload:
        value = payload.get("dhcp-relay-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "dhcp-relay-interface cannot exceed 15 characters")

    # Validate dhcp-relay-vrf-select if present
    if "dhcp-relay-vrf-select" in payload:
        value = payload.get("dhcp-relay-vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (
                        False,
                        "dhcp-relay-vrf-select must be between 0 and 511",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-relay-vrf-select must be numeric, got: {value}",
                )

    # Validate dhcp-broadcast-flag if present
    if "dhcp-broadcast-flag" in payload:
        value = payload.get("dhcp-broadcast-flag")
        if value and value not in VALID_BODY_DHCP_BROADCAST_FLAG:
            return (
                False,
                f"Invalid dhcp-broadcast-flag '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_BROADCAST_FLAG)}",
            )

    # Validate dhcp-relay-service if present
    if "dhcp-relay-service" in payload:
        value = payload.get("dhcp-relay-service")
        if value and value not in VALID_BODY_DHCP_RELAY_SERVICE:
            return (
                False,
                f"Invalid dhcp-relay-service '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_SERVICE)}",
            )

    # Validate dhcp-relay-circuit-id if present
    if "dhcp-relay-circuit-id" in payload:
        value = payload.get("dhcp-relay-circuit-id")
        if value and isinstance(value, str) and len(value) > 64:
            return (
                False,
                "dhcp-relay-circuit-id cannot exceed 64 characters",
            )

    # Validate dhcp-relay-request-all-server if present
    if "dhcp-relay-request-all-server" in payload:
        value = payload.get("dhcp-relay-request-all-server")
        if value and value not in VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER:
            return (
                False,
                f"Invalid dhcp-relay-request-all-server '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER)}",
            )

    # Validate dhcp-relay-allow-no-end-option if present
    if "dhcp-relay-allow-no-end-option" in payload:
        value = payload.get("dhcp-relay-allow-no-end-option")
        if value and value not in VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION:
            return (
                False,
                f"Invalid dhcp-relay-allow-no-end-option '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION)}",
            )

    # Validate dhcp-relay-type if present
    if "dhcp-relay-type" in payload:
        value = payload.get("dhcp-relay-type")
        if value and value not in VALID_BODY_DHCP_RELAY_TYPE:
            return (
                False,
                f"Invalid dhcp-relay-type '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_TYPE)}",
            )

    # Validate dhcp-smart-relay if present
    if "dhcp-smart-relay" in payload:
        value = payload.get("dhcp-smart-relay")
        if value and value not in VALID_BODY_DHCP_SMART_RELAY:
            return (
                False,
                f"Invalid dhcp-smart-relay '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SMART_RELAY)}",
            )

    # Validate dhcp-relay-agent-option if present
    if "dhcp-relay-agent-option" in payload:
        value = payload.get("dhcp-relay-agent-option")
        if value and value not in VALID_BODY_DHCP_RELAY_AGENT_OPTION:
            return (
                False,
                f"Invalid dhcp-relay-agent-option '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_AGENT_OPTION)}",
            )

    # Validate dhcp-classless-route-addition if present
    if "dhcp-classless-route-addition" in payload:
        value = payload.get("dhcp-classless-route-addition")
        if value and value not in VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION:
            return (
                False,
                f"Invalid dhcp-classless-route-addition '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION)}",
            )

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    # Validate gwdetect if present
    if "gwdetect" in payload:
        value = payload.get("gwdetect")
        if value and value not in VALID_BODY_GWDETECT:
            return (
                False,
                f"Invalid gwdetect '{value}'. Must be one of: {', '.join(VALID_BODY_GWDETECT)}",
            )

    # Validate ping-serv-status if present
    if "ping-serv-status" in payload:
        value = payload.get("ping-serv-status")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "ping-serv-status must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ping-serv-status must be numeric, got: {value}",
                )

    # Validate detectprotocol if present
    if "detectprotocol" in payload:
        value = payload.get("detectprotocol")
        if value and value not in VALID_BODY_DETECTPROTOCOL:
            return (
                False,
                f"Invalid detectprotocol '{value}'. Must be one of: {', '.join(VALID_BODY_DETECTPROTOCOL)}",
            )

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

    # Validate fail-detect if present
    if "fail-detect" in payload:
        value = payload.get("fail-detect")
        if value and value not in VALID_BODY_FAIL_DETECT:
            return (
                False,
                f"Invalid fail-detect '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_DETECT)}",
            )

    # Validate fail-detect-option if present
    if "fail-detect-option" in payload:
        value = payload.get("fail-detect-option")
        if value and value not in VALID_BODY_FAIL_DETECT_OPTION:
            return (
                False,
                f"Invalid fail-detect-option '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_DETECT_OPTION)}",
            )

    # Validate fail-alert-method if present
    if "fail-alert-method" in payload:
        value = payload.get("fail-alert-method")
        if value and value not in VALID_BODY_FAIL_ALERT_METHOD:
            return (
                False,
                f"Invalid fail-alert-method '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_ALERT_METHOD)}",
            )

    # Validate fail-action-on-extender if present
    if "fail-action-on-extender" in payload:
        value = payload.get("fail-action-on-extender")
        if value and value not in VALID_BODY_FAIL_ACTION_ON_EXTENDER:
            return (
                False,
                f"Invalid fail-action-on-extender '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_ACTION_ON_EXTENDER)}",
            )

    # Validate dhcp-client-identifier if present
    if "dhcp-client-identifier" in payload:
        value = payload.get("dhcp-client-identifier")
        if value and isinstance(value, str) and len(value) > 48:
            return (
                False,
                "dhcp-client-identifier cannot exceed 48 characters",
            )

    # Validate dhcp-renew-time if present
    if "dhcp-renew-time" in payload:
        value = payload.get("dhcp-renew-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 604800:
                    return (
                        False,
                        "dhcp-renew-time must be between 300 and 604800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-renew-time must be numeric, got: {value}",
                )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate pppoe-egress-cos if present
    if "pppoe-egress-cos" in payload:
        value = payload.get("pppoe-egress-cos")
        if value and value not in VALID_BODY_PPPOE_EGRESS_COS:
            return (
                False,
                f"Invalid pppoe-egress-cos '{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_EGRESS_COS)}",
            )

    # Validate pppoe-unnumbered-negotiate if present
    if "pppoe-unnumbered-negotiate" in payload:
        value = payload.get("pppoe-unnumbered-negotiate")
        if value and value not in VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE:
            return (
                False,
                f"Invalid pppoe-unnumbered-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE)}",
            )

    # Validate idle-timeout if present
    if "idle-timeout" in payload:
        value = payload.get("idle-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (False, "idle-timeout must be between 0 and 32767")
            except (ValueError, TypeError):
                return (False, f"idle-timeout must be numeric, got: {value}")

    # Validate multilink if present
    if "multilink" in payload:
        value = payload.get("multilink")
        if value and value not in VALID_BODY_MULTILINK:
            return (
                False,
                f"Invalid multilink '{value}'. Must be one of: {', '.join(VALID_BODY_MULTILINK)}",
            )

    # Validate mrru if present
    if "mrru" in payload:
        value = payload.get("mrru")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 296 or int_val > 65535:
                    return (False, "mrru must be between 296 and 65535")
            except (ValueError, TypeError):
                return (False, f"mrru must be numeric, got: {value}")

    # Validate detected-peer-mtu if present
    if "detected-peer-mtu" in payload:
        value = payload.get("detected-peer-mtu")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "detected-peer-mtu must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"detected-peer-mtu must be numeric, got: {value}",
                )

    # Validate disc-retry-timeout if present
    if "disc-retry-timeout" in payload:
        value = payload.get("disc-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "disc-retry-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"disc-retry-timeout must be numeric, got: {value}",
                )

    # Validate padt-retry-timeout if present
    if "padt-retry-timeout" in payload:
        value = payload.get("padt-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "padt-retry-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"padt-retry-timeout must be numeric, got: {value}",
                )

    # Validate service-name if present
    if "service-name" in payload:
        value = payload.get("service-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "service-name cannot exceed 63 characters")

    # Validate ac-name if present
    if "ac-name" in payload:
        value = payload.get("ac-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ac-name cannot exceed 63 characters")

    # Validate lcp-echo-interval if present
    if "lcp-echo-interval" in payload:
        value = payload.get("lcp-echo-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "lcp-echo-interval must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lcp-echo-interval must be numeric, got: {value}",
                )

    # Validate lcp-max-echo-fails if present
    if "lcp-max-echo-fails" in payload:
        value = payload.get("lcp-max-echo-fails")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "lcp-max-echo-fails must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lcp-max-echo-fails must be numeric, got: {value}",
                )

    # Validate defaultgw if present
    if "defaultgw" in payload:
        value = payload.get("defaultgw")
        if value and value not in VALID_BODY_DEFAULTGW:
            return (
                False,
                f"Invalid defaultgw '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULTGW)}",
            )

    # Validate dns-server-override if present
    if "dns-server-override" in payload:
        value = payload.get("dns-server-override")
        if value and value not in VALID_BODY_DNS_SERVER_OVERRIDE:
            return (
                False,
                f"Invalid dns-server-override '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVER_OVERRIDE)}",
            )

    # Validate dns-server-protocol if present
    if "dns-server-protocol" in payload:
        value = payload.get("dns-server-protocol")
        if value and value not in VALID_BODY_DNS_SERVER_PROTOCOL:
            return (
                False,
                f"Invalid dns-server-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVER_PROTOCOL)}",
            )

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate pptp-client if present
    if "pptp-client" in payload:
        value = payload.get("pptp-client")
        if value and value not in VALID_BODY_PPTP_CLIENT:
            return (
                False,
                f"Invalid pptp-client '{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_CLIENT)}",
            )

    # Validate pptp-user if present
    if "pptp-user" in payload:
        value = payload.get("pptp-user")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "pptp-user cannot exceed 64 characters")

    # Validate pptp-auth-type if present
    if "pptp-auth-type" in payload:
        value = payload.get("pptp-auth-type")
        if value and value not in VALID_BODY_PPTP_AUTH_TYPE:
            return (
                False,
                f"Invalid pptp-auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_AUTH_TYPE)}",
            )

    # Validate pptp-timeout if present
    if "pptp-timeout" in payload:
        value = payload.get("pptp-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "pptp-timeout must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"pptp-timeout must be numeric, got: {value}")

    # Validate arpforward if present
    if "arpforward" in payload:
        value = payload.get("arpforward")
        if value and value not in VALID_BODY_ARPFORWARD:
            return (
                False,
                f"Invalid arpforward '{value}'. Must be one of: {', '.join(VALID_BODY_ARPFORWARD)}",
            )

    # Validate ndiscforward if present
    if "ndiscforward" in payload:
        value = payload.get("ndiscforward")
        if value and value not in VALID_BODY_NDISCFORWARD:
            return (
                False,
                f"Invalid ndiscforward '{value}'. Must be one of: {', '.join(VALID_BODY_NDISCFORWARD)}",
            )

    # Validate broadcast-forward if present
    if "broadcast-forward" in payload:
        value = payload.get("broadcast-forward")
        if value and value not in VALID_BODY_BROADCAST_FORWARD:
            return (
                False,
                f"Invalid broadcast-forward '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_FORWARD)}",
            )

    # Validate bfd if present
    if "bfd" in payload:
        value = payload.get("bfd")
        if value and value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid bfd '{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )

    # Validate bfd-desired-min-tx if present
    if "bfd-desired-min-tx" in payload:
        value = payload.get("bfd-desired-min-tx")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100000:
                    return (
                        False,
                        "bfd-desired-min-tx must be between 1 and 100000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-desired-min-tx must be numeric, got: {value}",
                )

    # Validate bfd-detect-mult if present
    if "bfd-detect-mult" in payload:
        value = payload.get("bfd-detect-mult")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 50:
                    return (False, "bfd-detect-mult must be between 1 and 50")
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-detect-mult must be numeric, got: {value}",
                )

    # Validate bfd-required-min-rx if present
    if "bfd-required-min-rx" in payload:
        value = payload.get("bfd-required-min-rx")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100000:
                    return (
                        False,
                        "bfd-required-min-rx must be between 1 and 100000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-required-min-rx must be numeric, got: {value}",
                )

    # Validate l2forward if present
    if "l2forward" in payload:
        value = payload.get("l2forward")
        if value and value not in VALID_BODY_L2FORWARD:
            return (
                False,
                f"Invalid l2forward '{value}'. Must be one of: {', '.join(VALID_BODY_L2FORWARD)}",
            )

    # Validate icmp-send-redirect if present
    if "icmp-send-redirect" in payload:
        value = payload.get("icmp-send-redirect")
        if value and value not in VALID_BODY_ICMP_SEND_REDIRECT:
            return (
                False,
                f"Invalid icmp-send-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_SEND_REDIRECT)}",
            )

    # Validate icmp-accept-redirect if present
    if "icmp-accept-redirect" in payload:
        value = payload.get("icmp-accept-redirect")
        if value and value not in VALID_BODY_ICMP_ACCEPT_REDIRECT:
            return (
                False,
                f"Invalid icmp-accept-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_ACCEPT_REDIRECT)}",
            )

    # Validate reachable-time if present
    if "reachable-time" in payload:
        value = payload.get("reachable-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30000 or int_val > 3600000:
                    return (
                        False,
                        "reachable-time must be between 30000 and 3600000",
                    )
            except (ValueError, TypeError):
                return (False, f"reachable-time must be numeric, got: {value}")

    # Validate vlanforward if present
    if "vlanforward" in payload:
        value = payload.get("vlanforward")
        if value and value not in VALID_BODY_VLANFORWARD:
            return (
                False,
                f"Invalid vlanforward '{value}'. Must be one of: {', '.join(VALID_BODY_VLANFORWARD)}",
            )

    # Validate stpforward if present
    if "stpforward" in payload:
        value = payload.get("stpforward")
        if value and value not in VALID_BODY_STPFORWARD:
            return (
                False,
                f"Invalid stpforward '{value}'. Must be one of: {', '.join(VALID_BODY_STPFORWARD)}",
            )

    # Validate stpforward-mode if present
    if "stpforward-mode" in payload:
        value = payload.get("stpforward-mode")
        if value and value not in VALID_BODY_STPFORWARD_MODE:
            return (
                False,
                f"Invalid stpforward-mode '{value}'. Must be one of: {', '.join(VALID_BODY_STPFORWARD_MODE)}",
            )

    # Validate ips-sniffer-mode if present
    if "ips-sniffer-mode" in payload:
        value = payload.get("ips-sniffer-mode")
        if value and value not in VALID_BODY_IPS_SNIFFER_MODE:
            return (
                False,
                f"Invalid ips-sniffer-mode '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SNIFFER_MODE)}",
            )

    # Validate ident-accept if present
    if "ident-accept" in payload:
        value = payload.get("ident-accept")
        if value and value not in VALID_BODY_IDENT_ACCEPT:
            return (
                False,
                f"Invalid ident-accept '{value}'. Must be one of: {', '.join(VALID_BODY_IDENT_ACCEPT)}",
            )

    # Validate ipmac if present
    if "ipmac" in payload:
        value = payload.get("ipmac")
        if value and value not in VALID_BODY_IPMAC:
            return (
                False,
                f"Invalid ipmac '{value}'. Must be one of: {', '.join(VALID_BODY_IPMAC)}",
            )

    # Validate subst if present
    if "subst" in payload:
        value = payload.get("subst")
        if value and value not in VALID_BODY_SUBST:
            return (
                False,
                f"Invalid subst '{value}'. Must be one of: {', '.join(VALID_BODY_SUBST)}",
            )

    # Validate speed if present
    if "speed" in payload:
        value = payload.get("speed")
        if value and value not in VALID_BODY_SPEED:
            return (
                False,
                f"Invalid speed '{value}'. Must be one of: {', '.join(VALID_BODY_SPEED)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate netbios-forward if present
    if "netbios-forward" in payload:
        value = payload.get("netbios-forward")
        if value and value not in VALID_BODY_NETBIOS_FORWARD:
            return (
                False,
                f"Invalid netbios-forward '{value}'. Must be one of: {', '.join(VALID_BODY_NETBIOS_FORWARD)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate dedicated-to if present
    if "dedicated-to" in payload:
        value = payload.get("dedicated-to")
        if value and value not in VALID_BODY_DEDICATED_TO:
            return (
                False,
                f"Invalid dedicated-to '{value}'. Must be one of: {', '.join(VALID_BODY_DEDICATED_TO)}",
            )

    # Validate wccp if present
    if "wccp" in payload:
        value = payload.get("wccp")
        if value and value not in VALID_BODY_WCCP:
            return (
                False,
                f"Invalid wccp '{value}'. Must be one of: {', '.join(VALID_BODY_WCCP)}",
            )

    # Validate netflow-sampler if present
    if "netflow-sampler" in payload:
        value = payload.get("netflow-sampler")
        if value and value not in VALID_BODY_NETFLOW_SAMPLER:
            return (
                False,
                f"Invalid netflow-sampler '{value}'. Must be one of: {', '.join(VALID_BODY_NETFLOW_SAMPLER)}",
            )

    # Validate netflow-sample-rate if present
    if "netflow-sample-rate" in payload:
        value = payload.get("netflow-sample-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "netflow-sample-rate must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"netflow-sample-rate must be numeric, got: {value}",
                )

    # Validate netflow-sampler-id if present
    if "netflow-sampler-id" in payload:
        value = payload.get("netflow-sampler-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 254:
                    return (
                        False,
                        "netflow-sampler-id must be between 1 and 254",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"netflow-sampler-id must be numeric, got: {value}",
                )

    # Validate sflow-sampler if present
    if "sflow-sampler" in payload:
        value = payload.get("sflow-sampler")
        if value and value not in VALID_BODY_SFLOW_SAMPLER:
            return (
                False,
                f"Invalid sflow-sampler '{value}'. Must be one of: {', '.join(VALID_BODY_SFLOW_SAMPLER)}",
            )

    # Validate drop-fragment if present
    if "drop-fragment" in payload:
        value = payload.get("drop-fragment")
        if value and value not in VALID_BODY_DROP_FRAGMENT:
            return (
                False,
                f"Invalid drop-fragment '{value}'. Must be one of: {', '.join(VALID_BODY_DROP_FRAGMENT)}",
            )

    # Validate src-check if present
    if "src-check" in payload:
        value = payload.get("src-check")
        if value and value not in VALID_BODY_SRC_CHECK:
            return (
                False,
                f"Invalid src-check '{value}'. Must be one of: {', '.join(VALID_BODY_SRC_CHECK)}",
            )

    # Validate sample-rate if present
    if "sample-rate" in payload:
        value = payload.get("sample-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 99999:
                    return (False, "sample-rate must be between 10 and 99999")
            except (ValueError, TypeError):
                return (False, f"sample-rate must be numeric, got: {value}")

    # Validate polling-interval if present
    if "polling-interval" in payload:
        value = payload.get("polling-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "polling-interval must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"polling-interval must be numeric, got: {value}",
                )

    # Validate sample-direction if present
    if "sample-direction" in payload:
        value = payload.get("sample-direction")
        if value and value not in VALID_BODY_SAMPLE_DIRECTION:
            return (
                False,
                f"Invalid sample-direction '{value}'. Must be one of: {', '.join(VALID_BODY_SAMPLE_DIRECTION)}",
            )

    # Validate explicit-web-proxy if present
    if "explicit-web-proxy" in payload:
        value = payload.get("explicit-web-proxy")
        if value and value not in VALID_BODY_EXPLICIT_WEB_PROXY:
            return (
                False,
                f"Invalid explicit-web-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_EXPLICIT_WEB_PROXY)}",
            )

    # Validate explicit-ftp-proxy if present
    if "explicit-ftp-proxy" in payload:
        value = payload.get("explicit-ftp-proxy")
        if value and value not in VALID_BODY_EXPLICIT_FTP_PROXY:
            return (
                False,
                f"Invalid explicit-ftp-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_EXPLICIT_FTP_PROXY)}",
            )

    # Validate proxy-captive-portal if present
    if "proxy-captive-portal" in payload:
        value = payload.get("proxy-captive-portal")
        if value and value not in VALID_BODY_PROXY_CAPTIVE_PORTAL:
            return (
                False,
                f"Invalid proxy-captive-portal '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_CAPTIVE_PORTAL)}",
            )

    # Validate tcp-mss if present
    if "tcp-mss" in payload:
        value = payload.get("tcp-mss")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 48 or int_val > 65535:
                    return (False, "tcp-mss must be between 48 and 65535")
            except (ValueError, TypeError):
                return (False, f"tcp-mss must be numeric, got: {value}")

    # Validate inbandwidth if present
    if "inbandwidth" in payload:
        value = payload.get("inbandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "inbandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (False, f"inbandwidth must be numeric, got: {value}")

    # Validate outbandwidth if present
    if "outbandwidth" in payload:
        value = payload.get("outbandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "outbandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (False, f"outbandwidth must be numeric, got: {value}")

    # Validate egress-shaping-profile if present
    if "egress-shaping-profile" in payload:
        value = payload.get("egress-shaping-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "egress-shaping-profile cannot exceed 35 characters",
            )

    # Validate ingress-shaping-profile if present
    if "ingress-shaping-profile" in payload:
        value = payload.get("ingress-shaping-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "ingress-shaping-profile cannot exceed 35 characters",
            )

    # Validate spillover-threshold if present
    if "spillover-threshold" in payload:
        value = payload.get("spillover-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "spillover-threshold must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spillover-threshold must be numeric, got: {value}",
                )

    # Validate ingress-spillover-threshold if present
    if "ingress-spillover-threshold" in payload:
        value = payload.get("ingress-spillover-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "ingress-spillover-threshold must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ingress-spillover-threshold must be numeric, got: {value}",
                )

    # Validate weight if present
    if "weight" in payload:
        value = payload.get("weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "weight must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"weight must be numeric, got: {value}")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate external if present
    if "external" in payload:
        value = payload.get("external")
        if value and value not in VALID_BODY_EXTERNAL:
            return (
                False,
                f"Invalid external '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL)}",
            )

    # Validate mtu-override if present
    if "mtu-override" in payload:
        value = payload.get("mtu-override")
        if value and value not in VALID_BODY_MTU_OVERRIDE:
            return (
                False,
                f"Invalid mtu-override '{value}'. Must be one of: {', '.join(VALID_BODY_MTU_OVERRIDE)}",
            )

    # Validate mtu if present
    if "mtu" in payload:
        value = payload.get("mtu")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "mtu must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"mtu must be numeric, got: {value}")

    # Validate vlan-protocol if present
    if "vlan-protocol" in payload:
        value = payload.get("vlan-protocol")
        if value and value not in VALID_BODY_VLAN_PROTOCOL:
            return (
                False,
                f"Invalid vlan-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_PROTOCOL)}",
            )

    # Validate vlanid if present
    if "vlanid" in payload:
        value = payload.get("vlanid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4094:
                    return (False, "vlanid must be between 1 and 4094")
            except (ValueError, TypeError):
                return (False, f"vlanid must be numeric, got: {value}")

    # Validate trunk if present
    if "trunk" in payload:
        value = payload.get("trunk")
        if value and value not in VALID_BODY_TRUNK:
            return (
                False,
                f"Invalid trunk '{value}'. Must be one of: {', '.join(VALID_BODY_TRUNK)}",
            )

    # Validate forward-domain if present
    if "forward-domain" in payload:
        value = payload.get("forward-domain")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "forward-domain must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"forward-domain must be numeric, got: {value}")

    # Validate lacp-mode if present
    if "lacp-mode" in payload:
        value = payload.get("lacp-mode")
        if value and value not in VALID_BODY_LACP_MODE:
            return (
                False,
                f"Invalid lacp-mode '{value}'. Must be one of: {', '.join(VALID_BODY_LACP_MODE)}",
            )

    # Validate lacp-ha-secondary if present
    if "lacp-ha-secondary" in payload:
        value = payload.get("lacp-ha-secondary")
        if value and value not in VALID_BODY_LACP_HA_SECONDARY:
            return (
                False,
                f"Invalid lacp-ha-secondary '{value}'. Must be one of: {', '.join(VALID_BODY_LACP_HA_SECONDARY)}",
            )

    # Validate system-id-type if present
    if "system-id-type" in payload:
        value = payload.get("system-id-type")
        if value and value not in VALID_BODY_SYSTEM_ID_TYPE:
            return (
                False,
                f"Invalid system-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_ID_TYPE)}",
            )

    # Validate lacp-speed if present
    if "lacp-speed" in payload:
        value = payload.get("lacp-speed")
        if value and value not in VALID_BODY_LACP_SPEED:
            return (
                False,
                f"Invalid lacp-speed '{value}'. Must be one of: {', '.join(VALID_BODY_LACP_SPEED)}",
            )

    # Validate min-links if present
    if "min-links" in payload:
        value = payload.get("min-links")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 32:
                    return (False, "min-links must be between 1 and 32")
            except (ValueError, TypeError):
                return (False, f"min-links must be numeric, got: {value}")

    # Validate min-links-down if present
    if "min-links-down" in payload:
        value = payload.get("min-links-down")
        if value and value not in VALID_BODY_MIN_LINKS_DOWN:
            return (
                False,
                f"Invalid min-links-down '{value}'. Must be one of: {', '.join(VALID_BODY_MIN_LINKS_DOWN)}",
            )

    # Validate algorithm if present
    if "algorithm" in payload:
        value = payload.get("algorithm")
        if value and value not in VALID_BODY_ALGORITHM:
            return (
                False,
                f"Invalid algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_ALGORITHM)}",
            )

    # Validate link-up-delay if present
    if "link-up-delay" in payload:
        value = payload.get("link-up-delay")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 50 or int_val > 3600000:
                    return (
                        False,
                        "link-up-delay must be between 50 and 3600000",
                    )
            except (ValueError, TypeError):
                return (False, f"link-up-delay must be numeric, got: {value}")

    # Validate aggregate-type if present
    if "aggregate-type" in payload:
        value = payload.get("aggregate-type")
        if value and value not in VALID_BODY_AGGREGATE_TYPE:
            return (
                False,
                f"Invalid aggregate-type '{value}'. Must be one of: {', '.join(VALID_BODY_AGGREGATE_TYPE)}",
            )

    # Validate priority-override if present
    if "priority-override" in payload:
        value = payload.get("priority-override")
        if value and value not in VALID_BODY_PRIORITY_OVERRIDE:
            return (
                False,
                f"Invalid priority-override '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_OVERRIDE)}",
            )

    # Validate aggregate if present
    if "aggregate" in payload:
        value = payload.get("aggregate")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "aggregate cannot exceed 15 characters")

    # Validate redundant-interface if present
    if "redundant-interface" in payload:
        value = payload.get("redundant-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "redundant-interface cannot exceed 15 characters")

    # Validate devindex if present
    if "devindex" in payload:
        value = payload.get("devindex")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "devindex must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"devindex must be numeric, got: {value}")

    # Validate vindex if present
    if "vindex" in payload:
        value = payload.get("vindex")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "vindex must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"vindex must be numeric, got: {value}")

    # Validate switch if present
    if "switch" in payload:
        value = payload.get("switch")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "switch cannot exceed 15 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate alias if present
    if "alias" in payload:
        value = payload.get("alias")
        if value and isinstance(value, str) and len(value) > 25:
            return (False, "alias cannot exceed 25 characters")

    # Validate l2tp-client if present
    if "l2tp-client" in payload:
        value = payload.get("l2tp-client")
        if value and value not in VALID_BODY_L2TP_CLIENT:
            return (
                False,
                f"Invalid l2tp-client '{value}'. Must be one of: {', '.join(VALID_BODY_L2TP_CLIENT)}",
            )

    # Validate security-mode if present
    if "security-mode" in payload:
        value = payload.get("security-mode")
        if value and value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid security-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
            )

    # Validate security-mac-auth-bypass if present
    if "security-mac-auth-bypass" in payload:
        value = payload.get("security-mac-auth-bypass")
        if value and value not in VALID_BODY_SECURITY_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid security-mac-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MAC_AUTH_BYPASS)}",
            )

    # Validate security-ip-auth-bypass if present
    if "security-ip-auth-bypass" in payload:
        value = payload.get("security-ip-auth-bypass")
        if value and value not in VALID_BODY_SECURITY_IP_AUTH_BYPASS:
            return (
                False,
                f"Invalid security-ip-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_IP_AUTH_BYPASS)}",
            )

    # Validate security-8021x-mode if present
    if "security-8021x-mode" in payload:
        value = payload.get("security-8021x-mode")
        if value and value not in VALID_BODY_SECURITY_8021X_MODE:
            return (
                False,
                f"Invalid security-8021x-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_8021X_MODE)}",
            )

    # Validate security-8021x-master if present
    if "security-8021x-master" in payload:
        value = payload.get("security-8021x-master")
        if value and isinstance(value, str) and len(value) > 15:
            return (
                False,
                "security-8021x-master cannot exceed 15 characters",
            )

    # Validate security-8021x-dynamic-vlan-id if present
    if "security-8021x-dynamic-vlan-id" in payload:
        value = payload.get("security-8021x-dynamic-vlan-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4094:
                    return (
                        False,
                        "security-8021x-dynamic-vlan-id must be between 0 and 4094",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"security-8021x-dynamic-vlan-id must be numeric, got: {value}",
                )

    # Validate security-8021x-member-mode if present
    if "security-8021x-member-mode" in payload:
        value = payload.get("security-8021x-member-mode")
        if value and value not in VALID_BODY_SECURITY_8021X_MEMBER_MODE:
            return (
                False,
                f"Invalid security-8021x-member-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_8021X_MEMBER_MODE)}",
            )

    # Validate security-external-web if present
    if "security-external-web" in payload:
        value = payload.get("security-external-web")
        if value and isinstance(value, str) and len(value) > 1023:
            return (
                False,
                "security-external-web cannot exceed 1023 characters",
            )

    # Validate security-external-logout if present
    if "security-external-logout" in payload:
        value = payload.get("security-external-logout")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "security-external-logout cannot exceed 127 characters",
            )

    # Validate replacemsg-override-group if present
    if "replacemsg-override-group" in payload:
        value = payload.get("replacemsg-override-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "replacemsg-override-group cannot exceed 35 characters",
            )

    # Validate security-redirect-url if present
    if "security-redirect-url" in payload:
        value = payload.get("security-redirect-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (
                False,
                "security-redirect-url cannot exceed 1023 characters",
            )

    # Validate auth-cert if present
    if "auth-cert" in payload:
        value = payload.get("auth-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-cert cannot exceed 35 characters")

    # Validate auth-portal-addr if present
    if "auth-portal-addr" in payload:
        value = payload.get("auth-portal-addr")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auth-portal-addr cannot exceed 63 characters")

    # Validate security-exempt-list if present
    if "security-exempt-list" in payload:
        value = payload.get("security-exempt-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "security-exempt-list cannot exceed 35 characters")

    # Validate ike-saml-server if present
    if "ike-saml-server" in payload:
        value = payload.get("ike-saml-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ike-saml-server cannot exceed 35 characters")

    # Validate stp if present
    if "stp" in payload:
        value = payload.get("stp")
        if value and value not in VALID_BODY_STP:
            return (
                False,
                f"Invalid stp '{value}'. Must be one of: {', '.join(VALID_BODY_STP)}",
            )

    # Validate stp-ha-secondary if present
    if "stp-ha-secondary" in payload:
        value = payload.get("stp-ha-secondary")
        if value and value not in VALID_BODY_STP_HA_SECONDARY:
            return (
                False,
                f"Invalid stp-ha-secondary '{value}'. Must be one of: {', '.join(VALID_BODY_STP_HA_SECONDARY)}",
            )

    # Validate stp-edge if present
    if "stp-edge" in payload:
        value = payload.get("stp-edge")
        if value and value not in VALID_BODY_STP_EDGE:
            return (
                False,
                f"Invalid stp-edge '{value}'. Must be one of: {', '.join(VALID_BODY_STP_EDGE)}",
            )

    # Validate device-identification if present
    if "device-identification" in payload:
        value = payload.get("device-identification")
        if value and value not in VALID_BODY_DEVICE_IDENTIFICATION:
            return (
                False,
                f"Invalid device-identification '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_IDENTIFICATION)}",
            )

    # Validate exclude-signatures if present
    if "exclude-signatures" in payload:
        value = payload.get("exclude-signatures")
        if value and value not in VALID_BODY_EXCLUDE_SIGNATURES:
            return (
                False,
                f"Invalid exclude-signatures '{value}'. Must be one of: {', '.join(VALID_BODY_EXCLUDE_SIGNATURES)}",
            )

    # Validate device-user-identification if present
    if "device-user-identification" in payload:
        value = payload.get("device-user-identification")
        if value and value not in VALID_BODY_DEVICE_USER_IDENTIFICATION:
            return (
                False,
                f"Invalid device-user-identification '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_USER_IDENTIFICATION)}",
            )

    # Validate lldp-reception if present
    if "lldp-reception" in payload:
        value = payload.get("lldp-reception")
        if value and value not in VALID_BODY_LLDP_RECEPTION:
            return (
                False,
                f"Invalid lldp-reception '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_RECEPTION)}",
            )

    # Validate lldp-transmission if present
    if "lldp-transmission" in payload:
        value = payload.get("lldp-transmission")
        if value and value not in VALID_BODY_LLDP_TRANSMISSION:
            return (
                False,
                f"Invalid lldp-transmission '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_TRANSMISSION)}",
            )

    # Validate lldp-network-policy if present
    if "lldp-network-policy" in payload:
        value = payload.get("lldp-network-policy")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "lldp-network-policy cannot exceed 35 characters")

    # Validate estimated-upstream-bandwidth if present
    if "estimated-upstream-bandwidth" in payload:
        value = payload.get("estimated-upstream-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "estimated-upstream-bandwidth must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"estimated-upstream-bandwidth must be numeric, got: {value}",
                )

    # Validate estimated-downstream-bandwidth if present
    if "estimated-downstream-bandwidth" in payload:
        value = payload.get("estimated-downstream-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "estimated-downstream-bandwidth must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"estimated-downstream-bandwidth must be numeric, got: {value}",
                )

    # Validate measured-upstream-bandwidth if present
    if "measured-upstream-bandwidth" in payload:
        value = payload.get("measured-upstream-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "measured-upstream-bandwidth must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"measured-upstream-bandwidth must be numeric, got: {value}",
                )

    # Validate measured-downstream-bandwidth if present
    if "measured-downstream-bandwidth" in payload:
        value = payload.get("measured-downstream-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "measured-downstream-bandwidth must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"measured-downstream-bandwidth must be numeric, got: {value}",
                )

    # Validate bandwidth-measure-time if present
    if "bandwidth-measure-time" in payload:
        value = payload.get("bandwidth-measure-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "bandwidth-measure-time must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bandwidth-measure-time must be numeric, got: {value}",
                )

    # Validate monitor-bandwidth if present
    if "monitor-bandwidth" in payload:
        value = payload.get("monitor-bandwidth")
        if value and value not in VALID_BODY_MONITOR_BANDWIDTH:
            return (
                False,
                f"Invalid monitor-bandwidth '{value}'. Must be one of: {', '.join(VALID_BODY_MONITOR_BANDWIDTH)}",
            )

    # Validate vrrp-virtual-mac if present
    if "vrrp-virtual-mac" in payload:
        value = payload.get("vrrp-virtual-mac")
        if value and value not in VALID_BODY_VRRP_VIRTUAL_MAC:
            return (
                False,
                f"Invalid vrrp-virtual-mac '{value}'. Must be one of: {', '.join(VALID_BODY_VRRP_VIRTUAL_MAC)}",
            )

    # Validate role if present
    if "role" in payload:
        value = payload.get("role")
        if value and value not in VALID_BODY_ROLE:
            return (
                False,
                f"Invalid role '{value}'. Must be one of: {', '.join(VALID_BODY_ROLE)}",
            )

    # Validate snmp-index if present
    if "snmp-index" in payload:
        value = payload.get("snmp-index")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "snmp-index must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"snmp-index must be numeric, got: {value}")

    # Validate secondary-IP if present
    if "secondary-IP" in payload:
        value = payload.get("secondary-IP")
        if value and value not in VALID_BODY_SECONDARY_IP:
            return (
                False,
                f"Invalid secondary-IP '{value}'. Must be one of: {', '.join(VALID_BODY_SECONDARY_IP)}",
            )

    # Validate preserve-session-route if present
    if "preserve-session-route" in payload:
        value = payload.get("preserve-session-route")
        if value and value not in VALID_BODY_PRESERVE_SESSION_ROUTE:
            return (
                False,
                f"Invalid preserve-session-route '{value}'. Must be one of: {', '.join(VALID_BODY_PRESERVE_SESSION_ROUTE)}",
            )

    # Validate auto-auth-extension-device if present
    if "auto-auth-extension-device" in payload:
        value = payload.get("auto-auth-extension-device")
        if value and value not in VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE:
            return (
                False,
                f"Invalid auto-auth-extension-device '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE)}",
            )

    # Validate ap-discover if present
    if "ap-discover" in payload:
        value = payload.get("ap-discover")
        if value and value not in VALID_BODY_AP_DISCOVER:
            return (
                False,
                f"Invalid ap-discover '{value}'. Must be one of: {', '.join(VALID_BODY_AP_DISCOVER)}",
            )

    # Validate fortilink-neighbor-detect if present
    if "fortilink-neighbor-detect" in payload:
        value = payload.get("fortilink-neighbor-detect")
        if value and value not in VALID_BODY_FORTILINK_NEIGHBOR_DETECT:
            return (
                False,
                f"Invalid fortilink-neighbor-detect '{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK_NEIGHBOR_DETECT)}",
            )

    # Validate ip-managed-by-fortiipam if present
    if "ip-managed-by-fortiipam" in payload:
        value = payload.get("ip-managed-by-fortiipam")
        if value and value not in VALID_BODY_IP_MANAGED_BY_FORTIIPAM:
            return (
                False,
                f"Invalid ip-managed-by-fortiipam '{value}'. Must be one of: {', '.join(VALID_BODY_IP_MANAGED_BY_FORTIIPAM)}",
            )

    # Validate managed-subnetwork-size if present
    if "managed-subnetwork-size" in payload:
        value = payload.get("managed-subnetwork-size")
        if value and value not in VALID_BODY_MANAGED_SUBNETWORK_SIZE:
            return (
                False,
                f"Invalid managed-subnetwork-size '{value}'. Must be one of: {', '.join(VALID_BODY_MANAGED_SUBNETWORK_SIZE)}",
            )

    # Validate fortilink-split-interface if present
    if "fortilink-split-interface" in payload:
        value = payload.get("fortilink-split-interface")
        if value and value not in VALID_BODY_FORTILINK_SPLIT_INTERFACE:
            return (
                False,
                f"Invalid fortilink-split-interface '{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK_SPLIT_INTERFACE)}",
            )

    # Validate internal if present
    if "internal" in payload:
        value = payload.get("internal")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "internal must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"internal must be numeric, got: {value}")

    # Validate fortilink-backup-link if present
    if "fortilink-backup-link" in payload:
        value = payload.get("fortilink-backup-link")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "fortilink-backup-link must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fortilink-backup-link must be numeric, got: {value}",
                )

    # Validate switch-controller-access-vlan if present
    if "switch-controller-access-vlan" in payload:
        value = payload.get("switch-controller-access-vlan")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN:
            return (
                False,
                f"Invalid switch-controller-access-vlan '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN)}",
            )

    # Validate switch-controller-traffic-policy if present
    if "switch-controller-traffic-policy" in payload:
        value = payload.get("switch-controller-traffic-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "switch-controller-traffic-policy cannot exceed 63 characters",
            )

    # Validate switch-controller-rspan-mode if present
    if "switch-controller-rspan-mode" in payload:
        value = payload.get("switch-controller-rspan-mode")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE:
            return (
                False,
                f"Invalid switch-controller-rspan-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE)}",
            )

    # Validate switch-controller-netflow-collect if present
    if "switch-controller-netflow-collect" in payload:
        value = payload.get("switch-controller-netflow-collect")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT:
            return (
                False,
                f"Invalid switch-controller-netflow-collect '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT)}",
            )

    # Validate switch-controller-mgmt-vlan if present
    if "switch-controller-mgmt-vlan" in payload:
        value = payload.get("switch-controller-mgmt-vlan")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4094:
                    return (
                        False,
                        "switch-controller-mgmt-vlan must be between 1 and 4094",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"switch-controller-mgmt-vlan must be numeric, got: {value}",
                )

    # Validate switch-controller-igmp-snooping if present
    if "switch-controller-igmp-snooping" in payload:
        value = payload.get("switch-controller-igmp-snooping")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING:
            return (
                False,
                f"Invalid switch-controller-igmp-snooping '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING)}",
            )

    # Validate switch-controller-igmp-snooping-proxy if present
    if "switch-controller-igmp-snooping-proxy" in payload:
        value = payload.get("switch-controller-igmp-snooping-proxy")
        if (
            value
            and value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY
        ):
            return (
                False,
                f"Invalid switch-controller-igmp-snooping-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY)}",
            )

    # Validate switch-controller-igmp-snooping-fast-leave if present
    if "switch-controller-igmp-snooping-fast-leave" in payload:
        value = payload.get("switch-controller-igmp-snooping-fast-leave")
        if (
            value
            and value
            not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE
        ):
            return (
                False,
                f"Invalid switch-controller-igmp-snooping-fast-leave '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE)}",
            )

    # Validate switch-controller-dhcp-snooping if present
    if "switch-controller-dhcp-snooping" in payload:
        value = payload.get("switch-controller-dhcp-snooping")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING:
            return (
                False,
                f"Invalid switch-controller-dhcp-snooping '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING)}",
            )

    # Validate switch-controller-dhcp-snooping-verify-mac if present
    if "switch-controller-dhcp-snooping-verify-mac" in payload:
        value = payload.get("switch-controller-dhcp-snooping-verify-mac")
        if (
            value
            and value
            not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC
        ):
            return (
                False,
                f"Invalid switch-controller-dhcp-snooping-verify-mac '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC)}",
            )

    # Validate switch-controller-dhcp-snooping-option82 if present
    if "switch-controller-dhcp-snooping-option82" in payload:
        value = payload.get("switch-controller-dhcp-snooping-option82")
        if (
            value
            and value
            not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82
        ):
            return (
                False,
                f"Invalid switch-controller-dhcp-snooping-option82 '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82)}",
            )

    # Validate switch-controller-arp-inspection if present
    if "switch-controller-arp-inspection" in payload:
        value = payload.get("switch-controller-arp-inspection")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION:
            return (
                False,
                f"Invalid switch-controller-arp-inspection '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION)}",
            )

    # Validate switch-controller-learning-limit if present
    if "switch-controller-learning-limit" in payload:
        value = payload.get("switch-controller-learning-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "switch-controller-learning-limit must be between 0 and 128",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"switch-controller-learning-limit must be numeric, got: {value}",
                )

    # Validate switch-controller-nac if present
    if "switch-controller-nac" in payload:
        value = payload.get("switch-controller-nac")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "switch-controller-nac cannot exceed 35 characters",
            )

    # Validate switch-controller-dynamic if present
    if "switch-controller-dynamic" in payload:
        value = payload.get("switch-controller-dynamic")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "switch-controller-dynamic cannot exceed 35 characters",
            )

    # Validate switch-controller-feature if present
    if "switch-controller-feature" in payload:
        value = payload.get("switch-controller-feature")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_FEATURE:
            return (
                False,
                f"Invalid switch-controller-feature '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_FEATURE)}",
            )

    # Validate switch-controller-iot-scanning if present
    if "switch-controller-iot-scanning" in payload:
        value = payload.get("switch-controller-iot-scanning")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING:
            return (
                False,
                f"Invalid switch-controller-iot-scanning '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING)}",
            )

    # Validate switch-controller-offload if present
    if "switch-controller-offload" in payload:
        value = payload.get("switch-controller-offload")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD:
            return (
                False,
                f"Invalid switch-controller-offload '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_OFFLOAD)}",
            )

    # Validate switch-controller-offload-gw if present
    if "switch-controller-offload-gw" in payload:
        value = payload.get("switch-controller-offload-gw")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW:
            return (
                False,
                f"Invalid switch-controller-offload-gw '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW)}",
            )

    # Validate swc-vlan if present
    if "swc-vlan" in payload:
        value = payload.get("swc-vlan")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "swc-vlan must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"swc-vlan must be numeric, got: {value}")

    # Validate swc-first-create if present
    if "swc-first-create" in payload:
        value = payload.get("swc-first-create")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "swc-first-create must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"swc-first-create must be numeric, got: {value}",
                )

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    # Validate eap-supplicant if present
    if "eap-supplicant" in payload:
        value = payload.get("eap-supplicant")
        if value and value not in VALID_BODY_EAP_SUPPLICANT:
            return (
                False,
                f"Invalid eap-supplicant '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_SUPPLICANT)}",
            )

    # Validate eap-method if present
    if "eap-method" in payload:
        value = payload.get("eap-method")
        if value and value not in VALID_BODY_EAP_METHOD:
            return (
                False,
                f"Invalid eap-method '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_METHOD)}",
            )

    # Validate eap-identity if present
    if "eap-identity" in payload:
        value = payload.get("eap-identity")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "eap-identity cannot exceed 35 characters")

    # Validate eap-ca-cert if present
    if "eap-ca-cert" in payload:
        value = payload.get("eap-ca-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "eap-ca-cert cannot exceed 79 characters")

    # Validate eap-user-cert if present
    if "eap-user-cert" in payload:
        value = payload.get("eap-user-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "eap-user-cert cannot exceed 35 characters")

    # Validate default-purdue-level if present
    if "default-purdue-level" in payload:
        value = payload.get("default-purdue-level")
        if value and value not in VALID_BODY_DEFAULT_PURDUE_LEVEL:
            return (
                False,
                f"Invalid default-purdue-level '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_PURDUE_LEVEL)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_interface_put(
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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate vrf if present
    if "vr" in payload:
        value = payload.get("vr")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf must be numeric, got: {value}")

    # Validate cli-conn-status if present
    if "cli-conn-status" in payload:
        value = payload.get("cli-conn-status")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "cli-conn-status must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cli-conn-status must be numeric, got: {value}",
                )

    # Validate fortilink if present
    if "fortilink" in payload:
        value = payload.get("fortilink")
        if value and value not in VALID_BODY_FORTILINK:
            return (
                False,
                f"Invalid fortilink '{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK)}",
            )

    # Validate switch-controller-source-ip if present
    if "switch-controller-source-ip" in payload:
        value = payload.get("switch-controller-source-ip")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP:
            return (
                False,
                f"Invalid switch-controller-source-ip '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_SOURCE_IP)}",
            )

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate distance if present
    if "distance" in payload:
        value = payload.get("distance")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "distance must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"distance must be numeric, got: {value}")

    # Validate priority if present
    if "priority" in payload:
        value = payload.get("priority")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "priority must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"priority must be numeric, got: {value}")

    # Validate dhcp-relay-interface-select-method if present
    if "dhcp-relay-interface-select-method" in payload:
        value = payload.get("dhcp-relay-interface-select-method")
        if (
            value
            and value not in VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD
        ):
            return (
                False,
                f"Invalid dhcp-relay-interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate dhcp-relay-interface if present
    if "dhcp-relay-interface" in payload:
        value = payload.get("dhcp-relay-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "dhcp-relay-interface cannot exceed 15 characters")

    # Validate dhcp-relay-vrf-select if present
    if "dhcp-relay-vrf-select" in payload:
        value = payload.get("dhcp-relay-vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (
                        False,
                        "dhcp-relay-vrf-select must be between 0 and 511",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-relay-vrf-select must be numeric, got: {value}",
                )

    # Validate dhcp-broadcast-flag if present
    if "dhcp-broadcast-flag" in payload:
        value = payload.get("dhcp-broadcast-flag")
        if value and value not in VALID_BODY_DHCP_BROADCAST_FLAG:
            return (
                False,
                f"Invalid dhcp-broadcast-flag '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_BROADCAST_FLAG)}",
            )

    # Validate dhcp-relay-service if present
    if "dhcp-relay-service" in payload:
        value = payload.get("dhcp-relay-service")
        if value and value not in VALID_BODY_DHCP_RELAY_SERVICE:
            return (
                False,
                f"Invalid dhcp-relay-service '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_SERVICE)}",
            )

    # Validate dhcp-relay-circuit-id if present
    if "dhcp-relay-circuit-id" in payload:
        value = payload.get("dhcp-relay-circuit-id")
        if value and isinstance(value, str) and len(value) > 64:
            return (
                False,
                "dhcp-relay-circuit-id cannot exceed 64 characters",
            )

    # Validate dhcp-relay-request-all-server if present
    if "dhcp-relay-request-all-server" in payload:
        value = payload.get("dhcp-relay-request-all-server")
        if value and value not in VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER:
            return (
                False,
                f"Invalid dhcp-relay-request-all-server '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_REQUEST_ALL_SERVER)}",
            )

    # Validate dhcp-relay-allow-no-end-option if present
    if "dhcp-relay-allow-no-end-option" in payload:
        value = payload.get("dhcp-relay-allow-no-end-option")
        if value and value not in VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION:
            return (
                False,
                f"Invalid dhcp-relay-allow-no-end-option '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_ALLOW_NO_END_OPTION)}",
            )

    # Validate dhcp-relay-type if present
    if "dhcp-relay-type" in payload:
        value = payload.get("dhcp-relay-type")
        if value and value not in VALID_BODY_DHCP_RELAY_TYPE:
            return (
                False,
                f"Invalid dhcp-relay-type '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_TYPE)}",
            )

    # Validate dhcp-smart-relay if present
    if "dhcp-smart-relay" in payload:
        value = payload.get("dhcp-smart-relay")
        if value and value not in VALID_BODY_DHCP_SMART_RELAY:
            return (
                False,
                f"Invalid dhcp-smart-relay '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SMART_RELAY)}",
            )

    # Validate dhcp-relay-agent-option if present
    if "dhcp-relay-agent-option" in payload:
        value = payload.get("dhcp-relay-agent-option")
        if value and value not in VALID_BODY_DHCP_RELAY_AGENT_OPTION:
            return (
                False,
                f"Invalid dhcp-relay-agent-option '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_RELAY_AGENT_OPTION)}",
            )

    # Validate dhcp-classless-route-addition if present
    if "dhcp-classless-route-addition" in payload:
        value = payload.get("dhcp-classless-route-addition")
        if value and value not in VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION:
            return (
                False,
                f"Invalid dhcp-classless-route-addition '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_CLASSLESS_ROUTE_ADDITION)}",
            )

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    # Validate gwdetect if present
    if "gwdetect" in payload:
        value = payload.get("gwdetect")
        if value and value not in VALID_BODY_GWDETECT:
            return (
                False,
                f"Invalid gwdetect '{value}'. Must be one of: {', '.join(VALID_BODY_GWDETECT)}",
            )

    # Validate ping-serv-status if present
    if "ping-serv-status" in payload:
        value = payload.get("ping-serv-status")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "ping-serv-status must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ping-serv-status must be numeric, got: {value}",
                )

    # Validate detectprotocol if present
    if "detectprotocol" in payload:
        value = payload.get("detectprotocol")
        if value and value not in VALID_BODY_DETECTPROTOCOL:
            return (
                False,
                f"Invalid detectprotocol '{value}'. Must be one of: {', '.join(VALID_BODY_DETECTPROTOCOL)}",
            )

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

    # Validate fail-detect if present
    if "fail-detect" in payload:
        value = payload.get("fail-detect")
        if value and value not in VALID_BODY_FAIL_DETECT:
            return (
                False,
                f"Invalid fail-detect '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_DETECT)}",
            )

    # Validate fail-detect-option if present
    if "fail-detect-option" in payload:
        value = payload.get("fail-detect-option")
        if value and value not in VALID_BODY_FAIL_DETECT_OPTION:
            return (
                False,
                f"Invalid fail-detect-option '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_DETECT_OPTION)}",
            )

    # Validate fail-alert-method if present
    if "fail-alert-method" in payload:
        value = payload.get("fail-alert-method")
        if value and value not in VALID_BODY_FAIL_ALERT_METHOD:
            return (
                False,
                f"Invalid fail-alert-method '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_ALERT_METHOD)}",
            )

    # Validate fail-action-on-extender if present
    if "fail-action-on-extender" in payload:
        value = payload.get("fail-action-on-extender")
        if value and value not in VALID_BODY_FAIL_ACTION_ON_EXTENDER:
            return (
                False,
                f"Invalid fail-action-on-extender '{value}'. Must be one of: {', '.join(VALID_BODY_FAIL_ACTION_ON_EXTENDER)}",
            )

    # Validate dhcp-client-identifier if present
    if "dhcp-client-identifier" in payload:
        value = payload.get("dhcp-client-identifier")
        if value and isinstance(value, str) and len(value) > 48:
            return (
                False,
                "dhcp-client-identifier cannot exceed 48 characters",
            )

    # Validate dhcp-renew-time if present
    if "dhcp-renew-time" in payload:
        value = payload.get("dhcp-renew-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 604800:
                    return (
                        False,
                        "dhcp-renew-time must be between 300 and 604800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-renew-time must be numeric, got: {value}",
                )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate pppoe-egress-cos if present
    if "pppoe-egress-cos" in payload:
        value = payload.get("pppoe-egress-cos")
        if value and value not in VALID_BODY_PPPOE_EGRESS_COS:
            return (
                False,
                f"Invalid pppoe-egress-cos '{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_EGRESS_COS)}",
            )

    # Validate pppoe-unnumbered-negotiate if present
    if "pppoe-unnumbered-negotiate" in payload:
        value = payload.get("pppoe-unnumbered-negotiate")
        if value and value not in VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE:
            return (
                False,
                f"Invalid pppoe-unnumbered-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE)}",
            )

    # Validate idle-timeout if present
    if "idle-timeout" in payload:
        value = payload.get("idle-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (False, "idle-timeout must be between 0 and 32767")
            except (ValueError, TypeError):
                return (False, f"idle-timeout must be numeric, got: {value}")

    # Validate multilink if present
    if "multilink" in payload:
        value = payload.get("multilink")
        if value and value not in VALID_BODY_MULTILINK:
            return (
                False,
                f"Invalid multilink '{value}'. Must be one of: {', '.join(VALID_BODY_MULTILINK)}",
            )

    # Validate mrru if present
    if "mrru" in payload:
        value = payload.get("mrru")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 296 or int_val > 65535:
                    return (False, "mrru must be between 296 and 65535")
            except (ValueError, TypeError):
                return (False, f"mrru must be numeric, got: {value}")

    # Validate detected-peer-mtu if present
    if "detected-peer-mtu" in payload:
        value = payload.get("detected-peer-mtu")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "detected-peer-mtu must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"detected-peer-mtu must be numeric, got: {value}",
                )

    # Validate disc-retry-timeout if present
    if "disc-retry-timeout" in payload:
        value = payload.get("disc-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "disc-retry-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"disc-retry-timeout must be numeric, got: {value}",
                )

    # Validate padt-retry-timeout if present
    if "padt-retry-timeout" in payload:
        value = payload.get("padt-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "padt-retry-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"padt-retry-timeout must be numeric, got: {value}",
                )

    # Validate service-name if present
    if "service-name" in payload:
        value = payload.get("service-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "service-name cannot exceed 63 characters")

    # Validate ac-name if present
    if "ac-name" in payload:
        value = payload.get("ac-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ac-name cannot exceed 63 characters")

    # Validate lcp-echo-interval if present
    if "lcp-echo-interval" in payload:
        value = payload.get("lcp-echo-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "lcp-echo-interval must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lcp-echo-interval must be numeric, got: {value}",
                )

    # Validate lcp-max-echo-fails if present
    if "lcp-max-echo-fails" in payload:
        value = payload.get("lcp-max-echo-fails")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "lcp-max-echo-fails must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lcp-max-echo-fails must be numeric, got: {value}",
                )

    # Validate defaultgw if present
    if "defaultgw" in payload:
        value = payload.get("defaultgw")
        if value and value not in VALID_BODY_DEFAULTGW:
            return (
                False,
                f"Invalid defaultgw '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULTGW)}",
            )

    # Validate dns-server-override if present
    if "dns-server-override" in payload:
        value = payload.get("dns-server-override")
        if value and value not in VALID_BODY_DNS_SERVER_OVERRIDE:
            return (
                False,
                f"Invalid dns-server-override '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVER_OVERRIDE)}",
            )

    # Validate dns-server-protocol if present
    if "dns-server-protocol" in payload:
        value = payload.get("dns-server-protocol")
        if value and value not in VALID_BODY_DNS_SERVER_PROTOCOL:
            return (
                False,
                f"Invalid dns-server-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVER_PROTOCOL)}",
            )

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate pptp-client if present
    if "pptp-client" in payload:
        value = payload.get("pptp-client")
        if value and value not in VALID_BODY_PPTP_CLIENT:
            return (
                False,
                f"Invalid pptp-client '{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_CLIENT)}",
            )

    # Validate pptp-user if present
    if "pptp-user" in payload:
        value = payload.get("pptp-user")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "pptp-user cannot exceed 64 characters")

    # Validate pptp-auth-type if present
    if "pptp-auth-type" in payload:
        value = payload.get("pptp-auth-type")
        if value and value not in VALID_BODY_PPTP_AUTH_TYPE:
            return (
                False,
                f"Invalid pptp-auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_PPTP_AUTH_TYPE)}",
            )

    # Validate pptp-timeout if present
    if "pptp-timeout" in payload:
        value = payload.get("pptp-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "pptp-timeout must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"pptp-timeout must be numeric, got: {value}")

    # Validate arpforward if present
    if "arpforward" in payload:
        value = payload.get("arpforward")
        if value and value not in VALID_BODY_ARPFORWARD:
            return (
                False,
                f"Invalid arpforward '{value}'. Must be one of: {', '.join(VALID_BODY_ARPFORWARD)}",
            )

    # Validate ndiscforward if present
    if "ndiscforward" in payload:
        value = payload.get("ndiscforward")
        if value and value not in VALID_BODY_NDISCFORWARD:
            return (
                False,
                f"Invalid ndiscforward '{value}'. Must be one of: {', '.join(VALID_BODY_NDISCFORWARD)}",
            )

    # Validate broadcast-forward if present
    if "broadcast-forward" in payload:
        value = payload.get("broadcast-forward")
        if value and value not in VALID_BODY_BROADCAST_FORWARD:
            return (
                False,
                f"Invalid broadcast-forward '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_FORWARD)}",
            )

    # Validate bfd if present
    if "bfd" in payload:
        value = payload.get("bfd")
        if value and value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid bfd '{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )

    # Validate bfd-desired-min-tx if present
    if "bfd-desired-min-tx" in payload:
        value = payload.get("bfd-desired-min-tx")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100000:
                    return (
                        False,
                        "bfd-desired-min-tx must be between 1 and 100000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-desired-min-tx must be numeric, got: {value}",
                )

    # Validate bfd-detect-mult if present
    if "bfd-detect-mult" in payload:
        value = payload.get("bfd-detect-mult")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 50:
                    return (False, "bfd-detect-mult must be between 1 and 50")
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-detect-mult must be numeric, got: {value}",
                )

    # Validate bfd-required-min-rx if present
    if "bfd-required-min-rx" in payload:
        value = payload.get("bfd-required-min-rx")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100000:
                    return (
                        False,
                        "bfd-required-min-rx must be between 1 and 100000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bfd-required-min-rx must be numeric, got: {value}",
                )

    # Validate l2forward if present
    if "l2forward" in payload:
        value = payload.get("l2forward")
        if value and value not in VALID_BODY_L2FORWARD:
            return (
                False,
                f"Invalid l2forward '{value}'. Must be one of: {', '.join(VALID_BODY_L2FORWARD)}",
            )

    # Validate icmp-send-redirect if present
    if "icmp-send-redirect" in payload:
        value = payload.get("icmp-send-redirect")
        if value and value not in VALID_BODY_ICMP_SEND_REDIRECT:
            return (
                False,
                f"Invalid icmp-send-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_SEND_REDIRECT)}",
            )

    # Validate icmp-accept-redirect if present
    if "icmp-accept-redirect" in payload:
        value = payload.get("icmp-accept-redirect")
        if value and value not in VALID_BODY_ICMP_ACCEPT_REDIRECT:
            return (
                False,
                f"Invalid icmp-accept-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_ICMP_ACCEPT_REDIRECT)}",
            )

    # Validate reachable-time if present
    if "reachable-time" in payload:
        value = payload.get("reachable-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30000 or int_val > 3600000:
                    return (
                        False,
                        "reachable-time must be between 30000 and 3600000",
                    )
            except (ValueError, TypeError):
                return (False, f"reachable-time must be numeric, got: {value}")

    # Validate vlanforward if present
    if "vlanforward" in payload:
        value = payload.get("vlanforward")
        if value and value not in VALID_BODY_VLANFORWARD:
            return (
                False,
                f"Invalid vlanforward '{value}'. Must be one of: {', '.join(VALID_BODY_VLANFORWARD)}",
            )

    # Validate stpforward if present
    if "stpforward" in payload:
        value = payload.get("stpforward")
        if value and value not in VALID_BODY_STPFORWARD:
            return (
                False,
                f"Invalid stpforward '{value}'. Must be one of: {', '.join(VALID_BODY_STPFORWARD)}",
            )

    # Validate stpforward-mode if present
    if "stpforward-mode" in payload:
        value = payload.get("stpforward-mode")
        if value and value not in VALID_BODY_STPFORWARD_MODE:
            return (
                False,
                f"Invalid stpforward-mode '{value}'. Must be one of: {', '.join(VALID_BODY_STPFORWARD_MODE)}",
            )

    # Validate ips-sniffer-mode if present
    if "ips-sniffer-mode" in payload:
        value = payload.get("ips-sniffer-mode")
        if value and value not in VALID_BODY_IPS_SNIFFER_MODE:
            return (
                False,
                f"Invalid ips-sniffer-mode '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SNIFFER_MODE)}",
            )

    # Validate ident-accept if present
    if "ident-accept" in payload:
        value = payload.get("ident-accept")
        if value and value not in VALID_BODY_IDENT_ACCEPT:
            return (
                False,
                f"Invalid ident-accept '{value}'. Must be one of: {', '.join(VALID_BODY_IDENT_ACCEPT)}",
            )

    # Validate ipmac if present
    if "ipmac" in payload:
        value = payload.get("ipmac")
        if value and value not in VALID_BODY_IPMAC:
            return (
                False,
                f"Invalid ipmac '{value}'. Must be one of: {', '.join(VALID_BODY_IPMAC)}",
            )

    # Validate subst if present
    if "subst" in payload:
        value = payload.get("subst")
        if value and value not in VALID_BODY_SUBST:
            return (
                False,
                f"Invalid subst '{value}'. Must be one of: {', '.join(VALID_BODY_SUBST)}",
            )

    # Validate speed if present
    if "speed" in payload:
        value = payload.get("speed")
        if value and value not in VALID_BODY_SPEED:
            return (
                False,
                f"Invalid speed '{value}'. Must be one of: {', '.join(VALID_BODY_SPEED)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate netbios-forward if present
    if "netbios-forward" in payload:
        value = payload.get("netbios-forward")
        if value and value not in VALID_BODY_NETBIOS_FORWARD:
            return (
                False,
                f"Invalid netbios-forward '{value}'. Must be one of: {', '.join(VALID_BODY_NETBIOS_FORWARD)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate dedicated-to if present
    if "dedicated-to" in payload:
        value = payload.get("dedicated-to")
        if value and value not in VALID_BODY_DEDICATED_TO:
            return (
                False,
                f"Invalid dedicated-to '{value}'. Must be one of: {', '.join(VALID_BODY_DEDICATED_TO)}",
            )

    # Validate wccp if present
    if "wccp" in payload:
        value = payload.get("wccp")
        if value and value not in VALID_BODY_WCCP:
            return (
                False,
                f"Invalid wccp '{value}'. Must be one of: {', '.join(VALID_BODY_WCCP)}",
            )

    # Validate netflow-sampler if present
    if "netflow-sampler" in payload:
        value = payload.get("netflow-sampler")
        if value and value not in VALID_BODY_NETFLOW_SAMPLER:
            return (
                False,
                f"Invalid netflow-sampler '{value}'. Must be one of: {', '.join(VALID_BODY_NETFLOW_SAMPLER)}",
            )

    # Validate netflow-sample-rate if present
    if "netflow-sample-rate" in payload:
        value = payload.get("netflow-sample-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "netflow-sample-rate must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"netflow-sample-rate must be numeric, got: {value}",
                )

    # Validate netflow-sampler-id if present
    if "netflow-sampler-id" in payload:
        value = payload.get("netflow-sampler-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 254:
                    return (
                        False,
                        "netflow-sampler-id must be between 1 and 254",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"netflow-sampler-id must be numeric, got: {value}",
                )

    # Validate sflow-sampler if present
    if "sflow-sampler" in payload:
        value = payload.get("sflow-sampler")
        if value and value not in VALID_BODY_SFLOW_SAMPLER:
            return (
                False,
                f"Invalid sflow-sampler '{value}'. Must be one of: {', '.join(VALID_BODY_SFLOW_SAMPLER)}",
            )

    # Validate drop-fragment if present
    if "drop-fragment" in payload:
        value = payload.get("drop-fragment")
        if value and value not in VALID_BODY_DROP_FRAGMENT:
            return (
                False,
                f"Invalid drop-fragment '{value}'. Must be one of: {', '.join(VALID_BODY_DROP_FRAGMENT)}",
            )

    # Validate src-check if present
    if "src-check" in payload:
        value = payload.get("src-check")
        if value and value not in VALID_BODY_SRC_CHECK:
            return (
                False,
                f"Invalid src-check '{value}'. Must be one of: {', '.join(VALID_BODY_SRC_CHECK)}",
            )

    # Validate sample-rate if present
    if "sample-rate" in payload:
        value = payload.get("sample-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 99999:
                    return (False, "sample-rate must be between 10 and 99999")
            except (ValueError, TypeError):
                return (False, f"sample-rate must be numeric, got: {value}")

    # Validate polling-interval if present
    if "polling-interval" in payload:
        value = payload.get("polling-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (
                        False,
                        "polling-interval must be between 1 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"polling-interval must be numeric, got: {value}",
                )

    # Validate sample-direction if present
    if "sample-direction" in payload:
        value = payload.get("sample-direction")
        if value and value not in VALID_BODY_SAMPLE_DIRECTION:
            return (
                False,
                f"Invalid sample-direction '{value}'. Must be one of: {', '.join(VALID_BODY_SAMPLE_DIRECTION)}",
            )

    # Validate explicit-web-proxy if present
    if "explicit-web-proxy" in payload:
        value = payload.get("explicit-web-proxy")
        if value and value not in VALID_BODY_EXPLICIT_WEB_PROXY:
            return (
                False,
                f"Invalid explicit-web-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_EXPLICIT_WEB_PROXY)}",
            )

    # Validate explicit-ftp-proxy if present
    if "explicit-ftp-proxy" in payload:
        value = payload.get("explicit-ftp-proxy")
        if value and value not in VALID_BODY_EXPLICIT_FTP_PROXY:
            return (
                False,
                f"Invalid explicit-ftp-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_EXPLICIT_FTP_PROXY)}",
            )

    # Validate proxy-captive-portal if present
    if "proxy-captive-portal" in payload:
        value = payload.get("proxy-captive-portal")
        if value and value not in VALID_BODY_PROXY_CAPTIVE_PORTAL:
            return (
                False,
                f"Invalid proxy-captive-portal '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_CAPTIVE_PORTAL)}",
            )

    # Validate tcp-mss if present
    if "tcp-mss" in payload:
        value = payload.get("tcp-mss")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 48 or int_val > 65535:
                    return (False, "tcp-mss must be between 48 and 65535")
            except (ValueError, TypeError):
                return (False, f"tcp-mss must be numeric, got: {value}")

    # Validate inbandwidth if present
    if "inbandwidth" in payload:
        value = payload.get("inbandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "inbandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (False, f"inbandwidth must be numeric, got: {value}")

    # Validate outbandwidth if present
    if "outbandwidth" in payload:
        value = payload.get("outbandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "outbandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (False, f"outbandwidth must be numeric, got: {value}")

    # Validate egress-shaping-profile if present
    if "egress-shaping-profile" in payload:
        value = payload.get("egress-shaping-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "egress-shaping-profile cannot exceed 35 characters",
            )

    # Validate ingress-shaping-profile if present
    if "ingress-shaping-profile" in payload:
        value = payload.get("ingress-shaping-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "ingress-shaping-profile cannot exceed 35 characters",
            )

    # Validate spillover-threshold if present
    if "spillover-threshold" in payload:
        value = payload.get("spillover-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "spillover-threshold must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spillover-threshold must be numeric, got: {value}",
                )

    # Validate ingress-spillover-threshold if present
    if "ingress-spillover-threshold" in payload:
        value = payload.get("ingress-spillover-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 16776000:
                    return (
                        False,
                        "ingress-spillover-threshold must be between 0 and 16776000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ingress-spillover-threshold must be numeric, got: {value}",
                )

    # Validate weight if present
    if "weight" in payload:
        value = payload.get("weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "weight must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"weight must be numeric, got: {value}")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate external if present
    if "external" in payload:
        value = payload.get("external")
        if value and value not in VALID_BODY_EXTERNAL:
            return (
                False,
                f"Invalid external '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL)}",
            )

    # Validate mtu-override if present
    if "mtu-override" in payload:
        value = payload.get("mtu-override")
        if value and value not in VALID_BODY_MTU_OVERRIDE:
            return (
                False,
                f"Invalid mtu-override '{value}'. Must be one of: {', '.join(VALID_BODY_MTU_OVERRIDE)}",
            )

    # Validate mtu if present
    if "mtu" in payload:
        value = payload.get("mtu")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "mtu must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"mtu must be numeric, got: {value}")

    # Validate vlan-protocol if present
    if "vlan-protocol" in payload:
        value = payload.get("vlan-protocol")
        if value and value not in VALID_BODY_VLAN_PROTOCOL:
            return (
                False,
                f"Invalid vlan-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_PROTOCOL)}",
            )

    # Validate vlanid if present
    if "vlanid" in payload:
        value = payload.get("vlanid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4094:
                    return (False, "vlanid must be between 1 and 4094")
            except (ValueError, TypeError):
                return (False, f"vlanid must be numeric, got: {value}")

    # Validate trunk if present
    if "trunk" in payload:
        value = payload.get("trunk")
        if value and value not in VALID_BODY_TRUNK:
            return (
                False,
                f"Invalid trunk '{value}'. Must be one of: {', '.join(VALID_BODY_TRUNK)}",
            )

    # Validate forward-domain if present
    if "forward-domain" in payload:
        value = payload.get("forward-domain")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "forward-domain must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"forward-domain must be numeric, got: {value}")

    # Validate lacp-mode if present
    if "lacp-mode" in payload:
        value = payload.get("lacp-mode")
        if value and value not in VALID_BODY_LACP_MODE:
            return (
                False,
                f"Invalid lacp-mode '{value}'. Must be one of: {', '.join(VALID_BODY_LACP_MODE)}",
            )

    # Validate lacp-ha-secondary if present
    if "lacp-ha-secondary" in payload:
        value = payload.get("lacp-ha-secondary")
        if value and value not in VALID_BODY_LACP_HA_SECONDARY:
            return (
                False,
                f"Invalid lacp-ha-secondary '{value}'. Must be one of: {', '.join(VALID_BODY_LACP_HA_SECONDARY)}",
            )

    # Validate system-id-type if present
    if "system-id-type" in payload:
        value = payload.get("system-id-type")
        if value and value not in VALID_BODY_SYSTEM_ID_TYPE:
            return (
                False,
                f"Invalid system-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM_ID_TYPE)}",
            )

    # Validate lacp-speed if present
    if "lacp-speed" in payload:
        value = payload.get("lacp-speed")
        if value and value not in VALID_BODY_LACP_SPEED:
            return (
                False,
                f"Invalid lacp-speed '{value}'. Must be one of: {', '.join(VALID_BODY_LACP_SPEED)}",
            )

    # Validate min-links if present
    if "min-links" in payload:
        value = payload.get("min-links")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 32:
                    return (False, "min-links must be between 1 and 32")
            except (ValueError, TypeError):
                return (False, f"min-links must be numeric, got: {value}")

    # Validate min-links-down if present
    if "min-links-down" in payload:
        value = payload.get("min-links-down")
        if value and value not in VALID_BODY_MIN_LINKS_DOWN:
            return (
                False,
                f"Invalid min-links-down '{value}'. Must be one of: {', '.join(VALID_BODY_MIN_LINKS_DOWN)}",
            )

    # Validate algorithm if present
    if "algorithm" in payload:
        value = payload.get("algorithm")
        if value and value not in VALID_BODY_ALGORITHM:
            return (
                False,
                f"Invalid algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_ALGORITHM)}",
            )

    # Validate link-up-delay if present
    if "link-up-delay" in payload:
        value = payload.get("link-up-delay")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 50 or int_val > 3600000:
                    return (
                        False,
                        "link-up-delay must be between 50 and 3600000",
                    )
            except (ValueError, TypeError):
                return (False, f"link-up-delay must be numeric, got: {value}")

    # Validate aggregate-type if present
    if "aggregate-type" in payload:
        value = payload.get("aggregate-type")
        if value and value not in VALID_BODY_AGGREGATE_TYPE:
            return (
                False,
                f"Invalid aggregate-type '{value}'. Must be one of: {', '.join(VALID_BODY_AGGREGATE_TYPE)}",
            )

    # Validate priority-override if present
    if "priority-override" in payload:
        value = payload.get("priority-override")
        if value and value not in VALID_BODY_PRIORITY_OVERRIDE:
            return (
                False,
                f"Invalid priority-override '{value}'. Must be one of: {', '.join(VALID_BODY_PRIORITY_OVERRIDE)}",
            )

    # Validate aggregate if present
    if "aggregate" in payload:
        value = payload.get("aggregate")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "aggregate cannot exceed 15 characters")

    # Validate redundant-interface if present
    if "redundant-interface" in payload:
        value = payload.get("redundant-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "redundant-interface cannot exceed 15 characters")

    # Validate devindex if present
    if "devindex" in payload:
        value = payload.get("devindex")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "devindex must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"devindex must be numeric, got: {value}")

    # Validate vindex if present
    if "vindex" in payload:
        value = payload.get("vindex")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "vindex must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"vindex must be numeric, got: {value}")

    # Validate switch if present
    if "switch" in payload:
        value = payload.get("switch")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "switch cannot exceed 15 characters")

    # Validate description if present
    if "description" in payload:
        value = payload.get("description")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "description cannot exceed 255 characters")

    # Validate alias if present
    if "alias" in payload:
        value = payload.get("alias")
        if value and isinstance(value, str) and len(value) > 25:
            return (False, "alias cannot exceed 25 characters")

    # Validate l2tp-client if present
    if "l2tp-client" in payload:
        value = payload.get("l2tp-client")
        if value and value not in VALID_BODY_L2TP_CLIENT:
            return (
                False,
                f"Invalid l2tp-client '{value}'. Must be one of: {', '.join(VALID_BODY_L2TP_CLIENT)}",
            )

    # Validate security-mode if present
    if "security-mode" in payload:
        value = payload.get("security-mode")
        if value and value not in VALID_BODY_SECURITY_MODE:
            return (
                False,
                f"Invalid security-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MODE)}",
            )

    # Validate security-mac-auth-bypass if present
    if "security-mac-auth-bypass" in payload:
        value = payload.get("security-mac-auth-bypass")
        if value and value not in VALID_BODY_SECURITY_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid security-mac-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_MAC_AUTH_BYPASS)}",
            )

    # Validate security-ip-auth-bypass if present
    if "security-ip-auth-bypass" in payload:
        value = payload.get("security-ip-auth-bypass")
        if value and value not in VALID_BODY_SECURITY_IP_AUTH_BYPASS:
            return (
                False,
                f"Invalid security-ip-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_IP_AUTH_BYPASS)}",
            )

    # Validate security-8021x-mode if present
    if "security-8021x-mode" in payload:
        value = payload.get("security-8021x-mode")
        if value and value not in VALID_BODY_SECURITY_8021X_MODE:
            return (
                False,
                f"Invalid security-8021x-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_8021X_MODE)}",
            )

    # Validate security-8021x-master if present
    if "security-8021x-master" in payload:
        value = payload.get("security-8021x-master")
        if value and isinstance(value, str) and len(value) > 15:
            return (
                False,
                "security-8021x-master cannot exceed 15 characters",
            )

    # Validate security-8021x-dynamic-vlan-id if present
    if "security-8021x-dynamic-vlan-id" in payload:
        value = payload.get("security-8021x-dynamic-vlan-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4094:
                    return (
                        False,
                        "security-8021x-dynamic-vlan-id must be between 0 and 4094",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"security-8021x-dynamic-vlan-id must be numeric, got: {value}",
                )

    # Validate security-8021x-member-mode if present
    if "security-8021x-member-mode" in payload:
        value = payload.get("security-8021x-member-mode")
        if value and value not in VALID_BODY_SECURITY_8021X_MEMBER_MODE:
            return (
                False,
                f"Invalid security-8021x-member-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_8021X_MEMBER_MODE)}",
            )

    # Validate security-external-web if present
    if "security-external-web" in payload:
        value = payload.get("security-external-web")
        if value and isinstance(value, str) and len(value) > 1023:
            return (
                False,
                "security-external-web cannot exceed 1023 characters",
            )

    # Validate security-external-logout if present
    if "security-external-logout" in payload:
        value = payload.get("security-external-logout")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "security-external-logout cannot exceed 127 characters",
            )

    # Validate replacemsg-override-group if present
    if "replacemsg-override-group" in payload:
        value = payload.get("replacemsg-override-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "replacemsg-override-group cannot exceed 35 characters",
            )

    # Validate security-redirect-url if present
    if "security-redirect-url" in payload:
        value = payload.get("security-redirect-url")
        if value and isinstance(value, str) and len(value) > 1023:
            return (
                False,
                "security-redirect-url cannot exceed 1023 characters",
            )

    # Validate auth-cert if present
    if "auth-cert" in payload:
        value = payload.get("auth-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-cert cannot exceed 35 characters")

    # Validate auth-portal-addr if present
    if "auth-portal-addr" in payload:
        value = payload.get("auth-portal-addr")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auth-portal-addr cannot exceed 63 characters")

    # Validate security-exempt-list if present
    if "security-exempt-list" in payload:
        value = payload.get("security-exempt-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "security-exempt-list cannot exceed 35 characters")

    # Validate ike-saml-server if present
    if "ike-saml-server" in payload:
        value = payload.get("ike-saml-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ike-saml-server cannot exceed 35 characters")

    # Validate stp if present
    if "stp" in payload:
        value = payload.get("stp")
        if value and value not in VALID_BODY_STP:
            return (
                False,
                f"Invalid stp '{value}'. Must be one of: {', '.join(VALID_BODY_STP)}",
            )

    # Validate stp-ha-secondary if present
    if "stp-ha-secondary" in payload:
        value = payload.get("stp-ha-secondary")
        if value and value not in VALID_BODY_STP_HA_SECONDARY:
            return (
                False,
                f"Invalid stp-ha-secondary '{value}'. Must be one of: {', '.join(VALID_BODY_STP_HA_SECONDARY)}",
            )

    # Validate stp-edge if present
    if "stp-edge" in payload:
        value = payload.get("stp-edge")
        if value and value not in VALID_BODY_STP_EDGE:
            return (
                False,
                f"Invalid stp-edge '{value}'. Must be one of: {', '.join(VALID_BODY_STP_EDGE)}",
            )

    # Validate device-identification if present
    if "device-identification" in payload:
        value = payload.get("device-identification")
        if value and value not in VALID_BODY_DEVICE_IDENTIFICATION:
            return (
                False,
                f"Invalid device-identification '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_IDENTIFICATION)}",
            )

    # Validate exclude-signatures if present
    if "exclude-signatures" in payload:
        value = payload.get("exclude-signatures")
        if value and value not in VALID_BODY_EXCLUDE_SIGNATURES:
            return (
                False,
                f"Invalid exclude-signatures '{value}'. Must be one of: {', '.join(VALID_BODY_EXCLUDE_SIGNATURES)}",
            )

    # Validate device-user-identification if present
    if "device-user-identification" in payload:
        value = payload.get("device-user-identification")
        if value and value not in VALID_BODY_DEVICE_USER_IDENTIFICATION:
            return (
                False,
                f"Invalid device-user-identification '{value}'. Must be one of: {', '.join(VALID_BODY_DEVICE_USER_IDENTIFICATION)}",
            )

    # Validate lldp-reception if present
    if "lldp-reception" in payload:
        value = payload.get("lldp-reception")
        if value and value not in VALID_BODY_LLDP_RECEPTION:
            return (
                False,
                f"Invalid lldp-reception '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_RECEPTION)}",
            )

    # Validate lldp-transmission if present
    if "lldp-transmission" in payload:
        value = payload.get("lldp-transmission")
        if value and value not in VALID_BODY_LLDP_TRANSMISSION:
            return (
                False,
                f"Invalid lldp-transmission '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_TRANSMISSION)}",
            )

    # Validate lldp-network-policy if present
    if "lldp-network-policy" in payload:
        value = payload.get("lldp-network-policy")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "lldp-network-policy cannot exceed 35 characters")

    # Validate estimated-upstream-bandwidth if present
    if "estimated-upstream-bandwidth" in payload:
        value = payload.get("estimated-upstream-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "estimated-upstream-bandwidth must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"estimated-upstream-bandwidth must be numeric, got: {value}",
                )

    # Validate estimated-downstream-bandwidth if present
    if "estimated-downstream-bandwidth" in payload:
        value = payload.get("estimated-downstream-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "estimated-downstream-bandwidth must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"estimated-downstream-bandwidth must be numeric, got: {value}",
                )

    # Validate measured-upstream-bandwidth if present
    if "measured-upstream-bandwidth" in payload:
        value = payload.get("measured-upstream-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "measured-upstream-bandwidth must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"measured-upstream-bandwidth must be numeric, got: {value}",
                )

    # Validate measured-downstream-bandwidth if present
    if "measured-downstream-bandwidth" in payload:
        value = payload.get("measured-downstream-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "measured-downstream-bandwidth must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"measured-downstream-bandwidth must be numeric, got: {value}",
                )

    # Validate bandwidth-measure-time if present
    if "bandwidth-measure-time" in payload:
        value = payload.get("bandwidth-measure-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "bandwidth-measure-time must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bandwidth-measure-time must be numeric, got: {value}",
                )

    # Validate monitor-bandwidth if present
    if "monitor-bandwidth" in payload:
        value = payload.get("monitor-bandwidth")
        if value and value not in VALID_BODY_MONITOR_BANDWIDTH:
            return (
                False,
                f"Invalid monitor-bandwidth '{value}'. Must be one of: {', '.join(VALID_BODY_MONITOR_BANDWIDTH)}",
            )

    # Validate vrrp-virtual-mac if present
    if "vrrp-virtual-mac" in payload:
        value = payload.get("vrrp-virtual-mac")
        if value and value not in VALID_BODY_VRRP_VIRTUAL_MAC:
            return (
                False,
                f"Invalid vrrp-virtual-mac '{value}'. Must be one of: {', '.join(VALID_BODY_VRRP_VIRTUAL_MAC)}",
            )

    # Validate role if present
    if "role" in payload:
        value = payload.get("role")
        if value and value not in VALID_BODY_ROLE:
            return (
                False,
                f"Invalid role '{value}'. Must be one of: {', '.join(VALID_BODY_ROLE)}",
            )

    # Validate snmp-index if present
    if "snmp-index" in payload:
        value = payload.get("snmp-index")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "snmp-index must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"snmp-index must be numeric, got: {value}")

    # Validate secondary-IP if present
    if "secondary-IP" in payload:
        value = payload.get("secondary-IP")
        if value and value not in VALID_BODY_SECONDARY_IP:
            return (
                False,
                f"Invalid secondary-IP '{value}'. Must be one of: {', '.join(VALID_BODY_SECONDARY_IP)}",
            )

    # Validate preserve-session-route if present
    if "preserve-session-route" in payload:
        value = payload.get("preserve-session-route")
        if value and value not in VALID_BODY_PRESERVE_SESSION_ROUTE:
            return (
                False,
                f"Invalid preserve-session-route '{value}'. Must be one of: {', '.join(VALID_BODY_PRESERVE_SESSION_ROUTE)}",
            )

    # Validate auto-auth-extension-device if present
    if "auto-auth-extension-device" in payload:
        value = payload.get("auto-auth-extension-device")
        if value and value not in VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE:
            return (
                False,
                f"Invalid auto-auth-extension-device '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE)}",
            )

    # Validate ap-discover if present
    if "ap-discover" in payload:
        value = payload.get("ap-discover")
        if value and value not in VALID_BODY_AP_DISCOVER:
            return (
                False,
                f"Invalid ap-discover '{value}'. Must be one of: {', '.join(VALID_BODY_AP_DISCOVER)}",
            )

    # Validate fortilink-neighbor-detect if present
    if "fortilink-neighbor-detect" in payload:
        value = payload.get("fortilink-neighbor-detect")
        if value and value not in VALID_BODY_FORTILINK_NEIGHBOR_DETECT:
            return (
                False,
                f"Invalid fortilink-neighbor-detect '{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK_NEIGHBOR_DETECT)}",
            )

    # Validate ip-managed-by-fortiipam if present
    if "ip-managed-by-fortiipam" in payload:
        value = payload.get("ip-managed-by-fortiipam")
        if value and value not in VALID_BODY_IP_MANAGED_BY_FORTIIPAM:
            return (
                False,
                f"Invalid ip-managed-by-fortiipam '{value}'. Must be one of: {', '.join(VALID_BODY_IP_MANAGED_BY_FORTIIPAM)}",
            )

    # Validate managed-subnetwork-size if present
    if "managed-subnetwork-size" in payload:
        value = payload.get("managed-subnetwork-size")
        if value and value not in VALID_BODY_MANAGED_SUBNETWORK_SIZE:
            return (
                False,
                f"Invalid managed-subnetwork-size '{value}'. Must be one of: {', '.join(VALID_BODY_MANAGED_SUBNETWORK_SIZE)}",
            )

    # Validate fortilink-split-interface if present
    if "fortilink-split-interface" in payload:
        value = payload.get("fortilink-split-interface")
        if value and value not in VALID_BODY_FORTILINK_SPLIT_INTERFACE:
            return (
                False,
                f"Invalid fortilink-split-interface '{value}'. Must be one of: {', '.join(VALID_BODY_FORTILINK_SPLIT_INTERFACE)}",
            )

    # Validate internal if present
    if "internal" in payload:
        value = payload.get("internal")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "internal must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"internal must be numeric, got: {value}")

    # Validate fortilink-backup-link if present
    if "fortilink-backup-link" in payload:
        value = payload.get("fortilink-backup-link")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "fortilink-backup-link must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fortilink-backup-link must be numeric, got: {value}",
                )

    # Validate switch-controller-access-vlan if present
    if "switch-controller-access-vlan" in payload:
        value = payload.get("switch-controller-access-vlan")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN:
            return (
                False,
                f"Invalid switch-controller-access-vlan '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_ACCESS_VLAN)}",
            )

    # Validate switch-controller-traffic-policy if present
    if "switch-controller-traffic-policy" in payload:
        value = payload.get("switch-controller-traffic-policy")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "switch-controller-traffic-policy cannot exceed 63 characters",
            )

    # Validate switch-controller-rspan-mode if present
    if "switch-controller-rspan-mode" in payload:
        value = payload.get("switch-controller-rspan-mode")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE:
            return (
                False,
                f"Invalid switch-controller-rspan-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_RSPAN_MODE)}",
            )

    # Validate switch-controller-netflow-collect if present
    if "switch-controller-netflow-collect" in payload:
        value = payload.get("switch-controller-netflow-collect")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT:
            return (
                False,
                f"Invalid switch-controller-netflow-collect '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_NETFLOW_COLLECT)}",
            )

    # Validate switch-controller-mgmt-vlan if present
    if "switch-controller-mgmt-vlan" in payload:
        value = payload.get("switch-controller-mgmt-vlan")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4094:
                    return (
                        False,
                        "switch-controller-mgmt-vlan must be between 1 and 4094",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"switch-controller-mgmt-vlan must be numeric, got: {value}",
                )

    # Validate switch-controller-igmp-snooping if present
    if "switch-controller-igmp-snooping" in payload:
        value = payload.get("switch-controller-igmp-snooping")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING:
            return (
                False,
                f"Invalid switch-controller-igmp-snooping '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING)}",
            )

    # Validate switch-controller-igmp-snooping-proxy if present
    if "switch-controller-igmp-snooping-proxy" in payload:
        value = payload.get("switch-controller-igmp-snooping-proxy")
        if (
            value
            and value not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY
        ):
            return (
                False,
                f"Invalid switch-controller-igmp-snooping-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_PROXY)}",
            )

    # Validate switch-controller-igmp-snooping-fast-leave if present
    if "switch-controller-igmp-snooping-fast-leave" in payload:
        value = payload.get("switch-controller-igmp-snooping-fast-leave")
        if (
            value
            and value
            not in VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE
        ):
            return (
                False,
                f"Invalid switch-controller-igmp-snooping-fast-leave '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IGMP_SNOOPING_FAST_LEAVE)}",
            )

    # Validate switch-controller-dhcp-snooping if present
    if "switch-controller-dhcp-snooping" in payload:
        value = payload.get("switch-controller-dhcp-snooping")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING:
            return (
                False,
                f"Invalid switch-controller-dhcp-snooping '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING)}",
            )

    # Validate switch-controller-dhcp-snooping-verify-mac if present
    if "switch-controller-dhcp-snooping-verify-mac" in payload:
        value = payload.get("switch-controller-dhcp-snooping-verify-mac")
        if (
            value
            and value
            not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC
        ):
            return (
                False,
                f"Invalid switch-controller-dhcp-snooping-verify-mac '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_VERIFY_MAC)}",
            )

    # Validate switch-controller-dhcp-snooping-option82 if present
    if "switch-controller-dhcp-snooping-option82" in payload:
        value = payload.get("switch-controller-dhcp-snooping-option82")
        if (
            value
            and value
            not in VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82
        ):
            return (
                False,
                f"Invalid switch-controller-dhcp-snooping-option82 '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_DHCP_SNOOPING_OPTION82)}",
            )

    # Validate switch-controller-arp-inspection if present
    if "switch-controller-arp-inspection" in payload:
        value = payload.get("switch-controller-arp-inspection")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION:
            return (
                False,
                f"Invalid switch-controller-arp-inspection '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_ARP_INSPECTION)}",
            )

    # Validate switch-controller-learning-limit if present
    if "switch-controller-learning-limit" in payload:
        value = payload.get("switch-controller-learning-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "switch-controller-learning-limit must be between 0 and 128",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"switch-controller-learning-limit must be numeric, got: {value}",
                )

    # Validate switch-controller-nac if present
    if "switch-controller-nac" in payload:
        value = payload.get("switch-controller-nac")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "switch-controller-nac cannot exceed 35 characters",
            )

    # Validate switch-controller-dynamic if present
    if "switch-controller-dynamic" in payload:
        value = payload.get("switch-controller-dynamic")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "switch-controller-dynamic cannot exceed 35 characters",
            )

    # Validate switch-controller-feature if present
    if "switch-controller-feature" in payload:
        value = payload.get("switch-controller-feature")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_FEATURE:
            return (
                False,
                f"Invalid switch-controller-feature '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_FEATURE)}",
            )

    # Validate switch-controller-iot-scanning if present
    if "switch-controller-iot-scanning" in payload:
        value = payload.get("switch-controller-iot-scanning")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING:
            return (
                False,
                f"Invalid switch-controller-iot-scanning '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_IOT_SCANNING)}",
            )

    # Validate switch-controller-offload if present
    if "switch-controller-offload" in payload:
        value = payload.get("switch-controller-offload")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD:
            return (
                False,
                f"Invalid switch-controller-offload '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_OFFLOAD)}",
            )

    # Validate switch-controller-offload-gw if present
    if "switch-controller-offload-gw" in payload:
        value = payload.get("switch-controller-offload-gw")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW:
            return (
                False,
                f"Invalid switch-controller-offload-gw '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER_OFFLOAD_GW)}",
            )

    # Validate swc-vlan if present
    if "swc-vlan" in payload:
        value = payload.get("swc-vlan")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "swc-vlan must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"swc-vlan must be numeric, got: {value}")

    # Validate swc-first-create if present
    if "swc-first-create" in payload:
        value = payload.get("swc-first-create")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "swc-first-create must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"swc-first-create must be numeric, got: {value}",
                )

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    # Validate eap-supplicant if present
    if "eap-supplicant" in payload:
        value = payload.get("eap-supplicant")
        if value and value not in VALID_BODY_EAP_SUPPLICANT:
            return (
                False,
                f"Invalid eap-supplicant '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_SUPPLICANT)}",
            )

    # Validate eap-method if present
    if "eap-method" in payload:
        value = payload.get("eap-method")
        if value and value not in VALID_BODY_EAP_METHOD:
            return (
                False,
                f"Invalid eap-method '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_METHOD)}",
            )

    # Validate eap-identity if present
    if "eap-identity" in payload:
        value = payload.get("eap-identity")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "eap-identity cannot exceed 35 characters")

    # Validate eap-ca-cert if present
    if "eap-ca-cert" in payload:
        value = payload.get("eap-ca-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "eap-ca-cert cannot exceed 79 characters")

    # Validate eap-user-cert if present
    if "eap-user-cert" in payload:
        value = payload.get("eap-user-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "eap-user-cert cannot exceed 35 characters")

    # Validate default-purdue-level if present
    if "default-purdue-level" in payload:
        value = payload.get("default-purdue-level")
        if value and value not in VALID_BODY_DEFAULT_PURDUE_LEVEL:
            return (
                False,
                f"Invalid default-purdue-level '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_PURDUE_LEVEL)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_interface_delete(
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
