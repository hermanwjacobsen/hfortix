"""
Validation helpers for firewall vip endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification by generate_validators.py
Customize as needed for endpoint-specific business logic.
"""

from typing import Any

# Valid enum values from API documentation
VALID_BODY_TYPE = [
    "static-nat",
    "load-balance",
    "server-load-balance",
    "dns-translation",
    "fqdn",
    "access-proxy",
]
VALID_BODY_SERVER_TYPE = ["http", "https", "tcp", "udp", "ip"]
VALID_BODY_LDB_METHOD = [
    "static",
    "round-robin",
    "weighted",
    "least-session",
    "least-rtt",
    "first-alive",
    "http-host",
]
VALID_BODY_SRC_VIP_FILTER = ["disable", "enable"]
VALID_BODY_H2_SUPPORT = ["enable", "disable"]
VALID_BODY_H3_SUPPORT = ["enable", "disable"]
VALID_BODY_NAT44 = ["disable", "enable"]
VALID_BODY_NAT46 = ["disable", "enable"]
VALID_BODY_ADD_NAT46_ROUTE = ["disable", "enable"]
VALID_BODY_ARP_REPLY = ["disable", "enable"]
VALID_BODY_HTTP_REDIRECT = ["enable", "disable"]
VALID_BODY_PERSISTENCE = ["none", "http-cookie", "ssl-session-id"]
VALID_BODY_NAT_SOURCE_VIP = ["disable", "enable"]
VALID_BODY_PORTFORWARD = ["disable", "enable"]
VALID_BODY_STATUS = ["disable", "enable"]
VALID_BODY_PROTOCOL = ["tcp", "udp", "sctp", "icmp"]
VALID_BODY_PORTMAPPING_TYPE = ["1-to-1", "m-to-n"]
VALID_BODY_EMPTY_CERT_ACTION = ["accept", "block", "accept-unmanageable"]
VALID_BODY_USER_AGENT_DETECT = ["disable", "enable"]
VALID_BODY_CLIENT_CERT = ["disable", "enable"]
VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST = ["disable", "enable"]
VALID_BODY_HTTP_COOKIE_SHARE = ["disable", "same-ip"]
VALID_BODY_HTTPS_COOKIE_SECURE = ["disable", "enable"]
VALID_BODY_HTTP_MULTIPLEX = ["enable", "disable"]
VALID_BODY_HTTP_IP_HEADER = ["enable", "disable"]
VALID_BODY_OUTLOOK_WEB_ACCESS = ["disable", "enable"]
VALID_BODY_WEBLOGIC_SERVER = ["disable", "enable"]
VALID_BODY_WEBSPHERE_SERVER = ["disable", "enable"]
VALID_BODY_SSL_MODE = ["hal", "full"]
VALID_BODY_SSL_DH_BITS = ["768", "1024", "1536", "2048", "3072", "4096"]
VALID_BODY_SSL_ALGORITHM = ["high", "medium", "low", "custom"]
VALID_BODY_SSL_SERVER_ALGORITHM = ["high", "medium", "low", "custom", "client"]
VALID_BODY_SSL_PFS = ["require", "deny", "allow"]
VALID_BODY_SSL_MIN_VERSION = [
    "ssl-3.0",
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
]
VALID_BODY_SSL_MAX_VERSION = [
    "ssl-3.0",
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
]
VALID_BODY_SSL_SERVER_MIN_VERSION = [
    "ssl-3.0",
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
    "client",
]
VALID_BODY_SSL_SERVER_MAX_VERSION = [
    "ssl-3.0",
    "tls-1.0",
    "tls-1.1",
    "tls-1.2",
    "tls-1.3",
    "client",
]
VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS = ["enable", "disable"]
VALID_BODY_SSL_SEND_EMPTY_FRAGS = ["enable", "disable"]
VALID_BODY_SSL_CLIENT_FALLBACK = ["disable", "enable"]
VALID_BODY_SSL_CLIENT_RENEGOTIATION = ["allow", "deny", "secure"]
VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE = ["disable", "time", "count", "both"]
VALID_BODY_SSL_SERVER_RENEGOTIATION = ["enable", "disable"]
VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE = ["disable", "time", "count", "both"]
VALID_BODY_SSL_HTTP_LOCATION_CONVERSION = ["enable", "disable"]
VALID_BODY_SSL_HTTP_MATCH_HOST = ["enable", "disable"]
VALID_BODY_SSL_HPKP = ["disable", "enable", "report-only"]
VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS = ["disable", "enable"]
VALID_BODY_SSL_HSTS = ["disable", "enable"]
VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS = ["disable", "enable"]
VALID_BODY_ONE_CLICK_GSLB_SERVER = ["disable", "enable"]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_vip_get(
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


def validate_vip_post(payload: dict[str, Any]) -> tuple[bool, str | None]:
    """
    Validate POST request payload for creating vip.

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

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate dns-mapping-ttl if present
    if "dns-mapping-ttl" in payload:
        value = payload.get("dns-mapping-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 604800:
                    return (
                        False,
                        "dns-mapping-ttl must be between 0 and 604800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dns-mapping-ttl must be numeric, got: {value}",
                )

    # Validate ldb-method if present
    if "ldb-method" in payload:
        value = payload.get("ldb-method")
        if value and value not in VALID_BODY_LDB_METHOD:
            return (
                False,
                f"Invalid ldb-method '{value}'. Must be one of: {', '.join(VALID_BODY_LDB_METHOD)}",
            )

    # Validate src-vip-filter if present
    if "src-vip-filter" in payload:
        value = payload.get("src-vip-filter")
        if value and value not in VALID_BODY_SRC_VIP_FILTER:
            return (
                False,
                f"Invalid src-vip-filter '{value}'. Must be one of: {', '.join(VALID_BODY_SRC_VIP_FILTER)}",
            )

    # Validate h2-support if present
    if "h2-support" in payload:
        value = payload.get("h2-support")
        if value and value not in VALID_BODY_H2_SUPPORT:
            return (
                False,
                f"Invalid h2-support '{value}'. Must be one of: {', '.join(VALID_BODY_H2_SUPPORT)}",
            )

    # Validate h3-support if present
    if "h3-support" in payload:
        value = payload.get("h3-support")
        if value and value not in VALID_BODY_H3_SUPPORT:
            return (
                False,
                f"Invalid h3-support '{value}'. Must be one of: {', '.join(VALID_BODY_H3_SUPPORT)}",
            )

    # Validate nat44 if present
    if "nat44" in payload:
        value = payload.get("nat44")
        if value and value not in VALID_BODY_NAT44:
            return (
                False,
                f"Invalid nat44 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT44)}",
            )

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate add-nat46-route if present
    if "add-nat46-route" in payload:
        value = payload.get("add-nat46-route")
        if value and value not in VALID_BODY_ADD_NAT46_ROUTE:
            return (
                False,
                f"Invalid add-nat46-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT46_ROUTE)}",
            )

    # Validate mapped-addr if present
    if "mapped-addr" in payload:
        value = payload.get("mapped-addr")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "mapped-addr cannot exceed 79 characters")

    # Validate extintf if present
    if "extint" in payload:
        value = payload.get("extint")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "extintf cannot exceed 35 characters")

    # Validate arp-reply if present
    if "arp-reply" in payload:
        value = payload.get("arp-reply")
        if value and value not in VALID_BODY_ARP_REPLY:
            return (
                False,
                f"Invalid arp-reply '{value}'. Must be one of: {', '.join(VALID_BODY_ARP_REPLY)}",
            )

    # Validate http-redirect if present
    if "http-redirect" in payload:
        value = payload.get("http-redirect")
        if value and value not in VALID_BODY_HTTP_REDIRECT:
            return (
                False,
                f"Invalid http-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_REDIRECT)}",
            )

    # Validate persistence if present
    if "persistence" in payload:
        value = payload.get("persistence")
        if value and value not in VALID_BODY_PERSISTENCE:
            return (
                False,
                f"Invalid persistence '{value}'. Must be one of: {', '.join(VALID_BODY_PERSISTENCE)}",
            )

    # Validate nat-source-vip if present
    if "nat-source-vip" in payload:
        value = payload.get("nat-source-vip")
        if value and value not in VALID_BODY_NAT_SOURCE_VIP:
            return (
                False,
                f"Invalid nat-source-vip '{value}'. Must be one of: {', '.join(VALID_BODY_NAT_SOURCE_VIP)}",
            )

    # Validate portforward if present
    if "portforward" in payload:
        value = payload.get("portforward")
        if value and value not in VALID_BODY_PORTFORWARD:
            return (
                False,
                f"Invalid portforward '{value}'. Must be one of: {', '.join(VALID_BODY_PORTFORWARD)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate gratuitous-arp-interval if present
    if "gratuitous-arp-interval" in payload:
        value = payload.get("gratuitous-arp-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 8640000:
                    return (
                        False,
                        "gratuitous-arp-interval must be between 5 and 8640000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"gratuitous-arp-interval must be numeric, got: {value}",
                )

    # Validate portmapping-type if present
    if "portmapping-type" in payload:
        value = payload.get("portmapping-type")
        if value and value not in VALID_BODY_PORTMAPPING_TYPE:
            return (
                False,
                f"Invalid portmapping-type '{value}'. Must be one of: {', '.join(VALID_BODY_PORTMAPPING_TYPE)}",
            )

    # Validate empty-cert-action if present
    if "empty-cert-action" in payload:
        value = payload.get("empty-cert-action")
        if value and value not in VALID_BODY_EMPTY_CERT_ACTION:
            return (
                False,
                f"Invalid empty-cert-action '{value}'. Must be one of: {', '.join(VALID_BODY_EMPTY_CERT_ACTION)}",
            )

    # Validate user-agent-detect if present
    if "user-agent-detect" in payload:
        value = payload.get("user-agent-detect")
        if value and value not in VALID_BODY_USER_AGENT_DETECT:
            return (
                False,
                f"Invalid user-agent-detect '{value}'. Must be one of: {', '.join(VALID_BODY_USER_AGENT_DETECT)}",
            )

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and value not in VALID_BODY_CLIENT_CERT:
            return (
                False,
                f"Invalid client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT)}",
            )

    # Validate http-cookie-domain-from-host if present
    if "http-cookie-domain-from-host" in payload:
        value = payload.get("http-cookie-domain-from-host")
        if value and value not in VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST:
            return (
                False,
                f"Invalid http-cookie-domain-from-host '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST)}",
            )

    # Validate http-cookie-domain if present
    if "http-cookie-domain" in payload:
        value = payload.get("http-cookie-domain")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "http-cookie-domain cannot exceed 35 characters")

    # Validate http-cookie-path if present
    if "http-cookie-path" in payload:
        value = payload.get("http-cookie-path")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "http-cookie-path cannot exceed 35 characters")

    # Validate http-cookie-generation if present
    if "http-cookie-generation" in payload:
        value = payload.get("http-cookie-generation")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "http-cookie-generation must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-cookie-generation must be numeric, got: {value}",
                )

    # Validate http-cookie-age if present
    if "http-cookie-age" in payload:
        value = payload.get("http-cookie-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 525600:
                    return (
                        False,
                        "http-cookie-age must be between 0 and 525600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-cookie-age must be numeric, got: {value}",
                )

    # Validate http-cookie-share if present
    if "http-cookie-share" in payload:
        value = payload.get("http-cookie-share")
        if value and value not in VALID_BODY_HTTP_COOKIE_SHARE:
            return (
                False,
                f"Invalid http-cookie-share '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_COOKIE_SHARE)}",
            )

    # Validate https-cookie-secure if present
    if "https-cookie-secure" in payload:
        value = payload.get("https-cookie-secure")
        if value and value not in VALID_BODY_HTTPS_COOKIE_SECURE:
            return (
                False,
                f"Invalid https-cookie-secure '{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_COOKIE_SECURE)}",
            )

    # Validate http-multiplex if present
    if "http-multiplex" in payload:
        value = payload.get("http-multiplex")
        if value and value not in VALID_BODY_HTTP_MULTIPLEX:
            return (
                False,
                f"Invalid http-multiplex '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_MULTIPLEX)}",
            )

    # Validate http-multiplex-ttl if present
    if "http-multiplex-ttl" in payload:
        value = payload.get("http-multiplex-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "http-multiplex-ttl must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-multiplex-ttl must be numeric, got: {value}",
                )

    # Validate http-multiplex-max-request if present
    if "http-multiplex-max-request" in payload:
        value = payload.get("http-multiplex-max-request")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "http-multiplex-max-request must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-multiplex-max-request must be numeric, got: {value}",
                )

    # Validate http-multiplex-max-concurrent-request if present
    if "http-multiplex-max-concurrent-request" in payload:
        value = payload.get("http-multiplex-max-concurrent-request")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "http-multiplex-max-concurrent-request must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-multiplex-max-concurrent-request must be numeric, got: {value}",
                )

    # Validate http-ip-header if present
    if "http-ip-header" in payload:
        value = payload.get("http-ip-header")
        if value and value not in VALID_BODY_HTTP_IP_HEADER:
            return (
                False,
                f"Invalid http-ip-header '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_IP_HEADER)}",
            )

    # Validate http-ip-header-name if present
    if "http-ip-header-name" in payload:
        value = payload.get("http-ip-header-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "http-ip-header-name cannot exceed 35 characters")

    # Validate outlook-web-access if present
    if "outlook-web-access" in payload:
        value = payload.get("outlook-web-access")
        if value and value not in VALID_BODY_OUTLOOK_WEB_ACCESS:
            return (
                False,
                f"Invalid outlook-web-access '{value}'. Must be one of: {', '.join(VALID_BODY_OUTLOOK_WEB_ACCESS)}",
            )

    # Validate weblogic-server if present
    if "weblogic-server" in payload:
        value = payload.get("weblogic-server")
        if value and value not in VALID_BODY_WEBLOGIC_SERVER:
            return (
                False,
                f"Invalid weblogic-server '{value}'. Must be one of: {', '.join(VALID_BODY_WEBLOGIC_SERVER)}",
            )

    # Validate websphere-server if present
    if "websphere-server" in payload:
        value = payload.get("websphere-server")
        if value and value not in VALID_BODY_WEBSPHERE_SERVER:
            return (
                False,
                f"Invalid websphere-server '{value}'. Must be one of: {', '.join(VALID_BODY_WEBSPHERE_SERVER)}",
            )

    # Validate ssl-mode if present
    if "ssl-mode" in payload:
        value = payload.get("ssl-mode")
        if value and value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid ssl-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate ssl-algorithm if present
    if "ssl-algorithm" in payload:
        value = payload.get("ssl-algorithm")
        if value and value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid ssl-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )

    # Validate ssl-server-algorithm if present
    if "ssl-server-algorithm" in payload:
        value = payload.get("ssl-server-algorithm")
        if value and value not in VALID_BODY_SSL_SERVER_ALGORITHM:
            return (
                False,
                f"Invalid ssl-server-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_ALGORITHM)}",
            )

    # Validate ssl-pfs if present
    if "ssl-pfs" in payload:
        value = payload.get("ssl-pfs")
        if value and value not in VALID_BODY_SSL_PFS:
            return (
                False,
                f"Invalid ssl-pfs '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_PFS)}",
            )

    # Validate ssl-min-version if present
    if "ssl-min-version" in payload:
        value = payload.get("ssl-min-version")
        if value and value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid ssl-min-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )

    # Validate ssl-max-version if present
    if "ssl-max-version" in payload:
        value = payload.get("ssl-max-version")
        if value and value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )

    # Validate ssl-server-min-version if present
    if "ssl-server-min-version" in payload:
        value = payload.get("ssl-server-min-version")
        if value and value not in VALID_BODY_SSL_SERVER_MIN_VERSION:
            return (
                False,
                f"Invalid ssl-server-min-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_MIN_VERSION)}",
            )

    # Validate ssl-server-max-version if present
    if "ssl-server-max-version" in payload:
        value = payload.get("ssl-server-max-version")
        if value and value not in VALID_BODY_SSL_SERVER_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-server-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_MAX_VERSION)}",
            )

    # Validate ssl-accept-ffdhe-groups if present
    if "ssl-accept-ffdhe-groups" in payload:
        value = payload.get("ssl-accept-ffdhe-groups")
        if value and value not in VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS:
            return (
                False,
                f"Invalid ssl-accept-ffdhe-groups '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS)}",
            )

    # Validate ssl-send-empty-frags if present
    if "ssl-send-empty-frags" in payload:
        value = payload.get("ssl-send-empty-frags")
        if value and value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid ssl-send-empty-frags '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )

    # Validate ssl-client-fallback if present
    if "ssl-client-fallback" in payload:
        value = payload.get("ssl-client-fallback")
        if value and value not in VALID_BODY_SSL_CLIENT_FALLBACK:
            return (
                False,
                f"Invalid ssl-client-fallback '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_FALLBACK)}",
            )

    # Validate ssl-client-renegotiation if present
    if "ssl-client-renegotiation" in payload:
        value = payload.get("ssl-client-renegotiation")
        if value and value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid ssl-client-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )

    # Validate ssl-client-session-state-type if present
    if "ssl-client-session-state-type" in payload:
        value = payload.get("ssl-client-session-state-type")
        if value and value not in VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE:
            return (
                False,
                f"Invalid ssl-client-session-state-type '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE)}",
            )

    # Validate ssl-client-session-state-timeout if present
    if "ssl-client-session-state-timeout" in payload:
        value = payload.get("ssl-client-session-state-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 14400:
                    return (
                        False,
                        "ssl-client-session-state-timeout must be between 1 and 14400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-client-session-state-timeout must be numeric, got: {value}",
                )

    # Validate ssl-client-session-state-max if present
    if "ssl-client-session-state-max" in payload:
        value = payload.get("ssl-client-session-state-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10000:
                    return (
                        False,
                        "ssl-client-session-state-max must be between 1 and 10000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-client-session-state-max must be numeric, got: {value}",
                )

    # Validate ssl-client-rekey-count if present
    if "ssl-client-rekey-count" in payload:
        value = payload.get("ssl-client-rekey-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 200 or int_val > 1048576:
                    return (
                        False,
                        "ssl-client-rekey-count must be between 200 and 1048576",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-client-rekey-count must be numeric, got: {value}",
                )

    # Validate ssl-server-renegotiation if present
    if "ssl-server-renegotiation" in payload:
        value = payload.get("ssl-server-renegotiation")
        if value and value not in VALID_BODY_SSL_SERVER_RENEGOTIATION:
            return (
                False,
                f"Invalid ssl-server-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_RENEGOTIATION)}",
            )

    # Validate ssl-server-session-state-type if present
    if "ssl-server-session-state-type" in payload:
        value = payload.get("ssl-server-session-state-type")
        if value and value not in VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE:
            return (
                False,
                f"Invalid ssl-server-session-state-type '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE)}",
            )

    # Validate ssl-server-session-state-timeout if present
    if "ssl-server-session-state-timeout" in payload:
        value = payload.get("ssl-server-session-state-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 14400:
                    return (
                        False,
                        "ssl-server-session-state-timeout must be between 1 and 14400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-server-session-state-timeout must be numeric, got: {value}",
                )

    # Validate ssl-server-session-state-max if present
    if "ssl-server-session-state-max" in payload:
        value = payload.get("ssl-server-session-state-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10000:
                    return (
                        False,
                        "ssl-server-session-state-max must be between 1 and 10000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-server-session-state-max must be numeric, got: {value}",
                )

    # Validate ssl-http-location-conversion if present
    if "ssl-http-location-conversion" in payload:
        value = payload.get("ssl-http-location-conversion")
        if value and value not in VALID_BODY_SSL_HTTP_LOCATION_CONVERSION:
            return (
                False,
                f"Invalid ssl-http-location-conversion '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HTTP_LOCATION_CONVERSION)}",
            )

    # Validate ssl-http-match-host if present
    if "ssl-http-match-host" in payload:
        value = payload.get("ssl-http-match-host")
        if value and value not in VALID_BODY_SSL_HTTP_MATCH_HOST:
            return (
                False,
                f"Invalid ssl-http-match-host '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HTTP_MATCH_HOST)}",
            )

    # Validate ssl-hpkp if present
    if "ssl-hpkp" in payload:
        value = payload.get("ssl-hpkp")
        if value and value not in VALID_BODY_SSL_HPKP:
            return (
                False,
                f"Invalid ssl-hpkp '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HPKP)}",
            )

    # Validate ssl-hpkp-primary if present
    if "ssl-hpkp-primary" in payload:
        value = payload.get("ssl-hpkp-primary")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ssl-hpkp-primary cannot exceed 79 characters")

    # Validate ssl-hpkp-backup if present
    if "ssl-hpkp-backup" in payload:
        value = payload.get("ssl-hpkp-backup")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ssl-hpkp-backup cannot exceed 79 characters")

    # Validate ssl-hpkp-age if present
    if "ssl-hpkp-age" in payload:
        value = payload.get("ssl-hpkp-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 157680000:
                    return (
                        False,
                        "ssl-hpkp-age must be between 60 and 157680000",
                    )
            except (ValueError, TypeError):
                return (False, f"ssl-hpkp-age must be numeric, got: {value}")

    # Validate ssl-hpkp-report-uri if present
    if "ssl-hpkp-report-uri" in payload:
        value = payload.get("ssl-hpkp-report-uri")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "ssl-hpkp-report-uri cannot exceed 255 characters")

    # Validate ssl-hpkp-include-subdomains if present
    if "ssl-hpkp-include-subdomains" in payload:
        value = payload.get("ssl-hpkp-include-subdomains")
        if value and value not in VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid ssl-hpkp-include-subdomains '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS)}",
            )

    # Validate ssl-hsts if present
    if "ssl-hsts" in payload:
        value = payload.get("ssl-hsts")
        if value and value not in VALID_BODY_SSL_HSTS:
            return (
                False,
                f"Invalid ssl-hsts '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HSTS)}",
            )

    # Validate ssl-hsts-age if present
    if "ssl-hsts-age" in payload:
        value = payload.get("ssl-hsts-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 157680000:
                    return (
                        False,
                        "ssl-hsts-age must be between 60 and 157680000",
                    )
            except (ValueError, TypeError):
                return (False, f"ssl-hsts-age must be numeric, got: {value}")

    # Validate ssl-hsts-include-subdomains if present
    if "ssl-hsts-include-subdomains" in payload:
        value = payload.get("ssl-hsts-include-subdomains")
        if value and value not in VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid ssl-hsts-include-subdomains '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS)}",
            )

    # Validate max-embryonic-connections if present
    if "max-embryonic-connections" in payload:
        value = payload.get("max-embryonic-connections")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100000:
                    return (
                        False,
                        "max-embryonic-connections must be between 0 and 100000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-embryonic-connections must be numeric, got: {value}",
                )

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

    # Validate one-click-gslb-server if present
    if "one-click-gslb-server" in payload:
        value = payload.get("one-click-gslb-server")
        if value and value not in VALID_BODY_ONE_CLICK_GSLB_SERVER:
            return (
                False,
                f"Invalid one-click-gslb-server '{value}'. Must be one of: {', '.join(VALID_BODY_ONE_CLICK_GSLB_SERVER)}",
            )

    # Validate gslb-hostname if present
    if "gslb-hostname" in payload:
        value = payload.get("gslb-hostname")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "gslb-hostname cannot exceed 35 characters")

    # Validate gslb-domain-name if present
    if "gslb-domain-name" in payload:
        value = payload.get("gslb-domain-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "gslb-domain-name cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_vip_put(
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

    # Validate id if present
    if "id" in payload:
        value = payload.get("id")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 65535:
                    return (False, "id must be between 0 and 65535")
            except (ValueError, TypeError):
                return (False, f"id must be numeric, got: {value}")

    # Validate comment if present
    if "comment" in payload:
        value = payload.get("comment")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "comment cannot exceed 255 characters")

    # Validate type if present
    if "type" in payload:
        value = payload.get("type")
        if value and value not in VALID_BODY_TYPE:
            return (
                False,
                f"Invalid type '{value}'. Must be one of: {', '.join(VALID_BODY_TYPE)}",
            )

    # Validate server-type if present
    if "server-type" in payload:
        value = payload.get("server-type")
        if value and value not in VALID_BODY_SERVER_TYPE:
            return (
                False,
                f"Invalid server-type '{value}'. Must be one of: {', '.join(VALID_BODY_SERVER_TYPE)}",
            )

    # Validate dns-mapping-ttl if present
    if "dns-mapping-ttl" in payload:
        value = payload.get("dns-mapping-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 604800:
                    return (
                        False,
                        "dns-mapping-ttl must be between 0 and 604800",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"dns-mapping-ttl must be numeric, got: {value}",
                )

    # Validate ldb-method if present
    if "ldb-method" in payload:
        value = payload.get("ldb-method")
        if value and value not in VALID_BODY_LDB_METHOD:
            return (
                False,
                f"Invalid ldb-method '{value}'. Must be one of: {', '.join(VALID_BODY_LDB_METHOD)}",
            )

    # Validate src-vip-filter if present
    if "src-vip-filter" in payload:
        value = payload.get("src-vip-filter")
        if value and value not in VALID_BODY_SRC_VIP_FILTER:
            return (
                False,
                f"Invalid src-vip-filter '{value}'. Must be one of: {', '.join(VALID_BODY_SRC_VIP_FILTER)}",
            )

    # Validate h2-support if present
    if "h2-support" in payload:
        value = payload.get("h2-support")
        if value and value not in VALID_BODY_H2_SUPPORT:
            return (
                False,
                f"Invalid h2-support '{value}'. Must be one of: {', '.join(VALID_BODY_H2_SUPPORT)}",
            )

    # Validate h3-support if present
    if "h3-support" in payload:
        value = payload.get("h3-support")
        if value and value not in VALID_BODY_H3_SUPPORT:
            return (
                False,
                f"Invalid h3-support '{value}'. Must be one of: {', '.join(VALID_BODY_H3_SUPPORT)}",
            )

    # Validate nat44 if present
    if "nat44" in payload:
        value = payload.get("nat44")
        if value and value not in VALID_BODY_NAT44:
            return (
                False,
                f"Invalid nat44 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT44)}",
            )

    # Validate nat46 if present
    if "nat46" in payload:
        value = payload.get("nat46")
        if value and value not in VALID_BODY_NAT46:
            return (
                False,
                f"Invalid nat46 '{value}'. Must be one of: {', '.join(VALID_BODY_NAT46)}",
            )

    # Validate add-nat46-route if present
    if "add-nat46-route" in payload:
        value = payload.get("add-nat46-route")
        if value and value not in VALID_BODY_ADD_NAT46_ROUTE:
            return (
                False,
                f"Invalid add-nat46-route '{value}'. Must be one of: {', '.join(VALID_BODY_ADD_NAT46_ROUTE)}",
            )

    # Validate mapped-addr if present
    if "mapped-addr" in payload:
        value = payload.get("mapped-addr")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "mapped-addr cannot exceed 79 characters")

    # Validate extintf if present
    if "extint" in payload:
        value = payload.get("extint")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "extintf cannot exceed 35 characters")

    # Validate arp-reply if present
    if "arp-reply" in payload:
        value = payload.get("arp-reply")
        if value and value not in VALID_BODY_ARP_REPLY:
            return (
                False,
                f"Invalid arp-reply '{value}'. Must be one of: {', '.join(VALID_BODY_ARP_REPLY)}",
            )

    # Validate http-redirect if present
    if "http-redirect" in payload:
        value = payload.get("http-redirect")
        if value and value not in VALID_BODY_HTTP_REDIRECT:
            return (
                False,
                f"Invalid http-redirect '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_REDIRECT)}",
            )

    # Validate persistence if present
    if "persistence" in payload:
        value = payload.get("persistence")
        if value and value not in VALID_BODY_PERSISTENCE:
            return (
                False,
                f"Invalid persistence '{value}'. Must be one of: {', '.join(VALID_BODY_PERSISTENCE)}",
            )

    # Validate nat-source-vip if present
    if "nat-source-vip" in payload:
        value = payload.get("nat-source-vip")
        if value and value not in VALID_BODY_NAT_SOURCE_VIP:
            return (
                False,
                f"Invalid nat-source-vip '{value}'. Must be one of: {', '.join(VALID_BODY_NAT_SOURCE_VIP)}",
            )

    # Validate portforward if present
    if "portforward" in payload:
        value = payload.get("portforward")
        if value and value not in VALID_BODY_PORTFORWARD:
            return (
                False,
                f"Invalid portforward '{value}'. Must be one of: {', '.join(VALID_BODY_PORTFORWARD)}",
            )

    # Validate status if present
    if "status" in payload:
        value = payload.get("status")
        if value and value not in VALID_BODY_STATUS:
            return (
                False,
                f"Invalid status '{value}'. Must be one of: {', '.join(VALID_BODY_STATUS)}",
            )

    # Validate protocol if present
    if "protocol" in payload:
        value = payload.get("protocol")
        if value and value not in VALID_BODY_PROTOCOL:
            return (
                False,
                f"Invalid protocol '{value}'. Must be one of: {', '.join(VALID_BODY_PROTOCOL)}",
            )

    # Validate gratuitous-arp-interval if present
    if "gratuitous-arp-interval" in payload:
        value = payload.get("gratuitous-arp-interval")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 5 or int_val > 8640000:
                    return (
                        False,
                        "gratuitous-arp-interval must be between 5 and 8640000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"gratuitous-arp-interval must be numeric, got: {value}",
                )

    # Validate portmapping-type if present
    if "portmapping-type" in payload:
        value = payload.get("portmapping-type")
        if value and value not in VALID_BODY_PORTMAPPING_TYPE:
            return (
                False,
                f"Invalid portmapping-type '{value}'. Must be one of: {', '.join(VALID_BODY_PORTMAPPING_TYPE)}",
            )

    # Validate empty-cert-action if present
    if "empty-cert-action" in payload:
        value = payload.get("empty-cert-action")
        if value and value not in VALID_BODY_EMPTY_CERT_ACTION:
            return (
                False,
                f"Invalid empty-cert-action '{value}'. Must be one of: {', '.join(VALID_BODY_EMPTY_CERT_ACTION)}",
            )

    # Validate user-agent-detect if present
    if "user-agent-detect" in payload:
        value = payload.get("user-agent-detect")
        if value and value not in VALID_BODY_USER_AGENT_DETECT:
            return (
                False,
                f"Invalid user-agent-detect '{value}'. Must be one of: {', '.join(VALID_BODY_USER_AGENT_DETECT)}",
            )

    # Validate client-cert if present
    if "client-cert" in payload:
        value = payload.get("client-cert")
        if value and value not in VALID_BODY_CLIENT_CERT:
            return (
                False,
                f"Invalid client-cert '{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_CERT)}",
            )

    # Validate http-cookie-domain-from-host if present
    if "http-cookie-domain-from-host" in payload:
        value = payload.get("http-cookie-domain-from-host")
        if value and value not in VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST:
            return (
                False,
                f"Invalid http-cookie-domain-from-host '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_COOKIE_DOMAIN_FROM_HOST)}",
            )

    # Validate http-cookie-domain if present
    if "http-cookie-domain" in payload:
        value = payload.get("http-cookie-domain")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "http-cookie-domain cannot exceed 35 characters")

    # Validate http-cookie-path if present
    if "http-cookie-path" in payload:
        value = payload.get("http-cookie-path")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "http-cookie-path cannot exceed 35 characters")

    # Validate http-cookie-generation if present
    if "http-cookie-generation" in payload:
        value = payload.get("http-cookie-generation")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 4294967295:
                    return (
                        False,
                        "http-cookie-generation must be between 0 and 4294967295",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-cookie-generation must be numeric, got: {value}",
                )

    # Validate http-cookie-age if present
    if "http-cookie-age" in payload:
        value = payload.get("http-cookie-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 525600:
                    return (
                        False,
                        "http-cookie-age must be between 0 and 525600",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-cookie-age must be numeric, got: {value}",
                )

    # Validate http-cookie-share if present
    if "http-cookie-share" in payload:
        value = payload.get("http-cookie-share")
        if value and value not in VALID_BODY_HTTP_COOKIE_SHARE:
            return (
                False,
                f"Invalid http-cookie-share '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_COOKIE_SHARE)}",
            )

    # Validate https-cookie-secure if present
    if "https-cookie-secure" in payload:
        value = payload.get("https-cookie-secure")
        if value and value not in VALID_BODY_HTTPS_COOKIE_SECURE:
            return (
                False,
                f"Invalid https-cookie-secure '{value}'. Must be one of: {', '.join(VALID_BODY_HTTPS_COOKIE_SECURE)}",
            )

    # Validate http-multiplex if present
    if "http-multiplex" in payload:
        value = payload.get("http-multiplex")
        if value and value not in VALID_BODY_HTTP_MULTIPLEX:
            return (
                False,
                f"Invalid http-multiplex '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_MULTIPLEX)}",
            )

    # Validate http-multiplex-ttl if present
    if "http-multiplex-ttl" in payload:
        value = payload.get("http-multiplex-ttl")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "http-multiplex-ttl must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-multiplex-ttl must be numeric, got: {value}",
                )

    # Validate http-multiplex-max-request if present
    if "http-multiplex-max-request" in payload:
        value = payload.get("http-multiplex-max-request")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "http-multiplex-max-request must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-multiplex-max-request must be numeric, got: {value}",
                )

    # Validate http-multiplex-max-concurrent-request if present
    if "http-multiplex-max-concurrent-request" in payload:
        value = payload.get("http-multiplex-max-concurrent-request")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 2147483647:
                    return (
                        False,
                        "http-multiplex-max-concurrent-request must be between 0 and 2147483647",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"http-multiplex-max-concurrent-request must be numeric, got: {value}",
                )

    # Validate http-ip-header if present
    if "http-ip-header" in payload:
        value = payload.get("http-ip-header")
        if value and value not in VALID_BODY_HTTP_IP_HEADER:
            return (
                False,
                f"Invalid http-ip-header '{value}'. Must be one of: {', '.join(VALID_BODY_HTTP_IP_HEADER)}",
            )

    # Validate http-ip-header-name if present
    if "http-ip-header-name" in payload:
        value = payload.get("http-ip-header-name")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "http-ip-header-name cannot exceed 35 characters")

    # Validate outlook-web-access if present
    if "outlook-web-access" in payload:
        value = payload.get("outlook-web-access")
        if value and value not in VALID_BODY_OUTLOOK_WEB_ACCESS:
            return (
                False,
                f"Invalid outlook-web-access '{value}'. Must be one of: {', '.join(VALID_BODY_OUTLOOK_WEB_ACCESS)}",
            )

    # Validate weblogic-server if present
    if "weblogic-server" in payload:
        value = payload.get("weblogic-server")
        if value and value not in VALID_BODY_WEBLOGIC_SERVER:
            return (
                False,
                f"Invalid weblogic-server '{value}'. Must be one of: {', '.join(VALID_BODY_WEBLOGIC_SERVER)}",
            )

    # Validate websphere-server if present
    if "websphere-server" in payload:
        value = payload.get("websphere-server")
        if value and value not in VALID_BODY_WEBSPHERE_SERVER:
            return (
                False,
                f"Invalid websphere-server '{value}'. Must be one of: {', '.join(VALID_BODY_WEBSPHERE_SERVER)}",
            )

    # Validate ssl-mode if present
    if "ssl-mode" in payload:
        value = payload.get("ssl-mode")
        if value and value not in VALID_BODY_SSL_MODE:
            return (
                False,
                f"Invalid ssl-mode '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MODE)}",
            )

    # Validate ssl-dh-bits if present
    if "ssl-dh-bits" in payload:
        value = payload.get("ssl-dh-bits")
        if value and value not in VALID_BODY_SSL_DH_BITS:
            return (
                False,
                f"Invalid ssl-dh-bits '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_DH_BITS)}",
            )

    # Validate ssl-algorithm if present
    if "ssl-algorithm" in payload:
        value = payload.get("ssl-algorithm")
        if value and value not in VALID_BODY_SSL_ALGORITHM:
            return (
                False,
                f"Invalid ssl-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ALGORITHM)}",
            )

    # Validate ssl-server-algorithm if present
    if "ssl-server-algorithm" in payload:
        value = payload.get("ssl-server-algorithm")
        if value and value not in VALID_BODY_SSL_SERVER_ALGORITHM:
            return (
                False,
                f"Invalid ssl-server-algorithm '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_ALGORITHM)}",
            )

    # Validate ssl-pfs if present
    if "ssl-pfs" in payload:
        value = payload.get("ssl-pfs")
        if value and value not in VALID_BODY_SSL_PFS:
            return (
                False,
                f"Invalid ssl-pfs '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_PFS)}",
            )

    # Validate ssl-min-version if present
    if "ssl-min-version" in payload:
        value = payload.get("ssl-min-version")
        if value and value not in VALID_BODY_SSL_MIN_VERSION:
            return (
                False,
                f"Invalid ssl-min-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MIN_VERSION)}",
            )

    # Validate ssl-max-version if present
    if "ssl-max-version" in payload:
        value = payload.get("ssl-max-version")
        if value and value not in VALID_BODY_SSL_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_MAX_VERSION)}",
            )

    # Validate ssl-server-min-version if present
    if "ssl-server-min-version" in payload:
        value = payload.get("ssl-server-min-version")
        if value and value not in VALID_BODY_SSL_SERVER_MIN_VERSION:
            return (
                False,
                f"Invalid ssl-server-min-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_MIN_VERSION)}",
            )

    # Validate ssl-server-max-version if present
    if "ssl-server-max-version" in payload:
        value = payload.get("ssl-server-max-version")
        if value and value not in VALID_BODY_SSL_SERVER_MAX_VERSION:
            return (
                False,
                f"Invalid ssl-server-max-version '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_MAX_VERSION)}",
            )

    # Validate ssl-accept-ffdhe-groups if present
    if "ssl-accept-ffdhe-groups" in payload:
        value = payload.get("ssl-accept-ffdhe-groups")
        if value and value not in VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS:
            return (
                False,
                f"Invalid ssl-accept-ffdhe-groups '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_ACCEPT_FFDHE_GROUPS)}",
            )

    # Validate ssl-send-empty-frags if present
    if "ssl-send-empty-frags" in payload:
        value = payload.get("ssl-send-empty-frags")
        if value and value not in VALID_BODY_SSL_SEND_EMPTY_FRAGS:
            return (
                False,
                f"Invalid ssl-send-empty-frags '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SEND_EMPTY_FRAGS)}",
            )

    # Validate ssl-client-fallback if present
    if "ssl-client-fallback" in payload:
        value = payload.get("ssl-client-fallback")
        if value and value not in VALID_BODY_SSL_CLIENT_FALLBACK:
            return (
                False,
                f"Invalid ssl-client-fallback '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_FALLBACK)}",
            )

    # Validate ssl-client-renegotiation if present
    if "ssl-client-renegotiation" in payload:
        value = payload.get("ssl-client-renegotiation")
        if value and value not in VALID_BODY_SSL_CLIENT_RENEGOTIATION:
            return (
                False,
                f"Invalid ssl-client-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_RENEGOTIATION)}",
            )

    # Validate ssl-client-session-state-type if present
    if "ssl-client-session-state-type" in payload:
        value = payload.get("ssl-client-session-state-type")
        if value and value not in VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE:
            return (
                False,
                f"Invalid ssl-client-session-state-type '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_CLIENT_SESSION_STATE_TYPE)}",
            )

    # Validate ssl-client-session-state-timeout if present
    if "ssl-client-session-state-timeout" in payload:
        value = payload.get("ssl-client-session-state-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 14400:
                    return (
                        False,
                        "ssl-client-session-state-timeout must be between 1 and 14400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-client-session-state-timeout must be numeric, got: {value}",
                )

    # Validate ssl-client-session-state-max if present
    if "ssl-client-session-state-max" in payload:
        value = payload.get("ssl-client-session-state-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10000:
                    return (
                        False,
                        "ssl-client-session-state-max must be between 1 and 10000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-client-session-state-max must be numeric, got: {value}",
                )

    # Validate ssl-client-rekey-count if present
    if "ssl-client-rekey-count" in payload:
        value = payload.get("ssl-client-rekey-count")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 200 or int_val > 1048576:
                    return (
                        False,
                        "ssl-client-rekey-count must be between 200 and 1048576",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-client-rekey-count must be numeric, got: {value}",
                )

    # Validate ssl-server-renegotiation if present
    if "ssl-server-renegotiation" in payload:
        value = payload.get("ssl-server-renegotiation")
        if value and value not in VALID_BODY_SSL_SERVER_RENEGOTIATION:
            return (
                False,
                f"Invalid ssl-server-renegotiation '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_RENEGOTIATION)}",
            )

    # Validate ssl-server-session-state-type if present
    if "ssl-server-session-state-type" in payload:
        value = payload.get("ssl-server-session-state-type")
        if value and value not in VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE:
            return (
                False,
                f"Invalid ssl-server-session-state-type '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_SERVER_SESSION_STATE_TYPE)}",
            )

    # Validate ssl-server-session-state-timeout if present
    if "ssl-server-session-state-timeout" in payload:
        value = payload.get("ssl-server-session-state-timeout")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 14400:
                    return (
                        False,
                        "ssl-server-session-state-timeout must be between 1 and 14400",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-server-session-state-timeout must be numeric, got: {value}",
                )

    # Validate ssl-server-session-state-max if present
    if "ssl-server-session-state-max" in payload:
        value = payload.get("ssl-server-session-state-max")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 1 or int_val > 10000:
                    return (
                        False,
                        "ssl-server-session-state-max must be between 1 and 10000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"ssl-server-session-state-max must be numeric, got: {value}",
                )

    # Validate ssl-http-location-conversion if present
    if "ssl-http-location-conversion" in payload:
        value = payload.get("ssl-http-location-conversion")
        if value and value not in VALID_BODY_SSL_HTTP_LOCATION_CONVERSION:
            return (
                False,
                f"Invalid ssl-http-location-conversion '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HTTP_LOCATION_CONVERSION)}",
            )

    # Validate ssl-http-match-host if present
    if "ssl-http-match-host" in payload:
        value = payload.get("ssl-http-match-host")
        if value and value not in VALID_BODY_SSL_HTTP_MATCH_HOST:
            return (
                False,
                f"Invalid ssl-http-match-host '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HTTP_MATCH_HOST)}",
            )

    # Validate ssl-hpkp if present
    if "ssl-hpkp" in payload:
        value = payload.get("ssl-hpkp")
        if value and value not in VALID_BODY_SSL_HPKP:
            return (
                False,
                f"Invalid ssl-hpkp '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HPKP)}",
            )

    # Validate ssl-hpkp-primary if present
    if "ssl-hpkp-primary" in payload:
        value = payload.get("ssl-hpkp-primary")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ssl-hpkp-primary cannot exceed 79 characters")

    # Validate ssl-hpkp-backup if present
    if "ssl-hpkp-backup" in payload:
        value = payload.get("ssl-hpkp-backup")
        if value and isinstance(value, str) and len(value) > 79:
            return (False, "ssl-hpkp-backup cannot exceed 79 characters")

    # Validate ssl-hpkp-age if present
    if "ssl-hpkp-age" in payload:
        value = payload.get("ssl-hpkp-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 157680000:
                    return (
                        False,
                        "ssl-hpkp-age must be between 60 and 157680000",
                    )
            except (ValueError, TypeError):
                return (False, f"ssl-hpkp-age must be numeric, got: {value}")

    # Validate ssl-hpkp-report-uri if present
    if "ssl-hpkp-report-uri" in payload:
        value = payload.get("ssl-hpkp-report-uri")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "ssl-hpkp-report-uri cannot exceed 255 characters")

    # Validate ssl-hpkp-include-subdomains if present
    if "ssl-hpkp-include-subdomains" in payload:
        value = payload.get("ssl-hpkp-include-subdomains")
        if value and value not in VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid ssl-hpkp-include-subdomains '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HPKP_INCLUDE_SUBDOMAINS)}",
            )

    # Validate ssl-hsts if present
    if "ssl-hsts" in payload:
        value = payload.get("ssl-hsts")
        if value and value not in VALID_BODY_SSL_HSTS:
            return (
                False,
                f"Invalid ssl-hsts '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HSTS)}",
            )

    # Validate ssl-hsts-age if present
    if "ssl-hsts-age" in payload:
        value = payload.get("ssl-hsts-age")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 60 or int_val > 157680000:
                    return (
                        False,
                        "ssl-hsts-age must be between 60 and 157680000",
                    )
            except (ValueError, TypeError):
                return (False, f"ssl-hsts-age must be numeric, got: {value}")

    # Validate ssl-hsts-include-subdomains if present
    if "ssl-hsts-include-subdomains" in payload:
        value = payload.get("ssl-hsts-include-subdomains")
        if value and value not in VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS:
            return (
                False,
                f"Invalid ssl-hsts-include-subdomains '{value}'. Must be one of: {', '.join(VALID_BODY_SSL_HSTS_INCLUDE_SUBDOMAINS)}",
            )

    # Validate max-embryonic-connections if present
    if "max-embryonic-connections" in payload:
        value = payload.get("max-embryonic-connections")
        if value is not None:
            try:
                int_val = int(value)
                if int_val < 0 or int_val > 100000:
                    return (
                        False,
                        "max-embryonic-connections must be between 0 and 100000",
                    )
            except (ValueError, TypeError):
                return (
                    False,
                    f"max-embryonic-connections must be numeric, got: {value}",
                )

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

    # Validate one-click-gslb-server if present
    if "one-click-gslb-server" in payload:
        value = payload.get("one-click-gslb-server")
        if value and value not in VALID_BODY_ONE_CLICK_GSLB_SERVER:
            return (
                False,
                f"Invalid one-click-gslb-server '{value}'. Must be one of: {', '.join(VALID_BODY_ONE_CLICK_GSLB_SERVER)}",
            )

    # Validate gslb-hostname if present
    if "gslb-hostname" in payload:
        value = payload.get("gslb-hostname")
        if value and isinstance(value, str) and len(value) > 35:
            return (False, "gslb-hostname cannot exceed 35 characters")

    # Validate gslb-domain-name if present
    if "gslb-domain-name" in payload:
        value = payload.get("gslb-domain-name")
        if value and isinstance(value, str) and len(value) > 255:
            return (False, "gslb-domain-name cannot exceed 255 characters")

    return (True, None)


# ============================================================================
# DELETE Validation
# ============================================================================


def validate_vip_delete(name: str | None = None) -> tuple[bool, str | None]:
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
