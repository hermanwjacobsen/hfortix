"""
Validation helpers for system ntp endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_NTPSYNC = ["enable", "disable"]
VALID_BODY_TYPE = ["fortiguard", "custom"]
VALID_BODY_SERVER_MODE = ["enable", "disable"]
VALID_BODY_AUTHENTICATION = ["enable", "disable"]
VALID_BODY_KEY_TYPE = ["MD5", "SHA1", "SHA256"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ntp_get(
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


def validate_ntp_put(
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

    # Validate ntpsync if present
    if "ntpsync" in payload:
        value = payload.get("ntpsync")
        if value and value not in VALID_BODY_NTPSYNC:
            return (
                False,
                f"Invalid ntpsync '{value}'. Must be one of: {', '.join(VALID_BODY_NTPSYNC)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate syncinterval if present
    if "syncinterval" in payload:
        value = payload.get("syncinterval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 1440:
                    return (False, "syncinterval must be between 1 and 1440")
            except (ValueError, TypeError):
                return (False, f"syncinterval must be numeric, got: {value}")

    # Validate server-mode if present
    if "server-mode" in payload:
        value = payload.get("server-mode")
        if value and value not in VALID_BODY_SERVER_MODE:
            return (
                False,
                f"Invalid server-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_MODE)}",
            )

    # Validate authentication if present
    if "authentication" in payload:
        value = payload.get("authentication")
        if value and value not in VALID_BODY_AUTHENTICATION:
            return (
                False,
                f"Invalid authentication '{value}'. Must be one of: {', '.join(VALID_BODY_AUTHENTICATION)}",
            )

    # Validate key-type if present
    if "key-type" in payload:
        value = payload.get("key-type")
        if value and value not in VALID_BODY_KEY_TYPE:
            return (
                False,
                f"Invalid key-type '{value}'. Must be one of: {', '.join(VALID_BODY_KEY_TYPE)}",
            )

    # Validate key-id if present
    if "key-id" in payload:
        value = payload.get("key-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "key-id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"key-id must be numeric, got: {value}")

    return (True, None)
