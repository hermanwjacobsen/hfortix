"""
Validation helpers for system external_resource endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["enable", "disable"]
VALID_BODY_TYPE = [
    "category",
    "domain",
    "malware",
    "address",
    "mac-address",
    "data",
    "generic-address",
]
VALID_BODY_UPDATE_METHOD = ["feed", "push"]
VALID_BODY_CLIENT_CERT_AUTH = ["enable", "disable"]
VALID_BODY_SERVER_IDENTITY_CHECK = ["none", "basic", "full"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_external_resource_get(
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


def validate_external_resource_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating external_resource.

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

    # Validate namespace if present
    if "namespace" in payload:
        value = payload.get("namespace")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "namespace cannot exceed 15 characters")

    # Validate object-array-path if present
    if "object-array-path" in payload:
        value = payload.get("object-array-path")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "object-array-path cannot exceed 511 characters")

    # Validate address-name-field if present
    if "address-name-field" in payload:
        value = payload.get("address-name-field")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "address-name-field cannot exceed 511 characters")

    # Validate address-data-field if present
    if "address-data-field" in payload:
        value = payload.get("address-data-field")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "address-data-field cannot exceed 511 characters")

    # Validate address-comment-field if present
    if "address-comment-field" in payload:
        value = payload.get("address-comment-field")
        if value and isinstance(value, str) and len(value) > 511:
            return (
                False,
                "address-comment-field cannot exceed 511 characters",
            )

    # Validate update-method if present
    if "update-method" in payload:
        value = payload.get("update-method")
        if value and value not in VALID_BODY_UPDATE_METHOD:
            return (
                False,
                f"Invalid update-method '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_METHOD)}",
            )

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 192 or int_val > 221:
                    return (False, "category must be between 192 and 221")
            except (ValueError, TypeError):
                return (False, f"category must be numeric, got: {value}")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate client-cert-auth if present
    if "client-cert-auth" in payload:
        value = payload.get("client-cert-auth")
        if value and value not in VALID_BODY_CLIENT_CERT_AUTH:
            return (
                False,
                f"Invalid client-cert-auth '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT_AUTH)}",
            )

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "client-cert cannot exceed 79 characters")

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate resource if present
    if "resource" in payload:
        value = payload.get("resource")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "resource cannot exceed 511 characters")

    # Validate user-agent if present
    if "user-agent" in payload:
        value = payload.get("user-agent")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "user-agent cannot exceed 255 characters")

    # Validate server-identity-check if present
    if "server-identity-check" in payload:
        value = payload.get("server-identity-check")
        if value and value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid server-identity-check '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
            )

    # Validate refresh-rate if present
    if "refresh-rate" in payload:
        value = payload.get("refresh-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 43200:
                    return (False, "refresh-rate must be between 1 and 43200")
            except (ValueError, TypeError):
                return (False, f"refresh-rate must be numeric, got: {value}")

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_external_resource_put(
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

    # Validate namespace if present
    if "namespace" in payload:
        value = payload.get("namespace")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "namespace cannot exceed 15 characters")

    # Validate object-array-path if present
    if "object-array-path" in payload:
        value = payload.get("object-array-path")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "object-array-path cannot exceed 511 characters")

    # Validate address-name-field if present
    if "address-name-field" in payload:
        value = payload.get("address-name-field")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "address-name-field cannot exceed 511 characters")

    # Validate address-data-field if present
    if "address-data-field" in payload:
        value = payload.get("address-data-field")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "address-data-field cannot exceed 511 characters")

    # Validate address-comment-field if present
    if "address-comment-field" in payload:
        value = payload.get("address-comment-field")
        if value and isinstance(value, str) and len(value) > 511:
            return (
                False,
                "address-comment-field cannot exceed 511 characters",
            )

    # Validate update-method if present
    if "update-method" in payload:
        value = payload.get("update-method")
        if value and value not in VALID_BODY_UPDATE_METHOD:
            return (
                False,
                f"Invalid update-method '{value}'. Must be one of: {', '.join(VALID_BODY_UPDATE_METHOD)}",
            )

    # Validate category if present
    if "category" in payload:
        value = payload.get("category")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 192 or int_val > 221:
                    return (False, "category must be between 192 and 221")
            except (ValueError, TypeError):
                return (False, f"category must be numeric, got: {value}")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate client-cert-auth if present
    if "client-cert-auth" in payload:
        value = payload.get("client-cert-auth")
        if value and value not in VALID_BODY_CLIENT_CERT_AUTH:
            return (
                False,
                f"Invalid client-cert-auth '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT_AUTH)}",
            )

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "client-cert cannot exceed 79 characters")

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comments cannot exceed 255 characters")

    # Validate resource if present
    if "resource" in payload:
        value = payload.get("resource")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "resource cannot exceed 511 characters")

    # Validate user-agent if present
    if "user-agent" in payload:
        value = payload.get("user-agent")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "user-agent cannot exceed 255 characters")

    # Validate server-identity-check if present
    if "server-identity-check" in payload:
        value = payload.get("server-identity-check")
        if value and value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid server-identity-check '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
            )

    # Validate refresh-rate if present
    if "refresh-rate" in payload:
        value = payload.get("refresh-rate")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 43200:
                    return (False, "refresh-rate must be between 1 and 43200")
            except (ValueError, TypeError):
                return (False, f"refresh-rate must be numeric, got: {value}")

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate interface-select-method if present
    if "interface-select-method" in payload:
        value = payload.get("interface-select-method")
        if value and value not in VALID_BODY_INTERFACE_SELECT_METHOD:
            return (
                False,
                f"Invalid interface-select-method '{value}'. Must be one of: {', '.join(VALID_BODY_INTERFACE_SELECT_METHOD)}",
            )

    # Validate interface if present
    if "interface" in payload:
        value = payload.get("interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "interface cannot exceed 15 characters")

    # Validate vrf-select if present
    if "vrf-select" in payload:
        value = payload.get("vrf-select")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 511:
                    return (False, "vrf-select must be between 0 and 511")
            except (ValueError, TypeError):
                return (False, f"vrf-select must be numeric, got: {value}")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_external_resource_delete(
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
