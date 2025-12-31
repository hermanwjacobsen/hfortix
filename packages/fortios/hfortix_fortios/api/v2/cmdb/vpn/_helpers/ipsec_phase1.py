"""
Validation helpers for vpn ipsec_phase1 endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = ["static", "dynamic", "ddns"]
VALID_BODY_IKE_VERSION = ["1", "2"]
VALID_BODY_AUTHMETHOD = ["psk", "signature"]
VALID_BODY_AUTHMETHOD_REMOTE = ["psk", "signature"]
VALID_BODY_MODE = ["aggressive", "main"]
VALID_BODY_PEERTYPE = ["any", "one", "dialup", "peer", "peergrp"]
VALID_BODY_MODE_CFG = ["disable", "enable"]
VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR = ["disable", "enable"]
VALID_BODY_ASSIGN_IP = ["disable", "enable"]
VALID_BODY_ASSIGN_IP_FROM = ["range", "usrgrp", "dhcp", "name"]
VALID_BODY_DNS_MODE = ["manual", "auto"]
VALID_BODY_UNITY_SUPPORT = ["disable", "enable"]
VALID_BODY_INCLUDE_LOCAL_LAN = ["disable", "enable"]
VALID_BODY_SAVE_PASSWORD = ["disable", "enable"]
VALID_BODY_CLIENT_AUTO_NEGOTIATE = ["disable", "enable"]
VALID_BODY_CLIENT_KEEP_ALIVE = ["disable", "enable"]
VALID_BODY_PROPOSAL = [
    "des-md5",
    "des-sha1",
    "des-sha256",
    "des-sha384",
    "des-sha512",
    "3des-md5",
    "3des-sha1",
    "3des-sha256",
    "3des-sha384",
    "3des-sha512",
    "aes128-md5",
    "aes128-sha1",
    "aes128-sha256",
    "aes128-sha384",
    "aes128-sha512",
    "aes128gcm-prfsha1",
    "aes128gcm-prfsha256",
    "aes128gcm-prfsha384",
    "aes128gcm-prfsha512",
    "aes192-md5",
    "aes192-sha1",
    "aes192-sha256",
    "aes192-sha384",
    "aes192-sha512",
    "aes256-md5",
    "aes256-sha1",
    "aes256-sha256",
    "aes256-sha384",
    "aes256-sha512",
    "aes256gcm-prfsha1",
    "aes256gcm-prfsha256",
    "aes256gcm-prfsha384",
    "aes256gcm-prfsha512",
    "chacha20poly1305-prfsha1",
    "chacha20poly1305-prfsha256",
    "chacha20poly1305-prfsha384",
    "chacha20poly1305-prfsha512",
    "aria128-md5",
    "aria128-sha1",
    "aria128-sha256",
    "aria128-sha384",
    "aria128-sha512",
    "aria192-md5",
    "aria192-sha1",
    "aria192-sha256",
    "aria192-sha384",
    "aria192-sha512",
    "aria256-md5",
    "aria256-sha1",
    "aria256-sha256",
    "aria256-sha384",
    "aria256-sha512",
    "seed-md5",
    "seed-sha1",
    "seed-sha256",
    "seed-sha384",
    "seed-sha512",
]
VALID_BODY_ADD_ROUTE = ["disable", "enable"]
VALID_BODY_ADD_GW_ROUTE = ["enable", "disable"]
VALID_BODY_LOCALID_TYPE = [
    "auto",
    "fqdn",
    "user-fqdn",
    "keyid",
    "address",
    "asn1dn",
]
VALID_BODY_AUTO_NEGOTIATE = ["enable", "disable"]
VALID_BODY_FRAGMENTATION = ["enable", "disable"]
VALID_BODY_DPD = ["disable", "on-idle", "on-demand"]
VALID_BODY_NPU_OFFLOAD = ["enable", "disable"]
VALID_BODY_SEND_CERT_CHAIN = ["enable", "disable"]
VALID_BODY_DHGRP = [
    "1",
    "2",
    "5",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
]
VALID_BODY_ADDKE1 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE2 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE3 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE4 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE5 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE6 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_ADDKE7 = [
    "0",
    "35",
    "36",
    "37",
    "1080",
    "1081",
    "1082",
    "1083",
    "1084",
    "1085",
    "1089",
    "1090",
    "1091",
    "1092",
    "1093",
    "1094",
]
VALID_BODY_SUITE_B = ["disable", "suite-b-gcm-128", "suite-b-gcm-256"]
VALID_BODY_EAP = ["enable", "disable"]
VALID_BODY_EAP_IDENTITY = ["use-id-payload", "send-request"]
VALID_BODY_EAP_CERT_AUTH = ["enable", "disable"]
VALID_BODY_ACCT_VERIFY = ["enable", "disable"]
VALID_BODY_PPK = ["disable", "allow", "require"]
VALID_BODY_WIZARD_TYPE = [
    "custom",
    "dialup-forticlient",
    "dialup-ios",
    "dialup-android",
    "dialup-windows",
    "dialup-cisco",
    "static-fortigate",
    "dialup-fortigate",
    "static-cisco",
    "dialup-cisco-fw",
    "simplified-static-fortigate",
    "hub-fortigate-auto-discovery",
    "spoke-fortigate-auto-discovery",
    "fabric-overlay-orchestrator",
]
VALID_BODY_XAUTHTYPE = ["disable", "client", "pap", "chap", "auto"]
VALID_BODY_REAUTH = ["disable", "enable"]
VALID_BODY_GROUP_AUTHENTICATION = ["enable", "disable"]
VALID_BODY_MESH_SELECTOR_TYPE = ["disable", "subnet", "host"]
VALID_BODY_IDLE_TIMEOUT = ["enable", "disable"]
VALID_BODY_SHARED_IDLE_TIMEOUT = ["enable", "disable"]
VALID_BODY_HA_SYNC_ESP_SEQNO = ["enable", "disable"]
VALID_BODY_FGSP_SYNC = ["enable", "disable"]
VALID_BODY_INBOUND_DSCP_COPY = ["enable", "disable"]
VALID_BODY_NATTRAVERSAL = ["enable", "disable", "forced"]
VALID_BODY_CHILDLESS_IKE = ["enable", "disable"]
VALID_BODY_AZURE_AD_AUTOCONNECT = ["enable", "disable"]
VALID_BODY_CLIENT_RESUME = ["enable", "disable"]
VALID_BODY_REKEY = ["enable", "disable"]
VALID_BODY_DIGITAL_SIGNATURE_AUTH = ["enable", "disable"]
VALID_BODY_SIGNATURE_HASH_ALG = ["sha1", "sha2-256", "sha2-384", "sha2-512"]
VALID_BODY_RSA_SIGNATURE_FORMAT = ["pkcs1", "pss"]
VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE = ["enable", "disable"]
VALID_BODY_ENFORCE_UNIQUE_ID = ["disable", "keep-new", "keep-old"]
VALID_BODY_CERT_ID_VALIDATION = ["enable", "disable"]
VALID_BODY_FEC_EGRESS = ["enable", "disable"]
VALID_BODY_FEC_CODEC = ["rs", "xor"]
VALID_BODY_FEC_INGRESS = ["enable", "disable"]
VALID_BODY_NETWORK_OVERLAY = ["disable", "enable"]
VALID_BODY_DEV_ID_NOTIFICATION = ["disable", "enable"]
VALID_BODY_LOOPBACK_ASYMROUTE = ["enable", "disable"]
VALID_BODY_EXCHANGE_FGT_DEVICE_ID = ["enable", "disable"]
VALID_BODY_IPV6_AUTO_LINKLOCAL = ["enable", "disable"]
VALID_BODY_EMS_SN_CHECK = ["enable", "disable"]
VALID_BODY_CERT_TRUST_STORE = ["local", "ems"]
VALID_BODY_QKD = ["disable", "allow", "require"]
VALID_BODY_QKD_HYBRID = ["disable", "allow", "require"]
VALID_BODY_TRANSPORT = ["udp", "auto", "tcp"]
VALID_BODY_FORTINET_ESP = ["enable", "disable"]
VALID_BODY_REMOTE_GW_MATCH = ["any", "ipmask", "iprange", "geography", "ztna"]
VALID_BODY_REMOTE_GW6_MATCH = ["any", "ipprefix", "iprange", "geography"]
VALID_BODY_CERT_PEER_USERNAME_VALIDATION = [
    "none",
    "othername",
    "rfc822name",
    "cn",
]
VALID_BODY_CERT_PEER_USERNAME_STRIP = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ipsec_phase1_get(
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


def validate_ipsec_phase1_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ipsec_phase1.

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

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate ike-version if present
    if "ike-version" in payload:
        value = payload.get("ike-version")
        if value and value not in VALID_BODY_IKE_VERSION:
            return (
                False,
                f"Invalid ike-version '{value}'. Must be one of: {', '.join(VALID_BODY_IKE_VERSION)}",
            )

    # Validate remotegw-ddns if present
    if "remotegw-ddns" in payload:
        value = payload.get("remotegw-ddns")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "remotegw-ddns cannot exceed 63 characters")

    # Validate keylife if present
    if "keylife" in payload:
        value = payload.get("keylife")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 120 or int_val > 172800:
                    return (False, "keylife must be between 120 and 172800")
            except (ValueError, TypeError):
                return (False, f"keylife must be numeric, got: {value}")

    # Validate authmethod if present
    if "authmethod" in payload:
        value = payload.get("authmethod")
        if value and value not in VALID_BODY_AUTHMETHOD:
            return (
                False,
                f"Invalid authmethod '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHMETHOD)}",
            )

    # Validate authmethod-remote if present
    if "authmethod-remote" in payload:
        value = payload.get("authmethod-remote")
        if value and value not in VALID_BODY_AUTHMETHOD_REMOTE:
            return (
                False,
                f"Invalid authmethod-remote '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHMETHOD_REMOTE)}",
            )

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate peertype if present
    if "peertype" in payload:
        value = payload.get("peertype")
        if value and value not in VALID_BODY_PEERTYPE:
            return (
                False,
                f"Invalid peertype '{value}'. Must be one of: {', '.join(VALID_BODY_PEERTYPE)}",
            )

    # Validate peerid if present
    if "peerid" in payload:
        value = payload.get("peerid")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "peerid cannot exceed 255 characters")

    # Validate usrgrp if present
    if "usrgrp" in payload:
        value = payload.get("usrgrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "usrgrp cannot exceed 35 characters")

    # Validate peer if present
    if "peer" in payload:
        value = payload.get("peer")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "peer cannot exceed 35 characters")

    # Validate peergrp if present
    if "peergrp" in payload:
        value = payload.get("peergrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "peergrp cannot exceed 35 characters")

    # Validate mode-cfg if present
    if "mode-cfg" in payload:
        value = payload.get("mode-cfg")
        if value and value not in VALID_BODY_MODE_CFG:
            return (
                False,
                f"Invalid mode-cfg '{value}'. Must be one of: {', '.join(VALID_BODY_MODE_CFG)}",
            )

    # Validate mode-cfg-allow-client-selector if present
    if "mode-cfg-allow-client-selector" in payload:
        value = payload.get("mode-cfg-allow-client-selector")
        if value and value not in VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR:
            return (
                False,
                f"Invalid mode-cfg-allow-client-selector '{value}'. Must be one of: {', '.join(VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR)}",
            )

    # Validate assign-ip if present
    if "assign-ip" in payload:
        value = payload.get("assign-ip")
        if value and value not in VALID_BODY_ASSIGN_IP:
            return (
                False,
                f"Invalid assign-ip '{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGN_IP)}",
            )

    # Validate assign-ip-from if present
    if "assign-ip-from" in payload:
        value = payload.get("assign-ip-from")
        if value and value not in VALID_BODY_ASSIGN_IP_FROM:
            return (
                False,
                f"Invalid assign-ip-from '{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGN_IP_FROM)}",
            )

    # Validate dns-mode if present
    if "dns-mode" in payload:
        value = payload.get("dns-mode")
        if value and value not in VALID_BODY_DNS_MODE:
            return (
                False,
                f"Invalid dns-mode '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_MODE)}",
            )

    # Validate ipv4-split-include if present
    if "ipv4-split-include" in payload:
        value = payload.get("ipv4-split-include")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv4-split-include cannot exceed 79 characters")

    # Validate split-include-service if present
    if "split-include-service" in payload:
        value = payload.get("split-include-service")
        if value and isinstance(value, str) and len(value) > 79:
            return (
                False,
                "split-include-service cannot exceed 79 characters",
            )

    # Validate ipv4-name if present
    if "ipv4-name" in payload:
        value = payload.get("ipv4-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv4-name cannot exceed 79 characters")

    # Validate ipv6-prefix if present
    if "ipv6-prefix" in payload:
        value = payload.get("ipv6-prefix")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 128:
                    return (False, "ipv6-prefix must be between 1 and 128")
            except (ValueError, TypeError):
                return (False, f"ipv6-prefix must be numeric, got: {value}")

    # Validate ipv6-split-include if present
    if "ipv6-split-include" in payload:
        value = payload.get("ipv6-split-include")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv6-split-include cannot exceed 79 characters")

    # Validate ipv6-name if present
    if "ipv6-name" in payload:
        value = payload.get("ipv6-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv6-name cannot exceed 79 characters")

    # Validate ip-delay-interval if present
    if "ip-delay-interval" in payload:
        value = payload.get("ip-delay-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 28800:
                    return (
                        False,
                        "ip-delay-interval must be between 0 and 28800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ip-delay-interval must be numeric, got: {value}",
                )

    # Validate unity-support if present
    if "unity-support" in payload:
        value = payload.get("unity-support")
        if value and value not in VALID_BODY_UNITY_SUPPORT:
            return (
                False,
                f"Invalid unity-support '{value}'. Must be one of: {', '.join(VALID_BODY_UNITY_SUPPORT)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "domain cannot exceed 63 characters")

    # Validate banner if present
    if "banner" in payload:
        value = payload.get("banner")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "banner cannot exceed 1024 characters")

    # Validate include-local-lan if present
    if "include-local-lan" in payload:
        value = payload.get("include-local-lan")
        if value and value not in VALID_BODY_INCLUDE_LOCAL_LAN:
            return (
                False,
                f"Invalid include-local-lan '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_LOCAL_LAN)}",
            )

    # Validate ipv4-split-exclude if present
    if "ipv4-split-exclude" in payload:
        value = payload.get("ipv4-split-exclude")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv4-split-exclude cannot exceed 79 characters")

    # Validate ipv6-split-exclude if present
    if "ipv6-split-exclude" in payload:
        value = payload.get("ipv6-split-exclude")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv6-split-exclude cannot exceed 79 characters")

    # Validate save-password if present
    if "save-password" in payload:
        value = payload.get("save-password")
        if value and value not in VALID_BODY_SAVE_PASSWORD:
            return (
                False,
                f"Invalid save-password '{value}'. Must be one of: {', '.join(VALID_BODY_SAVE_PASSWORD)}",
            )

    # Validate client-auto-negotiate if present
    if "client-auto-negotiate" in payload:
        value = payload.get("client-auto-negotiate")
        if value and value not in VALID_BODY_CLIENT_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid client-auto-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_AUTO_NEGOTIATE)}",
            )

    # Validate client-keep-alive if present
    if "client-keep-alive" in payload:
        value = payload.get("client-keep-alive")
        if value and value not in VALID_BODY_CLIENT_KEEP_ALIVE:
            return (
                False,
                f"Invalid client-keep-alive '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_KEEP_ALIVE)}",
            )

    # Validate proposal if present
    if "proposal" in payload:
        value = payload.get("proposal")
        if value and value not in VALID_BODY_PROPOSAL:
            return (
                False,
                f"Invalid proposal '{value}'. Must be one of: {', '.join(VALID_BODY_PROPOSAL)}",
            )

    # Validate add-route if present
    if "add-route" in payload:
        value = payload.get("add-route")
        if value and value not in VALID_BODY_ADD_ROUTE:
            return (
                False,
                f"Invalid add-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_ROUTE)}",
            )

    # Validate add-gw-route if present
    if "add-gw-route" in payload:
        value = payload.get("add-gw-route")
        if value and value not in VALID_BODY_ADD_GW_ROUTE:
            return (
                False,
                f"Invalid add-gw-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_GW_ROUTE)}",
            )

    # Validate keepalive if present
    if "keepalive" in payload:
        value = payload.get("keepalive")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 900:
                    return (False, "keepalive must be between 5 and 900")
            except (ValueError, TypeError):
                return (False, f"keepalive must be numeric, got: {value}")

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

    # Validate localid if present
    if "localid" in payload:
        value = payload.get("localid")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "localid cannot exceed 63 characters")

    # Validate localid-type if present
    if "localid-type" in payload:
        value = payload.get("localid-type")
        if value and value not in VALID_BODY_LOCALID_TYPE:
            return (
                False,
                f"Invalid localid-type '{value}'. Must be one of: {', '.join(VALID_BODY_LOCALID_TYPE)}",
            )

    # Validate auto-negotiate if present
    if "auto-negotiate" in payload:
        value = payload.get("auto-negotiate")
        if value and value not in VALID_BODY_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid auto-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_NEGOTIATE)}",
            )

    # Validate negotiate-timeout if present
    if "negotiate-timeout" in payload:
        value = payload.get("negotiate-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (
                        False,
                        "negotiate-timeout must be between 1 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"negotiate-timeout must be numeric, got: {value}",
                )

    # Validate fragmentation if present
    if "fragmentation" in payload:
        value = payload.get("fragmentation")
        if value and value not in VALID_BODY_FRAGMENTATION:
            return (
                False,
                f"Invalid fragmentation '{value}'. Must be one of: {', '.join(VALID_BODY_FRAGMENTATION)}",
            )

    # Validate dpd if present
    if "dpd" in payload:
        value = payload.get("dpd")
        if value and value not in VALID_BODY_DPD:
            return (
                False,
                f"Invalid dpd '{value}'. Must be one of: {', '.join(VALID_BODY_DPD)}",
            )

    # Validate dpd-retrycount if present
    if "dpd-retrycount" in payload:
        value = payload.get("dpd-retrycount")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (False, "dpd-retrycount must be between 1 and 10")
            except (ValueError, TypeError):
                return (False, f"dpd-retrycount must be numeric, got: {value}")

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate npu-offload if present
    if "npu-offload" in payload:
        value = payload.get("npu-offload")
        if value and value not in VALID_BODY_NPU_OFFLOAD:
            return (
                False,
                f"Invalid npu-offload '{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOAD)}",
            )

    # Validate send-cert-chain if present
    if "send-cert-chain" in payload:
        value = payload.get("send-cert-chain")
        if value and value not in VALID_BODY_SEND_CERT_CHAIN:
            return (
                False,
                f"Invalid send-cert-chain '{value}'. Must be one of: {', '.join(VALID_BODY_SEND_CERT_CHAIN)}",
            )

    # Validate dhgrp if present
    if "dhgrp" in payload:
        value = payload.get("dhgrp")
        if value and value not in VALID_BODY_DHGRP:
            return (
                False,
                f"Invalid dhgrp '{value}'. Must be one of: {', '.join(VALID_BODY_DHGRP)}",
            )

    # Validate addke1 if present
    if "addke1" in payload:
        value = payload.get("addke1")
        if value and value not in VALID_BODY_ADDKE1:
            return (
                False,
                f"Invalid addke1 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE1)}",
            )

    # Validate addke2 if present
    if "addke2" in payload:
        value = payload.get("addke2")
        if value and value not in VALID_BODY_ADDKE2:
            return (
                False,
                f"Invalid addke2 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE2)}",
            )

    # Validate addke3 if present
    if "addke3" in payload:
        value = payload.get("addke3")
        if value and value not in VALID_BODY_ADDKE3:
            return (
                False,
                f"Invalid addke3 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE3)}",
            )

    # Validate addke4 if present
    if "addke4" in payload:
        value = payload.get("addke4")
        if value and value not in VALID_BODY_ADDKE4:
            return (
                False,
                f"Invalid addke4 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE4)}",
            )

    # Validate addke5 if present
    if "addke5" in payload:
        value = payload.get("addke5")
        if value and value not in VALID_BODY_ADDKE5:
            return (
                False,
                f"Invalid addke5 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE5)}",
            )

    # Validate addke6 if present
    if "addke6" in payload:
        value = payload.get("addke6")
        if value and value not in VALID_BODY_ADDKE6:
            return (
                False,
                f"Invalid addke6 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE6)}",
            )

    # Validate addke7 if present
    if "addke7" in payload:
        value = payload.get("addke7")
        if value and value not in VALID_BODY_ADDKE7:
            return (
                False,
                f"Invalid addke7 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE7)}",
            )

    # Validate suite-b if present
    if "suite-b" in payload:
        value = payload.get("suite-b")
        if value and value not in VALID_BODY_SUITE_B:
            return (
                False,
                f"Invalid suite-b '{value}'. Must be one of: {', '.join(VALID_BODY_SUITE_B)}",
            )

    # Validate eap if present
    if "eap" in payload:
        value = payload.get("eap")
        if value and value not in VALID_BODY_EAP:
            return (
                False,
                f"Invalid eap '{value}'. Must be one of: {', '.join(VALID_BODY_EAP)}",
            )

    # Validate eap-identity if present
    if "eap-identity" in payload:
        value = payload.get("eap-identity")
        if value and value not in VALID_BODY_EAP_IDENTITY:
            return (
                False,
                f"Invalid eap-identity '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_IDENTITY)}",
            )

    # Validate eap-exclude-peergrp if present
    if "eap-exclude-peergrp" in payload:
        value = payload.get("eap-exclude-peergrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "eap-exclude-peergrp cannot exceed 35 characters")

    # Validate eap-cert-auth if present
    if "eap-cert-auth" in payload:
        value = payload.get("eap-cert-auth")
        if value and value not in VALID_BODY_EAP_CERT_AUTH:
            return (
                False,
                f"Invalid eap-cert-auth '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_CERT_AUTH)}",
            )

    # Validate acct-verify if present
    if "acct-verify" in payload:
        value = payload.get("acct-verify")
        if value and value not in VALID_BODY_ACCT_VERIFY:
            return (
                False,
                f"Invalid acct-verify '{value}'. Must be one of: {', '.join(VALID_BODY_ACCT_VERIFY)}",
            )

    # Validate ppk if present
    if "ppk" in payload:
        value = payload.get("ppk")
        if value and value not in VALID_BODY_PPK:
            return (
                False,
                f"Invalid ppk '{value}'. Must be one of: {', '.join(VALID_BODY_PPK)}",
            )

    # Validate ppk-identity if present
    if "ppk-identity" in payload:
        value = payload.get("ppk-identity")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ppk-identity cannot exceed 35 characters")

    # Validate wizard-type if present
    if "wizard-type" in payload:
        value = payload.get("wizard-type")
        if value and value not in VALID_BODY_WIZARD_TYPE:
            return (
                False,
                f"Invalid wizard-type '{value}'. Must be one of: {', '.join(VALID_BODY_WIZARD_TYPE)}",
            )

    # Validate xauthtype if present
    if "xauthtype" in payload:
        value = payload.get("xauthtype")
        if value and value not in VALID_BODY_XAUTHTYPE:
            return (
                False,
                f"Invalid xauthtype '{value}'. Must be one of: {', '.join(VALID_BODY_XAUTHTYPE)}",
            )

    # Validate reauth if present
    if "reauth" in payload:
        value = payload.get("reauth")
        if value and value not in VALID_BODY_REAUTH:
            return (
                False,
                f"Invalid reauth '{value}'. Must be one of: {', '.join(VALID_BODY_REAUTH)}",
            )

    # Validate authusr if present
    if "authusr" in payload:
        value = payload.get("authusr")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "authusr cannot exceed 64 characters")

    # Validate group-authentication if present
    if "group-authentication" in payload:
        value = payload.get("group-authentication")
        if value and value not in VALID_BODY_GROUP_AUTHENTICATION:
            return (
                False,
                f"Invalid group-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_AUTHENTICATION)}",
            )

    # Validate authusrgrp if present
    if "authusrgrp" in payload:
        value = payload.get("authusrgrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "authusrgrp cannot exceed 35 characters")

    # Validate mesh-selector-type if present
    if "mesh-selector-type" in payload:
        value = payload.get("mesh-selector-type")
        if value and value not in VALID_BODY_MESH_SELECTOR_TYPE:
            return (
                False,
                f"Invalid mesh-selector-type '{value}'. Must be one of: {', '.join(VALID_BODY_MESH_SELECTOR_TYPE)}",
            )

    # Validate idle-timeout if present
    if "idle-timeout" in payload:
        value = payload.get("idle-timeout")
        if value and value not in VALID_BODY_IDLE_TIMEOUT:
            return (
                False,
                f"Invalid idle-timeout '{value}'. Must be one of: {', '.join(VALID_BODY_IDLE_TIMEOUT)}",
            )

    # Validate shared-idle-timeout if present
    if "shared-idle-timeout" in payload:
        value = payload.get("shared-idle-timeout")
        if value and value not in VALID_BODY_SHARED_IDLE_TIMEOUT:
            return (
                False,
                f"Invalid shared-idle-timeout '{value}'. Must be one of: {', '.join(VALID_BODY_SHARED_IDLE_TIMEOUT)}",
            )

    # Validate idle-timeoutinterval if present
    if "idle-timeoutinterval" in payload:
        value = payload.get("idle-timeoutinterval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 43200:
                    return (
                        False,
                        "idle-timeoutinterval must be between 5 and 43200",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"idle-timeoutinterval must be numeric, got: {value}",
                )

    # Validate ha-sync-esp-seqno if present
    if "ha-sync-esp-seqno" in payload:
        value = payload.get("ha-sync-esp-seqno")
        if value and value not in VALID_BODY_HA_SYNC_ESP_SEQNO:
            return (
                False,
                f"Invalid ha-sync-esp-seqno '{value}'. Must be one of: {', '.join(VALID_BODY_HA_SYNC_ESP_SEQNO)}",
            )

    # Validate fgsp-sync if present
    if "fgsp-sync" in payload:
        value = payload.get("fgsp-sync")
        if value and value not in VALID_BODY_FGSP_SYNC:
            return (
                False,
                f"Invalid fgsp-sync '{value}'. Must be one of: {', '.join(VALID_BODY_FGSP_SYNC)}",
            )

    # Validate inbound-dscp-copy if present
    if "inbound-dscp-copy" in payload:
        value = payload.get("inbound-dscp-copy")
        if value and value not in VALID_BODY_INBOUND_DSCP_COPY:
            return (
                False,
                f"Invalid inbound-dscp-copy '{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND_DSCP_COPY)}",
            )

    # Validate nattraversal if present
    if "nattraversal" in payload:
        value = payload.get("nattraversal")
        if value and value not in VALID_BODY_NATTRAVERSAL:
            return (
                False,
                f"Invalid nattraversal '{value}'. Must be one of: {', '.join(VALID_BODY_NATTRAVERSAL)}",
            )

    # Validate fragmentation-mtu if present
    if "fragmentation-mtu" in payload:
        value = payload.get("fragmentation-mtu")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 500 or int_val > 16000:
                    return (
                        False,
                        "fragmentation-mtu must be between 500 and 16000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fragmentation-mtu must be numeric, got: {value}",
                )

    # Validate childless-ike if present
    if "childless-ike" in payload:
        value = payload.get("childless-ike")
        if value and value not in VALID_BODY_CHILDLESS_IKE:
            return (
                False,
                f"Invalid childless-ike '{value}'. Must be one of: {', '.join(VALID_BODY_CHILDLESS_IKE)}",
            )

    # Validate azure-ad-autoconnect if present
    if "azure-ad-autoconnect" in payload:
        value = payload.get("azure-ad-autoconnect")
        if value and value not in VALID_BODY_AZURE_AD_AUTOCONNECT:
            return (
                False,
                f"Invalid azure-ad-autoconnect '{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_AD_AUTOCONNECT)}",
            )

    # Validate client-resume if present
    if "client-resume" in payload:
        value = payload.get("client-resume")
        if value and value not in VALID_BODY_CLIENT_RESUME:
            return (
                False,
                f"Invalid client-resume '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_RESUME)}",
            )

    # Validate client-resume-interval if present
    if "client-resume-interval" in payload:
        value = payload.get("client-resume-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 120 or int_val > 172800:
                    return (
                        False,
                        "client-resume-interval must be between 120 and 172800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-resume-interval must be numeric, got: {value}",
                )

    # Validate rekey if present
    if "rekey" in payload:
        value = payload.get("rekey")
        if value and value not in VALID_BODY_REKEY:
            return (
                False,
                f"Invalid rekey '{value}'. Must be one of: {', '.join(VALID_BODY_REKEY)}",
            )

    # Validate digital-signature-auth if present
    if "digital-signature-auth" in payload:
        value = payload.get("digital-signature-auth")
        if value and value not in VALID_BODY_DIGITAL_SIGNATURE_AUTH:
            return (
                False,
                f"Invalid digital-signature-auth '{value}'. Must be one of: {', '.join(VALID_BODY_DIGITAL_SIGNATURE_AUTH)}",
            )

    # Validate signature-hash-alg if present
    if "signature-hash-alg" in payload:
        value = payload.get("signature-hash-alg")
        if value and value not in VALID_BODY_SIGNATURE_HASH_ALG:
            return (
                False,
                f"Invalid signature-hash-alg '{value}'. Must be one of: {', '.join(VALID_BODY_SIGNATURE_HASH_ALG)}",
            )

    # Validate rsa-signature-format if present
    if "rsa-signature-format" in payload:
        value = payload.get("rsa-signature-format")
        if value and value not in VALID_BODY_RSA_SIGNATURE_FORMAT:
            return (
                False,
                f"Invalid rsa-signature-format '{value}'. Must be one of: {', '.join(VALID_BODY_RSA_SIGNATURE_FORMAT)}",
            )

    # Validate rsa-signature-hash-override if present
    if "rsa-signature-hash-override" in payload:
        value = payload.get("rsa-signature-hash-override")
        if value and value not in VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE:
            return (
                False,
                f"Invalid rsa-signature-hash-override '{value}'. Must be one of: {', '.join(VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE)}",
            )

    # Validate enforce-unique-id if present
    if "enforce-unique-id" in payload:
        value = payload.get("enforce-unique-id")
        if value and value not in VALID_BODY_ENFORCE_UNIQUE_ID:
            return (
                False,
                f"Invalid enforce-unique-id '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_UNIQUE_ID)}",
            )

    # Validate cert-id-validation if present
    if "cert-id-validation" in payload:
        value = payload.get("cert-id-validation")
        if value and value not in VALID_BODY_CERT_ID_VALIDATION:
            return (
                False,
                f"Invalid cert-id-validation '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_ID_VALIDATION)}",
            )

    # Validate fec-egress if present
    if "fec-egress" in payload:
        value = payload.get("fec-egress")
        if value and value not in VALID_BODY_FEC_EGRESS:
            return (
                False,
                f"Invalid fec-egress '{value}'. Must be one of: {', '.join(VALID_BODY_FEC_EGRESS)}",
            )

    # Validate fec-send-timeout if present
    if "fec-send-timeout" in payload:
        value = payload.get("fec-send-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1000:
                    return (
                        False,
                        "fec-send-timeout must be between 1 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fec-send-timeout must be numeric, got: {value}",
                )

    # Validate fec-base if present
    if "fec-base" in payload:
        value = payload.get("fec-base")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 20:
                    return (False, "fec-base must be between 1 and 20")
            except (ValueError, TypeError):
                return (False, f"fec-base must be numeric, got: {value}")

    # Validate fec-codec if present
    if "fec-codec" in payload:
        value = payload.get("fec-codec")
        if value and value not in VALID_BODY_FEC_CODEC:
            return (
                False,
                f"Invalid fec-codec '{value}'. Must be one of: {', '.join(VALID_BODY_FEC_CODEC)}",
            )

    # Validate fec-redundant if present
    if "fec-redundant" in payload:
        value = payload.get("fec-redundant")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 5:
                    return (False, "fec-redundant must be between 1 and 5")
            except (ValueError, TypeError):
                return (False, f"fec-redundant must be numeric, got: {value}")

    # Validate fec-ingress if present
    if "fec-ingress" in payload:
        value = payload.get("fec-ingress")
        if value and value not in VALID_BODY_FEC_INGRESS:
            return (
                False,
                f"Invalid fec-ingress '{value}'. Must be one of: {', '.join(VALID_BODY_FEC_INGRESS)}",
            )

    # Validate fec-receive-timeout if present
    if "fec-receive-timeout" in payload:
        value = payload.get("fec-receive-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1000:
                    return (
                        False,
                        "fec-receive-timeout must be between 1 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fec-receive-timeout must be numeric, got: {value}",
                )

    # Validate fec-health-check if present
    if "fec-health-check" in payload:
        value = payload.get("fec-health-check")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fec-health-check cannot exceed 35 characters")

    # Validate fec-mapping-profile if present
    if "fec-mapping-profile" in payload:
        value = payload.get("fec-mapping-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fec-mapping-profile cannot exceed 35 characters")

    # Validate network-overlay if present
    if "network-overlay" in payload:
        value = payload.get("network-overlay")
        if value and value not in VALID_BODY_NETWORK_OVERLAY:
            return (
                False,
                f"Invalid network-overlay '{value}'. Must be one of: {', '.join(VALID_BODY_NETWORK_OVERLAY)}",
            )

    # Validate network-id if present
    if "network-id" in payload:
        value = payload.get("network-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "network-id must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"network-id must be numeric, got: {value}")

    # Validate dev-id-notification if present
    if "dev-id-notification" in payload:
        value = payload.get("dev-id-notification")
        if value and value not in VALID_BODY_DEV_ID_NOTIFICATION:
            return (
                False,
                f"Invalid dev-id-notification '{value}'. Must be one of: {', '.join(VALID_BODY_DEV_ID_NOTIFICATION)}",
            )

    # Validate dev-id if present
    if "dev-id" in payload:
        value = payload.get("dev-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "dev-id cannot exceed 63 characters")

    # Validate loopback-asymroute if present
    if "loopback-asymroute" in payload:
        value = payload.get("loopback-asymroute")
        if value and value not in VALID_BODY_LOOPBACK_ASYMROUTE:
            return (
                False,
                f"Invalid loopback-asymroute '{value}'. Must be one of: {', '.join(VALID_BODY_LOOPBACK_ASYMROUTE)}",
            )

    # Validate link-cost if present
    if "link-cost" in payload:
        value = payload.get("link-cost")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "link-cost must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"link-cost must be numeric, got: {value}")

    # Validate kms if present
    if "kms" in payload:
        value = payload.get("kms")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "kms cannot exceed 35 characters")

    # Validate exchange-fgt-device-id if present
    if "exchange-fgt-device-id" in payload:
        value = payload.get("exchange-fgt-device-id")
        if value and value not in VALID_BODY_EXCHANGE_FGT_DEVICE_ID:
            return (
                False,
                f"Invalid exchange-fgt-device-id '{value}'. Must be one of: {', '.join(VALID_BODY_EXCHANGE_FGT_DEVICE_ID)}",
            )

    # Validate ipv6-auto-linklocal if present
    if "ipv6-auto-linklocal" in payload:
        value = payload.get("ipv6-auto-linklocal")
        if value and value not in VALID_BODY_IPV6_AUTO_LINKLOCAL:
            return (
                False,
                f"Invalid ipv6-auto-linklocal '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_AUTO_LINKLOCAL)}",
            )

    # Validate ems-sn-check if present
    if "ems-sn-check" in payload:
        value = payload.get("ems-sn-check")
        if value and value not in VALID_BODY_EMS_SN_CHECK:
            return (
                False,
                f"Invalid ems-sn-check '{value}'. Must be one of: {', '.join(VALID_BODY_EMS_SN_CHECK)}",
            )

    # Validate cert-trust-store if present
    if "cert-trust-store" in payload:
        value = payload.get("cert-trust-store")
        if value and value not in VALID_BODY_CERT_TRUST_STORE:
            return (
                False,
                f"Invalid cert-trust-store '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_TRUST_STORE)}",
            )

    # Validate qkd if present
    if "qkd" in payload:
        value = payload.get("qkd")
        if value and value not in VALID_BODY_QKD:
            return (
                False,
                f"Invalid qkd '{value}'. Must be one of: {', '.join(VALID_BODY_QKD)}",
            )

    # Validate qkd-hybrid if present
    if "qkd-hybrid" in payload:
        value = payload.get("qkd-hybrid")
        if value and value not in VALID_BODY_QKD_HYBRID:
            return (
                False,
                f"Invalid qkd-hybrid '{value}'. Must be one of: {', '.join(VALID_BODY_QKD_HYBRID)}",
            )

    # Validate qkd-profile if present
    if "qkd-profile" in payload:
        value = payload.get("qkd-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "qkd-profile cannot exceed 35 characters")

    # Validate transport if present
    if "transport" in payload:
        value = payload.get("transport")
        if value and value not in VALID_BODY_TRANSPORT:
            return (
                False,
                f"Invalid transport '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT)}",
            )

    # Validate fortinet-esp if present
    if "fortinet-esp" in payload:
        value = payload.get("fortinet-esp")
        if value and value not in VALID_BODY_FORTINET_ESP:
            return (
                False,
                f"Invalid fortinet-esp '{value}'. Must be one of: {', '.join(VALID_BODY_FORTINET_ESP)}",
            )

    # Validate auto-transport-threshold if present
    if "auto-transport-threshold" in payload:
        value = payload.get("auto-transport-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (
                        False,
                        "auto-transport-threshold must be between 1 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-transport-threshold must be numeric, got: {value}",
                )

    # Validate remote-gw-match if present
    if "remote-gw-match" in payload:
        value = payload.get("remote-gw-match")
        if value and value not in VALID_BODY_REMOTE_GW_MATCH:
            return (
                False,
                f"Invalid remote-gw-match '{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_GW_MATCH)}",
            )

    # Validate remote-gw-country if present
    if "remote-gw-country" in payload:
        value = payload.get("remote-gw-country")
        if value and isinstance(value, str) and len(value) > 2:
            return (False, "remote-gw-country cannot exceed 2 characters")

    # Validate remote-gw6-match if present
    if "remote-gw6-match" in payload:
        value = payload.get("remote-gw6-match")
        if value and value not in VALID_BODY_REMOTE_GW6_MATCH:
            return (
                False,
                f"Invalid remote-gw6-match '{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_GW6_MATCH)}",
            )

    # Validate remote-gw6-country if present
    if "remote-gw6-country" in payload:
        value = payload.get("remote-gw6-country")
        if value and isinstance(value, str) and len(value) > 2:
            return (False, "remote-gw6-country cannot exceed 2 characters")

    # Validate cert-peer-username-validation if present
    if "cert-peer-username-validation" in payload:
        value = payload.get("cert-peer-username-validation")
        if value and value not in VALID_BODY_CERT_PEER_USERNAME_VALIDATION:
            return (
                False,
                f"Invalid cert-peer-username-validation '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_PEER_USERNAME_VALIDATION)}",
            )

    # Validate cert-peer-username-strip if present
    if "cert-peer-username-strip" in payload:
        value = payload.get("cert-peer-username-strip")
        if value and value not in VALID_BODY_CERT_PEER_USERNAME_STRIP:
            return (
                False,
                f"Invalid cert-peer-username-strip '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_PEER_USERNAME_STRIP)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ipsec_phase1_put(
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

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate ike-version if present
    if "ike-version" in payload:
        value = payload.get("ike-version")
        if value and value not in VALID_BODY_IKE_VERSION:
            return (
                False,
                f"Invalid ike-version '{value}'. Must be one of: {', '.join(VALID_BODY_IKE_VERSION)}",
            )

    # Validate remotegw-ddns if present
    if "remotegw-ddns" in payload:
        value = payload.get("remotegw-ddns")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "remotegw-ddns cannot exceed 63 characters")

    # Validate keylife if present
    if "keylife" in payload:
        value = payload.get("keylife")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 120 or int_val > 172800:
                    return (False, "keylife must be between 120 and 172800")
            except (ValueError, TypeError):
                return (False, f"keylife must be numeric, got: {value}")

    # Validate authmethod if present
    if "authmethod" in payload:
        value = payload.get("authmethod")
        if value and value not in VALID_BODY_AUTHMETHOD:
            return (
                False,
                f"Invalid authmethod '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHMETHOD)}",
            )

    # Validate authmethod-remote if present
    if "authmethod-remote" in payload:
        value = payload.get("authmethod-remote")
        if value and value not in VALID_BODY_AUTHMETHOD_REMOTE:
            return (
                False,
                f"Invalid authmethod-remote '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHMETHOD_REMOTE)}",
            )

    # Validate mode if present
    if "mode" in payload:
        value = payload.get("mode")
        if value and value not in VALID_BODY_MODE:
            return (
                False,
                f"Invalid mode '{value}'. Must be one of: {', '.join(VALID_BODY_MODE)}",
            )

    # Validate peertype if present
    if "peertype" in payload:
        value = payload.get("peertype")
        if value and value not in VALID_BODY_PEERTYPE:
            return (
                False,
                f"Invalid peertype '{value}'. Must be one of: {', '.join(VALID_BODY_PEERTYPE)}",
            )

    # Validate peerid if present
    if "peerid" in payload:
        value = payload.get("peerid")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "peerid cannot exceed 255 characters")

    # Validate usrgrp if present
    if "usrgrp" in payload:
        value = payload.get("usrgrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "usrgrp cannot exceed 35 characters")

    # Validate peer if present
    if "peer" in payload:
        value = payload.get("peer")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "peer cannot exceed 35 characters")

    # Validate peergrp if present
    if "peergrp" in payload:
        value = payload.get("peergrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "peergrp cannot exceed 35 characters")

    # Validate mode-cfg if present
    if "mode-cfg" in payload:
        value = payload.get("mode-cfg")
        if value and value not in VALID_BODY_MODE_CFG:
            return (
                False,
                f"Invalid mode-cfg '{value}'. Must be one of: {', '.join(VALID_BODY_MODE_CFG)}",
            )

    # Validate mode-cfg-allow-client-selector if present
    if "mode-cfg-allow-client-selector" in payload:
        value = payload.get("mode-cfg-allow-client-selector")
        if value and value not in VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR:
            return (
                False,
                f"Invalid mode-cfg-allow-client-selector '{value}'. Must be one of: {', '.join(VALID_BODY_MODE_CFG_ALLOW_CLIENT_SELECTOR)}",
            )

    # Validate assign-ip if present
    if "assign-ip" in payload:
        value = payload.get("assign-ip")
        if value and value not in VALID_BODY_ASSIGN_IP:
            return (
                False,
                f"Invalid assign-ip '{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGN_IP)}",
            )

    # Validate assign-ip-from if present
    if "assign-ip-from" in payload:
        value = payload.get("assign-ip-from")
        if value and value not in VALID_BODY_ASSIGN_IP_FROM:
            return (
                False,
                f"Invalid assign-ip-from '{value}'. Must be one of: {', '.join(VALID_BODY_ASSIGN_IP_FROM)}",
            )

    # Validate dns-mode if present
    if "dns-mode" in payload:
        value = payload.get("dns-mode")
        if value and value not in VALID_BODY_DNS_MODE:
            return (
                False,
                f"Invalid dns-mode '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_MODE)}",
            )

    # Validate ipv4-split-include if present
    if "ipv4-split-include" in payload:
        value = payload.get("ipv4-split-include")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv4-split-include cannot exceed 79 characters")

    # Validate split-include-service if present
    if "split-include-service" in payload:
        value = payload.get("split-include-service")
        if value and isinstance(value, str) and len(value) > 79:
            return (
                False,
                "split-include-service cannot exceed 79 characters",
            )

    # Validate ipv4-name if present
    if "ipv4-name" in payload:
        value = payload.get("ipv4-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv4-name cannot exceed 79 characters")

    # Validate ipv6-prefix if present
    if "ipv6-prefix" in payload:
        value = payload.get("ipv6-prefix")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 128:
                    return (False, "ipv6-prefix must be between 1 and 128")
            except (ValueError, TypeError):
                return (False, f"ipv6-prefix must be numeric, got: {value}")

    # Validate ipv6-split-include if present
    if "ipv6-split-include" in payload:
        value = payload.get("ipv6-split-include")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv6-split-include cannot exceed 79 characters")

    # Validate ipv6-name if present
    if "ipv6-name" in payload:
        value = payload.get("ipv6-name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv6-name cannot exceed 79 characters")

    # Validate ip-delay-interval if present
    if "ip-delay-interval" in payload:
        value = payload.get("ip-delay-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 28800:
                    return (
                        False,
                        "ip-delay-interval must be between 0 and 28800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ip-delay-interval must be numeric, got: {value}",
                )

    # Validate unity-support if present
    if "unity-support" in payload:
        value = payload.get("unity-support")
        if value and value not in VALID_BODY_UNITY_SUPPORT:
            return (
                False,
                f"Invalid unity-support '{value}'. Must be one of: {', '.join(VALID_BODY_UNITY_SUPPORT)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "domain cannot exceed 63 characters")

    # Validate banner if present
    if "banner" in payload:
        value = payload.get("banner")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "banner cannot exceed 1024 characters")

    # Validate include-local-lan if present
    if "include-local-lan" in payload:
        value = payload.get("include-local-lan")
        if value and value not in VALID_BODY_INCLUDE_LOCAL_LAN:
            return (
                False,
                f"Invalid include-local-lan '{value}'. Must be one of: {', '.join(VALID_BODY_INCLUDE_LOCAL_LAN)}",
            )

    # Validate ipv4-split-exclude if present
    if "ipv4-split-exclude" in payload:
        value = payload.get("ipv4-split-exclude")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv4-split-exclude cannot exceed 79 characters")

    # Validate ipv6-split-exclude if present
    if "ipv6-split-exclude" in payload:
        value = payload.get("ipv6-split-exclude")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ipv6-split-exclude cannot exceed 79 characters")

    # Validate save-password if present
    if "save-password" in payload:
        value = payload.get("save-password")
        if value and value not in VALID_BODY_SAVE_PASSWORD:
            return (
                False,
                f"Invalid save-password '{value}'. Must be one of: {', '.join(VALID_BODY_SAVE_PASSWORD)}",
            )

    # Validate client-auto-negotiate if present
    if "client-auto-negotiate" in payload:
        value = payload.get("client-auto-negotiate")
        if value and value not in VALID_BODY_CLIENT_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid client-auto-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_AUTO_NEGOTIATE)}",
            )

    # Validate client-keep-alive if present
    if "client-keep-alive" in payload:
        value = payload.get("client-keep-alive")
        if value and value not in VALID_BODY_CLIENT_KEEP_ALIVE:
            return (
                False,
                f"Invalid client-keep-alive '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_KEEP_ALIVE)}",
            )

    # Validate proposal if present
    if "proposal" in payload:
        value = payload.get("proposal")
        if value and value not in VALID_BODY_PROPOSAL:
            return (
                False,
                f"Invalid proposal '{value}'. Must be one of: {', '.join(VALID_BODY_PROPOSAL)}",
            )

    # Validate add-route if present
    if "add-route" in payload:
        value = payload.get("add-route")
        if value and value not in VALID_BODY_ADD_ROUTE:
            return (
                False,
                f"Invalid add-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_ROUTE)}",
            )

    # Validate add-gw-route if present
    if "add-gw-route" in payload:
        value = payload.get("add-gw-route")
        if value and value not in VALID_BODY_ADD_GW_ROUTE:
            return (
                False,
                f"Invalid add-gw-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_GW_ROUTE)}",
            )

    # Validate keepalive if present
    if "keepalive" in payload:
        value = payload.get("keepalive")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 900:
                    return (False, "keepalive must be between 5 and 900")
            except (ValueError, TypeError):
                return (False, f"keepalive must be numeric, got: {value}")

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

    # Validate localid if present
    if "localid" in payload:
        value = payload.get("localid")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "localid cannot exceed 63 characters")

    # Validate localid-type if present
    if "localid-type" in payload:
        value = payload.get("localid-type")
        if value and value not in VALID_BODY_LOCALID_TYPE:
            return (
                False,
                f"Invalid localid-type '{value}'. Must be one of: {', '.join(VALID_BODY_LOCALID_TYPE)}",
            )

    # Validate auto-negotiate if present
    if "auto-negotiate" in payload:
        value = payload.get("auto-negotiate")
        if value and value not in VALID_BODY_AUTO_NEGOTIATE:
            return (
                False,
                f"Invalid auto-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_NEGOTIATE)}",
            )

    # Validate negotiate-timeout if present
    if "negotiate-timeout" in payload:
        value = payload.get("negotiate-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (
                        False,
                        "negotiate-timeout must be between 1 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"negotiate-timeout must be numeric, got: {value}",
                )

    # Validate fragmentation if present
    if "fragmentation" in payload:
        value = payload.get("fragmentation")
        if value and value not in VALID_BODY_FRAGMENTATION:
            return (
                False,
                f"Invalid fragmentation '{value}'. Must be one of: {', '.join(VALID_BODY_FRAGMENTATION)}",
            )

    # Validate dpd if present
    if "dpd" in payload:
        value = payload.get("dpd")
        if value and value not in VALID_BODY_DPD:
            return (
                False,
                f"Invalid dpd '{value}'. Must be one of: {', '.join(VALID_BODY_DPD)}",
            )

    # Validate dpd-retrycount if present
    if "dpd-retrycount" in payload:
        value = payload.get("dpd-retrycount")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (False, "dpd-retrycount must be between 1 and 10")
            except (ValueError, TypeError):
                return (False, f"dpd-retrycount must be numeric, got: {value}")

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate npu-offload if present
    if "npu-offload" in payload:
        value = payload.get("npu-offload")
        if value and value not in VALID_BODY_NPU_OFFLOAD:
            return (
                False,
                f"Invalid npu-offload '{value}'. Must be one of: {', '.join(VALID_BODY_NPU_OFFLOAD)}",
            )

    # Validate send-cert-chain if present
    if "send-cert-chain" in payload:
        value = payload.get("send-cert-chain")
        if value and value not in VALID_BODY_SEND_CERT_CHAIN:
            return (
                False,
                f"Invalid send-cert-chain '{value}'. Must be one of: {', '.join(VALID_BODY_SEND_CERT_CHAIN)}",
            )

    # Validate dhgrp if present
    if "dhgrp" in payload:
        value = payload.get("dhgrp")
        if value and value not in VALID_BODY_DHGRP:
            return (
                False,
                f"Invalid dhgrp '{value}'. Must be one of: {', '.join(VALID_BODY_DHGRP)}",
            )

    # Validate addke1 if present
    if "addke1" in payload:
        value = payload.get("addke1")
        if value and value not in VALID_BODY_ADDKE1:
            return (
                False,
                f"Invalid addke1 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE1)}",
            )

    # Validate addke2 if present
    if "addke2" in payload:
        value = payload.get("addke2")
        if value and value not in VALID_BODY_ADDKE2:
            return (
                False,
                f"Invalid addke2 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE2)}",
            )

    # Validate addke3 if present
    if "addke3" in payload:
        value = payload.get("addke3")
        if value and value not in VALID_BODY_ADDKE3:
            return (
                False,
                f"Invalid addke3 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE3)}",
            )

    # Validate addke4 if present
    if "addke4" in payload:
        value = payload.get("addke4")
        if value and value not in VALID_BODY_ADDKE4:
            return (
                False,
                f"Invalid addke4 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE4)}",
            )

    # Validate addke5 if present
    if "addke5" in payload:
        value = payload.get("addke5")
        if value and value not in VALID_BODY_ADDKE5:
            return (
                False,
                f"Invalid addke5 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE5)}",
            )

    # Validate addke6 if present
    if "addke6" in payload:
        value = payload.get("addke6")
        if value and value not in VALID_BODY_ADDKE6:
            return (
                False,
                f"Invalid addke6 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE6)}",
            )

    # Validate addke7 if present
    if "addke7" in payload:
        value = payload.get("addke7")
        if value and value not in VALID_BODY_ADDKE7:
            return (
                False,
                f"Invalid addke7 '{value}'. Must be one of: {', '.join(VALID_BODY_ADDKE7)}",
            )

    # Validate suite-b if present
    if "suite-b" in payload:
        value = payload.get("suite-b")
        if value and value not in VALID_BODY_SUITE_B:
            return (
                False,
                f"Invalid suite-b '{value}'. Must be one of: {', '.join(VALID_BODY_SUITE_B)}",
            )

    # Validate eap if present
    if "eap" in payload:
        value = payload.get("eap")
        if value and value not in VALID_BODY_EAP:
            return (
                False,
                f"Invalid eap '{value}'. Must be one of: {', '.join(VALID_BODY_EAP)}",
            )

    # Validate eap-identity if present
    if "eap-identity" in payload:
        value = payload.get("eap-identity")
        if value and value not in VALID_BODY_EAP_IDENTITY:
            return (
                False,
                f"Invalid eap-identity '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_IDENTITY)}",
            )

    # Validate eap-exclude-peergrp if present
    if "eap-exclude-peergrp" in payload:
        value = payload.get("eap-exclude-peergrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "eap-exclude-peergrp cannot exceed 35 characters")

    # Validate eap-cert-auth if present
    if "eap-cert-auth" in payload:
        value = payload.get("eap-cert-auth")
        if value and value not in VALID_BODY_EAP_CERT_AUTH:
            return (
                False,
                f"Invalid eap-cert-auth '{value}'. Must be one of: {', '.join(VALID_BODY_EAP_CERT_AUTH)}",
            )

    # Validate acct-verify if present
    if "acct-verify" in payload:
        value = payload.get("acct-verify")
        if value and value not in VALID_BODY_ACCT_VERIFY:
            return (
                False,
                f"Invalid acct-verify '{value}'. Must be one of: {', '.join(VALID_BODY_ACCT_VERIFY)}",
            )

    # Validate ppk if present
    if "ppk" in payload:
        value = payload.get("ppk")
        if value and value not in VALID_BODY_PPK:
            return (
                False,
                f"Invalid ppk '{value}'. Must be one of: {', '.join(VALID_BODY_PPK)}",
            )

    # Validate ppk-identity if present
    if "ppk-identity" in payload:
        value = payload.get("ppk-identity")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ppk-identity cannot exceed 35 characters")

    # Validate wizard-type if present
    if "wizard-type" in payload:
        value = payload.get("wizard-type")
        if value and value not in VALID_BODY_WIZARD_TYPE:
            return (
                False,
                f"Invalid wizard-type '{value}'. Must be one of: {', '.join(VALID_BODY_WIZARD_TYPE)}",
            )

    # Validate xauthtype if present
    if "xauthtype" in payload:
        value = payload.get("xauthtype")
        if value and value not in VALID_BODY_XAUTHTYPE:
            return (
                False,
                f"Invalid xauthtype '{value}'. Must be one of: {', '.join(VALID_BODY_XAUTHTYPE)}",
            )

    # Validate reauth if present
    if "reauth" in payload:
        value = payload.get("reauth")
        if value and value not in VALID_BODY_REAUTH:
            return (
                False,
                f"Invalid reauth '{value}'. Must be one of: {', '.join(VALID_BODY_REAUTH)}",
            )

    # Validate authusr if present
    if "authusr" in payload:
        value = payload.get("authusr")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "authusr cannot exceed 64 characters")

    # Validate group-authentication if present
    if "group-authentication" in payload:
        value = payload.get("group-authentication")
        if value and value not in VALID_BODY_GROUP_AUTHENTICATION:
            return (
                False,
                f"Invalid group-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_AUTHENTICATION)}",
            )

    # Validate authusrgrp if present
    if "authusrgrp" in payload:
        value = payload.get("authusrgrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "authusrgrp cannot exceed 35 characters")

    # Validate mesh-selector-type if present
    if "mesh-selector-type" in payload:
        value = payload.get("mesh-selector-type")
        if value and value not in VALID_BODY_MESH_SELECTOR_TYPE:
            return (
                False,
                f"Invalid mesh-selector-type '{value}'. Must be one of: {', '.join(VALID_BODY_MESH_SELECTOR_TYPE)}",
            )

    # Validate idle-timeout if present
    if "idle-timeout" in payload:
        value = payload.get("idle-timeout")
        if value and value not in VALID_BODY_IDLE_TIMEOUT:
            return (
                False,
                f"Invalid idle-timeout '{value}'. Must be one of: {', '.join(VALID_BODY_IDLE_TIMEOUT)}",
            )

    # Validate shared-idle-timeout if present
    if "shared-idle-timeout" in payload:
        value = payload.get("shared-idle-timeout")
        if value and value not in VALID_BODY_SHARED_IDLE_TIMEOUT:
            return (
                False,
                f"Invalid shared-idle-timeout '{value}'. Must be one of: {', '.join(VALID_BODY_SHARED_IDLE_TIMEOUT)}",
            )

    # Validate idle-timeoutinterval if present
    if "idle-timeoutinterval" in payload:
        value = payload.get("idle-timeoutinterval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 43200:
                    return (
                        False,
                        "idle-timeoutinterval must be between 5 and 43200",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"idle-timeoutinterval must be numeric, got: {value}",
                )

    # Validate ha-sync-esp-seqno if present
    if "ha-sync-esp-seqno" in payload:
        value = payload.get("ha-sync-esp-seqno")
        if value and value not in VALID_BODY_HA_SYNC_ESP_SEQNO:
            return (
                False,
                f"Invalid ha-sync-esp-seqno '{value}'. Must be one of: {', '.join(VALID_BODY_HA_SYNC_ESP_SEQNO)}",
            )

    # Validate fgsp-sync if present
    if "fgsp-sync" in payload:
        value = payload.get("fgsp-sync")
        if value and value not in VALID_BODY_FGSP_SYNC:
            return (
                False,
                f"Invalid fgsp-sync '{value}'. Must be one of: {', '.join(VALID_BODY_FGSP_SYNC)}",
            )

    # Validate inbound-dscp-copy if present
    if "inbound-dscp-copy" in payload:
        value = payload.get("inbound-dscp-copy")
        if value and value not in VALID_BODY_INBOUND_DSCP_COPY:
            return (
                False,
                f"Invalid inbound-dscp-copy '{value}'. Must be one of: {', '.join(VALID_BODY_INBOUND_DSCP_COPY)}",
            )

    # Validate nattraversal if present
    if "nattraversal" in payload:
        value = payload.get("nattraversal")
        if value and value not in VALID_BODY_NATTRAVERSAL:
            return (
                False,
                f"Invalid nattraversal '{value}'. Must be one of: {', '.join(VALID_BODY_NATTRAVERSAL)}",
            )

    # Validate fragmentation-mtu if present
    if "fragmentation-mtu" in payload:
        value = payload.get("fragmentation-mtu")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 500 or int_val > 16000:
                    return (
                        False,
                        "fragmentation-mtu must be between 500 and 16000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fragmentation-mtu must be numeric, got: {value}",
                )

    # Validate childless-ike if present
    if "childless-ike" in payload:
        value = payload.get("childless-ike")
        if value and value not in VALID_BODY_CHILDLESS_IKE:
            return (
                False,
                f"Invalid childless-ike '{value}'. Must be one of: {', '.join(VALID_BODY_CHILDLESS_IKE)}",
            )

    # Validate azure-ad-autoconnect if present
    if "azure-ad-autoconnect" in payload:
        value = payload.get("azure-ad-autoconnect")
        if value and value not in VALID_BODY_AZURE_AD_AUTOCONNECT:
            return (
                False,
                f"Invalid azure-ad-autoconnect '{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_AD_AUTOCONNECT)}",
            )

    # Validate client-resume if present
    if "client-resume" in payload:
        value = payload.get("client-resume")
        if value and value not in VALID_BODY_CLIENT_RESUME:
            return (
                False,
                f"Invalid client-resume '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_RESUME)}",
            )

    # Validate client-resume-interval if present
    if "client-resume-interval" in payload:
        value = payload.get("client-resume-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 120 or int_val > 172800:
                    return (
                        False,
                        "client-resume-interval must be between 120 and 172800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-resume-interval must be numeric, got: {value}",
                )

    # Validate rekey if present
    if "rekey" in payload:
        value = payload.get("rekey")
        if value and value not in VALID_BODY_REKEY:
            return (
                False,
                f"Invalid rekey '{value}'. Must be one of: {', '.join(VALID_BODY_REKEY)}",
            )

    # Validate digital-signature-auth if present
    if "digital-signature-auth" in payload:
        value = payload.get("digital-signature-auth")
        if value and value not in VALID_BODY_DIGITAL_SIGNATURE_AUTH:
            return (
                False,
                f"Invalid digital-signature-auth '{value}'. Must be one of: {', '.join(VALID_BODY_DIGITAL_SIGNATURE_AUTH)}",
            )

    # Validate signature-hash-alg if present
    if "signature-hash-alg" in payload:
        value = payload.get("signature-hash-alg")
        if value and value not in VALID_BODY_SIGNATURE_HASH_ALG:
            return (
                False,
                f"Invalid signature-hash-alg '{value}'. Must be one of: {', '.join(VALID_BODY_SIGNATURE_HASH_ALG)}",
            )

    # Validate rsa-signature-format if present
    if "rsa-signature-format" in payload:
        value = payload.get("rsa-signature-format")
        if value and value not in VALID_BODY_RSA_SIGNATURE_FORMAT:
            return (
                False,
                f"Invalid rsa-signature-format '{value}'. Must be one of: {', '.join(VALID_BODY_RSA_SIGNATURE_FORMAT)}",
            )

    # Validate rsa-signature-hash-override if present
    if "rsa-signature-hash-override" in payload:
        value = payload.get("rsa-signature-hash-override")
        if value and value not in VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE:
            return (
                False,
                f"Invalid rsa-signature-hash-override '{value}'. Must be one of: {', '.join(VALID_BODY_RSA_SIGNATURE_HASH_OVERRIDE)}",
            )

    # Validate enforce-unique-id if present
    if "enforce-unique-id" in payload:
        value = payload.get("enforce-unique-id")
        if value and value not in VALID_BODY_ENFORCE_UNIQUE_ID:
            return (
                False,
                f"Invalid enforce-unique-id '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_UNIQUE_ID)}",
            )

    # Validate cert-id-validation if present
    if "cert-id-validation" in payload:
        value = payload.get("cert-id-validation")
        if value and value not in VALID_BODY_CERT_ID_VALIDATION:
            return (
                False,
                f"Invalid cert-id-validation '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_ID_VALIDATION)}",
            )

    # Validate fec-egress if present
    if "fec-egress" in payload:
        value = payload.get("fec-egress")
        if value and value not in VALID_BODY_FEC_EGRESS:
            return (
                False,
                f"Invalid fec-egress '{value}'. Must be one of: {', '.join(VALID_BODY_FEC_EGRESS)}",
            )

    # Validate fec-send-timeout if present
    if "fec-send-timeout" in payload:
        value = payload.get("fec-send-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1000:
                    return (
                        False,
                        "fec-send-timeout must be between 1 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fec-send-timeout must be numeric, got: {value}",
                )

    # Validate fec-base if present
    if "fec-base" in payload:
        value = payload.get("fec-base")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 20:
                    return (False, "fec-base must be between 1 and 20")
            except (ValueError, TypeError):
                return (False, f"fec-base must be numeric, got: {value}")

    # Validate fec-codec if present
    if "fec-codec" in payload:
        value = payload.get("fec-codec")
        if value and value not in VALID_BODY_FEC_CODEC:
            return (
                False,
                f"Invalid fec-codec '{value}'. Must be one of: {', '.join(VALID_BODY_FEC_CODEC)}",
            )

    # Validate fec-redundant if present
    if "fec-redundant" in payload:
        value = payload.get("fec-redundant")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 5:
                    return (False, "fec-redundant must be between 1 and 5")
            except (ValueError, TypeError):
                return (False, f"fec-redundant must be numeric, got: {value}")

    # Validate fec-ingress if present
    if "fec-ingress" in payload:
        value = payload.get("fec-ingress")
        if value and value not in VALID_BODY_FEC_INGRESS:
            return (
                False,
                f"Invalid fec-ingress '{value}'. Must be one of: {', '.join(VALID_BODY_FEC_INGRESS)}",
            )

    # Validate fec-receive-timeout if present
    if "fec-receive-timeout" in payload:
        value = payload.get("fec-receive-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1000:
                    return (
                        False,
                        "fec-receive-timeout must be between 1 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fec-receive-timeout must be numeric, got: {value}",
                )

    # Validate fec-health-check if present
    if "fec-health-check" in payload:
        value = payload.get("fec-health-check")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fec-health-check cannot exceed 35 characters")

    # Validate fec-mapping-profile if present
    if "fec-mapping-profile" in payload:
        value = payload.get("fec-mapping-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fec-mapping-profile cannot exceed 35 characters")

    # Validate network-overlay if present
    if "network-overlay" in payload:
        value = payload.get("network-overlay")
        if value and value not in VALID_BODY_NETWORK_OVERLAY:
            return (
                False,
                f"Invalid network-overlay '{value}'. Must be one of: {', '.join(VALID_BODY_NETWORK_OVERLAY)}",
            )

    # Validate network-id if present
    if "network-id" in payload:
        value = payload.get("network-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "network-id must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"network-id must be numeric, got: {value}")

    # Validate dev-id-notification if present
    if "dev-id-notification" in payload:
        value = payload.get("dev-id-notification")
        if value and value not in VALID_BODY_DEV_ID_NOTIFICATION:
            return (
                False,
                f"Invalid dev-id-notification '{value}'. Must be one of: {', '.join(VALID_BODY_DEV_ID_NOTIFICATION)}",
            )

    # Validate dev-id if present
    if "dev-id" in payload:
        value = payload.get("dev-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "dev-id cannot exceed 63 characters")

    # Validate loopback-asymroute if present
    if "loopback-asymroute" in payload:
        value = payload.get("loopback-asymroute")
        if value and value not in VALID_BODY_LOOPBACK_ASYMROUTE:
            return (
                False,
                f"Invalid loopback-asymroute '{value}'. Must be one of: {', '.join(VALID_BODY_LOOPBACK_ASYMROUTE)}",
            )

    # Validate link-cost if present
    if "link-cost" in payload:
        value = payload.get("link-cost")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "link-cost must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"link-cost must be numeric, got: {value}")

    # Validate kms if present
    if "kms" in payload:
        value = payload.get("kms")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "kms cannot exceed 35 characters")

    # Validate exchange-fgt-device-id if present
    if "exchange-fgt-device-id" in payload:
        value = payload.get("exchange-fgt-device-id")
        if value and value not in VALID_BODY_EXCHANGE_FGT_DEVICE_ID:
            return (
                False,
                f"Invalid exchange-fgt-device-id '{value}'. Must be one of: {', '.join(VALID_BODY_EXCHANGE_FGT_DEVICE_ID)}",
            )

    # Validate ipv6-auto-linklocal if present
    if "ipv6-auto-linklocal" in payload:
        value = payload.get("ipv6-auto-linklocal")
        if value and value not in VALID_BODY_IPV6_AUTO_LINKLOCAL:
            return (
                False,
                f"Invalid ipv6-auto-linklocal '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_AUTO_LINKLOCAL)}",
            )

    # Validate ems-sn-check if present
    if "ems-sn-check" in payload:
        value = payload.get("ems-sn-check")
        if value and value not in VALID_BODY_EMS_SN_CHECK:
            return (
                False,
                f"Invalid ems-sn-check '{value}'. Must be one of: {', '.join(VALID_BODY_EMS_SN_CHECK)}",
            )

    # Validate cert-trust-store if present
    if "cert-trust-store" in payload:
        value = payload.get("cert-trust-store")
        if value and value not in VALID_BODY_CERT_TRUST_STORE:
            return (
                False,
                f"Invalid cert-trust-store '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_TRUST_STORE)}",
            )

    # Validate qkd if present
    if "qkd" in payload:
        value = payload.get("qkd")
        if value and value not in VALID_BODY_QKD:
            return (
                False,
                f"Invalid qkd '{value}'. Must be one of: {', '.join(VALID_BODY_QKD)}",
            )

    # Validate qkd-hybrid if present
    if "qkd-hybrid" in payload:
        value = payload.get("qkd-hybrid")
        if value and value not in VALID_BODY_QKD_HYBRID:
            return (
                False,
                f"Invalid qkd-hybrid '{value}'. Must be one of: {', '.join(VALID_BODY_QKD_HYBRID)}",
            )

    # Validate qkd-profile if present
    if "qkd-profile" in payload:
        value = payload.get("qkd-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "qkd-profile cannot exceed 35 characters")

    # Validate transport if present
    if "transport" in payload:
        value = payload.get("transport")
        if value and value not in VALID_BODY_TRANSPORT:
            return (
                False,
                f"Invalid transport '{value}'. Must be one of: {', '.join(VALID_BODY_TRANSPORT)}",
            )

    # Validate fortinet-esp if present
    if "fortinet-esp" in payload:
        value = payload.get("fortinet-esp")
        if value and value not in VALID_BODY_FORTINET_ESP:
            return (
                False,
                f"Invalid fortinet-esp '{value}'. Must be one of: {', '.join(VALID_BODY_FORTINET_ESP)}",
            )

    # Validate auto-transport-threshold if present
    if "auto-transport-threshold" in payload:
        value = payload.get("auto-transport-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (
                        False,
                        "auto-transport-threshold must be between 1 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-transport-threshold must be numeric, got: {value}",
                )

    # Validate remote-gw-match if present
    if "remote-gw-match" in payload:
        value = payload.get("remote-gw-match")
        if value and value not in VALID_BODY_REMOTE_GW_MATCH:
            return (
                False,
                f"Invalid remote-gw-match '{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_GW_MATCH)}",
            )

    # Validate remote-gw-country if present
    if "remote-gw-country" in payload:
        value = payload.get("remote-gw-country")
        if value and isinstance(value, str) and len(value) > 2:
            return (False, "remote-gw-country cannot exceed 2 characters")

    # Validate remote-gw6-match if present
    if "remote-gw6-match" in payload:
        value = payload.get("remote-gw6-match")
        if value and value not in VALID_BODY_REMOTE_GW6_MATCH:
            return (
                False,
                f"Invalid remote-gw6-match '{value}'. Must be one of: {', '.join(VALID_BODY_REMOTE_GW6_MATCH)}",
            )

    # Validate remote-gw6-country if present
    if "remote-gw6-country" in payload:
        value = payload.get("remote-gw6-country")
        if value and isinstance(value, str) and len(value) > 2:
            return (False, "remote-gw6-country cannot exceed 2 characters")

    # Validate cert-peer-username-validation if present
    if "cert-peer-username-validation" in payload:
        value = payload.get("cert-peer-username-validation")
        if value and value not in VALID_BODY_CERT_PEER_USERNAME_VALIDATION:
            return (
                False,
                f"Invalid cert-peer-username-validation '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_PEER_USERNAME_VALIDATION)}",
            )

    # Validate cert-peer-username-strip if present
    if "cert-peer-username-strip" in payload:
        value = payload.get("cert-peer-username-strip")
        if value and value not in VALID_BODY_CERT_PEER_USERNAME_STRIP:
            return (
                False,
                f"Invalid cert-peer-username-strip '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_PEER_USERNAME_STRIP)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ipsec_phase1_delete(
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
