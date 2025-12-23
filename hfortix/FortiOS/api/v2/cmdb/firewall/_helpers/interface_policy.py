"""
Validation helpers for firewall interface_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_LOGTRAFFIC = ["all", "utm", "disable"]
VALID_BODY_APPLICATION_LIST_STATUS = ["enable", "disable"]
VALID_BODY_IPS_SENSOR_STATUS = ["enable", "disable"]
VALID_BODY_DSRI = ["enable", "disable"]
VALID_BODY_AV_PROFILE_STATUS = ["enable", "disable"]
VALID_BODY_WEBFILTER_PROFILE_STATUS = ["enable", "disable"]
VALID_BODY_CASB_PROFILE_STATUS = ["enable", "disable"]
VALID_BODY_EMAILFILTER_PROFILE_STATUS = ["enable", "disable"]
VALID_BODY_DLP_PROFILE_STATUS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_interface_policy_get(
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


def validate_interface_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating interface_policy.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate application-list-status if present
    if "application-list-status" in payload:
        value = payload.get("application-list-status")
        if value and value not in VALID_BODY_APPLICATION_LIST_STATUS:
            return (
                False,
                f"Invalid application-list-status '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_LIST_STATUS)}",
            )

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate ips-sensor-status if present
    if "ips-sensor-status" in payload:
        value = payload.get("ips-sensor-status")
        if value and value not in VALID_BODY_IPS_SENSOR_STATUS:
            return (
                False,
                f"Invalid ips-sensor-status '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SENSOR_STATUS)}",
            )

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate dsri if present
    if "dsri" in payload:
        value = payload.get("dsri")
        if value and value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid dsri '{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )

    # Validate av-profile-status if present
    if "av-profile-status" in payload:
        value = payload.get("av-profile-status")
        if value and value not in VALID_BODY_AV_PROFILE_STATUS:
            return (
                False,
                f"Invalid av-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_AV_PROFILE_STATUS)}",
            )

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile-status if present
    if "webfilter-profile-status" in payload:
        value = payload.get("webfilter-profile-status")
        if value and value not in VALID_BODY_WEBFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid webfilter-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_PROFILE_STATUS)}",
            )

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate casb-profile-status if present
    if "casb-profile-status" in payload:
        value = payload.get("casb-profile-status")
        if value and value not in VALID_BODY_CASB_PROFILE_STATUS:
            return (
                False,
                f"Invalid casb-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_CASB_PROFILE_STATUS)}",
            )

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    # Validate emailfilter-profile-status if present
    if "emailfilter-profile-status" in payload:
        value = payload.get("emailfilter-profile-status")
        if value and value not in VALID_BODY_EMAILFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid emailfilter-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_EMAILFILTER_PROFILE_STATUS)}",
            )

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile-status if present
    if "dlp-profile-status" in payload:
        value = payload.get("dlp-profile-status")
        if value and value not in VALID_BODY_DLP_PROFILE_STATUS:
            return (
                False,
                f"Invalid dlp-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_DLP_PROFILE_STATUS)}",
            )

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_interface_policy_put(
    policyid: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        policyid: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # policyid is required for updates
    if not policyid:
        return (False, "policyid is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate policyid if present
    if "policyid" in payload:
        value = payload.get("policyid")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "policyid must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "interface cannot exceed 35 characters")

    # Validate application-list-status if present
    if "application-list-status" in payload:
        value = payload.get("application-list-status")
        if value and value not in VALID_BODY_APPLICATION_LIST_STATUS:
            return (
                False,
                f"Invalid application-list-status '{value}'. Must be one of: {', '.join(VALID_BODY_APPLICATION_LIST_STATUS)}",
            )

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate ips-sensor-status if present
    if "ips-sensor-status" in payload:
        value = payload.get("ips-sensor-status")
        if value and value not in VALID_BODY_IPS_SENSOR_STATUS:
            return (
                False,
                f"Invalid ips-sensor-status '{value}'. Must be one of: {', '.join(VALID_BODY_IPS_SENSOR_STATUS)}",
            )

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate dsri if present
    if "dsri" in payload:
        value = payload.get("dsri")
        if value and value not in VALID_BODY_DSRI:
            return (
                False,
                f"Invalid dsri '{value}'. Must be one of: {', '.join(VALID_BODY_DSRI)}",
            )

    # Validate av-profile-status if present
    if "av-profile-status" in payload:
        value = payload.get("av-profile-status")
        if value and value not in VALID_BODY_AV_PROFILE_STATUS:
            return (
                False,
                f"Invalid av-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_AV_PROFILE_STATUS)}",
            )

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile-status if present
    if "webfilter-profile-status" in payload:
        value = payload.get("webfilter-profile-status")
        if value and value not in VALID_BODY_WEBFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid webfilter-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_WEBFILTER_PROFILE_STATUS)}",
            )

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate casb-profile-status if present
    if "casb-profile-status" in payload:
        value = payload.get("casb-profile-status")
        if value and value not in VALID_BODY_CASB_PROFILE_STATUS:
            return (
                False,
                f"Invalid casb-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_CASB_PROFILE_STATUS)}",
            )

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    # Validate emailfilter-profile-status if present
    if "emailfilter-profile-status" in payload:
        value = payload.get("emailfilter-profile-status")
        if value and value not in VALID_BODY_EMAILFILTER_PROFILE_STATUS:
            return (
                False,
                f"Invalid emailfilter-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_EMAILFILTER_PROFILE_STATUS)}",
            )

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile-status if present
    if "dlp-profile-status" in payload:
        value = payload.get("dlp-profile-status")
        if value and value not in VALID_BODY_DLP_PROFILE_STATUS:
            return (
                False,
                f"Invalid dlp-profile-status '{value}'. Must be one of: {', '.join(VALID_BODY_DLP_PROFILE_STATUS)}",
            )

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_interface_policy_delete(
    policyid: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        policyid: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not policyid:
        return (False, "policyid is required for DELETE operation")

    return (True, None)
