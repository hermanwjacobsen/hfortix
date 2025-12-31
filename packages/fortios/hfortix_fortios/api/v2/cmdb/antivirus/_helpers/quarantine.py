"""
Validation helpers for antivirus quarantine endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_DROP_INFECTED = [
    "imap",
    "smtp",
    "pop3",
    "http",
    "ftp",
    "nntp",
    "imaps",
    "smtps",
    "pop3s",
    "https",
    "ftps",
    "mapi",
    "cifs",
    "ssh",
]
VALID_BODY_STORE_INFECTED = [
    "imap",
    "smtp",
    "pop3",
    "http",
    "ftp",
    "nntp",
    "imaps",
    "smtps",
    "pop3s",
    "https",
    "ftps",
    "mapi",
    "cifs",
    "ssh",
]
VALID_BODY_DROP_MACHINE_LEARNING = [
    "imap",
    "smtp",
    "pop3",
    "http",
    "ftp",
    "nntp",
    "imaps",
    "smtps",
    "pop3s",
    "https",
    "ftps",
    "mapi",
    "cifs",
    "ssh",
]
VALID_BODY_STORE_MACHINE_LEARNING = [
    "imap",
    "smtp",
    "pop3",
    "http",
    "ftp",
    "nntp",
    "imaps",
    "smtps",
    "pop3s",
    "https",
    "ftps",
    "mapi",
    "cifs",
    "ssh",
]
VALID_BODY_LOWSPACE = ["drop-new", "ovrw-old"]
VALID_BODY_DESTINATION = ["NULL", "disk", "FortiAnalyzer"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_quarantine_get(
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


def validate_quarantine_put(
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

    # Validate agelimit if present
    if "agelimit" in payload:
        value = payload.get("agelimit")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 479:
                    return (False, "agelimit must be between 0 and 479")
            except (ValueError, TypeError):
                return (False, f"agelimit must be numeric, got: {value}")

    # Validate maxfilesize if present
    if "maxfilesize" in payload:
        value = payload.get("maxfilesize")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 500:
                    return (False, "maxfilesize must be between 0 and 500")
            except (ValueError, TypeError):
                return (False, f"maxfilesize must be numeric, got: {value}")

    # Validate quarantine-quota if present
    if "quarantine-quota" in payload:
        value = payload.get("quarantine-quota")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "quarantine-quota must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"quarantine-quota must be numeric, got: {value}",
                )

    # Validate drop-infected if present
    if "drop-infected" in payload:
        value = payload.get("drop-infected")
        if value and value not in VALID_BODY_DROP_INFECTED:
            return (
                False,
                f"Invalid drop-infected '{value}'. Must be one of: {', '.join(VALID_BODY_DROP_INFECTED)}",
            )

    # Validate store-infected if present
    if "store-infected" in payload:
        value = payload.get("store-infected")
        if value and value not in VALID_BODY_STORE_INFECTED:
            return (
                False,
                f"Invalid store-infected '{value}'. Must be one of: {', '.join(VALID_BODY_STORE_INFECTED)}",
            )

    # Validate drop-machine-learning if present
    if "drop-machine-learning" in payload:
        value = payload.get("drop-machine-learning")
        if value and value not in VALID_BODY_DROP_MACHINE_LEARNING:
            return (
                False,
                f"Invalid drop-machine-learning '{value}'. Must be one of: {', '.join(VALID_BODY_DROP_MACHINE_LEARNING)}",
            )

    # Validate store-machine-learning if present
    if "store-machine-learning" in payload:
        value = payload.get("store-machine-learning")
        if value and value not in VALID_BODY_STORE_MACHINE_LEARNING:
            return (
                False,
                f"Invalid store-machine-learning '{value}'. Must be one of: {', '.join(VALID_BODY_STORE_MACHINE_LEARNING)}",
            )

    # Validate lowspace if present
    if "lowspace" in payload:
        value = payload.get("lowspace")
        if value and value not in VALID_BODY_LOWSPACE:
            return (
                False,
                f"Invalid lowspace '{value}'. Must be one of: {', '.join(VALID_BODY_LOWSPACE)}",
            )

    # Validate destination if present
    if "destination" in payload:
        value = payload.get("destination")
        if value and value not in VALID_BODY_DESTINATION:
            return (
                False,
                f"Invalid destination '{value}'. Must be one of: {', '.join(VALID_BODY_DESTINATION)}",
            )

    return (True, None)
