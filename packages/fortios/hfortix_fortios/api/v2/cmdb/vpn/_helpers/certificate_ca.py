"""
Validation helpers for vpn certificate_ca endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_RANGE = ["global", "vdom"]
VALID_BODY_SOURCE = ["factory", "user", "bundle"]
VALID_BODY_SSL_INSPECTION_TRUSTED = ["enable", "disable"]
VALID_BODY_OBSOLETE = ["disable", "enable"]
VALID_BODY_FABRIC_CA = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_certificate_ca_get(
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


def validate_certificate_ca_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating certificate_ca.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate range if present
    if "range" in payload:
        value = payload.get("range")
        if value and value not in VALID_BODY_RANGE:
            return (
                False,
                f"Invalid range '{value}'. Must be one of: {', '.join(VALID_BODY_RANGE)}",
            )

    # Validate source if present
    if "source" in payload:
        value = payload.get("source")
        if value and value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid source '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )

    # Validate ssl-inspection-trusted if present
    if "ssl-inspection-trusted" in payload:
        value = payload.get("ssl-inspection-trusted")
        if value and value not in VALID_BODY_SSL_INSPECTION_TRUSTED:
            return (
                False,
                f"Invalid ssl-inspection-trusted '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_INSPECTION_TRUSTED)}",
            )

    # Validate scep-url if present
    if "scep-url" in payload:
        value = payload.get("scep-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "scep-url cannot exceed 255 characters")

    # Validate est-url if present
    if "est-url" in payload:
        value = payload.get("est-url")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "est-url cannot exceed 255 characters")

    # Validate auto-update-days if present
    if "auto-update-days" in payload:
        value = payload.get("auto-update-days")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "auto-update-days must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-update-days must be numeric, got: {value}",
                )

    # Validate auto-update-days-warning if present
    if "auto-update-days-warning" in payload:
        value = payload.get("auto-update-days-warning")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "auto-update-days-warning must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"auto-update-days-warning must be numeric, got: {value}",
                )

    # Validate ca-identifier if present
    if "ca-identifier" in payload:
        value = payload.get("ca-identifier")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "ca-identifier cannot exceed 255 characters")

    # Validate obsolete if present
    if "obsolete" in payload:
        value = payload.get("obsolete")
        if value and value not in VALID_BODY_OBSOLETE:
            return (
                False,
                f"Invalid obsolete '{value}'. Must be one of: {', '.join(VALID_BODY_OBSOLETE)}",
            )

    # Validate fabric-ca if present
    if "fabric-ca" in payload:
        value = payload.get("fabric-ca")
        if value and value not in VALID_BODY_FABRIC_CA:
            return (
                False,
                f"Invalid fabric-ca '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_CA)}",
            )

    return (True, None)
