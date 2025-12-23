"""
Validation helpers for system ssh_config endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_SSH_KEX_ALGO = [
    "diffie-hellman-group1-sha1",
    "diffie-hellman-group14-sha1",
    "diffie-hellman-group14-sha256",
    "diffie-hellman-group16-sha512",
    "diffie-hellman-group18-sha512",
    "diffie-hellman-group-exchange-sha1",
    "diffie-hellman-group-exchange-sha256",
    "curve25519-sha256@libssh.org",
    "ecdh-sha2-nistp256",
    "ecdh-sha2-nistp384",
    "ecdh-sha2-nistp521",
]
VALID_BODY_SSH_ENC_ALGO = [
    "chacha20-poly1305@openssh.com",
    "aes128-ctr",
    "aes192-ctr",
    "aes256-ctr",
    "arcfour256",
    "arcfour128",
    "aes128-cbc",
    "3des-cbc",
    "blowfish-cbc",
    "cast128-cbc",
    "aes192-cbc",
    "aes256-cbc",
    "arcfour",
    "rijndael-cbc@lysator.liu.se",
    "aes128-gcm@openssh.com",
    "aes256-gcm@openssh.com",
]
VALID_BODY_SSH_MAC_ALGO = [
    "hmac-md5",
    "hmac-md5-etm@openssh.com",
    "hmac-md5-96",
    "hmac-md5-96-etm@openssh.com",
    "hmac-sha1",
    "hmac-sha1-etm@openssh.com",
    "hmac-sha2-256",
    "hmac-sha2-256-etm@openssh.com",
    "hmac-sha2-512",
    "hmac-sha2-512-etm@openssh.com",
    "hmac-ripemd160",
    "hmac-ripemd160@openssh.com",
    "hmac-ripemd160-etm@openssh.com",
    "umac-64@openssh.com",
    "umac-128@openssh.com",
    "umac-64-etm@openssh.com",
    "umac-128-etm@openssh.com",
]
VALID_BODY_SSH_HSK_ALGO = [
    "ssh-rsa",
    "ecdsa-sha2-nistp521",
    "ecdsa-sha2-nistp384",
    "ecdsa-sha2-nistp256",
    "rsa-sha2-256",
    "rsa-sha2-512",
    "ssh-ed25519",
]
VALID_BODY_SSH_HSK_OVERRIDE = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_ssh_config_get(
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


def validate_ssh_config_put(
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

    # Validate ssh-kex-algo if present
    if "ssh-kex-algo" in payload:
        value = payload.get("ssh-kex-algo")
        if value and value not in VALID_BODY_SSH_KEX_ALGO:
            return (
                False,
                f"Invalid ssh-kex-algo '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_KEX_ALGO)}",
            )

    # Validate ssh-enc-algo if present
    if "ssh-enc-algo" in payload:
        value = payload.get("ssh-enc-algo")
        if value and value not in VALID_BODY_SSH_ENC_ALGO:
            return (
                False,
                f"Invalid ssh-enc-algo '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_ENC_ALGO)}",
            )

    # Validate ssh-mac-algo if present
    if "ssh-mac-algo" in payload:
        value = payload.get("ssh-mac-algo")
        if value and value not in VALID_BODY_SSH_MAC_ALGO:
            return (
                False,
                f"Invalid ssh-mac-algo '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_MAC_ALGO)}",
            )

    # Validate ssh-hsk-algo if present
    if "ssh-hsk-algo" in payload:
        value = payload.get("ssh-hsk-algo")
        if value and value not in VALID_BODY_SSH_HSK_ALGO:
            return (
                False,
                f"Invalid ssh-hsk-algo '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_HSK_ALGO)}",
            )

    # Validate ssh-hsk-override if present
    if "ssh-hsk-override" in payload:
        value = payload.get("ssh-hsk-override")
        if value and value not in VALID_BODY_SSH_HSK_OVERRIDE:
            return (
                False,
                f"Invalid ssh-hsk-override '{value}'. Must be one of: {', '.join(VALID_BODY_SSH_HSK_OVERRIDE)}",
            )

    return (True, None)
