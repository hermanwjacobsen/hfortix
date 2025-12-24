"""
Validation helpers for wireless-controller hotspot20_hs_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ACCESS_NETWORK_TYPE = [
    "private-network",
    "private-network-with-guest-access",
    "chargeable-public-network",
    "free-public-network",
    "personal-device-network",
    "emergency-services-only-network",
    "test-or-experimental",
    "wildcard",
]
VALID_BODY_ACCESS_NETWORK_INTERNET = ["enable", "disable"]
VALID_BODY_ACCESS_NETWORK_ASRA = ["enable", "disable"]
VALID_BODY_ACCESS_NETWORK_ESR = ["enable", "disable"]
VALID_BODY_ACCESS_NETWORK_UESA = ["enable", "disable"]
VALID_BODY_VENUE_GROUP = [
    "unspecified",
    "assembly",
    "business",
    "educational",
    "factory",
    "institutional",
    "mercantile",
    "residential",
    "storage",
    "utility",
    "vehicular",
    "outdoor",
]
VALID_BODY_VENUE_TYPE = [
    "unspecified",
    "arena",
    "stadium",
    "passenger-terminal",
    "amphitheater",
    "amusement-park",
    "place-of-worship",
    "convention-center",
    "library",
    "museum",
    "restaurant",
    "theater",
    "bar",
    "coffee-shop",
    "zoo-or-aquarium",
    "emergency-center",
    "doctor-office",
    "bank",
    "fire-station",
    "police-station",
    "post-office",
    "professional-office",
    "research-facility",
    "attorney-office",
    "primary-school",
    "secondary-school",
    "university-or-college",
    "factory",
    "hospital",
    "long-term-care-facility",
    "rehab-center",
    "group-home",
    "prison-or-jail",
    "retail-store",
    "grocery-market",
    "auto-service-station",
    "shopping-mall",
    "gas-station",
    "private",
    "hotel-or-motel",
    "dormitory",
    "boarding-house",
    "automobile",
    "airplane",
    "bus",
    "ferry",
    "ship-or-boat",
    "train",
    "motor-bike",
    "muni-mesh-network",
    "city-park",
    "rest-area",
    "traffic-control",
    "bus-stop",
    "kiosk",
]
VALID_BODY_PROXY_ARP = ["enable", "disable"]
VALID_BODY_L2TIF = ["enable", "disable"]
VALID_BODY_PAME_BI = ["disable", "enable"]
VALID_BODY_DGAF = ["enable", "disable"]
VALID_BODY_WNM_SLEEP_MODE = ["enable", "disable"]
VALID_BODY_BSS_TRANSITION = ["enable", "disable"]
VALID_BODY_WBA_OPEN_ROAMING = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_hotspot20_hs_profile_get(
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


def validate_hotspot20_hs_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating hotspot20_hs_profile.

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

    # Validate release if present
    if "release" in payload:
        value = payload.get("release")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3:
                    return (False, "release must be between 1 and 3")
            except (ValueError, TypeError):
                return (False, f"release must be numeric, got: {value}")

    # Validate access-network-type if present
    if "access-network-type" in payload:
        value = payload.get("access-network-type")
        if value and value not in VALID_BODY_ACCESS_NETWORK_TYPE:
            return (
                False,
                f"Invalid access-network-type '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_TYPE)}",
            )

    # Validate access-network-internet if present
    if "access-network-internet" in payload:
        value = payload.get("access-network-internet")
        if value and value not in VALID_BODY_ACCESS_NETWORK_INTERNET:
            return (
                False,
                f"Invalid access-network-internet '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_INTERNET)}",
            )

    # Validate access-network-asra if present
    if "access-network-asra" in payload:
        value = payload.get("access-network-asra")
        if value and value not in VALID_BODY_ACCESS_NETWORK_ASRA:
            return (
                False,
                f"Invalid access-network-asra '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_ASRA)}",
            )

    # Validate access-network-esr if present
    if "access-network-esr" in payload:
        value = payload.get("access-network-esr")
        if value and value not in VALID_BODY_ACCESS_NETWORK_ESR:
            return (
                False,
                f"Invalid access-network-esr '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_ESR)}",
            )

    # Validate access-network-uesa if present
    if "access-network-uesa" in payload:
        value = payload.get("access-network-uesa")
        if value and value not in VALID_BODY_ACCESS_NETWORK_UESA:
            return (
                False,
                f"Invalid access-network-uesa '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_UESA)}",
            )

    # Validate venue-group if present
    if "venue-group" in payload:
        value = payload.get("venue-group")
        if value and value not in VALID_BODY_VENUE_GROUP:
            return (
                False,
                f"Invalid venue-group '{value}'. Must be one of: {', '.join(VALID_BODY_VENUE_GROUP)}",
            )

    # Validate venue-type if present
    if "venue-type" in payload:
        value = payload.get("venue-type")
        if value and value not in VALID_BODY_VENUE_TYPE:
            return (
                False,
                f"Invalid venue-type '{value}'. Must be one of: {', '.join(VALID_BODY_VENUE_TYPE)}",
            )

    # Validate proxy-arp if present
    if "proxy-arp" in payload:
        value = payload.get("proxy-arp")
        if value and value not in VALID_BODY_PROXY_ARP:
            return (
                False,
                f"Invalid proxy-arp '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_ARP)}",
            )

    # Validate l2tif if present
    if "l2ti" in payload:
        value = payload.get("l2ti")
        if value and value not in VALID_BODY_L2TIF:
            return (
                False,
                f"Invalid l2tif '{value}'. Must be one of: {', '.join(VALID_BODY_L2TIF)}",
            )

    # Validate pame-bi if present
    if "pame-bi" in payload:
        value = payload.get("pame-bi")
        if value and value not in VALID_BODY_PAME_BI:
            return (
                False,
                f"Invalid pame-bi '{value}'. Must be one of: {', '.join(VALID_BODY_PAME_BI)}",
            )

    # Validate anqp-domain-id if present
    if "anqp-domain-id" in payload:
        value = payload.get("anqp-domain-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "anqp-domain-id must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"anqp-domain-id must be numeric, got: {value}")

    # Validate domain-name if present
    if "domain-name" in payload:
        value = payload.get("domain-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "domain-name cannot exceed 255 characters")

    # Validate osu-ssid if present
    if "osu-ssid" in payload:
        value = payload.get("osu-ssid")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "osu-ssid cannot exceed 255 characters")

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

    # Validate dgaf if present
    if "dga" in payload:
        value = payload.get("dga")
        if value and value not in VALID_BODY_DGAF:
            return (
                False,
                f"Invalid dgaf '{value}'. Must be one of: {', '.join(VALID_BODY_DGAF)}",
            )

    # Validate deauth-request-timeout if present
    if "deauth-request-timeout" in payload:
        value = payload.get("deauth-request-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 120:
                    return (
                        False,
                        "deauth-request-timeout must be between 30 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"deauth-request-timeout must be numeric, got: {value}",
                )

    # Validate wnm-sleep-mode if present
    if "wnm-sleep-mode" in payload:
        value = payload.get("wnm-sleep-mode")
        if value and value not in VALID_BODY_WNM_SLEEP_MODE:
            return (
                False,
                f"Invalid wnm-sleep-mode '{value}'. Must be one of: {', '.join(VALID_BODY_WNM_SLEEP_MODE)}",
            )

    # Validate bss-transition if present
    if "bss-transition" in payload:
        value = payload.get("bss-transition")
        if value and value not in VALID_BODY_BSS_TRANSITION:
            return (
                False,
                f"Invalid bss-transition '{value}'. Must be one of: {', '.join(VALID_BODY_BSS_TRANSITION)}",
            )

    # Validate venue-name if present
    if "venue-name" in payload:
        value = payload.get("venue-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "venue-name cannot exceed 35 characters")

    # Validate venue-url if present
    if "venue-url" in payload:
        value = payload.get("venue-url")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "venue-url cannot exceed 35 characters")

    # Validate roaming-consortium if present
    if "roaming-consortium" in payload:
        value = payload.get("roaming-consortium")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "roaming-consortium cannot exceed 35 characters")

    # Validate nai-realm if present
    if "nai-realm" in payload:
        value = payload.get("nai-realm")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "nai-realm cannot exceed 35 characters")

    # Validate oper-friendly-name if present
    if "oper-friendly-name" in payload:
        value = payload.get("oper-friendly-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "oper-friendly-name cannot exceed 35 characters")

    # Validate oper-icon if present
    if "oper-icon" in payload:
        value = payload.get("oper-icon")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "oper-icon cannot exceed 35 characters")

    # Validate advice-of-charge if present
    if "advice-of-charge" in payload:
        value = payload.get("advice-of-charge")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "advice-of-charge cannot exceed 35 characters")

    # Validate osu-provider-nai if present
    if "osu-provider-nai" in payload:
        value = payload.get("osu-provider-nai")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "osu-provider-nai cannot exceed 35 characters")

    # Validate terms-and-conditions if present
    if "terms-and-conditions" in payload:
        value = payload.get("terms-and-conditions")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "terms-and-conditions cannot exceed 35 characters")

    # Validate wan-metrics if present
    if "wan-metrics" in payload:
        value = payload.get("wan-metrics")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "wan-metrics cannot exceed 35 characters")

    # Validate network-auth if present
    if "network-auth" in payload:
        value = payload.get("network-auth")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "network-auth cannot exceed 35 characters")

    # Validate 3gpp-plmn if present
    if "3gpp-plmn" in payload:
        value = payload.get("3gpp-plmn")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "3gpp-plmn cannot exceed 35 characters")

    # Validate conn-cap if present
    if "conn-cap" in payload:
        value = payload.get("conn-cap")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "conn-cap cannot exceed 35 characters")

    # Validate qos-map if present
    if "qos-map" in payload:
        value = payload.get("qos-map")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "qos-map cannot exceed 35 characters")

    # Validate ip-addr-type if present
    if "ip-addr-type" in payload:
        value = payload.get("ip-addr-type")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ip-addr-type cannot exceed 35 characters")

    # Validate wba-open-roaming if present
    if "wba-open-roaming" in payload:
        value = payload.get("wba-open-roaming")
        if value and value not in VALID_BODY_WBA_OPEN_ROAMING:
            return (
                False,
                f"Invalid wba-open-roaming '{value}'. Must be one of: {', '.join(VALID_BODY_WBA_OPEN_ROAMING)}",
            )

    # Validate wba-financial-clearing-provider if present
    if "wba-financial-clearing-provider" in payload:
        value = payload.get("wba-financial-clearing-provider")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "wba-financial-clearing-provider cannot exceed 127 characters",
            )

    # Validate wba-data-clearing-provider if present
    if "wba-data-clearing-provider" in payload:
        value = payload.get("wba-data-clearing-provider")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "wba-data-clearing-provider cannot exceed 127 characters",
            )

    # Validate wba-charging-currency if present
    if "wba-charging-currency" in payload:
        value = payload.get("wba-charging-currency")
        if value and isinstance(value, str) and len(value) > 3:
            return (False, "wba-charging-currency cannot exceed 3 characters")

    # Validate wba-charging-rate if present
    if "wba-charging-rate" in payload:
        value = payload.get("wba-charging-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "wba-charging-rate must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wba-charging-rate must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_hotspot20_hs_profile_put(
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

    # Validate release if present
    if "release" in payload:
        value = payload.get("release")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3:
                    return (False, "release must be between 1 and 3")
            except (ValueError, TypeError):
                return (False, f"release must be numeric, got: {value}")

    # Validate access-network-type if present
    if "access-network-type" in payload:
        value = payload.get("access-network-type")
        if value and value not in VALID_BODY_ACCESS_NETWORK_TYPE:
            return (
                False,
                f"Invalid access-network-type '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_TYPE)}",
            )

    # Validate access-network-internet if present
    if "access-network-internet" in payload:
        value = payload.get("access-network-internet")
        if value and value not in VALID_BODY_ACCESS_NETWORK_INTERNET:
            return (
                False,
                f"Invalid access-network-internet '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_INTERNET)}",
            )

    # Validate access-network-asra if present
    if "access-network-asra" in payload:
        value = payload.get("access-network-asra")
        if value and value not in VALID_BODY_ACCESS_NETWORK_ASRA:
            return (
                False,
                f"Invalid access-network-asra '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_ASRA)}",
            )

    # Validate access-network-esr if present
    if "access-network-esr" in payload:
        value = payload.get("access-network-esr")
        if value and value not in VALID_BODY_ACCESS_NETWORK_ESR:
            return (
                False,
                f"Invalid access-network-esr '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_ESR)}",
            )

    # Validate access-network-uesa if present
    if "access-network-uesa" in payload:
        value = payload.get("access-network-uesa")
        if value and value not in VALID_BODY_ACCESS_NETWORK_UESA:
            return (
                False,
                f"Invalid access-network-uesa '{value}'. Must be one of: {', '.join(VALID_BODY_ACCESS_NETWORK_UESA)}",
            )

    # Validate venue-group if present
    if "venue-group" in payload:
        value = payload.get("venue-group")
        if value and value not in VALID_BODY_VENUE_GROUP:
            return (
                False,
                f"Invalid venue-group '{value}'. Must be one of: {', '.join(VALID_BODY_VENUE_GROUP)}",
            )

    # Validate venue-type if present
    if "venue-type" in payload:
        value = payload.get("venue-type")
        if value and value not in VALID_BODY_VENUE_TYPE:
            return (
                False,
                f"Invalid venue-type '{value}'. Must be one of: {', '.join(VALID_BODY_VENUE_TYPE)}",
            )

    # Validate proxy-arp if present
    if "proxy-arp" in payload:
        value = payload.get("proxy-arp")
        if value and value not in VALID_BODY_PROXY_ARP:
            return (
                False,
                f"Invalid proxy-arp '{value}'. Must be one of: {', '.join(VALID_BODY_PROXY_ARP)}",
            )

    # Validate l2tif if present
    if "l2ti" in payload:
        value = payload.get("l2ti")
        if value and value not in VALID_BODY_L2TIF:
            return (
                False,
                f"Invalid l2tif '{value}'. Must be one of: {', '.join(VALID_BODY_L2TIF)}",
            )

    # Validate pame-bi if present
    if "pame-bi" in payload:
        value = payload.get("pame-bi")
        if value and value not in VALID_BODY_PAME_BI:
            return (
                False,
                f"Invalid pame-bi '{value}'. Must be one of: {', '.join(VALID_BODY_PAME_BI)}",
            )

    # Validate anqp-domain-id if present
    if "anqp-domain-id" in payload:
        value = payload.get("anqp-domain-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "anqp-domain-id must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (False, f"anqp-domain-id must be numeric, got: {value}")

    # Validate domain-name if present
    if "domain-name" in payload:
        value = payload.get("domain-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "domain-name cannot exceed 255 characters")

    # Validate osu-ssid if present
    if "osu-ssid" in payload:
        value = payload.get("osu-ssid")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "osu-ssid cannot exceed 255 characters")

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

    # Validate dgaf if present
    if "dga" in payload:
        value = payload.get("dga")
        if value and value not in VALID_BODY_DGAF:
            return (
                False,
                f"Invalid dgaf '{value}'. Must be one of: {', '.join(VALID_BODY_DGAF)}",
            )

    # Validate deauth-request-timeout if present
    if "deauth-request-timeout" in payload:
        value = payload.get("deauth-request-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 120:
                    return (
                        False,
                        "deauth-request-timeout must be between 30 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"deauth-request-timeout must be numeric, got: {value}",
                )

    # Validate wnm-sleep-mode if present
    if "wnm-sleep-mode" in payload:
        value = payload.get("wnm-sleep-mode")
        if value and value not in VALID_BODY_WNM_SLEEP_MODE:
            return (
                False,
                f"Invalid wnm-sleep-mode '{value}'. Must be one of: {', '.join(VALID_BODY_WNM_SLEEP_MODE)}",
            )

    # Validate bss-transition if present
    if "bss-transition" in payload:
        value = payload.get("bss-transition")
        if value and value not in VALID_BODY_BSS_TRANSITION:
            return (
                False,
                f"Invalid bss-transition '{value}'. Must be one of: {', '.join(VALID_BODY_BSS_TRANSITION)}",
            )

    # Validate venue-name if present
    if "venue-name" in payload:
        value = payload.get("venue-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "venue-name cannot exceed 35 characters")

    # Validate venue-url if present
    if "venue-url" in payload:
        value = payload.get("venue-url")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "venue-url cannot exceed 35 characters")

    # Validate roaming-consortium if present
    if "roaming-consortium" in payload:
        value = payload.get("roaming-consortium")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "roaming-consortium cannot exceed 35 characters")

    # Validate nai-realm if present
    if "nai-realm" in payload:
        value = payload.get("nai-realm")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "nai-realm cannot exceed 35 characters")

    # Validate oper-friendly-name if present
    if "oper-friendly-name" in payload:
        value = payload.get("oper-friendly-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "oper-friendly-name cannot exceed 35 characters")

    # Validate oper-icon if present
    if "oper-icon" in payload:
        value = payload.get("oper-icon")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "oper-icon cannot exceed 35 characters")

    # Validate advice-of-charge if present
    if "advice-of-charge" in payload:
        value = payload.get("advice-of-charge")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "advice-of-charge cannot exceed 35 characters")

    # Validate osu-provider-nai if present
    if "osu-provider-nai" in payload:
        value = payload.get("osu-provider-nai")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "osu-provider-nai cannot exceed 35 characters")

    # Validate terms-and-conditions if present
    if "terms-and-conditions" in payload:
        value = payload.get("terms-and-conditions")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "terms-and-conditions cannot exceed 35 characters")

    # Validate wan-metrics if present
    if "wan-metrics" in payload:
        value = payload.get("wan-metrics")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "wan-metrics cannot exceed 35 characters")

    # Validate network-auth if present
    if "network-auth" in payload:
        value = payload.get("network-auth")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "network-auth cannot exceed 35 characters")

    # Validate 3gpp-plmn if present
    if "3gpp-plmn" in payload:
        value = payload.get("3gpp-plmn")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "3gpp-plmn cannot exceed 35 characters")

    # Validate conn-cap if present
    if "conn-cap" in payload:
        value = payload.get("conn-cap")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "conn-cap cannot exceed 35 characters")

    # Validate qos-map if present
    if "qos-map" in payload:
        value = payload.get("qos-map")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "qos-map cannot exceed 35 characters")

    # Validate ip-addr-type if present
    if "ip-addr-type" in payload:
        value = payload.get("ip-addr-type")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ip-addr-type cannot exceed 35 characters")

    # Validate wba-open-roaming if present
    if "wba-open-roaming" in payload:
        value = payload.get("wba-open-roaming")
        if value and value not in VALID_BODY_WBA_OPEN_ROAMING:
            return (
                False,
                f"Invalid wba-open-roaming '{value}'. Must be one of: {', '.join(VALID_BODY_WBA_OPEN_ROAMING)}",
            )

    # Validate wba-financial-clearing-provider if present
    if "wba-financial-clearing-provider" in payload:
        value = payload.get("wba-financial-clearing-provider")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "wba-financial-clearing-provider cannot exceed 127 characters",
            )

    # Validate wba-data-clearing-provider if present
    if "wba-data-clearing-provider" in payload:
        value = payload.get("wba-data-clearing-provider")
        if value and isinstance(value, str) and len(value) > 127:
            return (
                False,
                "wba-data-clearing-provider cannot exceed 127 characters",
            )

    # Validate wba-charging-currency if present
    if "wba-charging-currency" in payload:
        value = payload.get("wba-charging-currency")
        if value and isinstance(value, str) and len(value) > 3:
            return (False, "wba-charging-currency cannot exceed 3 characters")

    # Validate wba-charging-rate if present
    if "wba-charging-rate" in payload:
        value = payload.get("wba-charging-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "wba-charging-rate must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"wba-charging-rate must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_hotspot20_hs_profile_delete(
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
