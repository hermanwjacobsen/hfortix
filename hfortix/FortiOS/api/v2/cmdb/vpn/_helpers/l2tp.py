"""
Validation helpers for vpn l2tp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_ENFORCE_IPSEC = ["enable", "disable"]
VALID_BODY_COMPRESS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_l2tp_get(
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


def validate_l2tp_put(
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

    # Validate usrgrp if present
    if "usrgrp" in payload:
        value = payload.get("usrgrp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "usrgrp cannot exceed 35 characters")

    # Validate enforce-ipsec if present
    if "enforce-ipsec" in payload:
        value = payload.get("enforce-ipsec")
        if value and value not in VALID_BODY_ENFORCE_IPSEC:
            return (
                False,
                f"Invalid enforce-ipsec '{value}'. Must be one of: {', '.join(VALID_BODY_ENFORCE_IPSEC)}",
            )

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

    # Validate hello-interval if present
    if "hello-interval" in payload:
        value = payload.get("hello-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3600:
                    return (
                        False,
                        "hello-interval must be between 0 and 3600",
                    )
            except (ValueError, TypeError):
                return (False, f"hello-interval must be numeric, got: {value}")

    # Validate compress if present
    if "compress" in payload:
        value = payload.get("compress")
        if value and value not in VALID_BODY_COMPRESS:
            return (
                False,
                f"Invalid compress '{value}'. Must be one of: {', '.join(VALID_BODY_COMPRESS)}",
            )

    return (True, None)
