"""
Validation helpers for diameter-filter profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_MONITOR_ALL_MESSAGES = ["disable", "enable"]
VALID_BODY_LOG_PACKET = ["disable", "enable"]
VALID_BODY_TRACK_REQUESTS_ANSWERS = ["disable", "enable"]
VALID_BODY_MISSING_REQUEST_ACTION = ["allow", "block", "reset", "monitor"]
VALID_BODY_PROTOCOL_VERSION_INVALID = ["allow", "block", "reset", "monitor"]
VALID_BODY_MESSAGE_LENGTH_INVALID = ["allow", "block", "reset", "monitor"]
VALID_BODY_REQUEST_ERROR_FLAG_SET = ["allow", "block", "reset", "monitor"]
VALID_BODY_CMD_FLAGS_RESERVE_SET = ["allow", "block", "reset", "monitor"]
VALID_BODY_COMMAND_CODE_INVALID = ["allow", "block", "reset", "monitor"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_profile_get(
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


def validate_profile_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating profile.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate monitor-all-messages if present
    if "monitor-all-messages" in payload:
        value = payload.get("monitor-all-messages")
        if value and value not in VALID_BODY_MONITOR_ALL_MESSAGES:
            return (
                False,
                f"Invalid monitor-all-messages '{value}'. Must be one of: {', '.join(VALID_BODY_MONITOR_ALL_MESSAGES)}",
            )

    # Validate log-packet if present
    if "log-packet" in payload:
        value = payload.get("log-packet")
        if value and value not in VALID_BODY_LOG_PACKET:
            return (
                False,
                f"Invalid log-packet '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_PACKET)}",
            )

    # Validate track-requests-answers if present
    if "track-requests-answers" in payload:
        value = payload.get("track-requests-answers")
        if value and value not in VALID_BODY_TRACK_REQUESTS_ANSWERS:
            return (
                False,
                f"Invalid track-requests-answers '{value}'. Must be one of: {', '.join(VALID_BODY_TRACK_REQUESTS_ANSWERS)}",
            )

    # Validate missing-request-action if present
    if "missing-request-action" in payload:
        value = payload.get("missing-request-action")
        if value and value not in VALID_BODY_MISSING_REQUEST_ACTION:
            return (
                False,
                f"Invalid missing-request-action '{value}'. Must be one of: {', '.join(VALID_BODY_MISSING_REQUEST_ACTION)}",
            )

    # Validate protocol-version-invalid if present
    if "protocol-version-invalid" in payload:
        value = payload.get("protocol-version-invalid")
        if value and value not in VALID_BODY_PROTOCOL_VERSION_INVALID:
            return (
                False,
                f"Invalid protocol-version-invalid '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL_VERSION_INVALID)}",
            )

    # Validate message-length-invalid if present
    if "message-length-invalid" in payload:
        value = payload.get("message-length-invalid")
        if value and value not in VALID_BODY_MESSAGE_LENGTH_INVALID:
            return (
                False,
                f"Invalid message-length-invalid '{value}'. Must be one of: {', '.join(VALID_BODY_MESSAGE_LENGTH_INVALID)}",
            )

    # Validate request-error-flag-set if present
    if "request-error-flag-set" in payload:
        value = payload.get("request-error-flag-set")
        if value and value not in VALID_BODY_REQUEST_ERROR_FLAG_SET:
            return (
                False,
                f"Invalid request-error-flag-set '{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST_ERROR_FLAG_SET)}",
            )

    # Validate cmd-flags-reserve-set if present
    if "cmd-flags-reserve-set" in payload:
        value = payload.get("cmd-flags-reserve-set")
        if value and value not in VALID_BODY_CMD_FLAGS_RESERVE_SET:
            return (
                False,
                f"Invalid cmd-flags-reserve-set '{value}'. Must be one of: {', '.join(VALID_BODY_CMD_FLAGS_RESERVE_SET)}",
            )

    # Validate command-code-invalid if present
    if "command-code-invalid" in payload:
        value = payload.get("command-code-invalid")
        if value and value not in VALID_BODY_COMMAND_CODE_INVALID:
            return (
                False,
                f"Invalid command-code-invalid '{value}'. Must be one of: {', '.join(VALID_BODY_COMMAND_CODE_INVALID)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_profile_put(
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
        if value and isinstance(value, str) and len(value) > 47:
            return (False, "name cannot exceed 47 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate monitor-all-messages if present
    if "monitor-all-messages" in payload:
        value = payload.get("monitor-all-messages")
        if value and value not in VALID_BODY_MONITOR_ALL_MESSAGES:
            return (
                False,
                f"Invalid monitor-all-messages '{value}'. Must be one of: {', '.join(VALID_BODY_MONITOR_ALL_MESSAGES)}",
            )

    # Validate log-packet if present
    if "log-packet" in payload:
        value = payload.get("log-packet")
        if value and value not in VALID_BODY_LOG_PACKET:
            return (
                False,
                f"Invalid log-packet '{value}'. Must be one of: {', '.join(VALID_BODY_LOG_PACKET)}",
            )

    # Validate track-requests-answers if present
    if "track-requests-answers" in payload:
        value = payload.get("track-requests-answers")
        if value and value not in VALID_BODY_TRACK_REQUESTS_ANSWERS:
            return (
                False,
                f"Invalid track-requests-answers '{value}'. Must be one of: {', '.join(VALID_BODY_TRACK_REQUESTS_ANSWERS)}",
            )

    # Validate missing-request-action if present
    if "missing-request-action" in payload:
        value = payload.get("missing-request-action")
        if value and value not in VALID_BODY_MISSING_REQUEST_ACTION:
            return (
                False,
                f"Invalid missing-request-action '{value}'. Must be one of: {', '.join(VALID_BODY_MISSING_REQUEST_ACTION)}",
            )

    # Validate protocol-version-invalid if present
    if "protocol-version-invalid" in payload:
        value = payload.get("protocol-version-invalid")
        if value and value not in VALID_BODY_PROTOCOL_VERSION_INVALID:
            return (
                False,
                f"Invalid protocol-version-invalid '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL_VERSION_INVALID)}",
            )

    # Validate message-length-invalid if present
    if "message-length-invalid" in payload:
        value = payload.get("message-length-invalid")
        if value and value not in VALID_BODY_MESSAGE_LENGTH_INVALID:
            return (
                False,
                f"Invalid message-length-invalid '{value}'. Must be one of: {', '.join(VALID_BODY_MESSAGE_LENGTH_INVALID)}",
            )

    # Validate request-error-flag-set if present
    if "request-error-flag-set" in payload:
        value = payload.get("request-error-flag-set")
        if value and value not in VALID_BODY_REQUEST_ERROR_FLAG_SET:
            return (
                False,
                f"Invalid request-error-flag-set '{value}'. Must be one of: {', '.join(VALID_BODY_REQUEST_ERROR_FLAG_SET)}",
            )

    # Validate cmd-flags-reserve-set if present
    if "cmd-flags-reserve-set" in payload:
        value = payload.get("cmd-flags-reserve-set")
        if value and value not in VALID_BODY_CMD_FLAGS_RESERVE_SET:
            return (
                False,
                f"Invalid cmd-flags-reserve-set '{value}'. Must be one of: {', '.join(VALID_BODY_CMD_FLAGS_RESERVE_SET)}",
            )

    # Validate command-code-invalid if present
    if "command-code-invalid" in payload:
        value = payload.get("command-code-invalid")
        if value and value not in VALID_BODY_COMMAND_CODE_INVALID:
            return (
                False,
                f"Invalid command-code-invalid '{value}'. Must be one of: {', '.join(VALID_BODY_COMMAND_CODE_INVALID)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_profile_delete(
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
