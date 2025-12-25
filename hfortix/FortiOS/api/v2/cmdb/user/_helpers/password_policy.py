"""
Validation helpers for user password_policy endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_EXPIRE_STATUS = ['enable', 'disable']
VALID_BODY_EXPIRED_PASSWORD_RENEWAL = ['enable', 'disable']
VALID_BODY_REUSE_PASSWORD = ['enable', 'disable']
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
# POST Validation
# ============================================================================


def validate_password_policy_post(
        payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating password_policy.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if 'name' in payload:
        value = payload.get('name')
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate expire-status if present
    if 'expire-status' in payload:
        value = payload.get('expire-status')
        if value and value not in VALID_BODY_EXPIRE_STATUS:
            return (
                False,
                f"Invalid expire-status '{value}'. Must be one of: "
                f"{', '.join(VALID_BODY_EXPIRE_STATUS)}"
            )

    # Validate expire-days if present
    if 'expire-days' in payload:
        value = payload.get('expire-days')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 999:
                    return (False, "expire-days must be between 0 and 999")
            except (ValueError, TypeError):
                return (False, f"expire-days must be numeric, got: {value}")

    # Validate warn-days if present
    if 'warn-days' in payload:
        value = payload.get('warn-days')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 30:
                    return (False, "warn-days must be between 0 and 30")
            except (ValueError, TypeError):
                return (False, f"warn-days must be numeric, got: {value}")

    # Validate expired-password-renewal if present
    if 'expired-password-renewal' in payload:
        value = payload.get('expired-password-renewal')
        if value and value not in VALID_BODY_EXPIRED_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid expired-password-renewal '{value}'. Must be one of: "
                f"{', '.join(VALID_BODY_EXPIRED_PASSWORD_RENEWAL)}"
            )

    # Validate minimum-length if present
    if 'minimum-length' in payload:
        value = payload.get('minimum-length')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 8 or int_val > 128:
                    return (False, "minimum-length must be between 8 and 128")
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
                        False,
                        "min-lower-case-letter must be between 0 and 128"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"min-lower-case-letter must be numeric, "
                    f"got: {value}"
                )

    # Validate min-upper-case-letter if present
    if 'min-upper-case-letter' in payload:
        value = payload.get('min-upper-case-letter')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "min-upper-case-letter must be between 0 and 128"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"min-upper-case-letter must be numeric, "
                    f"got: {value}"
                )

    # Validate min-non-alphanumeric if present
    if 'min-non-alphanumeric' in payload:
        value = payload.get('min-non-alphanumeric')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "min-non-alphanumeric must be between 0 and 128"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"min-non-alphanumeric must be numeric, "
                    f"got: {value}"
                )

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

    # Validate min-change-characters if present
    if 'min-change-characters' in payload:
        value = payload.get('min-change-characters')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "min-change-characters must be between 0 and 128"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"min-change-characters must be numeric, "
                    f"got: {value}"
                )

    # Validate reuse-password if present
    if 'reuse-password' in payload:
        value = payload.get('reuse-password')
        if value and value not in VALID_BODY_REUSE_PASSWORD:
            return (
                False,
                f"Invalid reuse-password '{value}'. Must be one of: "
                f"{', '.join(VALID_BODY_REUSE_PASSWORD)}"
            )

    # Validate reuse-password-limit if present
    if 'reuse-password-limit' in payload:
        value = payload.get('reuse-password-limit')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 20:
                    return (
                        False,
                        "reuse-password-limit must be between 0 and 20"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reuse-password-limit must be numeric, "
                    f"got: {value}"
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_password_policy_put(
    name: str | None = None,
    payload: dict[str, Any] | None = None
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
    if 'name' in payload:
        value = payload.get('name')
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "name cannot exceed 35 characters")

    # Validate expire-status if present
    if 'expire-status' in payload:
        value = payload.get('expire-status')
        if value and value not in VALID_BODY_EXPIRE_STATUS:
            return (
                False,
                f"Invalid expire-status '{value}'. Must be one of: "
                f"{', '.join(VALID_BODY_EXPIRE_STATUS)}"
            )

    # Validate expire-days if present
    if 'expire-days' in payload:
        value = payload.get('expire-days')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 999:
                    return (False, "expire-days must be between 0 and 999")
            except (ValueError, TypeError):
                return (False, f"expire-days must be numeric, got: {value}")

    # Validate warn-days if present
    if 'warn-days' in payload:
        value = payload.get('warn-days')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 30:
                    return (False, "warn-days must be between 0 and 30")
            except (ValueError, TypeError):
                return (False, f"warn-days must be numeric, got: {value}")

    # Validate expired-password-renewal if present
    if 'expired-password-renewal' in payload:
        value = payload.get('expired-password-renewal')
        if value and value not in VALID_BODY_EXPIRED_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid expired-password-renewal '{value}'. Must be one of: "
                f"{', '.join(VALID_BODY_EXPIRED_PASSWORD_RENEWAL)}"
            )

    # Validate minimum-length if present
    if 'minimum-length' in payload:
        value = payload.get('minimum-length')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 8 or int_val > 128:
                    return (False, "minimum-length must be between 8 and 128")
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
                        False,
                        "min-lower-case-letter must be between 0 and 128"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"min-lower-case-letter must be numeric, "
                    f"got: {value}"
                )

    # Validate min-upper-case-letter if present
    if 'min-upper-case-letter' in payload:
        value = payload.get('min-upper-case-letter')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "min-upper-case-letter must be between 0 and 128"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"min-upper-case-letter must be numeric, "
                    f"got: {value}"
                )

    # Validate min-non-alphanumeric if present
    if 'min-non-alphanumeric' in payload:
        value = payload.get('min-non-alphanumeric')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "min-non-alphanumeric must be between 0 and 128"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"min-non-alphanumeric must be numeric, "
                    f"got: {value}"
                )

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

    # Validate min-change-characters if present
    if 'min-change-characters' in payload:
        value = payload.get('min-change-characters')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 128:
                    return (
                        False,
                        "min-change-characters must be between 0 and 128"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"min-change-characters must be numeric, "
                    f"got: {value}"
                )

    # Validate reuse-password if present
    if 'reuse-password' in payload:
        value = payload.get('reuse-password')
        if value and value not in VALID_BODY_REUSE_PASSWORD:
            return (
                False,
                f"Invalid reuse-password '{value}'. Must be one of: "
                f"{', '.join(VALID_BODY_REUSE_PASSWORD)}"
            )

    # Validate reuse-password-limit if present
    if 'reuse-password-limit' in payload:
        value = payload.get('reuse-password-limit')
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 20:
                    return (
                        False,
                        "reuse-password-limit must be between 0 and 20"
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"reuse-password-limit must be numeric, "
                    f"got: {value}"
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_password_policy_delete(
        name: str | None = None) -> tuple[bool, str | None]:
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
