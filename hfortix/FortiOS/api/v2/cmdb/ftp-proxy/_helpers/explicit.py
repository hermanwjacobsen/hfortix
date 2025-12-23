"""
Validation helpers for ftp-proxy explicit endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_SEC_DEFAULT_ACTION = ["accept", "deny"]
VALID_BODY_SERVER_DATA_MODE = ["client", "passive"]
VALID_BODY_SSL = ["enable", "disable"]
VALID_BODY_SSL_DH_BITS = ["768", "1024", "1536", "2048"]
VALID_BODY_SSL_ALGORITHM = ["high", "medium", "low"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_explicit_get(
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


def validate_explicit_put(
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

    # Validate sec-default-action if present
    if "sec-default-action" in payload:
        value = payload.get("sec-default-action")
        if value and value not in VALID_BODY_SEC_DEFAULT_ACTION:
            return (
                False,
                f"Invalid sec-default-action '{value}'. Must be one of: {', '.join(VALID_BODY_SEC_DEFAULT_ACTION)}",
            )

    # Validate server-data-mode if present
    if "server-data-mode" in payload:
        value = payload.get("server-data-mode")
        if value and value not in VALID_BODY_SERVER_DATA_MODE:
            return (
                False,
                f"Invalid server-data-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_DATA_MODE)}",
            )

    # Validate ssl if present
    if "ssl" in payload:
        value = payload.get("ssl")
        if value and value not in VALID_BODY_SSL:
            return (
                False,
                f"Invalid ssl '{value}'. Must be one of: {', '.join(VALID_BODY_SSL)}",
            )

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate ssl-algorithm if present
    if "ssl-algorithm" in payload:
        value = payload.get("ssl-algorithm")
        if value and value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid ssl-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )

    return (True, None)
