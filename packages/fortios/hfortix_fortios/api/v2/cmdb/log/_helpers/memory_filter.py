"""
Validation helpers for log memory_filter endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
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
VALID_BODY_FORWARD_TRAFFIC = ["enable", "disable"]
VALID_BODY_LOCAL_TRAFFIC = ["enable", "disable"]
VALID_BODY_MULTICAST_TRAFFIC = ["enable", "disable"]
VALID_BODY_SNIFFER_TRAFFIC = ["enable", "disable"]
VALID_BODY_ZTNA_TRAFFIC = ["enable", "disable"]
VALID_BODY_HTTP_TRANSACTION = ["enable", "disable"]
VALID_BODY_ANOMALY = ["enable", "disable"]
VALID_BODY_VOIP = ["enable", "disable"]
VALID_BODY_FORTI_SWITCH = ["enable", "disable"]
VALID_BODY_DEBUG = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_memory_filter_get(
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


def validate_memory_filter_put(
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

    # Validate severity if present
    if "severity" in payload:
        value = payload.get("severity")
        if value and value not in VALID_BODY_SEVERITY:
            return (
                False,
                f"Invalid severity '{value}'. Must be one of: {', '.join(VALID_BODY_SEVERITY)}",
            )

    # Validate forward-traffic if present
    if "forward-traffic" in payload:
        value = payload.get("forward-traffic")
        if value and value not in VALID_BODY_FORWARD_TRAFFIC:
            return (
                False,
                f"Invalid forward-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_FORWARD_TRAFFIC)}",
            )

    # Validate local-traffic if present
    if "local-traffic" in payload:
        value = payload.get("local-traffic")
        if value and value not in VALID_BODY_LOCAL_TRAFFIC:
            return (
                False,
                f"Invalid local-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_LOCAL_TRAFFIC)}",
            )

    # Validate multicast-traffic if present
    if "multicast-traffic" in payload:
        value = payload.get("multicast-traffic")
        if value and value not in VALID_BODY_MULTICAST_TRAFFIC:
            return (
                False,
                f"Invalid multicast-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_MULTICAST_TRAFFIC)}",
            )

    # Validate sniffer-traffic if present
    if "sniffer-traffic" in payload:
        value = payload.get("sniffer-traffic")
        if value and value not in VALID_BODY_SNIFFER_TRAFFIC:
            return (
                False,
                f"Invalid sniffer-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_SNIFFER_TRAFFIC)}",
            )

    # Validate ztna-traffic if present
    if "ztna-traffic" in payload:
        value = payload.get("ztna-traffic")
        if value and value not in VALID_BODY_ZTNA_TRAFFIC:
            return (
                False,
                f"Invalid ztna-traffic '{value}'. Must be one of: {', '.join(VALID_BODY_ZTNA_TRAFFIC)}",
            )

    # Validate http-transaction if present
    if "http-transaction" in payload:
        value = payload.get("http-transaction")
        if value and value not in VALID_BODY_HTTP_TRANSACTION:
            return (
                False,
                f"Invalid http-transaction '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_TRANSACTION)}",
            )

    # Validate anomaly if present
    if "anomaly" in payload:
        value = payload.get("anomaly")
        if value and value not in VALID_BODY_ANOMALY:
            return (
                False,
                f"Invalid anomaly '{value}'. Must be one of: {', '.join(VALID_BODY_ANOMALY)}",
            )

    # Validate voip if present
    if "voip" in payload:
        value = payload.get("voip")
        if value and value not in VALID_BODY_VOIP:
            return (
                False,
                f"Invalid voip '{value}'. Must be one of: {', '.join(VALID_BODY_VOIP)}",
            )

    # Validate forti-switch if present
    if "forti-switch" in payload:
        value = payload.get("forti-switch")
        if value and value not in VALID_BODY_FORTI_SWITCH:
            return (
                False,
                f"Invalid forti-switch '{value}'. Must be one of: {', '.join(VALID_BODY_FORTI_SWITCH)}",
            )

    # Validate debug if present
    if "debug" in payload:
        value = payload.get("debug")
        if value and value not in VALID_BODY_DEBUG:
            return (
                False,
                f"Invalid debug '{value}'. Must be one of: {', '.join(VALID_BODY_DEBUG)}",
            )

    return (True, None)
