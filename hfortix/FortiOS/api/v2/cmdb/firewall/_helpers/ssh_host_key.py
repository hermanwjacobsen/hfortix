"""
Validation helpers for firewall ssh_host_key endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["trusted", "revoked"]
VALID_BODY_TYPE = [
    "RSA",
    "DSA",
    "ECDSA",
    "ED25519",
    "RSA-CA",
    "DSA-CA",
    "ECDSA-CA",
    "ED25519-CA",
]
VALID_BODY_NID = ["256", "384", "521"]
VALID_BODY_USAGE = ["transparent-proxy", "access-proxy"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ssh_host_key_get(
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


def validate_ssh_host_key_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ssh_host_key.

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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate nid if present
    if "nid" in payload:
        value = payload.get("nid")
        if value and value not in VALID_BODY_NID:
            return (
                False,
                f"Invalid nid '{value}'. Must be one of: {', '.join(VALID_BODY_NID)}",
            )

    # Validate usage if present
    if "usage" in payload:
        value = payload.get("usage")
        if value and value not in VALID_BODY_USAGE:
            return (
                False,
                f"Invalid usage '{value}'. Must be one of: {', '.join(VALID_BODY_USAGE)}",
            )

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "port must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "hostname cannot exceed 255 characters")

    # Validate public-key if present
    if "public-key" in payload:
        value = payload.get("public-key")
        if value and isinstance(value, str) and len(value) > 32768:
            return (False, "public-key cannot exceed 32768 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ssh_host_key_put(
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

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate nid if present
    if "nid" in payload:
        value = payload.get("nid")
        if value and value not in VALID_BODY_NID:
            return (
                False,
                f"Invalid nid '{value}'. Must be one of: {', '.join(VALID_BODY_NID)}",
            )

    # Validate usage if present
    if "usage" in payload:
        value = payload.get("usage")
        if value and value not in VALID_BODY_USAGE:
            return (
                False,
                f"Invalid usage '{value}'. Must be one of: {', '.join(VALID_BODY_USAGE)}",
            )

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (False, "port must be between 0 and 4294967295")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate hostname if present
    if "hostname" in payload:
        value = payload.get("hostname")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "hostname cannot exceed 255 characters")

    # Validate public-key if present
    if "public-key" in payload:
        value = payload.get("public-key")
        if value and isinstance(value, str) and len(value) > 32768:
            return (False, "public-key cannot exceed 32768 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ssh_host_key_delete(
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
