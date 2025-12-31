"""
Validation helpers for dlp data_type endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_VERIFY_TRANSFORMED_PATTERN = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_data_type_get(
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


def validate_data_type_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating data_type.

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

    # Validate pattern if present
    if "pattern" in payload:
        value = payload.get("pattern")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "pattern cannot exceed 255 characters")

    # Validate verify if present
    if "verify" in payload:
        value = payload.get("verify")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "verify cannot exceed 255 characters")

    # Validate verify2 if present
    if "verify2" in payload:
        value = payload.get("verify2")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "verify2 cannot exceed 255 characters")

    # Validate match-around if present
    if "match-around" in payload:
        value = payload.get("match-around")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "match-around cannot exceed 35 characters")

    # Validate look-back if present
    if "look-back" in payload:
        value = payload.get("look-back")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "look-back must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"look-back must be numeric, got: {value}")

    # Validate look-ahead if present
    if "look-ahead" in payload:
        value = payload.get("look-ahead")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "look-ahead must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"look-ahead must be numeric, got: {value}")

    # Validate match-back if present
    if "match-back" in payload:
        value = payload.get("match-back")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4096:
                    return (False, "match-back must be between 1 and 4096")
            except (ValueError, TypeError):
                return (False, f"match-back must be numeric, got: {value}")

    # Validate match-ahead if present
    if "match-ahead" in payload:
        value = payload.get("match-ahead")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4096:
                    return (False, "match-ahead must be between 1 and 4096")
            except (ValueError, TypeError):
                return (False, f"match-ahead must be numeric, got: {value}")

    # Validate transform if present
    if "transform" in payload:
        value = payload.get("transform")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "transform cannot exceed 255 characters")

    # Validate verify-transformed-pattern if present
    if "verify-transformed-pattern" in payload:
        value = payload.get("verify-transformed-pattern")
        if value and value not in VALID_BODY_VERIFY_TRANSFORMED_PATTERN:
            return (
                False,
                f"Invalid verify-transformed-pattern '{value}'. Must be one of: {', '.join(VALID_BODY_VERIFY_TRANSFORMED_PATTERN)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_data_type_put(
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

    # Validate pattern if present
    if "pattern" in payload:
        value = payload.get("pattern")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "pattern cannot exceed 255 characters")

    # Validate verify if present
    if "verify" in payload:
        value = payload.get("verify")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "verify cannot exceed 255 characters")

    # Validate verify2 if present
    if "verify2" in payload:
        value = payload.get("verify2")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "verify2 cannot exceed 255 characters")

    # Validate match-around if present
    if "match-around" in payload:
        value = payload.get("match-around")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "match-around cannot exceed 35 characters")

    # Validate look-back if present
    if "look-back" in payload:
        value = payload.get("look-back")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "look-back must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"look-back must be numeric, got: {value}")

    # Validate look-ahead if present
    if "look-ahead" in payload:
        value = payload.get("look-ahead")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 255:
                    return (False, "look-ahead must be between 1 and 255")
            except (ValueError, TypeError):
                return (False, f"look-ahead must be numeric, got: {value}")

    # Validate match-back if present
    if "match-back" in payload:
        value = payload.get("match-back")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4096:
                    return (False, "match-back must be between 1 and 4096")
            except (ValueError, TypeError):
                return (False, f"match-back must be numeric, got: {value}")

    # Validate match-ahead if present
    if "match-ahead" in payload:
        value = payload.get("match-ahead")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4096:
                    return (False, "match-ahead must be between 1 and 4096")
            except (ValueError, TypeError):
                return (False, f"match-ahead must be numeric, got: {value}")

    # Validate transform if present
    if "transform" in payload:
        value = payload.get("transform")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "transform cannot exceed 255 characters")

    # Validate verify-transformed-pattern if present
    if "verify-transformed-pattern" in payload:
        value = payload.get("verify-transformed-pattern")
        if value and value not in VALID_BODY_VERIFY_TRANSFORMED_PATTERN:
            return (
                False,
                f"Invalid verify-transformed-pattern '{value}'. Must be one of: {', '.join(VALID_BODY_VERIFY_TRANSFORMED_PATTERN)}",
            )

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_data_type_delete(
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
