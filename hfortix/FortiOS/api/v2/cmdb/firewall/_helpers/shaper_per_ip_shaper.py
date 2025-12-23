"""
Validation helpers for firewall shaper_per_ip_shaper endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_BANDWIDTH_UNIT = ["kbps", "mbps", "gbps"]
VALID_BODY_DIFFSERV_FORWARD = ["enable", "disable"]
VALID_BODY_DIFFSERV_REVERSE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_shaper_per_ip_shaper_get(
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


def validate_shaper_per_ip_shaper_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating shaper_per_ip_shaper.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate max-bandwidth if present
    if "max-bandwidth" in payload:
        value = payload.get("max-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "max-bandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (False, f"max-bandwidth must be numeric, got: {value}")

    # Validate bandwidth-unit if present
    if "bandwidth-unit" in payload:
        value = payload.get("bandwidth-unit")
        if value and value not in VALID_BODY_BANDWIDTH_UNIT:
            return (
                False,
                f"Invalid bandwidth-unit '{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_UNIT)}",
            )

    # Validate max-concurrent-session if present
    if "max-concurrent-session" in payload:
        value = payload.get("max-concurrent-session")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "max-concurrent-session must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-concurrent-session must be numeric, got: {value}",
                )

    # Validate max-concurrent-tcp-session if present
    if "max-concurrent-tcp-session" in payload:
        value = payload.get("max-concurrent-tcp-session")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "max-concurrent-tcp-session must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-concurrent-tcp-session must be numeric, got: {value}",
                )

    # Validate max-concurrent-udp-session if present
    if "max-concurrent-udp-session" in payload:
        value = payload.get("max-concurrent-udp-session")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "max-concurrent-udp-session must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-concurrent-udp-session must be numeric, got: {value}",
                )

    # Validate diffserv-forward if present
    if "diffserv-forward" in payload:
        value = payload.get("diffserv-forward")
        if value and value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid diffserv-forward '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )

    # Validate diffserv-reverse if present
    if "diffserv-reverse" in payload:
        value = payload.get("diffserv-reverse")
        if value and value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid diffserv-reverse '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_shaper_per_ip_shaper_put(
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
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate max-bandwidth if present
    if "max-bandwidth" in payload:
        value = payload.get("max-bandwidth")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 80000000:
                    return (
                        False,
                        "max-bandwidth must be between 0 and 80000000",
                    )
            except (ValueError, TypeError):
                return (False, f"max-bandwidth must be numeric, got: {value}")

    # Validate bandwidth-unit if present
    if "bandwidth-unit" in payload:
        value = payload.get("bandwidth-unit")
        if value and value not in VALID_BODY_BANDWIDTH_UNIT:
            return (
                False,
                f"Invalid bandwidth-unit '{value}'. Must be one of: {', '.join(VALID_BODY_BANDWIDTH_UNIT)}",
            )

    # Validate max-concurrent-session if present
    if "max-concurrent-session" in payload:
        value = payload.get("max-concurrent-session")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "max-concurrent-session must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-concurrent-session must be numeric, got: {value}",
                )

    # Validate max-concurrent-tcp-session if present
    if "max-concurrent-tcp-session" in payload:
        value = payload.get("max-concurrent-tcp-session")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "max-concurrent-tcp-session must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-concurrent-tcp-session must be numeric, got: {value}",
                )

    # Validate max-concurrent-udp-session if present
    if "max-concurrent-udp-session" in payload:
        value = payload.get("max-concurrent-udp-session")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2097000:
                    return (
                        False,
                        "max-concurrent-udp-session must be between 0 and 2097000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-concurrent-udp-session must be numeric, got: {value}",
                )

    # Validate diffserv-forward if present
    if "diffserv-forward" in payload:
        value = payload.get("diffserv-forward")
        if value and value not in VALID_BODY_DIFFSERV_FORWARD:
            return (
                False,
                f"Invalid diffserv-forward '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_FORWARD)}",
            )

    # Validate diffserv-reverse if present
    if "diffserv-reverse" in payload:
        value = payload.get("diffserv-reverse")
        if value and value not in VALID_BODY_DIFFSERV_REVERSE:
            return (
                False,
                f"Invalid diffserv-reverse '{value}'. Must be one of: {', '.join(VALID_BODY_DIFFSERV_REVERSE)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_shaper_per_ip_shaper_delete(
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
