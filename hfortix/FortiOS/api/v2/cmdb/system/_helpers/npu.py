"""
Validation helpers for system npu endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_DEDICATED_MANAGEMENT_CPU = ["enable", "disable"]
VALID_BODY_CAPWAP_OFFLOAD = ["enable", "disable"]
VALID_BODY_IPSEC_MTU_OVERRIDE = ["disable", "enable"]
VALID_BODY_IPSEC_ORDERING = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_npu_get(
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


def validate_npu_put(
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

    # Validate dedicated-management-cpu if present
    if "dedicated-management-cpu" in payload:
        value = payload.get("dedicated-management-cpu")
        if value and value not in VALID_BODY_DEDICATED_MANAGEMENT_CPU:
            return (
                False,
                f"Invalid dedicated-management-cpu '{value}'. Must be one of: {', '.join(VALID_BODY_DEDICATED_MANAGEMENT_CPU)}",
            )

    # Validate dedicated-management-affinity if present
    if "dedicated-management-affinity" in payload:
        value = payload.get("dedicated-management-affinity")
        if value and isinstance(value, str) and len(value) > 79:
            return (
                False,
                "dedicated-management-affinity cannot exceed 79 characters",
            )

    # Validate capwap-offload if present
    if "capwap-offload" in payload:
        value = payload.get("capwap-offload")
        if value and value not in VALID_BODY_CAPWAP_OFFLOAD:
            return (
                False,
                f"Invalid capwap-offload '{value}'. Must be one of: {', '.join(VALID_BODY_CAPWAP_OFFLOAD)}",
            )

    # Validate ipsec-mtu-override if present
    if "ipsec-mtu-override" in payload:
        value = payload.get("ipsec-mtu-override")
        if value and value not in VALID_BODY_IPSEC_MTU_OVERRIDE:
            return (
                False,
                f"Invalid ipsec-mtu-override '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_MTU_OVERRIDE)}",
            )

    # Validate ipsec-ordering if present
    if "ipsec-ordering" in payload:
        value = payload.get("ipsec-ordering")
        if value and value not in VALID_BODY_IPSEC_ORDERING:
            return (
                False,
                f"Invalid ipsec-ordering '{value}'. Must be one of: {', '.join(VALID_BODY_IPSEC_ORDERING)}",
            )

    return (True, None)
