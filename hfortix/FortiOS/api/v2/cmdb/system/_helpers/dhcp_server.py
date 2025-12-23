"""
Validation helpers for system dhcp_server endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["disable", "enable"]
VALID_BODY_MAC_ACL_DEFAULT_ACTION = ["assign", "block"]
VALID_BODY_FORTICLIENT_ON_NET_STATUS = ["disable", "enable"]
VALID_BODY_DNS_SERVICE = ["local", "default", "specify"]
VALID_BODY_WIFI_AC_SERVICE = ["specify", "local"]
VALID_BODY_NTP_SERVICE = ["local", "default", "specify"]
VALID_BODY_TIMEZONE_OPTION = ["disable", "default", "specify"]
VALID_BODY_SERVER_TYPE = ["regular", "ipsec"]
VALID_BODY_IP_MODE = ["range", "usrgrp"]
VALID_BODY_AUTO_CONFIGURATION = ["disable", "enable"]
VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM = ["disable", "enable"]
VALID_BODY_AUTO_MANAGED_STATUS = ["disable", "enable"]
VALID_BODY_DDNS_UPDATE = ["disable", "enable"]
VALID_BODY_DDNS_UPDATE_OVERRIDE = ["disable", "enable"]
VALID_BODY_DDNS_AUTH = ["disable", "tsig"]
VALID_BODY_VCI_MATCH = ["disable", "enable"]
VALID_BODY_SHARED_SUBNET = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_dhcp_server_get(
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


def validate_dhcp_server_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating dhcp_server.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate lease-time if present
    if "lease-time" in payload:
        value = payload.get("lease-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (
                        False,
                        "lease-time must be between 300 and 8640000",
                    )
            except (ValueError, TypeError):
                return (False, f"lease-time must be numeric, got: {value}")

    # Validate mac-acl-default-action if present
    if "mac-acl-default-action" in payload:
        value = payload.get("mac-acl-default-action")
        if value and value not in VALID_BODY_MAC_ACL_DEFAULT_ACTION:
            return (
                False,
                f"Invalid mac-acl-default-action '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_ACL_DEFAULT_ACTION)}",
            )

    # Validate forticlient-on-net-status if present
    if "forticlient-on-net-status" in payload:
        value = payload.get("forticlient-on-net-status")
        if value and value not in VALID_BODY_FORTICLIENT_ON_NET_STATUS:
            return (
                False,
                f"Invalid forticlient-on-net-status '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLIENT_ON_NET_STATUS)}",
            )

    # Validate dns-service if present
    if "dns-service" in payload:
        value = payload.get("dns-service")
        if value and value not in VALID_BODY_DNS_SERVICE:
            return (
                False,
                f"Invalid dns-service '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVICE)}",
            )

    # Validate wifi-ac-service if present
    if "wifi-ac-service" in payload:
        value = payload.get("wifi-ac-service")
        if value and value not in VALID_BODY_WIFI_AC_SERVICE:
            return (
                False,
                f"Invalid wifi-ac-service '{value}'. Must be one of: {', '.join(VALID_BODY_WIFI_AC_SERVICE)}",
            )

    # Validate ntp-service if present
    if "ntp-service" in payload:
        value = payload.get("ntp-service")
        if value and value not in VALID_BODY_NTP_SERVICE:
            return (
                False,
                f"Invalid ntp-service '{value}'. Must be one of: {', '.join(VALID_BODY_NTP_SERVICE)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "domain cannot exceed 35 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate timezone-option if present
    if "timezone-option" in payload:
        value = payload.get("timezone-option")
        if value and value not in VALID_BODY_TIMEZONE_OPTION:
            return (
                False,
                f"Invalid timezone-option '{value}'. Must be one of: {', '.join(VALID_BODY_TIMEZONE_OPTION)}",
            )

    # Validate timezone if present
    if "timezone" in payload:
        value = payload.get("timezone")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "timezone cannot exceed 63 characters")

    # Validate filename if present
    if "filename" in payload:
        value = payload.get("filename")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "filename cannot exceed 127 characters")

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate ip-mode if present
    if "ip-mode" in payload:
        value = payload.get("ip-mode")
        if value and value not in VALID_BODY_IP_MODE:
            return (
                False,
                f"Invalid ip-mode '{value}'. Must be one of: {', '.join(VALID_BODY_IP_MODE)}",
            )

    # Validate conflicted-ip-timeout if present
    if "conflicted-ip-timeout" in payload:
        value = payload.get("conflicted-ip-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 8640000:
                    return (
                        False,
                        "conflicted-ip-timeout must be between 60 and 8640000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"conflicted-ip-timeout must be numeric, got: {value}",
                )

    # Validate ipsec-lease-hold if present
    if "ipsec-lease-hold" in payload:
        value = payload.get("ipsec-lease-hold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 8640000:
                    return (
                        False,
                        "ipsec-lease-hold must be between 0 and 8640000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ipsec-lease-hold must be numeric, got: {value}",
                )

    # Validate auto-configuration if present
    if "auto-configuration" in payload:
        value = payload.get("auto-configuration")
        if value and value not in VALID_BODY_AUTO_CONFIGURATION:
            return (
                False,
                f"Invalid auto-configuration '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_CONFIGURATION)}",
            )

    # Validate dhcp-settings-from-fortiipam if present
    if "dhcp-settings-from-fortiipam" in payload:
        value = payload.get("dhcp-settings-from-fortiipam")
        if value and value not in VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM:
            return (
                False,
                f"Invalid dhcp-settings-from-fortiipam '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM)}",
            )

    # Validate auto-managed-status if present
    if "auto-managed-status" in payload:
        value = payload.get("auto-managed-status")
        if value and value not in VALID_BODY_AUTO_MANAGED_STATUS:
            return (
                False,
                f"Invalid auto-managed-status '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_MANAGED_STATUS)}",
            )

    # Validate ddns-update if present
    if "ddns-update" in payload:
        value = payload.get("ddns-update")
        if value and value not in VALID_BODY_DDNS_UPDATE:
            return (
                False,
                f"Invalid ddns-update '{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_UPDATE)}",
            )

    # Validate ddns-update-override if present
    if "ddns-update-override" in payload:
        value = payload.get("ddns-update-override")
        if value and value not in VALID_BODY_DDNS_UPDATE_OVERRIDE:
            return (
                False,
                f"Invalid ddns-update-override '{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_UPDATE_OVERRIDE)}",
            )

    # Validate ddns-zone if present
    if "ddns-zone" in payload:
        value = payload.get("ddns-zone")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-zone cannot exceed 64 characters")

    # Validate ddns-auth if present
    if "ddns-auth" in payload:
        value = payload.get("ddns-auth")
        if value and value not in VALID_BODY_DDNS_AUTH:
            return (
                False,
                f"Invalid ddns-auth '{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_AUTH)}",
            )

    # Validate ddns-keyname if present
    if "ddns-keyname" in payload:
        value = payload.get("ddns-keyname")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-keyname cannot exceed 64 characters")

    # Validate ddns-ttl if present
    if "ddns-ttl" in payload:
        value = payload.get("ddns-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 86400:
                    return (False, "ddns-ttl must be between 60 and 86400")
            except (ValueError, TypeError):
                return (False, f"ddns-ttl must be numeric, got: {value}")

    # Validate vci-match if present
    if "vci-match" in payload:
        value = payload.get("vci-match")
        if value and value not in VALID_BODY_VCI_MATCH:
            return (
                False,
                f"Invalid vci-match '{value}'. Must be one of: {', '.join(VALID_BODY_VCI_MATCH)}",
            )

    # Validate shared-subnet if present
    if "shared-subnet" in payload:
        value = payload.get("shared-subnet")
        if value and value not in VALID_BODY_SHARED_SUBNET:
            return (
                False,
                f"Invalid shared-subnet '{value}'. Must be one of: {', '.join(VALID_BODY_SHARED_SUBNET)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_dhcp_server_put(
    id: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        id: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # id is required for updates
    if not id:
        return (False, "id is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate lease-time if present
    if "lease-time" in payload:
        value = payload.get("lease-time")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 300 or int_val > 8640000:
                    return (
                        False,
                        "lease-time must be between 300 and 8640000",
                    )
            except (ValueError, TypeError):
                return (False, f"lease-time must be numeric, got: {value}")

    # Validate mac-acl-default-action if present
    if "mac-acl-default-action" in payload:
        value = payload.get("mac-acl-default-action")
        if value and value not in VALID_BODY_MAC_ACL_DEFAULT_ACTION:
            return (
                False,
                f"Invalid mac-acl-default-action '{value}'. Must be one of: {', '.join(VALID_BODY_MAC_ACL_DEFAULT_ACTION)}",
            )

    # Validate forticlient-on-net-status if present
    if "forticlient-on-net-status" in payload:
        value = payload.get("forticlient-on-net-status")
        if value and value not in VALID_BODY_FORTICLIENT_ON_NET_STATUS:
            return (
                False,
                f"Invalid forticlient-on-net-status '{value}'. Must be one of: {', '.join(VALID_BODY_FORTICLIENT_ON_NET_STATUS)}",
            )

    # Validate dns-service if present
    if "dns-service" in payload:
        value = payload.get("dns-service")
        if value and value not in VALID_BODY_DNS_SERVICE:
            return (
                False,
                f"Invalid dns-service '{value}'. Must be one of: {', '.join(VALID_BODY_DNS_SERVICE)}",
            )

    # Validate wifi-ac-service if present
    if "wifi-ac-service" in payload:
        value = payload.get("wifi-ac-service")
        if value and value not in VALID_BODY_WIFI_AC_SERVICE:
            return (
                False,
                f"Invalid wifi-ac-service '{value}'. Must be one of: {', '.join(VALID_BODY_WIFI_AC_SERVICE)}",
            )

    # Validate ntp-service if present
    if "ntp-service" in payload:
        value = payload.get("ntp-service")
        if value and value not in VALID_BODY_NTP_SERVICE:
            return (
                False,
                f"Invalid ntp-service '{value}'. Must be one of: {', '.join(VALID_BODY_NTP_SERVICE)}",
            )

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "domain cannot exceed 35 characters")

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate timezone-option if present
    if "timezone-option" in payload:
        value = payload.get("timezone-option")
        if value and value not in VALID_BODY_TIMEZONE_OPTION:
            return (
                False,
                f"Invalid timezone-option '{value}'. Must be one of: {', '.join(VALID_BODY_TIMEZONE_OPTION)}",
            )

    # Validate timezone if present
    if "timezone" in payload:
        value = payload.get("timezone")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "timezone cannot exceed 63 characters")

    # Validate filename if present
    if "filename" in payload:
        value = payload.get("filename")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "filename cannot exceed 127 characters")

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate ip-mode if present
    if "ip-mode" in payload:
        value = payload.get("ip-mode")
        if value and value not in VALID_BODY_IP_MODE:
            return (
                False,
                f"Invalid ip-mode '{value}'. Must be one of: {', '.join(VALID_BODY_IP_MODE)}",
            )

    # Validate conflicted-ip-timeout if present
    if "conflicted-ip-timeout" in payload:
        value = payload.get("conflicted-ip-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 8640000:
                    return (
                        False,
                        "conflicted-ip-timeout must be between 60 and 8640000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"conflicted-ip-timeout must be numeric, got: {value}",
                )

    # Validate ipsec-lease-hold if present
    if "ipsec-lease-hold" in payload:
        value = payload.get("ipsec-lease-hold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 8640000:
                    return (
                        False,
                        "ipsec-lease-hold must be between 0 and 8640000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ipsec-lease-hold must be numeric, got: {value}",
                )

    # Validate auto-configuration if present
    if "auto-configuration" in payload:
        value = payload.get("auto-configuration")
        if value and value not in VALID_BODY_AUTO_CONFIGURATION:
            return (
                False,
                f"Invalid auto-configuration '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_CONFIGURATION)}",
            )

    # Validate dhcp-settings-from-fortiipam if present
    if "dhcp-settings-from-fortiipam" in payload:
        value = payload.get("dhcp-settings-from-fortiipam")
        if value and value not in VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM:
            return (
                False,
                f"Invalid dhcp-settings-from-fortiipam '{value}'. Must be one of: {', '.join(VALID_BODY_DHCP_SETTINGS_FROM_FORTIIPAM)}",
            )

    # Validate auto-managed-status if present
    if "auto-managed-status" in payload:
        value = payload.get("auto-managed-status")
        if value and value not in VALID_BODY_AUTO_MANAGED_STATUS:
            return (
                False,
                f"Invalid auto-managed-status '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_MANAGED_STATUS)}",
            )

    # Validate ddns-update if present
    if "ddns-update" in payload:
        value = payload.get("ddns-update")
        if value and value not in VALID_BODY_DDNS_UPDATE:
            return (
                False,
                f"Invalid ddns-update '{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_UPDATE)}",
            )

    # Validate ddns-update-override if present
    if "ddns-update-override" in payload:
        value = payload.get("ddns-update-override")
        if value and value not in VALID_BODY_DDNS_UPDATE_OVERRIDE:
            return (
                False,
                f"Invalid ddns-update-override '{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_UPDATE_OVERRIDE)}",
            )

    # Validate ddns-zone if present
    if "ddns-zone" in payload:
        value = payload.get("ddns-zone")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-zone cannot exceed 64 characters")

    # Validate ddns-auth if present
    if "ddns-auth" in payload:
        value = payload.get("ddns-auth")
        if value and value not in VALID_BODY_DDNS_AUTH:
            return (
                False,
                f"Invalid ddns-auth '{value}'. Must be one of: {', '.join(VALID_BODY_DDNS_AUTH)}",
            )

    # Validate ddns-keyname if present
    if "ddns-keyname" in payload:
        value = payload.get("ddns-keyname")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "ddns-keyname cannot exceed 64 characters")

    # Validate ddns-ttl if present
    if "ddns-ttl" in payload:
        value = payload.get("ddns-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 86400:
                    return (False, "ddns-ttl must be between 60 and 86400")
            except (ValueError, TypeError):
                return (False, f"ddns-ttl must be numeric, got: {value}")

    # Validate vci-match if present
    if "vci-match" in payload:
        value = payload.get("vci-match")
        if value and value not in VALID_BODY_VCI_MATCH:
            return (
                False,
                f"Invalid vci-match '{value}'. Must be one of: {', '.join(VALID_BODY_VCI_MATCH)}",
            )

    # Validate shared-subnet if present
    if "shared-subnet" in payload:
        value = payload.get("shared-subnet")
        if value and value not in VALID_BODY_SHARED_SUBNET:
            return (
                False,
                f"Invalid shared-subnet '{value}'. Must be one of: {', '.join(VALID_BODY_SHARED_SUBNET)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_dhcp_server_delete(
    id: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        id: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not id:
        return (False, "id is required for DELETE operation")

    return (True, None)
