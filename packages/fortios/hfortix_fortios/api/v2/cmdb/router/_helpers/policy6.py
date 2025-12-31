"""
Validation helpers for router policy6 endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_INPUT_DEVICE_NEGATE = ["enable", "disable"]
VALID_BODY_SRC_NEGATE = ["enable", "disable"]
VALID_BODY_DST_NEGATE = ["enable", "disable"]
VALID_BODY_ACTION = ["deny", "permit"]
VALID_BODY_STATUS = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_policy6_get(
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


def validate_policy6_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating policy6.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate seq-num if present
    if "seq-num" in payload:
        value = payload.get("seq-num")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "seq-num must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"seq-num must be numeric, got: {value}")

    # Validate input-device-negate if present
    if "input-device-negate" in payload:
        value = payload.get("input-device-negate")
        if value and value not in VALID_BODY_INPUT_DEVICE_NEGATE:
            return (
                False,
                f"Invalid input-device-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INPUT_DEVICE_NEGATE)}",
            )

    # Validate src-negate if present
    if "src-negate" in payload:
        value = payload.get("src-negate")
        if value and value not in VALID_BODY_SRC_NEGATE:
            return (
                False,
                f"Invalid src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRC_NEGATE)}",
            )

    # Validate dst-negate if present
    if "dst-negate" in payload:
        value = payload.get("dst-negate")
        if value and value not in VALID_BODY_DST_NEGATE:
            return (
                False,
                f"Invalid dst-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DST_NEGATE)}",
            )

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate start-port if present
    if "start-port" in payload:
        value = payload.get("start-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "start-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"start-port must be numeric, got: {value}")

    # Validate end-port if present
    if "end-port" in payload:
        value = payload.get("end-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "end-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"end-port must be numeric, got: {value}")

    # Validate start-source-port if present
    if "start-source-port" in payload:
        value = payload.get("start-source-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "start-source-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"start-source-port must be numeric, got: {value}",
                )

    # Validate end-source-port if present
    if "end-source-port" in payload:
        value = payload.get("end-source-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "end-source-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"end-source-port must be numeric, got: {value}",
                )

    # Validate output-device if present
    if "output-device" in payload:
        value = payload.get("output-device")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "output-device cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_policy6_put(
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

    # Validate seq-num if present
    if "seq-num" in payload:
        value = payload.get("seq-num")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "seq-num must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"seq-num must be numeric, got: {value}")

    # Validate input-device-negate if present
    if "input-device-negate" in payload:
        value = payload.get("input-device-negate")
        if value and value not in VALID_BODY_INPUT_DEVICE_NEGATE:
            return (
                False,
                f"Invalid input-device-negate '{value}'. Must be one of: {', '.join(VALID_BODY_INPUT_DEVICE_NEGATE)}",
            )

    # Validate src-negate if present
    if "src-negate" in payload:
        value = payload.get("src-negate")
        if value and value not in VALID_BODY_SRC_NEGATE:
            return (
                False,
                f"Invalid src-negate '{value}'. Must be one of: {', '.join(VALID_BODY_SRC_NEGATE)}",
            )

    # Validate dst-negate if present
    if "dst-negate" in payload:
        value = payload.get("dst-negate")
        if value and value not in VALID_BODY_DST_NEGATE:
            return (
                False,
                f"Invalid dst-negate '{value}'. Must be one of: {', '.join(VALID_BODY_DST_NEGATE)}",
            )

    # Validate action if present
    if "action" in payload:
        value = payload.get("action")
        if value and value not in VALID_BODY_ACTION:
            return (
                False,
                f"Invalid action '{value}'. Must be one of: {', '.join(VALID_BODY_ACTION)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "protocol must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"protocol must be numeric, got: {value}")

    # Validate start-port if present
    if "start-port" in payload:
        value = payload.get("start-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "start-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"start-port must be numeric, got: {value}")

    # Validate end-port if present
    if "end-port" in payload:
        value = payload.get("end-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "end-port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"end-port must be numeric, got: {value}")

    # Validate start-source-port if present
    if "start-source-port" in payload:
        value = payload.get("start-source-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "start-source-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"start-source-port must be numeric, got: {value}",
                )

    # Validate end-source-port if present
    if "end-source-port" in payload:
        value = payload.get("end-source-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (
                        False,
                        "end-source-port must be between 1 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"end-source-port must be numeric, got: {value}",
                )

    # Validate output-device if present
    if "output-device" in payload:
        value = payload.get("output-device")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "output-device cannot exceed 35 characters")

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_policy6_delete() -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:

    Returns:
        Tuple of (is_valid, error_message)
    """
    return (True, None)
