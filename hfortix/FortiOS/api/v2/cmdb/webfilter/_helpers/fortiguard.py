"""
Validation helpers for webfilter fortiguard endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_CACHE_MODE = ["ttl", "db-ver"]
VALID_BODY_CACHE_PREFIX_MATCH = ["enable", "disable"]
VALID_BODY_OVRD_AUTH_HTTPS = ["enable", "disable"]
VALID_BODY_WARN_AUTH_HTTPS = ["enable", "disable"]
VALID_BODY_CLOSE_PORTS = ["enable", "disable"]
VALID_BODY_EMBED_IMAGE = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_fortiguard_get(
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


def validate_fortiguard_put(
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

    # Validate cache-mode if present
    if "cache-mode" in payload:
        value = payload.get("cache-mode")
        if value and value not in VALID_BODY_CACHE_MODE:
            return (
                False,
                f"Invalid cache-mode '{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_MODE)}",
            )

    # Validate cache-prefix-match if present
    if "cache-prefix-match" in payload:
        value = payload.get("cache-prefix-match")
        if value and value not in VALID_BODY_CACHE_PREFIX_MATCH:
            return (
                False,
                f"Invalid cache-prefix-match '{value}'. Must be one of: {', '.join(VALID_BODY_CACHE_PREFIX_MATCH)}",
            )

    # Validate cache-mem-permille if present
    if "cache-mem-permille" in payload:
        value = payload.get("cache-mem-permille")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 150:
                    return (
                        False,
                        "cache-mem-permille must be between 1 and 150",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"cache-mem-permille must be numeric, got: {value}",
                )

    # Validate ovrd-auth-port-http if present
    if "ovrd-auth-port-http" in payload:
        value = payload.get("ovrd-auth-port-http")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "ovrd-auth-port-http must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ovrd-auth-port-http must be numeric, got: {value}",
                )

    # Validate ovrd-auth-port-https if present
    if "ovrd-auth-port-https" in payload:
        value = payload.get("ovrd-auth-port-https")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "ovrd-auth-port-https must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ovrd-auth-port-https must be numeric, got: {value}",
                )

    # Validate ovrd-auth-port-https-flow if present
    if "ovrd-auth-port-https-flow" in payload:
        value = payload.get("ovrd-auth-port-https-flow")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "ovrd-auth-port-https-flow must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ovrd-auth-port-https-flow must be numeric, got: {value}",
                )

    # Validate ovrd-auth-port-warning if present
    if "ovrd-auth-port-warning" in payload:
        value = payload.get("ovrd-auth-port-warning")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "ovrd-auth-port-warning must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ovrd-auth-port-warning must be numeric, got: {value}",
                )

    # Validate ovrd-auth-https if present
    if "ovrd-auth-https" in payload:
        value = payload.get("ovrd-auth-https")
        if value and value not in VALID_BODY_OVRD_AUTH_HTTPS:
            return (
                False,
                f"Invalid ovrd-auth-https '{value}'. Must be one of: {', '.join(VALID_BODY_OVRD_AUTH_HTTPS)}",
            )

    # Validate warn-auth-https if present
    if "warn-auth-https" in payload:
        value = payload.get("warn-auth-https")
        if value and value not in VALID_BODY_WARN_AUTH_HTTPS:
            return (
                False,
                f"Invalid warn-auth-https '{value}'. Must be one of: {', '.join(VALID_BODY_WARN_AUTH_HTTPS)}",
            )

    # Validate close-ports if present
    if "close-ports" in payload:
        value = payload.get("close-ports")
        if value and value not in VALID_BODY_CLOSE_PORTS:
            return (
                False,
                f"Invalid close-ports '{value}'. Must be one of: {', '.join(VALID_BODY_CLOSE_PORTS)}",
            )

    # Validate request-packet-size-limit if present
    if "request-packet-size-limit" in payload:
        value = payload.get("request-packet-size-limit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 576 or int_val > 10000:
                    return (
                        False,
                        "request-packet-size-limit must be between 576 and 10000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"request-packet-size-limit must be numeric, got: {value}",
                )

    # Validate embed-image if present
    if "embed-image" in payload:
        value = payload.get("embed-image")
        if value and value not in VALID_BODY_EMBED_IMAGE:
            return (
                False,
                f"Invalid embed-image '{value}'. Must be one of: {', '.join(VALID_BODY_EMBED_IMAGE)}",
            )

    return (True, None)
