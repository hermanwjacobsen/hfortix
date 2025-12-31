"""
Validation helpers for switch-controller lldp_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MED_TLVS = [
    "inventory-management",
    "network-policy",
    "power-management",
    "location-identification",
]
VALID_BODY_802_1_TLVS = ["port-vlan-id"]
VALID_BODY_802_3_TLVS = ["max-frame-size", "power-negotiation"]
VALID_BODY_AUTO_ISL = ["disable", "enable"]
VALID_BODY_AUTO_MCLAG_ICL = ["disable", "enable"]
VALID_BODY_AUTO_ISL_AUTH = ["legacy", "strict", "relax"]
VALID_BODY_AUTO_ISL_AUTH_ENCRYPT = ["none", "mixed", "must"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_lldp_profile_get(
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


def validate_lldp_profile_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating lldp_profile.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate med-tlvs if present
    if "med-tlvs" in payload:
        value = payload.get("med-tlvs")
        if value and value not in VALID_BODY_MED_TLVS:
            return (
                False,
                f"Invalid med-tlvs '{value}'. Must be one of: {', '.join(VALID_BODY_MED_TLVS)}",
            )

    # Validate 802.1-tlvs if present
    if "802.1-tlvs" in payload:
        value = payload.get("802.1-tlvs")
        if value and value not in VALID_BODY_802_1_TLVS:
            return (
                False,
                f"Invalid 802.1-tlvs '{value}'. Must be one of: {', '.join(VALID_BODY_802_1_TLVS)}",
            )

    # Validate 802.3-tlvs if present
    if "802.3-tlvs" in payload:
        value = payload.get("802.3-tlvs")
        if value and value not in VALID_BODY_802_3_TLVS:
            return (
                False,
                f"Invalid 802.3-tlvs '{value}'. Must be one of: {', '.join(VALID_BODY_802_3_TLVS)}",
            )

    # Validate auto-isl if present
    if "auto-isl" in payload:
        value = payload.get("auto-isl")
        if value and value not in VALID_BODY_AUTO_ISL:
            return (
                False,
                f"Invalid auto-isl '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL)}",
            )

    # Validate auto-isl-hello-timer if present
    if "auto-isl-hello-timer" in payload:
        value = payload.get("auto-isl-hello-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "auto-isl-hello-timer must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-isl-hello-timer must be numeric, got: {value}",
                )

    # Validate auto-isl-receive-timeout if present
    if "auto-isl-receive-timeout" in payload:
        value = payload.get("auto-isl-receive-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 90:
                    return (
                        False,
                        "auto-isl-receive-timeout must be between 0 and 90",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-isl-receive-timeout must be numeric, got: {value}",
                )

    # Validate auto-isl-port-group if present
    if "auto-isl-port-group" in payload:
        value = payload.get("auto-isl-port-group")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 9:
                    return (
                        False,
                        "auto-isl-port-group must be between 0 and 9",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-isl-port-group must be numeric, got: {value}",
                )

    # Validate auto-mclag-icl if present
    if "auto-mclag-icl" in payload:
        value = payload.get("auto-mclag-icl")
        if value and value not in VALID_BODY_AUTO_MCLAG_ICL:
            return (
                False,
                f"Invalid auto-mclag-icl '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_MCLAG_ICL)}",
            )

    # Validate auto-isl-auth if present
    if "auto-isl-auth" in payload:
        value = payload.get("auto-isl-auth")
        if value and value not in VALID_BODY_AUTO_ISL_AUTH:
            return (
                False,
                f"Invalid auto-isl-auth '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL_AUTH)}",
            )

    # Validate auto-isl-auth-user if present
    if "auto-isl-auth-user" in payload:
        value = payload.get("auto-isl-auth-user")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auto-isl-auth-user cannot exceed 63 characters")

    # Validate auto-isl-auth-identity if present
    if "auto-isl-auth-identity" in payload:
        value = payload.get("auto-isl-auth-identity")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "auto-isl-auth-identity cannot exceed 63 characters",
            )

    # Validate auto-isl-auth-reauth if present
    if "auto-isl-auth-reauth" in payload:
        value = payload.get("auto-isl-auth-reauth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 180 or int_val > 3600:
                    return (
                        False,
                        "auto-isl-auth-reauth must be between 180 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-isl-auth-reauth must be numeric, got: {value}",
                )

    # Validate auto-isl-auth-encrypt if present
    if "auto-isl-auth-encrypt" in payload:
        value = payload.get("auto-isl-auth-encrypt")
        if value and value not in VALID_BODY_AUTO_ISL_AUTH_ENCRYPT:
            return (
                False,
                f"Invalid auto-isl-auth-encrypt '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL_AUTH_ENCRYPT)}",
            )

    # Validate auto-isl-auth-macsec-profile if present
    if "auto-isl-auth-macsec-profile" in payload:
        value = payload.get("auto-isl-auth-macsec-profile")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "auto-isl-auth-macsec-profile cannot exceed 63 characters",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_lldp_profile_put(
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
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate med-tlvs if present
    if "med-tlvs" in payload:
        value = payload.get("med-tlvs")
        if value and value not in VALID_BODY_MED_TLVS:
            return (
                False,
                f"Invalid med-tlvs '{value}'. Must be one of: {', '.join(VALID_BODY_MED_TLVS)}",
            )

    # Validate 802.1-tlvs if present
    if "802.1-tlvs" in payload:
        value = payload.get("802.1-tlvs")
        if value and value not in VALID_BODY_802_1_TLVS:
            return (
                False,
                f"Invalid 802.1-tlvs '{value}'. Must be one of: {', '.join(VALID_BODY_802_1_TLVS)}",
            )

    # Validate 802.3-tlvs if present
    if "802.3-tlvs" in payload:
        value = payload.get("802.3-tlvs")
        if value and value not in VALID_BODY_802_3_TLVS:
            return (
                False,
                f"Invalid 802.3-tlvs '{value}'. Must be one of: {', '.join(VALID_BODY_802_3_TLVS)}",
            )

    # Validate auto-isl if present
    if "auto-isl" in payload:
        value = payload.get("auto-isl")
        if value and value not in VALID_BODY_AUTO_ISL:
            return (
                False,
                f"Invalid auto-isl '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL)}",
            )

    # Validate auto-isl-hello-timer if present
    if "auto-isl-hello-timer" in payload:
        value = payload.get("auto-isl-hello-timer")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 30:
                    return (
                        False,
                        "auto-isl-hello-timer must be between 1 and 30",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-isl-hello-timer must be numeric, got: {value}",
                )

    # Validate auto-isl-receive-timeout if present
    if "auto-isl-receive-timeout" in payload:
        value = payload.get("auto-isl-receive-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 90:
                    return (
                        False,
                        "auto-isl-receive-timeout must be between 0 and 90",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-isl-receive-timeout must be numeric, got: {value}",
                )

    # Validate auto-isl-port-group if present
    if "auto-isl-port-group" in payload:
        value = payload.get("auto-isl-port-group")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 9:
                    return (
                        False,
                        "auto-isl-port-group must be between 0 and 9",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-isl-port-group must be numeric, got: {value}",
                )

    # Validate auto-mclag-icl if present
    if "auto-mclag-icl" in payload:
        value = payload.get("auto-mclag-icl")
        if value and value not in VALID_BODY_AUTO_MCLAG_ICL:
            return (
                False,
                f"Invalid auto-mclag-icl '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_MCLAG_ICL)}",
            )

    # Validate auto-isl-auth if present
    if "auto-isl-auth" in payload:
        value = payload.get("auto-isl-auth")
        if value and value not in VALID_BODY_AUTO_ISL_AUTH:
            return (
                False,
                f"Invalid auto-isl-auth '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL_AUTH)}",
            )

    # Validate auto-isl-auth-user if present
    if "auto-isl-auth-user" in payload:
        value = payload.get("auto-isl-auth-user")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "auto-isl-auth-user cannot exceed 63 characters")

    # Validate auto-isl-auth-identity if present
    if "auto-isl-auth-identity" in payload:
        value = payload.get("auto-isl-auth-identity")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "auto-isl-auth-identity cannot exceed 63 characters",
            )

    # Validate auto-isl-auth-reauth if present
    if "auto-isl-auth-reauth" in payload:
        value = payload.get("auto-isl-auth-reauth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 180 or int_val > 3600:
                    return (
                        False,
                        "auto-isl-auth-reauth must be between 180 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-isl-auth-reauth must be numeric, got: {value}",
                )

    # Validate auto-isl-auth-encrypt if present
    if "auto-isl-auth-encrypt" in payload:
        value = payload.get("auto-isl-auth-encrypt")
        if value and value not in VALID_BODY_AUTO_ISL_AUTH_ENCRYPT:
            return (
                False,
                f"Invalid auto-isl-auth-encrypt '{value}'. Must be one of: {', '.join(VALID_BODY_AUTO_ISL_AUTH_ENCRYPT)}",
            )

    # Validate auto-isl-auth-macsec-profile if present
    if "auto-isl-auth-macsec-profile" in payload:
        value = payload.get("auto-isl-auth-macsec-profile")
        if value and isinstance(value, str) and len(value) > 63:
            return (
                False,
                "auto-isl-auth-macsec-profile cannot exceed 63 characters",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_lldp_profile_delete(
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
