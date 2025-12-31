"""
Validation helpers for wireless-controller wids_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SENSOR_MODE = ["disable", "foreign", "both"]
VALID_BODY_AP_SCAN = ["disable", "enable"]
VALID_BODY_AP_SCAN_PASSIVE = ["enable", "disable"]
VALID_BODY_AP_AUTO_SUPPRESS = ["enable", "disable"]
VALID_BODY_WIRELESS_BRIDGE = ["enable", "disable"]
VALID_BODY_DEAUTH_BROADCAST = ["enable", "disable"]
VALID_BODY_NULL_SSID_PROBE_RESP = ["enable", "disable"]
VALID_BODY_LONG_DURATION_ATTACK = ["enable", "disable"]
VALID_BODY_INVALID_MAC_OUI = ["enable", "disable"]
VALID_BODY_WEAK_WEP_IV = ["enable", "disable"]
VALID_BODY_AUTH_FRAME_FLOOD = ["enable", "disable"]
VALID_BODY_ASSOC_FRAME_FLOOD = ["enable", "disable"]
VALID_BODY_REASSOC_FLOOD = ["enable", "disable"]
VALID_BODY_PROBE_FLOOD = ["enable", "disable"]
VALID_BODY_BCN_FLOOD = ["enable", "disable"]
VALID_BODY_RTS_FLOOD = ["enable", "disable"]
VALID_BODY_CTS_FLOOD = ["enable", "disable"]
VALID_BODY_CLIENT_FLOOD = ["enable", "disable"]
VALID_BODY_BLOCK_ACK_FLOOD = ["enable", "disable"]
VALID_BODY_PSPOLL_FLOOD = ["enable", "disable"]
VALID_BODY_NETSTUMBLER = ["enable", "disable"]
VALID_BODY_WELLENREITER = ["enable", "disable"]
VALID_BODY_SPOOFED_DEAUTH = ["enable", "disable"]
VALID_BODY_ASLEAP_ATTACK = ["enable", "disable"]
VALID_BODY_EAPOL_START_FLOOD = ["enable", "disable"]
VALID_BODY_EAPOL_LOGOFF_FLOOD = ["enable", "disable"]
VALID_BODY_EAPOL_SUCC_FLOOD = ["enable", "disable"]
VALID_BODY_EAPOL_FAIL_FLOOD = ["enable", "disable"]
VALID_BODY_EAPOL_PRE_SUCC_FLOOD = ["enable", "disable"]
VALID_BODY_EAPOL_PRE_FAIL_FLOOD = ["enable", "disable"]
VALID_BODY_WINDOWS_BRIDGE = ["enable", "disable"]
VALID_BODY_DISASSOC_BROADCAST = ["enable", "disable"]
VALID_BODY_AP_SPOOFING = ["enable", "disable"]
VALID_BODY_CHAN_BASED_MITM = ["enable", "disable"]
VALID_BODY_ADHOC_VALID_SSID = ["enable", "disable"]
VALID_BODY_ADHOC_NETWORK = ["enable", "disable"]
VALID_BODY_EAPOL_KEY_OVERFLOW = ["enable", "disable"]
VALID_BODY_AP_IMPERSONATION = ["enable", "disable"]
VALID_BODY_INVALID_ADDR_COMBINATION = ["enable", "disable"]
VALID_BODY_BEACON_WRONG_CHANNEL = ["enable", "disable"]
VALID_BODY_HT_GREENFIELD = ["enable", "disable"]
VALID_BODY_OVERFLOW_IE = ["enable", "disable"]
VALID_BODY_MALFORMED_HT_IE = ["enable", "disable"]
VALID_BODY_MALFORMED_AUTH = ["enable", "disable"]
VALID_BODY_MALFORMED_ASSOCIATION = ["enable", "disable"]
VALID_BODY_HT_40MHZ_INTOLERANCE = ["enable", "disable"]
VALID_BODY_VALID_SSID_MISUSE = ["enable", "disable"]
VALID_BODY_VALID_CLIENT_MISASSOCIATION = ["enable", "disable"]
VALID_BODY_HOTSPOTTER_ATTACK = ["enable", "disable"]
VALID_BODY_PWSAVE_DOS_ATTACK = ["enable", "disable"]
VALID_BODY_OMERTA_ATTACK = ["enable", "disable"]
VALID_BODY_DISCONNECT_STATION = ["enable", "disable"]
VALID_BODY_UNENCRYPTED_VALID = ["enable", "disable"]
VALID_BODY_FATA_JACK = ["enable", "disable"]
VALID_BODY_RISKY_ENCRYPTION = ["enable", "disable"]
VALID_BODY_FUZZED_BEACON = ["enable", "disable"]
VALID_BODY_FUZZED_PROBE_REQUEST = ["enable", "disable"]
VALID_BODY_FUZZED_PROBE_RESPONSE = ["enable", "disable"]
VALID_BODY_AIR_JACK = ["enable", "disable"]
VALID_BODY_WPA_FT_ATTACK = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wids_profile_get(
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


def validate_wids_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating wids_profile.

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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate sensor-mode if present
    if "sensor-mode" in payload:
        value = payload.get("sensor-mode")
        if value and value not in VALID_BODY_SENSOR_MODE:
            return (
                False,
                f"Invalid sensor-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SENSOR_MODE)}",
            )

    # Validate ap-scan if present
    if "ap-scan" in payload:
        value = payload.get("ap-scan")
        if value and value not in VALID_BODY_AP_SCAN:
            return (
                False,
                f"Invalid ap-scan '{value}'. Must be one of: {', '.join(VALID_BODY_AP_SCAN)}",
            )

    # Validate ap-bgscan-period if present
    if "ap-bgscan-period" in payload:
        value = payload.get("ap-bgscan-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (
                        False,
                        "ap-bgscan-period must be between 10 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-bgscan-period must be numeric, got: {value}",
                )

    # Validate ap-bgscan-intv if present
    if "ap-bgscan-intv" in payload:
        value = payload.get("ap-bgscan-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 600:
                    return (False, "ap-bgscan-intv must be between 1 and 600")
            except (ValueError, TypeError):
                return (False, f"ap-bgscan-intv must be numeric, got: {value}")

    # Validate ap-bgscan-duration if present
    if "ap-bgscan-duration" in payload:
        value = payload.get("ap-bgscan-duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 1000:
                    return (
                        False,
                        "ap-bgscan-duration must be between 10 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-bgscan-duration must be numeric, got: {value}",
                )

    # Validate ap-bgscan-idle if present
    if "ap-bgscan-idle" in payload:
        value = payload.get("ap-bgscan-idle")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000:
                    return (
                        False,
                        "ap-bgscan-idle must be between 0 and 1000",
                    )
            except (ValueError, TypeError):
                return (False, f"ap-bgscan-idle must be numeric, got: {value}")

    # Validate ap-bgscan-report-intv if present
    if "ap-bgscan-report-intv" in payload:
        value = payload.get("ap-bgscan-report-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 15 or int_val > 600:
                    return (
                        False,
                        "ap-bgscan-report-intv must be between 15 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-bgscan-report-intv must be numeric, got: {value}",
                )

    # Validate ap-fgscan-report-intv if present
    if "ap-fgscan-report-intv" in payload:
        value = payload.get("ap-fgscan-report-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 15 or int_val > 600:
                    return (
                        False,
                        "ap-fgscan-report-intv must be between 15 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-fgscan-report-intv must be numeric, got: {value}",
                )

    # Validate ap-scan-passive if present
    if "ap-scan-passive" in payload:
        value = payload.get("ap-scan-passive")
        if value and value not in VALID_BODY_AP_SCAN_PASSIVE:
            return (
                False,
                f"Invalid ap-scan-passive '{value}'. Must be one of: {', '.join(VALID_BODY_AP_SCAN_PASSIVE)}",
            )

    # Validate ap-scan-threshold if present
    if "ap-scan-threshold" in payload:
        value = payload.get("ap-scan-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "ap-scan-threshold cannot exceed 7 characters")

    # Validate ap-auto-suppress if present
    if "ap-auto-suppress" in payload:
        value = payload.get("ap-auto-suppress")
        if value and value not in VALID_BODY_AP_AUTO_SUPPRESS:
            return (
                False,
                f"Invalid ap-auto-suppress '{value}'. Must be one of: {', '.join(VALID_BODY_AP_AUTO_SUPPRESS)}",
            )

    # Validate wireless-bridge if present
    if "wireless-bridge" in payload:
        value = payload.get("wireless-bridge")
        if value and value not in VALID_BODY_WIRELESS_BRIDGE:
            return (
                False,
                f"Invalid wireless-bridge '{value}'. Must be one of: {', '.join(VALID_BODY_WIRELESS_BRIDGE)}",
            )

    # Validate deauth-broadcast if present
    if "deauth-broadcast" in payload:
        value = payload.get("deauth-broadcast")
        if value and value not in VALID_BODY_DEAUTH_BROADCAST:
            return (
                False,
                f"Invalid deauth-broadcast '{value}'. Must be one of: {', '.join(VALID_BODY_DEAUTH_BROADCAST)}",
            )

    # Validate null-ssid-probe-resp if present
    if "null-ssid-probe-resp" in payload:
        value = payload.get("null-ssid-probe-resp")
        if value and value not in VALID_BODY_NULL_SSID_PROBE_RESP:
            return (
                False,
                f"Invalid null-ssid-probe-resp '{value}'. Must be one of: {', '.join(VALID_BODY_NULL_SSID_PROBE_RESP)}",
            )

    # Validate long-duration-attack if present
    if "long-duration-attack" in payload:
        value = payload.get("long-duration-attack")
        if value and value not in VALID_BODY_LONG_DURATION_ATTACK:
            return (
                False,
                f"Invalid long-duration-attack '{value}'. Must be one of: {', '.join(VALID_BODY_LONG_DURATION_ATTACK)}",
            )

    # Validate long-duration-thresh if present
    if "long-duration-thresh" in payload:
        value = payload.get("long-duration-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1000 or int_val > 32767:
                    return (
                        False,
                        "long-duration-thresh must be between 1000 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"long-duration-thresh must be numeric, got: {value}",
                )

    # Validate invalid-mac-oui if present
    if "invalid-mac-oui" in payload:
        value = payload.get("invalid-mac-oui")
        if value and value not in VALID_BODY_INVALID_MAC_OUI:
            return (
                False,
                f"Invalid invalid-mac-oui '{value}'. Must be one of: {', '.join(VALID_BODY_INVALID_MAC_OUI)}",
            )

    # Validate weak-wep-iv if present
    if "weak-wep-iv" in payload:
        value = payload.get("weak-wep-iv")
        if value and value not in VALID_BODY_WEAK_WEP_IV:
            return (
                False,
                f"Invalid weak-wep-iv '{value}'. Must be one of: {', '.join(VALID_BODY_WEAK_WEP_IV)}",
            )

    # Validate auth-frame-flood if present
    if "auth-frame-flood" in payload:
        value = payload.get("auth-frame-flood")
        if value and value not in VALID_BODY_AUTH_FRAME_FLOOD:
            return (
                False,
                f"Invalid auth-frame-flood '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_FRAME_FLOOD)}",
            )

    # Validate auth-flood-time if present
    if "auth-flood-time" in payload:
        value = payload.get("auth-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 120:
                    return (
                        False,
                        "auth-flood-time must be between 5 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-flood-time must be numeric, got: {value}",
                )

    # Validate auth-flood-thresh if present
    if "auth-flood-thresh" in payload:
        value = payload.get("auth-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "auth-flood-thresh must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-flood-thresh must be numeric, got: {value}",
                )

    # Validate assoc-frame-flood if present
    if "assoc-frame-flood" in payload:
        value = payload.get("assoc-frame-flood")
        if value and value not in VALID_BODY_ASSOC_FRAME_FLOOD:
            return (
                False,
                f"Invalid assoc-frame-flood '{value}'. Must be one of: {', '.join(VALID_BODY_ASSOC_FRAME_FLOOD)}",
            )

    # Validate assoc-flood-time if present
    if "assoc-flood-time" in payload:
        value = payload.get("assoc-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 120:
                    return (
                        False,
                        "assoc-flood-time must be between 5 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"assoc-flood-time must be numeric, got: {value}",
                )

    # Validate assoc-flood-thresh if present
    if "assoc-flood-thresh" in payload:
        value = payload.get("assoc-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "assoc-flood-thresh must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"assoc-flood-thresh must be numeric, got: {value}",
                )

    # Validate reassoc-flood if present
    if "reassoc-flood" in payload:
        value = payload.get("reassoc-flood")
        if value and value not in VALID_BODY_REASSOC_FLOOD:
            return (
                False,
                f"Invalid reassoc-flood '{value}'. Must be one of: {', '.join(VALID_BODY_REASSOC_FLOOD)}",
            )

    # Validate reassoc-flood-time if present
    if "reassoc-flood-time" in payload:
        value = payload.get("reassoc-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "reassoc-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reassoc-flood-time must be numeric, got: {value}",
                )

    # Validate reassoc-flood-thresh if present
    if "reassoc-flood-thresh" in payload:
        value = payload.get("reassoc-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "reassoc-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reassoc-flood-thresh must be numeric, got: {value}",
                )

    # Validate probe-flood if present
    if "probe-flood" in payload:
        value = payload.get("probe-flood")
        if value and value not in VALID_BODY_PROBE_FLOOD:
            return (
                False,
                f"Invalid probe-flood '{value}'. Must be one of: {', '.join(VALID_BODY_PROBE_FLOOD)}",
            )

    # Validate probe-flood-time if present
    if "probe-flood-time" in payload:
        value = payload.get("probe-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "probe-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"probe-flood-time must be numeric, got: {value}",
                )

    # Validate probe-flood-thresh if present
    if "probe-flood-thresh" in payload:
        value = payload.get("probe-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "probe-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"probe-flood-thresh must be numeric, got: {value}",
                )

    # Validate bcn-flood if present
    if "bcn-flood" in payload:
        value = payload.get("bcn-flood")
        if value and value not in VALID_BODY_BCN_FLOOD:
            return (
                False,
                f"Invalid bcn-flood '{value}'. Must be one of: {', '.join(VALID_BODY_BCN_FLOOD)}",
            )

    # Validate bcn-flood-time if present
    if "bcn-flood-time" in payload:
        value = payload.get("bcn-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (False, "bcn-flood-time must be between 1 and 120")
            except (ValueError, TypeError):
                return (False, f"bcn-flood-time must be numeric, got: {value}")

    # Validate bcn-flood-thresh if present
    if "bcn-flood-thresh" in payload:
        value = payload.get("bcn-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "bcn-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bcn-flood-thresh must be numeric, got: {value}",
                )

    # Validate rts-flood if present
    if "rts-flood" in payload:
        value = payload.get("rts-flood")
        if value and value not in VALID_BODY_RTS_FLOOD:
            return (
                False,
                f"Invalid rts-flood '{value}'. Must be one of: {', '.join(VALID_BODY_RTS_FLOOD)}",
            )

    # Validate rts-flood-time if present
    if "rts-flood-time" in payload:
        value = payload.get("rts-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (False, "rts-flood-time must be between 1 and 120")
            except (ValueError, TypeError):
                return (False, f"rts-flood-time must be numeric, got: {value}")

    # Validate rts-flood-thresh if present
    if "rts-flood-thresh" in payload:
        value = payload.get("rts-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "rts-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rts-flood-thresh must be numeric, got: {value}",
                )

    # Validate cts-flood if present
    if "cts-flood" in payload:
        value = payload.get("cts-flood")
        if value and value not in VALID_BODY_CTS_FLOOD:
            return (
                False,
                f"Invalid cts-flood '{value}'. Must be one of: {', '.join(VALID_BODY_CTS_FLOOD)}",
            )

    # Validate cts-flood-time if present
    if "cts-flood-time" in payload:
        value = payload.get("cts-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (False, "cts-flood-time must be between 1 and 120")
            except (ValueError, TypeError):
                return (False, f"cts-flood-time must be numeric, got: {value}")

    # Validate cts-flood-thresh if present
    if "cts-flood-thresh" in payload:
        value = payload.get("cts-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "cts-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cts-flood-thresh must be numeric, got: {value}",
                )

    # Validate client-flood if present
    if "client-flood" in payload:
        value = payload.get("client-flood")
        if value and value not in VALID_BODY_CLIENT_FLOOD:
            return (
                False,
                f"Invalid client-flood '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_FLOOD)}",
            )

    # Validate client-flood-time if present
    if "client-flood-time" in payload:
        value = payload.get("client-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "client-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-flood-time must be numeric, got: {value}",
                )

    # Validate client-flood-thresh if present
    if "client-flood-thresh" in payload:
        value = payload.get("client-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "client-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-flood-thresh must be numeric, got: {value}",
                )

    # Validate block_ack-flood if present
    if "block_ack-flood" in payload:
        value = payload.get("block_ack-flood")
        if value and value not in VALID_BODY_BLOCK_ACK_FLOOD:
            return (
                False,
                f"Invalid block_ack-flood '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_ACK_FLOOD)}",
            )

    # Validate block_ack-flood-time if present
    if "block_ack-flood-time" in payload:
        value = payload.get("block_ack-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "block_ack-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"block_ack-flood-time must be numeric, got: {value}",
                )

    # Validate block_ack-flood-thresh if present
    if "block_ack-flood-thresh" in payload:
        value = payload.get("block_ack-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "block_ack-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"block_ack-flood-thresh must be numeric, got: {value}",
                )

    # Validate pspoll-flood if present
    if "pspoll-flood" in payload:
        value = payload.get("pspoll-flood")
        if value and value not in VALID_BODY_PSPOLL_FLOOD:
            return (
                False,
                f"Invalid pspoll-flood '{value}'. Must be one of: {', '.join(VALID_BODY_PSPOLL_FLOOD)}",
            )

    # Validate pspoll-flood-time if present
    if "pspoll-flood-time" in payload:
        value = payload.get("pspoll-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "pspoll-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pspoll-flood-time must be numeric, got: {value}",
                )

    # Validate pspoll-flood-thresh if present
    if "pspoll-flood-thresh" in payload:
        value = payload.get("pspoll-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "pspoll-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pspoll-flood-thresh must be numeric, got: {value}",
                )

    # Validate netstumbler if present
    if "netstumbler" in payload:
        value = payload.get("netstumbler")
        if value and value not in VALID_BODY_NETSTUMBLER:
            return (
                False,
                f"Invalid netstumbler '{value}'. Must be one of: {', '.join(VALID_BODY_NETSTUMBLER)}",
            )

    # Validate netstumbler-time if present
    if "netstumbler-time" in payload:
        value = payload.get("netstumbler-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "netstumbler-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"netstumbler-time must be numeric, got: {value}",
                )

    # Validate netstumbler-thresh if present
    if "netstumbler-thresh" in payload:
        value = payload.get("netstumbler-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "netstumbler-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"netstumbler-thresh must be numeric, got: {value}",
                )

    # Validate wellenreiter if present
    if "wellenreiter" in payload:
        value = payload.get("wellenreiter")
        if value and value not in VALID_BODY_WELLENREITER:
            return (
                False,
                f"Invalid wellenreiter '{value}'. Must be one of: {', '.join(VALID_BODY_WELLENREITER)}",
            )

    # Validate wellenreiter-time if present
    if "wellenreiter-time" in payload:
        value = payload.get("wellenreiter-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "wellenreiter-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wellenreiter-time must be numeric, got: {value}",
                )

    # Validate wellenreiter-thresh if present
    if "wellenreiter-thresh" in payload:
        value = payload.get("wellenreiter-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "wellenreiter-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wellenreiter-thresh must be numeric, got: {value}",
                )

    # Validate spoofed-deauth if present
    if "spoofed-deauth" in payload:
        value = payload.get("spoofed-deauth")
        if value and value not in VALID_BODY_SPOOFED_DEAUTH:
            return (
                False,
                f"Invalid spoofed-deauth '{value}'. Must be one of: {', '.join(VALID_BODY_SPOOFED_DEAUTH)}",
            )

    # Validate asleap-attack if present
    if "asleap-attack" in payload:
        value = payload.get("asleap-attack")
        if value and value not in VALID_BODY_ASLEAP_ATTACK:
            return (
                False,
                f"Invalid asleap-attack '{value}'. Must be one of: {', '.join(VALID_BODY_ASLEAP_ATTACK)}",
            )

    # Validate eapol-start-flood if present
    if "eapol-start-flood" in payload:
        value = payload.get("eapol-start-flood")
        if value and value not in VALID_BODY_EAPOL_START_FLOOD:
            return (
                False,
                f"Invalid eapol-start-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_START_FLOOD)}",
            )

    # Validate eapol-start-thresh if present
    if "eapol-start-thresh" in payload:
        value = payload.get("eapol-start-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-start-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-start-thresh must be numeric, got: {value}",
                )

    # Validate eapol-start-intv if present
    if "eapol-start-intv" in payload:
        value = payload.get("eapol-start-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-start-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-start-intv must be numeric, got: {value}",
                )

    # Validate eapol-logoff-flood if present
    if "eapol-logoff-flood" in payload:
        value = payload.get("eapol-logoff-flood")
        if value and value not in VALID_BODY_EAPOL_LOGOFF_FLOOD:
            return (
                False,
                f"Invalid eapol-logoff-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_LOGOFF_FLOOD)}",
            )

    # Validate eapol-logoff-thresh if present
    if "eapol-logoff-thresh" in payload:
        value = payload.get("eapol-logoff-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-logoff-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-logoff-thresh must be numeric, got: {value}",
                )

    # Validate eapol-logoff-intv if present
    if "eapol-logoff-intv" in payload:
        value = payload.get("eapol-logoff-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-logoff-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-logoff-intv must be numeric, got: {value}",
                )

    # Validate eapol-succ-flood if present
    if "eapol-succ-flood" in payload:
        value = payload.get("eapol-succ-flood")
        if value and value not in VALID_BODY_EAPOL_SUCC_FLOOD:
            return (
                False,
                f"Invalid eapol-succ-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_SUCC_FLOOD)}",
            )

    # Validate eapol-succ-thresh if present
    if "eapol-succ-thresh" in payload:
        value = payload.get("eapol-succ-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-succ-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-succ-thresh must be numeric, got: {value}",
                )

    # Validate eapol-succ-intv if present
    if "eapol-succ-intv" in payload:
        value = payload.get("eapol-succ-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-succ-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-succ-intv must be numeric, got: {value}",
                )

    # Validate eapol-fail-flood if present
    if "eapol-fail-flood" in payload:
        value = payload.get("eapol-fail-flood")
        if value and value not in VALID_BODY_EAPOL_FAIL_FLOOD:
            return (
                False,
                f"Invalid eapol-fail-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_FAIL_FLOOD)}",
            )

    # Validate eapol-fail-thresh if present
    if "eapol-fail-thresh" in payload:
        value = payload.get("eapol-fail-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-fail-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-fail-thresh must be numeric, got: {value}",
                )

    # Validate eapol-fail-intv if present
    if "eapol-fail-intv" in payload:
        value = payload.get("eapol-fail-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-fail-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-fail-intv must be numeric, got: {value}",
                )

    # Validate eapol-pre-succ-flood if present
    if "eapol-pre-succ-flood" in payload:
        value = payload.get("eapol-pre-succ-flood")
        if value and value not in VALID_BODY_EAPOL_PRE_SUCC_FLOOD:
            return (
                False,
                f"Invalid eapol-pre-succ-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_PRE_SUCC_FLOOD)}",
            )

    # Validate eapol-pre-succ-thresh if present
    if "eapol-pre-succ-thresh" in payload:
        value = payload.get("eapol-pre-succ-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-pre-succ-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-pre-succ-thresh must be numeric, got: {value}",
                )

    # Validate eapol-pre-succ-intv if present
    if "eapol-pre-succ-intv" in payload:
        value = payload.get("eapol-pre-succ-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-pre-succ-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-pre-succ-intv must be numeric, got: {value}",
                )

    # Validate eapol-pre-fail-flood if present
    if "eapol-pre-fail-flood" in payload:
        value = payload.get("eapol-pre-fail-flood")
        if value and value not in VALID_BODY_EAPOL_PRE_FAIL_FLOOD:
            return (
                False,
                f"Invalid eapol-pre-fail-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_PRE_FAIL_FLOOD)}",
            )

    # Validate eapol-pre-fail-thresh if present
    if "eapol-pre-fail-thresh" in payload:
        value = payload.get("eapol-pre-fail-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-pre-fail-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-pre-fail-thresh must be numeric, got: {value}",
                )

    # Validate eapol-pre-fail-intv if present
    if "eapol-pre-fail-intv" in payload:
        value = payload.get("eapol-pre-fail-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-pre-fail-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-pre-fail-intv must be numeric, got: {value}",
                )

    # Validate deauth-unknown-src-thresh if present
    if "deauth-unknown-src-thresh" in payload:
        value = payload.get("deauth-unknown-src-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "deauth-unknown-src-thresh must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"deauth-unknown-src-thresh must be numeric, got: {value}",
                )

    # Validate windows-bridge if present
    if "windows-bridge" in payload:
        value = payload.get("windows-bridge")
        if value and value not in VALID_BODY_WINDOWS_BRIDGE:
            return (
                False,
                f"Invalid windows-bridge '{value}'. Must be one of: {', '.join(VALID_BODY_WINDOWS_BRIDGE)}",
            )

    # Validate disassoc-broadcast if present
    if "disassoc-broadcast" in payload:
        value = payload.get("disassoc-broadcast")
        if value and value not in VALID_BODY_DISASSOC_BROADCAST:
            return (
                False,
                f"Invalid disassoc-broadcast '{value}'. Must be one of: {', '.join(VALID_BODY_DISASSOC_BROADCAST)}",
            )

    # Validate ap-spoofing if present
    if "ap-spoofing" in payload:
        value = payload.get("ap-spoofing")
        if value and value not in VALID_BODY_AP_SPOOFING:
            return (
                False,
                f"Invalid ap-spoofing '{value}'. Must be one of: {', '.join(VALID_BODY_AP_SPOOFING)}",
            )

    # Validate chan-based-mitm if present
    if "chan-based-mitm" in payload:
        value = payload.get("chan-based-mitm")
        if value and value not in VALID_BODY_CHAN_BASED_MITM:
            return (
                False,
                f"Invalid chan-based-mitm '{value}'. Must be one of: {', '.join(VALID_BODY_CHAN_BASED_MITM)}",
            )

    # Validate adhoc-valid-ssid if present
    if "adhoc-valid-ssid" in payload:
        value = payload.get("adhoc-valid-ssid")
        if value and value not in VALID_BODY_ADHOC_VALID_SSID:
            return (
                False,
                f"Invalid adhoc-valid-ssid '{value}'. Must be one of: {', '.join(VALID_BODY_ADHOC_VALID_SSID)}",
            )

    # Validate adhoc-network if present
    if "adhoc-network" in payload:
        value = payload.get("adhoc-network")
        if value and value not in VALID_BODY_ADHOC_NETWORK:
            return (
                False,
                f"Invalid adhoc-network '{value}'. Must be one of: {', '.join(VALID_BODY_ADHOC_NETWORK)}",
            )

    # Validate eapol-key-overflow if present
    if "eapol-key-overflow" in payload:
        value = payload.get("eapol-key-overflow")
        if value and value not in VALID_BODY_EAPOL_KEY_OVERFLOW:
            return (
                False,
                f"Invalid eapol-key-overflow '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_KEY_OVERFLOW)}",
            )

    # Validate ap-impersonation if present
    if "ap-impersonation" in payload:
        value = payload.get("ap-impersonation")
        if value and value not in VALID_BODY_AP_IMPERSONATION:
            return (
                False,
                f"Invalid ap-impersonation '{value}'. Must be one of: {', '.join(VALID_BODY_AP_IMPERSONATION)}",
            )

    # Validate invalid-addr-combination if present
    if "invalid-addr-combination" in payload:
        value = payload.get("invalid-addr-combination")
        if value and value not in VALID_BODY_INVALID_ADDR_COMBINATION:
            return (
                False,
                f"Invalid invalid-addr-combination '{value}'. Must be one of: {', '.join(VALID_BODY_INVALID_ADDR_COMBINATION)}",
            )

    # Validate beacon-wrong-channel if present
    if "beacon-wrong-channel" in payload:
        value = payload.get("beacon-wrong-channel")
        if value and value not in VALID_BODY_BEACON_WRONG_CHANNEL:
            return (
                False,
                f"Invalid beacon-wrong-channel '{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_WRONG_CHANNEL)}",
            )

    # Validate ht-greenfield if present
    if "ht-greenfield" in payload:
        value = payload.get("ht-greenfield")
        if value and value not in VALID_BODY_HT_GREENFIELD:
            return (
                False,
                f"Invalid ht-greenfield '{value}'. Must be one of: {', '.join(VALID_BODY_HT_GREENFIELD)}",
            )

    # Validate overflow-ie if present
    if "overflow-ie" in payload:
        value = payload.get("overflow-ie")
        if value and value not in VALID_BODY_OVERFLOW_IE:
            return (
                False,
                f"Invalid overflow-ie '{value}'. Must be one of: {', '.join(VALID_BODY_OVERFLOW_IE)}",
            )

    # Validate malformed-ht-ie if present
    if "malformed-ht-ie" in payload:
        value = payload.get("malformed-ht-ie")
        if value and value not in VALID_BODY_MALFORMED_HT_IE:
            return (
                False,
                f"Invalid malformed-ht-ie '{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_HT_IE)}",
            )

    # Validate malformed-auth if present
    if "malformed-auth" in payload:
        value = payload.get("malformed-auth")
        if value and value not in VALID_BODY_MALFORMED_AUTH:
            return (
                False,
                f"Invalid malformed-auth '{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_AUTH)}",
            )

    # Validate malformed-association if present
    if "malformed-association" in payload:
        value = payload.get("malformed-association")
        if value and value not in VALID_BODY_MALFORMED_ASSOCIATION:
            return (
                False,
                f"Invalid malformed-association '{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_ASSOCIATION)}",
            )

    # Validate ht-40mhz-intolerance if present
    if "ht-40mhz-intolerance" in payload:
        value = payload.get("ht-40mhz-intolerance")
        if value and value not in VALID_BODY_HT_40MHZ_INTOLERANCE:
            return (
                False,
                f"Invalid ht-40mhz-intolerance '{value}'. Must be one of: {', '.join(VALID_BODY_HT_40MHZ_INTOLERANCE)}",
            )

    # Validate valid-ssid-misuse if present
    if "valid-ssid-misuse" in payload:
        value = payload.get("valid-ssid-misuse")
        if value and value not in VALID_BODY_VALID_SSID_MISUSE:
            return (
                False,
                f"Invalid valid-ssid-misuse '{value}'. Must be one of: {', '.join(VALID_BODY_VALID_SSID_MISUSE)}",
            )

    # Validate valid-client-misassociation if present
    if "valid-client-misassociation" in payload:
        value = payload.get("valid-client-misassociation")
        if value and value not in VALID_BODY_VALID_CLIENT_MISASSOCIATION:
            return (
                False,
                f"Invalid valid-client-misassociation '{value}'. Must be one of: {', '.join(VALID_BODY_VALID_CLIENT_MISASSOCIATION)}",
            )

    # Validate hotspotter-attack if present
    if "hotspotter-attack" in payload:
        value = payload.get("hotspotter-attack")
        if value and value not in VALID_BODY_HOTSPOTTER_ATTACK:
            return (
                False,
                f"Invalid hotspotter-attack '{value}'. Must be one of: {', '.join(VALID_BODY_HOTSPOTTER_ATTACK)}",
            )

    # Validate pwsave-dos-attack if present
    if "pwsave-dos-attack" in payload:
        value = payload.get("pwsave-dos-attack")
        if value and value not in VALID_BODY_PWSAVE_DOS_ATTACK:
            return (
                False,
                f"Invalid pwsave-dos-attack '{value}'. Must be one of: {', '.join(VALID_BODY_PWSAVE_DOS_ATTACK)}",
            )

    # Validate omerta-attack if present
    if "omerta-attack" in payload:
        value = payload.get("omerta-attack")
        if value and value not in VALID_BODY_OMERTA_ATTACK:
            return (
                False,
                f"Invalid omerta-attack '{value}'. Must be one of: {', '.join(VALID_BODY_OMERTA_ATTACK)}",
            )

    # Validate disconnect-station if present
    if "disconnect-station" in payload:
        value = payload.get("disconnect-station")
        if value and value not in VALID_BODY_DISCONNECT_STATION:
            return (
                False,
                f"Invalid disconnect-station '{value}'. Must be one of: {', '.join(VALID_BODY_DISCONNECT_STATION)}",
            )

    # Validate unencrypted-valid if present
    if "unencrypted-valid" in payload:
        value = payload.get("unencrypted-valid")
        if value and value not in VALID_BODY_UNENCRYPTED_VALID:
            return (
                False,
                f"Invalid unencrypted-valid '{value}'. Must be one of: {', '.join(VALID_BODY_UNENCRYPTED_VALID)}",
            )

    # Validate fata-jack if present
    if "fata-jack" in payload:
        value = payload.get("fata-jack")
        if value and value not in VALID_BODY_FATA_JACK:
            return (
                False,
                f"Invalid fata-jack '{value}'. Must be one of: {', '.join(VALID_BODY_FATA_JACK)}",
            )

    # Validate risky-encryption if present
    if "risky-encryption" in payload:
        value = payload.get("risky-encryption")
        if value and value not in VALID_BODY_RISKY_ENCRYPTION:
            return (
                False,
                f"Invalid risky-encryption '{value}'. Must be one of: {', '.join(VALID_BODY_RISKY_ENCRYPTION)}",
            )

    # Validate fuzzed-beacon if present
    if "fuzzed-beacon" in payload:
        value = payload.get("fuzzed-beacon")
        if value and value not in VALID_BODY_FUZZED_BEACON:
            return (
                False,
                f"Invalid fuzzed-beacon '{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_BEACON)}",
            )

    # Validate fuzzed-probe-request if present
    if "fuzzed-probe-request" in payload:
        value = payload.get("fuzzed-probe-request")
        if value and value not in VALID_BODY_FUZZED_PROBE_REQUEST:
            return (
                False,
                f"Invalid fuzzed-probe-request '{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_PROBE_REQUEST)}",
            )

    # Validate fuzzed-probe-response if present
    if "fuzzed-probe-response" in payload:
        value = payload.get("fuzzed-probe-response")
        if value and value not in VALID_BODY_FUZZED_PROBE_RESPONSE:
            return (
                False,
                f"Invalid fuzzed-probe-response '{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_PROBE_RESPONSE)}",
            )

    # Validate air-jack if present
    if "air-jack" in payload:
        value = payload.get("air-jack")
        if value and value not in VALID_BODY_AIR_JACK:
            return (
                False,
                f"Invalid air-jack '{value}'. Must be one of: {', '.join(VALID_BODY_AIR_JACK)}",
            )

    # Validate wpa-ft-attack if present
    if "wpa-ft-attack" in payload:
        value = payload.get("wpa-ft-attack")
        if value and value not in VALID_BODY_WPA_FT_ATTACK:
            return (
                False,
                f"Invalid wpa-ft-attack '{value}'. Must be one of: {', '.join(VALID_BODY_WPA_FT_ATTACK)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wids_profile_put(
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "comment cannot exceed 63 characters")

    # Validate sensor-mode if present
    if "sensor-mode" in payload:
        value = payload.get("sensor-mode")
        if value and value not in VALID_BODY_SENSOR_MODE:
            return (
                False,
                f"Invalid sensor-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SENSOR_MODE)}",
            )

    # Validate ap-scan if present
    if "ap-scan" in payload:
        value = payload.get("ap-scan")
        if value and value not in VALID_BODY_AP_SCAN:
            return (
                False,
                f"Invalid ap-scan '{value}'. Must be one of: {', '.join(VALID_BODY_AP_SCAN)}",
            )

    # Validate ap-bgscan-period if present
    if "ap-bgscan-period" in payload:
        value = payload.get("ap-bgscan-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 3600:
                    return (
                        False,
                        "ap-bgscan-period must be between 10 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-bgscan-period must be numeric, got: {value}",
                )

    # Validate ap-bgscan-intv if present
    if "ap-bgscan-intv" in payload:
        value = payload.get("ap-bgscan-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 600:
                    return (False, "ap-bgscan-intv must be between 1 and 600")
            except (ValueError, TypeError):
                return (False, f"ap-bgscan-intv must be numeric, got: {value}")

    # Validate ap-bgscan-duration if present
    if "ap-bgscan-duration" in payload:
        value = payload.get("ap-bgscan-duration")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 10 or int_val > 1000:
                    return (
                        False,
                        "ap-bgscan-duration must be between 10 and 1000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-bgscan-duration must be numeric, got: {value}",
                )

    # Validate ap-bgscan-idle if present
    if "ap-bgscan-idle" in payload:
        value = payload.get("ap-bgscan-idle")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 1000:
                    return (
                        False,
                        "ap-bgscan-idle must be between 0 and 1000",
                    )
            except (ValueError, TypeError):
                return (False, f"ap-bgscan-idle must be numeric, got: {value}")

    # Validate ap-bgscan-report-intv if present
    if "ap-bgscan-report-intv" in payload:
        value = payload.get("ap-bgscan-report-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 15 or int_val > 600:
                    return (
                        False,
                        "ap-bgscan-report-intv must be between 15 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-bgscan-report-intv must be numeric, got: {value}",
                )

    # Validate ap-fgscan-report-intv if present
    if "ap-fgscan-report-intv" in payload:
        value = payload.get("ap-fgscan-report-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 15 or int_val > 600:
                    return (
                        False,
                        "ap-fgscan-report-intv must be between 15 and 600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ap-fgscan-report-intv must be numeric, got: {value}",
                )

    # Validate ap-scan-passive if present
    if "ap-scan-passive" in payload:
        value = payload.get("ap-scan-passive")
        if value and value not in VALID_BODY_AP_SCAN_PASSIVE:
            return (
                False,
                f"Invalid ap-scan-passive '{value}'. Must be one of: {', '.join(VALID_BODY_AP_SCAN_PASSIVE)}",
            )

    # Validate ap-scan-threshold if present
    if "ap-scan-threshold" in payload:
        value = payload.get("ap-scan-threshold")
        if value and isinstance(value, str) and len(value) > 7:
            return (False, "ap-scan-threshold cannot exceed 7 characters")

    # Validate ap-auto-suppress if present
    if "ap-auto-suppress" in payload:
        value = payload.get("ap-auto-suppress")
        if value and value not in VALID_BODY_AP_AUTO_SUPPRESS:
            return (
                False,
                f"Invalid ap-auto-suppress '{value}'. Must be one of: {', '.join(VALID_BODY_AP_AUTO_SUPPRESS)}",
            )

    # Validate wireless-bridge if present
    if "wireless-bridge" in payload:
        value = payload.get("wireless-bridge")
        if value and value not in VALID_BODY_WIRELESS_BRIDGE:
            return (
                False,
                f"Invalid wireless-bridge '{value}'. Must be one of: {', '.join(VALID_BODY_WIRELESS_BRIDGE)}",
            )

    # Validate deauth-broadcast if present
    if "deauth-broadcast" in payload:
        value = payload.get("deauth-broadcast")
        if value and value not in VALID_BODY_DEAUTH_BROADCAST:
            return (
                False,
                f"Invalid deauth-broadcast '{value}'. Must be one of: {', '.join(VALID_BODY_DEAUTH_BROADCAST)}",
            )

    # Validate null-ssid-probe-resp if present
    if "null-ssid-probe-resp" in payload:
        value = payload.get("null-ssid-probe-resp")
        if value and value not in VALID_BODY_NULL_SSID_PROBE_RESP:
            return (
                False,
                f"Invalid null-ssid-probe-resp '{value}'. Must be one of: {', '.join(VALID_BODY_NULL_SSID_PROBE_RESP)}",
            )

    # Validate long-duration-attack if present
    if "long-duration-attack" in payload:
        value = payload.get("long-duration-attack")
        if value and value not in VALID_BODY_LONG_DURATION_ATTACK:
            return (
                False,
                f"Invalid long-duration-attack '{value}'. Must be one of: {', '.join(VALID_BODY_LONG_DURATION_ATTACK)}",
            )

    # Validate long-duration-thresh if present
    if "long-duration-thresh" in payload:
        value = payload.get("long-duration-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1000 or int_val > 32767:
                    return (
                        False,
                        "long-duration-thresh must be between 1000 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"long-duration-thresh must be numeric, got: {value}",
                )

    # Validate invalid-mac-oui if present
    if "invalid-mac-oui" in payload:
        value = payload.get("invalid-mac-oui")
        if value and value not in VALID_BODY_INVALID_MAC_OUI:
            return (
                False,
                f"Invalid invalid-mac-oui '{value}'. Must be one of: {', '.join(VALID_BODY_INVALID_MAC_OUI)}",
            )

    # Validate weak-wep-iv if present
    if "weak-wep-iv" in payload:
        value = payload.get("weak-wep-iv")
        if value and value not in VALID_BODY_WEAK_WEP_IV:
            return (
                False,
                f"Invalid weak-wep-iv '{value}'. Must be one of: {', '.join(VALID_BODY_WEAK_WEP_IV)}",
            )

    # Validate auth-frame-flood if present
    if "auth-frame-flood" in payload:
        value = payload.get("auth-frame-flood")
        if value and value not in VALID_BODY_AUTH_FRAME_FLOOD:
            return (
                False,
                f"Invalid auth-frame-flood '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_FRAME_FLOOD)}",
            )

    # Validate auth-flood-time if present
    if "auth-flood-time" in payload:
        value = payload.get("auth-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 120:
                    return (
                        False,
                        "auth-flood-time must be between 5 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-flood-time must be numeric, got: {value}",
                )

    # Validate auth-flood-thresh if present
    if "auth-flood-thresh" in payload:
        value = payload.get("auth-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "auth-flood-thresh must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auth-flood-thresh must be numeric, got: {value}",
                )

    # Validate assoc-frame-flood if present
    if "assoc-frame-flood" in payload:
        value = payload.get("assoc-frame-flood")
        if value and value not in VALID_BODY_ASSOC_FRAME_FLOOD:
            return (
                False,
                f"Invalid assoc-frame-flood '{value}'. Must be one of: {', '.join(VALID_BODY_ASSOC_FRAME_FLOOD)}",
            )

    # Validate assoc-flood-time if present
    if "assoc-flood-time" in payload:
        value = payload.get("assoc-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 120:
                    return (
                        False,
                        "assoc-flood-time must be between 5 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"assoc-flood-time must be numeric, got: {value}",
                )

    # Validate assoc-flood-thresh if present
    if "assoc-flood-thresh" in payload:
        value = payload.get("assoc-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "assoc-flood-thresh must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"assoc-flood-thresh must be numeric, got: {value}",
                )

    # Validate reassoc-flood if present
    if "reassoc-flood" in payload:
        value = payload.get("reassoc-flood")
        if value and value not in VALID_BODY_REASSOC_FLOOD:
            return (
                False,
                f"Invalid reassoc-flood '{value}'. Must be one of: {', '.join(VALID_BODY_REASSOC_FLOOD)}",
            )

    # Validate reassoc-flood-time if present
    if "reassoc-flood-time" in payload:
        value = payload.get("reassoc-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "reassoc-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reassoc-flood-time must be numeric, got: {value}",
                )

    # Validate reassoc-flood-thresh if present
    if "reassoc-flood-thresh" in payload:
        value = payload.get("reassoc-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "reassoc-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reassoc-flood-thresh must be numeric, got: {value}",
                )

    # Validate probe-flood if present
    if "probe-flood" in payload:
        value = payload.get("probe-flood")
        if value and value not in VALID_BODY_PROBE_FLOOD:
            return (
                False,
                f"Invalid probe-flood '{value}'. Must be one of: {', '.join(VALID_BODY_PROBE_FLOOD)}",
            )

    # Validate probe-flood-time if present
    if "probe-flood-time" in payload:
        value = payload.get("probe-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "probe-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"probe-flood-time must be numeric, got: {value}",
                )

    # Validate probe-flood-thresh if present
    if "probe-flood-thresh" in payload:
        value = payload.get("probe-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "probe-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"probe-flood-thresh must be numeric, got: {value}",
                )

    # Validate bcn-flood if present
    if "bcn-flood" in payload:
        value = payload.get("bcn-flood")
        if value and value not in VALID_BODY_BCN_FLOOD:
            return (
                False,
                f"Invalid bcn-flood '{value}'. Must be one of: {', '.join(VALID_BODY_BCN_FLOOD)}",
            )

    # Validate bcn-flood-time if present
    if "bcn-flood-time" in payload:
        value = payload.get("bcn-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (False, "bcn-flood-time must be between 1 and 120")
            except (ValueError, TypeError):
                return (False, f"bcn-flood-time must be numeric, got: {value}")

    # Validate bcn-flood-thresh if present
    if "bcn-flood-thresh" in payload:
        value = payload.get("bcn-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "bcn-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"bcn-flood-thresh must be numeric, got: {value}",
                )

    # Validate rts-flood if present
    if "rts-flood" in payload:
        value = payload.get("rts-flood")
        if value and value not in VALID_BODY_RTS_FLOOD:
            return (
                False,
                f"Invalid rts-flood '{value}'. Must be one of: {', '.join(VALID_BODY_RTS_FLOOD)}",
            )

    # Validate rts-flood-time if present
    if "rts-flood-time" in payload:
        value = payload.get("rts-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (False, "rts-flood-time must be between 1 and 120")
            except (ValueError, TypeError):
                return (False, f"rts-flood-time must be numeric, got: {value}")

    # Validate rts-flood-thresh if present
    if "rts-flood-thresh" in payload:
        value = payload.get("rts-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "rts-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"rts-flood-thresh must be numeric, got: {value}",
                )

    # Validate cts-flood if present
    if "cts-flood" in payload:
        value = payload.get("cts-flood")
        if value and value not in VALID_BODY_CTS_FLOOD:
            return (
                False,
                f"Invalid cts-flood '{value}'. Must be one of: {', '.join(VALID_BODY_CTS_FLOOD)}",
            )

    # Validate cts-flood-time if present
    if "cts-flood-time" in payload:
        value = payload.get("cts-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (False, "cts-flood-time must be between 1 and 120")
            except (ValueError, TypeError):
                return (False, f"cts-flood-time must be numeric, got: {value}")

    # Validate cts-flood-thresh if present
    if "cts-flood-thresh" in payload:
        value = payload.get("cts-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "cts-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cts-flood-thresh must be numeric, got: {value}",
                )

    # Validate client-flood if present
    if "client-flood" in payload:
        value = payload.get("client-flood")
        if value and value not in VALID_BODY_CLIENT_FLOOD:
            return (
                False,
                f"Invalid client-flood '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_FLOOD)}",
            )

    # Validate client-flood-time if present
    if "client-flood-time" in payload:
        value = payload.get("client-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "client-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-flood-time must be numeric, got: {value}",
                )

    # Validate client-flood-thresh if present
    if "client-flood-thresh" in payload:
        value = payload.get("client-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "client-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"client-flood-thresh must be numeric, got: {value}",
                )

    # Validate block_ack-flood if present
    if "block_ack-flood" in payload:
        value = payload.get("block_ack-flood")
        if value and value not in VALID_BODY_BLOCK_ACK_FLOOD:
            return (
                False,
                f"Invalid block_ack-flood '{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_ACK_FLOOD)}",
            )

    # Validate block_ack-flood-time if present
    if "block_ack-flood-time" in payload:
        value = payload.get("block_ack-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "block_ack-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"block_ack-flood-time must be numeric, got: {value}",
                )

    # Validate block_ack-flood-thresh if present
    if "block_ack-flood-thresh" in payload:
        value = payload.get("block_ack-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "block_ack-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"block_ack-flood-thresh must be numeric, got: {value}",
                )

    # Validate pspoll-flood if present
    if "pspoll-flood" in payload:
        value = payload.get("pspoll-flood")
        if value and value not in VALID_BODY_PSPOLL_FLOOD:
            return (
                False,
                f"Invalid pspoll-flood '{value}'. Must be one of: {', '.join(VALID_BODY_PSPOLL_FLOOD)}",
            )

    # Validate pspoll-flood-time if present
    if "pspoll-flood-time" in payload:
        value = payload.get("pspoll-flood-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "pspoll-flood-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pspoll-flood-time must be numeric, got: {value}",
                )

    # Validate pspoll-flood-thresh if present
    if "pspoll-flood-thresh" in payload:
        value = payload.get("pspoll-flood-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "pspoll-flood-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"pspoll-flood-thresh must be numeric, got: {value}",
                )

    # Validate netstumbler if present
    if "netstumbler" in payload:
        value = payload.get("netstumbler")
        if value and value not in VALID_BODY_NETSTUMBLER:
            return (
                False,
                f"Invalid netstumbler '{value}'. Must be one of: {', '.join(VALID_BODY_NETSTUMBLER)}",
            )

    # Validate netstumbler-time if present
    if "netstumbler-time" in payload:
        value = payload.get("netstumbler-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "netstumbler-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"netstumbler-time must be numeric, got: {value}",
                )

    # Validate netstumbler-thresh if present
    if "netstumbler-thresh" in payload:
        value = payload.get("netstumbler-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "netstumbler-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"netstumbler-thresh must be numeric, got: {value}",
                )

    # Validate wellenreiter if present
    if "wellenreiter" in payload:
        value = payload.get("wellenreiter")
        if value and value not in VALID_BODY_WELLENREITER:
            return (
                False,
                f"Invalid wellenreiter '{value}'. Must be one of: {', '.join(VALID_BODY_WELLENREITER)}",
            )

    # Validate wellenreiter-time if present
    if "wellenreiter-time" in payload:
        value = payload.get("wellenreiter-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "wellenreiter-time must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wellenreiter-time must be numeric, got: {value}",
                )

    # Validate wellenreiter-thresh if present
    if "wellenreiter-thresh" in payload:
        value = payload.get("wellenreiter-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65100:
                    return (
                        False,
                        "wellenreiter-thresh must be between 1 and 65100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wellenreiter-thresh must be numeric, got: {value}",
                )

    # Validate spoofed-deauth if present
    if "spoofed-deauth" in payload:
        value = payload.get("spoofed-deauth")
        if value and value not in VALID_BODY_SPOOFED_DEAUTH:
            return (
                False,
                f"Invalid spoofed-deauth '{value}'. Must be one of: {', '.join(VALID_BODY_SPOOFED_DEAUTH)}",
            )

    # Validate asleap-attack if present
    if "asleap-attack" in payload:
        value = payload.get("asleap-attack")
        if value and value not in VALID_BODY_ASLEAP_ATTACK:
            return (
                False,
                f"Invalid asleap-attack '{value}'. Must be one of: {', '.join(VALID_BODY_ASLEAP_ATTACK)}",
            )

    # Validate eapol-start-flood if present
    if "eapol-start-flood" in payload:
        value = payload.get("eapol-start-flood")
        if value and value not in VALID_BODY_EAPOL_START_FLOOD:
            return (
                False,
                f"Invalid eapol-start-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_START_FLOOD)}",
            )

    # Validate eapol-start-thresh if present
    if "eapol-start-thresh" in payload:
        value = payload.get("eapol-start-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-start-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-start-thresh must be numeric, got: {value}",
                )

    # Validate eapol-start-intv if present
    if "eapol-start-intv" in payload:
        value = payload.get("eapol-start-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-start-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-start-intv must be numeric, got: {value}",
                )

    # Validate eapol-logoff-flood if present
    if "eapol-logoff-flood" in payload:
        value = payload.get("eapol-logoff-flood")
        if value and value not in VALID_BODY_EAPOL_LOGOFF_FLOOD:
            return (
                False,
                f"Invalid eapol-logoff-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_LOGOFF_FLOOD)}",
            )

    # Validate eapol-logoff-thresh if present
    if "eapol-logoff-thresh" in payload:
        value = payload.get("eapol-logoff-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-logoff-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-logoff-thresh must be numeric, got: {value}",
                )

    # Validate eapol-logoff-intv if present
    if "eapol-logoff-intv" in payload:
        value = payload.get("eapol-logoff-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-logoff-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-logoff-intv must be numeric, got: {value}",
                )

    # Validate eapol-succ-flood if present
    if "eapol-succ-flood" in payload:
        value = payload.get("eapol-succ-flood")
        if value and value not in VALID_BODY_EAPOL_SUCC_FLOOD:
            return (
                False,
                f"Invalid eapol-succ-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_SUCC_FLOOD)}",
            )

    # Validate eapol-succ-thresh if present
    if "eapol-succ-thresh" in payload:
        value = payload.get("eapol-succ-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-succ-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-succ-thresh must be numeric, got: {value}",
                )

    # Validate eapol-succ-intv if present
    if "eapol-succ-intv" in payload:
        value = payload.get("eapol-succ-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-succ-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-succ-intv must be numeric, got: {value}",
                )

    # Validate eapol-fail-flood if present
    if "eapol-fail-flood" in payload:
        value = payload.get("eapol-fail-flood")
        if value and value not in VALID_BODY_EAPOL_FAIL_FLOOD:
            return (
                False,
                f"Invalid eapol-fail-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_FAIL_FLOOD)}",
            )

    # Validate eapol-fail-thresh if present
    if "eapol-fail-thresh" in payload:
        value = payload.get("eapol-fail-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-fail-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-fail-thresh must be numeric, got: {value}",
                )

    # Validate eapol-fail-intv if present
    if "eapol-fail-intv" in payload:
        value = payload.get("eapol-fail-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-fail-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-fail-intv must be numeric, got: {value}",
                )

    # Validate eapol-pre-succ-flood if present
    if "eapol-pre-succ-flood" in payload:
        value = payload.get("eapol-pre-succ-flood")
        if value and value not in VALID_BODY_EAPOL_PRE_SUCC_FLOOD:
            return (
                False,
                f"Invalid eapol-pre-succ-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_PRE_SUCC_FLOOD)}",
            )

    # Validate eapol-pre-succ-thresh if present
    if "eapol-pre-succ-thresh" in payload:
        value = payload.get("eapol-pre-succ-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-pre-succ-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-pre-succ-thresh must be numeric, got: {value}",
                )

    # Validate eapol-pre-succ-intv if present
    if "eapol-pre-succ-intv" in payload:
        value = payload.get("eapol-pre-succ-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-pre-succ-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-pre-succ-intv must be numeric, got: {value}",
                )

    # Validate eapol-pre-fail-flood if present
    if "eapol-pre-fail-flood" in payload:
        value = payload.get("eapol-pre-fail-flood")
        if value and value not in VALID_BODY_EAPOL_PRE_FAIL_FLOOD:
            return (
                False,
                f"Invalid eapol-pre-fail-flood '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_PRE_FAIL_FLOOD)}",
            )

    # Validate eapol-pre-fail-thresh if present
    if "eapol-pre-fail-thresh" in payload:
        value = payload.get("eapol-pre-fail-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 100:
                    return (
                        False,
                        "eapol-pre-fail-thresh must be between 2 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-pre-fail-thresh must be numeric, got: {value}",
                )

    # Validate eapol-pre-fail-intv if present
    if "eapol-pre-fail-intv" in payload:
        value = payload.get("eapol-pre-fail-intv")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "eapol-pre-fail-intv must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"eapol-pre-fail-intv must be numeric, got: {value}",
                )

    # Validate deauth-unknown-src-thresh if present
    if "deauth-unknown-src-thresh" in payload:
        value = payload.get("deauth-unknown-src-thresh")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "deauth-unknown-src-thresh must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"deauth-unknown-src-thresh must be numeric, got: {value}",
                )

    # Validate windows-bridge if present
    if "windows-bridge" in payload:
        value = payload.get("windows-bridge")
        if value and value not in VALID_BODY_WINDOWS_BRIDGE:
            return (
                False,
                f"Invalid windows-bridge '{value}'. Must be one of: {', '.join(VALID_BODY_WINDOWS_BRIDGE)}",
            )

    # Validate disassoc-broadcast if present
    if "disassoc-broadcast" in payload:
        value = payload.get("disassoc-broadcast")
        if value and value not in VALID_BODY_DISASSOC_BROADCAST:
            return (
                False,
                f"Invalid disassoc-broadcast '{value}'. Must be one of: {', '.join(VALID_BODY_DISASSOC_BROADCAST)}",
            )

    # Validate ap-spoofing if present
    if "ap-spoofing" in payload:
        value = payload.get("ap-spoofing")
        if value and value not in VALID_BODY_AP_SPOOFING:
            return (
                False,
                f"Invalid ap-spoofing '{value}'. Must be one of: {', '.join(VALID_BODY_AP_SPOOFING)}",
            )

    # Validate chan-based-mitm if present
    if "chan-based-mitm" in payload:
        value = payload.get("chan-based-mitm")
        if value and value not in VALID_BODY_CHAN_BASED_MITM:
            return (
                False,
                f"Invalid chan-based-mitm '{value}'. Must be one of: {', '.join(VALID_BODY_CHAN_BASED_MITM)}",
            )

    # Validate adhoc-valid-ssid if present
    if "adhoc-valid-ssid" in payload:
        value = payload.get("adhoc-valid-ssid")
        if value and value not in VALID_BODY_ADHOC_VALID_SSID:
            return (
                False,
                f"Invalid adhoc-valid-ssid '{value}'. Must be one of: {', '.join(VALID_BODY_ADHOC_VALID_SSID)}",
            )

    # Validate adhoc-network if present
    if "adhoc-network" in payload:
        value = payload.get("adhoc-network")
        if value and value not in VALID_BODY_ADHOC_NETWORK:
            return (
                False,
                f"Invalid adhoc-network '{value}'. Must be one of: {', '.join(VALID_BODY_ADHOC_NETWORK)}",
            )

    # Validate eapol-key-overflow if present
    if "eapol-key-overflow" in payload:
        value = payload.get("eapol-key-overflow")
        if value and value not in VALID_BODY_EAPOL_KEY_OVERFLOW:
            return (
                False,
                f"Invalid eapol-key-overflow '{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_KEY_OVERFLOW)}",
            )

    # Validate ap-impersonation if present
    if "ap-impersonation" in payload:
        value = payload.get("ap-impersonation")
        if value and value not in VALID_BODY_AP_IMPERSONATION:
            return (
                False,
                f"Invalid ap-impersonation '{value}'. Must be one of: {', '.join(VALID_BODY_AP_IMPERSONATION)}",
            )

    # Validate invalid-addr-combination if present
    if "invalid-addr-combination" in payload:
        value = payload.get("invalid-addr-combination")
        if value and value not in VALID_BODY_INVALID_ADDR_COMBINATION:
            return (
                False,
                f"Invalid invalid-addr-combination '{value}'. Must be one of: {', '.join(VALID_BODY_INVALID_ADDR_COMBINATION)}",
            )

    # Validate beacon-wrong-channel if present
    if "beacon-wrong-channel" in payload:
        value = payload.get("beacon-wrong-channel")
        if value and value not in VALID_BODY_BEACON_WRONG_CHANNEL:
            return (
                False,
                f"Invalid beacon-wrong-channel '{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_WRONG_CHANNEL)}",
            )

    # Validate ht-greenfield if present
    if "ht-greenfield" in payload:
        value = payload.get("ht-greenfield")
        if value and value not in VALID_BODY_HT_GREENFIELD:
            return (
                False,
                f"Invalid ht-greenfield '{value}'. Must be one of: {', '.join(VALID_BODY_HT_GREENFIELD)}",
            )

    # Validate overflow-ie if present
    if "overflow-ie" in payload:
        value = payload.get("overflow-ie")
        if value and value not in VALID_BODY_OVERFLOW_IE:
            return (
                False,
                f"Invalid overflow-ie '{value}'. Must be one of: {', '.join(VALID_BODY_OVERFLOW_IE)}",
            )

    # Validate malformed-ht-ie if present
    if "malformed-ht-ie" in payload:
        value = payload.get("malformed-ht-ie")
        if value and value not in VALID_BODY_MALFORMED_HT_IE:
            return (
                False,
                f"Invalid malformed-ht-ie '{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_HT_IE)}",
            )

    # Validate malformed-auth if present
    if "malformed-auth" in payload:
        value = payload.get("malformed-auth")
        if value and value not in VALID_BODY_MALFORMED_AUTH:
            return (
                False,
                f"Invalid malformed-auth '{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_AUTH)}",
            )

    # Validate malformed-association if present
    if "malformed-association" in payload:
        value = payload.get("malformed-association")
        if value and value not in VALID_BODY_MALFORMED_ASSOCIATION:
            return (
                False,
                f"Invalid malformed-association '{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_ASSOCIATION)}",
            )

    # Validate ht-40mhz-intolerance if present
    if "ht-40mhz-intolerance" in payload:
        value = payload.get("ht-40mhz-intolerance")
        if value and value not in VALID_BODY_HT_40MHZ_INTOLERANCE:
            return (
                False,
                f"Invalid ht-40mhz-intolerance '{value}'. Must be one of: {', '.join(VALID_BODY_HT_40MHZ_INTOLERANCE)}",
            )

    # Validate valid-ssid-misuse if present
    if "valid-ssid-misuse" in payload:
        value = payload.get("valid-ssid-misuse")
        if value and value not in VALID_BODY_VALID_SSID_MISUSE:
            return (
                False,
                f"Invalid valid-ssid-misuse '{value}'. Must be one of: {', '.join(VALID_BODY_VALID_SSID_MISUSE)}",
            )

    # Validate valid-client-misassociation if present
    if "valid-client-misassociation" in payload:
        value = payload.get("valid-client-misassociation")
        if value and value not in VALID_BODY_VALID_CLIENT_MISASSOCIATION:
            return (
                False,
                f"Invalid valid-client-misassociation '{value}'. Must be one of: {', '.join(VALID_BODY_VALID_CLIENT_MISASSOCIATION)}",
            )

    # Validate hotspotter-attack if present
    if "hotspotter-attack" in payload:
        value = payload.get("hotspotter-attack")
        if value and value not in VALID_BODY_HOTSPOTTER_ATTACK:
            return (
                False,
                f"Invalid hotspotter-attack '{value}'. Must be one of: {', '.join(VALID_BODY_HOTSPOTTER_ATTACK)}",
            )

    # Validate pwsave-dos-attack if present
    if "pwsave-dos-attack" in payload:
        value = payload.get("pwsave-dos-attack")
        if value and value not in VALID_BODY_PWSAVE_DOS_ATTACK:
            return (
                False,
                f"Invalid pwsave-dos-attack '{value}'. Must be one of: {', '.join(VALID_BODY_PWSAVE_DOS_ATTACK)}",
            )

    # Validate omerta-attack if present
    if "omerta-attack" in payload:
        value = payload.get("omerta-attack")
        if value and value not in VALID_BODY_OMERTA_ATTACK:
            return (
                False,
                f"Invalid omerta-attack '{value}'. Must be one of: {', '.join(VALID_BODY_OMERTA_ATTACK)}",
            )

    # Validate disconnect-station if present
    if "disconnect-station" in payload:
        value = payload.get("disconnect-station")
        if value and value not in VALID_BODY_DISCONNECT_STATION:
            return (
                False,
                f"Invalid disconnect-station '{value}'. Must be one of: {', '.join(VALID_BODY_DISCONNECT_STATION)}",
            )

    # Validate unencrypted-valid if present
    if "unencrypted-valid" in payload:
        value = payload.get("unencrypted-valid")
        if value and value not in VALID_BODY_UNENCRYPTED_VALID:
            return (
                False,
                f"Invalid unencrypted-valid '{value}'. Must be one of: {', '.join(VALID_BODY_UNENCRYPTED_VALID)}",
            )

    # Validate fata-jack if present
    if "fata-jack" in payload:
        value = payload.get("fata-jack")
        if value and value not in VALID_BODY_FATA_JACK:
            return (
                False,
                f"Invalid fata-jack '{value}'. Must be one of: {', '.join(VALID_BODY_FATA_JACK)}",
            )

    # Validate risky-encryption if present
    if "risky-encryption" in payload:
        value = payload.get("risky-encryption")
        if value and value not in VALID_BODY_RISKY_ENCRYPTION:
            return (
                False,
                f"Invalid risky-encryption '{value}'. Must be one of: {', '.join(VALID_BODY_RISKY_ENCRYPTION)}",
            )

    # Validate fuzzed-beacon if present
    if "fuzzed-beacon" in payload:
        value = payload.get("fuzzed-beacon")
        if value and value not in VALID_BODY_FUZZED_BEACON:
            return (
                False,
                f"Invalid fuzzed-beacon '{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_BEACON)}",
            )

    # Validate fuzzed-probe-request if present
    if "fuzzed-probe-request" in payload:
        value = payload.get("fuzzed-probe-request")
        if value and value not in VALID_BODY_FUZZED_PROBE_REQUEST:
            return (
                False,
                f"Invalid fuzzed-probe-request '{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_PROBE_REQUEST)}",
            )

    # Validate fuzzed-probe-response if present
    if "fuzzed-probe-response" in payload:
        value = payload.get("fuzzed-probe-response")
        if value and value not in VALID_BODY_FUZZED_PROBE_RESPONSE:
            return (
                False,
                f"Invalid fuzzed-probe-response '{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_PROBE_RESPONSE)}",
            )

    # Validate air-jack if present
    if "air-jack" in payload:
        value = payload.get("air-jack")
        if value and value not in VALID_BODY_AIR_JACK:
            return (
                False,
                f"Invalid air-jack '{value}'. Must be one of: {', '.join(VALID_BODY_AIR_JACK)}",
            )

    # Validate wpa-ft-attack if present
    if "wpa-ft-attack" in payload:
        value = payload.get("wpa-ft-attack")
        if value and value not in VALID_BODY_WPA_FT_ATTACK:
            return (
                False,
                f"Invalid wpa-ft-attack '{value}'. Must be one of: {', '.join(VALID_BODY_WPA_FT_ATTACK)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_wids_profile_delete(
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
