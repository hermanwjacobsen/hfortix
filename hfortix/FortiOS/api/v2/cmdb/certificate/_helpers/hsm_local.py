"""
Validation helpers for certificate hsm_local endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_VENDOR = ["unknown", "gch"]
VALID_BODY_API_VERSION = ["unknown", "gch-default"]
VALID_BODY_RANGE = ["global", "vdom"]
VALID_BODY_SOURCE = ["factory", "user", "bundle"]
VALID_BODY_GCH_CRYPTOKEY_ALGORITHM = [
    "rsa-sign-pkcs1-2048-sha256",
    "rsa-sign-pkcs1-3072-sha256",
    "rsa-sign-pkcs1-4096-sha256",
    "rsa-sign-pkcs1-4096-sha512",
    "rsa-sign-pss-2048-sha256",
    "rsa-sign-pss-3072-sha256",
    "rsa-sign-pss-4096-sha256",
    "rsa-sign-pss-4096-sha512",
    "ec-sign-p256-sha256",
    "ec-sign-p384-sha384",
    "ec-sign-secp256k1-sha256",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_hsm_local_get(
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


def validate_hsm_local_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating hsm_local.

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

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "comments cannot exceed 511 characters")

    # Validate vendor if present
    if "vendor" in payload:
        value = payload.get("vendor")
        if value and value not in VALID_BODY_VENDOR:
            return (
                False,
                f"Invalid vendor '{value}'. Must be one of: {', '.join(VALID_BODY_VENDOR)}",
            )

    # Validate api-version if present
    if "api-version" in payload:
        value = payload.get("api-version")
        if value and value not in VALID_BODY_API_VERSION:
            return (
                False,
                f"Invalid api-version '{value}'. Must be one of: {', '.join(VALID_BODY_API_VERSION)}",
            )

    # Validate range if present
    if "range" in payload:
        value = payload.get("range")
        if value and value not in VALID_BODY_RANGE:
            return (
                False,
                f"Invalid range '{value}'. Must be one of: {', '.join(VALID_BODY_RANGE)}",
            )

    # Validate source if present
    if "source" in payload:
        value = payload.get("source")
        if value and value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid source '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )

    # Validate gch-url if present
    if "gch-url" in payload:
        value = payload.get("gch-url")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "gch-url cannot exceed 1024 characters")

    # Validate gch-project if present
    if "gch-project" in payload:
        value = payload.get("gch-project")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "gch-project cannot exceed 31 characters")

    # Validate gch-location if present
    if "gch-location" in payload:
        value = payload.get("gch-location")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "gch-location cannot exceed 63 characters")

    # Validate gch-keyring if present
    if "gch-keyring" in payload:
        value = payload.get("gch-keyring")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "gch-keyring cannot exceed 63 characters")

    # Validate gch-cryptokey if present
    if "gch-cryptokey" in payload:
        value = payload.get("gch-cryptokey")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "gch-cryptokey cannot exceed 63 characters")

    # Validate gch-cryptokey-version if present
    if "gch-cryptokey-version" in payload:
        value = payload.get("gch-cryptokey-version")
        if value and isinstance(value, str) and len(value) > 31:
            return (
                False,
                "gch-cryptokey-version cannot exceed 31 characters",
            )

    # Validate gch-cloud-service-name if present
    if "gch-cloud-service-name" in payload:
        value = payload.get("gch-cloud-service-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "gch-cloud-service-name cannot exceed 35 characters",
            )

    # Validate gch-cryptokey-algorithm if present
    if "gch-cryptokey-algorithm" in payload:
        value = payload.get("gch-cryptokey-algorithm")
        if value and value not in VALID_BODY_GCH_CRYPTOKEY_ALGORITHM:
            return (
                False,
                f"Invalid gch-cryptokey-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_GCH_CRYPTOKEY_ALGORITHM)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_hsm_local_put(
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

    # Validate comments if present
    if "comments" in payload:
        value = payload.get("comments")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "comments cannot exceed 511 characters")

    # Validate vendor if present
    if "vendor" in payload:
        value = payload.get("vendor")
        if value and value not in VALID_BODY_VENDOR:
            return (
                False,
                f"Invalid vendor '{value}'. Must be one of: {', '.join(VALID_BODY_VENDOR)}",
            )

    # Validate api-version if present
    if "api-version" in payload:
        value = payload.get("api-version")
        if value and value not in VALID_BODY_API_VERSION:
            return (
                False,
                f"Invalid api-version '{value}'. Must be one of: {', '.join(VALID_BODY_API_VERSION)}",
            )

    # Validate range if present
    if "range" in payload:
        value = payload.get("range")
        if value and value not in VALID_BODY_RANGE:
            return (
                False,
                f"Invalid range '{value}'. Must be one of: {', '.join(VALID_BODY_RANGE)}",
            )

    # Validate source if present
    if "source" in payload:
        value = payload.get("source")
        if value and value not in VALID_BODY_SOURCE:
            return (
                False,
                f"Invalid source '{value}'. Must be one of: {', '.join(VALID_BODY_SOURCE)}",
            )

    # Validate gch-url if present
    if "gch-url" in payload:
        value = payload.get("gch-url")
        if value and isinstance(value, str) and len(value) > 1024:
            return (False, "gch-url cannot exceed 1024 characters")

    # Validate gch-project if present
    if "gch-project" in payload:
        value = payload.get("gch-project")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "gch-project cannot exceed 31 characters")

    # Validate gch-location if present
    if "gch-location" in payload:
        value = payload.get("gch-location")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "gch-location cannot exceed 63 characters")

    # Validate gch-keyring if present
    if "gch-keyring" in payload:
        value = payload.get("gch-keyring")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "gch-keyring cannot exceed 63 characters")

    # Validate gch-cryptokey if present
    if "gch-cryptokey" in payload:
        value = payload.get("gch-cryptokey")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "gch-cryptokey cannot exceed 63 characters")

    # Validate gch-cryptokey-version if present
    if "gch-cryptokey-version" in payload:
        value = payload.get("gch-cryptokey-version")
        if value and isinstance(value, str) and len(value) > 31:
            return (
                False,
                "gch-cryptokey-version cannot exceed 31 characters",
            )

    # Validate gch-cloud-service-name if present
    if "gch-cloud-service-name" in payload:
        value = payload.get("gch-cloud-service-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "gch-cloud-service-name cannot exceed 35 characters",
            )

    # Validate gch-cryptokey-algorithm if present
    if "gch-cryptokey-algorithm" in payload:
        value = payload.get("gch-cryptokey-algorithm")
        if value and value not in VALID_BODY_GCH_CRYPTOKEY_ALGORITHM:
            return (
                False,
                f"Invalid gch-cryptokey-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_GCH_CRYPTOKEY_ALGORITHM)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_hsm_local_delete(
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
