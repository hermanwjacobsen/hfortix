"""
Validation helpers for log eventfilter endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_EVENT = ["enable", "disable"]
VALID_BODY_SYSTEM = ["enable", "disable"]
VALID_BODY_VPN = ["enable", "disable"]
VALID_BODY_USER = ["enable", "disable"]
VALID_BODY_ROUTER = ["enable", "disable"]
VALID_BODY_WIRELESS_ACTIVITY = ["enable", "disable"]
VALID_BODY_WAN_OPT = ["enable", "disable"]
VALID_BODY_ENDPOINT = ["enable", "disable"]
VALID_BODY_HA = ["enable", "disable"]
VALID_BODY_SECURITY_RATING = ["enable", "disable"]
VALID_BODY_FORTIEXTENDER = ["enable", "disable"]
VALID_BODY_CONNECTOR = ["enable", "disable"]
VALID_BODY_SDWAN = ["enable", "disable"]
VALID_BODY_CIFS = ["enable", "disable"]
VALID_BODY_SWITCH_CONTROLLER = ["enable", "disable"]
VALID_BODY_REST_API = ["enable", "disable"]
VALID_BODY_WEB_SVC = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_eventfilter_get(
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


def validate_eventfilter_put(
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

    # Validate event if present
    if "event" in payload:
        value = payload.get("event")
        if value and value not in VALID_BODY_EVENT:
            return (
                False,
                f"Invalid event '{value}'. Must be one of: {', '.join(VALID_BODY_EVENT)}",
            )

    # Validate system if present
    if "system" in payload:
        value = payload.get("system")
        if value and value not in VALID_BODY_SYSTEM:
            return (
                False,
                f"Invalid system '{value}'. Must be one of: {', '.join(VALID_BODY_SYSTEM)}",
            )

    # Validate vpn if present
    if "vpn" in payload:
        value = payload.get("vpn")
        if value and value not in VALID_BODY_VPN:
            return (
                False,
                f"Invalid vpn '{value}'. Must be one of: {', '.join(VALID_BODY_VPN)}",
            )

    # Validate user if present
    if "user" in payload:
        value = payload.get("user")
        if value and value not in VALID_BODY_USER:
            return (
                False,
                f"Invalid user '{value}'. Must be one of: {', '.join(VALID_BODY_USER)}",
            )

    # Validate router if present
    if "router" in payload:
        value = payload.get("router")
        if value and value not in VALID_BODY_ROUTER:
            return (
                False,
                f"Invalid router '{value}'. Must be one of: {', '.join(VALID_BODY_ROUTER)}",
            )

    # Validate wireless-activity if present
    if "wireless-activity" in payload:
        value = payload.get("wireless-activity")
        if value and value not in VALID_BODY_WIRELESS_ACTIVITY:
            return (
                False,
                f"Invalid wireless-activity '{value}'. Must be one of: {', '.join(VALID_BODY_WIRELESS_ACTIVITY)}",
            )

    # Validate wan-opt if present
    if "wan-opt" in payload:
        value = payload.get("wan-opt")
        if value and value not in VALID_BODY_WAN_OPT:
            return (
                False,
                f"Invalid wan-opt '{value}'. Must be one of: {', '.join(VALID_BODY_WAN_OPT)}",
            )

    # Validate endpoint if present
    if "endpoint" in payload:
        value = payload.get("endpoint")
        if value and value not in VALID_BODY_ENDPOINT:
            return (
                False,
                f"Invalid endpoint '{value}'. Must be one of: {', '.join(VALID_BODY_ENDPOINT)}",
            )

    # Validate ha if present
    if "ha" in payload:
        value = payload.get("ha")
        if value and value not in VALID_BODY_HA:
            return (
                False,
                f"Invalid ha '{value}'. Must be one of: {', '.join(VALID_BODY_HA)}",
            )

    # Validate security-rating if present
    if "security-rating" in payload:
        value = payload.get("security-rating")
        if value and value not in VALID_BODY_SECURITY_RATING:
            return (
                False,
                f"Invalid security-rating '{value}'. Must be one of: {', '.join(VALID_BODY_SECURITY_RATING)}",
            )

    # Validate fortiextender if present
    if "fortiextender" in payload:
        value = payload.get("fortiextender")
        if value and value not in VALID_BODY_FORTIEXTENDER:
            return (
                False,
                f"Invalid fortiextender '{value}'. Must be one of: {', '.join(VALID_BODY_FORTIEXTENDER)}",
            )

    # Validate connector if present
    if "connector" in payload:
        value = payload.get("connector")
        if value and value not in VALID_BODY_CONNECTOR:
            return (
                False,
                f"Invalid connector '{value}'. Must be one of: {', '.join(VALID_BODY_CONNECTOR)}",
            )

    # Validate sdwan if present
    if "sdwan" in payload:
        value = payload.get("sdwan")
        if value and value not in VALID_BODY_SDWAN:
            return (
                False,
                f"Invalid sdwan '{value}'. Must be one of: {', '.join(VALID_BODY_SDWAN)}",
            )

    # Validate cifs if present
    if "cifs" in payload:
        value = payload.get("cifs")
        if value and value not in VALID_BODY_CIFS:
            return (
                False,
                f"Invalid cifs '{value}'. Must be one of: {', '.join(VALID_BODY_CIFS)}",
            )

    # Validate switch-controller if present
    if "switch-controller" in payload:
        value = payload.get("switch-controller")
        if value and value not in VALID_BODY_SWITCH_CONTROLLER:
            return (
                False,
                f"Invalid switch-controller '{value}'. Must be one of: {', '.join(VALID_BODY_SWITCH_CONTROLLER)}",
            )

    # Validate rest-api if present
    if "rest-api" in payload:
        value = payload.get("rest-api")
        if value and value not in VALID_BODY_REST_API:
            return (
                False,
                f"Invalid rest-api '{value}'. Must be one of: {', '.join(VALID_BODY_REST_API)}",
            )

    # Validate web-svc if present
    if "web-svc" in payload:
        value = payload.get("web-svc")
        if value and value not in VALID_BODY_WEB_SVC:
            return (
                False,
                f"Invalid web-svc '{value}'. Must be one of: {', '.join(VALID_BODY_WEB_SVC)}",
            )

    return (True, None)
