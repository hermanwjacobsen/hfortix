"""
Validation helpers for system global_ endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_LANGUAGE = [
    "english",
    "french",
    "spanish",
    "portuguese",
    "japanese",
    "trach",
    "simch",
    "korean",
]
VALID_BODY_GUI_ALLOW_INCOMPATIBLE_FABRIC_FGT = ["enable", "disable"]
VALID_BODY_GUI_IPV6 = ["enable", "disable"]
VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS = ["enable", "disable"]
VALID_BODY_GUI_LOCAL_OUT = ["enable", "disable"]
VALID_BODY_GUI_CERTIFICATES = ["enable", "disable"]
VALID_BODY_GUI_CUSTOM_LANGUAGE = ["enable", "disable"]
VALID_BODY_GUI_WIRELESS_OPENSECURITY = ["enable", "disable"]
VALID_BODY_GUI_APP_DETECTION_SDWAN = ["enable", "disable"]
VALID_BODY_GUI_DISPLAY_HOSTNAME = ["enable", "disable"]
VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX = ["enable", "disable"]
VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING = ["enable", "disable"]
VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING = ["enable", "disable"]
VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING = ["enable", "disable"]
VALID_BODY_GUI_WORKFLOW_MANAGEMENT = ["enable", "disable"]
VALID_BODY_GUI_CDN_USAGE = ["enable", "disable"]
VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS = ["tlsv1-1", "tlsv1-2", "tlsv1-3"]
VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES = [
    "TLS-AES-128-GCM-SHA256",
    "TLS-AES-256-GCM-SHA384",
    "TLS-CHACHA20-POLY1305-SHA256",
    "TLS-AES-128-CCM-SHA256",
    "TLS-AES-128-CCM-8-SHA256",
]
VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS = [
    "RSA",
    "DHE",
    "ECDHE",
    "DSS",
    "ECDSA",
    "AES",
    "AESGCM",
    "CAMELLIA",
    "3DES",
    "SHA1",
    "SHA256",
    "SHA384",
    "STATIC",
    "CHACHA20",
    "ARIA",
    "AESCCM",
]
VALID_BODY_SSD_TRIM_FREQ = ["never", "hourly", "daily", "weekly", "monthly"]
VALID_BODY_SSD_TRIM_WEEKDAY = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
VALID_BODY_ADMIN_CONCURRENT = ["enable", "disable"]
VALID_BODY_PURDUE_LEVEL = ["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"]
VALID_BODY_DAILY_RESTART = ["enable", "disable"]
VALID_BODY_WAD_RESTART_MODE = ["none", "time", "memory"]
VALID_BODY_BATCH_CMDB = ["enable", "disable"]
VALID_BODY_MULTI_FACTOR_AUTHENTICATION = ["optional", "mandatory"]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_AUTORUN_LOG_FSCK = ["enable", "disable"]
VALID_BODY_TRAFFIC_PRIORITY = ["tos", "dscp"]
VALID_BODY_TRAFFIC_PRIORITY_LEVEL = ["low", "medium", "high"]
VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO = ["cubic", "bbr", "bbr2", "reno"]
VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID = ["enable", "disable"]
VALID_BODY_QUIC_PMTUD = ["enable", "disable"]
VALID_BODY_ANTI_REPLAY = ["disable", "loose", "strict"]
VALID_BODY_SEND_PMTU_ICMP = ["enable", "disable"]
VALID_BODY_HONOR_DF = ["enable", "disable"]
VALID_BODY_PMTU_DISCOVERY = ["enable", "disable"]
VALID_BODY_VIRTUAL_SWITCH_VLAN = ["enable", "disable"]
VALID_BODY_REVISION_IMAGE_AUTO_BACKUP = ["enable", "disable"]
VALID_BODY_REVISION_BACKUP_ON_LOGOUT = ["enable", "disable"]
VALID_BODY_STRONG_CRYPTO = ["enable", "disable"]
VALID_BODY_SSL_STATIC_KEY_CIPHERS = ["enable", "disable"]
VALID_BODY_SNAT_ROUTE_CHANGE = ["enable", "disable"]
VALID_BODY_IPV6_SNAT_ROUTE_CHANGE = ["enable", "disable"]
VALID_BODY_SPEEDTEST_SERVER = ["enable", "disable"]
VALID_BODY_CLI_AUDIT_LOG = ["enable", "disable"]
VALID_BODY_DH_PARAMS = ["1024", "1536", "2048", "3072", "4096", "6144", "8192"]
VALID_BODY_FDS_STATISTICS = ["enable", "disable"]
VALID_BODY_TCP_OPTION = ["enable", "disable"]
VALID_BODY_LLDP_TRANSMISSION = ["enable", "disable"]
VALID_BODY_LLDP_RECEPTION = ["enable", "disable"]
VALID_BODY_PROXY_KEEP_ALIVE_MODE = ["session", "traffic", "re-authentication"]
VALID_BODY_PROXY_AUTH_LIFETIME = ["enable", "disable"]
VALID_BODY_PROXY_RESOURCE_MODE = ["enable", "disable"]
VALID_BODY_PROXY_CERT_USE_MGMT_VDOM = ["enable", "disable"]
VALID_BODY_CHECK_PROTOCOL_HEADER = ["loose", "strict"]
VALID_BODY_VIP_ARP_RANGE = ["unlimited", "restricted"]
VALID_BODY_RESET_SESSIONLESS_TCP = ["enable", "disable"]
VALID_BODY_ALLOW_TRAFFIC_REDIRECT = ["enable", "disable"]
VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT = ["enable", "disable"]
VALID_BODY_STRICT_DIRTY_SESSION_CHECK = ["enable", "disable"]
VALID_BODY_PRE_LOGIN_BANNER = ["enable", "disable"]
VALID_BODY_POST_LOGIN_BANNER = ["disable", "enable"]
VALID_BODY_TFTP = ["enable", "disable"]
VALID_BODY_AV_FAILOPEN = ["pass", "of", "one-shot"]
VALID_BODY_AV_FAILOPEN_SESSION = ["enable", "disable"]
VALID_BODY_LOG_SINGLE_CPU_HIGH = ["enable", "disable"]
VALID_BODY_CHECK_RESET_RANGE = ["strict", "disable"]
VALID_BODY_SINGLE_VDOM_NPUVLINK = ["enable", "disable"]
VALID_BODY_VDOM_MODE = ["no-vdom", "multi-vdom"]
VALID_BODY_LONG_VDOM_NAME = ["enable", "disable"]
VALID_BODY_UPGRADE_REPORT = ["enable", "disable"]
VALID_BODY_EDIT_VDOM_PROMPT = ["enable", "disable"]
VALID_BODY_ADMIN_HTTPS_REDIRECT = ["enable", "disable"]
VALID_BODY_ADMIN_SSH_PASSWORD = ["enable", "disable"]
VALID_BODY_ADMIN_RESTRICT_LOCAL = ["all", "non-console-only", "disable"]
VALID_BODY_ADMIN_SSH_V1 = ["enable", "disable"]
VALID_BODY_ADMIN_TELNET = ["enable", "disable"]
VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN = ["enable", "disable"]
VALID_BODY_ADMIN_RESET_BUTTON = ["enable", "disable"]
VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED = ["enable", "disable"]
VALID_BODY_AUTH_KEEPALIVE = ["enable", "disable"]
VALID_BODY_AUTH_SESSION_LIMIT = ["block-new", "logout-inactive"]
VALID_BODY_CLT_CERT_REQ = ["enable", "disable"]
VALID_BODY_CFG_SAVE = ["automatic", "manual", "revert"]
VALID_BODY_REBOOT_UPON_CONFIG_RESTORE = ["enable", "disable"]
VALID_BODY_ADMIN_SCP = ["enable", "disable"]
VALID_BODY_WIRELESS_CONTROLLER = ["enable", "disable"]
VALID_BODY_FORTIEXTENDER = ["disable", "enable"]
VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN = ["disable", "enable"]
VALID_BODY_FORTIEXTENDER_VLAN_MODE = ["enable", "disable"]
VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER = ["disable", "enable"]
VALID_BODY_PROXY_HARDWARE_ACCELERATION = ["disable", "enable"]
VALID_BODY_FGD_ALERT_SUBSCRIPTION = [
    "advisory",
    "latest-threat",
    "latest-virus",
    "latest-attack",
    "new-antivirus-db",
    "new-attack-db",
]
VALID_BODY_IPSEC_HMAC_OFFLOAD = ["enable", "disable"]
VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE = ["enable", "disable"]
VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE = ["enable", "disable"]
VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP = ["enable", "disable"]
VALID_BODY_CSR_CA_ATTRIBUTE = ["enable", "disable"]
VALID_BODY_WIMAX_4G_USB = ["enable", "disable"]
VALID_BODY_WAD_SOURCE_AFFINITY = ["disable", "enable"]
VALID_BODY_LOGIN_TIMESTAMP = ["enable", "disable"]
VALID_BODY_IP_CONFLICT_DETECTION = ["enable", "disable"]
VALID_BODY_SPECIAL_FILE_23_SUPPORT = ["disable", "enable"]
VALID_BODY_LOG_UUID_ADDRESS = ["enable", "disable"]
VALID_BODY_LOG_SSL_CONNECTION = ["enable", "disable"]
VALID_BODY_REST_API_KEY_URL_QUERY = ["enable", "disable"]
VALID_BODY_IPSEC_ASIC_OFFLOAD = ["enable", "disable"]
VALID_BODY_PRIVATE_DATA_ENCRYPTION = ["disable", "enable"]
VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE = ["enable", "disable"]
VALID_BODY_GUI_THEME = [
    "jade",
    "neutrino",
    "mariner",
    "graphite",
    "melongene",
    "jet-stream",
    "security-fabric",
    "retro",
    "dark-matter",
    "onyx",
    "eclipse",
]
VALID_BODY_GUI_DATE_FORMAT = [
    "yyyy/MM/dd",
    "dd/MM/yyyy",
    "MM/dd/yyyy",
    "yyyy-MM-dd",
    "dd-MM-yyyy",
    "MM-dd-yyyy",
]
VALID_BODY_GUI_DATE_TIME_SOURCE = ["system", "browser"]
VALID_BODY_CLOUD_COMMUNICATION = ["enable", "disable"]
VALID_BODY_FORTITOKEN_CLOUD = ["enable", "disable"]
VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS = ["enable", "disable"]
VALID_BODY_IRQ_TIME_ACCOUNTING = ["auto", "force"]
VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT = ["enable", "disable"]
VALID_BODY_FORTICONVERTER_INTEGRATION = ["enable", "disable"]
VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD = ["once", "disable"]
VALID_BODY_INTERNET_SERVICE_DATABASE = [
    "mini",
    "standard",
    "full",
    "on-demand",
]
VALID_BODY_GEOIP_FULL_DB = ["enable", "disable"]
VALID_BODY_EARLY_TCP_NPU_SESSION = ["enable", "disable"]
VALID_BODY_NPU_NEIGHBOR_UPDATE = ["enable", "disable"]
VALID_BODY_DELAY_TCP_NPU_SESSION = ["enable", "disable"]
VALID_BODY_INTERFACE_SUBNET_USAGE = ["disable", "enable"]
VALID_BODY_FORTIGSLB_INTEGRATION = ["disable", "enable"]
VALID_BODY_AUTH_SESSION_AUTO_BACKUP = ["enable", "disable"]
VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL = [
    "1min",
    "5min",
    "15min",
    "30min",
    "1hr",
]
VALID_BODY_APPLICATION_BANDWIDTH_TRACKING = ["disable", "enable"]
VALID_BODY_TLS_SESSION_CACHE = ["enable", "disable"]
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

    # Validate language if present
    if "language" in payload:
        value = payload.get("language")
        if value and value not in VALID_BODY_LANGUAGE:
            return (
                False,
                f"Invalid language '{value}'. Must be one of: {', '.join(VALID_BODY_LANGUAGE)}",
            )

    # Validate gui-allow-incompatible-fabric-fgt if present
    if "gui-allow-incompatible-fabric-fgt" in payload:
        value = payload.get("gui-allow-incompatible-fabric-fgt")
        if value and value not in VALID_BODY_GUI_ALLOW_INCOMPATIBLE_FABRIC_FGT:
            return (
                False,
                f"Invalid gui-allow-incompatible-fabric-fgt '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_ALLOW_INCOMPATIBLE_FABRIC_FGT)}",
            )

    # Validate gui-ipv6 if present
    if "gui-ipv6" in payload:
        value = payload.get("gui-ipv6")
        if value and value not in VALID_BODY_GUI_IPV6:
            return (
                False,
                f"Invalid gui-ipv6 '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_IPV6)}",
            )

    # Validate gui-replacement-message-groups if present
    if "gui-replacement-message-groups" in payload:
        value = payload.get("gui-replacement-message-groups")
        if value and value not in VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS:
            return (
                False,
                f"Invalid gui-replacement-message-groups '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_REPLACEMENT_MESSAGE_GROUPS)}",
            )

    # Validate gui-local-out if present
    if "gui-local-out" in payload:
        value = payload.get("gui-local-out")
        if value and value not in VALID_BODY_GUI_LOCAL_OUT:
            return (
                False,
                f"Invalid gui-local-out '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_LOCAL_OUT)}",
            )

    # Validate gui-certificates if present
    if "gui-certificates" in payload:
        value = payload.get("gui-certificates")
        if value and value not in VALID_BODY_GUI_CERTIFICATES:
            return (
                False,
                f"Invalid gui-certificates '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_CERTIFICATES)}",
            )

    # Validate gui-custom-language if present
    if "gui-custom-language" in payload:
        value = payload.get("gui-custom-language")
        if value and value not in VALID_BODY_GUI_CUSTOM_LANGUAGE:
            return (
                False,
                f"Invalid gui-custom-language '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_CUSTOM_LANGUAGE)}",
            )

    # Validate gui-wireless-opensecurity if present
    if "gui-wireless-opensecurity" in payload:
        value = payload.get("gui-wireless-opensecurity")
        if value and value not in VALID_BODY_GUI_WIRELESS_OPENSECURITY:
            return (
                False,
                f"Invalid gui-wireless-opensecurity '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WIRELESS_OPENSECURITY)}",
            )

    # Validate gui-app-detection-sdwan if present
    if "gui-app-detection-sdwan" in payload:
        value = payload.get("gui-app-detection-sdwan")
        if value and value not in VALID_BODY_GUI_APP_DETECTION_SDWAN:
            return (
                False,
                f"Invalid gui-app-detection-sdwan '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_APP_DETECTION_SDWAN)}",
            )

    # Validate gui-display-hostname if present
    if "gui-display-hostname" in payload:
        value = payload.get("gui-display-hostname")
        if value and value not in VALID_BODY_GUI_DISPLAY_HOSTNAME:
            return (
                False,
                f"Invalid gui-display-hostname '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DISPLAY_HOSTNAME)}",
            )

    # Validate gui-fortigate-cloud-sandbox if present
    if "gui-fortigate-cloud-sandbox" in payload:
        value = payload.get("gui-fortigate-cloud-sandbox")
        if value and value not in VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX:
            return (
                False,
                f"Invalid gui-fortigate-cloud-sandbox '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FORTIGATE_CLOUD_SANDBOX)}",
            )

    # Validate gui-firmware-upgrade-warning if present
    if "gui-firmware-upgrade-warning" in payload:
        value = payload.get("gui-firmware-upgrade-warning")
        if value and value not in VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING:
            return (
                False,
                f"Invalid gui-firmware-upgrade-warning '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FIRMWARE_UPGRADE_WARNING)}",
            )

    # Validate gui-forticare-registration-setup-warning if present
    if "gui-forticare-registration-setup-warning" in payload:
        value = payload.get("gui-forticare-registration-setup-warning")
        if (
            value
            and value
            not in VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING
        ):
            return (
                False,
                f"Invalid gui-forticare-registration-setup-warning '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_FORTICARE_REGISTRATION_SETUP_WARNING)}",
            )

    # Validate gui-auto-upgrade-setup-warning if present
    if "gui-auto-upgrade-setup-warning" in payload:
        value = payload.get("gui-auto-upgrade-setup-warning")
        if value and value not in VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING:
            return (
                False,
                f"Invalid gui-auto-upgrade-setup-warning '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_AUTO_UPGRADE_SETUP_WARNING)}",
            )

    # Validate gui-workflow-management if present
    if "gui-workflow-management" in payload:
        value = payload.get("gui-workflow-management")
        if value and value not in VALID_BODY_GUI_WORKFLOW_MANAGEMENT:
            return (
                False,
                f"Invalid gui-workflow-management '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_WORKFLOW_MANAGEMENT)}",
            )

    # Validate gui-cdn-usage if present
    if "gui-cdn-usage" in payload:
        value = payload.get("gui-cdn-usage")
        if value and value not in VALID_BODY_GUI_CDN_USAGE:
            return (
                False,
                f"Invalid gui-cdn-usage '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_CDN_USAGE)}",
            )

    # Validate admin-https-ssl-versions if present
    if "admin-https-ssl-versions" in payload:
        value = payload.get("admin-https-ssl-versions")
        if value and value not in VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS:
            return (
                False,
                f"Invalid admin-https-ssl-versions '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_SSL_VERSIONS)}",
            )

    # Validate admin-https-ssl-ciphersuites if present
    if "admin-https-ssl-ciphersuites" in payload:
        value = payload.get("admin-https-ssl-ciphersuites")
        if value and value not in VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES:
            return (
                False,
                f"Invalid admin-https-ssl-ciphersuites '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_SSL_CIPHERSUITES)}",
            )

    # Validate admin-https-ssl-banned-ciphers if present
    if "admin-https-ssl-banned-ciphers" in payload:
        value = payload.get("admin-https-ssl-banned-ciphers")
        if value and value not in VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS:
            return (
                False,
                f"Invalid admin-https-ssl-banned-ciphers '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_SSL_BANNED_CIPHERS)}",
            )

    # Validate admintimeout if present
    if "admintimeout" in payload:
        value = payload.get("admintimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 480:
                    return (False, "admintimeout must be between 1 and 480")
            except (ValueError, TypeError):
                return (False, f"admintimeout must be numeric, got: {value}")

    # Validate admin-console-timeout if present
    if "admin-console-timeout" in payload:
        value = payload.get("admin-console-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 15 or int_val > 300:
                    return (
                        False,
                        "admin-console-timeout must be between 15 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"admin-console-timeout must be numeric, got: {value}",
                )

    # Validate ssd-trim-freq if present
    if "ssd-trim-freq" in payload:
        value = payload.get("ssd-trim-freq")
        if value and value not in VALID_BODY_SSD_TRIM_FREQ:
            return (
                False,
                f"Invalid ssd-trim-freq '{value}'. Must be one of: {', '.join(VALID_BODY_SSD_TRIM_FREQ)}",
            )

    # Validate ssd-trim-hour if present
    if "ssd-trim-hour" in payload:
        value = payload.get("ssd-trim-hour")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 23:
                    return (False, "ssd-trim-hour must be between 0 and 23")
            except (ValueError, TypeError):
                return (False, f"ssd-trim-hour must be numeric, got: {value}")

    # Validate ssd-trim-min if present
    if "ssd-trim-min" in payload:
        value = payload.get("ssd-trim-min")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 60:
                    return (False, "ssd-trim-min must be between 0 and 60")
            except (ValueError, TypeError):
                return (False, f"ssd-trim-min must be numeric, got: {value}")

    # Validate ssd-trim-weekday if present
    if "ssd-trim-weekday" in payload:
        value = payload.get("ssd-trim-weekday")
        if value and value not in VALID_BODY_SSD_TRIM_WEEKDAY:
            return (
                False,
                f"Invalid ssd-trim-weekday '{value}'. Must be one of: {', '.join(VALID_BODY_SSD_TRIM_WEEKDAY)}",
            )

    # Validate ssd-trim-date if present
    if "ssd-trim-date" in payload:
        value = payload.get("ssd-trim-date")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 31:
                    return (False, "ssd-trim-date must be between 1 and 31")
            except (ValueError, TypeError):
                return (False, f"ssd-trim-date must be numeric, got: {value}")

    # Validate admin-concurrent if present
    if "admin-concurrent" in payload:
        value = payload.get("admin-concurrent")
        if value and value not in VALID_BODY_ADMIN_CONCURRENT:
            return (
                False,
                f"Invalid admin-concurrent '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_CONCURRENT)}",
            )

    # Validate admin-lockout-threshold if present
    if "admin-lockout-threshold" in payload:
        value = payload.get("admin-lockout-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (
                        False,
                        "admin-lockout-threshold must be between 1 and 10",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"admin-lockout-threshold must be numeric, got: {value}",
                )

    # Validate admin-lockout-duration if present
    if "admin-lockout-duration" in payload:
        value = payload.get("admin-lockout-duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2147483647:
                    return (
                        False,
                        "admin-lockout-duration must be between 1 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"admin-lockout-duration must be numeric, got: {value}",
                )

    # Validate refresh if present
    if "refresh" in payload:
        value = payload.get("refresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "refresh must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"refresh must be numeric, got: {value}")

    # Validate interval if present
    if "interval" in payload:
        value = payload.get("interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "interval must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"interval must be numeric, got: {value}")

    # Validate failtime if present
    if "failtime" in payload:
        value = payload.get("failtime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "failtime must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"failtime must be numeric, got: {value}")

    # Validate purdue-level if present
    if "purdue-level" in payload:
        value = payload.get("purdue-level")
        if value and value not in VALID_BODY_PURDUE_LEVEL:
            return (
                False,
                f"Invalid purdue-level '{value}'. Must be one of: {', '.join(VALID_BODY_PURDUE_LEVEL)}",
            )

    # Validate daily-restart if present
    if "daily-restart" in payload:
        value = payload.get("daily-restart")
        if value and value not in VALID_BODY_DAILY_RESTART:
            return (
                False,
                f"Invalid daily-restart '{value}'. Must be one of: {', '.join(VALID_BODY_DAILY_RESTART)}",
            )

    # Validate wad-restart-mode if present
    if "wad-restart-mode" in payload:
        value = payload.get("wad-restart-mode")
        if value and value not in VALID_BODY_WAD_RESTART_MODE:
            return (
                False,
                f"Invalid wad-restart-mode '{value}'. Must be one of: {', '.join(VALID_BODY_WAD_RESTART_MODE)}",
            )

    # Validate wad-p2s-max-body-size if present
    if "wad-p2s-max-body-size" in payload:
        value = payload.get("wad-p2s-max-body-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 32:
                    return (
                        False,
                        "wad-p2s-max-body-size must be between 1 and 32",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wad-p2s-max-body-size must be numeric, got: {value}",
                )

    # Validate radius-port if present
    if "radius-port" in payload:
        value = payload.get("radius-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "radius-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"radius-port must be numeric, got: {value}")

    # Validate speedtestd-server-port if present
    if "speedtestd-server-port" in payload:
        value = payload.get("speedtestd-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "speedtestd-server-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"speedtestd-server-port must be numeric, got: {value}",
                )

    # Validate speedtestd-ctrl-port if present
    if "speedtestd-ctrl-port" in payload:
        value = payload.get("speedtestd-ctrl-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "speedtestd-ctrl-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"speedtestd-ctrl-port must be numeric, got: {value}",
                )

    # Validate admin-login-max if present
    if "admin-login-max" in payload:
        value = payload.get("admin-login-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "admin-login-max must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"admin-login-max must be numeric, got: {value}",
                )

    # Validate remoteauthtimeout if present
    if "remoteauthtimeout" in payload:
        value = payload.get("remoteauthtimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (
                        False,
                        "remoteauthtimeout must be between 1 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"remoteauthtimeout must be numeric, got: {value}",
                )

    # Validate ldapconntimeout if present
    if "ldapconntimeout" in payload:
        value = payload.get("ldapconntimeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300000:
                    return (
                        False,
                        "ldapconntimeout must be between 1 and 300000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ldapconntimeout must be numeric, got: {value}",
                )

    # Validate batch-cmdb if present
    if "batch-cmdb" in payload:
        value = payload.get("batch-cmdb")
        if value and value not in VALID_BODY_BATCH_CMDB:
            return (
                False,
                f"Invalid batch-cmdb '{value}'. Must be one of: {', '.join(VALID_BODY_BATCH_CMDB)}",
            )

    # Validate multi-factor-authentication if present
    if "multi-factor-authentication" in payload:
        value = payload.get("multi-factor-authentication")
        if value and value not in VALID_BODY_MULTI_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid multi-factor-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_MULTI_FACTOR_AUTHENTICATION)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate autorun-log-fsck if present
    if "autorun-log-fsck" in payload:
        value = payload.get("autorun-log-fsck")
        if value and value not in VALID_BODY_AUTORUN_LOG_FSCK:
            return (
                False,
                f"Invalid autorun-log-fsck '{value}'. Must be one of: {', '.join(VALID_BODY_AUTORUN_LOG_FSCK)}",
            )

    # Validate timezone if present
    if "timezone" in payload:
        value = payload.get("timezone")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "timezone cannot exceed 63 characters")

    # Validate traffic-priority if present
    if "traffic-priority" in payload:
        value = payload.get("traffic-priority")
        if value and value not in VALID_BODY_TRAFFIC_PRIORITY:
            return (
                False,
                f"Invalid traffic-priority '{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_PRIORITY)}",
            )

    # Validate traffic-priority-level if present
    if "traffic-priority-level" in payload:
        value = payload.get("traffic-priority-level")
        if value and value not in VALID_BODY_TRAFFIC_PRIORITY_LEVEL:
            return (
                False,
                f"Invalid traffic-priority-level '{value}'. Must be one of: {', '.join(VALID_BODY_TRAFFIC_PRIORITY_LEVEL)}",
            )

    # Validate quic-congestion-control-algo if present
    if "quic-congestion-control-algo" in payload:
        value = payload.get("quic-congestion-control-algo")
        if value and value not in VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO:
            return (
                False,
                f"Invalid quic-congestion-control-algo '{value}'. Must be one of: {', '.join(VALID_BODY_QUIC_CONGESTION_CONTROL_ALGO)}",
            )

    # Validate quic-max-datagram-size if present
    if "quic-max-datagram-size" in payload:
        value = payload.get("quic-max-datagram-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1200 or int_val > 1500:
                    return (
                        False,
                        "quic-max-datagram-size must be between 1200 and 1500",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"quic-max-datagram-size must be numeric, got: {value}",
                )

    # Validate quic-udp-payload-size-shaping-per-cid if present
    if "quic-udp-payload-size-shaping-per-cid" in payload:
        value = payload.get("quic-udp-payload-size-shaping-per-cid")
        if (
            value
            and value not in VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID
        ):
            return (
                False,
                f"Invalid quic-udp-payload-size-shaping-per-cid '{value}'. Must be one of: {', '.join(VALID_BODY_QUIC_UDP_PAYLOAD_SIZE_SHAPING_PER_CID)}",
            )

    # Validate quic-ack-thresold if present
    if "quic-ack-thresold" in payload:
        value = payload.get("quic-ack-thresold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 5:
                    return (
                        False,
                        "quic-ack-thresold must be between 2 and 5",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"quic-ack-thresold must be numeric, got: {value}",
                )

    # Validate quic-pmtud if present
    if "quic-pmtud" in payload:
        value = payload.get("quic-pmtud")
        if value and value not in VALID_BODY_QUIC_PMTUD:
            return (
                False,
                f"Invalid quic-pmtud '{value}'. Must be one of: {', '.join(VALID_BODY_QUIC_PMTUD)}",
            )

    # Validate quic-tls-handshake-timeout if present
    if "quic-tls-handshake-timeout" in payload:
        value = payload.get("quic-tls-handshake-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 60:
                    return (
                        False,
                        "quic-tls-handshake-timeout must be between 1 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"quic-tls-handshake-timeout must be numeric, got: {value}",
                )

    # Validate anti-replay if present
    if "anti-replay" in payload:
        value = payload.get("anti-replay")
        if value and value not in VALID_BODY_ANTI_REPLAY:
            return (
                False,
                f"Invalid anti-replay '{value}'. Must be one of: {', '.join(VALID_BODY_ANTI_REPLAY)}",
            )

    # Validate send-pmtu-icmp if present
    if "send-pmtu-icmp" in payload:
        value = payload.get("send-pmtu-icmp")
        if value and value not in VALID_BODY_SEND_PMTU_ICMP:
            return (
                False,
                f"Invalid send-pmtu-icmp '{value}'. Must be one of: {', '.join(VALID_BODY_SEND_PMTU_ICMP)}",
            )

    # Validate honor-df if present
    if "honor-d" in payload:
        value = payload.get("honor-d")
        if value and value not in VALID_BODY_HONOR_DF:
            return (
                False,
                f"Invalid honor-df '{value}'. Must be one of: {', '.join(VALID_BODY_HONOR_DF)}",
            )

    # Validate pmtu-discovery if present
    if "pmtu-discovery" in payload:
        value = payload.get("pmtu-discovery")
        if value and value not in VALID_BODY_PMTU_DISCOVERY:
            return (
                False,
                f"Invalid pmtu-discovery '{value}'. Must be one of: {', '.join(VALID_BODY_PMTU_DISCOVERY)}",
            )

    # Validate virtual-switch-vlan if present
    if "virtual-switch-vlan" in payload:
        value = payload.get("virtual-switch-vlan")
        if value and value not in VALID_BODY_VIRTUAL_SWITCH_VLAN:
            return (
                False,
                f"Invalid virtual-switch-vlan '{value}'. Must be one of: {', '.join(VALID_BODY_VIRTUAL_SWITCH_VLAN)}",
            )

    # Validate revision-image-auto-backup if present
    if "revision-image-auto-backup" in payload:
        value = payload.get("revision-image-auto-backup")
        if value and value not in VALID_BODY_REVISION_IMAGE_AUTO_BACKUP:
            return (
                False,
                f"Invalid revision-image-auto-backup '{value}'. Must be one of: {', '.join(VALID_BODY_REVISION_IMAGE_AUTO_BACKUP)}",
            )

    # Validate revision-backup-on-logout if present
    if "revision-backup-on-logout" in payload:
        value = payload.get("revision-backup-on-logout")
        if value and value not in VALID_BODY_REVISION_BACKUP_ON_LOGOUT:
            return (
                False,
                f"Invalid revision-backup-on-logout '{value}'. Must be one of: {', '.join(VALID_BODY_REVISION_BACKUP_ON_LOGOUT)}",
            )

    # Validate management-vdom if present
    if "management-vdom" in payload:
        value = payload.get("management-vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "management-vdom cannot exceed 31 characters")

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "hostname cannot exceed 35 characters")

    # Validate alias if present
    if "alias" in payload:
        value = payload.get("alias")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "alias cannot exceed 35 characters")

    # Validate strong-crypto if present
    if "strong-crypto" in payload:
        value = payload.get("strong-crypto")
        if value and value not in VALID_BODY_STRONG_CRYPTO:
            return (
                False,
                f"Invalid strong-crypto '{value}'. Must be one of: {', '.join(VALID_BODY_STRONG_CRYPTO)}",
            )

    # Validate ssl-static-key-ciphers if present
    if "ssl-static-key-ciphers" in payload:
        value = payload.get("ssl-static-key-ciphers")
        if value and value not in VALID_BODY_SSL_STATIC_KEY_CIPHERS:
            return (
                False,
                f"Invalid ssl-static-key-ciphers '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_STATIC_KEY_CIPHERS)}",
            )

    # Validate snat-route-change if present
    if "snat-route-change" in payload:
        value = payload.get("snat-route-change")
        if value and value not in VALID_BODY_SNAT_ROUTE_CHANGE:
            return (
                False,
                f"Invalid snat-route-change '{value}'. Must be one of: {', '.join(VALID_BODY_SNAT_ROUTE_CHANGE)}",
            )

    # Validate ipv6-snat-route-change if present
    if "ipv6-snat-route-change" in payload:
        value = payload.get("ipv6-snat-route-change")
        if value and value not in VALID_BODY_IPV6_SNAT_ROUTE_CHANGE:
            return (
                False,
                f"Invalid ipv6-snat-route-change '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_SNAT_ROUTE_CHANGE)}",
            )

    # Validate speedtest-server if present
    if "speedtest-server" in payload:
        value = payload.get("speedtest-server")
        if value and value not in VALID_BODY_SPEEDTEST_SERVER:
            return (
                False,
                f"Invalid speedtest-server '{value}'. Must be one of: {', '.join(VALID_BODY_SPEEDTEST_SERVER)}",
            )

    # Validate cli-audit-log if present
    if "cli-audit-log" in payload:
        value = payload.get("cli-audit-log")
        if value and value not in VALID_BODY_CLI_AUDIT_LOG:
            return (
                False,
                f"Invalid cli-audit-log '{value}'. Must be one of: {', '.join(VALID_BODY_CLI_AUDIT_LOG)}",
            )

    # Validate dh-params if present
    if "dh-params" in payload:
        value = payload.get("dh-params")
        if value and value not in VALID_BODY_DH_PARAMS:
            return (
                False,
                f"Invalid dh-params '{value}'. Must be one of: {', '.join(VALID_BODY_DH_PARAMS)}",
            )

    # Validate fds-statistics if present
    if "fds-statistics" in payload:
        value = payload.get("fds-statistics")
        if value and value not in VALID_BODY_FDS_STATISTICS:
            return (
                False,
                f"Invalid fds-statistics '{value}'. Must be one of: {', '.join(VALID_BODY_FDS_STATISTICS)}",
            )

    # Validate fds-statistics-period if present
    if "fds-statistics-period" in payload:
        value = payload.get("fds-statistics-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1440:
                    return (
                        False,
                        "fds-statistics-period must be between 1 and 1440",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fds-statistics-period must be numeric, got: {value}",
                )

    # Validate tcp-option if present
    if "tcp-option" in payload:
        value = payload.get("tcp-option")
        if value and value not in VALID_BODY_TCP_OPTION:
            return (
                False,
                f"Invalid tcp-option '{value}'. Must be one of: {', '.join(VALID_BODY_TCP_OPTION)}",
            )

    # Validate lldp-transmission if present
    if "lldp-transmission" in payload:
        value = payload.get("lldp-transmission")
        if value and value not in VALID_BODY_LLDP_TRANSMISSION:
            return (
                False,
                f"Invalid lldp-transmission '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_TRANSMISSION)}",
            )

    # Validate lldp-reception if present
    if "lldp-reception" in payload:
        value = payload.get("lldp-reception")
        if value and value not in VALID_BODY_LLDP_RECEPTION:
            return (
                False,
                f"Invalid lldp-reception '{value}'. Must be one of: {', '.join(VALID_BODY_LLDP_RECEPTION)}",
            )

    # Validate proxy-auth-timeout if present
    if "proxy-auth-timeout" in payload:
        value = payload.get("proxy-auth-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10000:
                    return (
                        False,
                        "proxy-auth-timeout must be between 1 and 10000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"proxy-auth-timeout must be numeric, got: {value}",
                )

    # Validate proxy-keep-alive-mode if present
    if "proxy-keep-alive-mode" in payload:
        value = payload.get("proxy-keep-alive-mode")
        if value and value not in VALID_BODY_PROXY_KEEP_ALIVE_MODE:
            return (
                False,
                f"Invalid proxy-keep-alive-mode '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_KEEP_ALIVE_MODE)}",
            )

    # Validate proxy-re-authentication-time if present
    if "proxy-re-authentication-time" in payload:
        value = payload.get("proxy-re-authentication-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 86400:
                    return (
                        False,
                        "proxy-re-authentication-time must be between 1 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"proxy-re-authentication-time must be numeric, got: {value}",
                )

    # Validate proxy-auth-lifetime if present
    if "proxy-auth-lifetime" in payload:
        value = payload.get("proxy-auth-lifetime")
        if value and value not in VALID_BODY_PROXY_AUTH_LIFETIME:
            return (
                False,
                f"Invalid proxy-auth-lifetime '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_AUTH_LIFETIME)}",
            )

    # Validate proxy-auth-lifetime-timeout if present
    if "proxy-auth-lifetime-timeout" in payload:
        value = payload.get("proxy-auth-lifetime-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 65535:
                    return (
                        False,
                        "proxy-auth-lifetime-timeout must be between 5 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"proxy-auth-lifetime-timeout must be numeric, got: {value}",
                )

    # Validate proxy-resource-mode if present
    if "proxy-resource-mode" in payload:
        value = payload.get("proxy-resource-mode")
        if value and value not in VALID_BODY_PROXY_RESOURCE_MODE:
            return (
                False,
                f"Invalid proxy-resource-mode '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_RESOURCE_MODE)}",
            )

    # Validate proxy-cert-use-mgmt-vdom if present
    if "proxy-cert-use-mgmt-vdom" in payload:
        value = payload.get("proxy-cert-use-mgmt-vdom")
        if value and value not in VALID_BODY_PROXY_CERT_USE_MGMT_VDOM:
            return (
                False,
                f"Invalid proxy-cert-use-mgmt-vdom '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_CERT_USE_MGMT_VDOM)}",
            )

    # Validate sys-perf-log-interval if present
    if "sys-perf-log-interval" in payload:
        value = payload.get("sys-perf-log-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 15:
                    return (
                        False,
                        "sys-perf-log-interval must be between 0 and 15",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sys-perf-log-interval must be numeric, got: {value}",
                )

    # Validate check-protocol-header if present
    if "check-protocol-header" in payload:
        value = payload.get("check-protocol-header")
        if value and value not in VALID_BODY_CHECK_PROTOCOL_HEADER:
            return (
                False,
                f"Invalid check-protocol-header '{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_PROTOCOL_HEADER)}",
            )

    # Validate vip-arp-range if present
    if "vip-arp-range" in payload:
        value = payload.get("vip-arp-range")
        if value and value not in VALID_BODY_VIP_ARP_RANGE:
            return (
                False,
                f"Invalid vip-arp-range '{value}'. Must be one of: {', '.join(VALID_BODY_VIP_ARP_RANGE)}",
            )

    # Validate reset-sessionless-tcp if present
    if "reset-sessionless-tcp" in payload:
        value = payload.get("reset-sessionless-tcp")
        if value and value not in VALID_BODY_RESET_SESSIONLESS_TCP:
            return (
                False,
                f"Invalid reset-sessionless-tcp '{value}'. Must be one of: {', '.join(VALID_BODY_RESET_SESSIONLESS_TCP)}",
            )

    # Validate allow-traffic-redirect if present
    if "allow-traffic-redirect" in payload:
        value = payload.get("allow-traffic-redirect")
        if value and value not in VALID_BODY_ALLOW_TRAFFIC_REDIRECT:
            return (
                False,
                f"Invalid allow-traffic-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_ALLOW_TRAFFIC_REDIRECT)}",
            )

    # Validate ipv6-allow-traffic-redirect if present
    if "ipv6-allow-traffic-redirect" in payload:
        value = payload.get("ipv6-allow-traffic-redirect")
        if value and value not in VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT:
            return (
                False,
                f"Invalid ipv6-allow-traffic-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ALLOW_TRAFFIC_REDIRECT)}",
            )

    # Validate strict-dirty-session-check if present
    if "strict-dirty-session-check" in payload:
        value = payload.get("strict-dirty-session-check")
        if value and value not in VALID_BODY_STRICT_DIRTY_SESSION_CHECK:
            return (
                False,
                f"Invalid strict-dirty-session-check '{value}'. Must be one of: {', '.join(VALID_BODY_STRICT_DIRTY_SESSION_CHECK)}",
            )

    # Validate tcp-halfclose-timer if present
    if "tcp-halfclose-timer" in payload:
        value = payload.get("tcp-halfclose-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 86400:
                    return (
                        False,
                        "tcp-halfclose-timer must be between 1 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-halfclose-timer must be numeric, got: {value}",
                )

    # Validate tcp-halfopen-timer if present
    if "tcp-halfopen-timer" in payload:
        value = payload.get("tcp-halfopen-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 86400:
                    return (
                        False,
                        "tcp-halfopen-timer must be between 1 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-halfopen-timer must be numeric, got: {value}",
                )

    # Validate tcp-timewait-timer if present
    if "tcp-timewait-timer" in payload:
        value = payload.get("tcp-timewait-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 300:
                    return (
                        False,
                        "tcp-timewait-timer must be between 0 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"tcp-timewait-timer must be numeric, got: {value}",
                )

    # Validate tcp-rst-timer if present
    if "tcp-rst-timer" in payload:
        value = payload.get("tcp-rst-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 300:
                    return (False, "tcp-rst-timer must be between 5 and 300")
            except (ValueError, TypeError):
                return (False, f"tcp-rst-timer must be numeric, got: {value}")

    # Validate udp-idle-timer if present
    if "udp-idle-timer" in payload:
        value = payload.get("udp-idle-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 86400:
                    return (
                        False,
                        "udp-idle-timer must be between 1 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"udp-idle-timer must be numeric, got: {value}")

    # Validate block-session-timer if present
    if "block-session-timer" in payload:
        value = payload.get("block-session-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 300:
                    return (
                        False,
                        "block-session-timer must be between 1 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"block-session-timer must be numeric, got: {value}",
                )

    # Validate pre-login-banner if present
    if "pre-login-banner" in payload:
        value = payload.get("pre-login-banner")
        if value and value not in VALID_BODY_PRE_LOGIN_BANNER:
            return (
                False,
                f"Invalid pre-login-banner '{value}'. Must be one of: {', '.join(VALID_BODY_PRE_LOGIN_BANNER)}",
            )

    # Validate post-login-banner if present
    if "post-login-banner" in payload:
        value = payload.get("post-login-banner")
        if value and value not in VALID_BODY_POST_LOGIN_BANNER:
            return (
                False,
                f"Invalid post-login-banner '{value}'. Must be one of: {', '.join(VALID_BODY_POST_LOGIN_BANNER)}",
            )

    # Validate tftp if present
    if "tftp" in payload:
        value = payload.get("tftp")
        if value and value not in VALID_BODY_TFTP:
            return (
                False,
                f"Invalid tftp '{value}'. Must be one of: {', '.join(VALID_BODY_TFTP)}",
            )

    # Validate av-failopen if present
    if "av-failopen" in payload:
        value = payload.get("av-failopen")
        if value and value not in VALID_BODY_AV_FAILOPEN:
            return (
                False,
                f"Invalid av-failopen '{value}'. Must be one of: {', '.join(VALID_BODY_AV_FAILOPEN)}",
            )

    # Validate av-failopen-session if present
    if "av-failopen-session" in payload:
        value = payload.get("av-failopen-session")
        if value and value not in VALID_BODY_AV_FAILOPEN_SESSION:
            return (
                False,
                f"Invalid av-failopen-session '{value}'. Must be one of: {', '.join(VALID_BODY_AV_FAILOPEN_SESSION)}",
            )

    # Validate memory-use-threshold-extreme if present
    if "memory-use-threshold-extreme" in payload:
        value = payload.get("memory-use-threshold-extreme")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 70 or int_val > 97:
                    return (
                        False,
                        "memory-use-threshold-extreme must be between 70 and 97",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"memory-use-threshold-extreme must be numeric, got: {value}",
                )

    # Validate memory-use-threshold-red if present
    if "memory-use-threshold-red" in payload:
        value = payload.get("memory-use-threshold-red")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 70 or int_val > 97:
                    return (
                        False,
                        "memory-use-threshold-red must be between 70 and 97",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"memory-use-threshold-red must be numeric, got: {value}",
                )

    # Validate memory-use-threshold-green if present
    if "memory-use-threshold-green" in payload:
        value = payload.get("memory-use-threshold-green")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 70 or int_val > 97:
                    return (
                        False,
                        "memory-use-threshold-green must be between 70 and 97",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"memory-use-threshold-green must be numeric, got: {value}",
                )

    # Validate ip-fragment-mem-thresholds if present
    if "ip-fragment-mem-thresholds" in payload:
        value = payload.get("ip-fragment-mem-thresholds")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 32 or int_val > 2047:
                    return (
                        False,
                        "ip-fragment-mem-thresholds must be between 32 and 2047",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ip-fragment-mem-thresholds must be numeric, got: {value}",
                )

    # Validate ip-fragment-timeout if present
    if "ip-fragment-timeout" in payload:
        value = payload.get("ip-fragment-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 30:
                    return (
                        False,
                        "ip-fragment-timeout must be between 3 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ip-fragment-timeout must be numeric, got: {value}",
                )

    # Validate ipv6-fragment-timeout if present
    if "ipv6-fragment-timeout" in payload:
        value = payload.get("ipv6-fragment-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 60:
                    return (
                        False,
                        "ipv6-fragment-timeout must be between 5 and 60",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ipv6-fragment-timeout must be numeric, got: {value}",
                )

    # Validate cpu-use-threshold if present
    if "cpu-use-threshold" in payload:
        value = payload.get("cpu-use-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 50 or int_val > 99:
                    return (
                        False,
                        "cpu-use-threshold must be between 50 and 99",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cpu-use-threshold must be numeric, got: {value}",
                )

    # Validate log-single-cpu-high if present
    if "log-single-cpu-high" in payload:
        value = payload.get("log-single-cpu-high")
        if value and value not in VALID_BODY_LOG_SINGLE_CPU_HIGH:
            return (
                False,
                f"Invalid log-single-cpu-high '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_SINGLE_CPU_HIGH)}",
            )

    # Validate check-reset-range if present
    if "check-reset-range" in payload:
        value = payload.get("check-reset-range")
        if value and value not in VALID_BODY_CHECK_RESET_RANGE:
            return (
                False,
                f"Invalid check-reset-range '{value}'. Must be one of: {', '.join(VALID_BODY_CHECK_RESET_RANGE)}",
            )

    # Validate single-vdom-npuvlink if present
    if "single-vdom-npuvlink" in payload:
        value = payload.get("single-vdom-npuvlink")
        if value and value not in VALID_BODY_SINGLE_VDOM_NPUVLINK:
            return (
                False,
                f"Invalid single-vdom-npuvlink '{value}'. Must be one of: {', '.join(VALID_BODY_SINGLE_VDOM_NPUVLINK)}",
            )

    # Validate vdom-mode if present
    if "vdom-mode" in payload:
        value = payload.get("vdom-mode")
        if value and value not in VALID_BODY_VDOM_MODE:
            return (
                False,
                f"Invalid vdom-mode '{value}'. Must be one of: {', '.join(VALID_BODY_VDOM_MODE)}",
            )

    # Validate long-vdom-name if present
    if "long-vdom-name" in payload:
        value = payload.get("long-vdom-name")
        if value and value not in VALID_BODY_LONG_VDOM_NAME:
            return (
                False,
                f"Invalid long-vdom-name '{value}'. Must be one of: {', '.join(VALID_BODY_LONG_VDOM_NAME)}",
            )

    # Validate upgrade-report if present
    if "upgrade-report" in payload:
        value = payload.get("upgrade-report")
        if value and value not in VALID_BODY_UPGRADE_REPORT:
            return (
                False,
                f"Invalid upgrade-report '{value}'. Must be one of: {', '.join(VALID_BODY_UPGRADE_REPORT)}",
            )

    # Validate edit-vdom-prompt if present
    if "edit-vdom-prompt" in payload:
        value = payload.get("edit-vdom-prompt")
        if value and value not in VALID_BODY_EDIT_VDOM_PROMPT:
            return (
                False,
                f"Invalid edit-vdom-prompt '{value}'. Must be one of: {', '.join(VALID_BODY_EDIT_VDOM_PROMPT)}",
            )

    # Validate admin-port if present
    if "admin-port" in payload:
        value = payload.get("admin-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "admin-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"admin-port must be numeric, got: {value}")

    # Validate admin-sport if present
    if "admin-sport" in payload:
        value = payload.get("admin-sport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "admin-sport must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"admin-sport must be numeric, got: {value}")

    # Validate admin-host if present
    if "admin-host" in payload:
        value = payload.get("admin-host")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "admin-host cannot exceed 255 characters")

    # Validate admin-https-redirect if present
    if "admin-https-redirect" in payload:
        value = payload.get("admin-https-redirect")
        if value and value not in VALID_BODY_ADMIN_HTTPS_REDIRECT:
            return (
                False,
                f"Invalid admin-https-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_REDIRECT)}",
            )

    # Validate admin-hsts-max-age if present
    if "admin-hsts-max-age" in payload:
        value = payload.get("admin-hsts-max-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "admin-hsts-max-age must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"admin-hsts-max-age must be numeric, got: {value}",
                )

    # Validate admin-ssh-password if present
    if "admin-ssh-password" in payload:
        value = payload.get("admin-ssh-password")
        if value and value not in VALID_BODY_ADMIN_SSH_PASSWORD:
            return (
                False,
                f"Invalid admin-ssh-password '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_SSH_PASSWORD)}",
            )

    # Validate admin-restrict-local if present
    if "admin-restrict-local" in payload:
        value = payload.get("admin-restrict-local")
        if value and value not in VALID_BODY_ADMIN_RESTRICT_LOCAL:
            return (
                False,
                f"Invalid admin-restrict-local '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_RESTRICT_LOCAL)}",
            )

    # Validate admin-ssh-port if present
    if "admin-ssh-port" in payload:
        value = payload.get("admin-ssh-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "admin-ssh-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"admin-ssh-port must be numeric, got: {value}")

    # Validate admin-ssh-grace-time if present
    if "admin-ssh-grace-time" in payload:
        value = payload.get("admin-ssh-grace-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (
                        False,
                        "admin-ssh-grace-time must be between 10 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"admin-ssh-grace-time must be numeric, got: {value}",
                )

    # Validate admin-ssh-v1 if present
    if "admin-ssh-v1" in payload:
        value = payload.get("admin-ssh-v1")
        if value and value not in VALID_BODY_ADMIN_SSH_V1:
            return (
                False,
                f"Invalid admin-ssh-v1 '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_SSH_V1)}",
            )

    # Validate admin-telnet if present
    if "admin-telnet" in payload:
        value = payload.get("admin-telnet")
        if value and value not in VALID_BODY_ADMIN_TELNET:
            return (
                False,
                f"Invalid admin-telnet '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_TELNET)}",
            )

    # Validate admin-telnet-port if present
    if "admin-telnet-port" in payload:
        value = payload.get("admin-telnet-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "admin-telnet-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"admin-telnet-port must be numeric, got: {value}",
                )

    # Validate admin-forticloud-sso-login if present
    if "admin-forticloud-sso-login" in payload:
        value = payload.get("admin-forticloud-sso-login")
        if value and value not in VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN:
            return (
                False,
                f"Invalid admin-forticloud-sso-login '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_FORTICLOUD_SSO_LOGIN)}",
            )

    # Validate admin-forticloud-sso-default-profile if present
    if "admin-forticloud-sso-default-profile" in payload:
        value = payload.get("admin-forticloud-sso-default-profile")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "admin-forticloud-sso-default-profile cannot exceed 35 characters",
            )

    # Validate admin-reset-button if present
    if "admin-reset-button" in payload:
        value = payload.get("admin-reset-button")
        if value and value not in VALID_BODY_ADMIN_RESET_BUTTON:
            return (
                False,
                f"Invalid admin-reset-button '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_RESET_BUTTON)}",
            )

    # Validate admin-server-cert if present
    if "admin-server-cert" in payload:
        value = payload.get("admin-server-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "admin-server-cert cannot exceed 35 characters")

    # Validate admin-https-pki-required if present
    if "admin-https-pki-required" in payload:
        value = payload.get("admin-https-pki-required")
        if value and value not in VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED:
            return (
                False,
                f"Invalid admin-https-pki-required '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_HTTPS_PKI_REQUIRED)}",
            )

    # Validate wifi-certificate if present
    if "wifi-certificate" in payload:
        value = payload.get("wifi-certificate")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "wifi-certificate cannot exceed 35 characters")

    # Validate dhcp-lease-backup-interval if present
    if "dhcp-lease-backup-interval" in payload:
        value = payload.get("dhcp-lease-backup-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (
                        False,
                        "dhcp-lease-backup-interval must be between 10 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dhcp-lease-backup-interval must be numeric, got: {value}",
                )

    # Validate wifi-ca-certificate if present
    if "wifi-ca-certificate" in payload:
        value = payload.get("wifi-ca-certificate")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "wifi-ca-certificate cannot exceed 79 characters")

    # Validate auth-http-port if present
    if "auth-http-port" in payload:
        value = payload.get("auth-http-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "auth-http-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"auth-http-port must be numeric, got: {value}")

    # Validate auth-https-port if present
    if "auth-https-port" in payload:
        value = payload.get("auth-https-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "auth-https-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-https-port must be numeric, got: {value}",
                )

    # Validate auth-ike-saml-port if present
    if "auth-ike-saml-port" in payload:
        value = payload.get("auth-ike-saml-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "auth-ike-saml-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-ike-saml-port must be numeric, got: {value}",
                )

    # Validate auth-keepalive if present
    if "auth-keepalive" in payload:
        value = payload.get("auth-keepalive")
        if value and value not in VALID_BODY_AUTH_KEEPALIVE:
            return (
                False,
                f"Invalid auth-keepalive '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_KEEPALIVE)}",
            )

    # Validate policy-auth-concurrent if present
    if "policy-auth-concurrent" in payload:
        value = payload.get("policy-auth-concurrent")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100:
                    return (
                        False,
                        "policy-auth-concurrent must be between 0 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"policy-auth-concurrent must be numeric, got: {value}",
                )

    # Validate auth-session-limit if present
    if "auth-session-limit" in payload:
        value = payload.get("auth-session-limit")
        if value and value not in VALID_BODY_AUTH_SESSION_LIMIT:
            return (
                False,
                f"Invalid auth-session-limit '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SESSION_LIMIT)}",
            )

    # Validate auth-cert if present
    if "auth-cert" in payload:
        value = payload.get("auth-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-cert cannot exceed 35 characters")

    # Validate clt-cert-req if present
    if "clt-cert-req" in payload:
        value = payload.get("clt-cert-req")
        if value and value not in VALID_BODY_CLT_CERT_REQ:
            return (
                False,
                f"Invalid clt-cert-req '{value}'. Must be one of: {', '.join(VALID_BODY_CLT_CERT_REQ)}",
            )

    # Validate fortiservice-port if present
    if "fortiservice-port" in payload:
        value = payload.get("fortiservice-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "fortiservice-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fortiservice-port must be numeric, got: {value}",
                )

    # Validate cfg-save if present
    if "cfg-save" in payload:
        value = payload.get("cfg-save")
        if value and value not in VALID_BODY_CFG_SAVE:
            return (
                False,
                f"Invalid cfg-save '{value}'. Must be one of: {', '.join(VALID_BODY_CFG_SAVE)}",
            )

    # Validate cfg-revert-timeout if present
    if "cfg-revert-timeout" in payload:
        value = payload.get("cfg-revert-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 4294967295:
                    return (
                        False,
                        "cfg-revert-timeout must be between 10 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cfg-revert-timeout must be numeric, got: {value}",
                )

    # Validate reboot-upon-config-restore if present
    if "reboot-upon-config-restore" in payload:
        value = payload.get("reboot-upon-config-restore")
        if value and value not in VALID_BODY_REBOOT_UPON_CONFIG_RESTORE:
            return (
                False,
                f"Invalid reboot-upon-config-restore '{value}'. Must be one of: {', '.join(VALID_BODY_REBOOT_UPON_CONFIG_RESTORE)}",
            )

    # Validate admin-scp if present
    if "admin-scp" in payload:
        value = payload.get("admin-scp")
        if value and value not in VALID_BODY_ADMIN_SCP:
            return (
                False,
                f"Invalid admin-scp '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_SCP)}",
            )

    # Validate wireless-controller if present
    if "wireless-controller" in payload:
        value = payload.get("wireless-controller")
        if value and value not in VALID_BODY_WIRELESS_CONTROLLER:
            return (
                False,
                f"Invalid wireless-controller '{value}'. Must be one of: {', '.join(VALID_BODY_WIRELESS_CONTROLLER)}",
            )

    # Validate wireless-controller-port if present
    if "wireless-controller-port" in payload:
        value = payload.get("wireless-controller-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1024 or int_val > 49150:
                    return (
                        False,
                        "wireless-controller-port must be between 1024 and 49150",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wireless-controller-port must be numeric, got: {value}",
                )

    # Validate fortiextender-data-port if present
    if "fortiextender-data-port" in payload:
        value = payload.get("fortiextender-data-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1024 or int_val > 49150:
                    return (
                        False,
                        "fortiextender-data-port must be between 1024 and 49150",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fortiextender-data-port must be numeric, got: {value}",
                )

    # Validate fortiextender if present
    if "fortiextender" in payload:
        value = payload.get("fortiextender")
        if value and value not in VALID_BODY_FORTIEXTENDER:
            return (
                False,
                f"Invalid fortiextender '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER)}",
            )

    # Validate fortiextender-discovery-lockdown if present
    if "fortiextender-discovery-lockdown" in payload:
        value = payload.get("fortiextender-discovery-lockdown")
        if value and value not in VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN:
            return (
                False,
                f"Invalid fortiextender-discovery-lockdown '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER_DISCOVERY_LOCKDOWN)}",
            )

    # Validate fortiextender-vlan-mode if present
    if "fortiextender-vlan-mode" in payload:
        value = payload.get("fortiextender-vlan-mode")
        if value and value not in VALID_BODY_FORTIEXTENDER_VLAN_MODE:
            return (
                False,
                f"Invalid fortiextender-vlan-mode '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER_VLAN_MODE)}",
            )

    # Validate fortiextender-provision-on-authorization if present
    if "fortiextender-provision-on-authorization" in payload:
        value = payload.get("fortiextender-provision-on-authorization")
        if (
            value
            and value
            not in VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION
        ):
            return (
                False,
                f"Invalid fortiextender-provision-on-authorization '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER_PROVISION_ON_AUTHORIZATION)}",
            )

    # Validate switch-controller if present
    if "switch-controller" in payload:
        value = payload.get("switch-controller")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER:
            return (
                False,
                f"Invalid switch-controller '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER)}",
            )

    # Validate dnsproxy-worker-count if present
    if "dnsproxy-worker-count" in payload:
        value = payload.get("dnsproxy-worker-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 8:
                    return (
                        False,
                        "dnsproxy-worker-count must be between 1 and 8",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dnsproxy-worker-count must be numeric, got: {value}",
                )

    # Validate url-filter-count if present
    if "url-filter-count" in payload:
        value = payload.get("url-filter-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1:
                    return (False, "url-filter-count must be between 1 and 1")
            except (ValueError, TypeError):
                return (
                    False,
                    f"url-filter-count must be numeric, got: {value}",
                )

    # Validate httpd-max-worker-count if present
    if "httpd-max-worker-count" in payload:
        value = payload.get("httpd-max-worker-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "httpd-max-worker-count must be between 0 and 128",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"httpd-max-worker-count must be numeric, got: {value}",
                )

    # Validate proxy-worker-count if present
    if "proxy-worker-count" in payload:
        value = payload.get("proxy-worker-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 8:
                    return (
                        False,
                        "proxy-worker-count must be between 1 and 8",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"proxy-worker-count must be numeric, got: {value}",
                )

    # Validate scanunit-count if present
    if "scanunit-count" in payload:
        value = payload.get("scanunit-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 8:
                    return (False, "scanunit-count must be between 1 and 8")
            except (ValueError, TypeError):
                return (False, f"scanunit-count must be numeric, got: {value}")

    # Validate proxy-hardware-acceleration if present
    if "proxy-hardware-acceleration" in payload:
        value = payload.get("proxy-hardware-acceleration")
        if value and value not in VALID_BODY_PROXY_HARDWARE_ACCELERATION:
            return (
                False,
                f"Invalid proxy-hardware-acceleration '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_HARDWARE_ACCELERATION)}",
            )

    # Validate fgd-alert-subscription if present
    if "fgd-alert-subscription" in payload:
        value = payload.get("fgd-alert-subscription")
        if value and value not in VALID_BODY_FGD_ALERT_SUBSCRIPTION:
            return (
                False,
                f"Invalid fgd-alert-subscription '{value}'. Must be one of: {', '.join(VALID_BODY_FGD_ALERT_SUBSCRIPTION)}",
            )

    # Validate ipsec-hmac-offload if present
    if "ipsec-hmac-offload" in payload:
        value = payload.get("ipsec-hmac-offload")
        if value and value not in VALID_BODY_IPSEC_HMAC_OFFLOAD:
            return (
                False,
                f"Invalid ipsec-hmac-offload '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_HMAC_OFFLOAD)}",
            )

    # Validate ipv6-accept-dad if present
    if "ipv6-accept-dad" in payload:
        value = payload.get("ipv6-accept-dad")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2:
                    return (False, "ipv6-accept-dad must be between 0 and 2")
            except (ValueError, TypeError):
                return (
                    False,
                    f"ipv6-accept-dad must be numeric, got: {value}",
                )

    # Validate ipv6-allow-anycast-probe if present
    if "ipv6-allow-anycast-probe" in payload:
        value = payload.get("ipv6-allow-anycast-probe")
        if value and value not in VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE:
            return (
                False,
                f"Invalid ipv6-allow-anycast-probe '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ALLOW_ANYCAST_PROBE)}",
            )

    # Validate ipv6-allow-multicast-probe if present
    if "ipv6-allow-multicast-probe" in payload:
        value = payload.get("ipv6-allow-multicast-probe")
        if value and value not in VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE:
            return (
                False,
                f"Invalid ipv6-allow-multicast-probe '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ALLOW_MULTICAST_PROBE)}",
            )

    # Validate ipv6-allow-local-in-silent-drop if present
    if "ipv6-allow-local-in-silent-drop" in payload:
        value = payload.get("ipv6-allow-local-in-silent-drop")
        if value and value not in VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP:
            return (
                False,
                f"Invalid ipv6-allow-local-in-silent-drop '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6_ALLOW_LOCAL_IN_SILENT_DROP)}",
            )

    # Validate csr-ca-attribute if present
    if "csr-ca-attribute" in payload:
        value = payload.get("csr-ca-attribute")
        if value and value not in VALID_BODY_CSR_CA_ATTRIBUTE:
            return (
                False,
                f"Invalid csr-ca-attribute '{value}'. Must be one of: {', '.join(VALID_BODY_CSR_CA_ATTRIBUTE)}",
            )

    # Validate wimax-4g-usb if present
    if "wimax-4g-usb" in payload:
        value = payload.get("wimax-4g-usb")
        if value and value not in VALID_BODY_WIMAX_4G_USB:
            return (
                False,
                f"Invalid wimax-4g-usb '{value}'. Must be one of: {', '.join(VALID_BODY_WIMAX_4G_USB)}",
            )

    # Validate cert-chain-max if present
    if "cert-chain-max" in payload:
        value = payload.get("cert-chain-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 2147483647:
                    return (
                        False,
                        "cert-chain-max must be between 1 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"cert-chain-max must be numeric, got: {value}")

    # Validate two-factor-ftk-expiry if present
    if "two-factor-ftk-expiry" in payload:
        value = payload.get("two-factor-ftk-expiry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 600:
                    return (
                        False,
                        "two-factor-ftk-expiry must be between 60 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"two-factor-ftk-expiry must be numeric, got: {value}",
                )

    # Validate two-factor-email-expiry if present
    if "two-factor-email-expiry" in payload:
        value = payload.get("two-factor-email-expiry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 300:
                    return (
                        False,
                        "two-factor-email-expiry must be between 30 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"two-factor-email-expiry must be numeric, got: {value}",
                )

    # Validate two-factor-sms-expiry if present
    if "two-factor-sms-expiry" in payload:
        value = payload.get("two-factor-sms-expiry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 300:
                    return (
                        False,
                        "two-factor-sms-expiry must be between 30 and 300",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"two-factor-sms-expiry must be numeric, got: {value}",
                )

    # Validate two-factor-fac-expiry if present
    if "two-factor-fac-expiry" in payload:
        value = payload.get("two-factor-fac-expiry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (
                        False,
                        "two-factor-fac-expiry must be between 10 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"two-factor-fac-expiry must be numeric, got: {value}",
                )

    # Validate two-factor-ftm-expiry if present
    if "two-factor-ftm-expiry" in payload:
        value = payload.get("two-factor-ftm-expiry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 168:
                    return (
                        False,
                        "two-factor-ftm-expiry must be between 1 and 168",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"two-factor-ftm-expiry must be numeric, got: {value}",
                )

    # Validate wad-worker-count if present
    if "wad-worker-count" in payload:
        value = payload.get("wad-worker-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2:
                    return (False, "wad-worker-count must be between 0 and 2")
            except (ValueError, TypeError):
                return (
                    False,
                    f"wad-worker-count must be numeric, got: {value}",
                )

    # Validate wad-worker-dev-cache if present
    if "wad-worker-dev-cache" in payload:
        value = payload.get("wad-worker-dev-cache")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 10240:
                    return (
                        False,
                        "wad-worker-dev-cache must be between 0 and 10240",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wad-worker-dev-cache must be numeric, got: {value}",
                )

    # Validate wad-csvc-cs-count if present
    if "wad-csvc-cs-count" in payload:
        value = payload.get("wad-csvc-cs-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1:
                    return (
                        False,
                        "wad-csvc-cs-count must be between 1 and 1",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wad-csvc-cs-count must be numeric, got: {value}",
                )

    # Validate wad-csvc-db-count if present
    if "wad-csvc-db-count" in payload:
        value = payload.get("wad-csvc-db-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 8:
                    return (
                        False,
                        "wad-csvc-db-count must be between 0 and 8",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wad-csvc-db-count must be numeric, got: {value}",
                )

    # Validate wad-source-affinity if present
    if "wad-source-affinity" in payload:
        value = payload.get("wad-source-affinity")
        if value and value not in VALID_BODY_WAD_SOURCE_AFFINITY:
            return (
                False,
                f"Invalid wad-source-affinity '{value}'. Must be one of: {', '.join(VALID_BODY_WAD_SOURCE_AFFINITY)}",
            )

    # Validate wad-memory-change-granularity if present
    if "wad-memory-change-granularity" in payload:
        value = payload.get("wad-memory-change-granularity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 25:
                    return (
                        False,
                        "wad-memory-change-granularity must be between 5 and 25",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wad-memory-change-granularity must be numeric, got: {value}",
                )

    # Validate login-timestamp if present
    if "login-timestamp" in payload:
        value = payload.get("login-timestamp")
        if value and value not in VALID_BODY_LOGIN_TIMESTAMP:
            return (
                False,
                f"Invalid login-timestamp '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_TIMESTAMP)}",
            )

    # Validate ip-conflict-detection if present
    if "ip-conflict-detection" in payload:
        value = payload.get("ip-conflict-detection")
        if value and value not in VALID_BODY_IP_CONFLICT_DETECTION:
            return (
                False,
                f"Invalid ip-conflict-detection '{value}'. Must be one of: {', '.join(VALID_BODY_IP_CONFLICT_DETECTION)}",
            )

    # Validate miglogd-children if present
    if "miglogd-children" in payload:
        value = payload.get("miglogd-children")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 15:
                    return (
                        False,
                        "miglogd-children must be between 0 and 15",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"miglogd-children must be numeric, got: {value}",
                )

    # Validate log-daemon-cpu-threshold if present
    if "log-daemon-cpu-threshold" in payload:
        value = payload.get("log-daemon-cpu-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 99:
                    return (
                        False,
                        "log-daemon-cpu-threshold must be between 0 and 99",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"log-daemon-cpu-threshold must be numeric, got: {value}",
                )

    # Validate special-file-23-support if present
    if "special-file-23-support" in payload:
        value = payload.get("special-file-23-support")
        if value and value not in VALID_BODY_SPECIAL_FILE_23_SUPPORT:
            return (
                False,
                f"Invalid special-file-23-support '{value}'. Must be one of: {', '.join(VALID_BODY_SPECIAL_FILE_23_SUPPORT)}",
            )

    # Validate log-uuid-address if present
    if "log-uuid-address" in payload:
        value = payload.get("log-uuid-address")
        if value and value not in VALID_BODY_LOG_UUID_ADDRESS:
            return (
                False,
                f"Invalid log-uuid-address '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_UUID_ADDRESS)}",
            )

    # Validate log-ssl-connection if present
    if "log-ssl-connection" in payload:
        value = payload.get("log-ssl-connection")
        if value and value not in VALID_BODY_LOG_SSL_CONNECTION:
            return (
                False,
                f"Invalid log-ssl-connection '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_SSL_CONNECTION)}",
            )

    # Validate rest-api-key-url-query if present
    if "rest-api-key-url-query" in payload:
        value = payload.get("rest-api-key-url-query")
        if value and value not in VALID_BODY_REST_API_KEY_URL_QUERY:
            return (
                False,
                f"Invalid rest-api-key-url-query '{value}'. Must be one of: {', '.join(VALID_BODY_REST_API_KEY_URL_QUERY)}",
            )

    # Validate gui-cdn-domain-override if present
    if "gui-cdn-domain-override" in payload:
        value = payload.get("gui-cdn-domain-override")
        if value and isinstance(value, str) and len(value) > 255:
            return (
                False,
                "gui-cdn-domain-override cannot exceed 255 characters",
            )

    # Validate arp-max-entry if present
    if "arp-max-entry" in payload:
        value = payload.get("arp-max-entry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 131072 or int_val > 2147483647:
                    return (
                        False,
                        "arp-max-entry must be between 131072 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"arp-max-entry must be numeric, got: {value}")

    # Validate ha-affinity if present
    if "ha-affinity" in payload:
        value = payload.get("ha-affinity")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ha-affinity cannot exceed 79 characters")

    # Validate bfd-affinity if present
    if "bfd-affinity" in payload:
        value = payload.get("bfd-affinity")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "bfd-affinity cannot exceed 79 characters")

    # Validate cmdbsvr-affinity if present
    if "cmdbsvr-affinity" in payload:
        value = payload.get("cmdbsvr-affinity")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "cmdbsvr-affinity cannot exceed 79 characters")

    # Validate ndp-max-entry if present
    if "ndp-max-entry" in payload:
        value = payload.get("ndp-max-entry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 65536 or int_val > 2147483647:
                    return (
                        False,
                        "ndp-max-entry must be between 65536 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (False, f"ndp-max-entry must be numeric, got: {value}")

    # Validate br-fdb-max-entry if present
    if "br-fdb-max-entry" in payload:
        value = payload.get("br-fdb-max-entry")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 8192 or int_val > 2147483647:
                    return (
                        False,
                        "br-fdb-max-entry must be between 8192 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"br-fdb-max-entry must be numeric, got: {value}",
                )

    # Validate max-route-cache-size if present
    if "max-route-cache-size" in payload:
        value = payload.get("max-route-cache-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "max-route-cache-size must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-route-cache-size must be numeric, got: {value}",
                )

    # Validate ipsec-asic-offload if present
    if "ipsec-asic-offload" in payload:
        value = payload.get("ipsec-asic-offload")
        if value and value not in VALID_BODY_IPSEC_ASIC_OFFLOAD:
            return (
                False,
                f"Invalid ipsec-asic-offload '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_ASIC_OFFLOAD)}",
            )

    # Validate device-idle-timeout if present
    if "device-idle-timeout" in payload:
        value = payload.get("device-idle-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 31536000:
                    return (
                        False,
                        "device-idle-timeout must be between 30 and 31536000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"device-idle-timeout must be numeric, got: {value}",
                )

    # Validate user-device-store-max-devices if present
    if "user-device-store-max-devices" in payload:
        value = payload.get("user-device-store-max-devices")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10135 or int_val > 28959:
                    return (
                        False,
                        "user-device-store-max-devices must be between 10135 and 28959",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"user-device-store-max-devices must be numeric, got: {value}",
                )

    # Validate user-device-store-max-device-mem if present
    if "user-device-store-max-device-mem" in payload:
        value = payload.get("user-device-store-max-device-mem")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 5:
                    return (
                        False,
                        "user-device-store-max-device-mem must be between 1 and 5",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"user-device-store-max-device-mem must be numeric, got: {value}",
                )

    # Validate user-device-store-max-users if present
    if "user-device-store-max-users" in payload:
        value = payload.get("user-device-store-max-users")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10135 or int_val > 28959:
                    return (
                        False,
                        "user-device-store-max-users must be between 10135 and 28959",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"user-device-store-max-users must be numeric, got: {value}",
                )

    # Validate user-device-store-max-unified-mem if present
    if "user-device-store-max-unified-mem" in payload:
        value = payload.get("user-device-store-max-unified-mem")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 20271513 or int_val > 202715136:
                    return (
                        False,
                        "user-device-store-max-unified-mem must be between 20271513 and 202715136",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"user-device-store-max-unified-mem must be numeric, got: {value}",
                )

    # Validate gui-device-latitude if present
    if "gui-device-latitude" in payload:
        value = payload.get("gui-device-latitude")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "gui-device-latitude cannot exceed 19 characters")

    # Validate gui-device-longitude if present
    if "gui-device-longitude" in payload:
        value = payload.get("gui-device-longitude")
        if value and isinstance(value, str) and len(value) > 19:
            return (False, "gui-device-longitude cannot exceed 19 characters")

    # Validate private-data-encryption if present
    if "private-data-encryption" in payload:
        value = payload.get("private-data-encryption")
        if value and value not in VALID_BODY_PRIVATE_DATA_ENCRYPTION:
            return (
                False,
                f"Invalid private-data-encryption '{value}'. Must be one of: {', '.join(VALID_BODY_PRIVATE_DATA_ENCRYPTION)}",
            )

    # Validate auto-auth-extension-device if present
    if "auto-auth-extension-device" in payload:
        value = payload.get("auto-auth-extension-device")
        if value and value not in VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE:
            return (
                False,
                f"Invalid auto-auth-extension-device '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_AUTH_EXTENSION_DEVICE)}",
            )

    # Validate gui-theme if present
    if "gui-theme" in payload:
        value = payload.get("gui-theme")
        if value and value not in VALID_BODY_GUI_THEME:
            return (
                False,
                f"Invalid gui-theme '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_THEME)}",
            )

    # Validate gui-date-format if present
    if "gui-date-format" in payload:
        value = payload.get("gui-date-format")
        if value and value not in VALID_BODY_GUI_DATE_FORMAT:
            return (
                False,
                f"Invalid gui-date-format '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DATE_FORMAT)}",
            )

    # Validate gui-date-time-source if present
    if "gui-date-time-source" in payload:
        value = payload.get("gui-date-time-source")
        if value and value not in VALID_BODY_GUI_DATE_TIME_SOURCE:
            return (
                False,
                f"Invalid gui-date-time-source '{value}'. Must be one of: {', '.join(VALID_BODY_GUI_DATE_TIME_SOURCE)}",
            )

    # Validate igmp-state-limit if present
    if "igmp-state-limit" in payload:
        value = payload.get("igmp-state-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 96 or int_val > 128000:
                    return (
                        False,
                        "igmp-state-limit must be between 96 and 128000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"igmp-state-limit must be numeric, got: {value}",
                )

    # Validate cloud-communication if present
    if "cloud-communication" in payload:
        value = payload.get("cloud-communication")
        if value and value not in VALID_BODY_CLOUD_COMMUNICATION:
            return (
                False,
                f"Invalid cloud-communication '{value}'. Must be one of: {', '.join(VALID_BODY_CLOUD_COMMUNICATION)}",
            )

    # Validate ipsec-ha-seqjump-rate if present
    if "ipsec-ha-seqjump-rate" in payload:
        value = payload.get("ipsec-ha-seqjump-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10:
                    return (
                        False,
                        "ipsec-ha-seqjump-rate must be between 1 and 10",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ipsec-ha-seqjump-rate must be numeric, got: {value}",
                )

    # Validate fortitoken-cloud if present
    if "fortitoken-cloud" in payload:
        value = payload.get("fortitoken-cloud")
        if value and value not in VALID_BODY_FORTITOKEN_CLOUD:
            return (
                False,
                f"Invalid fortitoken-cloud '{value}'. Must be one of: {', '.join(VALID_BODY_FORTITOKEN_CLOUD)}",
            )

    # Validate fortitoken-cloud-push-status if present
    if "fortitoken-cloud-push-status" in payload:
        value = payload.get("fortitoken-cloud-push-status")
        if value and value not in VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS:
            return (
                False,
                f"Invalid fortitoken-cloud-push-status '{value}'. Must be one of: {', '.join(VALID_BODY_FORTITOKEN_CLOUD_PUSH_STATUS)}",
            )

    # Validate fortitoken-cloud-region if present
    if "fortitoken-cloud-region" in payload:
        value = payload.get("fortitoken-cloud-region")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "fortitoken-cloud-region cannot exceed 63 characters",
            )

    # Validate fortitoken-cloud-sync-interval if present
    if "fortitoken-cloud-sync-interval" in payload:
        value = payload.get("fortitoken-cloud-sync-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 336:
                    return (
                        False,
                        "fortitoken-cloud-sync-interval must be between 0 and 336",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fortitoken-cloud-sync-interval must be numeric, got: {value}",
                )

    # Validate irq-time-accounting if present
    if "irq-time-accounting" in payload:
        value = payload.get("irq-time-accounting")
        if value and value not in VALID_BODY_IRQ_TIME_ACCOUNTING:
            return (
                False,
                f"Invalid irq-time-accounting '{value}'. Must be one of: {', '.join(VALID_BODY_IRQ_TIME_ACCOUNTING)}",
            )

    # Validate management-ip if present
    if "management-ip" in payload:
        value = payload.get("management-ip")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "management-ip cannot exceed 255 characters")

    # Validate management-port if present
    if "management-port" in payload:
        value = payload.get("management-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "management-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"management-port must be numeric, got: {value}",
                )

    # Validate management-port-use-admin-sport if present
    if "management-port-use-admin-sport" in payload:
        value = payload.get("management-port-use-admin-sport")
        if value and value not in VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT:
            return (
                False,
                f"Invalid management-port-use-admin-sport '{value}'. Must be one of: {', '.join(VALID_BODY_MANAGEMENT_PORT_USE_ADMIN_SPORT)}",
            )

    # Validate forticonverter-integration if present
    if "forticonverter-integration" in payload:
        value = payload.get("forticonverter-integration")
        if value and value not in VALID_BODY_FORTICONVERTER_INTEGRATION:
            return (
                False,
                f"Invalid forticonverter-integration '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICONVERTER_INTEGRATION)}",
            )

    # Validate forticonverter-config-upload if present
    if "forticonverter-config-upload" in payload:
        value = payload.get("forticonverter-config-upload")
        if value and value not in VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD:
            return (
                False,
                f"Invalid forticonverter-config-upload '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICONVERTER_CONFIG_UPLOAD)}",
            )

    # Validate internet-service-database if present
    if "internet-service-database" in payload:
        value = payload.get("internet-service-database")
        if value and value not in VALID_BODY_INTERNET_SERVICE_DATABASE:
            return (
                False,
                f"Invalid internet-service-database '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_DATABASE)}",
            )

    # Validate geoip-full-db if present
    if "geoip-full-db" in payload:
        value = payload.get("geoip-full-db")
        if value and value not in VALID_BODY_GEOIP_FULL_DB:
            return (
                False,
                f"Invalid geoip-full-db '{value}'. Must be one of: {', '.join(VALID_BODY_GEOIP_FULL_DB)}",
            )

    # Validate early-tcp-npu-session if present
    if "early-tcp-npu-session" in payload:
        value = payload.get("early-tcp-npu-session")
        if value and value not in VALID_BODY_EARLY_TCP_NPU_SESSION:
            return (
                False,
                f"Invalid early-tcp-npu-session '{value}'. Must be one of: {', '.join(VALID_BODY_EARLY_TCP_NPU_SESSION)}",
            )

    # Validate npu-neighbor-update if present
    if "npu-neighbor-update" in payload:
        value = payload.get("npu-neighbor-update")
        if value and value not in VALID_BODY_NPU_NEIGHBOR_UPDATE:
            return (
                False,
                f"Invalid npu-neighbor-update '{value}'. Must be one of: {', '.join(VALID_BODY_NPU_NEIGHBOR_UPDATE)}",
            )

    # Validate delay-tcp-npu-session if present
    if "delay-tcp-npu-session" in payload:
        value = payload.get("delay-tcp-npu-session")
        if value and value not in VALID_BODY_DELAY_TCP_NPU_SESSION:
            return (
                False,
                f"Invalid delay-tcp-npu-session '{value}'. Must be one of: {', '.join(VALID_BODY_DELAY_TCP_NPU_SESSION)}",
            )

    # Validate interface-subnet-usage if present
    if "interface-subnet-usage" in payload:
        value = payload.get("interface-subnet-usage")
        if value and value not in VALID_BODY_INTERFACE_SUBNET_USAGE:
            return (
                False,
                f"Invalid interface-subnet-usage '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SUBNET_USAGE)}",
            )

    # Validate sflowd-max-children-num if present
    if "sflowd-max-children-num" in payload:
        value = payload.get("sflowd-max-children-num")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 6:
                    return (
                        False,
                        "sflowd-max-children-num must be between 0 and 6",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sflowd-max-children-num must be numeric, got: {value}",
                )

    # Validate fortigslb-integration if present
    if "fortigslb-integration" in payload:
        value = payload.get("fortigslb-integration")
        if value and value not in VALID_BODY_FORTIGSLB_INTEGRATION:
            return (
                False,
                f"Invalid fortigslb-integration '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIGSLB_INTEGRATION)}",
            )

    # Validate user-history-password-threshold if present
    if "user-history-password-threshold" in payload:
        value = payload.get("user-history-password-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 15:
                    return (
                        False,
                        "user-history-password-threshold must be between 3 and 15",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"user-history-password-threshold must be numeric, got: {value}",
                )

    # Validate auth-session-auto-backup if present
    if "auth-session-auto-backup" in payload:
        value = payload.get("auth-session-auto-backup")
        if value and value not in VALID_BODY_AUTH_SESSION_AUTO_BACKUP:
            return (
                False,
                f"Invalid auth-session-auto-backup '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SESSION_AUTO_BACKUP)}",
            )

    # Validate auth-session-auto-backup-interval if present
    if "auth-session-auto-backup-interval" in payload:
        value = payload.get("auth-session-auto-backup-interval")
        if value and value not in VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL:
            return (
                False,
                f"Invalid auth-session-auto-backup-interval '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SESSION_AUTO_BACKUP_INTERVAL)}",
            )

    # Validate scim-https-port if present
    if "scim-https-port" in payload:
        value = payload.get("scim-https-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "scim-https-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"scim-https-port must be numeric, got: {value}",
                )

    # Validate scim-http-port if present
    if "scim-http-port" in payload:
        value = payload.get("scim-http-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "scim-http-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"scim-http-port must be numeric, got: {value}")

    # Validate scim-server-cert if present
    if "scim-server-cert" in payload:
        value = payload.get("scim-server-cert")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "scim-server-cert cannot exceed 35 characters")

    # Validate application-bandwidth-tracking if present
    if "application-bandwidth-tracking" in payload:
        value = payload.get("application-bandwidth-tracking")
        if value and value not in VALID_BODY_APPLICATION_BANDWIDTH_TRACKING:
            return (
                False,
                f"Invalid application-bandwidth-tracking '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_BANDWIDTH_TRACKING)}",
            )

    # Validate tls-session-cache if present
    if "tls-session-cache" in payload:
        value = payload.get("tls-session-cache")
        if value and value not in VALID_BODY_TLS_SESSION_CACHE:
            return (
                False,
                f"Invalid tls-session-cache '{value}'. Must be one of: {', '.join(VALID_BODY_TLS_SESSION_CACHE)}",
            )

    return (True, None)
