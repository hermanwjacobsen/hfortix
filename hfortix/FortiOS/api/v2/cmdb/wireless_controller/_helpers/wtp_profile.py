"""
Validation helpers for wireless-controller wtp_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_CONTROL_MESSAGE_OFFLOAD = [
    "ebp-frame",
    "aeroscout-tag",
    "ap-list",
    "sta-list",
    "sta-cap-list",
    "stats",
    "aeroscout-mu",
    "sta-health",
    "spectral-analysis",
]
VALID_BODY_APCFG_MESH = ["enable", "disable"]
VALID_BODY_APCFG_MESH_AP_TYPE = ["ethernet", "mesh", "auto"]
VALID_BODY_APCFG_MESH_ETH_BRIDGE = ["enable", "disable"]
VALID_BODY_WAN_PORT_MODE = ["wan-lan", "wan-only"]
VALID_BODY_ENERGY_EFFICIENT_ETHERNET = ["enable", "disable"]
VALID_BODY_LED_STATE = ["enable", "disable"]
VALID_BODY_DTLS_POLICY = [
    "clear-text",
    "dtls-enabled",
    "ipsec-vpn",
    "ipsec-sn-vpn",
]
VALID_BODY_DTLS_IN_KERNEL = ["enable", "disable"]
VALID_BODY_HANDOFF_ROAMING = ["enable", "disable"]
VALID_BODY_AP_COUNTRY = [
    "--",
    "AF",
    "AL",
    "DZ",
    "AS",
    "AO",
    "AR",
    "AM",
    "AU",
    "AT",
    "AZ",
    "BS",
    "BH",
    "BD",
    "BB",
    "BY",
    "BE",
    "BZ",
    "BJ",
    "BM",
    "BT",
    "BO",
    "BA",
    "BW",
    "BR",
    "BN",
    "BG",
    "BF",
    "KH",
    "CM",
    "KY",
    "CF",
    "TD",
    "CL",
    "CN",
    "CX",
    "CO",
    "CG",
    "CD",
    "CR",
    "HR",
    "CY",
    "CZ",
    "DK",
    "DJ",
    "DM",
    "DO",
    "EC",
    "EG",
    "SV",
    "ET",
    "EE",
    "GF",
    "PF",
    "FO",
    "FJ",
    "FI",
    "FR",
    "GA",
    "GE",
    "GM",
    "DE",
    "GH",
    "GI",
    "GR",
    "GL",
    "GD",
    "GP",
    "GU",
    "GT",
    "GY",
    "HT",
    "HN",
    "HK",
    "HU",
    "IS",
    "IN",
    "ID",
    "IQ",
    "IE",
    "IM",
    "IL",
    "IT",
    "CI",
    "JM",
    "JO",
    "KZ",
    "KE",
    "KR",
    "KW",
    "LA",
    "LV",
    "LB",
    "LS",
    "LR",
    "LY",
    "LI",
    "LT",
    "LU",
    "MO",
    "MK",
    "MG",
    "MW",
    "MY",
    "MV",
    "ML",
    "MT",
    "MH",
    "MQ",
    "MR",
    "MU",
    "YT",
    "MX",
    "FM",
    "MD",
    "MC",
    "MN",
    "MA",
    "MZ",
    "MM",
    "NA",
    "NP",
    "NL",
    "AN",
    "AW",
    "NZ",
    "NI",
    "NE",
    "NG",
    "NO",
    "MP",
    "OM",
    "PK",
    "PW",
    "PA",
    "PG",
    "PY",
    "PE",
    "PH",
    "PL",
    "PT",
    "PR",
    "QA",
    "RE",
    "RO",
    "RU",
    "RW",
    "BL",
    "KN",
    "LC",
    "MF",
    "PM",
    "VC",
    "SA",
    "SN",
    "RS",
    "ME",
    "SL",
    "SG",
    "SK",
    "SI",
    "SO",
    "ZA",
    "ES",
    "LK",
    "SR",
    "SZ",
    "SE",
    "CH",
    "TW",
    "TZ",
    "TH",
    "TL",
    "TG",
    "TT",
    "TN",
    "TR",
    "TM",
    "AE",
    "TC",
    "UG",
    "UA",
    "GB",
    "US",
    "PS",
    "UY",
    "UZ",
    "VU",
    "VE",
    "VN",
    "VI",
    "WF",
    "YE",
    "ZM",
    "ZW",
    "JP",
    "CA",
]
VALID_BODY_IP_FRAGMENT_PREVENTING = ["tcp-mss-adjust", "icmp-unreachable"]
VALID_BODY_SPLIT_TUNNELING_ACL_PATH = ["tunnel", "local"]
VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET = ["enable", "disable"]
VALID_BODY_ALLOWACCESS = ["https", "ssh", "snmp"]
VALID_BODY_LOGIN_PASSWD_CHANGE = ["yes", "default", "no"]
VALID_BODY_LLDP = ["enable", "disable"]
VALID_BODY_POE_MODE = [
    "auto",
    "8023a",
    "8023at",
    "power-adapter",
    "full",
    "high",
    "low",
]
VALID_BODY_USB_PORT = ["enable", "disable"]
VALID_BODY_FREQUENCY_HANDOFF = ["enable", "disable"]
VALID_BODY_AP_HANDOFF = ["enable", "disable"]
VALID_BODY_DEFAULT_MESH_ROOT = ["enable", "disable"]
VALID_BODY_EXT_INFO_ENABLE = ["enable", "disable"]
VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT = [
    "platform-determined",
    "outdoor",
    "indoor",
]
VALID_BODY_CONSOLE_LOGIN = ["enable", "disable"]
VALID_BODY_WAN_PORT_AUTH = ["none", "802.1x"]
VALID_BODY_WAN_PORT_AUTH_METHODS = ["all", "EAP-FAST", "EAP-TLS", "EAP-PEAP"]
VALID_BODY_WAN_PORT_AUTH_MACSEC = ["enable", "disable"]
VALID_BODY_APCFG_AUTO_CERT = ["enable", "disable"]
VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL = ["none", "est", "scep"]
VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO = [
    "rsa-1024",
    "rsa-1536",
    "rsa-2048",
    "rsa-4096",
    "ec-secp256r1",
    "ec-secp384r1",
    "ec-secp521r1",
]
VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE = ["rsa", "ec"]
VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE = ["1024", "1536", "2048", "4096"]
VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME = [
    "secp256r1",
    "secp384r1",
    "secp521r1",
]
VALID_BODY_UNII_4_5GHZ_BAND = ["enable", "disable"]
VALID_BODY_ADMIN_RESTRICT_LOCAL = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wtp_profile_get(
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


def validate_wtp_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating wtp_profile.

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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate control-message-offload if present
    if "control-message-offload" in payload:
        value = payload.get("control-message-offload")
        if value and value not in VALID_BODY_CONTROL_MESSAGE_OFFLOAD:
            return (
                False,
                f"Invalid control-message-offload '{value}'. Must be one of: {', '.join(VALID_BODY_CONTROL_MESSAGE_OFFLOAD)}",
            )

    # Validate bonjour-profile if present
    if "bonjour-profile" in payload:
        value = payload.get("bonjour-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "bonjour-profile cannot exceed 35 characters")

    # Validate apcfg-profile if present
    if "apcfg-profile" in payload:
        value = payload.get("apcfg-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "apcfg-profile cannot exceed 35 characters")

    # Validate apcfg-mesh if present
    if "apcfg-mesh" in payload:
        value = payload.get("apcfg-mesh")
        if value and value not in VALID_BODY_APCFG_MESH:
            return (
                False,
                f"Invalid apcfg-mesh '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH)}",
            )

    # Validate apcfg-mesh-ap-type if present
    if "apcfg-mesh-ap-type" in payload:
        value = payload.get("apcfg-mesh-ap-type")
        if value and value not in VALID_BODY_APCFG_MESH_AP_TYPE:
            return (
                False,
                f"Invalid apcfg-mesh-ap-type '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH_AP_TYPE)}",
            )

    # Validate apcfg-mesh-ssid if present
    if "apcfg-mesh-ssid" in payload:
        value = payload.get("apcfg-mesh-ssid")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "apcfg-mesh-ssid cannot exceed 15 characters")

    # Validate apcfg-mesh-eth-bridge if present
    if "apcfg-mesh-eth-bridge" in payload:
        value = payload.get("apcfg-mesh-eth-bridge")
        if value and value not in VALID_BODY_APCFG_MESH_ETH_BRIDGE:
            return (
                False,
                f"Invalid apcfg-mesh-eth-bridge '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH_ETH_BRIDGE)}",
            )

    # Validate ble-profile if present
    if "ble-profile" in payload:
        value = payload.get("ble-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ble-profile cannot exceed 35 characters")

    # Validate lw-profile if present
    if "lw-profile" in payload:
        value = payload.get("lw-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "lw-profile cannot exceed 35 characters")

    # Validate syslog-profile if present
    if "syslog-profile" in payload:
        value = payload.get("syslog-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "syslog-profile cannot exceed 35 characters")

    # Validate wan-port-mode if present
    if "wan-port-mode" in payload:
        value = payload.get("wan-port-mode")
        if value and value not in VALID_BODY_WAN_PORT_MODE:
            return (
                False,
                f"Invalid wan-port-mode '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_MODE)}",
            )

    # Validate energy-efficient-ethernet if present
    if "energy-efficient-ethernet" in payload:
        value = payload.get("energy-efficient-ethernet")
        if value and value not in VALID_BODY_ENERGY_EFFICIENT_ETHERNET:
            return (
                False,
                f"Invalid energy-efficient-ethernet '{value}'. Must be one of: {', '.join(VALID_BODY_ENERGY_EFFICIENT_ETHERNET)}",
            )

    # Validate led-state if present
    if "led-state" in payload:
        value = payload.get("led-state")
        if value and value not in VALID_BODY_LED_STATE:
            return (
                False,
                f"Invalid led-state '{value}'. Must be one of: {', '.join(VALID_BODY_LED_STATE)}",
            )

    # Validate dtls-policy if present
    if "dtls-policy" in payload:
        value = payload.get("dtls-policy")
        if value and value not in VALID_BODY_DTLS_POLICY:
            return (
                False,
                f"Invalid dtls-policy '{value}'. Must be one of: {', '.join(VALID_BODY_DTLS_POLICY)}",
            )

    # Validate dtls-in-kernel if present
    if "dtls-in-kernel" in payload:
        value = payload.get("dtls-in-kernel")
        if value and value not in VALID_BODY_DTLS_IN_KERNEL:
            return (
                False,
                f"Invalid dtls-in-kernel '{value}'. Must be one of: {', '.join(VALID_BODY_DTLS_IN_KERNEL)}",
            )

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

    # Validate handoff-rssi if present
    if "handoff-rssi" in payload:
        value = payload.get("handoff-rssi")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 20 or int_val > 30:
                    return (False, "handoff-rssi must be between 20 and 30")
            except (ValueError, TypeError):
                return (False, f"handoff-rssi must be numeric, got: {value}")

    # Validate handoff-sta-thresh if present
    if "handoff-sta-thresh" in payload:
        value = payload.get("handoff-sta-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 60:
                    return (
                        False,
                        "handoff-sta-thresh must be between 5 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"handoff-sta-thresh must be numeric, got: {value}",
                )

    # Validate handoff-roaming if present
    if "handoff-roaming" in payload:
        value = payload.get("handoff-roaming")
        if value and value not in VALID_BODY_HANDOFF_ROAMING:
            return (
                False,
                f"Invalid handoff-roaming '{value}'. Must be one of: {', '.join(VALID_BODY_HANDOFF_ROAMING)}",
            )

    # Validate ap-country if present
    if "ap-country" in payload:
        value = payload.get("ap-country")
        if value and value not in VALID_BODY_AP_COUNTRY:
            return (
                False,
                f"Invalid ap-country '{value}'. Must be one of: {', '.join(VALID_BODY_AP_COUNTRY)}",
            )

    # Validate ip-fragment-preventing if present
    if "ip-fragment-preventing" in payload:
        value = payload.get("ip-fragment-preventing")
        if value and value not in VALID_BODY_IP_FRAGMENT_PREVENTING:
            return (
                False,
                f"Invalid ip-fragment-preventing '{value}'. Must be one of: {', '.join(VALID_BODY_IP_FRAGMENT_PREVENTING)}",
            )

    # Validate tun-mtu-uplink if present
    if "tun-mtu-uplink" in payload:
        value = payload.get("tun-mtu-uplink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 576 or int_val > 1500:
                    return (
                        False,
                        "tun-mtu-uplink must be between 576 and 1500",
                    )
            except (ValueError, TypeError):
                return (False, f"tun-mtu-uplink must be numeric, got: {value}")

    # Validate tun-mtu-downlink if present
    if "tun-mtu-downlink" in payload:
        value = payload.get("tun-mtu-downlink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 576 or int_val > 1500:
                    return (
                        False,
                        "tun-mtu-downlink must be between 576 and 1500",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tun-mtu-downlink must be numeric, got: {value}",
                )

    # Validate split-tunneling-acl-path if present
    if "split-tunneling-acl-path" in payload:
        value = payload.get("split-tunneling-acl-path")
        if value and value not in VALID_BODY_SPLIT_TUNNELING_ACL_PATH:
            return (
                False,
                f"Invalid split-tunneling-acl-path '{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING_ACL_PATH)}",
            )

    # Validate split-tunneling-acl-local-ap-subnet if present
    if "split-tunneling-acl-local-ap-subnet" in payload:
        value = payload.get("split-tunneling-acl-local-ap-subnet")
        if (
            value
            and value not in VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET
        ):
            return (
                False,
                f"Invalid split-tunneling-acl-local-ap-subnet '{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET)}",
            )

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    # Validate login-passwd-change if present
    if "login-passwd-change" in payload:
        value = payload.get("login-passwd-change")
        if value and value not in VALID_BODY_LOGIN_PASSWD_CHANGE:
            return (
                False,
                f"Invalid login-passwd-change '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWD_CHANGE)}",
            )

    # Validate lldp if present
    if "lldp" in payload:
        value = payload.get("lldp")
        if value and value not in VALID_BODY_LLDP:
            return (
                False,
                f"Invalid lldp '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP)}",
            )

    # Validate poe-mode if present
    if "poe-mode" in payload:
        value = payload.get("poe-mode")
        if value and value not in VALID_BODY_POE_MODE:
            return (
                False,
                f"Invalid poe-mode '{value}'. Must be one of: {', '.join(VALID_BODY_POE_MODE)}",
            )

    # Validate usb-port if present
    if "usb-port" in payload:
        value = payload.get("usb-port")
        if value and value not in VALID_BODY_USB_PORT:
            return (
                False,
                f"Invalid usb-port '{value}'. Must be one of: {', '.join(VALID_BODY_USB_PORT)}",
            )

    # Validate frequency-handoff if present
    if "frequency-handof" in payload:
        value = payload.get("frequency-handof")
        if value and value not in VALID_BODY_FREQUENCY_HANDOFF:
            return (
                False,
                f"Invalid frequency-handoff '{value}'. Must be one of: {', '.join(VALID_BODY_FREQUENCY_HANDOFF)}",
            )

    # Validate ap-handoff if present
    if "ap-handof" in payload:
        value = payload.get("ap-handof")
        if value and value not in VALID_BODY_AP_HANDOFF:
            return (
                False,
                f"Invalid ap-handoff '{value}'. Must be one of: {', '.join(VALID_BODY_AP_HANDOFF)}",
            )

    # Validate default-mesh-root if present
    if "default-mesh-root" in payload:
        value = payload.get("default-mesh-root")
        if value and value not in VALID_BODY_DEFAULT_MESH_ROOT:
            return (
                False,
                f"Invalid default-mesh-root '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_MESH_ROOT)}",
            )

    # Validate ext-info-enable if present
    if "ext-info-enable" in payload:
        value = payload.get("ext-info-enable")
        if value and value not in VALID_BODY_EXT_INFO_ENABLE:
            return (
                False,
                f"Invalid ext-info-enable '{value}'. Must be one of: {', '.join(VALID_BODY_EXT_INFO_ENABLE)}",
            )

    # Validate indoor-outdoor-deployment if present
    if "indoor-outdoor-deployment" in payload:
        value = payload.get("indoor-outdoor-deployment")
        if value and value not in VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT:
            return (
                False,
                f"Invalid indoor-outdoor-deployment '{value}'. Must be one of: {', '.join(VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT)}",
            )

    # Validate console-login if present
    if "console-login" in payload:
        value = payload.get("console-login")
        if value and value not in VALID_BODY_CONSOLE_LOGIN:
            return (
                False,
                f"Invalid console-login '{value}'. Must be one of: {', '.join(VALID_BODY_CONSOLE_LOGIN)}",
            )

    # Validate wan-port-auth if present
    if "wan-port-auth" in payload:
        value = payload.get("wan-port-auth")
        if value and value not in VALID_BODY_WAN_PORT_AUTH:
            return (
                False,
                f"Invalid wan-port-auth '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH)}",
            )

    # Validate wan-port-auth-usrname if present
    if "wan-port-auth-usrname" in payload:
        value = payload.get("wan-port-auth-usrname")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "wan-port-auth-usrname cannot exceed 63 characters",
            )

    # Validate wan-port-auth-methods if present
    if "wan-port-auth-methods" in payload:
        value = payload.get("wan-port-auth-methods")
        if value and value not in VALID_BODY_WAN_PORT_AUTH_METHODS:
            return (
                False,
                f"Invalid wan-port-auth-methods '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH_METHODS)}",
            )

    # Validate wan-port-auth-macsec if present
    if "wan-port-auth-macsec" in payload:
        value = payload.get("wan-port-auth-macsec")
        if value and value not in VALID_BODY_WAN_PORT_AUTH_MACSEC:
            return (
                False,
                f"Invalid wan-port-auth-macsec '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH_MACSEC)}",
            )

    # Validate apcfg-auto-cert if present
    if "apcfg-auto-cert" in payload:
        value = payload.get("apcfg-auto-cert")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT:
            return (
                False,
                f"Invalid apcfg-auto-cert '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT)}",
            )

    # Validate apcfg-auto-cert-enroll-protocol if present
    if "apcfg-auto-cert-enroll-protocol" in payload:
        value = payload.get("apcfg-auto-cert-enroll-protocol")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL:
            return (
                False,
                f"Invalid apcfg-auto-cert-enroll-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL)}",
            )

    # Validate apcfg-auto-cert-crypto-algo if present
    if "apcfg-auto-cert-crypto-algo" in payload:
        value = payload.get("apcfg-auto-cert-crypto-algo")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO:
            return (
                False,
                f"Invalid apcfg-auto-cert-crypto-algo '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO)}",
            )

    # Validate apcfg-auto-cert-est-server if present
    if "apcfg-auto-cert-est-server" in payload:
        value = payload.get("apcfg-auto-cert-est-server")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-est-server cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-est-ca-id if present
    if "apcfg-auto-cert-est-ca-id" in payload:
        value = payload.get("apcfg-auto-cert-est-ca-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-est-ca-id cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-est-http-username if present
    if "apcfg-auto-cert-est-http-username" in payload:
        value = payload.get("apcfg-auto-cert-est-http-username")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "apcfg-auto-cert-est-http-username cannot exceed 63 characters",
            )

    # Validate apcfg-auto-cert-est-subject if present
    if "apcfg-auto-cert-est-subject" in payload:
        value = payload.get("apcfg-auto-cert-est-subject")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "apcfg-auto-cert-est-subject cannot exceed 127 characters",
            )

    # Validate apcfg-auto-cert-est-subject-alt-name if present
    if "apcfg-auto-cert-est-subject-alt-name" in payload:
        value = payload.get("apcfg-auto-cert-est-subject-alt-name")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "apcfg-auto-cert-est-subject-alt-name cannot exceed 127 characters",
            )

    # Validate apcfg-auto-cert-auto-regen-days if present
    if "apcfg-auto-cert-auto-regen-days" in payload:
        value = payload.get("apcfg-auto-cert-auto-regen-days")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "apcfg-auto-cert-auto-regen-days must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"apcfg-auto-cert-auto-regen-days must be numeric, got: {value}",
                )

    # Validate apcfg-auto-cert-est-https-ca if present
    if "apcfg-auto-cert-est-https-ca" in payload:
        value = payload.get("apcfg-auto-cert-est-https-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (
                False,
                "apcfg-auto-cert-est-https-ca cannot exceed 79 characters",
            )

    # Validate apcfg-auto-cert-scep-keytype if present
    if "apcfg-auto-cert-scep-keytype" in payload:
        value = payload.get("apcfg-auto-cert-scep-keytype")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE:
            return (
                False,
                f"Invalid apcfg-auto-cert-scep-keytype '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE)}",
            )

    # Validate apcfg-auto-cert-scep-keysize if present
    if "apcfg-auto-cert-scep-keysize" in payload:
        value = payload.get("apcfg-auto-cert-scep-keysize")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE:
            return (
                False,
                f"Invalid apcfg-auto-cert-scep-keysize '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE)}",
            )

    # Validate apcfg-auto-cert-scep-ec-name if present
    if "apcfg-auto-cert-scep-ec-name" in payload:
        value = payload.get("apcfg-auto-cert-scep-ec-name")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME:
            return (
                False,
                f"Invalid apcfg-auto-cert-scep-ec-name '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME)}",
            )

    # Validate apcfg-auto-cert-scep-sub-fully-dn if present
    if "apcfg-auto-cert-scep-sub-fully-dn" in payload:
        value = payload.get("apcfg-auto-cert-scep-sub-fully-dn")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-scep-sub-fully-dn cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-scep-url if present
    if "apcfg-auto-cert-scep-url" in payload:
        value = payload.get("apcfg-auto-cert-scep-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-scep-url cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-scep-ca-id if present
    if "apcfg-auto-cert-scep-ca-id" in payload:
        value = payload.get("apcfg-auto-cert-scep-ca-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-scep-ca-id cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-scep-subject-alt-name if present
    if "apcfg-auto-cert-scep-subject-alt-name" in payload:
        value = payload.get("apcfg-auto-cert-scep-subject-alt-name")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "apcfg-auto-cert-scep-subject-alt-name cannot exceed 127 characters",
            )

    # Validate apcfg-auto-cert-scep-https-ca if present
    if "apcfg-auto-cert-scep-https-ca" in payload:
        value = payload.get("apcfg-auto-cert-scep-https-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (
                False,
                "apcfg-auto-cert-scep-https-ca cannot exceed 79 characters",
            )

    # Validate unii-4-5ghz-band if present
    if "unii-4-5ghz-band" in payload:
        value = payload.get("unii-4-5ghz-band")
        if value and value not in VALID_BODY_UNII_4_5GHZ_BAND:
            return (
                False,
                f"Invalid unii-4-5ghz-band '{value}'. Must be one of: {', '.join(VALID_BODY_UNII_4_5GHZ_BAND)}",
            )

    # Validate admin-auth-tacacs+ if present
    if "admin-auth-tacacs+" in payload:
        value = payload.get("admin-auth-tacacs+")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "admin-auth-tacacs+ cannot exceed 35 characters")

    # Validate admin-restrict-local if present
    if "admin-restrict-local" in payload:
        value = payload.get("admin-restrict-local")
        if value and value not in VALID_BODY_ADMIN_RESTRICT_LOCAL:
            return (
                False,
                f"Invalid admin-restrict-local '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_RESTRICT_LOCAL)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wtp_profile_put(
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

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate control-message-offload if present
    if "control-message-offload" in payload:
        value = payload.get("control-message-offload")
        if value and value not in VALID_BODY_CONTROL_MESSAGE_OFFLOAD:
            return (
                False,
                f"Invalid control-message-offload '{value}'. Must be one of: {', '.join(VALID_BODY_CONTROL_MESSAGE_OFFLOAD)}",
            )

    # Validate bonjour-profile if present
    if "bonjour-profile" in payload:
        value = payload.get("bonjour-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "bonjour-profile cannot exceed 35 characters")

    # Validate apcfg-profile if present
    if "apcfg-profile" in payload:
        value = payload.get("apcfg-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "apcfg-profile cannot exceed 35 characters")

    # Validate apcfg-mesh if present
    if "apcfg-mesh" in payload:
        value = payload.get("apcfg-mesh")
        if value and value not in VALID_BODY_APCFG_MESH:
            return (
                False,
                f"Invalid apcfg-mesh '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH)}",
            )

    # Validate apcfg-mesh-ap-type if present
    if "apcfg-mesh-ap-type" in payload:
        value = payload.get("apcfg-mesh-ap-type")
        if value and value not in VALID_BODY_APCFG_MESH_AP_TYPE:
            return (
                False,
                f"Invalid apcfg-mesh-ap-type '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH_AP_TYPE)}",
            )

    # Validate apcfg-mesh-ssid if present
    if "apcfg-mesh-ssid" in payload:
        value = payload.get("apcfg-mesh-ssid")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "apcfg-mesh-ssid cannot exceed 15 characters")

    # Validate apcfg-mesh-eth-bridge if present
    if "apcfg-mesh-eth-bridge" in payload:
        value = payload.get("apcfg-mesh-eth-bridge")
        if value and value not in VALID_BODY_APCFG_MESH_ETH_BRIDGE:
            return (
                False,
                f"Invalid apcfg-mesh-eth-bridge '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_MESH_ETH_BRIDGE)}",
            )

    # Validate ble-profile if present
    if "ble-profile" in payload:
        value = payload.get("ble-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ble-profile cannot exceed 35 characters")

    # Validate lw-profile if present
    if "lw-profile" in payload:
        value = payload.get("lw-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "lw-profile cannot exceed 35 characters")

    # Validate syslog-profile if present
    if "syslog-profile" in payload:
        value = payload.get("syslog-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "syslog-profile cannot exceed 35 characters")

    # Validate wan-port-mode if present
    if "wan-port-mode" in payload:
        value = payload.get("wan-port-mode")
        if value and value not in VALID_BODY_WAN_PORT_MODE:
            return (
                False,
                f"Invalid wan-port-mode '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_MODE)}",
            )

    # Validate energy-efficient-ethernet if present
    if "energy-efficient-ethernet" in payload:
        value = payload.get("energy-efficient-ethernet")
        if value and value not in VALID_BODY_ENERGY_EFFICIENT_ETHERNET:
            return (
                False,
                f"Invalid energy-efficient-ethernet '{value}'. Must be one of: {', '.join(VALID_BODY_ENERGY_EFFICIENT_ETHERNET)}",
            )

    # Validate led-state if present
    if "led-state" in payload:
        value = payload.get("led-state")
        if value and value not in VALID_BODY_LED_STATE:
            return (
                False,
                f"Invalid led-state '{value}'. Must be one of: {', '.join(VALID_BODY_LED_STATE)}",
            )

    # Validate dtls-policy if present
    if "dtls-policy" in payload:
        value = payload.get("dtls-policy")
        if value and value not in VALID_BODY_DTLS_POLICY:
            return (
                False,
                f"Invalid dtls-policy '{value}'. Must be one of: {', '.join(VALID_BODY_DTLS_POLICY)}",
            )

    # Validate dtls-in-kernel if present
    if "dtls-in-kernel" in payload:
        value = payload.get("dtls-in-kernel")
        if value and value not in VALID_BODY_DTLS_IN_KERNEL:
            return (
                False,
                f"Invalid dtls-in-kernel '{value}'. Must be one of: {', '.join(VALID_BODY_DTLS_IN_KERNEL)}",
            )

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

    # Validate handoff-rssi if present
    if "handoff-rssi" in payload:
        value = payload.get("handoff-rssi")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 20 or int_val > 30:
                    return (False, "handoff-rssi must be between 20 and 30")
            except (ValueError, TypeError):
                return (False, f"handoff-rssi must be numeric, got: {value}")

    # Validate handoff-sta-thresh if present
    if "handoff-sta-thresh" in payload:
        value = payload.get("handoff-sta-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 60:
                    return (
                        False,
                        "handoff-sta-thresh must be between 5 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"handoff-sta-thresh must be numeric, got: {value}",
                )

    # Validate handoff-roaming if present
    if "handoff-roaming" in payload:
        value = payload.get("handoff-roaming")
        if value and value not in VALID_BODY_HANDOFF_ROAMING:
            return (
                False,
                f"Invalid handoff-roaming '{value}'. Must be one of: {', '.join(VALID_BODY_HANDOFF_ROAMING)}",
            )

    # Validate ap-country if present
    if "ap-country" in payload:
        value = payload.get("ap-country")
        if value and value not in VALID_BODY_AP_COUNTRY:
            return (
                False,
                f"Invalid ap-country '{value}'. Must be one of: {', '.join(VALID_BODY_AP_COUNTRY)}",
            )

    # Validate ip-fragment-preventing if present
    if "ip-fragment-preventing" in payload:
        value = payload.get("ip-fragment-preventing")
        if value and value not in VALID_BODY_IP_FRAGMENT_PREVENTING:
            return (
                False,
                f"Invalid ip-fragment-preventing '{value}'. Must be one of: {', '.join(VALID_BODY_IP_FRAGMENT_PREVENTING)}",
            )

    # Validate tun-mtu-uplink if present
    if "tun-mtu-uplink" in payload:
        value = payload.get("tun-mtu-uplink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 576 or int_val > 1500:
                    return (
                        False,
                        "tun-mtu-uplink must be between 576 and 1500",
                    )
            except (ValueError, TypeError):
                return (False, f"tun-mtu-uplink must be numeric, got: {value}")

    # Validate tun-mtu-downlink if present
    if "tun-mtu-downlink" in payload:
        value = payload.get("tun-mtu-downlink")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 576 or int_val > 1500:
                    return (
                        False,
                        "tun-mtu-downlink must be between 576 and 1500",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tun-mtu-downlink must be numeric, got: {value}",
                )

    # Validate split-tunneling-acl-path if present
    if "split-tunneling-acl-path" in payload:
        value = payload.get("split-tunneling-acl-path")
        if value and value not in VALID_BODY_SPLIT_TUNNELING_ACL_PATH:
            return (
                False,
                f"Invalid split-tunneling-acl-path '{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING_ACL_PATH)}",
            )

    # Validate split-tunneling-acl-local-ap-subnet if present
    if "split-tunneling-acl-local-ap-subnet" in payload:
        value = payload.get("split-tunneling-acl-local-ap-subnet")
        if (
            value
            and value not in VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET
        ):
            return (
                False,
                f"Invalid split-tunneling-acl-local-ap-subnet '{value}'. Must be one of: {', '.join(VALID_BODY_SPLIT_TUNNELING_ACL_LOCAL_AP_SUBNET)}",
            )

    # Validate allowaccess if present
    if "allowaccess" in payload:
        value = payload.get("allowaccess")
        if value and value not in VALID_BODY_ALLOWACCESS:
            return (
                False,
                f"Invalid allowaccess '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOWACCESS)}",
            )

    # Validate login-passwd-change if present
    if "login-passwd-change" in payload:
        value = payload.get("login-passwd-change")
        if value and value not in VALID_BODY_LOGIN_PASSWD_CHANGE:
            return (
                False,
                f"Invalid login-passwd-change '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_PASSWD_CHANGE)}",
            )

    # Validate lldp if present
    if "lldp" in payload:
        value = payload.get("lldp")
        if value and value not in VALID_BODY_LLDP:
            return (
                False,
                f"Invalid lldp '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP)}",
            )

    # Validate poe-mode if present
    if "poe-mode" in payload:
        value = payload.get("poe-mode")
        if value and value not in VALID_BODY_POE_MODE:
            return (
                False,
                f"Invalid poe-mode '{value}'. Must be one of: {', '.join(VALID_BODY_POE_MODE)}",
            )

    # Validate usb-port if present
    if "usb-port" in payload:
        value = payload.get("usb-port")
        if value and value not in VALID_BODY_USB_PORT:
            return (
                False,
                f"Invalid usb-port '{value}'. Must be one of: {', '.join(VALID_BODY_USB_PORT)}",
            )

    # Validate frequency-handoff if present
    if "frequency-handof" in payload:
        value = payload.get("frequency-handof")
        if value and value not in VALID_BODY_FREQUENCY_HANDOFF:
            return (
                False,
                f"Invalid frequency-handoff '{value}'. Must be one of: {', '.join(VALID_BODY_FREQUENCY_HANDOFF)}",
            )

    # Validate ap-handoff if present
    if "ap-handof" in payload:
        value = payload.get("ap-handof")
        if value and value not in VALID_BODY_AP_HANDOFF:
            return (
                False,
                f"Invalid ap-handoff '{value}'. Must be one of: {', '.join(VALID_BODY_AP_HANDOFF)}",
            )

    # Validate default-mesh-root if present
    if "default-mesh-root" in payload:
        value = payload.get("default-mesh-root")
        if value and value not in VALID_BODY_DEFAULT_MESH_ROOT:
            return (
                False,
                f"Invalid default-mesh-root '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_MESH_ROOT)}",
            )

    # Validate ext-info-enable if present
    if "ext-info-enable" in payload:
        value = payload.get("ext-info-enable")
        if value and value not in VALID_BODY_EXT_INFO_ENABLE:
            return (
                False,
                f"Invalid ext-info-enable '{value}'. Must be one of: {', '.join(VALID_BODY_EXT_INFO_ENABLE)}",
            )

    # Validate indoor-outdoor-deployment if present
    if "indoor-outdoor-deployment" in payload:
        value = payload.get("indoor-outdoor-deployment")
        if value and value not in VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT:
            return (
                False,
                f"Invalid indoor-outdoor-deployment '{value}'. Must be one of: {', '.join(VALID_BODY_INDOOR_OUTDOOR_DEPLOYMENT)}",
            )

    # Validate console-login if present
    if "console-login" in payload:
        value = payload.get("console-login")
        if value and value not in VALID_BODY_CONSOLE_LOGIN:
            return (
                False,
                f"Invalid console-login '{value}'. Must be one of: {', '.join(VALID_BODY_CONSOLE_LOGIN)}",
            )

    # Validate wan-port-auth if present
    if "wan-port-auth" in payload:
        value = payload.get("wan-port-auth")
        if value and value not in VALID_BODY_WAN_PORT_AUTH:
            return (
                False,
                f"Invalid wan-port-auth '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH)}",
            )

    # Validate wan-port-auth-usrname if present
    if "wan-port-auth-usrname" in payload:
        value = payload.get("wan-port-auth-usrname")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "wan-port-auth-usrname cannot exceed 63 characters",
            )

    # Validate wan-port-auth-methods if present
    if "wan-port-auth-methods" in payload:
        value = payload.get("wan-port-auth-methods")
        if value and value not in VALID_BODY_WAN_PORT_AUTH_METHODS:
            return (
                False,
                f"Invalid wan-port-auth-methods '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH_METHODS)}",
            )

    # Validate wan-port-auth-macsec if present
    if "wan-port-auth-macsec" in payload:
        value = payload.get("wan-port-auth-macsec")
        if value and value not in VALID_BODY_WAN_PORT_AUTH_MACSEC:
            return (
                False,
                f"Invalid wan-port-auth-macsec '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_PORT_AUTH_MACSEC)}",
            )

    # Validate apcfg-auto-cert if present
    if "apcfg-auto-cert" in payload:
        value = payload.get("apcfg-auto-cert")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT:
            return (
                False,
                f"Invalid apcfg-auto-cert '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT)}",
            )

    # Validate apcfg-auto-cert-enroll-protocol if present
    if "apcfg-auto-cert-enroll-protocol" in payload:
        value = payload.get("apcfg-auto-cert-enroll-protocol")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL:
            return (
                False,
                f"Invalid apcfg-auto-cert-enroll-protocol '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_ENROLL_PROTOCOL)}",
            )

    # Validate apcfg-auto-cert-crypto-algo if present
    if "apcfg-auto-cert-crypto-algo" in payload:
        value = payload.get("apcfg-auto-cert-crypto-algo")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO:
            return (
                False,
                f"Invalid apcfg-auto-cert-crypto-algo '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_CRYPTO_ALGO)}",
            )

    # Validate apcfg-auto-cert-est-server if present
    if "apcfg-auto-cert-est-server" in payload:
        value = payload.get("apcfg-auto-cert-est-server")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-est-server cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-est-ca-id if present
    if "apcfg-auto-cert-est-ca-id" in payload:
        value = payload.get("apcfg-auto-cert-est-ca-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-est-ca-id cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-est-http-username if present
    if "apcfg-auto-cert-est-http-username" in payload:
        value = payload.get("apcfg-auto-cert-est-http-username")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "apcfg-auto-cert-est-http-username cannot exceed 63 characters",
            )

    # Validate apcfg-auto-cert-est-subject if present
    if "apcfg-auto-cert-est-subject" in payload:
        value = payload.get("apcfg-auto-cert-est-subject")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "apcfg-auto-cert-est-subject cannot exceed 127 characters",
            )

    # Validate apcfg-auto-cert-est-subject-alt-name if present
    if "apcfg-auto-cert-est-subject-alt-name" in payload:
        value = payload.get("apcfg-auto-cert-est-subject-alt-name")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "apcfg-auto-cert-est-subject-alt-name cannot exceed 127 characters",
            )

    # Validate apcfg-auto-cert-auto-regen-days if present
    if "apcfg-auto-cert-auto-regen-days" in payload:
        value = payload.get("apcfg-auto-cert-auto-regen-days")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "apcfg-auto-cert-auto-regen-days must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"apcfg-auto-cert-auto-regen-days must be numeric, got: {value}",
                )

    # Validate apcfg-auto-cert-est-https-ca if present
    if "apcfg-auto-cert-est-https-ca" in payload:
        value = payload.get("apcfg-auto-cert-est-https-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (
                False,
                "apcfg-auto-cert-est-https-ca cannot exceed 79 characters",
            )

    # Validate apcfg-auto-cert-scep-keytype if present
    if "apcfg-auto-cert-scep-keytype" in payload:
        value = payload.get("apcfg-auto-cert-scep-keytype")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE:
            return (
                False,
                f"Invalid apcfg-auto-cert-scep-keytype '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYTYPE)}",
            )

    # Validate apcfg-auto-cert-scep-keysize if present
    if "apcfg-auto-cert-scep-keysize" in payload:
        value = payload.get("apcfg-auto-cert-scep-keysize")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE:
            return (
                False,
                f"Invalid apcfg-auto-cert-scep-keysize '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_KEYSIZE)}",
            )

    # Validate apcfg-auto-cert-scep-ec-name if present
    if "apcfg-auto-cert-scep-ec-name" in payload:
        value = payload.get("apcfg-auto-cert-scep-ec-name")
        if value and value not in VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME:
            return (
                False,
                f"Invalid apcfg-auto-cert-scep-ec-name '{value}'. Must be one of: {', '.join(VALID_BODY_APCFG_AUTO_CERT_SCEP_EC_NAME)}",
            )

    # Validate apcfg-auto-cert-scep-sub-fully-dn if present
    if "apcfg-auto-cert-scep-sub-fully-dn" in payload:
        value = payload.get("apcfg-auto-cert-scep-sub-fully-dn")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-scep-sub-fully-dn cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-scep-url if present
    if "apcfg-auto-cert-scep-url" in payload:
        value = payload.get("apcfg-auto-cert-scep-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-scep-url cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-scep-ca-id if present
    if "apcfg-auto-cert-scep-ca-id" in payload:
        value = payload.get("apcfg-auto-cert-scep-ca-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "apcfg-auto-cert-scep-ca-id cannot exceed 255 characters",
            )

    # Validate apcfg-auto-cert-scep-subject-alt-name if present
    if "apcfg-auto-cert-scep-subject-alt-name" in payload:
        value = payload.get("apcfg-auto-cert-scep-subject-alt-name")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "apcfg-auto-cert-scep-subject-alt-name cannot exceed 127 characters",
            )

    # Validate apcfg-auto-cert-scep-https-ca if present
    if "apcfg-auto-cert-scep-https-ca" in payload:
        value = payload.get("apcfg-auto-cert-scep-https-ca")
        if value and isinstance(value, str) and len(value) > 79:
            return (
                False,
                "apcfg-auto-cert-scep-https-ca cannot exceed 79 characters",
            )

    # Validate unii-4-5ghz-band if present
    if "unii-4-5ghz-band" in payload:
        value = payload.get("unii-4-5ghz-band")
        if value and value not in VALID_BODY_UNII_4_5GHZ_BAND:
            return (
                False,
                f"Invalid unii-4-5ghz-band '{value}'. Must be one of: {', '.join(VALID_BODY_UNII_4_5GHZ_BAND)}",
            )

    # Validate admin-auth-tacacs+ if present
    if "admin-auth-tacacs+" in payload:
        value = payload.get("admin-auth-tacacs+")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "admin-auth-tacacs+ cannot exceed 35 characters")

    # Validate admin-restrict-local if present
    if "admin-restrict-local" in payload:
        value = payload.get("admin-restrict-local")
        if value and value not in VALID_BODY_ADMIN_RESTRICT_LOCAL:
            return (
                False,
                f"Invalid admin-restrict-local '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_RESTRICT_LOCAL)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_wtp_profile_delete(
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
