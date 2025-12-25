"""
Validation helpers for system password_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ['enable', 'disable']
VALID_BODY_APPLY_TO = ['admin-password', 'ipsec-preshared-key']
VALID_BODY_EXPIRE_STATUS = ['enable', 'disable']
VALID_BODY_REUSE_PASSWORD = ['enable', 'disable']
VALID_BODY_LOGIN_LOCKOUT_UPON_WEAKER_ENCRYPTION = ['enable', 'disable']
VALID_QUERY_ACTION = ['default', 'schema']

# ============================================================================
# GET Validation
# ============================================================================


def validate_password_policy_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any
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
    if 'action' in params:
        value = params.get('action')
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: "
                f"{', '.join(VALID_QUERY_ACTION)}"
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_password_policy_put(
    payload: dict[str, Any] | None = None
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
    if 'status' in payload:
        value = payload.get('status')
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}"
            )

    # Validate apply-to if present
    if 'apply-to' in payload:
        value = payload.get('apply-to')
        if value and value not in VALID_BODY_APPLY_TO:
            return (
                False,
                f"Invalid apply-to '{value}'. Must be one of: {', '.join(VALID_BODY_APPLY_TO)}"
            )

    # Validate minimum-length if present
    if 'minimum-length' in payload:
        value = payload.get('minimum-length')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 12 or int_val > 128:
                    return (False, "minimum-length must be between 12 and 128")
            except (ValueError, TypeError):
                return (False, f"minimum-length must be numeric, got: {value}")

    # Validate min-lower-case-letter if present
    if 'min-lower-case-letter' in payload:
        value = payload.get('min-lower-case-letter')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False, "min-lower-case-letter must be between 0 and 128")
            except (ValueError, TypeError):
                return (
                    False, f"min-lower-case-letter must be numeric, got: {value}")

    # Validate min-upper-case-letter if present
    if 'min-upper-case-letter' in payload:
        value = payload.get('min-upper-case-letter')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False, "min-upper-case-letter must be between 0 and 128")
            except (ValueError, TypeError):
                return (
                    False, f"min-upper-case-letter must be numeric, got: {value}")

    # Validate min-non-alphanumeric if present
    if 'min-non-alphanumeric' in payload:
        value = payload.get('min-non-alphanumeric')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False, "min-non-alphanumeric must be between 0 and 128")
            except (ValueError, TypeError):
                return (
                    False, f"min-non-alphanumeric must be numeric, got: {value}")

    # Validate min-number if present
    if 'min-number' in payload:
        value = payload.get('min-number')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (False, "min-number must be between 0 and 128")
            except (ValueError, TypeError):
                return (False, f"min-number must be numeric, got: {value}")

    # Validate expire-status if present
    if 'expire-status' in payload:
        value = payload.get('expire-status')
        if value and value not in VALID_BODY_EXPIRE_STATUS:
            return (
                False,
                f"Invalid expire-status '{value}'. Must be one of: {', '.join(VALID_BODY_EXPIRE_STATUS)}"
            )

    # Validate expire-day if present
    if 'expire-day' in payload:
        value = payload.get('expire-day')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 999:
                    return (False, "expire-day must be between 1 and 999")
            except (ValueError, TypeError):
                return (False, f"expire-day must be numeric, got: {value}")

    # Validate reuse-password if present
    if 'reuse-password' in payload:
        value = payload.get('reuse-password')
        if value and value not in VALID_BODY_REUSE_PASSWORD:
            return (
                False,
                f"Invalid reuse-password '{value}'. Must be one of: {', '.join(VALID_BODY_REUSE_PASSWORD)}"
            )

    # Validate reuse-password-limit if present
    if 'reuse-password-limit' in payload:
        value = payload.get('reuse-password-limit')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 20:
                    return (
                        False, "reuse-password-limit must be between 0 and 20")
            except (ValueError, TypeError):
                return (
                    False, f"reuse-password-limit must be numeric, got: {value}")

    # Validate login-lockout-upon-weaker-encryption if present
    if 'login-lockout-upon-weaker-encryption' in payload:
        value = payload.get('login-lockout-upon-weaker-encryption')
        if value and value not in VALID_BODY_LOGIN_LOCKOUT_UPON_WEAKER_ENCRYPTION:
            return (
                False,
                f"Invalid login-lockout-upon-weaker-encryption '{value}'. Must be one of: {', '.join(VALID_BODY_LOGIN_LOCKOUT_UPON_WEAKER_ENCRYPTION)}")

    return (True, None)
