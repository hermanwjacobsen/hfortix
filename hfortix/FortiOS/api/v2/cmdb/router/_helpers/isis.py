"""
Validation helpers for router isis endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_IS_TYPE = ["level-1-2", "level-1", "level-2-only"]
VALID_BODY_ADV_PASSIVE_ONLY = ["enable", "disable"]
VALID_BODY_ADV_PASSIVE_ONLY6 = ["enable", "disable"]
VALID_BODY_AUTH_MODE_L1 = ["password", "md5"]
VALID_BODY_AUTH_MODE_L2 = ["password", "md5"]
VALID_BODY_AUTH_SENDONLY_L1 = ["enable", "disable"]
VALID_BODY_AUTH_SENDONLY_L2 = ["enable", "disable"]
VALID_BODY_IGNORE_LSP_ERRORS = ["enable", "disable"]
VALID_BODY_DYNAMIC_HOSTNAME = ["enable", "disable"]
VALID_BODY_ADJACENCY_CHECK = ["enable", "disable"]
VALID_BODY_ADJACENCY_CHECK6 = ["enable", "disable"]
VALID_BODY_OVERLOAD_BIT = ["enable", "disable"]
VALID_BODY_OVERLOAD_BIT_SUPPRESS = ["external", "interlevel"]
VALID_BODY_DEFAULT_ORIGINATE = ["enable", "disable"]
VALID_BODY_DEFAULT_ORIGINATE6 = ["enable", "disable"]
VALID_BODY_METRIC_STYLE = [
    "narrow",
    "wide",
    "transition",
    "narrow-transition",
    "narrow-transition-l1",
    "narrow-transition-l2",
    "wide-l1",
    "wide-l2",
    "wide-transition",
    "wide-transition-l1",
    "wide-transition-l2",
    "transition-l1",
    "transition-l2",
]
VALID_BODY_REDISTRIBUTE_L1 = ["enable", "disable"]
VALID_BODY_REDISTRIBUTE_L2 = ["enable", "disable"]
VALID_BODY_REDISTRIBUTE6_L1 = ["enable", "disable"]
VALID_BODY_REDISTRIBUTE6_L2 = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_isis_get(
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


def validate_isis_put(
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

    # Validate is-type if present
    if "is-type" in payload:
        value = payload.get("is-type")
        if value and value not in VALID_BODY_IS_TYPE:
            return (
                False,
                f"Invalid is-type '{value}'. Must be one of: {', '.join(VALID_BODY_IS_TYPE)}",
            )

    # Validate adv-passive-only if present
    if "adv-passive-only" in payload:
        value = payload.get("adv-passive-only")
        if value and value not in VALID_BODY_ADV_PASSIVE_ONLY:
            return (
                False,
                f"Invalid adv-passive-only '{value}'. Must be one of: {', '.join(VALID_BODY_ADV_PASSIVE_ONLY)}",
            )

    # Validate adv-passive-only6 if present
    if "adv-passive-only6" in payload:
        value = payload.get("adv-passive-only6")
        if value and value not in VALID_BODY_ADV_PASSIVE_ONLY6:
            return (
                False,
                f"Invalid adv-passive-only6 '{value}'. Must be one of: {', '.join(VALID_BODY_ADV_PASSIVE_ONLY6)}",
            )

    # Validate auth-mode-l1 if present
    if "auth-mode-l1" in payload:
        value = payload.get("auth-mode-l1")
        if value and value not in VALID_BODY_AUTH_MODE_L1:
            return (
                False,
                f"Invalid auth-mode-l1 '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_MODE_L1)}",
            )

    # Validate auth-mode-l2 if present
    if "auth-mode-l2" in payload:
        value = payload.get("auth-mode-l2")
        if value and value not in VALID_BODY_AUTH_MODE_L2:
            return (
                False,
                f"Invalid auth-mode-l2 '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_MODE_L2)}",
            )

    # Validate auth-keychain-l1 if present
    if "auth-keychain-l1" in payload:
        value = payload.get("auth-keychain-l1")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-keychain-l1 cannot exceed 35 characters")

    # Validate auth-keychain-l2 if present
    if "auth-keychain-l2" in payload:
        value = payload.get("auth-keychain-l2")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "auth-keychain-l2 cannot exceed 35 characters")

    # Validate auth-sendonly-l1 if present
    if "auth-sendonly-l1" in payload:
        value = payload.get("auth-sendonly-l1")
        if value and value not in VALID_BODY_AUTH_SENDONLY_L1:
            return (
                False,
                f"Invalid auth-sendonly-l1 '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SENDONLY_L1)}",
            )

    # Validate auth-sendonly-l2 if present
    if "auth-sendonly-l2" in payload:
        value = payload.get("auth-sendonly-l2")
        if value and value not in VALID_BODY_AUTH_SENDONLY_L2:
            return (
                False,
                f"Invalid auth-sendonly-l2 '{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_SENDONLY_L2)}",
            )

    # Validate ignore-lsp-errors if present
    if "ignore-lsp-errors" in payload:
        value = payload.get("ignore-lsp-errors")
        if value and value not in VALID_BODY_IGNORE_LSP_ERRORS:
            return (
                False,
                f"Invalid ignore-lsp-errors '{value}'. Must be one of: {', '.join(VALID_BODY_IGNORE_LSP_ERRORS)}",
            )

    # Validate lsp-gen-interval-l1 if present
    if "lsp-gen-interval-l1" in payload:
        value = payload.get("lsp-gen-interval-l1")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "lsp-gen-interval-l1 must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lsp-gen-interval-l1 must be numeric, got: {value}",
                )

    # Validate lsp-gen-interval-l2 if present
    if "lsp-gen-interval-l2" in payload:
        value = payload.get("lsp-gen-interval-l2")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 120:
                    return (
                        False,
                        "lsp-gen-interval-l2 must be between 1 and 120",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lsp-gen-interval-l2 must be numeric, got: {value}",
                )

    # Validate lsp-refresh-interval if present
    if "lsp-refresh-interval" in payload:
        value = payload.get("lsp-refresh-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "lsp-refresh-interval must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"lsp-refresh-interval must be numeric, got: {value}",
                )

    # Validate max-lsp-lifetime if present
    if "max-lsp-lifetime" in payload:
        value = payload.get("max-lsp-lifetime")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 350 or int_val > 65535:
                    return (
                        False,
                        "max-lsp-lifetime must be between 350 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-lsp-lifetime must be numeric, got: {value}",
                )

    # Validate dynamic-hostname if present
    if "dynamic-hostname" in payload:
        value = payload.get("dynamic-hostname")
        if value and value not in VALID_BODY_DYNAMIC_HOSTNAME:
            return (
                False,
                f"Invalid dynamic-hostname '{value}'. Must be one of: {', '.join(VALID_BODY_DYNAMIC_HOSTNAME)}",
            )

    # Validate adjacency-check if present
    if "adjacency-check" in payload:
        value = payload.get("adjacency-check")
        if value and value not in VALID_BODY_ADJACENCY_CHECK:
            return (
                False,
                f"Invalid adjacency-check '{value}'. Must be one of: {', '.join(VALID_BODY_ADJACENCY_CHECK)}",
            )

    # Validate adjacency-check6 if present
    if "adjacency-check6" in payload:
        value = payload.get("adjacency-check6")
        if value and value not in VALID_BODY_ADJACENCY_CHECK6:
            return (
                False,
                f"Invalid adjacency-check6 '{value}'. Must be one of: {', '.join(VALID_BODY_ADJACENCY_CHECK6)}",
            )

    # Validate overload-bit if present
    if "overload-bit" in payload:
        value = payload.get("overload-bit")
        if value and value not in VALID_BODY_OVERLOAD_BIT:
            return (
                False,
                f"Invalid overload-bit '{value}'. Must be one of: {', '.join(VALID_BODY_OVERLOAD_BIT)}",
            )

    # Validate overload-bit-suppress if present
    if "overload-bit-suppress" in payload:
        value = payload.get("overload-bit-suppress")
        if value and value not in VALID_BODY_OVERLOAD_BIT_SUPPRESS:
            return (
                False,
                f"Invalid overload-bit-suppress '{value}'. Must be one of: {', '.join(VALID_BODY_OVERLOAD_BIT_SUPPRESS)}",
            )

    # Validate overload-bit-on-startup if present
    if "overload-bit-on-startup" in payload:
        value = payload.get("overload-bit-on-startup")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 86400:
                    return (
                        False,
                        "overload-bit-on-startup must be between 5 and 86400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"overload-bit-on-startup must be numeric, got: {value}",
                )

    # Validate default-originate if present
    if "default-originate" in payload:
        value = payload.get("default-originate")
        if value and value not in VALID_BODY_DEFAULT_ORIGINATE:
            return (
                False,
                f"Invalid default-originate '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_ORIGINATE)}",
            )

    # Validate default-originate6 if present
    if "default-originate6" in payload:
        value = payload.get("default-originate6")
        if value and value not in VALID_BODY_DEFAULT_ORIGINATE6:
            return (
                False,
                f"Invalid default-originate6 '{value}'. Must be one of: {', '.join(VALID_BODY_DEFAULT_ORIGINATE6)}",
            )

    # Validate metric-style if present
    if "metric-style" in payload:
        value = payload.get("metric-style")
        if value and value not in VALID_BODY_METRIC_STYLE:
            return (
                False,
                f"Invalid metric-style '{value}'. Must be one of: {', '.join(VALID_BODY_METRIC_STYLE)}",
            )

    # Validate redistribute-l1 if present
    if "redistribute-l1" in payload:
        value = payload.get("redistribute-l1")
        if value and value not in VALID_BODY_REDISTRIBUTE_L1:
            return (
                False,
                f"Invalid redistribute-l1 '{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE_L1)}",
            )

    # Validate redistribute-l1-list if present
    if "redistribute-l1-list" in payload:
        value = payload.get("redistribute-l1-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "redistribute-l1-list cannot exceed 35 characters")

    # Validate redistribute-l2 if present
    if "redistribute-l2" in payload:
        value = payload.get("redistribute-l2")
        if value and value not in VALID_BODY_REDISTRIBUTE_L2:
            return (
                False,
                f"Invalid redistribute-l2 '{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE_L2)}",
            )

    # Validate redistribute-l2-list if present
    if "redistribute-l2-list" in payload:
        value = payload.get("redistribute-l2-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "redistribute-l2-list cannot exceed 35 characters")

    # Validate redistribute6-l1 if present
    if "redistribute6-l1" in payload:
        value = payload.get("redistribute6-l1")
        if value and value not in VALID_BODY_REDISTRIBUTE6_L1:
            return (
                False,
                f"Invalid redistribute6-l1 '{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE6_L1)}",
            )

    # Validate redistribute6-l1-list if present
    if "redistribute6-l1-list" in payload:
        value = payload.get("redistribute6-l1-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "redistribute6-l1-list cannot exceed 35 characters",
            )

    # Validate redistribute6-l2 if present
    if "redistribute6-l2" in payload:
        value = payload.get("redistribute6-l2")
        if value and value not in VALID_BODY_REDISTRIBUTE6_L2:
            return (
                False,
                f"Invalid redistribute6-l2 '{value}'. Must be one of: {', '.join(VALID_BODY_REDISTRIBUTE6_L2)}",
            )

    # Validate redistribute6-l2-list if present
    if "redistribute6-l2-list" in payload:
        value = payload.get("redistribute6-l2-list")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "redistribute6-l2-list cannot exceed 35 characters",
            )

    return (True, None)
