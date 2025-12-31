"""
Validation helpers for authentication scheme endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_METHOD = [
    "ntlm",
    "basic",
    "digest",
    "form",
    "negotiate",
    "fsso",
    "rsso",
    "ssh-publickey",
    "cert",
    "saml",
    "entra-sso",
]
VALID_BODY_NEGOTIATE_NTLM = ["enable", "disable"]
VALID_BODY_REQUIRE_TFA = ["enable", "disable"]
VALID_BODY_FSSO_GUEST = ["enable", "disable"]
VALID_BODY_USER_CERT = ["enable", "disable"]
VALID_BODY_CERT_HTTP_HEADER = ["enable", "disable"]
VALID_BODY_GROUP_ATTR_TYPE = ["display-name", "external-id"]
VALID_BODY_DIGEST_ALGO = ["md5", "sha-256"]
VALID_BODY_DIGEST_RFC2069 = ["enable", "disable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_scheme_get(
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


def validate_scheme_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating scheme.

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

    # Validate method if present
    if "method" in payload:
        value = payload.get("method")
        if value and value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid method '{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )

    # Validate negotiate-ntlm if present
    if "negotiate-ntlm" in payload:
        value = payload.get("negotiate-ntlm")
        if value and value not in VALID_BODY_NEGOTIATE_NTLM:
            return (
                False,
                f"Invalid negotiate-ntlm '{value}'. Must be one of: {', '.join(VALID_BODY_NEGOTIATE_NTLM)}",
            )

    # Validate kerberos-keytab if present
    if "kerberos-keytab" in payload:
        value = payload.get("kerberos-keytab")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "kerberos-keytab cannot exceed 35 characters")

    # Validate domain-controller if present
    if "domain-controller" in payload:
        value = payload.get("domain-controller")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "domain-controller cannot exceed 35 characters")

    # Validate saml-server if present
    if "saml-server" in payload:
        value = payload.get("saml-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "saml-server cannot exceed 35 characters")

    # Validate saml-timeout if present
    if "saml-timeout" in payload:
        value = payload.get("saml-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 1200:
                    return (False, "saml-timeout must be between 30 and 1200")
            except (ValueError, TypeError):
                return (False, f"saml-timeout must be numeric, got: {value}")

    # Validate fsso-agent-for-ntlm if present
    if "fsso-agent-for-ntlm" in payload:
        value = payload.get("fsso-agent-for-ntlm")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fsso-agent-for-ntlm cannot exceed 35 characters")

    # Validate require-tfa if present
    if "require-tfa" in payload:
        value = payload.get("require-tfa")
        if value and value not in VALID_BODY_REQUIRE_TFA:
            return (
                False,
                f"Invalid require-tfa '{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_TFA)}",
            )

    # Validate fsso-guest if present
    if "fsso-guest" in payload:
        value = payload.get("fsso-guest")
        if value and value not in VALID_BODY_FSSO_GUEST:
            return (
                False,
                f"Invalid fsso-guest '{value}'. Must be one of: {', '.join(VALID_BODY_FSSO_GUEST)}",
            )

    # Validate user-cert if present
    if "user-cert" in payload:
        value = payload.get("user-cert")
        if value and value not in VALID_BODY_USER_CERT:
            return (
                False,
                f"Invalid user-cert '{value}'. Must be one of: {', '.join(VALID_BODY_USER_CERT)}",
            )

    # Validate cert-http-header if present
    if "cert-http-header" in payload:
        value = payload.get("cert-http-header")
        if value and value not in VALID_BODY_CERT_HTTP_HEADER:
            return (
                False,
                f"Invalid cert-http-header '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_HTTP_HEADER)}",
            )

    # Validate ssh-ca if present
    if "ssh-ca" in payload:
        value = payload.get("ssh-ca")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssh-ca cannot exceed 35 characters")

    # Validate external-idp if present
    if "external-idp" in payload:
        value = payload.get("external-idp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "external-idp cannot exceed 35 characters")

    # Validate group-attr-type if present
    if "group-attr-type" in payload:
        value = payload.get("group-attr-type")
        if value and value not in VALID_BODY_GROUP_ATTR_TYPE:
            return (
                False,
                f"Invalid group-attr-type '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_ATTR_TYPE)}",
            )

    # Validate digest-algo if present
    if "digest-algo" in payload:
        value = payload.get("digest-algo")
        if value and value not in VALID_BODY_DIGEST_ALGO:
            return (
                False,
                f"Invalid digest-algo '{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_ALGO)}",
            )

    # Validate digest-rfc2069 if present
    if "digest-rfc2069" in payload:
        value = payload.get("digest-rfc2069")
        if value and value not in VALID_BODY_DIGEST_RFC2069:
            return (
                False,
                f"Invalid digest-rfc2069 '{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_RFC2069)}",
            )

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_scheme_put(
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

    # Validate method if present
    if "method" in payload:
        value = payload.get("method")
        if value and value not in VALID_BODY_METHOD:
            return (
                False,
                f"Invalid method '{value}'. Must be one of: {', '.join(VALID_BODY_METHOD)}",
            )

    # Validate negotiate-ntlm if present
    if "negotiate-ntlm" in payload:
        value = payload.get("negotiate-ntlm")
        if value and value not in VALID_BODY_NEGOTIATE_NTLM:
            return (
                False,
                f"Invalid negotiate-ntlm '{value}'. Must be one of: {', '.join(VALID_BODY_NEGOTIATE_NTLM)}",
            )

    # Validate kerberos-keytab if present
    if "kerberos-keytab" in payload:
        value = payload.get("kerberos-keytab")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "kerberos-keytab cannot exceed 35 characters")

    # Validate domain-controller if present
    if "domain-controller" in payload:
        value = payload.get("domain-controller")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "domain-controller cannot exceed 35 characters")

    # Validate saml-server if present
    if "saml-server" in payload:
        value = payload.get("saml-server")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "saml-server cannot exceed 35 characters")

    # Validate saml-timeout if present
    if "saml-timeout" in payload:
        value = payload.get("saml-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 30 or int_val > 1200:
                    return (False, "saml-timeout must be between 30 and 1200")
            except (ValueError, TypeError):
                return (False, f"saml-timeout must be numeric, got: {value}")

    # Validate fsso-agent-for-ntlm if present
    if "fsso-agent-for-ntlm" in payload:
        value = payload.get("fsso-agent-for-ntlm")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "fsso-agent-for-ntlm cannot exceed 35 characters")

    # Validate require-tfa if present
    if "require-tfa" in payload:
        value = payload.get("require-tfa")
        if value and value not in VALID_BODY_REQUIRE_TFA:
            return (
                False,
                f"Invalid require-tfa '{value}'. Must be one of: {', '.join(VALID_BODY_REQUIRE_TFA)}",
            )

    # Validate fsso-guest if present
    if "fsso-guest" in payload:
        value = payload.get("fsso-guest")
        if value and value not in VALID_BODY_FSSO_GUEST:
            return (
                False,
                f"Invalid fsso-guest '{value}'. Must be one of: {', '.join(VALID_BODY_FSSO_GUEST)}",
            )

    # Validate user-cert if present
    if "user-cert" in payload:
        value = payload.get("user-cert")
        if value and value not in VALID_BODY_USER_CERT:
            return (
                False,
                f"Invalid user-cert '{value}'. Must be one of: {', '.join(VALID_BODY_USER_CERT)}",
            )

    # Validate cert-http-header if present
    if "cert-http-header" in payload:
        value = payload.get("cert-http-header")
        if value and value not in VALID_BODY_CERT_HTTP_HEADER:
            return (
                False,
                f"Invalid cert-http-header '{value}'. Must be one of: {', '.join(VALID_BODY_CERT_HTTP_HEADER)}",
            )

    # Validate ssh-ca if present
    if "ssh-ca" in payload:
        value = payload.get("ssh-ca")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "ssh-ca cannot exceed 35 characters")

    # Validate external-idp if present
    if "external-idp" in payload:
        value = payload.get("external-idp")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "external-idp cannot exceed 35 characters")

    # Validate group-attr-type if present
    if "group-attr-type" in payload:
        value = payload.get("group-attr-type")
        if value and value not in VALID_BODY_GROUP_ATTR_TYPE:
            return (
                False,
                f"Invalid group-attr-type '{value}'. Must be one of: {', '.join(VALID_BODY_GROUP_ATTR_TYPE)}",
            )

    # Validate digest-algo if present
    if "digest-algo" in payload:
        value = payload.get("digest-algo")
        if value and value not in VALID_BODY_DIGEST_ALGO:
            return (
                False,
                f"Invalid digest-algo '{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_ALGO)}",
            )

    # Validate digest-rfc2069 if present
    if "digest-rfc2069" in payload:
        value = payload.get("digest-rfc2069")
        if value and value not in VALID_BODY_DIGEST_RFC2069:
            return (
                False,
                f"Invalid digest-rfc2069 '{value}'. Must be one of: {', '.join(VALID_BODY_DIGEST_RFC2069)}",
            )

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_scheme_delete(name: str | None = None) -> tuple[bool, str | None]:
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
