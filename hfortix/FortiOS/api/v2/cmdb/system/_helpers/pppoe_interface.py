"""
Validation helpers for system pppoe_interface endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_DIAL_ON_DEMAND = ["enable", "disable"]
VALID_BODY_IPV6 = ["enable", "disable"]
VALID_BODY_PPPOE_EGRESS_COS = [
    "cos0",
    "cos1",
    "cos2",
    "cos3",
    "cos4",
    "cos5",
    "cos6",
    "cos7",
]
VALID_BODY_AUTH_TYPE = ["auto", "pap", "chap", "mschapv1", "mschapv2"]
VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE = ["enable", "disable"]
VALID_BODY_MULTILINK = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_pppoe_interface_get(
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


def validate_pppoe_interface_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating pppoe_interface.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate dial-on-demand if present
    if "dial-on-demand" in payload:
        value = payload.get("dial-on-demand")
        if value and value not in VALID_BODY_DIAL_ON_DEMAND:
            return (
                False,
                f"Invalid dial-on-demand '{value}'. Must be one of: {', '.join(VALID_BODY_DIAL_ON_DEMAND)}",
            )

    # Validate ipv6 if present
    if "ipv6" in payload:
        value = payload.get("ipv6")
        if value and value not in VALID_BODY_IPV6:
            return (
                False,
                f"Invalid ipv6 '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6)}",
            )

    # Validate device if present
    if "device" in payload:
        value = payload.get("device")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "device cannot exceed 15 characters")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate pppoe-egress-cos if present
    if "pppoe-egress-cos" in payload:
        value = payload.get("pppoe-egress-cos")
        if value and value not in VALID_BODY_PPPOE_EGRESS_COS:
            return (
                False,
                f"Invalid pppoe-egress-cos '{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_EGRESS_COS)}",
            )

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate pppoe-unnumbered-negotiate if present
    if "pppoe-unnumbered-negotiate" in payload:
        value = payload.get("pppoe-unnumbered-negotiate")
        if value and value not in VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE:
            return (
                False,
                f"Invalid pppoe-unnumbered-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE)}",
            )

    # Validate idle-timeout if present
    if "idle-timeout" in payload:
        value = payload.get("idle-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "idle-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"idle-timeout must be numeric, got: {value}")

    # Validate multilink if present
    if "multilink" in payload:
        value = payload.get("multilink")
        if value and value not in VALID_BODY_MULTILINK:
            return (
                False,
                f"Invalid multilink '{value}'. Must be one of: {', '.join(VALID_BODY_MULTILINK)}",
            )

    # Validate mrru if present
    if "mrru" in payload:
        value = payload.get("mrru")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 296 or int_val > 65535:
                    return (False, "mrru must be between 296 and 65535")
            except (ValueError, TypeError):
                return (False, f"mrru must be numeric, got: {value}")

    # Validate disc-retry-timeout if present
    if "disc-retry-timeout" in payload:
        value = payload.get("disc-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "disc-retry-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"disc-retry-timeout must be numeric, got: {value}",
                )

    # Validate padt-retry-timeout if present
    if "padt-retry-timeout" in payload:
        value = payload.get("padt-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "padt-retry-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"padt-retry-timeout must be numeric, got: {value}",
                )

    # Validate service-name if present
    if "service-name" in payload:
        value = payload.get("service-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "service-name cannot exceed 63 characters")

    # Validate ac-name if present
    if "ac-name" in payload:
        value = payload.get("ac-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ac-name cannot exceed 63 characters")

    # Validate lcp-echo-interval if present
    if "lcp-echo-interval" in payload:
        value = payload.get("lcp-echo-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "lcp-echo-interval must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lcp-echo-interval must be numeric, got: {value}",
                )

    # Validate lcp-max-echo-fails if present
    if "lcp-max-echo-fails" in payload:
        value = payload.get("lcp-max-echo-fails")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "lcp-max-echo-fails must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lcp-max-echo-fails must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_pppoe_interface_put(
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
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "name cannot exceed 15 characters")

    # Validate dial-on-demand if present
    if "dial-on-demand" in payload:
        value = payload.get("dial-on-demand")
        if value and value not in VALID_BODY_DIAL_ON_DEMAND:
            return (
                False,
                f"Invalid dial-on-demand '{value}'. Must be one of: {', '.join(VALID_BODY_DIAL_ON_DEMAND)}",
            )

    # Validate ipv6 if present
    if "ipv6" in payload:
        value = payload.get("ipv6")
        if value and value not in VALID_BODY_IPV6:
            return (
                False,
                f"Invalid ipv6 '{value}'. Must be one of: {', '.join(VALID_BODY_IPV6)}",
            )

    # Validate device if present
    if "device" in payload:
        value = payload.get("device")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "device cannot exceed 15 characters")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate pppoe-egress-cos if present
    if "pppoe-egress-cos" in payload:
        value = payload.get("pppoe-egress-cos")
        if value and value not in VALID_BODY_PPPOE_EGRESS_COS:
            return (
                False,
                f"Invalid pppoe-egress-cos '{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_EGRESS_COS)}",
            )

    # Validate auth-type if present
    if "auth-type" in payload:
        value = payload.get("auth-type")
        if value and value not in VALID_BODY_AUTH_TYPE:
            return (
                False,
                f"Invalid auth-type '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_TYPE)}",
            )

    # Validate pppoe-unnumbered-negotiate if present
    if "pppoe-unnumbered-negotiate" in payload:
        value = payload.get("pppoe-unnumbered-negotiate")
        if value and value not in VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE:
            return (
                False,
                f"Invalid pppoe-unnumbered-negotiate '{value}'. Must be one of: {', '.join(VALID_BODY_PPPOE_UNNUMBERED_NEGOTIATE)}",
            )

    # Validate idle-timeout if present
    if "idle-timeout" in payload:
        value = payload.get("idle-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "idle-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"idle-timeout must be numeric, got: {value}")

    # Validate multilink if present
    if "multilink" in payload:
        value = payload.get("multilink")
        if value and value not in VALID_BODY_MULTILINK:
            return (
                False,
                f"Invalid multilink '{value}'. Must be one of: {', '.join(VALID_BODY_MULTILINK)}",
            )

    # Validate mrru if present
    if "mrru" in payload:
        value = payload.get("mrru")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 296 or int_val > 65535:
                    return (False, "mrru must be between 296 and 65535")
            except (ValueError, TypeError):
                return (False, f"mrru must be numeric, got: {value}")

    # Validate disc-retry-timeout if present
    if "disc-retry-timeout" in payload:
        value = payload.get("disc-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "disc-retry-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"disc-retry-timeout must be numeric, got: {value}",
                )

    # Validate padt-retry-timeout if present
    if "padt-retry-timeout" in payload:
        value = payload.get("padt-retry-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "padt-retry-timeout must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"padt-retry-timeout must be numeric, got: {value}",
                )

    # Validate service-name if present
    if "service-name" in payload:
        value = payload.get("service-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "service-name cannot exceed 63 characters")

    # Validate ac-name if present
    if "ac-name" in payload:
        value = payload.get("ac-name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "ac-name cannot exceed 63 characters")

    # Validate lcp-echo-interval if present
    if "lcp-echo-interval" in payload:
        value = payload.get("lcp-echo-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "lcp-echo-interval must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lcp-echo-interval must be numeric, got: {value}",
                )

    # Validate lcp-max-echo-fails if present
    if "lcp-max-echo-fails" in payload:
        value = payload.get("lcp-max-echo-fails")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32767:
                    return (
                        False,
                        "lcp-max-echo-fails must be between 0 and 32767",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lcp-max-echo-fails must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_pppoe_interface_delete(
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
