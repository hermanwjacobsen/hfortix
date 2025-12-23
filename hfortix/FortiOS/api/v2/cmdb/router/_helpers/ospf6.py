"""
Validation helpers for router ospf6 endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_ABR_TYPE = ["cisco", "ibm", "standard"]
VALID_BODY_DEFAULT_INFORMATION_ORIGINATE = ["enable", "always", "disable"]
VALID_BODY_LOG_NEIGHBOUR_CHANGES = ["enable", "disable"]
VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE = ["1", "2"]
VALID_BODY_BFD = ["enable", "disable"]
VALID_BODY_RESTART_MODE = ["none", "graceful-restart"]
VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ospf6_get(
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


def validate_ospf6_put(
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

    # Validate abr-type if present
    if "abr-type" in payload:
        value = payload.get("abr-type")
        if value and value not in VALID_BODY_ABR_TYPE:
            return (
                False,
                f"Invalid abr-type '{value}'. Must be one of: {', '.join(VALID_BODY_ABR_TYPE)}",
            )

    # Validate auto-cost-ref-bandwidth if present
    if "auto-cost-ref-bandwidth" in payload:
        value = payload.get("auto-cost-ref-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1000000:
                    return (
                        False,
                        "auto-cost-ref-bandwidth must be between 1 and 1000000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-cost-ref-bandwidth must be numeric, got: {value}",
                )

    # Validate default-information-originate if present
    if "default-information-originate" in payload:
        value = payload.get("default-information-originate")
        if value and value not in VALID_BODY_DEFAULT_INFORMATION_ORIGINATE:
            return (
                False,
                f"Invalid default-information-originate '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_INFORMATION_ORIGINATE)}",
            )

    # Validate log-neighbour-changes if present
    if "log-neighbour-changes" in payload:
        value = payload.get("log-neighbour-changes")
        if value and value not in VALID_BODY_LOG_NEIGHBOUR_CHANGES:
            return (
                False,
                f"Invalid log-neighbour-changes '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_NEIGHBOUR_CHANGES)}",
            )

    # Validate default-information-metric if present
    if "default-information-metric" in payload:
        value = payload.get("default-information-metric")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16777214:
                    return (
                        False,
                        "default-information-metric must be between 1 and 16777214",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"default-information-metric must be numeric, got: {value}",
                )

    # Validate default-information-metric-type if present
    if "default-information-metric-type" in payload:
        value = payload.get("default-information-metric-type")
        if value and value not in VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE:
            return (
                False,
                f"Invalid default-information-metric-type '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_INFORMATION_METRIC_TYPE)}",
            )

    # Validate default-information-route-map if present
    if "default-information-route-map" in payload:
        value = payload.get("default-information-route-map")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "default-information-route-map cannot exceed 35 characters",
            )

    # Validate default-metric if present
    if "default-metric" in payload:
        value = payload.get("default-metric")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 16777214:
                    return (
                        False,
                        "default-metric must be between 1 and 16777214",
                    )
            except (ValueError, TypeError):
                return (False, f"default-metric must be numeric, got: {value}")

    # Validate bfd if present
    if "bfd" in payload:
        value = payload.get("bfd")
        if value and value not in VALID_BODY_BFD:
            return (
                False,
                f"Invalid bfd '{value}'. Must be one of: {', '.join(VALID_BODY_BFD)}",
            )

    # Validate restart-mode if present
    if "restart-mode" in payload:
        value = payload.get("restart-mode")
        if value and value not in VALID_BODY_RESTART_MODE:
            return (
                False,
                f"Invalid restart-mode '{value}'. Must be one of: {', '.join(VALID_BODY_RESTART_MODE)}",
            )

    # Validate restart-period if present
    if "restart-period" in payload:
        value = payload.get("restart-period")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 3600:
                    return (
                        False,
                        "restart-period must be between 1 and 3600",
                    )
            except (ValueError, TypeError):
                return (False, f"restart-period must be numeric, got: {value}")

    # Validate restart-on-topology-change if present
    if "restart-on-topology-change" in payload:
        value = payload.get("restart-on-topology-change")
        if value and value not in VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE:
            return (
                False,
                f"Invalid restart-on-topology-change '{value}'. Must be one of: {', '.join(VALID_BODY_RESTART_ON_TOPOLOGY_CHANGE)}",
            )

    return (True, None)
