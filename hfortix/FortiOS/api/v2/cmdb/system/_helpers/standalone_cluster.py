"""
Validation helpers for system standalone_cluster endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_LAYER2_CONNECTION = ["available", "unavailable"]
VALID_BODY_ENCRYPTION = ["enable", "disable"]
VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL = ["cps-preferred", "strict-anti-replay"]
VALID_BODY_HELPER_TRAFFIC_BOUNCE = ["enable", "disable"]
VALID_BODY_UTM_TRAFFIC_BOUNCE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_standalone_cluster_get(
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


def validate_standalone_cluster_put(
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

    # Validate standalone-group-id if present
    if "standalone-group-id" in payload:
        value = payload.get("standalone-group-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (
                        False,
                        "standalone-group-id must be between 0 and 255",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"standalone-group-id must be numeric, got: {value}",
                )

    # Validate group-member-id if present
    if "group-member-id" in payload:
        value = payload.get("group-member-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 15:
                    return (False, "group-member-id must be between 0 and 15")
            except (ValueError, TypeError):
                return (
                    False,
                    f"group-member-id must be numeric, got: {value}",
                )

    # Validate layer2-connection if present
    if "layer2-connection" in payload:
        value = payload.get("layer2-connection")
        if value and value not in VALID_BODY_LAYER2_CONNECTION:
            return (
                False,
                f"Invalid layer2-connection '{value}'. Must be one of: {', '.join(VALID_BODY_LAYER2_CONNECTION)}",
            )

    # Validate encryption if present
    if "encryption" in payload:
        value = payload.get("encryption")
        if value and value not in VALID_BODY_ENCRYPTION:
            return (
                False,
                f"Invalid encryption '{value}'. Must be one of: {', '.join(VALID_BODY_ENCRYPTION)}",
            )

    # Validate asymmetric-traffic-control if present
    if "asymmetric-traffic-control" in payload:
        value = payload.get("asymmetric-traffic-control")
        if value and value not in VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL:
            return (
                False,
                f"Invalid asymmetric-traffic-control '{value}'. Must be one of: {', '.join(VALID_BODY_ASYMMETRIC_TRAFFIC_CONTROL)}",
            )

    # Validate helper-traffic-bounce if present
    if "helper-traffic-bounce" in payload:
        value = payload.get("helper-traffic-bounce")
        if value and value not in VALID_BODY_HELPER_TRAFFIC_BOUNCE:
            return (
                False,
                f"Invalid helper-traffic-bounce '{value}'. Must be one of: {', '.join(VALID_BODY_HELPER_TRAFFIC_BOUNCE)}",
            )

    # Validate utm-traffic-bounce if present
    if "utm-traffic-bounce" in payload:
        value = payload.get("utm-traffic-bounce")
        if value and value not in VALID_BODY_UTM_TRAFFIC_BOUNCE:
            return (
                False,
                f"Invalid utm-traffic-bounce '{value}'. Must be one of: {', '.join(VALID_BODY_UTM_TRAFFIC_BOUNCE)}",
            )

    return (True, None)
