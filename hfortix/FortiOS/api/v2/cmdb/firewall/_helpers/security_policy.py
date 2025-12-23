"""
Validation helpers for firewall security_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SRCADDR_NEGATE = ["enable", "disable"]
VALID_BODY_DSTADDR_NEGATE = ["enable", "disable"]
VALID_BODY_SRCADDR6_NEGATE = ["enable", "disable"]
VALID_BODY_DSTADDR6_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_SRC = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE_SRC_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6 = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_NEGATE = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_SRC = ["enable", "disable"]
VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE = ["enable", "disable"]
VALID_BODY_ENFORCE_DEFAULT_APP_PORT = ["enable", "disable"]
VALID_BODY_SERVICE_NEGATE = ["enable", "disable"]
VALID_BODY_ACTION = ["accept", "deny"]
VALID_BODY_SEND_DENY_PACKET = ["disable", "enable"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_LOGTRAFFIC = ["all", "utm", "disable"]
VALID_BODY_LEARNING_MODE = ["enable", "disable"]
VALID_BODY_NAT46 = ["enable", "disable"]
VALID_BODY_NAT64 = ["enable", "disable"]
VALID_BODY_PROFILE_TYPE = ["single", "group"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_security_policy_get(
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


def validate_security_policy_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating security_policy.

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
                if int_val < 0 or int_val > 4294967294:
                    return (
                        False,
                        "policyid must be between 0 and 4294967294",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate srcaddr-negate if present
    if "srcaddr-negate" in payload:
        value = payload.get("srcaddr-negate")
        if value and value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid srcaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )

    # Validate dstaddr-negate if present
    if "dstaddr-negate" in payload:
        value = payload.get("dstaddr-negate")
        if value and value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid dstaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )

    # Validate srcaddr6-negate if present
    if "srcaddr6-negate" in payload:
        value = payload.get("srcaddr6-negate")
        if value and value not in VALID_BODY_SRCADDR6_NEGATE:
            return (
                False,
                f"Invalid srcaddr6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR6_NEGATE)}",
            )

    # Validate dstaddr6-negate if present
    if "dstaddr6-negate" in payload:
        value = payload.get("dstaddr6-negate")
        if value and value not in VALID_BODY_DSTADDR6_NEGATE:
            return (
                False,
                f"Invalid dstaddr6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR6_NEGATE)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-negate if present
    if "internet-service-negate" in payload:
        value = payload.get("internet-service-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            return (
                False,
                f"Invalid internet-service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_NEGATE)}",
            )

    # Validate internet-service-src if present
    if "internet-service-src" in payload:
        value = payload.get("internet-service-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid internet-service-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )

    # Validate internet-service-src-negate if present
    if "internet-service-src-negate" in payload:
        value = payload.get("internet-service-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}",
            )

    # Validate internet-service6 if present
    if "internet-service6" in payload:
        value = payload.get("internet-service6")
        if value and value not in VALID_BODY_INTERNET_SERVICE6:
            return (
                False,
                f"Invalid internet-service6 '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6)}",
            )

    # Validate internet-service6-negate if present
    if "internet-service6-negate" in payload:
        value = payload.get("internet-service6-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            return (
                False,
                f"Invalid internet-service6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_NEGATE)}",
            )

    # Validate internet-service6-src if present
    if "internet-service6-src" in payload:
        value = payload.get("internet-service6-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid internet-service6-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )

    # Validate internet-service6-src-negate if present
    if "internet-service6-src-negate" in payload:
        value = payload.get("internet-service6-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service6-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )

    # Validate enforce-default-app-port if present
    if "enforce-default-app-port" in payload:
        value = payload.get("enforce-default-app-port")
        if value and value not in VALID_BODY_ENFORCE_DEFAULT_APP_PORT:
            return (
                False,
                f"Invalid enforce-default-app-port '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_DEFAULT_APP_PORT)}",
            )

    # Validate service-negate if present
    if "service-negate" in payload:
        value = payload.get("service-negate")
        if value and value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate send-deny-packet if present
    if "send-deny-packet" in payload:
        value = payload.get("send-deny-packet")
        if value and value not in VALID_BODY_SEND_DENY_PACKET:
            return (
                False,
                f"Invalid send-deny-packet '{value}'. Must be one of: {', '.join(VALID_BODY_SEND_DENY_PACKET)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate learning-mode if present
    if "learning-mode" in payload:
        value = payload.get("learning-mode")
        if value and value not in VALID_BODY_LEARNING_MODE:
            return (
                False,
                f"Invalid learning-mode '{value}'. Must be one of: {', '.join(VALID_BODY_LEARNING_MODE)}",
            )

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate nat64 if present
    if "nat64" in payload:
        value = payload.get("nat64")
        if value and value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid nat64 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )

    # Validate profile-type if present
    if "profile-type" in payload:
        value = payload.get("profile-type")
        if value and value not in VALID_BODY_PROFILE_TYPE:
            return (
                False,
                f"Invalid profile-type '{value}'. Must be one of: {', '.join(VALID_BODY_PROFILE_TYPE)}",
            )

    # Validate profile-group if present
    if "profile-group" in payload:
        value = payload.get("profile-group")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "profile-group cannot exceed 47 characters")

    # Validate profile-protocol-options if present
    if "profile-protocol-options" in payload:
        value = payload.get("profile-protocol-options")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "profile-protocol-options cannot exceed 47 characters",
            )

    # Validate ssl-ssh-profile if present
    if "ssl-ssh-profile" in payload:
        value = payload.get("ssl-ssh-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssl-ssh-profile cannot exceed 47 characters")

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate dnsfilter-profile if present
    if "dnsfilter-profile" in payload:
        value = payload.get("dnsfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dnsfilter-profile cannot exceed 47 characters")

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    # Validate file-filter-profile if present
    if "file-filter-profile" in payload:
        value = payload.get("file-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "file-filter-profile cannot exceed 47 characters")

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate voip-profile if present
    if "voip-profile" in payload:
        value = payload.get("voip-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "voip-profile cannot exceed 47 characters")

    # Validate ips-voip-filter if present
    if "ips-voip-filter" in payload:
        value = payload.get("ips-voip-filter")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-voip-filter cannot exceed 47 characters")

    # Validate sctp-filter-profile if present
    if "sctp-filter-profile" in payload:
        value = payload.get("sctp-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "sctp-filter-profile cannot exceed 47 characters")

    # Validate diameter-filter-profile if present
    if "diameter-filter-profile" in payload:
        value = payload.get("diameter-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "diameter-filter-profile cannot exceed 47 characters",
            )

    # Validate virtual-patch-profile if present
    if "virtual-patch-profile" in payload:
        value = payload.get("virtual-patch-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "virtual-patch-profile cannot exceed 47 characters",
            )

    # Validate icap-profile if present
    if "icap-profile" in payload:
        value = payload.get("icap-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "icap-profile cannot exceed 47 characters")

    # Validate videofilter-profile if present
    if "videofilter-profile" in payload:
        value = payload.get("videofilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "videofilter-profile cannot exceed 47 characters")

    # Validate ssh-filter-profile if present
    if "ssh-filter-profile" in payload:
        value = payload.get("ssh-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssh-filter-profile cannot exceed 47 characters")

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_security_policy_put(
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
                if int_val < 0 or int_val > 4294967294:
                    return (
                        False,
                        "policyid must be between 0 and 4294967294",
                    )
            except (ValueError, TypeError):
                return (False, f"policyid must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 1023:
            return (False, "comments cannot exceed 1023 characters")

    # Validate srcaddr-negate if present
    if "srcaddr-negate" in payload:
        value = payload.get("srcaddr-negate")
        if value and value not in VALID_BODY_SRCADDR_NEGATE:
            return (
                False,
                f"Invalid srcaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR_NEGATE)}",
            )

    # Validate dstaddr-negate if present
    if "dstaddr-negate" in payload:
        value = payload.get("dstaddr-negate")
        if value and value not in VALID_BODY_DSTADDR_NEGATE:
            return (
                False,
                f"Invalid dstaddr-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR_NEGATE)}",
            )

    # Validate srcaddr6-negate if present
    if "srcaddr6-negate" in payload:
        value = payload.get("srcaddr6-negate")
        if value and value not in VALID_BODY_SRCADDR6_NEGATE:
            return (
                False,
                f"Invalid srcaddr6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRCADDR6_NEGATE)}",
            )

    # Validate dstaddr6-negate if present
    if "dstaddr6-negate" in payload:
        value = payload.get("dstaddr6-negate")
        if value and value not in VALID_BODY_DSTADDR6_NEGATE:
            return (
                False,
                f"Invalid dstaddr6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DSTADDR6_NEGATE)}",
            )

    # Validate internet-service if present
    if "internet-service" in payload:
        value = payload.get("internet-service")
        if value and value not in VALID_BODY_INTERNET_SERVICE:
            return (
                False,
                f"Invalid internet-service '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE)}",
            )

    # Validate internet-service-negate if present
    if "internet-service-negate" in payload:
        value = payload.get("internet-service-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_NEGATE:
            return (
                False,
                f"Invalid internet-service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_NEGATE)}",
            )

    # Validate internet-service-src if present
    if "internet-service-src" in payload:
        value = payload.get("internet-service-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC:
            return (
                False,
                f"Invalid internet-service-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC)}",
            )

    # Validate internet-service-src-negate if present
    if "internet-service-src-negate" in payload:
        value = payload.get("internet-service-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE_SRC_NEGATE)}",
            )

    # Validate internet-service6 if present
    if "internet-service6" in payload:
        value = payload.get("internet-service6")
        if value and value not in VALID_BODY_INTERNET_SERVICE6:
            return (
                False,
                f"Invalid internet-service6 '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6)}",
            )

    # Validate internet-service6-negate if present
    if "internet-service6-negate" in payload:
        value = payload.get("internet-service6-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_NEGATE:
            return (
                False,
                f"Invalid internet-service6-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_NEGATE)}",
            )

    # Validate internet-service6-src if present
    if "internet-service6-src" in payload:
        value = payload.get("internet-service6-src")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC:
            return (
                False,
                f"Invalid internet-service6-src '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC)}",
            )

    # Validate internet-service6-src-negate if present
    if "internet-service6-src-negate" in payload:
        value = payload.get("internet-service6-src-negate")
        if value and value not in VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE:
            return (
                False,
                f"Invalid internet-service6-src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INTERNET_SERVICE6_SRC_NEGATE)}",
            )

    # Validate enforce-default-app-port if present
    if "enforce-default-app-port" in payload:
        value = payload.get("enforce-default-app-port")
        if value and value not in VALID_BODY_ENFORCE_DEFAULT_APP_PORT:
            return (
                False,
                f"Invalid enforce-default-app-port '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_DEFAULT_APP_PORT)}",
            )

    # Validate service-negate if present
    if "service-negate" in payload:
        value = payload.get("service-negate")
        if value and value not in VALID_BODY_SERVICE_NEGATE:
            return (
                False,
                f"Invalid service-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SERVICE_NEGATE)}",
            )

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate send-deny-packet if present
    if "send-deny-packet" in payload:
        value = payload.get("send-deny-packet")
        if value and value not in VALID_BODY_SEND_DENY_PACKET:
            return (
                False,
                f"Invalid send-deny-packet '{value}'. Must be one of: {', '.join(VALID_BODY_SEND_DENY_PACKET)}",
            )

    # Validate schedule if present
    if "schedule" in payload:
        value = payload.get("schedule")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "schedule cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate logtraffic if present
    if "logtraffic" in payload:
        value = payload.get("logtraffic")
        if value and value not in VALID_BODY_LOGTRAFFIC:
            return (
                False,
                f"Invalid logtraffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOGTRAFFIC)}",
            )

    # Validate learning-mode if present
    if "learning-mode" in payload:
        value = payload.get("learning-mode")
        if value and value not in VALID_BODY_LEARNING_MODE:
            return (
                False,
                f"Invalid learning-mode '{value}'. Must be one of: {', '.join(VALID_BODY_LEARNING_MODE)}",
            )

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate nat64 if present
    if "nat64" in payload:
        value = payload.get("nat64")
        if value and value not in VALID_BODY_NAT64:
            return (
                False,
                f"Invalid nat64 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT64)}",
            )

    # Validate profile-type if present
    if "profile-type" in payload:
        value = payload.get("profile-type")
        if value and value not in VALID_BODY_PROFILE_TYPE:
            return (
                False,
                f"Invalid profile-type '{value}'. Must be one of: {', '.join(VALID_BODY_PROFILE_TYPE)}",
            )

    # Validate profile-group if present
    if "profile-group" in payload:
        value = payload.get("profile-group")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "profile-group cannot exceed 47 characters")

    # Validate profile-protocol-options if present
    if "profile-protocol-options" in payload:
        value = payload.get("profile-protocol-options")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "profile-protocol-options cannot exceed 47 characters",
            )

    # Validate ssl-ssh-profile if present
    if "ssl-ssh-profile" in payload:
        value = payload.get("ssl-ssh-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssl-ssh-profile cannot exceed 47 characters")

    # Validate av-profile if present
    if "av-profile" in payload:
        value = payload.get("av-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "av-profile cannot exceed 47 characters")

    # Validate webfilter-profile if present
    if "webfilter-profile" in payload:
        value = payload.get("webfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "webfilter-profile cannot exceed 47 characters")

    # Validate dnsfilter-profile if present
    if "dnsfilter-profile" in payload:
        value = payload.get("dnsfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dnsfilter-profile cannot exceed 47 characters")

    # Validate emailfilter-profile if present
    if "emailfilter-profile" in payload:
        value = payload.get("emailfilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "emailfilter-profile cannot exceed 47 characters")

    # Validate dlp-profile if present
    if "dlp-profile" in payload:
        value = payload.get("dlp-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "dlp-profile cannot exceed 47 characters")

    # Validate file-filter-profile if present
    if "file-filter-profile" in payload:
        value = payload.get("file-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "file-filter-profile cannot exceed 47 characters")

    # Validate ips-sensor if present
    if "ips-sensor" in payload:
        value = payload.get("ips-sensor")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-sensor cannot exceed 47 characters")

    # Validate application-list if present
    if "application-list" in payload:
        value = payload.get("application-list")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "application-list cannot exceed 47 characters")

    # Validate voip-profile if present
    if "voip-profile" in payload:
        value = payload.get("voip-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "voip-profile cannot exceed 47 characters")

    # Validate ips-voip-filter if present
    if "ips-voip-filter" in payload:
        value = payload.get("ips-voip-filter")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ips-voip-filter cannot exceed 47 characters")

    # Validate sctp-filter-profile if present
    if "sctp-filter-profile" in payload:
        value = payload.get("sctp-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "sctp-filter-profile cannot exceed 47 characters")

    # Validate diameter-filter-profile if present
    if "diameter-filter-profile" in payload:
        value = payload.get("diameter-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "diameter-filter-profile cannot exceed 47 characters",
            )

    # Validate virtual-patch-profile if present
    if "virtual-patch-profile" in payload:
        value = payload.get("virtual-patch-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (
                False,
                "virtual-patch-profile cannot exceed 47 characters",
            )

    # Validate icap-profile if present
    if "icap-profile" in payload:
        value = payload.get("icap-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "icap-profile cannot exceed 47 characters")

    # Validate videofilter-profile if present
    if "videofilter-profile" in payload:
        value = payload.get("videofilter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "videofilter-profile cannot exceed 47 characters")

    # Validate ssh-filter-profile if present
    if "ssh-filter-profile" in payload:
        value = payload.get("ssh-filter-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "ssh-filter-profile cannot exceed 47 characters")

    # Validate casb-profile if present
    if "casb-profile" in payload:
        value = payload.get("casb-profile")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "casb-profile cannot exceed 47 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_security_policy_delete(
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
