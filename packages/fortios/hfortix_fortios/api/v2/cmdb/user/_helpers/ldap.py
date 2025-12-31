"""
Validation helpers for user ldap endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SERVER_IDENTITY_CHECK = ["enable", "disable"]
VALID_BODY_TYPE = ["simple", "anonymous", "regular"]
VALID_BODY_TWO_FACTOR = ["disable", "fortitoken-cloud"]
VALID_BODY_TWO_FACTOR_AUTHENTICATION = ["fortitoken", "email", "sms"]
VALID_BODY_TWO_FACTOR_NOTIFICATION = ["email", "sms"]
VALID_BODY_GROUP_MEMBER_CHECK = [
    "user-attr",
    "group-object",
    "posix-group-object",
]
VALID_BODY_SECURE = ["disable", "starttls", "ldaps"]
VALID_BODY_SSL_MIN_PROTO_VERSION = [
    "default",
    "SSLv3",
    "TLSv1",
    "TLSv1-1",
    "TLSv1-2",
    "TLSv1-3",
]
VALID_BODY_PASSWORD_EXPIRY_WARNING = ["enable", "disable"]
VALID_BODY_PASSWORD_RENEWAL = ["enable", "disable"]
VALID_BODY_ACCOUNT_KEY_PROCESSING = ["same", "strip"]
VALID_BODY_ACCOUNT_KEY_CERT_FIELD = [
    "othername",
    "rfc822name",
    "dnsname",
    "cn",
]
VALID_BODY_SEARCH_TYPE = ["recursive"]
VALID_BODY_CLIENT_CERT_AUTH = ["enable", "disable"]
VALID_BODY_OBTAIN_USER_INFO = ["enable", "disable"]
VALID_BODY_INTERFACE_SELECT_METHOD = ["auto", "sdwan", "specify"]
VALID_BODY_ANTIPHISH = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ldap_get(
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


def validate_ldap_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating ldap.

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

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate secondary-server if present
    if "secondary-server" in payload:
        value = payload.get("secondary-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "secondary-server cannot exceed 63 characters")

    # Validate tertiary-server if present
    if "tertiary-server" in payload:
        value = payload.get("tertiary-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "tertiary-server cannot exceed 63 characters")

    # Validate status-ttl if present
    if "status-ttl" in payload:
        value = payload.get("status-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 600:
                    return (False, "status-ttl must be between 0 and 600")
            except (ValueError, TypeError):
                return (False, f"status-ttl must be numeric, got: {value}")

    # Validate server-identity-check if present
    if "server-identity-check" in payload:
        value = payload.get("server-identity-check")
        if value and value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid server-identity-check '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
            )

    # Validate source-ip if present
    if "source-ip" in payload:
        value = payload.get("source-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "source-ip cannot exceed 63 characters")

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate source-port if present
    if "source-port" in payload:
        value = payload.get("source-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "source-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"source-port must be numeric, got: {value}")

    # Validate cnid if present
    if "cnid" in payload:
        value = payload.get("cnid")
        if value and isinstance(value, str) and len(value) > 20:
            return (False, "cnid cannot exceed 20 characters")

    # Validate dn if present
    if "dn" in payload:
        value = payload.get("dn")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "dn cannot exceed 511 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate two-factor if present
    if "two-factor" in payload:
        value = payload.get("two-factor")
        if value and value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid two-factor '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )

    # Validate two-factor-authentication if present
    if "two-factor-authentication" in payload:
        value = payload.get("two-factor-authentication")
        if value and value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid two-factor-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )

    # Validate two-factor-notification if present
    if "two-factor-notification" in payload:
        value = payload.get("two-factor-notification")
        if value and value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid two-factor-notification '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )

    # Validate two-factor-filter if present
    if "two-factor-filter" in payload:
        value = payload.get("two-factor-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "two-factor-filter cannot exceed 2047 characters")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "username cannot exceed 511 characters")

    # Validate group-member-check if present
    if "group-member-check" in payload:
        value = payload.get("group-member-check")
        if value and value not in VALID_BODY_GROUP_MEMBER_CHECK:
            return (
                False,
                f"Invalid group-member-check '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_MEMBER_CHECK)}",
            )

    # Validate group-search-base if present
    if "group-search-base" in payload:
        value = payload.get("group-search-base")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "group-search-base cannot exceed 511 characters")

    # Validate group-object-filter if present
    if "group-object-filter" in payload:
        value = payload.get("group-object-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (
                False,
                "group-object-filter cannot exceed 2047 characters",
            )

    # Validate group-filter if present
    if "group-filter" in payload:
        value = payload.get("group-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "group-filter cannot exceed 2047 characters")

    # Validate secure if present
    if "secure" in payload:
        value = payload.get("secure")
        if value and value not in VALID_BODY_SECURE:
            return (
                False,
                f"Invalid secure '{value}'. Must be one of: {', '.join(VALID_BODY_SECURE)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate ca-cert if present
    if "ca-cert" in payload:
        value = payload.get("ca-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ca-cert cannot exceed 79 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate password-expiry-warning if present
    if "password-expiry-warning" in payload:
        value = payload.get("password-expiry-warning")
        if value and value not in VALID_BODY_PASSWORD_EXPIRY_WARNING:
            return (
                False,
                f"Invalid password-expiry-warning '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_EXPIRY_WARNING)}",
            )

    # Validate password-renewal if present
    if "password-renewal" in payload:
        value = payload.get("password-renewal")
        if value and value not in VALID_BODY_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid password-renewal '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_RENEWAL)}",
            )

    # Validate member-attr if present
    if "member-attr" in payload:
        value = payload.get("member-attr")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "member-attr cannot exceed 63 characters")

    # Validate account-key-processing if present
    if "account-key-processing" in payload:
        value = payload.get("account-key-processing")
        if value and value not in VALID_BODY_ACCOUNT_KEY_PROCESSING:
            return (
                False,
                f"Invalid account-key-processing '{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_PROCESSING)}",
            )

    # Validate account-key-cert-field if present
    if "account-key-cert-field" in payload:
        value = payload.get("account-key-cert-field")
        if value and value not in VALID_BODY_ACCOUNT_KEY_CERT_FIELD:
            return (
                False,
                f"Invalid account-key-cert-field '{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_CERT_FIELD)}",
            )

    # Validate account-key-filter if present
    if "account-key-filter" in payload:
        value = payload.get("account-key-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "account-key-filter cannot exceed 2047 characters")

    # Validate search-type if present
    if "search-type" in payload:
        value = payload.get("search-type")
        if value and value not in VALID_BODY_SEARCH_TYPE:
            return (
                False,
                f"Invalid search-type '{value}'. Must be one of: {', '.join(VALID_BODY_SEARCH_TYPE)}",
            )

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

    # Validate obtain-user-info if present
    if "obtain-user-info" in payload:
        value = payload.get("obtain-user-info")
        if value and value not in VALID_BODY_OBTAIN_USER_INFO:
            return (
                False,
                f"Invalid obtain-user-info '{value}'. Must be one of: {', '.join(VALID_BODY_OBTAIN_USER_INFO)}",
            )

    # Validate user-info-exchange-server if present
    if "user-info-exchange-server" in payload:
        value = payload.get("user-info-exchange-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "user-info-exchange-server cannot exceed 35 characters",
            )

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

    # Validate antiphish if present
    if "antiphish" in payload:
        value = payload.get("antiphish")
        if value and value not in VALID_BODY_ANTIPHISH:
            return (
                False,
                f"Invalid antiphish '{value}'. Must be one of: {', '.join(VALID_BODY_ANTIPHISH)}",
            )

    # Validate password-attr if present
    if "password-attr" in payload:
        value = payload.get("password-attr")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "password-attr cannot exceed 35 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_ldap_put(
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

    # Validate server if present
    if "server" in payload:
        value = payload.get("server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "server cannot exceed 63 characters")

    # Validate secondary-server if present
    if "secondary-server" in payload:
        value = payload.get("secondary-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "secondary-server cannot exceed 63 characters")

    # Validate tertiary-server if present
    if "tertiary-server" in payload:
        value = payload.get("tertiary-server")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "tertiary-server cannot exceed 63 characters")

    # Validate status-ttl if present
    if "status-ttl" in payload:
        value = payload.get("status-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 600:
                    return (False, "status-ttl must be between 0 and 600")
            except (ValueError, TypeError):
                return (False, f"status-ttl must be numeric, got: {value}")

    # Validate server-identity-check if present
    if "server-identity-check" in payload:
        value = payload.get("server-identity-check")
        if value and value not in VALID_BODY_SERVER_IDENTITY_CHECK:
            return (
                False,
                f"Invalid server-identity-check '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_IDENTITY_CHECK)}",
            )

    # Validate source-ip if present
    if "source-ip" in payload:
        value = payload.get("source-ip")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "source-ip cannot exceed 63 characters")

    # Validate source-ip-interface if present
    if "source-ip-interface" in payload:
        value = payload.get("source-ip-interface")
        if value and isinstance(value, str) and len(value) > 15:
            return (False, "source-ip-interface cannot exceed 15 characters")

    # Validate source-port if present
    if "source-port" in payload:
        value = payload.get("source-port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "source-port must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"source-port must be numeric, got: {value}")

    # Validate cnid if present
    if "cnid" in payload:
        value = payload.get("cnid")
        if value and isinstance(value, str) and len(value) > 20:
            return (False, "cnid cannot exceed 20 characters")

    # Validate dn if present
    if "dn" in payload:
        value = payload.get("dn")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "dn cannot exceed 511 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate two-factor if present
    if "two-factor" in payload:
        value = payload.get("two-factor")
        if value and value not in VALID_BODY_TWO_FACTOR:
            return (
                False,
                f"Invalid two-factor '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR)}",
            )

    # Validate two-factor-authentication if present
    if "two-factor-authentication" in payload:
        value = payload.get("two-factor-authentication")
        if value and value not in VALID_BODY_TWO_FACTOR_AUTHENTICATION:
            return (
                False,
                f"Invalid two-factor-authentication '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_AUTHENTICATION)}",
            )

    # Validate two-factor-notification if present
    if "two-factor-notification" in payload:
        value = payload.get("two-factor-notification")
        if value and value not in VALID_BODY_TWO_FACTOR_NOTIFICATION:
            return (
                False,
                f"Invalid two-factor-notification '{value}'. Must be one of: {', '.join(VALID_BODY_TWO_FACTOR_NOTIFICATION)}",
            )

    # Validate two-factor-filter if present
    if "two-factor-filter" in payload:
        value = payload.get("two-factor-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "two-factor-filter cannot exceed 2047 characters")

    # Validate username if present
    if "username" in payload:
        value = payload.get("username")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "username cannot exceed 511 characters")

    # Validate group-member-check if present
    if "group-member-check" in payload:
        value = payload.get("group-member-check")
        if value and value not in VALID_BODY_GROUP_MEMBER_CHECK:
            return (
                False,
                f"Invalid group-member-check '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_MEMBER_CHECK)}",
            )

    # Validate group-search-base if present
    if "group-search-base" in payload:
        value = payload.get("group-search-base")
        if value and isinstance(value, str) and len(value) > 511:
            return (False, "group-search-base cannot exceed 511 characters")

    # Validate group-object-filter if present
    if "group-object-filter" in payload:
        value = payload.get("group-object-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (
                False,
                "group-object-filter cannot exceed 2047 characters",
            )

    # Validate group-filter if present
    if "group-filter" in payload:
        value = payload.get("group-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "group-filter cannot exceed 2047 characters")

    # Validate secure if present
    if "secure" in payload:
        value = payload.get("secure")
        if value and value not in VALID_BODY_SECURE:
            return (
                False,
                f"Invalid secure '{value}'. Must be one of: {', '.join(VALID_BODY_SECURE)}",
            )

    # Validate ssl-min-proto-version if present
    if "ssl-min-proto-version" in payload:
        value = payload.get("ssl-min-proto-version")
        if value and value not in VALID_BODY_SSL_MIN_PROTO_VERSION:
            return (
                False,
                f"Invalid ssl-min-proto-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_PROTO_VERSION)}",
            )

    # Validate ca-cert if present
    if "ca-cert" in payload:
        value = payload.get("ca-cert")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ca-cert cannot exceed 79 characters")

    # Validate port if present
    if "port" in payload:
        value = payload.get("port")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 65535:
                    return (False, "port must be between 1 and 65535")
            except (ValueError, TypeError):
                return (False, f"port must be numeric, got: {value}")

    # Validate password-expiry-warning if present
    if "password-expiry-warning" in payload:
        value = payload.get("password-expiry-warning")
        if value and value not in VALID_BODY_PASSWORD_EXPIRY_WARNING:
            return (
                False,
                f"Invalid password-expiry-warning '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_EXPIRY_WARNING)}",
            )

    # Validate password-renewal if present
    if "password-renewal" in payload:
        value = payload.get("password-renewal")
        if value and value not in VALID_BODY_PASSWORD_RENEWAL:
            return (
                False,
                f"Invalid password-renewal '{value}'. Must be one of: {', '.join(VALID_BODY_PASSWORD_RENEWAL)}",
            )

    # Validate member-attr if present
    if "member-attr" in payload:
        value = payload.get("member-attr")
        if value and isinstance(value, str) and len(value) > 63:
            return (False, "member-attr cannot exceed 63 characters")

    # Validate account-key-processing if present
    if "account-key-processing" in payload:
        value = payload.get("account-key-processing")
        if value and value not in VALID_BODY_ACCOUNT_KEY_PROCESSING:
            return (
                False,
                f"Invalid account-key-processing '{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_PROCESSING)}",
            )

    # Validate account-key-cert-field if present
    if "account-key-cert-field" in payload:
        value = payload.get("account-key-cert-field")
        if value and value not in VALID_BODY_ACCOUNT_KEY_CERT_FIELD:
            return (
                False,
                f"Invalid account-key-cert-field '{value}'. Must be one of: {', '.join(VALID_BODY_ACCOUNT_KEY_CERT_FIELD)}",
            )

    # Validate account-key-filter if present
    if "account-key-filter" in payload:
        value = payload.get("account-key-filter")
        if value and isinstance(value, str) and len(value) > 2047:
            return (False, "account-key-filter cannot exceed 2047 characters")

    # Validate search-type if present
    if "search-type" in payload:
        value = payload.get("search-type")
        if value and value not in VALID_BODY_SEARCH_TYPE:
            return (
                False,
                f"Invalid search-type '{value}'. Must be one of: {', '.join(VALID_BODY_SEARCH_TYPE)}",
            )

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

    # Validate obtain-user-info if present
    if "obtain-user-info" in payload:
        value = payload.get("obtain-user-info")
        if value and value not in VALID_BODY_OBTAIN_USER_INFO:
            return (
                False,
                f"Invalid obtain-user-info '{value}'. Must be one of: {', '.join(VALID_BODY_OBTAIN_USER_INFO)}",
            )

    # Validate user-info-exchange-server if present
    if "user-info-exchange-server" in payload:
        value = payload.get("user-info-exchange-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (
                False,
                "user-info-exchange-server cannot exceed 35 characters",
            )

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

    # Validate antiphish if present
    if "antiphish" in payload:
        value = payload.get("antiphish")
        if value and value not in VALID_BODY_ANTIPHISH:
            return (
                False,
                f"Invalid antiphish '{value}'. Must be one of: {', '.join(VALID_BODY_ANTIPHISH)}",
            )

    # Validate password-attr if present
    if "password-attr" in payload:
        value = payload.get("password-attr")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "password-attr cannot exceed 35 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_ldap_delete(name: str | None = None) -> tuple[bool, str | None]:
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
