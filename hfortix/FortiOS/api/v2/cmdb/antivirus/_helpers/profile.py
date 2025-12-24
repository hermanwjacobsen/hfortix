"""
Validation helpers for antivirus profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = ["flow", "proxy"]
VALID_BODY_FORTISANDBOX_MODE = ["analytics-suspicious", "analytics-everything"]
VALID_BODY_ANALYTICS_DB = ["disable", "enable"]
VALID_BODY_MOBILE_MALWARE_DB = ["disable", "enable"]
VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN = ["disable", "enable"]
VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL = ["disable", "enable"]
VALID_BODY_EMS_THREAT_FEED = ["disable", "enable"]
VALID_BODY_AV_VIRUS_LOG = ["enable", "disable"]
VALID_BODY_EXTENDED_LOG = ["enable", "disable"]
VALID_BODY_SCAN_MODE = ["default", "legacy"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_profile_get(
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


def validate_profile_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating profile.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate feature-set if present
    if "feature-set" in payload:
        value = payload.get("feature-set")
        if value and value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid feature-set '{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )

    # Validate fortisandbox-mode if present
    if "fortisandbox-mode" in payload:
        value = payload.get("fortisandbox-mode")
        if value and value not in VALID_BODY_FORTISANDBOX_MODE:
            return (
                False,
                f"Invalid fortisandbox-mode '{value}'. Must be one of: {', '.join(VALID_BODY_FORTISANDBOX_MODE)}",
            )

    # Validate fortisandbox-max-upload if present
    if "fortisandbox-max-upload" in payload:
        value = payload.get("fortisandbox-max-upload")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 193:
                    return (
                        False,
                        "fortisandbox-max-upload must be between 1 and 193",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fortisandbox-max-upload must be numeric, got: {value}",
                )

    # Validate analytics-ignore-filetype if present
    if "analytics-ignore-filetype" in payload:
        value = payload.get("analytics-ignore-filetype")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "analytics-ignore-filetype must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"analytics-ignore-filetype must be numeric, got: {value}",
                )

    # Validate analytics-accept-filetype if present
    if "analytics-accept-filetype" in payload:
        value = payload.get("analytics-accept-filetype")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "analytics-accept-filetype must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"analytics-accept-filetype must be numeric, got: {value}",
                )

    # Validate analytics-db if present
    if "analytics-db" in payload:
        value = payload.get("analytics-db")
        if value and value not in VALID_BODY_ANALYTICS_DB:
            return (
                False,
                f"Invalid analytics-db '{value}'. Must be one of: {', '.join(VALID_BODY_ANALYTICS_DB)}",
            )

    # Validate mobile-malware-db if present
    if "mobile-malware-db" in payload:
        value = payload.get("mobile-malware-db")
        if value and value not in VALID_BODY_MOBILE_MALWARE_DB:
            return (
                False,
                f"Invalid mobile-malware-db '{value}'. Must be one of: {', '.join(VALID_BODY_MOBILE_MALWARE_DB)}",
            )

    # Validate outbreak-prevention-archive-scan if present
    if "outbreak-prevention-archive-scan" in payload:
        value = payload.get("outbreak-prevention-archive-scan")
        if value and value not in VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN:
            return (
                False,
                f"Invalid outbreak-prevention-archive-scan '{value}'. Must be one of: {', '.join(VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN)}",
            )

    # Validate external-blocklist-enable-all if present
    if "external-blocklist-enable-all" in payload:
        value = payload.get("external-blocklist-enable-all")
        if value and value not in VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL:
            return (
                False,
                f"Invalid external-blocklist-enable-all '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL)}",
            )

    # Validate ems-threat-feed if present
    if "ems-threat-feed" in payload:
        value = payload.get("ems-threat-feed")
        if value and value not in VALID_BODY_EMS_THREAT_FEED:
            return (
                False,
                f"Invalid ems-threat-feed '{value}'. Must be one of: {', '.join(VALID_BODY_EMS_THREAT_FEED)}",
            )

    # Validate av-virus-log if present
    if "av-virus-log" in payload:
        value = payload.get("av-virus-log")
        if value and value not in VALID_BODY_AV_VIRUS_LOG:
            return (
                False,
                f"Invalid av-virus-log '{value}'. Must be one of: {', '.join(VALID_BODY_AV_VIRUS_LOG)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate scan-mode if present
    if "scan-mode" in payload:
        value = payload.get("scan-mode")
        if value and value not in VALID_BODY_SCAN_MODE:
            return (
                False,
                f"Invalid scan-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_MODE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_profile_put(
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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate feature-set if present
    if "feature-set" in payload:
        value = payload.get("feature-set")
        if value and value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid feature-set '{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )

    # Validate fortisandbox-mode if present
    if "fortisandbox-mode" in payload:
        value = payload.get("fortisandbox-mode")
        if value and value not in VALID_BODY_FORTISANDBOX_MODE:
            return (
                False,
                f"Invalid fortisandbox-mode '{value}'. Must be one of: {', '.join(VALID_BODY_FORTISANDBOX_MODE)}",
            )

    # Validate fortisandbox-max-upload if present
    if "fortisandbox-max-upload" in payload:
        value = payload.get("fortisandbox-max-upload")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 193:
                    return (
                        False,
                        "fortisandbox-max-upload must be between 1 and 193",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"fortisandbox-max-upload must be numeric, got: {value}",
                )

    # Validate analytics-ignore-filetype if present
    if "analytics-ignore-filetype" in payload:
        value = payload.get("analytics-ignore-filetype")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "analytics-ignore-filetype must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"analytics-ignore-filetype must be numeric, got: {value}",
                )

    # Validate analytics-accept-filetype if present
    if "analytics-accept-filetype" in payload:
        value = payload.get("analytics-accept-filetype")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "analytics-accept-filetype must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"analytics-accept-filetype must be numeric, got: {value}",
                )

    # Validate analytics-db if present
    if "analytics-db" in payload:
        value = payload.get("analytics-db")
        if value and value not in VALID_BODY_ANALYTICS_DB:
            return (
                False,
                f"Invalid analytics-db '{value}'. Must be one of: {', '.join(VALID_BODY_ANALYTICS_DB)}",
            )

    # Validate mobile-malware-db if present
    if "mobile-malware-db" in payload:
        value = payload.get("mobile-malware-db")
        if value and value not in VALID_BODY_MOBILE_MALWARE_DB:
            return (
                False,
                f"Invalid mobile-malware-db '{value}'. Must be one of: {', '.join(VALID_BODY_MOBILE_MALWARE_DB)}",
            )

    # Validate outbreak-prevention-archive-scan if present
    if "outbreak-prevention-archive-scan" in payload:
        value = payload.get("outbreak-prevention-archive-scan")
        if value and value not in VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN:
            return (
                False,
                f"Invalid outbreak-prevention-archive-scan '{value}'. Must be one of: {', '.join(VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN)}",
            )

    # Validate external-blocklist-enable-all if present
    if "external-blocklist-enable-all" in payload:
        value = payload.get("external-blocklist-enable-all")
        if value and value not in VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL:
            return (
                False,
                f"Invalid external-blocklist-enable-all '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL)}",
            )

    # Validate ems-threat-feed if present
    if "ems-threat-feed" in payload:
        value = payload.get("ems-threat-feed")
        if value and value not in VALID_BODY_EMS_THREAT_FEED:
            return (
                False,
                f"Invalid ems-threat-feed '{value}'. Must be one of: {', '.join(VALID_BODY_EMS_THREAT_FEED)}",
            )

    # Validate av-virus-log if present
    if "av-virus-log" in payload:
        value = payload.get("av-virus-log")
        if value and value not in VALID_BODY_AV_VIRUS_LOG:
            return (
                False,
                f"Invalid av-virus-log '{value}'. Must be one of: {', '.join(VALID_BODY_AV_VIRUS_LOG)}",
            )

    # Validate extended-log if present
    if "extended-log" in payload:
        value = payload.get("extended-log")
        if value and value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid extended-log '{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )

    # Validate scan-mode if present
    if "scan-mode" in payload:
        value = payload.get("scan-mode")
        if value and value not in VALID_BODY_SCAN_MODE:
            return (
                False,
                f"Invalid scan-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_MODE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_profile_delete(
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
