"""
Validation helpers for system fabric_vpn endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_SYNC_MODE = ["enable", "disable"]
VALID_BODY_POLICY_RULE = ["health-check", "manual", "auto"]
VALID_BODY_VPN_ROLE = ["hub", "spoke"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fabric_vpn_get(
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


def validate_fabric_vpn_put(
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

    # Validate sync-mode if present
    if "sync-mode" in payload:
        value = payload.get("sync-mode")
        if value and value not in VALID_BODY_SYNC_MODE:
            return (
                False,
                f"Invalid sync-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SYNC_MODE)}",
            )

    # Validate branch-name if present
    if "branch-name" in payload:
        value = payload.get("branch-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "branch-name cannot exceed 35 characters")

    # Validate policy-rule if present
    if "policy-rule" in payload:
        value = payload.get("policy-rule")
        if value and value not in VALID_BODY_POLICY_RULE:
            return (
                False,
                f"Invalid policy-rule '{value}'. Must be one of: {', '.join(VALID_BODY_POLICY_RULE)}",
            )

    # Validate vpn-role if present
    if "vpn-role" in payload:
        value = payload.get("vpn-role")
        if value and value not in VALID_BODY_VPN_ROLE:
            return (
                False,
                f"Invalid vpn-role '{value}'. Must be one of: {', '.join(VALID_BODY_VPN_ROLE)}",
            )

    # Validate loopback-interface if present
    if "loopback-interface" in payload:
        value = payload.get("loopback-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "loopback-interface cannot exceed 15 characters")

    # Validate loopback-advertised-subnet if present
    if "loopback-advertised-subnet" in payload:
        value = payload.get("loopback-advertised-subnet")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "loopback-advertised-subnet must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"loopback-advertised-subnet must be numeric, got: {value}",
                )

    # Validate sdwan-zone if present
    if "sdwan-zone" in payload:
        value = payload.get("sdwan-zone")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sdwan-zone cannot exceed 35 characters")

    # Validate health-checks if present
    if "health-checks" in payload:
        value = payload.get("health-checks")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "health-checks cannot exceed 35 characters")

    return (True, None)
