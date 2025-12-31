"""
Validation helpers for firewall internet_service endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_DIRECTION = ["src", "dst", "both"]
VALID_BODY_DATABASE = ["isdb", "irdb"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_internet_service_get(
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


def validate_internet_service_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating internet_service.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate icon-id if present
    if "icon-id" in payload:
        value = payload.get("icon-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "icon-id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"icon-id must be numeric, got: {value}")

    # Validate direction if present
    if "direction" in payload:
        value = payload.get("direction")
        if value and value not in VALID_BODY_DIRECTION:
            return (
                False,
                f"Invalid direction '{value}'. Must be one of: {', '.join(VALID_BODY_DIRECTION)}",
            )

    # Validate database if present
    if "database" in payload:
        value = payload.get("database")
        if value and value not in VALID_BODY_DATABASE:
            return (
                False,
                f"Invalid database '{value}'. Must be one of: {', '.join(VALID_BODY_DATABASE)}",
            )

    # Validate ip-range-number if present
    if "ip-range-number" in payload:
        value = payload.get("ip-range-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ip-range-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ip-range-number must be numeric, got: {value}",
                )

    # Validate extra-ip-range-number if present
    if "extra-ip-range-number" in payload:
        value = payload.get("extra-ip-range-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "extra-ip-range-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"extra-ip-range-number must be numeric, got: {value}",
                )

    # Validate ip-number if present
    if "ip-number" in payload:
        value = payload.get("ip-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ip-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"ip-number must be numeric, got: {value}")

    # Validate ip6-range-number if present
    if "ip6-range-number" in payload:
        value = payload.get("ip6-range-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ip6-range-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ip6-range-number must be numeric, got: {value}",
                )

    # Validate extra-ip6-range-number if present
    if "extra-ip6-range-number" in payload:
        value = payload.get("extra-ip6-range-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "extra-ip6-range-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"extra-ip6-range-number must be numeric, got: {value}",
                )

    # Validate singularity if present
    if "singularity" in payload:
        value = payload.get("singularity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "singularity must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"singularity must be numeric, got: {value}")

    # Validate obsolete if present
    if "obsolete" in payload:
        value = payload.get("obsolete")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "obsolete must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"obsolete must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_internet_service_put(
    id: str | None = None, payload: dict[str, Any] | None = None
) -> tuple[bool, str | None]:
    """
    Validate PUT request payload for updating {endpoint_name}.

    Args:
        id: Object identifier (required)
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # id is required for updates
    if not id:
        return (False, "id is required for PUT operation")

    # If no payload provided, nothing to validate
    if not payload:
        return (True, None)

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "name cannot exceed 63 characters")

    # Validate icon-id if present
    if "icon-id" in payload:
        value = payload.get("icon-id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "icon-id must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"icon-id must be numeric, got: {value}")

    # Validate direction if present
    if "direction" in payload:
        value = payload.get("direction")
        if value and value not in VALID_BODY_DIRECTION:
            return (
                False,
                f"Invalid direction '{value}'. Must be one of: {', '.join(VALID_BODY_DIRECTION)}",
            )

    # Validate database if present
    if "database" in payload:
        value = payload.get("database")
        if value and value not in VALID_BODY_DATABASE:
            return (
                False,
                f"Invalid database '{value}'. Must be one of: {', '.join(VALID_BODY_DATABASE)}",
            )

    # Validate ip-range-number if present
    if "ip-range-number" in payload:
        value = payload.get("ip-range-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ip-range-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ip-range-number must be numeric, got: {value}",
                )

    # Validate extra-ip-range-number if present
    if "extra-ip-range-number" in payload:
        value = payload.get("extra-ip-range-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "extra-ip-range-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"extra-ip-range-number must be numeric, got: {value}",
                )

    # Validate ip-number if present
    if "ip-number" in payload:
        value = payload.get("ip-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ip-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"ip-number must be numeric, got: {value}")

    # Validate ip6-range-number if present
    if "ip6-range-number" in payload:
        value = payload.get("ip6-range-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "ip6-range-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ip6-range-number must be numeric, got: {value}",
                )

    # Validate extra-ip6-range-number if present
    if "extra-ip6-range-number" in payload:
        value = payload.get("extra-ip6-range-number")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "extra-ip6-range-number must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"extra-ip6-range-number must be numeric, got: {value}",
                )

    # Validate singularity if present
    if "singularity" in payload:
        value = payload.get("singularity")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "singularity must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"singularity must be numeric, got: {value}")

    # Validate obsolete if present
    if "obsolete" in payload:
        value = payload.get("obsolete")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 255:
                    return (False, "obsolete must be between 0 and 255")
            except (ValueError, TypeError):
                return (False, f"obsolete must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_internet_service_delete(
    id: str | None = None,
) -> tuple[bool, str | None]:
    """
    Validate DELETE request parameters.

    Args:
        id: Object identifier (required)

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not id:
        return (False, "id is required for DELETE operation")

    return (True, None)
