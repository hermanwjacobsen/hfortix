"""
Validation helpers for system fortiguard endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FORTIGUARD_ANYCAST = ["enable", "disable"]
VALID_BODY_FORTIGUARD_ANYCAST_SOURCE = ["fortinet", "aws", "debug"]
VALID_BODY_PROTOCOL = ["udp", "http", "https"]
VALID_BODY_PORT = ["8888", "53", "80", "443"]
VALID_BODY_AUTO_JOIN_FORTICLOUD = ["enable", "disable"]
VALID_BODY_UPDATE_SERVER_LOCATION = ["automatic", "usa", "eu"]
VALID_BODY_UPDATE_FFDB = ["enable", "disable"]
VALID_BODY_UPDATE_UWDB = ["enable", "disable"]
VALID_BODY_UPDATE_DLDB = ["enable", "disable"]
VALID_BODY_UPDATE_EXTDB = ["enable", "disable"]
VALID_BODY_UPDATE_BUILD_PROXY = ["enable", "disable"]
VALID_BODY_PERSISTENT_CONNECTION = ["enable", "disable"]
VALID_BODY_AUTO_FIRMWARE_UPGRADE = ["enable", "disable"]
VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION = ["enable", "disable"]
VALID_BODY_ANTISPAM_FORCE_OFF = ["enable", "disable"]
VALID_BODY_ANTISPAM_CACHE = ["enable", "disable"]
VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF = ["enable", "disable"]
VALID_BODY_OUTBREAK_PREVENTION_CACHE = ["enable", "disable"]
VALID_BODY_WEBFILTER_FORCE_OFF = ["enable", "disable"]
VALID_BODY_WEBFILTER_CACHE = ["enable", "disable"]
VALID_BODY_SDNS_OPTIONS = ["include-question-section"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortiguard_get(
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


def validate_fortiguard_put(
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

    # Validate fortiguard-anycast if present
    if "fortiguard-anycast" in payload:
        value = payload.get("fortiguard-anycast")
        if value and value not in VALID_BODY_FORTIGUARD_ANYCAST:
            return (
                False,
                f"Invalid fortiguard-anycast '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIGUARD_ANYCAST)}",
            )

    # Validate fortiguard-anycast-source if present
    if "fortiguard-anycast-source" in payload:
        value = payload.get("fortiguard-anycast-source")
        if value and value not in VALID_BODY_FORTIGUARD_ANYCAST_SOURCE:
            return (
                False,
                f"Invalid fortiguard-anycast-source '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIGUARD_ANYCAST_SOURCE)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value and value not in VALID_BODY_PORT:
            return (
                False,
                f"Invalid port '{value}'. Must be one of: {', '.join(VALID_BODY_PORT)}",
            )

    # Validate service-account-id if present
    if "service-account-id" in payload:
        value = payload.get("service-account-id")
        if value and isinstance(value, str) and len(value) > 50:
            return (False, "service-account-id cannot exceed 50 characters")

    # Validate load-balance-servers if present
    if "load-balance-servers" in payload:
        value = payload.get("load-balance-servers")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 266:
                    return (
                        False,
                        "load-balance-servers must be between 1 and 266",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"load-balance-servers must be numeric, got: {value}",
                )

    # Validate auto-join-forticloud if present
    if "auto-join-forticloud" in payload:
        value = payload.get("auto-join-forticloud")
        if value and value not in VALID_BODY_AUTO_JOIN_FORTICLOUD:
            return (
                False,
                f"Invalid auto-join-forticloud '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_JOIN_FORTICLOUD)}",
            )

    # Validate update-server-location if present
    if "update-server-location" in payload:
        value = payload.get("update-server-location")
        if value and value not in VALID_BODY_UPDATE_SERVER_LOCATION:
            return (
                False,
                f"Invalid update-server-location '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_SERVER_LOCATION)}",
            )

    # Validate sandbox-region if present
    if "sandbox-region" in payload:
        value = payload.get("sandbox-region")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "sandbox-region cannot exceed 63 characters")

    # Validate update-ffdb if present
    if "update-ffdb" in payload:
        value = payload.get("update-ffdb")
        if value and value not in VALID_BODY_UPDATE_FFDB:
            return (
                False,
                f"Invalid update-ffdb '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_FFDB)}",
            )

    # Validate update-uwdb if present
    if "update-uwdb" in payload:
        value = payload.get("update-uwdb")
        if value and value not in VALID_BODY_UPDATE_UWDB:
            return (
                False,
                f"Invalid update-uwdb '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_UWDB)}",
            )

    # Validate update-dldb if present
    if "update-dldb" in payload:
        value = payload.get("update-dldb")
        if value and value not in VALID_BODY_UPDATE_DLDB:
            return (
                False,
                f"Invalid update-dldb '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_DLDB)}",
            )

    # Validate update-extdb if present
    if "update-extdb" in payload:
        value = payload.get("update-extdb")
        if value and value not in VALID_BODY_UPDATE_EXTDB:
            return (
                False,
                f"Invalid update-extdb '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_EXTDB)}",
            )

    # Validate update-build-proxy if present
    if "update-build-proxy" in payload:
        value = payload.get("update-build-proxy")
        if value and value not in VALID_BODY_UPDATE_BUILD_PROXY:
            return (
                False,
                f"Invalid update-build-proxy '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_BUILD_PROXY)}",
            )

    # Validate persistent-connection if present
    if "persistent-connection" in payload:
        value = payload.get("persistent-connection")
        if value and value not in VALID_BODY_PERSISTENT_CONNECTION:
            return (
                False,
                f"Invalid persistent-connection '{value}'. Must be one of: {', '.join(VALID_BODY_PERSISTENT_CONNECTION)}",
            )

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate auto-firmware-upgrade if present
    if "auto-firmware-upgrade" in payload:
        value = payload.get("auto-firmware-upgrade")
        if value and value not in VALID_BODY_AUTO_FIRMWARE_UPGRADE:
            return (
                False,
                f"Invalid auto-firmware-upgrade '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_FIRMWARE_UPGRADE)}",
            )

    # Validate auto-firmware-upgrade-day if present
    if "auto-firmware-upgrade-day" in payload:
        value = payload.get("auto-firmware-upgrade-day")
        if value and value not in VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY:
            return (
                False,
                f"Invalid auto-firmware-upgrade-day '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_FIRMWARE_UPGRADE_DAY)}",
            )

    # Validate auto-firmware-upgrade-delay if present
    if "auto-firmware-upgrade-delay" in payload:
        value = payload.get("auto-firmware-upgrade-delay")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 14:
                    return (
                        False,
                        "auto-firmware-upgrade-delay must be between 0 and 14",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-firmware-upgrade-delay must be numeric, got: {value}",
                )

    # Validate auto-firmware-upgrade-start-hour if present
    if "auto-firmware-upgrade-start-hour" in payload:
        value = payload.get("auto-firmware-upgrade-start-hour")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 23:
                    return (
                        False,
                        "auto-firmware-upgrade-start-hour must be between 0 and 23",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-firmware-upgrade-start-hour must be numeric, got: {value}",
                )

    # Validate auto-firmware-upgrade-end-hour if present
    if "auto-firmware-upgrade-end-hour" in payload:
        value = payload.get("auto-firmware-upgrade-end-hour")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 23:
                    return (
                        False,
                        "auto-firmware-upgrade-end-hour must be between 0 and 23",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-firmware-upgrade-end-hour must be numeric, got: {value}",
                )

    # Validate FDS-license-expiring-days if present
    if "FDS-license-expiring-days" in payload:
        value = payload.get("FDS-license-expiring-days")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "FDS-license-expiring-days must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"FDS-license-expiring-days must be numeric, got: {value}",
                )

    # Validate subscribe-update-notification if present
    if "subscribe-update-notification" in payload:
        value = payload.get("subscribe-update-notification")
        if value and value not in VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION:
            return (
                False,
                f"Invalid subscribe-update-notification '{value}'. Must be one of: {', '.join(VALID_BODY_SUBSCRIBE_UPDATE_NOTIFICATION)}",
            )

    # Validate antispam-force-off if present
    if "antispam-force-of" in payload:
        value = payload.get("antispam-force-of")
        if value and value not in VALID_BODY_ANTISPAM_FORCE_OFF:
            return (
                False,
                f"Invalid antispam-force-off '{value}'. Must be one of: {', '.join(VALID_BODY_ANTISPAM_FORCE_OFF)}",
            )

    # Validate antispam-cache if present
    if "antispam-cache" in payload:
        value = payload.get("antispam-cache")
        if value and value not in VALID_BODY_ANTISPAM_CACHE:
            return (
                False,
                f"Invalid antispam-cache '{value}'. Must be one of: {', '.join(VALID_BODY_ANTISPAM_CACHE)}",
            )

    # Validate antispam-cache-ttl if present
    if "antispam-cache-ttl" in payload:
        value = payload.get("antispam-cache-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 86400:
                    return (
                        False,
                        "antispam-cache-ttl must be between 300 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"antispam-cache-ttl must be numeric, got: {value}",
                )

    # Validate antispam-cache-mpermille if present
    if "antispam-cache-mpermille" in payload:
        value = payload.get("antispam-cache-mpermille")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 150:
                    return (
                        False,
                        "antispam-cache-mpermille must be between 1 and 150",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"antispam-cache-mpermille must be numeric, got: {value}",
                )

    # Validate antispam-license if present
    if "antispam-license" in payload:
        value = payload.get("antispam-license")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "antispam-license must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"antispam-license must be numeric, got: {value}",
                )

    # Validate antispam-expiration if present
    if "antispam-expiration" in payload:
        value = payload.get("antispam-expiration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "antispam-expiration must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"antispam-expiration must be numeric, got: {value}",
                )

    # Validate antispam-timeout if present
    if "antispam-timeout" in payload:
        value = payload.get("antispam-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "antispam-timeout must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"antispam-timeout must be numeric, got: {value}",
                )

    # Validate outbreak-prevention-force-off if present
    if "outbreak-prevention-force-of" in payload:
        value = payload.get("outbreak-prevention-force-of")
        if value and value not in VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF:
            return (
                False,
                f"Invalid outbreak-prevention-force-off '{value}'. Must be one of: {', '.join(VALID_BODY_OUTBREAK_PREVENTION_FORCE_OFF)}",
            )

    # Validate outbreak-prevention-cache if present
    if "outbreak-prevention-cache" in payload:
        value = payload.get("outbreak-prevention-cache")
        if value and value not in VALID_BODY_OUTBREAK_PREVENTION_CACHE:
            return (
                False,
                f"Invalid outbreak-prevention-cache '{value}'. Must be one of: {', '.join(VALID_BODY_OUTBREAK_PREVENTION_CACHE)}",
            )

    # Validate outbreak-prevention-cache-ttl if present
    if "outbreak-prevention-cache-ttl" in payload:
        value = payload.get("outbreak-prevention-cache-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 86400:
                    return (
                        False,
                        "outbreak-prevention-cache-ttl must be between 300 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"outbreak-prevention-cache-ttl must be numeric, got: {value}",
                )

    # Validate outbreak-prevention-cache-mpermille if present
    if "outbreak-prevention-cache-mpermille" in payload:
        value = payload.get("outbreak-prevention-cache-mpermille")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 150:
                    return (
                        False,
                        "outbreak-prevention-cache-mpermille must be between 1 and 150",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"outbreak-prevention-cache-mpermille must be numeric, got: {value}",
                )

    # Validate outbreak-prevention-license if present
    if "outbreak-prevention-license" in payload:
        value = payload.get("outbreak-prevention-license")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "outbreak-prevention-license must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"outbreak-prevention-license must be numeric, got: {value}",
                )

    # Validate outbreak-prevention-expiration if present
    if "outbreak-prevention-expiration" in payload:
        value = payload.get("outbreak-prevention-expiration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "outbreak-prevention-expiration must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"outbreak-prevention-expiration must be numeric, got: {value}",
                )

    # Validate outbreak-prevention-timeout if present
    if "outbreak-prevention-timeout" in payload:
        value = payload.get("outbreak-prevention-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "outbreak-prevention-timeout must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"outbreak-prevention-timeout must be numeric, got: {value}",
                )

    # Validate webfilter-force-off if present
    if "webfilter-force-of" in payload:
        value = payload.get("webfilter-force-of")
        if value and value not in VALID_BODY_WEBFILTER_FORCE_OFF:
            return (
                False,
                f"Invalid webfilter-force-off '{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_FORCE_OFF)}",
            )

    # Validate webfilter-cache if present
    if "webfilter-cache" in payload:
        value = payload.get("webfilter-cache")
        if value and value not in VALID_BODY_WEBFILTER_CACHE:
            return (
                False,
                f"Invalid webfilter-cache '{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_CACHE)}",
            )

    # Validate webfilter-cache-ttl if present
    if "webfilter-cache-ttl" in payload:
        value = payload.get("webfilter-cache-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 86400:
                    return (
                        False,
                        "webfilter-cache-ttl must be between 300 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"webfilter-cache-ttl must be numeric, got: {value}",
                )

    # Validate webfilter-license if present
    if "webfilter-license" in payload:
        value = payload.get("webfilter-license")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "webfilter-license must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"webfilter-license must be numeric, got: {value}",
                )

    # Validate webfilter-expiration if present
    if "webfilter-expiration" in payload:
        value = payload.get("webfilter-expiration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "webfilter-expiration must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"webfilter-expiration must be numeric, got: {value}",
                )

    # Validate webfilter-timeout if present
    if "webfilter-timeout" in payload:
        value = payload.get("webfilter-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "webfilter-timeout must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"webfilter-timeout must be numeric, got: {value}",
                )

    # Validate sdns-server-port if present
    if "sdns-server-port" in payload:
        value = payload.get("sdns-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "sdns-server-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"sdns-server-port must be numeric, got: {value}",
                )

    # Validate anycast-sdns-server-port if present
    if "anycast-sdns-server-port" in payload:
        value = payload.get("anycast-sdns-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "anycast-sdns-server-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"anycast-sdns-server-port must be numeric, got: {value}",
                )

    # Validate sdns-options if present
    if "sdns-options" in payload:
        value = payload.get("sdns-options")
        if value and value not in VALID_BODY_SDNS_OPTIONS:
            return (
                False,
                f"Invalid sdns-options '{value}'. Must be one of: {', '.join(VALID_BODY_SDNS_OPTIONS)}",
            )

    # Validate proxy-server-ip if present
    if "proxy-server-ip" in payload:
        value = payload.get("proxy-server-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "proxy-server-ip cannot exceed 63 characters")

    # Validate proxy-server-port if present
    if "proxy-server-port" in payload:
        value = payload.get("proxy-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "proxy-server-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"proxy-server-port must be numeric, got: {value}",
                )

    # Validate proxy-username if present
    if "proxy-username" in payload:
        value = payload.get("proxy-username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "proxy-username cannot exceed 64 characters")

    # Validate ddns-server-port if present
    if "ddns-server-port" in payload:
        value = payload.get("ddns-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "ddns-server-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ddns-server-port must be numeric, got: {value}",
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
