"""
Validation helpers for wireless-controller vap endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_PRE_AUTH = ["enable", "disable"]
VALID_BODY_EXTERNAL_PRE_AUTH = ["enable", "disable"]
VALID_BODY_MESH_BACKHAUL = ["enable", "disable"]
VALID_BODY_BROADCAST_SSID = ["enable", "disable"]
VALID_BODY_SECURITY = [
    "open",
    "wep64",
    "wep128",
    "wpa-personal",
    "wpa-enterprise",
    "wpa-only-personal",
    "wpa-only-enterprise",
    "wpa2-only-personal",
    "wpa2-only-enterprise",
    "wpa3-enterprise",
    "wpa3-only-enterprise",
    "wpa3-enterprise-transition",
    "wpa3-sae",
    "wpa3-sae-transition",
    "owe",
    "osen",
]
VALID_BODY_PMF = ["disable", "enable", "optional"]
VALID_BODY_BEACON_PROTECTION = ["disable", "enable"]
VALID_BODY_OKC = ["disable", "enable"]
VALID_BODY_MBO = ["disable", "enable"]
VALID_BODY_MBO_CELL_DATA_CONN_PREF = ["excluded", "prefer-not", "prefer-use"]
VALID_BODY_80211K = ["disable", "enable"]
VALID_BODY_80211V = ["disable", "enable"]
VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND = ["disable", "enable"]
VALID_BODY_FAST_BSS_TRANSITION = ["disable", "enable"]
VALID_BODY_FT_OVER_DS = ["disable", "enable"]
VALID_BODY_SAE_GROUPS = ["19", "20", "21"]
VALID_BODY_OWE_GROUPS = ["19", "20", "21"]
VALID_BODY_OWE_TRANSITION = ["disable", "enable"]
VALID_BODY_ADDITIONAL_AKMS = ["akm6", "akm24"]
VALID_BODY_EAPOL_KEY_RETRIES = ["disable", "enable"]
VALID_BODY_TKIP_COUNTER_MEASURE = ["enable", "disable"]
VALID_BODY_EXTERNAL_WEB_FORMAT = [
    "auto-detect",
    "no-query-string",
    "partial-query-string",
]
VALID_BODY_MAC_USERNAME_DELIMITER = [
    "hyphen",
    "single-hyphen",
    "colon",
    "none",
]
VALID_BODY_MAC_PASSWORD_DELIMITER = [
    "hyphen",
    "single-hyphen",
    "colon",
    "none",
]
VALID_BODY_MAC_CALLING_STATION_DELIMITER = [
    "hyphen",
    "single-hyphen",
    "colon",
    "none",
]
VALID_BODY_MAC_CALLED_STATION_DELIMITER = [
    "hyphen",
    "single-hyphen",
    "colon",
    "none",
]
VALID_BODY_MAC_CASE = ["uppercase", "lowercase"]
VALID_BODY_CALLED_STATION_ID_TYPE = ["mac", "ip", "apname"]
VALID_BODY_MAC_AUTH_BYPASS = ["enable", "disable"]
VALID_BODY_RADIUS_MAC_AUTH = ["enable", "disable"]
VALID_BODY_RADIUS_MAC_MPSK_AUTH = ["enable", "disable"]
VALID_BODY_AUTH = ["radius", "usergroup"]
VALID_BODY_ENCRYPT = ["TKIP", "AES", "TKIP-AES"]
VALID_BODY_SAE_H2E_ONLY = ["enable", "disable"]
VALID_BODY_SAE_HNP_ONLY = ["enable", "disable"]
VALID_BODY_SAE_PK = ["enable", "disable"]
VALID_BODY_AKM24_ONLY = ["disable", "enable"]
VALID_BODY_NAS_FILTER_RULE = ["enable", "disable"]
VALID_BODY_DOMAIN_NAME_STRIPPING = ["disable", "enable"]
VALID_BODY_MLO = ["disable", "enable"]
VALID_BODY_LOCAL_STANDALONE = ["enable", "disable"]
VALID_BODY_LOCAL_STANDALONE_NAT = ["enable", "disable"]
VALID_BODY_LOCAL_STANDALONE_DNS = ["enable", "disable"]
VALID_BODY_LOCAL_LAN_PARTITION = ["enable", "disable"]
VALID_BODY_LOCAL_BRIDGING = ["enable", "disable"]
VALID_BODY_LOCAL_LAN = ["allow", "deny"]
VALID_BODY_LOCAL_AUTHENTICATION = ["enable", "disable"]
VALID_BODY_CAPTIVE_PORTAL = ["enable", "disable"]
VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS = ["enable", "disable"]
VALID_BODY_PORTAL_TYPE = [
    "auth",
    "auth+disclaimer",
    "disclaimer",
    "email-collect",
    "cmcc",
    "cmcc-macauth",
    "auth-mac",
    "external-auth",
    "external-macauth",
]
VALID_BODY_INTRA_VAP_PRIVACY = ["enable", "disable"]
VALID_BODY_LDPC = ["disable", "rx", "tx", "rxtx"]
VALID_BODY_HIGH_EFFICIENCY = ["enable", "disable"]
VALID_BODY_TARGET_WAKE_TIME = ["enable", "disable"]
VALID_BODY_PORT_MACAUTH = ["disable", "radius", "address-group"]
VALID_BODY_BSS_COLOR_PARTIAL = ["enable", "disable"]
VALID_BODY_SPLIT_TUNNELING = ["enable", "disable"]
VALID_BODY_NAC = ["enable", "disable"]
VALID_BODY_VLAN_AUTO = ["enable", "disable"]
VALID_BODY_DYNAMIC_VLAN = ["enable", "disable"]
VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING = ["enable", "disable"]
VALID_BODY_MULTICAST_RATE = ["0", "6000", "12000", "24000"]
VALID_BODY_MULTICAST_ENHANCE = ["enable", "disable"]
VALID_BODY_IGMP_SNOOPING = ["enable", "disable"]
VALID_BODY_DHCP_ADDRESS_ENFORCEMENT = ["enable", "disable"]
VALID_BODY_BROADCAST_SUPPRESSION = [
    "dhcp-up",
    "dhcp-down",
    "dhcp-starvation",
    "dhcp-ucast",
    "arp-known",
    "arp-unknown",
    "arp-reply",
    "arp-poison",
    "arp-proxy",
    "netbios-ns",
    "netbios-ds",
    "ipv6",
    "all-other-mc",
    "all-other-bc",
]
VALID_BODY_IPV6_RULES = [
    "drop-icmp6ra",
    "drop-icmp6rs",
    "drop-llmnr6",
    "drop-icmp6mld2",
    "drop-dhcp6s",
    "drop-dhcp6c",
    "ndp-proxy",
    "drop-ns-dad",
    "drop-ns-nondad",
]
VALID_BODY_MU_MIMO = ["enable", "disable"]
VALID_BODY_PROBE_RESP_SUPPRESSION = ["enable", "disable"]
VALID_BODY_RADIO_SENSITIVITY = ["enable", "disable"]
VALID_BODY_QUARANTINE = ["enable", "disable"]
VALID_BODY_VLAN_POOLING = ["wtp-group", "round-robin", "hash", "disable"]
VALID_BODY_DHCP_OPTION43_INSERTION = ["enable", "disable"]
VALID_BODY_DHCP_OPTION82_INSERTION = ["enable", "disable"]
VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION = [
    "style-1",
    "style-2",
    "style-3",
    "disable",
]
VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION = ["style-1", "disable"]
VALID_BODY_PTK_REKEY = ["enable", "disable"]
VALID_BODY_GTK_REKEY = ["enable", "disable"]
VALID_BODY_EAP_REAUTH = ["enable", "disable"]
VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE = ["enable", "disable"]
VALID_BODY_RATES_11A = [
    "6",
    "6-basic",
    "9",
    "9-basic",
    "12",
    "12-basic",
    "18",
    "18-basic",
    "24",
    "24-basic",
    "36",
    "36-basic",
    "48",
    "48-basic",
    "54",
    "54-basic",
]
VALID_BODY_RATES_11BG = [
    "1",
    "1-basic",
    "2",
    "2-basic",
    "5.5",
    "5.5-basic",
    "11",
    "11-basic",
    "6",
    "6-basic",
    "9",
    "9-basic",
    "12",
    "12-basic",
    "18",
    "18-basic",
    "24",
    "24-basic",
    "36",
    "36-basic",
    "48",
    "48-basic",
    "54",
    "54-basic",
]
VALID_BODY_RATES_11N_SS12 = [
    "mcs0/1",
    "mcs1/1",
    "mcs2/1",
    "mcs3/1",
    "mcs4/1",
    "mcs5/1",
    "mcs6/1",
    "mcs7/1",
    "mcs8/2",
    "mcs9/2",
    "mcs10/2",
    "mcs11/2",
    "mcs12/2",
    "mcs13/2",
    "mcs14/2",
    "mcs15/2",
]
VALID_BODY_RATES_11N_SS34 = [
    "mcs16/3",
    "mcs17/3",
    "mcs18/3",
    "mcs19/3",
    "mcs20/3",
    "mcs21/3",
    "mcs22/3",
    "mcs23/3",
    "mcs24/4",
    "mcs25/4",
    "mcs26/4",
    "mcs27/4",
    "mcs28/4",
    "mcs29/4",
    "mcs30/4",
    "mcs31/4",
]
VALID_BODY_UTM_STATUS = ["enable", "disable"]
VALID_BODY_UTM_LOG = ["enable", "disable"]
VALID_BODY_SCAN_BOTNET_CONNECTIONS = ["disable", "monitor", "block"]
VALID_BODY_ADDRESS_GROUP_POLICY = ["disable", "allow", "deny"]
VALID_BODY_STICKY_CLIENT_REMOVE = ["enable", "disable"]
VALID_BODY_BSTM_DISASSOCIATION_IMMINENT = ["enable", "disable"]
VALID_BODY_BEACON_ADVERTISING = ["name", "model", "serial-number"]
VALID_BODY_OSEN = ["enable", "disable"]
VALID_BODY_APPLICATION_DETECTION_ENGINE = ["enable", "disable"]
VALID_BODY_APPLICATION_DSCP_MARKING = ["enable", "disable"]
VALID_BODY_L3_ROAMING = ["enable", "disable"]
VALID_BODY_L3_ROAMING_MODE = ["direct", "indirect"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vap_get(
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


def validate_vap_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating vap.

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

    # Validate pre-auth if present
    if "pre-auth" in payload:
        value = payload.get("pre-auth")
        if value and value not in VALID_BODY_PRE_AUTH:
            return (
                False,
                f"Invalid pre-auth '{value}'. Must be one of: {', '.join(VALID_BODY_PRE_AUTH)}",
            )

    # Validate external-pre-auth if present
    if "external-pre-auth" in payload:
        value = payload.get("external-pre-auth")
        if value and value not in VALID_BODY_EXTERNAL_PRE_AUTH:
            return (
                False,
                f"Invalid external-pre-auth '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_PRE_AUTH)}",
            )

    # Validate mesh-backhaul if present
    if "mesh-backhaul" in payload:
        value = payload.get("mesh-backhaul")
        if value and value not in VALID_BODY_MESH_BACKHAUL:
            return (
                False,
                f"Invalid mesh-backhaul '{value}'. Must be one of: {', '.join(VALID_BODY_MESH_BACKHAUL)}",
            )

    # Validate atf-weight if present
    if "atf-weight" in payload:
        value = payload.get("atf-weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (False, "atf-weight must be between 0 and 100")
            except (ValueError, TypeError):
                return (False, f"atf-weight must be numeric, got: {value}")

    # Validate max-clients if present
    if "max-clients" in payload:
        value = payload.get("max-clients")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-clients must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-clients must be numeric, got: {value}")

    # Validate max-clients-ap if present
    if "max-clients-ap" in payload:
        value = payload.get("max-clients-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-clients-ap must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-clients-ap must be numeric, got: {value}")

    # Validate ssid if present
    if "ssid" in payload:
        value = payload.get("ssid")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "ssid cannot exceed 32 characters")

    # Validate broadcast-ssid if present
    if "broadcast-ssid" in payload:
        value = payload.get("broadcast-ssid")
        if value and value not in VALID_BODY_BROADCAST_SSID:
            return (
                False,
                f"Invalid broadcast-ssid '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SSID)}",
            )

    # Validate security if present
    if "security" in payload:
        value = payload.get("security")
        if value and value not in VALID_BODY_SECURITY:
            return (
                False,
                f"Invalid security '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY)}",
            )

    # Validate pmf if present
    if "pm" in payload:
        value = payload.get("pm")
        if value and value not in VALID_BODY_PMF:
            return (
                False,
                f"Invalid pmf '{value}'. Must be one of: {', '.join(VALID_BODY_PMF)}",
            )

    # Validate pmf-assoc-comeback-timeout if present
    if "pmf-assoc-comeback-timeout" in payload:
        value = payload.get("pmf-assoc-comeback-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 20:
                    return (
                        False,
                        "pmf-assoc-comeback-timeout must be between 1 and 20",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pmf-assoc-comeback-timeout must be numeric, got: {value}",
                )

    # Validate pmf-sa-query-retry-timeout if present
    if "pmf-sa-query-retry-timeout" in payload:
        value = payload.get("pmf-sa-query-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 5:
                    return (
                        False,
                        "pmf-sa-query-retry-timeout must be between 1 and 5",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pmf-sa-query-retry-timeout must be numeric, got: {value}",
                )

    # Validate beacon-protection if present
    if "beacon-protection" in payload:
        value = payload.get("beacon-protection")
        if value and value not in VALID_BODY_BEACON_PROTECTION:
            return (
                False,
                f"Invalid beacon-protection '{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_PROTECTION)}",
            )

    # Validate okc if present
    if "okc" in payload:
        value = payload.get("okc")
        if value and value not in VALID_BODY_OKC:
            return (
                False,
                f"Invalid okc '{value}'. Must be one of: {', '.join(VALID_BODY_OKC)}",
            )

    # Validate mbo if present
    if "mbo" in payload:
        value = payload.get("mbo")
        if value and value not in VALID_BODY_MBO:
            return (
                False,
                f"Invalid mbo '{value}'. Must be one of: {', '.join(VALID_BODY_MBO)}",
            )

    # Validate gas-comeback-delay if present
    if "gas-comeback-delay" in payload:
        value = payload.get("gas-comeback-delay")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 100 or int_val > 10000:
                    return (
                        False,
                        "gas-comeback-delay must be between 100 and 10000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"gas-comeback-delay must be numeric, got: {value}",
                )

    # Validate gas-fragmentation-limit if present
    if "gas-fragmentation-limit" in payload:
        value = payload.get("gas-fragmentation-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 512 or int_val > 4096:
                    return (
                        False,
                        "gas-fragmentation-limit must be between 512 and 4096",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"gas-fragmentation-limit must be numeric, got: {value}",
                )

    # Validate mbo-cell-data-conn-pref if present
    if "mbo-cell-data-conn-pre" in payload:
        value = payload.get("mbo-cell-data-conn-pre")
        if value and value not in VALID_BODY_MBO_CELL_DATA_CONN_PREF:
            return (
                False,
                f"Invalid mbo-cell-data-conn-pref '{value}'. Must be one of: {', '.join(VALID_BODY_MBO_CELL_DATA_CONN_PREF)}",
            )

    # Validate 80211k if present
    if "80211k" in payload:
        value = payload.get("80211k")
        if value and value not in VALID_BODY_80211K:
            return (
                False,
                f"Invalid 80211k '{value}'. Must be one of: {', '.join(VALID_BODY_80211K)}",
            )

    # Validate 80211v if present
    if "80211v" in payload:
        value = payload.get("80211v")
        if value and value not in VALID_BODY_80211V:
            return (
                False,
                f"Invalid 80211v '{value}'. Must be one of: {', '.join(VALID_BODY_80211V)}",
            )

    # Validate neighbor-report-dual-band if present
    if "neighbor-report-dual-band" in payload:
        value = payload.get("neighbor-report-dual-band")
        if value and value not in VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND:
            return (
                False,
                f"Invalid neighbor-report-dual-band '{value}'. Must be one of: {', '.join(VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND)}",
            )

    # Validate fast-bss-transition if present
    if "fast-bss-transition" in payload:
        value = payload.get("fast-bss-transition")
        if value and value not in VALID_BODY_FAST_BSS_TRANSITION:
            return (
                False,
                f"Invalid fast-bss-transition '{value}'. Must be one of: {', '.join(VALID_BODY_FAST_BSS_TRANSITION)}",
            )

    # Validate ft-mobility-domain if present
    if "ft-mobility-domain" in payload:
        value = payload.get("ft-mobility-domain")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "ft-mobility-domain must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ft-mobility-domain must be numeric, got: {value}",
                )

    # Validate ft-r0-key-lifetime if present
    if "ft-r0-key-lifetime" in payload:
        value = payload.get("ft-r0-key-lifetime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "ft-r0-key-lifetime must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ft-r0-key-lifetime must be numeric, got: {value}",
                )

    # Validate ft-over-ds if present
    if "ft-over-ds" in payload:
        value = payload.get("ft-over-ds")
        if value and value not in VALID_BODY_FT_OVER_DS:
            return (
                False,
                f"Invalid ft-over-ds '{value}'. Must be one of: {', '.join(VALID_BODY_FT_OVER_DS)}",
            )

    # Validate sae-groups if present
    if "sae-groups" in payload:
        value = payload.get("sae-groups")
        if value and value not in VALID_BODY_SAE_GROUPS:
            return (
                False,
                f"Invalid sae-groups '{value}'. Must be one of: {', '.join(VALID_BODY_SAE_GROUPS)}",
            )

    # Validate owe-groups if present
    if "owe-groups" in payload:
        value = payload.get("owe-groups")
        if value and value not in VALID_BODY_OWE_GROUPS:
            return (
                False,
                f"Invalid owe-groups '{value}'. Must be one of: {', '.join(VALID_BODY_OWE_GROUPS)}",
            )

    # Validate owe-transition if present
    if "owe-transition" in payload:
        value = payload.get("owe-transition")
        if value and value not in VALID_BODY_OWE_TRANSITION:
            return (
                False,
                f"Invalid owe-transition '{value}'. Must be one of: {', '.join(VALID_BODY_OWE_TRANSITION)}",
            )

    # Validate owe-transition-ssid if present
    if "owe-transition-ssid" in payload:
        value = payload.get("owe-transition-ssid")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "owe-transition-ssid cannot exceed 32 characters")

    # Validate additional-akms if present
    if "additional-akms" in payload:
        value = payload.get("additional-akms")
        if value and value not in VALID_BODY_ADDITIONAL_AKMS:
            return (
                False,
                f"Invalid additional-akms '{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_AKMS)}",
            )

    # Validate eapol-key-retries if present
    if "eapol-key-retries" in payload:
        value = payload.get("eapol-key-retries")
        if value and value not in VALID_BODY_EAPOL_KEY_RETRIES:
            return (
                False,
                f"Invalid eapol-key-retries '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_KEY_RETRIES)}",
            )

    # Validate tkip-counter-measure if present
    if "tkip-counter-measure" in payload:
        value = payload.get("tkip-counter-measure")
        if value and value not in VALID_BODY_TKIP_COUNTER_MEASURE:
            return (
                False,
                f"Invalid tkip-counter-measure '{value}'. Must be one of: {', '.join(VALID_BODY_TKIP_COUNTER_MEASURE)}",
            )

    # Validate external-web if present
    if "external-web" in payload:
        value = payload.get("external-web")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "external-web cannot exceed 1023 characters")

    # Validate external-web-format if present
    if "external-web-format" in payload:
        value = payload.get("external-web-format")
        if value and value not in VALID_BODY_EXTERNAL_WEB_FORMAT:
            return (
                False,
                f"Invalid external-web-format '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_WEB_FORMAT)}",
            )

    # Validate external-logout if present
    if "external-logout" in payload:
        value = payload.get("external-logout")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "external-logout cannot exceed 127 characters")

    # Validate mac-username-delimiter if present
    if "mac-username-delimiter" in payload:
        value = payload.get("mac-username-delimiter")
        if value and value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            return (
                False,
                f"Invalid mac-username-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_USERNAME_DELIMITER)}",
            )

    # Validate mac-password-delimiter if present
    if "mac-password-delimiter" in payload:
        value = payload.get("mac-password-delimiter")
        if value and value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            return (
                False,
                f"Invalid mac-password-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_PASSWORD_DELIMITER)}",
            )

    # Validate mac-calling-station-delimiter if present
    if "mac-calling-station-delimiter" in payload:
        value = payload.get("mac-calling-station-delimiter")
        if value and value not in VALID_BODY_MAC_CALLING_STATION_DELIMITER:
            return (
                False,
                f"Invalid mac-calling-station-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLING_STATION_DELIMITER)}",
            )

    # Validate mac-called-station-delimiter if present
    if "mac-called-station-delimiter" in payload:
        value = payload.get("mac-called-station-delimiter")
        if value and value not in VALID_BODY_MAC_CALLED_STATION_DELIMITER:
            return (
                False,
                f"Invalid mac-called-station-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLED_STATION_DELIMITER)}",
            )

    # Validate mac-case if present
    if "mac-case" in payload:
        value = payload.get("mac-case")
        if value and value not in VALID_BODY_MAC_CASE:
            return (
                False,
                f"Invalid mac-case '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CASE)}",
            )

    # Validate called-station-id-type if present
    if "called-station-id-type" in payload:
        value = payload.get("called-station-id-type")
        if value and value not in VALID_BODY_CALLED_STATION_ID_TYPE:
            return (
                False,
                f"Invalid called-station-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_CALLED_STATION_ID_TYPE)}",
            )

    # Validate mac-auth-bypass if present
    if "mac-auth-bypass" in payload:
        value = payload.get("mac-auth-bypass")
        if value and value not in VALID_BODY_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid mac-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_AUTH_BYPASS)}",
            )

    # Validate radius-mac-auth if present
    if "radius-mac-auth" in payload:
        value = payload.get("radius-mac-auth")
        if value and value not in VALID_BODY_RADIUS_MAC_AUTH:
            return (
                False,
                f"Invalid radius-mac-auth '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_AUTH)}",
            )

    # Validate radius-mac-auth-server if present
    if "radius-mac-auth-server" in payload:
        value = payload.get("radius-mac-auth-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "radius-mac-auth-server cannot exceed 35 characters",
            )

    # Validate radius-mac-auth-block-interval if present
    if "radius-mac-auth-block-interval" in payload:
        value = payload.get("radius-mac-auth-block-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 864000:
                    return (
                        False,
                        "radius-mac-auth-block-interval must be between 30 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"radius-mac-auth-block-interval must be numeric, got: {value}",
                )

    # Validate radius-mac-mpsk-auth if present
    if "radius-mac-mpsk-auth" in payload:
        value = payload.get("radius-mac-mpsk-auth")
        if value and value not in VALID_BODY_RADIUS_MAC_MPSK_AUTH:
            return (
                False,
                f"Invalid radius-mac-mpsk-auth '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_MPSK_AUTH)}",
            )

    # Validate radius-mac-mpsk-timeout if present
    if "radius-mac-mpsk-timeout" in payload:
        value = payload.get("radius-mac-mpsk-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 864000:
                    return (
                        False,
                        "radius-mac-mpsk-timeout must be between 300 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"radius-mac-mpsk-timeout must be numeric, got: {value}",
                )

    # Validate auth if present
    if "auth" in payload:
        value = payload.get("auth")
        if value and value not in VALID_BODY_AUTH:
            return (
                False,
                f"Invalid auth '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH)}",
            )

    # Validate encrypt if present
    if "encrypt" in payload:
        value = payload.get("encrypt")
        if value and value not in VALID_BODY_ENCRYPT:
            return (
                False,
                f"Invalid encrypt '{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPT)}",
            )

    # Validate keyindex if present
    if "keyindex" in payload:
        value = payload.get("keyindex")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4:
                    return (False, "keyindex must be between 1 and 4")
            except (ValueError, TypeError):
                return (False, f"keyindex must be numeric, got: {value}")

    # Validate sae-h2e-only if present
    if "sae-h2e-only" in payload:
        value = payload.get("sae-h2e-only")
        if value and value not in VALID_BODY_SAE_H2E_ONLY:
            return (
                False,
                f"Invalid sae-h2e-only '{value}'. Must be one of: {', '.join(VALID_BODY_SAE_H2E_ONLY)}",
            )

    # Validate sae-hnp-only if present
    if "sae-hnp-only" in payload:
        value = payload.get("sae-hnp-only")
        if value and value not in VALID_BODY_SAE_HNP_ONLY:
            return (
                False,
                f"Invalid sae-hnp-only '{value}'. Must be one of: {', '.join(VALID_BODY_SAE_HNP_ONLY)}",
            )

    # Validate sae-pk if present
    if "sae-pk" in payload:
        value = payload.get("sae-pk")
        if value and value not in VALID_BODY_SAE_PK:
            return (
                False,
                f"Invalid sae-pk '{value}'. Must be one of: {', '.join(VALID_BODY_SAE_PK)}",
            )

    # Validate sae-private-key if present
    if "sae-private-key" in payload:
        value = payload.get("sae-private-key")
        if value and isinstance(value, str) and len(value) > 359:
            return (False, "sae-private-key cannot exceed 359 characters")

    # Validate akm24-only if present
    if "akm24-only" in payload:
        value = payload.get("akm24-only")
        if value and value not in VALID_BODY_AKM24_ONLY:
            return (
                False,
                f"Invalid akm24-only '{value}'. Must be one of: {', '.join(VALID_BODY_AKM24_ONLY)}",
            )

    # Validate radius-server if present
    if "radius-server" in payload:
        value = payload.get("radius-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "radius-server cannot exceed 35 characters")

    # Validate nas-filter-rule if present
    if "nas-filter-rule" in payload:
        value = payload.get("nas-filter-rule")
        if value and value not in VALID_BODY_NAS_FILTER_RULE:
            return (
                False,
                f"Invalid nas-filter-rule '{value}'. Must be one of: {', '.join(VALID_BODY_NAS_FILTER_RULE)}",
            )

    # Validate domain-name-stripping if present
    if "domain-name-stripping" in payload:
        value = payload.get("domain-name-stripping")
        if value and value not in VALID_BODY_DOMAIN_NAME_STRIPPING:
            return (
                False,
                f"Invalid domain-name-stripping '{value}'. Must be one of: {', '.join(VALID_BODY_DOMAIN_NAME_STRIPPING)}",
            )

    # Validate mlo if present
    if "mlo" in payload:
        value = payload.get("mlo")
        if value and value not in VALID_BODY_MLO:
            return (
                False,
                f"Invalid mlo '{value}'. Must be one of: {', '.join(VALID_BODY_MLO)}",
            )

    # Validate local-standalone if present
    if "local-standalone" in payload:
        value = payload.get("local-standalone")
        if value and value not in VALID_BODY_LOCAL_STANDALONE:
            return (
                False,
                f"Invalid local-standalone '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE)}",
            )

    # Validate local-standalone-nat if present
    if "local-standalone-nat" in payload:
        value = payload.get("local-standalone-nat")
        if value and value not in VALID_BODY_LOCAL_STANDALONE_NAT:
            return (
                False,
                f"Invalid local-standalone-nat '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE_NAT)}",
            )

    # Validate dhcp-lease-time if present
    if "dhcp-lease-time" in payload:
        value = payload.get("dhcp-lease-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (
                        False,
                        "dhcp-lease-time must be between 300 and 8640000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-lease-time must be numeric, got: {value}",
                )

    # Validate local-standalone-dns if present
    if "local-standalone-dns" in payload:
        value = payload.get("local-standalone-dns")
        if value and value not in VALID_BODY_LOCAL_STANDALONE_DNS:
            return (
                False,
                f"Invalid local-standalone-dns '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE_DNS)}",
            )

    # Validate local-lan-partition if present
    if "local-lan-partition" in payload:
        value = payload.get("local-lan-partition")
        if value and value not in VALID_BODY_LOCAL_LAN_PARTITION:
            return (
                False,
                f"Invalid local-lan-partition '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_LAN_PARTITION)}",
            )

    # Validate local-bridging if present
    if "local-bridging" in payload:
        value = payload.get("local-bridging")
        if value and value not in VALID_BODY_LOCAL_BRIDGING:
            return (
                False,
                f"Invalid local-bridging '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_BRIDGING)}",
            )

    # Validate local-lan if present
    if "local-lan" in payload:
        value = payload.get("local-lan")
        if value and value not in VALID_BODY_LOCAL_LAN:
            return (
                False,
                f"Invalid local-lan '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_LAN)}",
            )

    # Validate local-authentication if present
    if "local-authentication" in payload:
        value = payload.get("local-authentication")
        if value and value not in VALID_BODY_LOCAL_AUTHENTICATION:
            return (
                False,
                f"Invalid local-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_AUTHENTICATION)}",
            )

    # Validate captive-portal if present
    if "captive-portal" in payload:
        value = payload.get("captive-portal")
        if value and value not in VALID_BODY_CAPTIVE_PORTAL:
            return (
                False,
                f"Invalid captive-portal '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL)}",
            )

    # Validate captive-network-assistant-bypass if present
    if "captive-network-assistant-bypass" in payload:
        value = payload.get("captive-network-assistant-bypass")
        if value and value not in VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS:
            return (
                False,
                f"Invalid captive-network-assistant-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS)}",
            )

    # Validate portal-message-override-group if present
    if "portal-message-override-group" in payload:
        value = payload.get("portal-message-override-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "portal-message-override-group cannot exceed 35 characters",
            )

    # Validate portal-type if present
    if "portal-type" in payload:
        value = payload.get("portal-type")
        if value and value not in VALID_BODY_PORTAL_TYPE:
            return (
                False,
                f"Invalid portal-type '{value}'. Must be one of: {', '.join(VALID_BODY_PORTAL_TYPE)}",
            )

    # Validate security-exempt-list if present
    if "security-exempt-list" in payload:
        value = payload.get("security-exempt-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "security-exempt-list cannot exceed 35 characters")

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

    # Validate intra-vap-privacy if present
    if "intra-vap-privacy" in payload:
        value = payload.get("intra-vap-privacy")
        if value and value not in VALID_BODY_INTRA_VAP_PRIVACY:
            return (
                False,
                f"Invalid intra-vap-privacy '{value}'. Must be one of: {', '.join(VALID_BODY_INTRA_VAP_PRIVACY)}",
            )

    # Validate ldpc if present
    if "ldpc" in payload:
        value = payload.get("ldpc")
        if value and value not in VALID_BODY_LDPC:
            return (
                False,
                f"Invalid ldpc '{value}'. Must be one of: {', '.join(VALID_BODY_LDPC)}",
            )

    # Validate high-efficiency if present
    if "high-efficiency" in payload:
        value = payload.get("high-efficiency")
        if value and value not in VALID_BODY_HIGH_EFFICIENCY:
            return (
                False,
                f"Invalid high-efficiency '{value}'. Must be one of: {', '.join(VALID_BODY_HIGH_EFFICIENCY)}",
            )

    # Validate target-wake-time if present
    if "target-wake-time" in payload:
        value = payload.get("target-wake-time")
        if value and value not in VALID_BODY_TARGET_WAKE_TIME:
            return (
                False,
                f"Invalid target-wake-time '{value}'. Must be one of: {', '.join(VALID_BODY_TARGET_WAKE_TIME)}",
            )

    # Validate port-macauth if present
    if "port-macauth" in payload:
        value = payload.get("port-macauth")
        if value and value not in VALID_BODY_PORT_MACAUTH:
            return (
                False,
                f"Invalid port-macauth '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_MACAUTH)}",
            )

    # Validate port-macauth-timeout if present
    if "port-macauth-timeout" in payload:
        value = payload.get("port-macauth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 65535:
                    return (
                        False,
                        "port-macauth-timeout must be between 60 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"port-macauth-timeout must be numeric, got: {value}",
                )

    # Validate port-macauth-reauth-timeout if present
    if "port-macauth-reauth-timeout" in payload:
        value = payload.get("port-macauth-reauth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 120 or int_val > 65535:
                    return (
                        False,
                        "port-macauth-reauth-timeout must be between 120 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"port-macauth-reauth-timeout must be numeric, got: {value}",
                )

    # Validate bss-color-partial if present
    if "bss-color-partial" in payload:
        value = payload.get("bss-color-partial")
        if value and value not in VALID_BODY_BSS_COLOR_PARTIAL:
            return (
                False,
                f"Invalid bss-color-partial '{value}'. Must be one of: {', '.join(VALID_BODY_BSS_COLOR_PARTIAL)}",
            )

    # Validate mpsk-profile if present
    if "mpsk-profile" in payload:
        value = payload.get("mpsk-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "mpsk-profile cannot exceed 35 characters")

    # Validate split-tunneling if present
    if "split-tunneling" in payload:
        value = payload.get("split-tunneling")
        if value and value not in VALID_BODY_SPLIT_TUNNELING:
            return (
                False,
                f"Invalid split-tunneling '{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING)}",
            )

    # Validate nac if present
    if "nac" in payload:
        value = payload.get("nac")
        if value and value not in VALID_BODY_NAC:
            return (
                False,
                f"Invalid nac '{value}'. Must be one of: {', '.join(VALID_BODY_NAC)}",
            )

    # Validate nac-profile if present
    if "nac-profile" in payload:
        value = payload.get("nac-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "nac-profile cannot exceed 35 characters")

    # Validate vlanid if present
    if "vlanid" in payload:
        value = payload.get("vlanid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4094:
                    return (False, "vlanid must be between 0 and 4094")
            except (ValueError, TypeError):
                return (False, f"vlanid must be numeric, got: {value}")

    # Validate vlan-auto if present
    if "vlan-auto" in payload:
        value = payload.get("vlan-auto")
        if value and value not in VALID_BODY_VLAN_AUTO:
            return (
                False,
                f"Invalid vlan-auto '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_AUTO)}",
            )

    # Validate dynamic-vlan if present
    if "dynamic-vlan" in payload:
        value = payload.get("dynamic-vlan")
        if value and value not in VALID_BODY_DYNAMIC_VLAN:
            return (
                False,
                f"Invalid dynamic-vlan '{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_VLAN)}",
            )

    # Validate captive-portal-fw-accounting if present
    if "captive-portal-fw-accounting" in payload:
        value = payload.get("captive-portal-fw-accounting")
        if value and value not in VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING:
            return (
                False,
                f"Invalid captive-portal-fw-accounting '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING)}",
            )

    # Validate captive-portal-ac-name if present
    if "captive-portal-ac-name" in payload:
        value = payload.get("captive-portal-ac-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "captive-portal-ac-name cannot exceed 35 characters",
            )

    # Validate captive-portal-auth-timeout if present
    if "captive-portal-auth-timeout" in payload:
        value = payload.get("captive-portal-auth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 864000:
                    return (
                        False,
                        "captive-portal-auth-timeout must be between 0 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"captive-portal-auth-timeout must be numeric, got: {value}",
                )

    # Validate multicast-rate if present
    if "multicast-rate" in payload:
        value = payload.get("multicast-rate")
        if value and value not in VALID_BODY_MULTICAST_RATE:
            return (
                False,
                f"Invalid multicast-rate '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_RATE)}",
            )

    # Validate multicast-enhance if present
    if "multicast-enhance" in payload:
        value = payload.get("multicast-enhance")
        if value and value not in VALID_BODY_MULTICAST_ENHANCE:
            return (
                False,
                f"Invalid multicast-enhance '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_ENHANCE)}",
            )

    # Validate igmp-snooping if present
    if "igmp-snooping" in payload:
        value = payload.get("igmp-snooping")
        if value and value not in VALID_BODY_IGMP_SNOOPING:
            return (
                False,
                f"Invalid igmp-snooping '{value}'. Must be one of: {', '.join(VALID_BODY_IGMP_SNOOPING)}",
            )

    # Validate dhcp-address-enforcement if present
    if "dhcp-address-enforcement" in payload:
        value = payload.get("dhcp-address-enforcement")
        if value and value not in VALID_BODY_DHCP_ADDRESS_ENFORCEMENT:
            return (
                False,
                f"Invalid dhcp-address-enforcement '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_ADDRESS_ENFORCEMENT)}",
            )

    # Validate broadcast-suppression if present
    if "broadcast-suppression" in payload:
        value = payload.get("broadcast-suppression")
        if value and value not in VALID_BODY_BROADCAST_SUPPRESSION:
            return (
                False,
                f"Invalid broadcast-suppression '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SUPPRESSION)}",
            )

    # Validate ipv6-rules if present
    if "ipv6-rules" in payload:
        value = payload.get("ipv6-rules")
        if value and value not in VALID_BODY_IPV6_RULES:
            return (
                False,
                f"Invalid ipv6-rules '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_RULES)}",
            )

    # Validate me-disable-thresh if present
    if "me-disable-thresh" in payload:
        value = payload.get("me-disable-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 256:
                    return (
                        False,
                        "me-disable-thresh must be between 2 and 256",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"me-disable-thresh must be numeric, got: {value}",
                )

    # Validate mu-mimo if present
    if "mu-mimo" in payload:
        value = payload.get("mu-mimo")
        if value and value not in VALID_BODY_MU_MIMO:
            return (
                False,
                f"Invalid mu-mimo '{value}'. Must be one of: {', '.join(VALID_BODY_MU_MIMO)}",
            )

    # Validate probe-resp-suppression if present
    if "probe-resp-suppression" in payload:
        value = payload.get("probe-resp-suppression")
        if value and value not in VALID_BODY_PROBE_RESP_SUPPRESSION:
            return (
                False,
                f"Invalid probe-resp-suppression '{value}'. Must be one of: {', '.join(VALID_BODY_PROBE_RESP_SUPPRESSION)}",
            )

    # Validate probe-resp-threshold if present
    if "probe-resp-threshold" in payload:
        value = payload.get("probe-resp-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "probe-resp-threshold cannot exceed 7 characters")

    # Validate radio-sensitivity if present
    if "radio-sensitivity" in payload:
        value = payload.get("radio-sensitivity")
        if value and value not in VALID_BODY_RADIO_SENSITIVITY:
            return (
                False,
                f"Invalid radio-sensitivity '{value}'. Must be one of: {', '.join(VALID_BODY_RADIO_SENSITIVITY)}",
            )

    # Validate quarantine if present
    if "quarantine" in payload:
        value = payload.get("quarantine")
        if value and value not in VALID_BODY_QUARANTINE:
            return (
                False,
                f"Invalid quarantine '{value}'. Must be one of: {', '.join(VALID_BODY_QUARANTINE)}",
            )

    # Validate radio-5g-threshold if present
    if "radio-5g-threshold" in payload:
        value = payload.get("radio-5g-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "radio-5g-threshold cannot exceed 7 characters")

    # Validate radio-2g-threshold if present
    if "radio-2g-threshold" in payload:
        value = payload.get("radio-2g-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "radio-2g-threshold cannot exceed 7 characters")

    # Validate vlan-pooling if present
    if "vlan-pooling" in payload:
        value = payload.get("vlan-pooling")
        if value and value not in VALID_BODY_VLAN_POOLING:
            return (
                False,
                f"Invalid vlan-pooling '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_POOLING)}",
            )

    # Validate dhcp-option43-insertion if present
    if "dhcp-option43-insertion" in payload:
        value = payload.get("dhcp-option43-insertion")
        if value and value not in VALID_BODY_DHCP_OPTION43_INSERTION:
            return (
                False,
                f"Invalid dhcp-option43-insertion '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION43_INSERTION)}",
            )

    # Validate dhcp-option82-insertion if present
    if "dhcp-option82-insertion" in payload:
        value = payload.get("dhcp-option82-insertion")
        if value and value not in VALID_BODY_DHCP_OPTION82_INSERTION:
            return (
                False,
                f"Invalid dhcp-option82-insertion '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_INSERTION)}",
            )

    # Validate dhcp-option82-circuit-id-insertion if present
    if "dhcp-option82-circuit-id-insertion" in payload:
        value = payload.get("dhcp-option82-circuit-id-insertion")
        if (
            value
            and value not in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION
        ):
            return (
                False,
                f"Invalid dhcp-option82-circuit-id-insertion '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION)}",
            )

    # Validate dhcp-option82-remote-id-insertion if present
    if "dhcp-option82-remote-id-insertion" in payload:
        value = payload.get("dhcp-option82-remote-id-insertion")
        if value and value not in VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION:
            return (
                False,
                f"Invalid dhcp-option82-remote-id-insertion '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION)}",
            )

    # Validate ptk-rekey if present
    if "ptk-rekey" in payload:
        value = payload.get("ptk-rekey")
        if value and value not in VALID_BODY_PTK_REKEY:
            return (
                False,
                f"Invalid ptk-rekey '{value}'. Must be one of: {', '.join(VALID_BODY_PTK_REKEY)}",
            )

    # Validate ptk-rekey-intv if present
    if "ptk-rekey-intv" in payload:
        value = payload.get("ptk-rekey-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 600 or int_val > 864000:
                    return (
                        False,
                        "ptk-rekey-intv must be between 600 and 864000",
                    )
            except (ValueError, TypeError):
                return (False, f"ptk-rekey-intv must be numeric, got: {value}")

    # Validate gtk-rekey if present
    if "gtk-rekey" in payload:
        value = payload.get("gtk-rekey")
        if value and value not in VALID_BODY_GTK_REKEY:
            return (
                False,
                f"Invalid gtk-rekey '{value}'. Must be one of: {', '.join(VALID_BODY_GTK_REKEY)}",
            )

    # Validate gtk-rekey-intv if present
    if "gtk-rekey-intv" in payload:
        value = payload.get("gtk-rekey-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 600 or int_val > 864000:
                    return (
                        False,
                        "gtk-rekey-intv must be between 600 and 864000",
                    )
            except (ValueError, TypeError):
                return (False, f"gtk-rekey-intv must be numeric, got: {value}")

    # Validate eap-reauth if present
    if "eap-reauth" in payload:
        value = payload.get("eap-reauth")
        if value and value not in VALID_BODY_EAP_REAUTH:
            return (
                False,
                f"Invalid eap-reauth '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_REAUTH)}",
            )

    # Validate eap-reauth-intv if present
    if "eap-reauth-intv" in payload:
        value = payload.get("eap-reauth-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1800 or int_val > 864000:
                    return (
                        False,
                        "eap-reauth-intv must be between 1800 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eap-reauth-intv must be numeric, got: {value}",
                )

    # Validate roaming-acct-interim-update if present
    if "roaming-acct-interim-update" in payload:
        value = payload.get("roaming-acct-interim-update")
        if value and value not in VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE:
            return (
                False,
                f"Invalid roaming-acct-interim-update '{value}'. Must be one of: {', '.join(VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE)}",
            )

    # Validate qos-profile if present
    if "qos-profile" in payload:
        value = payload.get("qos-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "qos-profile cannot exceed 35 characters")

    # Validate hotspot20-profile if present
    if "hotspot20-profile" in payload:
        value = payload.get("hotspot20-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hotspot20-profile cannot exceed 35 characters")

    # Validate access-control-list if present
    if "access-control-list" in payload:
        value = payload.get("access-control-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "access-control-list cannot exceed 35 characters")

    # Validate primary-wag-profile if present
    if "primary-wag-profile" in payload:
        value = payload.get("primary-wag-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "primary-wag-profile cannot exceed 35 characters")

    # Validate secondary-wag-profile if present
    if "secondary-wag-profile" in payload:
        value = payload.get("secondary-wag-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "secondary-wag-profile cannot exceed 35 characters",
            )

    # Validate tunnel-echo-interval if present
    if "tunnel-echo-interval" in payload:
        value = payload.get("tunnel-echo-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "tunnel-echo-interval must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tunnel-echo-interval must be numeric, got: {value}",
                )

    # Validate tunnel-fallback-interval if present
    if "tunnel-fallback-interval" in payload:
        value = payload.get("tunnel-fallback-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "tunnel-fallback-interval must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tunnel-fallback-interval must be numeric, got: {value}",
                )

    # Validate rates-11a if present
    if "rates-11a" in payload:
        value = payload.get("rates-11a")
        if value and value not in VALID_BODY_RATES_11A:
            return (
                False,
                f"Invalid rates-11a '{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11A)}",
            )

    # Validate rates-11bg if present
    if "rates-11bg" in payload:
        value = payload.get("rates-11bg")
        if value and value not in VALID_BODY_RATES_11BG:
            return (
                False,
                f"Invalid rates-11bg '{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11BG)}",
            )

    # Validate rates-11n-ss12 if present
    if "rates-11n-ss12" in payload:
        value = payload.get("rates-11n-ss12")
        if value and value not in VALID_BODY_RATES_11N_SS12:
            return (
                False,
                f"Invalid rates-11n-ss12 '{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11N_SS12)}",
            )

    # Validate rates-11n-ss34 if present
    if "rates-11n-ss34" in payload:
        value = payload.get("rates-11n-ss34")
        if value and value not in VALID_BODY_RATES_11N_SS34:
            return (
                False,
                f"Invalid rates-11n-ss34 '{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11N_SS34)}",
            )

    # Validate rates-11ac-mcs-map if present
    if "rates-11ac-mcs-map" in payload:
        value = payload.get("rates-11ac-mcs-map")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "rates-11ac-mcs-map cannot exceed 63 characters")

    # Validate rates-11ax-mcs-map if present
    if "rates-11ax-mcs-map" in payload:
        value = payload.get("rates-11ax-mcs-map")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "rates-11ax-mcs-map cannot exceed 63 characters")

    # Validate rates-11be-mcs-map if present
    if "rates-11be-mcs-map" in payload:
        value = payload.get("rates-11be-mcs-map")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "rates-11be-mcs-map cannot exceed 15 characters")

    # Validate rates-11be-mcs-map-160 if present
    if "rates-11be-mcs-map-160" in payload:
        value = payload.get("rates-11be-mcs-map-160")
        if value and isinstance(value, str) and len(value) > 15:
            return (
                False,
                "rates-11be-mcs-map-160 cannot exceed 15 characters",
            )

    # Validate rates-11be-mcs-map-320 if present
    if "rates-11be-mcs-map-320" in payload:
        value = payload.get("rates-11be-mcs-map-320")
        if value and isinstance(value, str) and len(value) > 15:
            return (
                False,
                "rates-11be-mcs-map-320 cannot exceed 15 characters",
            )

    # Validate utm-profile if present
    if "utm-profile" in payload:
        value = payload.get("utm-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "utm-profile cannot exceed 35 characters")

    # Validate utm-status if present
    if "utm-status" in payload:
        value = payload.get("utm-status")
        if value and value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid utm-status '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )

    # Validate utm-log if present
    if "utm-log" in payload:
        value = payload.get("utm-log")
        if value and value not in VALID_BODY_UTM_LOG:
            return (
                False,
                f"Invalid utm-log '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_LOG)}",
            )

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate antivirus-profile if present
    if "antivirus-profile" in payload:
        value = payload.get("antivirus-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "antivirus-profile cannot exceed 47 characters")

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate scan-botnet-connections if present
    if "scan-botnet-connections" in payload:
        value = payload.get("scan-botnet-connections")
        if value and value not in VALID_BODY_SCAN_BOTNET_CONNECTIONS:
            return (
                False,
                f"Invalid scan-botnet-connections '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_BOTNET_CONNECTIONS)}",
            )

    # Validate address-group if present
    if "address-group" in payload:
        value = payload.get("address-group")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "address-group cannot exceed 79 characters")

    # Validate address-group-policy if present
    if "address-group-policy" in payload:
        value = payload.get("address-group-policy")
        if value and value not in VALID_BODY_ADDRESS_GROUP_POLICY:
            return (
                False,
                f"Invalid address-group-policy '{value}'. Must be one of: {', '.join(VALID_BODY_ADDRESS_GROUP_POLICY)}",
            )

    # Validate sticky-client-remove if present
    if "sticky-client-remove" in payload:
        value = payload.get("sticky-client-remove")
        if value and value not in VALID_BODY_STICKY_CLIENT_REMOVE:
            return (
                False,
                f"Invalid sticky-client-remove '{value}'. Must be one of: {', '.join(VALID_BODY_STICKY_CLIENT_REMOVE)}",
            )

    # Validate sticky-client-threshold-5g if present
    if "sticky-client-threshold-5g" in payload:
        value = payload.get("sticky-client-threshold-5g")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "sticky-client-threshold-5g cannot exceed 7 characters",
            )

    # Validate sticky-client-threshold-2g if present
    if "sticky-client-threshold-2g" in payload:
        value = payload.get("sticky-client-threshold-2g")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "sticky-client-threshold-2g cannot exceed 7 characters",
            )

    # Validate sticky-client-threshold-6g if present
    if "sticky-client-threshold-6g" in payload:
        value = payload.get("sticky-client-threshold-6g")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "sticky-client-threshold-6g cannot exceed 7 characters",
            )

    # Validate bstm-rssi-disassoc-timer if present
    if "bstm-rssi-disassoc-timer" in payload:
        value = payload.get("bstm-rssi-disassoc-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2000:
                    return (
                        False,
                        "bstm-rssi-disassoc-timer must be between 1 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bstm-rssi-disassoc-timer must be numeric, got: {value}",
                )

    # Validate bstm-load-balancing-disassoc-timer if present
    if "bstm-load-balancing-disassoc-timer" in payload:
        value = payload.get("bstm-load-balancing-disassoc-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "bstm-load-balancing-disassoc-timer must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bstm-load-balancing-disassoc-timer must be numeric, got: {value}",
                )

    # Validate bstm-disassociation-imminent if present
    if "bstm-disassociation-imminent" in payload:
        value = payload.get("bstm-disassociation-imminent")
        if value and value not in VALID_BODY_BSTM_DISASSOCIATION_IMMINENT:
            return (
                False,
                f"Invalid bstm-disassociation-imminent '{value}'. Must be one of: {', '.join(VALID_BODY_BSTM_DISASSOCIATION_IMMINENT)}",
            )

    # Validate beacon-advertising if present
    if "beacon-advertising" in payload:
        value = payload.get("beacon-advertising")
        if value and value not in VALID_BODY_BEACON_ADVERTISING:
            return (
                False,
                f"Invalid beacon-advertising '{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_ADVERTISING)}",
            )

    # Validate osen if present
    if "osen" in payload:
        value = payload.get("osen")
        if value and value not in VALID_BODY_OSEN:
            return (
                False,
                f"Invalid osen '{value}'. Must be one of: {', '.join(VALID_BODY_OSEN)}",
            )

    # Validate application-detection-engine if present
    if "application-detection-engine" in payload:
        value = payload.get("application-detection-engine")
        if value and value not in VALID_BODY_APPLICATION_DETECTION_ENGINE:
            return (
                False,
                f"Invalid application-detection-engine '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_DETECTION_ENGINE)}",
            )

    # Validate application-dscp-marking if present
    if "application-dscp-marking" in payload:
        value = payload.get("application-dscp-marking")
        if value and value not in VALID_BODY_APPLICATION_DSCP_MARKING:
            return (
                False,
                f"Invalid application-dscp-marking '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_DSCP_MARKING)}",
            )

    # Validate application-report-intv if present
    if "application-report-intv" in payload:
        value = payload.get("application-report-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 864000:
                    return (
                        False,
                        "application-report-intv must be between 30 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"application-report-intv must be numeric, got: {value}",
                )

    # Validate l3-roaming if present
    if "l3-roaming" in payload:
        value = payload.get("l3-roaming")
        if value and value not in VALID_BODY_L3_ROAMING:
            return (
                False,
                f"Invalid l3-roaming '{value}'. Must be one of: {', '.join(VALID_BODY_L3_ROAMING)}",
            )

    # Validate l3-roaming-mode if present
    if "l3-roaming-mode" in payload:
        value = payload.get("l3-roaming-mode")
        if value and value not in VALID_BODY_L3_ROAMING_MODE:
            return (
                False,
                f"Invalid l3-roaming-mode '{value}'. Must be one of: {', '.join(VALID_BODY_L3_ROAMING_MODE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vap_put(
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

    # Validate pre-auth if present
    if "pre-auth" in payload:
        value = payload.get("pre-auth")
        if value and value not in VALID_BODY_PRE_AUTH:
            return (
                False,
                f"Invalid pre-auth '{value}'. Must be one of: {', '.join(VALID_BODY_PRE_AUTH)}",
            )

    # Validate external-pre-auth if present
    if "external-pre-auth" in payload:
        value = payload.get("external-pre-auth")
        if value and value not in VALID_BODY_EXTERNAL_PRE_AUTH:
            return (
                False,
                f"Invalid external-pre-auth '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_PRE_AUTH)}",
            )

    # Validate mesh-backhaul if present
    if "mesh-backhaul" in payload:
        value = payload.get("mesh-backhaul")
        if value and value not in VALID_BODY_MESH_BACKHAUL:
            return (
                False,
                f"Invalid mesh-backhaul '{value}'. Must be one of: {', '.join(VALID_BODY_MESH_BACKHAUL)}",
            )

    # Validate atf-weight if present
    if "atf-weight" in payload:
        value = payload.get("atf-weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (False, "atf-weight must be between 0 and 100")
            except (ValueError, TypeError):
                return (False, f"atf-weight must be numeric, got: {value}")

    # Validate max-clients if present
    if "max-clients" in payload:
        value = payload.get("max-clients")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-clients must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-clients must be numeric, got: {value}")

    # Validate max-clients-ap if present
    if "max-clients-ap" in payload:
        value = payload.get("max-clients-ap")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-clients-ap must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"max-clients-ap must be numeric, got: {value}")

    # Validate ssid if present
    if "ssid" in payload:
        value = payload.get("ssid")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "ssid cannot exceed 32 characters")

    # Validate broadcast-ssid if present
    if "broadcast-ssid" in payload:
        value = payload.get("broadcast-ssid")
        if value and value not in VALID_BODY_BROADCAST_SSID:
            return (
                False,
                f"Invalid broadcast-ssid '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SSID)}",
            )

    # Validate security if present
    if "security" in payload:
        value = payload.get("security")
        if value and value not in VALID_BODY_SECURITY:
            return (
                False,
                f"Invalid security '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY)}",
            )

    # Validate pmf if present
    if "pm" in payload:
        value = payload.get("pm")
        if value and value not in VALID_BODY_PMF:
            return (
                False,
                f"Invalid pmf '{value}'. Must be one of: {', '.join(VALID_BODY_PMF)}",
            )

    # Validate pmf-assoc-comeback-timeout if present
    if "pmf-assoc-comeback-timeout" in payload:
        value = payload.get("pmf-assoc-comeback-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 20:
                    return (
                        False,
                        "pmf-assoc-comeback-timeout must be between 1 and 20",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pmf-assoc-comeback-timeout must be numeric, got: {value}",
                )

    # Validate pmf-sa-query-retry-timeout if present
    if "pmf-sa-query-retry-timeout" in payload:
        value = payload.get("pmf-sa-query-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 5:
                    return (
                        False,
                        "pmf-sa-query-retry-timeout must be between 1 and 5",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pmf-sa-query-retry-timeout must be numeric, got: {value}",
                )

    # Validate beacon-protection if present
    if "beacon-protection" in payload:
        value = payload.get("beacon-protection")
        if value and value not in VALID_BODY_BEACON_PROTECTION:
            return (
                False,
                f"Invalid beacon-protection '{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_PROTECTION)}",
            )

    # Validate okc if present
    if "okc" in payload:
        value = payload.get("okc")
        if value and value not in VALID_BODY_OKC:
            return (
                False,
                f"Invalid okc '{value}'. Must be one of: {', '.join(VALID_BODY_OKC)}",
            )

    # Validate mbo if present
    if "mbo" in payload:
        value = payload.get("mbo")
        if value and value not in VALID_BODY_MBO:
            return (
                False,
                f"Invalid mbo '{value}'. Must be one of: {', '.join(VALID_BODY_MBO)}",
            )

    # Validate gas-comeback-delay if present
    if "gas-comeback-delay" in payload:
        value = payload.get("gas-comeback-delay")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 100 or int_val > 10000:
                    return (
                        False,
                        "gas-comeback-delay must be between 100 and 10000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"gas-comeback-delay must be numeric, got: {value}",
                )

    # Validate gas-fragmentation-limit if present
    if "gas-fragmentation-limit" in payload:
        value = payload.get("gas-fragmentation-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 512 or int_val > 4096:
                    return (
                        False,
                        "gas-fragmentation-limit must be between 512 and 4096",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"gas-fragmentation-limit must be numeric, got: {value}",
                )

    # Validate mbo-cell-data-conn-pref if present
    if "mbo-cell-data-conn-pre" in payload:
        value = payload.get("mbo-cell-data-conn-pre")
        if value and value not in VALID_BODY_MBO_CELL_DATA_CONN_PREF:
            return (
                False,
                f"Invalid mbo-cell-data-conn-pref '{value}'. Must be one of: {', '.join(VALID_BODY_MBO_CELL_DATA_CONN_PREF)}",
            )

    # Validate 80211k if present
    if "80211k" in payload:
        value = payload.get("80211k")
        if value and value not in VALID_BODY_80211K:
            return (
                False,
                f"Invalid 80211k '{value}'. Must be one of: {', '.join(VALID_BODY_80211K)}",
            )

    # Validate 80211v if present
    if "80211v" in payload:
        value = payload.get("80211v")
        if value and value not in VALID_BODY_80211V:
            return (
                False,
                f"Invalid 80211v '{value}'. Must be one of: {', '.join(VALID_BODY_80211V)}",
            )

    # Validate neighbor-report-dual-band if present
    if "neighbor-report-dual-band" in payload:
        value = payload.get("neighbor-report-dual-band")
        if value and value not in VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND:
            return (
                False,
                f"Invalid neighbor-report-dual-band '{value}'. Must be one of: {', '.join(VALID_BODY_NEIGHBOR_REPORT_DUAL_BAND)}",
            )

    # Validate fast-bss-transition if present
    if "fast-bss-transition" in payload:
        value = payload.get("fast-bss-transition")
        if value and value not in VALID_BODY_FAST_BSS_TRANSITION:
            return (
                False,
                f"Invalid fast-bss-transition '{value}'. Must be one of: {', '.join(VALID_BODY_FAST_BSS_TRANSITION)}",
            )

    # Validate ft-mobility-domain if present
    if "ft-mobility-domain" in payload:
        value = payload.get("ft-mobility-domain")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "ft-mobility-domain must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ft-mobility-domain must be numeric, got: {value}",
                )

    # Validate ft-r0-key-lifetime if present
    if "ft-r0-key-lifetime" in payload:
        value = payload.get("ft-r0-key-lifetime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "ft-r0-key-lifetime must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ft-r0-key-lifetime must be numeric, got: {value}",
                )

    # Validate ft-over-ds if present
    if "ft-over-ds" in payload:
        value = payload.get("ft-over-ds")
        if value and value not in VALID_BODY_FT_OVER_DS:
            return (
                False,
                f"Invalid ft-over-ds '{value}'. Must be one of: {', '.join(VALID_BODY_FT_OVER_DS)}",
            )

    # Validate sae-groups if present
    if "sae-groups" in payload:
        value = payload.get("sae-groups")
        if value and value not in VALID_BODY_SAE_GROUPS:
            return (
                False,
                f"Invalid sae-groups '{value}'. Must be one of: {', '.join(VALID_BODY_SAE_GROUPS)}",
            )

    # Validate owe-groups if present
    if "owe-groups" in payload:
        value = payload.get("owe-groups")
        if value and value not in VALID_BODY_OWE_GROUPS:
            return (
                False,
                f"Invalid owe-groups '{value}'. Must be one of: {', '.join(VALID_BODY_OWE_GROUPS)}",
            )

    # Validate owe-transition if present
    if "owe-transition" in payload:
        value = payload.get("owe-transition")
        if value and value not in VALID_BODY_OWE_TRANSITION:
            return (
                False,
                f"Invalid owe-transition '{value}'. Must be one of: {', '.join(VALID_BODY_OWE_TRANSITION)}",
            )

    # Validate owe-transition-ssid if present
    if "owe-transition-ssid" in payload:
        value = payload.get("owe-transition-ssid")
        if value and isinstance(value, str) and len(value) > 32:
            return (False, "owe-transition-ssid cannot exceed 32 characters")

    # Validate additional-akms if present
    if "additional-akms" in payload:
        value = payload.get("additional-akms")
        if value and value not in VALID_BODY_ADDITIONAL_AKMS:
            return (
                False,
                f"Invalid additional-akms '{value}'. Must be one of: {', '.join(VALID_BODY_ADDITIONAL_AKMS)}",
            )

    # Validate eapol-key-retries if present
    if "eapol-key-retries" in payload:
        value = payload.get("eapol-key-retries")
        if value and value not in VALID_BODY_EAPOL_KEY_RETRIES:
            return (
                False,
                f"Invalid eapol-key-retries '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_KEY_RETRIES)}",
            )

    # Validate tkip-counter-measure if present
    if "tkip-counter-measure" in payload:
        value = payload.get("tkip-counter-measure")
        if value and value not in VALID_BODY_TKIP_COUNTER_MEASURE:
            return (
                False,
                f"Invalid tkip-counter-measure '{value}'. Must be one of: {', '.join(VALID_BODY_TKIP_COUNTER_MEASURE)}",
            )

    # Validate external-web if present
    if "external-web" in payload:
        value = payload.get("external-web")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "external-web cannot exceed 1023 characters")

    # Validate external-web-format if present
    if "external-web-format" in payload:
        value = payload.get("external-web-format")
        if value and value not in VALID_BODY_EXTERNAL_WEB_FORMAT:
            return (
                False,
                f"Invalid external-web-format '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_WEB_FORMAT)}",
            )

    # Validate external-logout if present
    if "external-logout" in payload:
        value = payload.get("external-logout")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "external-logout cannot exceed 127 characters")

    # Validate mac-username-delimiter if present
    if "mac-username-delimiter" in payload:
        value = payload.get("mac-username-delimiter")
        if value and value not in VALID_BODY_MAC_USERNAME_DELIMITER:
            return (
                False,
                f"Invalid mac-username-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_USERNAME_DELIMITER)}",
            )

    # Validate mac-password-delimiter if present
    if "mac-password-delimiter" in payload:
        value = payload.get("mac-password-delimiter")
        if value and value not in VALID_BODY_MAC_PASSWORD_DELIMITER:
            return (
                False,
                f"Invalid mac-password-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_PASSWORD_DELIMITER)}",
            )

    # Validate mac-calling-station-delimiter if present
    if "mac-calling-station-delimiter" in payload:
        value = payload.get("mac-calling-station-delimiter")
        if value and value not in VALID_BODY_MAC_CALLING_STATION_DELIMITER:
            return (
                False,
                f"Invalid mac-calling-station-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLING_STATION_DELIMITER)}",
            )

    # Validate mac-called-station-delimiter if present
    if "mac-called-station-delimiter" in payload:
        value = payload.get("mac-called-station-delimiter")
        if value and value not in VALID_BODY_MAC_CALLED_STATION_DELIMITER:
            return (
                False,
                f"Invalid mac-called-station-delimiter '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CALLED_STATION_DELIMITER)}",
            )

    # Validate mac-case if present
    if "mac-case" in payload:
        value = payload.get("mac-case")
        if value and value not in VALID_BODY_MAC_CASE:
            return (
                False,
                f"Invalid mac-case '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_CASE)}",
            )

    # Validate called-station-id-type if present
    if "called-station-id-type" in payload:
        value = payload.get("called-station-id-type")
        if value and value not in VALID_BODY_CALLED_STATION_ID_TYPE:
            return (
                False,
                f"Invalid called-station-id-type '{value}'. Must be one of: {', '.join(VALID_BODY_CALLED_STATION_ID_TYPE)}",
            )

    # Validate mac-auth-bypass if present
    if "mac-auth-bypass" in payload:
        value = payload.get("mac-auth-bypass")
        if value and value not in VALID_BODY_MAC_AUTH_BYPASS:
            return (
                False,
                f"Invalid mac-auth-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_AUTH_BYPASS)}",
            )

    # Validate radius-mac-auth if present
    if "radius-mac-auth" in payload:
        value = payload.get("radius-mac-auth")
        if value and value not in VALID_BODY_RADIUS_MAC_AUTH:
            return (
                False,
                f"Invalid radius-mac-auth '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_AUTH)}",
            )

    # Validate radius-mac-auth-server if present
    if "radius-mac-auth-server" in payload:
        value = payload.get("radius-mac-auth-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "radius-mac-auth-server cannot exceed 35 characters",
            )

    # Validate radius-mac-auth-block-interval if present
    if "radius-mac-auth-block-interval" in payload:
        value = payload.get("radius-mac-auth-block-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 864000:
                    return (
                        False,
                        "radius-mac-auth-block-interval must be between 30 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"radius-mac-auth-block-interval must be numeric, got: {value}",
                )

    # Validate radius-mac-mpsk-auth if present
    if "radius-mac-mpsk-auth" in payload:
        value = payload.get("radius-mac-mpsk-auth")
        if value and value not in VALID_BODY_RADIUS_MAC_MPSK_AUTH:
            return (
                False,
                f"Invalid radius-mac-mpsk-auth '{value}'. Must be one of: {', '.join(VALID_BODY_RADIUS_MAC_MPSK_AUTH)}",
            )

    # Validate radius-mac-mpsk-timeout if present
    if "radius-mac-mpsk-timeout" in payload:
        value = payload.get("radius-mac-mpsk-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 864000:
                    return (
                        False,
                        "radius-mac-mpsk-timeout must be between 300 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"radius-mac-mpsk-timeout must be numeric, got: {value}",
                )

    # Validate auth if present
    if "auth" in payload:
        value = payload.get("auth")
        if value and value not in VALID_BODY_AUTH:
            return (
                False,
                f"Invalid auth '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH)}",
            )

    # Validate encrypt if present
    if "encrypt" in payload:
        value = payload.get("encrypt")
        if value and value not in VALID_BODY_ENCRYPT:
            return (
                False,
                f"Invalid encrypt '{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPT)}",
            )

    # Validate keyindex if present
    if "keyindex" in payload:
        value = payload.get("keyindex")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4:
                    return (False, "keyindex must be between 1 and 4")
            except (ValueError, TypeError):
                return (False, f"keyindex must be numeric, got: {value}")

    # Validate sae-h2e-only if present
    if "sae-h2e-only" in payload:
        value = payload.get("sae-h2e-only")
        if value and value not in VALID_BODY_SAE_H2E_ONLY:
            return (
                False,
                f"Invalid sae-h2e-only '{value}'. Must be one of: {', '.join(VALID_BODY_SAE_H2E_ONLY)}",
            )

    # Validate sae-hnp-only if present
    if "sae-hnp-only" in payload:
        value = payload.get("sae-hnp-only")
        if value and value not in VALID_BODY_SAE_HNP_ONLY:
            return (
                False,
                f"Invalid sae-hnp-only '{value}'. Must be one of: {', '.join(VALID_BODY_SAE_HNP_ONLY)}",
            )

    # Validate sae-pk if present
    if "sae-pk" in payload:
        value = payload.get("sae-pk")
        if value and value not in VALID_BODY_SAE_PK:
            return (
                False,
                f"Invalid sae-pk '{value}'. Must be one of: {', '.join(VALID_BODY_SAE_PK)}",
            )

    # Validate sae-private-key if present
    if "sae-private-key" in payload:
        value = payload.get("sae-private-key")
        if value and isinstance(value, str) and len(value) > 359:
            return (False, "sae-private-key cannot exceed 359 characters")

    # Validate akm24-only if present
    if "akm24-only" in payload:
        value = payload.get("akm24-only")
        if value and value not in VALID_BODY_AKM24_ONLY:
            return (
                False,
                f"Invalid akm24-only '{value}'. Must be one of: {', '.join(VALID_BODY_AKM24_ONLY)}",
            )

    # Validate radius-server if present
    if "radius-server" in payload:
        value = payload.get("radius-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "radius-server cannot exceed 35 characters")

    # Validate nas-filter-rule if present
    if "nas-filter-rule" in payload:
        value = payload.get("nas-filter-rule")
        if value and value not in VALID_BODY_NAS_FILTER_RULE:
            return (
                False,
                f"Invalid nas-filter-rule '{value}'. Must be one of: {', '.join(VALID_BODY_NAS_FILTER_RULE)}",
            )

    # Validate domain-name-stripping if present
    if "domain-name-stripping" in payload:
        value = payload.get("domain-name-stripping")
        if value and value not in VALID_BODY_DOMAIN_NAME_STRIPPING:
            return (
                False,
                f"Invalid domain-name-stripping '{value}'. Must be one of: {', '.join(VALID_BODY_DOMAIN_NAME_STRIPPING)}",
            )

    # Validate mlo if present
    if "mlo" in payload:
        value = payload.get("mlo")
        if value and value not in VALID_BODY_MLO:
            return (
                False,
                f"Invalid mlo '{value}'. Must be one of: {', '.join(VALID_BODY_MLO)}",
            )

    # Validate local-standalone if present
    if "local-standalone" in payload:
        value = payload.get("local-standalone")
        if value and value not in VALID_BODY_LOCAL_STANDALONE:
            return (
                False,
                f"Invalid local-standalone '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE)}",
            )

    # Validate local-standalone-nat if present
    if "local-standalone-nat" in payload:
        value = payload.get("local-standalone-nat")
        if value and value not in VALID_BODY_LOCAL_STANDALONE_NAT:
            return (
                False,
                f"Invalid local-standalone-nat '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE_NAT)}",
            )

    # Validate dhcp-lease-time if present
    if "dhcp-lease-time" in payload:
        value = payload.get("dhcp-lease-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (
                        False,
                        "dhcp-lease-time must be between 300 and 8640000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-lease-time must be numeric, got: {value}",
                )

    # Validate local-standalone-dns if present
    if "local-standalone-dns" in payload:
        value = payload.get("local-standalone-dns")
        if value and value not in VALID_BODY_LOCAL_STANDALONE_DNS:
            return (
                False,
                f"Invalid local-standalone-dns '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_STANDALONE_DNS)}",
            )

    # Validate local-lan-partition if present
    if "local-lan-partition" in payload:
        value = payload.get("local-lan-partition")
        if value and value not in VALID_BODY_LOCAL_LAN_PARTITION:
            return (
                False,
                f"Invalid local-lan-partition '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_LAN_PARTITION)}",
            )

    # Validate local-bridging if present
    if "local-bridging" in payload:
        value = payload.get("local-bridging")
        if value and value not in VALID_BODY_LOCAL_BRIDGING:
            return (
                False,
                f"Invalid local-bridging '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_BRIDGING)}",
            )

    # Validate local-lan if present
    if "local-lan" in payload:
        value = payload.get("local-lan")
        if value and value not in VALID_BODY_LOCAL_LAN:
            return (
                False,
                f"Invalid local-lan '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_LAN)}",
            )

    # Validate local-authentication if present
    if "local-authentication" in payload:
        value = payload.get("local-authentication")
        if value and value not in VALID_BODY_LOCAL_AUTHENTICATION:
            return (
                False,
                f"Invalid local-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_AUTHENTICATION)}",
            )

    # Validate captive-portal if present
    if "captive-portal" in payload:
        value = payload.get("captive-portal")
        if value and value not in VALID_BODY_CAPTIVE_PORTAL:
            return (
                False,
                f"Invalid captive-portal '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL)}",
            )

    # Validate captive-network-assistant-bypass if present
    if "captive-network-assistant-bypass" in payload:
        value = payload.get("captive-network-assistant-bypass")
        if value and value not in VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS:
            return (
                False,
                f"Invalid captive-network-assistant-bypass '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_NETWORK_ASSISTANT_BYPASS)}",
            )

    # Validate portal-message-override-group if present
    if "portal-message-override-group" in payload:
        value = payload.get("portal-message-override-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "portal-message-override-group cannot exceed 35 characters",
            )

    # Validate portal-type if present
    if "portal-type" in payload:
        value = payload.get("portal-type")
        if value and value not in VALID_BODY_PORTAL_TYPE:
            return (
                False,
                f"Invalid portal-type '{value}'. Must be one of: {', '.join(VALID_BODY_PORTAL_TYPE)}",
            )

    # Validate security-exempt-list if present
    if "security-exempt-list" in payload:
        value = payload.get("security-exempt-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "security-exempt-list cannot exceed 35 characters")

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

    # Validate intra-vap-privacy if present
    if "intra-vap-privacy" in payload:
        value = payload.get("intra-vap-privacy")
        if value and value not in VALID_BODY_INTRA_VAP_PRIVACY:
            return (
                False,
                f"Invalid intra-vap-privacy '{value}'. Must be one of: {', '.join(VALID_BODY_INTRA_VAP_PRIVACY)}",
            )

    # Validate ldpc if present
    if "ldpc" in payload:
        value = payload.get("ldpc")
        if value and value not in VALID_BODY_LDPC:
            return (
                False,
                f"Invalid ldpc '{value}'. Must be one of: {', '.join(VALID_BODY_LDPC)}",
            )

    # Validate high-efficiency if present
    if "high-efficiency" in payload:
        value = payload.get("high-efficiency")
        if value and value not in VALID_BODY_HIGH_EFFICIENCY:
            return (
                False,
                f"Invalid high-efficiency '{value}'. Must be one of: {', '.join(VALID_BODY_HIGH_EFFICIENCY)}",
            )

    # Validate target-wake-time if present
    if "target-wake-time" in payload:
        value = payload.get("target-wake-time")
        if value and value not in VALID_BODY_TARGET_WAKE_TIME:
            return (
                False,
                f"Invalid target-wake-time '{value}'. Must be one of: {', '.join(VALID_BODY_TARGET_WAKE_TIME)}",
            )

    # Validate port-macauth if present
    if "port-macauth" in payload:
        value = payload.get("port-macauth")
        if value and value not in VALID_BODY_PORT_MACAUTH:
            return (
                False,
                f"Invalid port-macauth '{value}'. Must be one of: {', '.join(VALID_BODY_PORT_MACAUTH)}",
            )

    # Validate port-macauth-timeout if present
    if "port-macauth-timeout" in payload:
        value = payload.get("port-macauth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 65535:
                    return (
                        False,
                        "port-macauth-timeout must be between 60 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"port-macauth-timeout must be numeric, got: {value}",
                )

    # Validate port-macauth-reauth-timeout if present
    if "port-macauth-reauth-timeout" in payload:
        value = payload.get("port-macauth-reauth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 120 or int_val > 65535:
                    return (
                        False,
                        "port-macauth-reauth-timeout must be between 120 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"port-macauth-reauth-timeout must be numeric, got: {value}",
                )

    # Validate bss-color-partial if present
    if "bss-color-partial" in payload:
        value = payload.get("bss-color-partial")
        if value and value not in VALID_BODY_BSS_COLOR_PARTIAL:
            return (
                False,
                f"Invalid bss-color-partial '{value}'. Must be one of: {', '.join(VALID_BODY_BSS_COLOR_PARTIAL)}",
            )

    # Validate mpsk-profile if present
    if "mpsk-profile" in payload:
        value = payload.get("mpsk-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "mpsk-profile cannot exceed 35 characters")

    # Validate split-tunneling if present
    if "split-tunneling" in payload:
        value = payload.get("split-tunneling")
        if value and value not in VALID_BODY_SPLIT_TUNNELING:
            return (
                False,
                f"Invalid split-tunneling '{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING)}",
            )

    # Validate nac if present
    if "nac" in payload:
        value = payload.get("nac")
        if value and value not in VALID_BODY_NAC:
            return (
                False,
                f"Invalid nac '{value}'. Must be one of: {', '.join(VALID_BODY_NAC)}",
            )

    # Validate nac-profile if present
    if "nac-profile" in payload:
        value = payload.get("nac-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "nac-profile cannot exceed 35 characters")

    # Validate vlanid if present
    if "vlanid" in payload:
        value = payload.get("vlanid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4094:
                    return (False, "vlanid must be between 0 and 4094")
            except (ValueError, TypeError):
                return (False, f"vlanid must be numeric, got: {value}")

    # Validate vlan-auto if present
    if "vlan-auto" in payload:
        value = payload.get("vlan-auto")
        if value and value not in VALID_BODY_VLAN_AUTO:
            return (
                False,
                f"Invalid vlan-auto '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_AUTO)}",
            )

    # Validate dynamic-vlan if present
    if "dynamic-vlan" in payload:
        value = payload.get("dynamic-vlan")
        if value and value not in VALID_BODY_DYNAMIC_VLAN:
            return (
                False,
                f"Invalid dynamic-vlan '{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_VLAN)}",
            )

    # Validate captive-portal-fw-accounting if present
    if "captive-portal-fw-accounting" in payload:
        value = payload.get("captive-portal-fw-accounting")
        if value and value not in VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING:
            return (
                False,
                f"Invalid captive-portal-fw-accounting '{value}'. Must be one of: {', '.join(VALID_BODY_CAPTIVE_PORTAL_FW_ACCOUNTING)}",
            )

    # Validate captive-portal-ac-name if present
    if "captive-portal-ac-name" in payload:
        value = payload.get("captive-portal-ac-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "captive-portal-ac-name cannot exceed 35 characters",
            )

    # Validate captive-portal-auth-timeout if present
    if "captive-portal-auth-timeout" in payload:
        value = payload.get("captive-portal-auth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 864000:
                    return (
                        False,
                        "captive-portal-auth-timeout must be between 0 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"captive-portal-auth-timeout must be numeric, got: {value}",
                )

    # Validate multicast-rate if present
    if "multicast-rate" in payload:
        value = payload.get("multicast-rate")
        if value and value not in VALID_BODY_MULTICAST_RATE:
            return (
                False,
                f"Invalid multicast-rate '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_RATE)}",
            )

    # Validate multicast-enhance if present
    if "multicast-enhance" in payload:
        value = payload.get("multicast-enhance")
        if value and value not in VALID_BODY_MULTICAST_ENHANCE:
            return (
                False,
                f"Invalid multicast-enhance '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_ENHANCE)}",
            )

    # Validate igmp-snooping if present
    if "igmp-snooping" in payload:
        value = payload.get("igmp-snooping")
        if value and value not in VALID_BODY_IGMP_SNOOPING:
            return (
                False,
                f"Invalid igmp-snooping '{value}'. Must be one of: {', '.join(VALID_BODY_IGMP_SNOOPING)}",
            )

    # Validate dhcp-address-enforcement if present
    if "dhcp-address-enforcement" in payload:
        value = payload.get("dhcp-address-enforcement")
        if value and value not in VALID_BODY_DHCP_ADDRESS_ENFORCEMENT:
            return (
                False,
                f"Invalid dhcp-address-enforcement '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_ADDRESS_ENFORCEMENT)}",
            )

    # Validate broadcast-suppression if present
    if "broadcast-suppression" in payload:
        value = payload.get("broadcast-suppression")
        if value and value not in VALID_BODY_BROADCAST_SUPPRESSION:
            return (
                False,
                f"Invalid broadcast-suppression '{value}'. Must be one of: {', '.join(VALID_BODY_BROADCAST_SUPPRESSION)}",
            )

    # Validate ipv6-rules if present
    if "ipv6-rules" in payload:
        value = payload.get("ipv6-rules")
        if value and value not in VALID_BODY_IPV6_RULES:
            return (
                False,
                f"Invalid ipv6-rules '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_RULES)}",
            )

    # Validate me-disable-thresh if present
    if "me-disable-thresh" in payload:
        value = payload.get("me-disable-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 256:
                    return (
                        False,
                        "me-disable-thresh must be between 2 and 256",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"me-disable-thresh must be numeric, got: {value}",
                )

    # Validate mu-mimo if present
    if "mu-mimo" in payload:
        value = payload.get("mu-mimo")
        if value and value not in VALID_BODY_MU_MIMO:
            return (
                False,
                f"Invalid mu-mimo '{value}'. Must be one of: {', '.join(VALID_BODY_MU_MIMO)}",
            )

    # Validate probe-resp-suppression if present
    if "probe-resp-suppression" in payload:
        value = payload.get("probe-resp-suppression")
        if value and value not in VALID_BODY_PROBE_RESP_SUPPRESSION:
            return (
                False,
                f"Invalid probe-resp-suppression '{value}'. Must be one of: {', '.join(VALID_BODY_PROBE_RESP_SUPPRESSION)}",
            )

    # Validate probe-resp-threshold if present
    if "probe-resp-threshold" in payload:
        value = payload.get("probe-resp-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "probe-resp-threshold cannot exceed 7 characters")

    # Validate radio-sensitivity if present
    if "radio-sensitivity" in payload:
        value = payload.get("radio-sensitivity")
        if value and value not in VALID_BODY_RADIO_SENSITIVITY:
            return (
                False,
                f"Invalid radio-sensitivity '{value}'. Must be one of: {', '.join(VALID_BODY_RADIO_SENSITIVITY)}",
            )

    # Validate quarantine if present
    if "quarantine" in payload:
        value = payload.get("quarantine")
        if value and value not in VALID_BODY_QUARANTINE:
            return (
                False,
                f"Invalid quarantine '{value}'. Must be one of: {', '.join(VALID_BODY_QUARANTINE)}",
            )

    # Validate radio-5g-threshold if present
    if "radio-5g-threshold" in payload:
        value = payload.get("radio-5g-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "radio-5g-threshold cannot exceed 7 characters")

    # Validate radio-2g-threshold if present
    if "radio-2g-threshold" in payload:
        value = payload.get("radio-2g-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "radio-2g-threshold cannot exceed 7 characters")

    # Validate vlan-pooling if present
    if "vlan-pooling" in payload:
        value = payload.get("vlan-pooling")
        if value and value not in VALID_BODY_VLAN_POOLING:
            return (
                False,
                f"Invalid vlan-pooling '{value}'. Must be one of: {', '.join(VALID_BODY_VLAN_POOLING)}",
            )

    # Validate dhcp-option43-insertion if present
    if "dhcp-option43-insertion" in payload:
        value = payload.get("dhcp-option43-insertion")
        if value and value not in VALID_BODY_DHCP_OPTION43_INSERTION:
            return (
                False,
                f"Invalid dhcp-option43-insertion '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION43_INSERTION)}",
            )

    # Validate dhcp-option82-insertion if present
    if "dhcp-option82-insertion" in payload:
        value = payload.get("dhcp-option82-insertion")
        if value and value not in VALID_BODY_DHCP_OPTION82_INSERTION:
            return (
                False,
                f"Invalid dhcp-option82-insertion '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_INSERTION)}",
            )

    # Validate dhcp-option82-circuit-id-insertion if present
    if "dhcp-option82-circuit-id-insertion" in payload:
        value = payload.get("dhcp-option82-circuit-id-insertion")
        if (
            value
            and value not in VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION
        ):
            return (
                False,
                f"Invalid dhcp-option82-circuit-id-insertion '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_CIRCUIT_ID_INSERTION)}",
            )

    # Validate dhcp-option82-remote-id-insertion if present
    if "dhcp-option82-remote-id-insertion" in payload:
        value = payload.get("dhcp-option82-remote-id-insertion")
        if value and value not in VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION:
            return (
                False,
                f"Invalid dhcp-option82-remote-id-insertion '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_OPTION82_REMOTE_ID_INSERTION)}",
            )

    # Validate ptk-rekey if present
    if "ptk-rekey" in payload:
        value = payload.get("ptk-rekey")
        if value and value not in VALID_BODY_PTK_REKEY:
            return (
                False,
                f"Invalid ptk-rekey '{value}'. Must be one of: {', '.join(VALID_BODY_PTK_REKEY)}",
            )

    # Validate ptk-rekey-intv if present
    if "ptk-rekey-intv" in payload:
        value = payload.get("ptk-rekey-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 600 or int_val > 864000:
                    return (
                        False,
                        "ptk-rekey-intv must be between 600 and 864000",
                    )
            except (ValueError, TypeError):
                return (False, f"ptk-rekey-intv must be numeric, got: {value}")

    # Validate gtk-rekey if present
    if "gtk-rekey" in payload:
        value = payload.get("gtk-rekey")
        if value and value not in VALID_BODY_GTK_REKEY:
            return (
                False,
                f"Invalid gtk-rekey '{value}'. Must be one of: {', '.join(VALID_BODY_GTK_REKEY)}",
            )

    # Validate gtk-rekey-intv if present
    if "gtk-rekey-intv" in payload:
        value = payload.get("gtk-rekey-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 600 or int_val > 864000:
                    return (
                        False,
                        "gtk-rekey-intv must be between 600 and 864000",
                    )
            except (ValueError, TypeError):
                return (False, f"gtk-rekey-intv must be numeric, got: {value}")

    # Validate eap-reauth if present
    if "eap-reauth" in payload:
        value = payload.get("eap-reauth")
        if value and value not in VALID_BODY_EAP_REAUTH:
            return (
                False,
                f"Invalid eap-reauth '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_REAUTH)}",
            )

    # Validate eap-reauth-intv if present
    if "eap-reauth-intv" in payload:
        value = payload.get("eap-reauth-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1800 or int_val > 864000:
                    return (
                        False,
                        "eap-reauth-intv must be between 1800 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eap-reauth-intv must be numeric, got: {value}",
                )

    # Validate roaming-acct-interim-update if present
    if "roaming-acct-interim-update" in payload:
        value = payload.get("roaming-acct-interim-update")
        if value and value not in VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE:
            return (
                False,
                f"Invalid roaming-acct-interim-update '{value}'. Must be one of: {', '.join(VALID_BODY_ROAMING_ACCT_INTERIM_UPDATE)}",
            )

    # Validate qos-profile if present
    if "qos-profile" in payload:
        value = payload.get("qos-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "qos-profile cannot exceed 35 characters")

    # Validate hotspot20-profile if present
    if "hotspot20-profile" in payload:
        value = payload.get("hotspot20-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hotspot20-profile cannot exceed 35 characters")

    # Validate access-control-list if present
    if "access-control-list" in payload:
        value = payload.get("access-control-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "access-control-list cannot exceed 35 characters")

    # Validate primary-wag-profile if present
    if "primary-wag-profile" in payload:
        value = payload.get("primary-wag-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "primary-wag-profile cannot exceed 35 characters")

    # Validate secondary-wag-profile if present
    if "secondary-wag-profile" in payload:
        value = payload.get("secondary-wag-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "secondary-wag-profile cannot exceed 35 characters",
            )

    # Validate tunnel-echo-interval if present
    if "tunnel-echo-interval" in payload:
        value = payload.get("tunnel-echo-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "tunnel-echo-interval must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tunnel-echo-interval must be numeric, got: {value}",
                )

    # Validate tunnel-fallback-interval if present
    if "tunnel-fallback-interval" in payload:
        value = payload.get("tunnel-fallback-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "tunnel-fallback-interval must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tunnel-fallback-interval must be numeric, got: {value}",
                )

    # Validate rates-11a if present
    if "rates-11a" in payload:
        value = payload.get("rates-11a")
        if value and value not in VALID_BODY_RATES_11A:
            return (
                False,
                f"Invalid rates-11a '{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11A)}",
            )

    # Validate rates-11bg if present
    if "rates-11bg" in payload:
        value = payload.get("rates-11bg")
        if value and value not in VALID_BODY_RATES_11BG:
            return (
                False,
                f"Invalid rates-11bg '{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11BG)}",
            )

    # Validate rates-11n-ss12 if present
    if "rates-11n-ss12" in payload:
        value = payload.get("rates-11n-ss12")
        if value and value not in VALID_BODY_RATES_11N_SS12:
            return (
                False,
                f"Invalid rates-11n-ss12 '{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11N_SS12)}",
            )

    # Validate rates-11n-ss34 if present
    if "rates-11n-ss34" in payload:
        value = payload.get("rates-11n-ss34")
        if value and value not in VALID_BODY_RATES_11N_SS34:
            return (
                False,
                f"Invalid rates-11n-ss34 '{value}'. Must be one of: {', '.join(VALID_BODY_RATES_11N_SS34)}",
            )

    # Validate rates-11ac-mcs-map if present
    if "rates-11ac-mcs-map" in payload:
        value = payload.get("rates-11ac-mcs-map")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "rates-11ac-mcs-map cannot exceed 63 characters")

    # Validate rates-11ax-mcs-map if present
    if "rates-11ax-mcs-map" in payload:
        value = payload.get("rates-11ax-mcs-map")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "rates-11ax-mcs-map cannot exceed 63 characters")

    # Validate rates-11be-mcs-map if present
    if "rates-11be-mcs-map" in payload:
        value = payload.get("rates-11be-mcs-map")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "rates-11be-mcs-map cannot exceed 15 characters")

    # Validate rates-11be-mcs-map-160 if present
    if "rates-11be-mcs-map-160" in payload:
        value = payload.get("rates-11be-mcs-map-160")
        if value and isinstance(value, str) and len(value) > 15:
            return (
                False,
                "rates-11be-mcs-map-160 cannot exceed 15 characters",
            )

    # Validate rates-11be-mcs-map-320 if present
    if "rates-11be-mcs-map-320" in payload:
        value = payload.get("rates-11be-mcs-map-320")
        if value and isinstance(value, str) and len(value) > 15:
            return (
                False,
                "rates-11be-mcs-map-320 cannot exceed 15 characters",
            )

    # Validate utm-profile if present
    if "utm-profile" in payload:
        value = payload.get("utm-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "utm-profile cannot exceed 35 characters")

    # Validate utm-status if present
    if "utm-status" in payload:
        value = payload.get("utm-status")
        if value and value not in VALID_BODY_UTM_STATUS:
            return (
                False,
                f"Invalid utm-status '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_STATUS)}",
            )

    # Validate utm-log if present
    if "utm-log" in payload:
        value = payload.get("utm-log")
        if value and value not in VALID_BODY_UTM_LOG:
            return (
                False,
                f"Invalid utm-log '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_LOG)}",
            )

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate antivirus-profile if present
    if "antivirus-profile" in payload:
        value = payload.get("antivirus-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "antivirus-profile cannot exceed 47 characters")

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate scan-botnet-connections if present
    if "scan-botnet-connections" in payload:
        value = payload.get("scan-botnet-connections")
        if value and value not in VALID_BODY_SCAN_BOTNET_CONNECTIONS:
            return (
                False,
                f"Invalid scan-botnet-connections '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_BOTNET_CONNECTIONS)}",
            )

    # Validate address-group if present
    if "address-group" in payload:
        value = payload.get("address-group")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "address-group cannot exceed 79 characters")

    # Validate address-group-policy if present
    if "address-group-policy" in payload:
        value = payload.get("address-group-policy")
        if value and value not in VALID_BODY_ADDRESS_GROUP_POLICY:
            return (
                False,
                f"Invalid address-group-policy '{value}'. Must be one of: {', '.join(VALID_BODY_ADDRESS_GROUP_POLICY)}",
            )

    # Validate sticky-client-remove if present
    if "sticky-client-remove" in payload:
        value = payload.get("sticky-client-remove")
        if value and value not in VALID_BODY_STICKY_CLIENT_REMOVE:
            return (
                False,
                f"Invalid sticky-client-remove '{value}'. Must be one of: {', '.join(VALID_BODY_STICKY_CLIENT_REMOVE)}",
            )

    # Validate sticky-client-threshold-5g if present
    if "sticky-client-threshold-5g" in payload:
        value = payload.get("sticky-client-threshold-5g")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "sticky-client-threshold-5g cannot exceed 7 characters",
            )

    # Validate sticky-client-threshold-2g if present
    if "sticky-client-threshold-2g" in payload:
        value = payload.get("sticky-client-threshold-2g")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "sticky-client-threshold-2g cannot exceed 7 characters",
            )

    # Validate sticky-client-threshold-6g if present
    if "sticky-client-threshold-6g" in payload:
        value = payload.get("sticky-client-threshold-6g")
        if value and isinstance(value, str) and len(value) > 7:
            return (
                False,
                "sticky-client-threshold-6g cannot exceed 7 characters",
            )

    # Validate bstm-rssi-disassoc-timer if present
    if "bstm-rssi-disassoc-timer" in payload:
        value = payload.get("bstm-rssi-disassoc-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2000:
                    return (
                        False,
                        "bstm-rssi-disassoc-timer must be between 1 and 2000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bstm-rssi-disassoc-timer must be numeric, got: {value}",
                )

    # Validate bstm-load-balancing-disassoc-timer if present
    if "bstm-load-balancing-disassoc-timer" in payload:
        value = payload.get("bstm-load-balancing-disassoc-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "bstm-load-balancing-disassoc-timer must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bstm-load-balancing-disassoc-timer must be numeric, got: {value}",
                )

    # Validate bstm-disassociation-imminent if present
    if "bstm-disassociation-imminent" in payload:
        value = payload.get("bstm-disassociation-imminent")
        if value and value not in VALID_BODY_BSTM_DISASSOCIATION_IMMINENT:
            return (
                False,
                f"Invalid bstm-disassociation-imminent '{value}'. Must be one of: {', '.join(VALID_BODY_BSTM_DISASSOCIATION_IMMINENT)}",
            )

    # Validate beacon-advertising if present
    if "beacon-advertising" in payload:
        value = payload.get("beacon-advertising")
        if value and value not in VALID_BODY_BEACON_ADVERTISING:
            return (
                False,
                f"Invalid beacon-advertising '{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_ADVERTISING)}",
            )

    # Validate osen if present
    if "osen" in payload:
        value = payload.get("osen")
        if value and value not in VALID_BODY_OSEN:
            return (
                False,
                f"Invalid osen '{value}'. Must be one of: {', '.join(VALID_BODY_OSEN)}",
            )

    # Validate application-detection-engine if present
    if "application-detection-engine" in payload:
        value = payload.get("application-detection-engine")
        if value and value not in VALID_BODY_APPLICATION_DETECTION_ENGINE:
            return (
                False,
                f"Invalid application-detection-engine '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_DETECTION_ENGINE)}",
            )

    # Validate application-dscp-marking if present
    if "application-dscp-marking" in payload:
        value = payload.get("application-dscp-marking")
        if value and value not in VALID_BODY_APPLICATION_DSCP_MARKING:
            return (
                False,
                f"Invalid application-dscp-marking '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_DSCP_MARKING)}",
            )

    # Validate application-report-intv if present
    if "application-report-intv" in payload:
        value = payload.get("application-report-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 864000:
                    return (
                        False,
                        "application-report-intv must be between 30 and 864000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"application-report-intv must be numeric, got: {value}",
                )

    # Validate l3-roaming if present
    if "l3-roaming" in payload:
        value = payload.get("l3-roaming")
        if value and value not in VALID_BODY_L3_ROAMING:
            return (
                False,
                f"Invalid l3-roaming '{value}'. Must be one of: {', '.join(VALID_BODY_L3_ROAMING)}",
            )

    # Validate l3-roaming-mode if present
    if "l3-roaming-mode" in payload:
        value = payload.get("l3-roaming-mode")
        if value and value not in VALID_BODY_L3_ROAMING_MODE:
            return (
                False,
                f"Invalid l3-roaming-mode '{value}'. Must be one of: {', '.join(VALID_BODY_L3_ROAMING_MODE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_vap_delete(name: str | None = None) -> tuple[bool, str | None]:
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
