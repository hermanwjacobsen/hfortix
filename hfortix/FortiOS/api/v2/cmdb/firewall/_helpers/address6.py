"""
Validation helpers for firewall address6 endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "ipprefix",
    "iprange",
    "fqdn",
    "geography",
    "dynamic",
    "template",
    "mac",
    "route-tag",
    "wildcard",
]
VALID_BODY_HOST_TYPE = ["any", "specific"]
VALID_BODY_SDN_ADDR_TYPE = ["private", "public", "all"]
VALID_BODY_PASSIVE_FQDN_LEARNING = ["disable", "enable"]
VALID_BODY_FABRIC_OBJECT = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_address6_get(
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


def validate_address6_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating address6.

    Args:
        payload: The payload to validate

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Validate name if present
    if "name" in payload:
        value = payload.get("name")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate route-tag if present
    if "route-tag" in payload:
        value = payload.get("route-tag")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4294967295:
                    return (
                        False,
                        "route-tag must be between 1 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"route-tag must be numeric, got: {value}")

    # Validate sdn if present
    if "sdn" in payload:
        value = payload.get("sdn")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sdn cannot exceed 35 characters")

    # Validate fqdn if present
    if "fqdn" in payload:
        value = payload.get("fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fqdn cannot exceed 255 characters")

    # Validate country if present
    if "country" in payload:
        value = payload.get("country")
        if value and isinstance(value, str) and len(value) > 2:
            return (False, "country cannot exceed 2 characters")

    # Validate cache-ttl if present
    if "cache-ttl" in payload:
        value = payload.get("cache-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (False, "cache-ttl must be between 0 and 86400")
            except (ValueError, TypeError):
                return (False, f"cache-ttl must be numeric, got: {value}")

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    # Validate obj-id if present
    if "obj-id" in payload:
        value = payload.get("obj-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "obj-id cannot exceed 255 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate template if present
    if "template" in payload:
        value = payload.get("template")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "template cannot exceed 63 characters")

    # Validate host-type if present
    if "host-type" in payload:
        value = payload.get("host-type")
        if value and value not in VALID_BODY_HOST_TYPE:
            return (
                False,
                f"Invalid host-type '{value}'. Must be one of: {', '.join(VALID_BODY_HOST_TYPE)}",
            )

    # Validate tenant if present
    if "tenant" in payload:
        value = payload.get("tenant")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "tenant cannot exceed 35 characters")

    # Validate epg-name if present
    if "epg-name" in payload:
        value = payload.get("epg-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "epg-name cannot exceed 255 characters")

    # Validate sdn-tag if present
    if "sdn-tag" in payload:
        value = payload.get("sdn-tag")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "sdn-tag cannot exceed 15 characters")

    # Validate filter if present
    if "filter" in payload:
        value = payload.get("filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "filter cannot exceed 2047 characters")

    # Validate sdn-addr-type if present
    if "sdn-addr-type" in payload:
        value = payload.get("sdn-addr-type")
        if value and value not in VALID_BODY_SDN_ADDR_TYPE:
            return (
                False,
                f"Invalid sdn-addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_SDN_ADDR_TYPE)}",
            )

    # Validate passive-fqdn-learning if present
    if "passive-fqdn-learning" in payload:
        value = payload.get("passive-fqdn-learning")
        if value and value not in VALID_BODY_PASSIVE_FQDN_LEARNING:
            return (
                False,
                f"Invalid passive-fqdn-learning '{value}'. Must be one of: {', '.join(VALID_BODY_PASSIVE_FQDN_LEARNING)}",
            )

    # Validate fabric-object if present
    if "fabric-object" in payload:
        value = payload.get("fabric-object")
        if value and value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid fabric-object '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_address6_put(
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
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "name cannot exceed 79 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate route-tag if present
    if "route-tag" in payload:
        value = payload.get("route-tag")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 4294967295:
                    return (
                        False,
                        "route-tag must be between 1 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (False, f"route-tag must be numeric, got: {value}")

    # Validate sdn if present
    if "sdn" in payload:
        value = payload.get("sdn")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "sdn cannot exceed 35 characters")

    # Validate fqdn if present
    if "fqdn" in payload:
        value = payload.get("fqdn")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "fqdn cannot exceed 255 characters")

    # Validate country if present
    if "country" in payload:
        value = payload.get("country")
        if value and isinstance(value, str) and len(value) > 2:
            return (False, "country cannot exceed 2 characters")

    # Validate cache-ttl if present
    if "cache-ttl" in payload:
        value = payload.get("cache-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 86400:
                    return (False, "cache-ttl must be between 0 and 86400")
            except (ValueError, TypeError):
                return (False, f"cache-ttl must be numeric, got: {value}")

    # Validate color if present
    if "color" in payload:
        value = payload.get("color")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 32:
                    return (False, "color must be between 0 and 32")
            except (ValueError, TypeError):
                return (False, f"color must be numeric, got: {value}")

    # Validate obj-id if present
    if "obj-id" in payload:
        value = payload.get("obj-id")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "obj-id cannot exceed 255 characters")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate template if present
    if "template" in payload:
        value = payload.get("template")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "template cannot exceed 63 characters")

    # Validate host-type if present
    if "host-type" in payload:
        value = payload.get("host-type")
        if value and value not in VALID_BODY_HOST_TYPE:
            return (
                False,
                f"Invalid host-type '{value}'. Must be one of: {', '.join(VALID_BODY_HOST_TYPE)}",
            )

    # Validate tenant if present
    if "tenant" in payload:
        value = payload.get("tenant")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "tenant cannot exceed 35 characters")

    # Validate epg-name if present
    if "epg-name" in payload:
        value = payload.get("epg-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "epg-name cannot exceed 255 characters")

    # Validate sdn-tag if present
    if "sdn-tag" in payload:
        value = payload.get("sdn-tag")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "sdn-tag cannot exceed 15 characters")

    # Validate filter if present
    if "filter" in payload:
        value = payload.get("filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "filter cannot exceed 2047 characters")

    # Validate sdn-addr-type if present
    if "sdn-addr-type" in payload:
        value = payload.get("sdn-addr-type")
        if value and value not in VALID_BODY_SDN_ADDR_TYPE:
            return (
                False,
                f"Invalid sdn-addr-type '{value}'. Must be one of: {', '.join(VALID_BODY_SDN_ADDR_TYPE)}",
            )

    # Validate passive-fqdn-learning if present
    if "passive-fqdn-learning" in payload:
        value = payload.get("passive-fqdn-learning")
        if value and value not in VALID_BODY_PASSIVE_FQDN_LEARNING:
            return (
                False,
                f"Invalid passive-fqdn-learning '{value}'. Must be one of: {', '.join(VALID_BODY_PASSIVE_FQDN_LEARNING)}",
            )

    # Validate fabric-object if present
    if "fabric-object" in payload:
        value = payload.get("fabric-object")
        if value and value not in VALID_BODY_FABRIC_OBJECT:
            return (
                False,
                f"Invalid fabric-object '{value}'. Must be one of: {', '.join(VALID_BODY_FABRIC_OBJECT)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_address6_delete(
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
