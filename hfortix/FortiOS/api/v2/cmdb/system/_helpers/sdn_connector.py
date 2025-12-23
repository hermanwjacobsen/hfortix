"""
Validation helpers for system sdn_connector endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_STATUS = ["disable", "enable"]
VALID_BODY_TYPE = [
    "aci",
    "alicloud",
    "aws",
    "azure",
    "gcp",
    "nsx",
    "nuage",
    "oci",
    "openstack",
    "kubernetes",
    "vmware",
    "sepm",
    "aci-direct",
    "ibm",
    "nutanix",
    "sap",
]
VALID_BODY_USE_METADATA_IAM = ["disable", "enable"]
VALID_BODY_MICROSOFT_365 = ["disable", "enable"]
VALID_BODY_HA_STATUS = ["disable", "enable"]
VALID_BODY_VERIFY_CERTIFICATE = ["disable", "enable"]
VALID_BODY_ALT_RESOURCE_IP = ["disable", "enable"]
VALID_BODY_AZURE_REGION = ["global", "china", "germany", "usgov", "local"]
VALID_BODY_OCI_REGION_TYPE = ["commercial", "government"]
VALID_BODY_IBM_REGION = [
    "dallas",
    "washington-dc",
    "london",
    "frankfurt",
    "sydney",
    "tokyo",
    "osaka",
    "toronto",
    "sao-paulo",
    "madrid",
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_sdn_connector_get(
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


def validate_sdn_connector_post(
    payload: dict[str, Any],
) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating sdn_connector.

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

    # Validate proxy if present
    if "proxy" in payload:
        value = payload.get("proxy")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "proxy cannot exceed 35 characters")

    # Validate use-metadata-iam if present
    if "use-metadata-iam" in payload:
        value = payload.get("use-metadata-iam")
        if value and value not in VALID_BODY_USE_METADATA_IAM:
            return (
                False,
                f"Invalid use-metadata-iam '{value}'. Must be one of: {', '.join(VALID_BODY_USE_METADATA_IAM)}",
            )

    # Validate microsoft-365 if present
    if "microsoft-365" in payload:
        value = payload.get("microsoft-365")
        if value and value not in VALID_BODY_MICROSOFT_365:
            return (
                False,
                f"Invalid microsoft-365 '{value}'. Must be one of: {', '.join(VALID_BODY_MICROSOFT_365)}",
            )

    # Validate ha-status if present
    if "ha-status" in payload:
        value = payload.get("ha-status")
        if value and value not in VALID_BODY_HA_STATUS:
            return (
                False,
                f"Invalid ha-status '{value}'. Must be one of: {', '.join(VALID_BODY_HA_STATUS)}",
            )

    # Validate verify-certificate if present
    if "verify-certificate" in payload:
        value = payload.get("verify-certificate")
        if value and value not in VALID_BODY_VERIFY_CERTIFICATE:
            return (
                False,
                f"Invalid verify-certificate '{value}'. Must be one of: {', '.join(VALID_BODY_VERIFY_CERTIFICATE)}",
            )

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "server cannot exceed 127 characters")

    # Validate server-port if present
    if "server-port" in payload:
        value = payload.get("server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "server-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"server-port must be numeric, got: {value}")

    # Validate message-server-port if present
    if "message-server-port" in payload:
        value = payload.get("message-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "message-server-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"message-server-port must be numeric, got: {value}",
                )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate vcenter-server if present
    if "vcenter-server" in payload:
        value = payload.get("vcenter-server")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "vcenter-server cannot exceed 127 characters")

    # Validate vcenter-username if present
    if "vcenter-username" in payload:
        value = payload.get("vcenter-username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "vcenter-username cannot exceed 64 characters")

    # Validate access-key if present
    if "access-key" in payload:
        value = payload.get("access-key")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "access-key cannot exceed 31 characters")

    # Validate region if present
    if "region" in payload:
        value = payload.get("region")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "region cannot exceed 31 characters")

    # Validate vpc-id if present
    if "vpc-id" in payload:
        value = payload.get("vpc-id")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vpc-id cannot exceed 31 characters")

    # Validate alt-resource-ip if present
    if "alt-resource-ip" in payload:
        value = payload.get("alt-resource-ip")
        if value and value not in VALID_BODY_ALT_RESOURCE_IP:
            return (
                False,
                f"Invalid alt-resource-ip '{value}'. Must be one of: {', '.join(VALID_BODY_ALT_RESOURCE_IP)}",
            )

    # Validate tenant-id if present
    if "tenant-id" in payload:
        value = payload.get("tenant-id")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "tenant-id cannot exceed 127 characters")

    # Validate client-id if present
    if "client-id" in payload:
        value = payload.get("client-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "client-id cannot exceed 63 characters")

    # Validate subscription-id if present
    if "subscription-id" in payload:
        value = payload.get("subscription-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "subscription-id cannot exceed 63 characters")

    # Validate resource-group if present
    if "resource-group" in payload:
        value = payload.get("resource-group")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "resource-group cannot exceed 63 characters")

    # Validate login-endpoint if present
    if "login-endpoint" in payload:
        value = payload.get("login-endpoint")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "login-endpoint cannot exceed 127 characters")

    # Validate resource-url if present
    if "resource-url" in payload:
        value = payload.get("resource-url")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "resource-url cannot exceed 127 characters")

    # Validate azure-region if present
    if "azure-region" in payload:
        value = payload.get("azure-region")
        if value and value not in VALID_BODY_AZURE_REGION:
            return (
                False,
                f"Invalid azure-region '{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_REGION)}",
            )

    # Validate user-id if present
    if "user-id" in payload:
        value = payload.get("user-id")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "user-id cannot exceed 127 characters")

    # Validate oci-region-type if present
    if "oci-region-type" in payload:
        value = payload.get("oci-region-type")
        if value and value not in VALID_BODY_OCI_REGION_TYPE:
            return (
                False,
                f"Invalid oci-region-type '{value}'. Must be one of: {', '.join(VALID_BODY_OCI_REGION_TYPE)}",
            )

    # Validate oci-cert if present
    if "oci-cert" in payload:
        value = payload.get("oci-cert")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "oci-cert cannot exceed 63 characters")

    # Validate oci-fingerprint if present
    if "oci-fingerprint" in payload:
        value = payload.get("oci-fingerprint")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "oci-fingerprint cannot exceed 63 characters")

    # Validate service-account if present
    if "service-account" in payload:
        value = payload.get("service-account")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "service-account cannot exceed 127 characters")

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "domain cannot exceed 127 characters")

    # Validate group-name if present
    if "group-name" in payload:
        value = payload.get("group-name")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "group-name cannot exceed 127 characters")

    # Validate server-cert if present
    if "server-cert" in payload:
        value = payload.get("server-cert")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "server-cert cannot exceed 127 characters")

    # Validate server-ca-cert if present
    if "server-ca-cert" in payload:
        value = payload.get("server-ca-cert")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "server-ca-cert cannot exceed 127 characters")

    # Validate ibm-region if present
    if "ibm-region" in payload:
        value = payload.get("ibm-region")
        if value and value not in VALID_BODY_IBM_REGION:
            return (
                False,
                f"Invalid ibm-region '{value}'. Must be one of: {', '.join(VALID_BODY_IBM_REGION)}",
            )

    # Validate par-id if present
    if "par-id" in payload:
        value = payload.get("par-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "par-id cannot exceed 63 characters")

    # Validate update-interval if present
    if "update-interval" in payload:
        value = payload.get("update-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3600:
                    return (
                        False,
                        "update-interval must be between 0 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"update-interval must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_sdn_connector_put(
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

    # Validate proxy if present
    if "proxy" in payload:
        value = payload.get("proxy")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "proxy cannot exceed 35 characters")

    # Validate use-metadata-iam if present
    if "use-metadata-iam" in payload:
        value = payload.get("use-metadata-iam")
        if value and value not in VALID_BODY_USE_METADATA_IAM:
            return (
                False,
                f"Invalid use-metadata-iam '{value}'. Must be one of: {', '.join(VALID_BODY_USE_METADATA_IAM)}",
            )

    # Validate microsoft-365 if present
    if "microsoft-365" in payload:
        value = payload.get("microsoft-365")
        if value and value not in VALID_BODY_MICROSOFT_365:
            return (
                False,
                f"Invalid microsoft-365 '{value}'. Must be one of: {', '.join(VALID_BODY_MICROSOFT_365)}",
            )

    # Validate ha-status if present
    if "ha-status" in payload:
        value = payload.get("ha-status")
        if value and value not in VALID_BODY_HA_STATUS:
            return (
                False,
                f"Invalid ha-status '{value}'. Must be one of: {', '.join(VALID_BODY_HA_STATUS)}",
            )

    # Validate verify-certificate if present
    if "verify-certificate" in payload:
        value = payload.get("verify-certificate")
        if value and value not in VALID_BODY_VERIFY_CERTIFICATE:
            return (
                False,
                f"Invalid verify-certificate '{value}'. Must be one of: {', '.join(VALID_BODY_VERIFY_CERTIFICATE)}",
            )

    # Validate vdom if present
    if "vdom" in payload:
        value = payload.get("vdom")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vdom cannot exceed 31 characters")

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "server cannot exceed 127 characters")

    # Validate server-port if present
    if "server-port" in payload:
        value = payload.get("server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "server-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"server-port must be numeric, got: {value}")

    # Validate message-server-port if present
    if "message-server-port" in payload:
        value = payload.get("message-server-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (
                        False,
                        "message-server-port must be between 0 and 65535",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"message-server-port must be numeric, got: {value}",
                )

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "username cannot exceed 64 characters")

    # Validate vcenter-server if present
    if "vcenter-server" in payload:
        value = payload.get("vcenter-server")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "vcenter-server cannot exceed 127 characters")

    # Validate vcenter-username if present
    if "vcenter-username" in payload:
        value = payload.get("vcenter-username")
        if value and isinstance(value, str) and len(value) > 64:
            return (False, "vcenter-username cannot exceed 64 characters")

    # Validate access-key if present
    if "access-key" in payload:
        value = payload.get("access-key")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "access-key cannot exceed 31 characters")

    # Validate region if present
    if "region" in payload:
        value = payload.get("region")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "region cannot exceed 31 characters")

    # Validate vpc-id if present
    if "vpc-id" in payload:
        value = payload.get("vpc-id")
        if value and isinstance(value, str) and len(value) > 31:
            return (False, "vpc-id cannot exceed 31 characters")

    # Validate alt-resource-ip if present
    if "alt-resource-ip" in payload:
        value = payload.get("alt-resource-ip")
        if value and value not in VALID_BODY_ALT_RESOURCE_IP:
            return (
                False,
                f"Invalid alt-resource-ip '{value}'. Must be one of: {', '.join(VALID_BODY_ALT_RESOURCE_IP)}",
            )

    # Validate tenant-id if present
    if "tenant-id" in payload:
        value = payload.get("tenant-id")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "tenant-id cannot exceed 127 characters")

    # Validate client-id if present
    if "client-id" in payload:
        value = payload.get("client-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "client-id cannot exceed 63 characters")

    # Validate subscription-id if present
    if "subscription-id" in payload:
        value = payload.get("subscription-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "subscription-id cannot exceed 63 characters")

    # Validate resource-group if present
    if "resource-group" in payload:
        value = payload.get("resource-group")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "resource-group cannot exceed 63 characters")

    # Validate login-endpoint if present
    if "login-endpoint" in payload:
        value = payload.get("login-endpoint")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "login-endpoint cannot exceed 127 characters")

    # Validate resource-url if present
    if "resource-url" in payload:
        value = payload.get("resource-url")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "resource-url cannot exceed 127 characters")

    # Validate azure-region if present
    if "azure-region" in payload:
        value = payload.get("azure-region")
        if value and value not in VALID_BODY_AZURE_REGION:
            return (
                False,
                f"Invalid azure-region '{value}'. Must be one of: {', '.join(VALID_BODY_AZURE_REGION)}",
            )

    # Validate user-id if present
    if "user-id" in payload:
        value = payload.get("user-id")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "user-id cannot exceed 127 characters")

    # Validate oci-region-type if present
    if "oci-region-type" in payload:
        value = payload.get("oci-region-type")
        if value and value not in VALID_BODY_OCI_REGION_TYPE:
            return (
                False,
                f"Invalid oci-region-type '{value}'. Must be one of: {', '.join(VALID_BODY_OCI_REGION_TYPE)}",
            )

    # Validate oci-cert if present
    if "oci-cert" in payload:
        value = payload.get("oci-cert")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "oci-cert cannot exceed 63 characters")

    # Validate oci-fingerprint if present
    if "oci-fingerprint" in payload:
        value = payload.get("oci-fingerprint")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "oci-fingerprint cannot exceed 63 characters")

    # Validate service-account if present
    if "service-account" in payload:
        value = payload.get("service-account")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "service-account cannot exceed 127 characters")

    # Validate domain if present
    if "domain" in payload:
        value = payload.get("domain")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "domain cannot exceed 127 characters")

    # Validate group-name if present
    if "group-name" in payload:
        value = payload.get("group-name")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "group-name cannot exceed 127 characters")

    # Validate server-cert if present
    if "server-cert" in payload:
        value = payload.get("server-cert")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "server-cert cannot exceed 127 characters")

    # Validate server-ca-cert if present
    if "server-ca-cert" in payload:
        value = payload.get("server-ca-cert")
        if value and isinstance(value, str) and len(value) > 127:
            return (False, "server-ca-cert cannot exceed 127 characters")

    # Validate ibm-region if present
    if "ibm-region" in payload:
        value = payload.get("ibm-region")
        if value and value not in VALID_BODY_IBM_REGION:
            return (
                False,
                f"Invalid ibm-region '{value}'. Must be one of: {', '.join(VALID_BODY_IBM_REGION)}",
            )

    # Validate par-id if present
    if "par-id" in payload:
        value = payload.get("par-id")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "par-id cannot exceed 63 characters")

    # Validate update-interval if present
    if "update-interval" in payload:
        value = payload.get("update-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 3600:
                    return (
                        False,
                        "update-interval must be between 0 and 3600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"update-interval must be numeric, got: {value}",
                )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_sdn_connector_delete(
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
