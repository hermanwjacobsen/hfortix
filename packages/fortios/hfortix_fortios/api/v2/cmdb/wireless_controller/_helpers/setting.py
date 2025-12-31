"""
Validation helpers for wireless-controller setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_COUNTRY = [
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
VALID_BODY_DUPLICATE_SSID = ["enable", "disable"]
VALID_BODY_FAPC_COMPATIBILITY = ["enable", "disable"]
VALID_BODY_WFA_COMPATIBILITY = ["enable", "disable"]
VALID_BODY_PHISHING_SSID_DETECT = ["enable", "disable"]
VALID_BODY_FAKE_SSID_ACTION = ["log", "suppress"]
VALID_BODY_FIRMWARE_PROVISION_ON_AUTHORIZATION = ["enable", "disable"]
VALID_BODY_ROLLING_WTP_UPGRADE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_setting_get(
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


def validate_setting_put(
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

    # Validate account-id if present
    if "account-id" in payload:
        value = payload.get("account-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "account-id cannot exceed 63 characters")

    # Validate country if present
    if "country" in payload:
        value = payload.get("country")
        if value and value not in VALID_BODY_COUNTRY:
            return (
                False,
                f"Invalid country '{value}'. Must be one of: {', '.join(VALID_BODY_COUNTRY)}",
            )

    # Validate duplicate-ssid if present
    if "duplicate-ssid" in payload:
        value = payload.get("duplicate-ssid")
        if value and value not in VALID_BODY_DUPLICATE_SSID:
            return (
                False,
                f"Invalid duplicate-ssid '{value}'. Must be one of: {', '.join(VALID_BODY_DUPLICATE_SSID)}",
            )

    # Validate fapc-compatibility if present
    if "fapc-compatibility" in payload:
        value = payload.get("fapc-compatibility")
        if value and value not in VALID_BODY_FAPC_COMPATIBILITY:
            return (
                False,
                f"Invalid fapc-compatibility '{value}'. Must be one of: {', '.join(VALID_BODY_FAPC_COMPATIBILITY)}",
            )

    # Validate wfa-compatibility if present
    if "wfa-compatibility" in payload:
        value = payload.get("wfa-compatibility")
        if value and value not in VALID_BODY_WFA_COMPATIBILITY:
            return (
                False,
                f"Invalid wfa-compatibility '{value}'. Must be one of: {', '.join(VALID_BODY_WFA_COMPATIBILITY)}",
            )

    # Validate phishing-ssid-detect if present
    if "phishing-ssid-detect" in payload:
        value = payload.get("phishing-ssid-detect")
        if value and value not in VALID_BODY_PHISHING_SSID_DETECT:
            return (
                False,
                f"Invalid phishing-ssid-detect '{value}'. Must be one of: {', '.join(VALID_BODY_PHISHING_SSID_DETECT)}",
            )

    # Validate fake-ssid-action if present
    if "fake-ssid-action" in payload:
        value = payload.get("fake-ssid-action")
        if value and value not in VALID_BODY_FAKE_SSID_ACTION:
            return (
                False,
                f"Invalid fake-ssid-action '{value}'. Must be one of: {', '.join(VALID_BODY_FAKE_SSID_ACTION)}",
            )

    # Validate device-weight if present
    if "device-weight" in payload:
        value = payload.get("device-weight")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "device-weight must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"device-weight must be numeric, got: {value}")

    # Validate device-holdoff if present
    if "device-holdof" in payload:
        value = payload.get("device-holdof")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 60:
                    return (False, "device-holdoff must be between 0 and 60")
            except (ValueError, TypeError):
                return (False, f"device-holdoff must be numeric, got: {value}")

    # Validate device-idle if present
    if "device-idle" in payload:
        value = payload.get("device-idle")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 14400:
                    return (False, "device-idle must be between 0 and 14400")
            except (ValueError, TypeError):
                return (False, f"device-idle must be numeric, got: {value}")

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

    # Validate rolling-wtp-upgrade if present
    if "rolling-wtp-upgrade" in payload:
        value = payload.get("rolling-wtp-upgrade")
        if value and value not in VALID_BODY_ROLLING_WTP_UPGRADE:
            return (
                False,
                f"Invalid rolling-wtp-upgrade '{value}'. Must be one of: {', '.join(VALID_BODY_ROLLING_WTP_UPGRADE)}",
            )

    # Validate darrp-optimize if present
    if "darrp-optimize" in payload:
        value = payload.get("darrp-optimize")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (
                        False,
                        "darrp-optimize must be between 0 and 86400",
                    )
            except (ValueError, TypeError):
                return (False, f"darrp-optimize must be numeric, got: {value}")

    return (True, None)
