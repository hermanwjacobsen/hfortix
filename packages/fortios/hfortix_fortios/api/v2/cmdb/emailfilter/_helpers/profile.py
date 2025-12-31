"""
Validation helpers for emailfilter profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = ["flow", "proxy"]
VALID_BODY_SPAM_LOG = ["disable", "enable"]
VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE = ["disable", "enable"]
VALID_BODY_SPAM_FILTERING = ["enable", "disable"]
VALID_BODY_EXTERNAL = ["enable", "disable"]
VALID_BODY_OPTIONS = [
    "bannedword",
    "spambal",
    "spamfsip",
    "spamfssubmit",
    "spamfschksum",
    "spamfsurl",
    "spamhelodns",
    "spamraddrdns",
    "spamrbl",
    "spamhdrcheck",
    "spamfsphish",
]
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

    # Validate feature-set if present
    if "feature-set" in payload:
        value = payload.get("feature-set")
        if value and value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid feature-set '{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate spam-log if present
    if "spam-log" in payload:
        value = payload.get("spam-log")
        if value and value not in VALID_BODY_SPAM_LOG:
            return (
                False,
                f"Invalid spam-log '{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_LOG)}",
            )

    # Validate spam-log-fortiguard-response if present
    if "spam-log-fortiguard-response" in payload:
        value = payload.get("spam-log-fortiguard-response")
        if value and value not in VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE:
            return (
                False,
                f"Invalid spam-log-fortiguard-response '{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE)}",
            )

    # Validate spam-filtering if present
    if "spam-filtering" in payload:
        value = payload.get("spam-filtering")
        if value and value not in VALID_BODY_SPAM_FILTERING:
            return (
                False,
                f"Invalid spam-filtering '{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_FILTERING)}",
            )

    # Validate external if present
    if "external" in payload:
        value = payload.get("external")
        if value and value not in VALID_BODY_EXTERNAL:
            return (
                False,
                f"Invalid external '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL)}",
            )

    # Validate options if present
    if "options" in payload:
        value = payload.get("options")
        if value and value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid options '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )

    # Validate spam-bword-threshold if present
    if "spam-bword-threshold" in payload:
        value = payload.get("spam-bword-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "spam-bword-threshold must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spam-bword-threshold must be numeric, got: {value}",
                )

    # Validate spam-bword-table if present
    if "spam-bword-table" in payload:
        value = payload.get("spam-bword-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-bword-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spam-bword-table must be numeric, got: {value}",
                )

    # Validate spam-bal-table if present
    if "spam-bal-table" in payload:
        value = payload.get("spam-bal-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-bal-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"spam-bal-table must be numeric, got: {value}")

    # Validate spam-mheader-table if present
    if "spam-mheader-table" in payload:
        value = payload.get("spam-mheader-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-mheader-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spam-mheader-table must be numeric, got: {value}",
                )

    # Validate spam-rbl-table if present
    if "spam-rbl-table" in payload:
        value = payload.get("spam-rbl-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-rbl-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"spam-rbl-table must be numeric, got: {value}")

    # Validate spam-iptrust-table if present
    if "spam-iptrust-table" in payload:
        value = payload.get("spam-iptrust-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-iptrust-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spam-iptrust-table must be numeric, got: {value}",
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

    # Validate feature-set if present
    if "feature-set" in payload:
        value = payload.get("feature-set")
        if value and value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid feature-set '{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )

    # Validate replacemsg-group if present
    if "replacemsg-group" in payload:
        value = payload.get("replacemsg-group")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "replacemsg-group cannot exceed 35 characters")

    # Validate spam-log if present
    if "spam-log" in payload:
        value = payload.get("spam-log")
        if value and value not in VALID_BODY_SPAM_LOG:
            return (
                False,
                f"Invalid spam-log '{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_LOG)}",
            )

    # Validate spam-log-fortiguard-response if present
    if "spam-log-fortiguard-response" in payload:
        value = payload.get("spam-log-fortiguard-response")
        if value and value not in VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE:
            return (
                False,
                f"Invalid spam-log-fortiguard-response '{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_LOG_FORTIGUARD_RESPONSE)}",
            )

    # Validate spam-filtering if present
    if "spam-filtering" in payload:
        value = payload.get("spam-filtering")
        if value and value not in VALID_BODY_SPAM_FILTERING:
            return (
                False,
                f"Invalid spam-filtering '{value}'. Must be one of: {', '.join(VALID_BODY_SPAM_FILTERING)}",
            )

    # Validate external if present
    if "external" in payload:
        value = payload.get("external")
        if value and value not in VALID_BODY_EXTERNAL:
            return (
                False,
                f"Invalid external '{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL)}",
            )

    # Validate options if present
    if "options" in payload:
        value = payload.get("options")
        if value and value not in VALID_BODY_OPTIONS:
            return (
                False,
                f"Invalid options '{value}'. Must be one of: {', '.join(VALID_BODY_OPTIONS)}",
            )

    # Validate spam-bword-threshold if present
    if "spam-bword-threshold" in payload:
        value = payload.get("spam-bword-threshold")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "spam-bword-threshold must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spam-bword-threshold must be numeric, got: {value}",
                )

    # Validate spam-bword-table if present
    if "spam-bword-table" in payload:
        value = payload.get("spam-bword-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-bword-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spam-bword-table must be numeric, got: {value}",
                )

    # Validate spam-bal-table if present
    if "spam-bal-table" in payload:
        value = payload.get("spam-bal-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-bal-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"spam-bal-table must be numeric, got: {value}")

    # Validate spam-mheader-table if present
    if "spam-mheader-table" in payload:
        value = payload.get("spam-mheader-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-mheader-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spam-mheader-table must be numeric, got: {value}",
                )

    # Validate spam-rbl-table if present
    if "spam-rbl-table" in payload:
        value = payload.get("spam-rbl-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-rbl-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"spam-rbl-table must be numeric, got: {value}")

    # Validate spam-iptrust-table if present
    if "spam-iptrust-table" in payload:
        value = payload.get("spam-iptrust-table")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "spam-iptrust-table must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"spam-iptrust-table must be numeric, got: {value}",
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
