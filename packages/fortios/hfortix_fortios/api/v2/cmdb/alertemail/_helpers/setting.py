"""
Validation helpers for alertemail setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FILTER_MODE = ["category", "threshold"]
VALID_BODY_IPS_LOGS = ["enable", "disable"]
VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS = ["enable", "disable"]
VALID_BODY_HA_LOGS = ["enable", "disable"]
VALID_BODY_IPSEC_ERRORS_LOGS = ["enable", "disable"]
VALID_BODY_FDS_UPDATE_LOGS = ["enable", "disable"]
VALID_BODY_PPP_ERRORS_LOGS = ["enable", "disable"]
VALID_BODY_ANTIVIRUS_LOGS = ["enable", "disable"]
VALID_BODY_WEBFILTER_LOGS = ["enable", "disable"]
VALID_BODY_CONFIGURATION_CHANGES_LOGS = ["enable", "disable"]
VALID_BODY_VIOLATION_TRAFFIC_LOGS = ["enable", "disable"]
VALID_BODY_ADMIN_LOGIN_LOGS = ["enable", "disable"]
VALID_BODY_FDS_LICENSE_EXPIRING_WARNING = ["enable", "disable"]
VALID_BODY_LOG_DISK_USAGE_WARNING = ["enable", "disable"]
VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING = ["enable", "disable"]
VALID_BODY_AMC_INTERFACE_BYPASS_MODE = ["enable", "disable"]
VALID_BODY_FIPS_CC_ERRORS = ["enable", "disable"]
VALID_BODY_FSSO_DISCONNECT_LOGS = ["enable", "disable"]
VALID_BODY_SSH_LOGS = ["enable", "disable"]
VALID_BODY_SEVERITY = [
    "emergency",
    "alert",
    "critical",
    "error",
    "warning",
    "notification",
    "information",
    "debug",
]
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

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "username cannot exceed 63 characters")

    # Validate mailto1 if present
    if "mailto1" in payload:
        value = payload.get("mailto1")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "mailto1 cannot exceed 63 characters")

    # Validate mailto2 if present
    if "mailto2" in payload:
        value = payload.get("mailto2")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "mailto2 cannot exceed 63 characters")

    # Validate mailto3 if present
    if "mailto3" in payload:
        value = payload.get("mailto3")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "mailto3 cannot exceed 63 characters")

    # Validate filter-mode if present
    if "filter-mode" in payload:
        value = payload.get("filter-mode")
        if value and value not in VALID_BODY_FILTER_MODE:
            return (
                False,
                f"Invalid filter-mode '{value}'. Must be one of: {', '.join(VALID_BODY_FILTER_MODE)}",
            )

    # Validate email-interval if present
    if "email-interval" in payload:
        value = payload.get("email-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "email-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (False, f"email-interval must be numeric, got: {value}")

    # Validate IPS-logs if present
    if "IPS-logs" in payload:
        value = payload.get("IPS-logs")
        if value and value not in VALID_BODY_IPS_LOGS:
            return (
                False,
                f"Invalid IPS-logs '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_LOGS)}",
            )

    # Validate firewall-authentication-failure-logs if present
    if "firewall-authentication-failure-logs" in payload:
        value = payload.get("firewall-authentication-failure-logs")
        if (
            value
            and value not in VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS
        ):
            return (
                False,
                f"Invalid firewall-authentication-failure-logs '{value}'. Must be one of: {', '.join(VALID_BODY_FIREWALL_AUTHENTICATION_FAILURE_LOGS)}",
            )

    # Validate HA-logs if present
    if "HA-logs" in payload:
        value = payload.get("HA-logs")
        if value and value not in VALID_BODY_HA_LOGS:
            return (
                False,
                f"Invalid HA-logs '{value}'. Must be one of: {', '.join(VALID_BODY_HA_LOGS)}",
            )

    # Validate IPsec-errors-logs if present
    if "IPsec-errors-logs" in payload:
        value = payload.get("IPsec-errors-logs")
        if value and value not in VALID_BODY_IPSEC_ERRORS_LOGS:
            return (
                False,
                f"Invalid IPsec-errors-logs '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_ERRORS_LOGS)}",
            )

    # Validate FDS-update-logs if present
    if "FDS-update-logs" in payload:
        value = payload.get("FDS-update-logs")
        if value and value not in VALID_BODY_FDS_UPDATE_LOGS:
            return (
                False,
                f"Invalid FDS-update-logs '{value}'. Must be one of: {', '.join(VALID_BODY_FDS_UPDATE_LOGS)}",
            )

    # Validate PPP-errors-logs if present
    if "PPP-errors-logs" in payload:
        value = payload.get("PPP-errors-logs")
        if value and value not in VALID_BODY_PPP_ERRORS_LOGS:
            return (
                False,
                f"Invalid PPP-errors-logs '{value}'. Must be one of: {', '.join(VALID_BODY_PPP_ERRORS_LOGS)}",
            )

    # Validate antivirus-logs if present
    if "antivirus-logs" in payload:
        value = payload.get("antivirus-logs")
        if value and value not in VALID_BODY_ANTIVIRUS_LOGS:
            return (
                False,
                f"Invalid antivirus-logs '{value}'. Must be one of: {', '.join(VALID_BODY_ANTIVIRUS_LOGS)}",
            )

    # Validate webfilter-logs if present
    if "webfilter-logs" in payload:
        value = payload.get("webfilter-logs")
        if value and value not in VALID_BODY_WEBFILTER_LOGS:
            return (
                False,
                f"Invalid webfilter-logs '{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_LOGS)}",
            )

    # Validate configuration-changes-logs if present
    if "configuration-changes-logs" in payload:
        value = payload.get("configuration-changes-logs")
        if value and value not in VALID_BODY_CONFIGURATION_CHANGES_LOGS:
            return (
                False,
                f"Invalid configuration-changes-logs '{value}'. Must be one of: {', '.join(VALID_BODY_CONFIGURATION_CHANGES_LOGS)}",
            )

    # Validate violation-traffic-logs if present
    if "violation-traffic-logs" in payload:
        value = payload.get("violation-traffic-logs")
        if value and value not in VALID_BODY_VIOLATION_TRAFFIC_LOGS:
            return (
                False,
                f"Invalid violation-traffic-logs '{value}'. Must be one of: {', '.join(VALID_BODY_VIOLATION_TRAFFIC_LOGS)}",
            )

    # Validate admin-login-logs if present
    if "admin-login-logs" in payload:
        value = payload.get("admin-login-logs")
        if value and value not in VALID_BODY_ADMIN_LOGIN_LOGS:
            return (
                False,
                f"Invalid admin-login-logs '{value}'. Must be one of: {', '.join(VALID_BODY_ADMIN_LOGIN_LOGS)}",
            )

    # Validate FDS-license-expiring-warning if present
    if "FDS-license-expiring-warning" in payload:
        value = payload.get("FDS-license-expiring-warning")
        if value and value not in VALID_BODY_FDS_LICENSE_EXPIRING_WARNING:
            return (
                False,
                f"Invalid FDS-license-expiring-warning '{value}'. Must be one of: {', '.join(VALID_BODY_FDS_LICENSE_EXPIRING_WARNING)}",
            )

    # Validate log-disk-usage-warning if present
    if "log-disk-usage-warning" in payload:
        value = payload.get("log-disk-usage-warning")
        if value and value not in VALID_BODY_LOG_DISK_USAGE_WARNING:
            return (
                False,
                f"Invalid log-disk-usage-warning '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_DISK_USAGE_WARNING)}",
            )

    # Validate fortiguard-log-quota-warning if present
    if "fortiguard-log-quota-warning" in payload:
        value = payload.get("fortiguard-log-quota-warning")
        if value and value not in VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING:
            return (
                False,
                f"Invalid fortiguard-log-quota-warning '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIGUARD_LOG_QUOTA_WARNING)}",
            )

    # Validate amc-interface-bypass-mode if present
    if "amc-interface-bypass-mode" in payload:
        value = payload.get("amc-interface-bypass-mode")
        if value and value not in VALID_BODY_AMC_INTERFACE_BYPASS_MODE:
            return (
                False,
                f"Invalid amc-interface-bypass-mode '{value}'. Must be one of: {', '.join(VALID_BODY_AMC_INTERFACE_BYPASS_MODE)}",
            )

    # Validate FIPS-CC-errors if present
    if "FIPS-CC-errors" in payload:
        value = payload.get("FIPS-CC-errors")
        if value and value not in VALID_BODY_FIPS_CC_ERRORS:
            return (
                False,
                f"Invalid FIPS-CC-errors '{value}'. Must be one of: {', '.join(VALID_BODY_FIPS_CC_ERRORS)}",
            )

    # Validate FSSO-disconnect-logs if present
    if "FSSO-disconnect-logs" in payload:
        value = payload.get("FSSO-disconnect-logs")
        if value and value not in VALID_BODY_FSSO_DISCONNECT_LOGS:
            return (
                False,
                f"Invalid FSSO-disconnect-logs '{value}'. Must be one of: {', '.join(VALID_BODY_FSSO_DISCONNECT_LOGS)}",
            )

    # Validate ssh-logs if present
    if "ssh-logs" in payload:
        value = payload.get("ssh-logs")
        if value and value not in VALID_BODY_SSH_LOGS:
            return (
                False,
                f"Invalid ssh-logs '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_LOGS)}",
            )

    # Validate local-disk-usage if present
    if "local-disk-usage" in payload:
        value = payload.get("local-disk-usage")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99:
                    return (
                        False,
                        "local-disk-usage must be between 1 and 99",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"local-disk-usage must be numeric, got: {value}",
                )

    # Validate emergency-interval if present
    if "emergency-interval" in payload:
        value = payload.get("emergency-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "emergency-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"emergency-interval must be numeric, got: {value}",
                )

    # Validate alert-interval if present
    if "alert-interval" in payload:
        value = payload.get("alert-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "alert-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (False, f"alert-interval must be numeric, got: {value}")

    # Validate critical-interval if present
    if "critical-interval" in payload:
        value = payload.get("critical-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "critical-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"critical-interval must be numeric, got: {value}",
                )

    # Validate error-interval if present
    if "error-interval" in payload:
        value = payload.get("error-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "error-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (False, f"error-interval must be numeric, got: {value}")

    # Validate warning-interval if present
    if "warning-interval" in payload:
        value = payload.get("warning-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "warning-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"warning-interval must be numeric, got: {value}",
                )

    # Validate notification-interval if present
    if "notification-interval" in payload:
        value = payload.get("notification-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "notification-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"notification-interval must be numeric, got: {value}",
                )

    # Validate information-interval if present
    if "information-interval" in payload:
        value = payload.get("information-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "information-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"information-interval must be numeric, got: {value}",
                )

    # Validate debug-interval if present
    if "debug-interval" in payload:
        value = payload.get("debug-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 99999:
                    return (
                        False,
                        "debug-interval must be between 1 and 99999",
                    )
            except (ValueError, TypeError):
                return (False, f"debug-interval must be numeric, got: {value}")

    # Validate severity if present
    if "severity" in payload:
        value = payload.get("severity")
        if value and value not in VALID_BODY_SEVERITY:
            return (
                False,
                f"Invalid severity '{value}'. Must be one of: {', '.join(VALID_BODY_SEVERITY)}",
            )

    return (True, None)
