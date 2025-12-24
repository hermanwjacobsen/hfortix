"""
Validation helpers for log disk_setting endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_IPS_ARCHIVE = ["enable", "disable"]
VALID_BODY_ROLL_SCHEDULE = ["daily", "weekly"]
VALID_BODY_ROLL_DAY = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]
VALID_BODY_DISKFULL = ["overwrite", "nolog"]
VALID_BODY_UPLOAD = ["enable", "disable"]
VALID_BODY_UPLOAD_DESTINATION = ["ftp-server"]
VALID_BODY_UPLOADTYPE = [
    "traffic",
    "event",
    "virus",
    "webfilter",
    "IPS",
    "emailfilter",
    "dlp-archive",
    "anomaly",
    "voip",
    "dlp",
    "app-ctrl",
    "wa",
    "dns",
    "ssh",
    "ssl",
    "file-filter",
    "icap",
    "virtual-patch",
    "debug",
]
VALID_BODY_UPLOADSCHED = ["disable", "enable"]
VALID_BODY_UPLOAD_DELETE_FILES = ["enable", "disable"]
VALID_BODY_UPLOAD_SSL_CONN = ["default", "high", "low", "disable"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_disk_setting_get(
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


def validate_disk_setting_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate ips-archive if present
    if "ips-archive" in payload:
        value = payload.get("ips-archive")
        if value and value not in VALID_BODY_IPS_ARCHIVE:
            return (
                False,
                f"Invalid ips-archive '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_ARCHIVE)}",
            )

    # Validate max-log-file-size if present
    if "max-log-file-size" in payload:
        value = payload.get("max-log-file-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 100:
                    return (
                        False,
                        "max-log-file-size must be between 1 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-log-file-size must be numeric, got: {value}",
                )

    # Validate max-policy-packet-capture-size if present
    if "max-policy-packet-capture-size" in payload:
        value = payload.get("max-policy-packet-capture-size")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "max-policy-packet-capture-size must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-policy-packet-capture-size must be numeric, got: {value}",
                )

    # Validate roll-schedule if present
    if "roll-schedule" in payload:
        value = payload.get("roll-schedule")
        if value and value not in VALID_BODY_ROLL_SCHEDULE:
            return (
                False,
                f"Invalid roll-schedule '{value}'. Must be one of: {', '.join(VALID_BODY_ROLL_SCHEDULE)}",
            )

    # Validate roll-day if present
    if "roll-day" in payload:
        value = payload.get("roll-day")
        if value and value not in VALID_BODY_ROLL_DAY:
            return (
                False,
                f"Invalid roll-day '{value}'. Must be one of: {', '.join(VALID_BODY_ROLL_DAY)}",
            )

    # Validate diskfull if present
    if "diskfull" in payload:
        value = payload.get("diskfull")
        if value and value not in VALID_BODY_DISKFULL:
            return (
                False,
                f"Invalid diskfull '{value}'. Must be one of: {', '.join(VALID_BODY_DISKFULL)}",
            )

    # Validate log-quota if present
    if "log-quota" in payload:
        value = payload.get("log-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "log-quota must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"log-quota must be numeric, got: {value}")

    # Validate dlp-archive-quota if present
    if "dlp-archive-quota" in payload:
        value = payload.get("dlp-archive-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "dlp-archive-quota must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dlp-archive-quota must be numeric, got: {value}",
                )

    # Validate report-quota if present
    if "report-quota" in payload:
        value = payload.get("report-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "report-quota must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"report-quota must be numeric, got: {value}")

    # Validate maximum-log-age if present
    if "maximum-log-age" in payload:
        value = payload.get("maximum-log-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3650:
                    return (
                        False,
                        "maximum-log-age must be between 0 and 3650",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"maximum-log-age must be numeric, got: {value}",
                )

    # Validate upload if present
    if "upload" in payload:
        value = payload.get("upload")
        if value and value not in VALID_BODY_UPLOAD:
            return (
                False,
                f"Invalid upload '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD)}",
            )

    # Validate upload-destination if present
    if "upload-destination" in payload:
        value = payload.get("upload-destination")
        if value and value not in VALID_BODY_UPLOAD_DESTINATION:
            return (
                False,
                f"Invalid upload-destination '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_DESTINATION)}",
            )

    # Validate uploadport if present
    if "uploadport" in payload:
        value = payload.get("uploadport")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "uploadport must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"uploadport must be numeric, got: {value}")

    # Validate uploaduser if present
    if "uploaduser" in payload:
        value = payload.get("uploaduser")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "uploaduser cannot exceed 35 characters")

    # Validate uploaddir if present
    if "uploaddir" in payload:
        value = payload.get("uploaddir")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "uploaddir cannot exceed 63 characters")

    # Validate uploadtype if present
    if "uploadtype" in payload:
        value = payload.get("uploadtype")
        if value and value not in VALID_BODY_UPLOADTYPE:
            return (
                False,
                f"Invalid uploadtype '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOADTYPE)}",
            )

    # Validate uploadsched if present
    if "uploadsched" in payload:
        value = payload.get("uploadsched")
        if value and value not in VALID_BODY_UPLOADSCHED:
            return (
                False,
                f"Invalid uploadsched '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOADSCHED)}",
            )

    # Validate upload-delete-files if present
    if "upload-delete-files" in payload:
        value = payload.get("upload-delete-files")
        if value and value not in VALID_BODY_UPLOAD_DELETE_FILES:
            return (
                False,
                f"Invalid upload-delete-files '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_DELETE_FILES)}",
            )

    # Validate upload-ssl-conn if present
    if "upload-ssl-conn" in payload:
        value = payload.get("upload-ssl-conn")
        if value and value not in VALID_BODY_UPLOAD_SSL_CONN:
            return (
                False,
                f"Invalid upload-ssl-conn '{value}'. Must be one of: {', '.join(VALID_BODY_UPLOAD_SSL_CONN)}",
            )

    # Validate full-first-warning-threshold if present
    if "full-first-warning-threshold" in payload:
        value = payload.get("full-first-warning-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 98:
                    return (
                        False,
                        "full-first-warning-threshold must be between 1 and 98",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"full-first-warning-threshold must be numeric, got: {value}",
                )

    # Validate full-second-warning-threshold if present
    if "full-second-warning-threshold" in payload:
        value = payload.get("full-second-warning-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 2 or int_val > 99:
                    return (
                        False,
                        "full-second-warning-threshold must be between 2 and 99",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"full-second-warning-threshold must be numeric, got: {value}",
                )

    # Validate full-final-warning-threshold if present
    if "full-final-warning-threshold" in payload:
        value = payload.get("full-final-warning-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 3 or int_val > 100:
                    return (
                        False,
                        "full-final-warning-threshold must be between 3 and 100",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"full-final-warning-threshold must be numeric, got: {value}",
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
