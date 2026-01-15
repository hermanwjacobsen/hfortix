"""
FortiOS CMDB - Firewall vip6

Configuration endpoint for managing cmdb firewall/vip6 objects.

API Endpoints:
    GET    /cmdb/firewall/vip6
    POST   /cmdb/firewall/vip6
    PUT    /cmdb/firewall/vip6/{identifier}
    DELETE /cmdb/firewall/vip6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_vip6.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.firewall_vip6.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
    normalize_table_field,  # For table field normalization
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Vip6(CRUDEndpoint, MetadataMixin):
    """Vip6 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "vip6"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "src_filter": {
            "mkey": "range",
            "required_fields": ['range'],
            "example": "[{'range': 'value'}]",
        },
        "realservers": {
            "mkey": "id",
            "required_fields": ['ip'],
            "example": "[{'ip': '192.168.1.10'}]",
        },
        "ssl_certificate": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "ssl_cipher_suites": {
            "mkey": "priority",
            "required_fields": ['cipher'],
            "example": "[{'cipher': 'TLS-AES-128-GCM-SHA256'}]",
        },
        "ssl_server_cipher_suites": {
            "mkey": "priority",
            "required_fields": ['cipher'],
            "example": "[{'cipher': 'TLS-AES-128-GCM-SHA256'}]",
        },
        "monitor": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
    }
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Vip6 endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        q_datasource: bool | None = None,
        q_skip_to: int | None = None,
        q_with_meta: bool | None = None,
        q_with_contents_hash: bool | None = None,
        q_skip: bool | None = None,
        q_format: list[str] | None = None,
        q_key: str | None = None,
        q_pattern: str | None = None,
        q_scope: str | None = None,
        q_exclude_default_values: bool | None = None,
        q_datasource_format: dict[str, Any] | None = None,
        q_unfiltered_count: int | None = None,
        q_stat_items: str | None = None,
        q_primary_keys: str | None = None,
        q_action: Literal["default", "schema"] | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve firewall/vip6 configuration.

        Configure virtual IP for IPv6.

        Args:
            name: String identifier to retrieve specific object.
                If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance or list of FortiObject instances. Returns Coroutine if using async client.
            Use .dict, .json, or .raw properties to access as dictionary.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all firewall/vip6 objects
            >>> result = fgt.api.cmdb.firewall_vip6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/vip6 by name
            >>> result = fgt.api.cmdb.firewall_vip6.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_vip6.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.firewall_vip6.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.firewall_vip6.get_schema()

        See Also:
            - post(): Create new firewall/vip6 object
            - put(): Update existing firewall/vip6 object
            - delete(): Remove firewall/vip6 object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        if q_datasource is not None:
            params["datasource"] = q_datasource
        if q_skip_to is not None:
            params["skip_to"] = q_skip_to
        if q_with_meta is not None:
            params["with_meta"] = q_with_meta
        if q_with_contents_hash is not None:
            params["with_contents_hash"] = q_with_contents_hash
        if q_skip is not None:
            params["skip"] = q_skip
        if q_format is not None:
            params["format"] = q_format
        if q_key is not None:
            params["key"] = q_key
        if q_pattern is not None:
            params["pattern"] = q_pattern
        if q_scope is not None:
            params["scope"] = q_scope
        if q_exclude_default_values is not None:
            params["exclude-default-values"] = q_exclude_default_values
        if q_datasource_format is not None:
            params["datasource_format"] = q_datasource_format
        if q_unfiltered_count is not None:
            params["unfiltered_count"] = q_unfiltered_count
        if q_stat_items is not None:
            params["stat-items"] = q_stat_items
        if q_primary_keys is not None:
            params["primary_keys"] = q_primary_keys
        if q_action is not None:
            params["action"] = q_action
        
        if name:
            endpoint = "/firewall/vip6/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/firewall/vip6"
            unwrap_single = False
        
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.firewall_vip6.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.firewall_vip6.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    # ========================================================================
    # PUT Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        comment: str | None = None,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = None,
        src_filter: str | list[str] | list[dict[str, Any]] | None = None,
        src_vip_filter: Literal["disable", "enable"] | None = None,
        extip: str | None = None,
        mappedip: str | None = None,
        nat_source_vip: Literal["disable", "enable"] | None = None,
        ndp_reply: Literal["disable", "enable"] | None = None,
        portforward: Literal["disable", "enable"] | None = None,
        protocol: Literal["tcp", "udp", "sctp"] | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        color: int | None = None,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = None,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = None,
        http_redirect: Literal["enable", "disable"] | None = None,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = None,
        h2_support: Literal["enable", "disable"] | None = None,
        h3_support: Literal["enable", "disable"] | None = None,
        quic: str | None = None,
        nat66: Literal["disable", "enable"] | None = None,
        nat64: Literal["disable", "enable"] | None = None,
        add_nat64_route: Literal["disable", "enable"] | None = None,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = None,
        user_agent_detect: Literal["disable", "enable"] | None = None,
        client_cert: Literal["disable", "enable"] | None = None,
        realservers: str | list[str] | list[dict[str, Any]] | None = None,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: Literal["disable", "same-ip"] | None = None,
        https_cookie_secure: Literal["disable", "enable"] | None = None,
        http_multiplex: Literal["enable", "disable"] | None = None,
        http_ip_header: Literal["enable", "disable"] | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: Literal["disable", "enable"] | None = None,
        weblogic_server: Literal["disable", "enable"] | None = None,
        websphere_server: Literal["disable", "enable"] | None = None,
        ssl_mode: Literal["half", "full"] | None = None,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = None,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = None,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = None,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = None,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_pfs: Literal["require", "deny", "allow"] | None = None,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = None,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = None,
        ssl_client_fallback: Literal["disable", "enable"] | None = None,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = None,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = None,
        ssl_http_match_host: Literal["enable", "disable"] | None = None,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = None,
        ssl_hsts: Literal["disable", "enable"] | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = None,
        monitor: str | list[str] | list[dict[str, Any]] | None = None,
        max_embryonic_connections: int | None = None,
        embedded_ipv4_address: Literal["disable", "enable"] | None = None,
        ipv4_mappedip: str | None = None,
        ipv4_mappedport: str | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing firewall/vip6 object.

        Configure virtual IP for IPv6.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Virtual ip6 name.
            id: Custom defined ID.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            comment: Comment.
            type: Configure a static NAT server load balance VIP or access proxy.
            src_filter: Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses with spaces.
                Default format: [{'range': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'range': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'range': 'val1'}, ...]
                  - List of dicts: [{'range': 'value'}] (recommended)
            src_vip_filter: Enable/disable use of 'src-filter' to match destinations for the reverse SNAT rule.
            extip: IPv6 address or address range on the external interface that you want to map to an address or address range on the destination network.
            mappedip: Mapped IPv6 address range in the format startIP-endIP.
            nat_source_vip: Enable to perform SNAT on traffic from mappedip to the extip for all egress interfaces.
            ndp_reply: Enable/disable this FortiGate unit's ability to respond to NDP requests for this virtual IP address (default = enable).
            portforward: Enable port forwarding.
            protocol: Protocol to use when forwarding packets.
            extport: Incoming port number range that you want to map to a port number range on the destination network.
            mappedport: Port number range on the destination network to which the external port number range is mapped.
            color: Color of icon on the GUI.
            ldb_method: Method used to distribute sessions to real servers.
            server_type: Protocol to be load balanced by the virtual server (also called the server load balance virtual IP).
            http_redirect: Enable/disable redirection of HTTP to HTTPS.
            persistence: Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.
            h2_support: Enable/disable HTTP2 support (default = enable).
            h3_support: Enable/disable HTTP3/QUIC support (default = disable).
            quic: QUIC setting.
            nat66: Enable/disable DNAT66.
            nat64: Enable/disable DNAT64.
            add_nat64_route: Enable/disable adding NAT64 route.
            empty_cert_action: Action for an empty client certificate.
            user_agent_detect: Enable/disable detecting device type by HTTP user-agent if no client certificate is provided.
            client_cert: Enable/disable requesting client certificate.
            realservers: Select the real servers that this server load balancing VIP will distribute traffic to.
                Default format: [{'ip': '192.168.1.10'}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'ip': '192.168.1.10'}] (recommended)
            http_cookie_domain_from_host: Enable/disable use of HTTP cookie domain from host field in HTTP.
            http_cookie_domain: Domain that HTTP cookie persistence should apply to.
            http_cookie_path: Limit HTTP cookie persistence to the specified path.
            http_cookie_generation: Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.
            http_cookie_age: Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.
            http_cookie_share: Control sharing of cookies across virtual servers. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.
            https_cookie_secure: Enable/disable verification that inserted HTTPS cookies are secure.
            http_multiplex: Enable/disable HTTP multiplexing.
            http_ip_header: For HTTP multiplexing, enable to add the original client IP address in the X-Forwarded-For HTTP header.
            http_ip_header_name: For HTTP multiplexing, enter a custom HTTPS header name. The original client IP address is added to this header. If empty, X-Forwarded-For is used.
            outlook_web_access: Enable to add the Front-End-Https header for Microsoft Outlook Web Access.
            weblogic_server: Enable to add an HTTP header to indicate SSL offloading for a WebLogic server.
            websphere_server: Enable to add an HTTP header to indicate SSL offloading for a WebSphere server.
            ssl_mode: Apply SSL offloading between the client and the FortiGate (half) or from the client to the FortiGate and from the FortiGate to the server (full).
            ssl_certificate: Name of the certificate to use for SSL handshake.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ssl_dh_bits: Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.
            ssl_algorithm: Permitted encryption algorithms for SSL sessions according to encryption strength.
            ssl_cipher_suites: SSL/TLS cipher suites acceptable from a client, ordered by priority.
                Default format: [{'cipher': 'TLS-AES-128-GCM-SHA256'}]
                Supported formats:
                  - Single string: "value" → [{'priority': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'priority': 'val1'}, ...]
                  - List of dicts: [{'cipher': 'TLS-AES-128-GCM-SHA256'}] (recommended)
            ssl_server_renegotiation: Enable/disable secure renegotiation to comply with RFC 5746.
            ssl_server_algorithm: Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.
            ssl_server_cipher_suites: SSL/TLS cipher suites to offer to a server, ordered by priority.
                Default format: [{'cipher': 'TLS-AES-128-GCM-SHA256'}]
                Supported formats:
                  - Single string: "value" → [{'priority': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'priority': 'val1'}, ...]
                  - List of dicts: [{'cipher': 'TLS-AES-128-GCM-SHA256'}] (recommended)
            ssl_pfs: Select the cipher suites that can be used for SSL perfect forward secrecy (PFS). Applies to both client and server sessions.
            ssl_min_version: Lowest SSL/TLS version acceptable from a client.
            ssl_max_version: Highest SSL/TLS version acceptable from a client.
            ssl_server_min_version: Lowest SSL/TLS version acceptable from a server. Use the client setting by default.
            ssl_server_max_version: Highest SSL/TLS version acceptable from a server. Use the client setting by default.
            ssl_accept_ffdhe_groups: Enable/disable FFDHE cipher suite for SSL key exchange.
            ssl_send_empty_frags: Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3.0 & TLS 1.0 only). May need to be disabled for compatibility with older systems.
            ssl_client_fallback: Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507).
            ssl_client_renegotiation: Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746.
            ssl_client_session_state_type: How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate.
            ssl_client_session_state_timeout: Number of minutes to keep client to FortiGate SSL session state.
            ssl_client_session_state_max: Maximum number of client to FortiGate SSL session states to keep.
            ssl_client_rekey_count: Maximum length of data in MB before triggering a client rekey (0 = disable).
            ssl_server_session_state_type: How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate.
            ssl_server_session_state_timeout: Number of minutes to keep FortiGate to Server SSL session state.
            ssl_server_session_state_max: Maximum number of FortiGate to Server SSL session states to keep.
            ssl_http_location_conversion: Enable to replace HTTP with HTTPS in the reply's Location HTTP header field.
            ssl_http_match_host: Enable/disable HTTP host matching for location conversion.
            ssl_hpkp: Enable/disable including HPKP header in response.
            ssl_hpkp_primary: Certificate to generate primary HPKP pin from.
            ssl_hpkp_backup: Certificate to generate backup HPKP pin from.
            ssl_hpkp_age: Number of minutes the web browser should keep HPKP.
            ssl_hpkp_report_uri: URL to report HPKP violations to.
            ssl_hpkp_include_subdomains: Indicate that HPKP header applies to all subdomains.
            ssl_hsts: Enable/disable including HSTS header in response.
            ssl_hsts_age: Number of seconds the client should honor the HSTS setting.
            ssl_hsts_include_subdomains: Indicate that HSTS header applies to all subdomains.
            monitor: Name of the health check monitor to use when polling to determine a virtual server's connectivity status.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            max_embryonic_connections: Maximum number of incomplete connections.
            embedded_ipv4_address: Enable/disable use of the lower 32 bits of the external IPv6 address as mapped IPv4 address.
            ipv4_mappedip: Range of mapped IP addresses. Specify the start IP address followed by a space and the end IP address.
            ipv4_mappedport: IPv4 port number range on the destination network to which the external port number range is mapped.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_vip6.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_vip6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if src_filter is not None:
            src_filter = normalize_table_field(
                src_filter,
                mkey="range",
                required_fields=['range'],
                field_name="src_filter",
                example="[{'range': 'value'}]",
            )
        if realservers is not None:
            realservers = normalize_table_field(
                realservers,
                mkey="id",
                required_fields=['ip'],
                field_name="realservers",
                example="[{'ip': '192.168.1.10'}]",
            )
        if ssl_certificate is not None:
            ssl_certificate = normalize_table_field(
                ssl_certificate,
                mkey="name",
                required_fields=['name'],
                field_name="ssl_certificate",
                example="[{'name': 'value'}]",
            )
        if ssl_cipher_suites is not None:
            ssl_cipher_suites = normalize_table_field(
                ssl_cipher_suites,
                mkey="priority",
                required_fields=['cipher'],
                field_name="ssl_cipher_suites",
                example="[{'cipher': 'TLS-AES-128-GCM-SHA256'}]",
            )
        if ssl_server_cipher_suites is not None:
            ssl_server_cipher_suites = normalize_table_field(
                ssl_server_cipher_suites,
                mkey="priority",
                required_fields=['cipher'],
                field_name="ssl_server_cipher_suites",
                example="[{'cipher': 'TLS-AES-128-GCM-SHA256'}]",
            )
        if monitor is not None:
            monitor = normalize_table_field(
                monitor,
                mkey="name",
                required_fields=['name'],
                field_name="monitor",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            id=id,
            uuid=uuid,
            comment=comment,
            type=type,
            src_filter=src_filter,
            src_vip_filter=src_vip_filter,
            extip=extip,
            mappedip=mappedip,
            nat_source_vip=nat_source_vip,
            ndp_reply=ndp_reply,
            portforward=portforward,
            protocol=protocol,
            extport=extport,
            mappedport=mappedport,
            color=color,
            ldb_method=ldb_method,
            server_type=server_type,
            http_redirect=http_redirect,
            persistence=persistence,
            h2_support=h2_support,
            h3_support=h3_support,
            quic=quic,
            nat66=nat66,
            nat64=nat64,
            add_nat64_route=add_nat64_route,
            empty_cert_action=empty_cert_action,
            user_agent_detect=user_agent_detect,
            client_cert=client_cert,
            realservers=realservers,
            http_cookie_domain_from_host=http_cookie_domain_from_host,
            http_cookie_domain=http_cookie_domain,
            http_cookie_path=http_cookie_path,
            http_cookie_generation=http_cookie_generation,
            http_cookie_age=http_cookie_age,
            http_cookie_share=http_cookie_share,
            https_cookie_secure=https_cookie_secure,
            http_multiplex=http_multiplex,
            http_ip_header=http_ip_header,
            http_ip_header_name=http_ip_header_name,
            outlook_web_access=outlook_web_access,
            weblogic_server=weblogic_server,
            websphere_server=websphere_server,
            ssl_mode=ssl_mode,
            ssl_certificate=ssl_certificate,
            ssl_dh_bits=ssl_dh_bits,
            ssl_algorithm=ssl_algorithm,
            ssl_cipher_suites=ssl_cipher_suites,
            ssl_server_renegotiation=ssl_server_renegotiation,
            ssl_server_algorithm=ssl_server_algorithm,
            ssl_server_cipher_suites=ssl_server_cipher_suites,
            ssl_pfs=ssl_pfs,
            ssl_min_version=ssl_min_version,
            ssl_max_version=ssl_max_version,
            ssl_server_min_version=ssl_server_min_version,
            ssl_server_max_version=ssl_server_max_version,
            ssl_accept_ffdhe_groups=ssl_accept_ffdhe_groups,
            ssl_send_empty_frags=ssl_send_empty_frags,
            ssl_client_fallback=ssl_client_fallback,
            ssl_client_renegotiation=ssl_client_renegotiation,
            ssl_client_session_state_type=ssl_client_session_state_type,
            ssl_client_session_state_timeout=ssl_client_session_state_timeout,
            ssl_client_session_state_max=ssl_client_session_state_max,
            ssl_client_rekey_count=ssl_client_rekey_count,
            ssl_server_session_state_type=ssl_server_session_state_type,
            ssl_server_session_state_timeout=ssl_server_session_state_timeout,
            ssl_server_session_state_max=ssl_server_session_state_max,
            ssl_http_location_conversion=ssl_http_location_conversion,
            ssl_http_match_host=ssl_http_match_host,
            ssl_hpkp=ssl_hpkp,
            ssl_hpkp_primary=ssl_hpkp_primary,
            ssl_hpkp_backup=ssl_hpkp_backup,
            ssl_hpkp_age=ssl_hpkp_age,
            ssl_hpkp_report_uri=ssl_hpkp_report_uri,
            ssl_hpkp_include_subdomains=ssl_hpkp_include_subdomains,
            ssl_hsts=ssl_hsts,
            ssl_hsts_age=ssl_hsts_age,
            ssl_hsts_include_subdomains=ssl_hsts_include_subdomains,
            monitor=monitor,
            max_embryonic_connections=max_embryonic_connections,
            embedded_ipv4_address=embedded_ipv4_address,
            ipv4_mappedip=ipv4_mappedip,
            ipv4_mappedport=ipv4_mappedport,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.vip6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/vip6",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/firewall/vip6/" + str(name_value)

        # Add explicit query parameters for PUT
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_before is not None:
            params["before"] = q_before
        if q_after is not None:
            params["after"] = q_after
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )

    # ========================================================================
    # POST Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        comment: str | None = None,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = None,
        src_filter: str | list[str] | list[dict[str, Any]] | None = None,
        src_vip_filter: Literal["disable", "enable"] | None = None,
        extip: str | None = None,
        mappedip: str | None = None,
        nat_source_vip: Literal["disable", "enable"] | None = None,
        ndp_reply: Literal["disable", "enable"] | None = None,
        portforward: Literal["disable", "enable"] | None = None,
        protocol: Literal["tcp", "udp", "sctp"] | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        color: int | None = None,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = None,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = None,
        http_redirect: Literal["enable", "disable"] | None = None,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = None,
        h2_support: Literal["enable", "disable"] | None = None,
        h3_support: Literal["enable", "disable"] | None = None,
        quic: str | None = None,
        nat66: Literal["disable", "enable"] | None = None,
        nat64: Literal["disable", "enable"] | None = None,
        add_nat64_route: Literal["disable", "enable"] | None = None,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = None,
        user_agent_detect: Literal["disable", "enable"] | None = None,
        client_cert: Literal["disable", "enable"] | None = None,
        realservers: str | list[str] | list[dict[str, Any]] | None = None,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: Literal["disable", "same-ip"] | None = None,
        https_cookie_secure: Literal["disable", "enable"] | None = None,
        http_multiplex: Literal["enable", "disable"] | None = None,
        http_ip_header: Literal["enable", "disable"] | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: Literal["disable", "enable"] | None = None,
        weblogic_server: Literal["disable", "enable"] | None = None,
        websphere_server: Literal["disable", "enable"] | None = None,
        ssl_mode: Literal["half", "full"] | None = None,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = None,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = None,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = None,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = None,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_pfs: Literal["require", "deny", "allow"] | None = None,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = None,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = None,
        ssl_client_fallback: Literal["disable", "enable"] | None = None,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = None,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = None,
        ssl_http_match_host: Literal["enable", "disable"] | None = None,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = None,
        ssl_hsts: Literal["disable", "enable"] | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = None,
        monitor: str | list[str] | list[dict[str, Any]] | None = None,
        max_embryonic_connections: int | None = None,
        embedded_ipv4_address: Literal["disable", "enable"] | None = None,
        ipv4_mappedip: str | None = None,
        ipv4_mappedport: str | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new firewall/vip6 object.

        Configure virtual IP for IPv6.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Virtual ip6 name.
            id: Custom defined ID.
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            comment: Comment.
            type: Configure a static NAT server load balance VIP or access proxy.
            src_filter: Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses with spaces.
                Default format: [{'range': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'range': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'range': 'val1'}, ...]
                  - List of dicts: [{'range': 'value'}] (recommended)
            src_vip_filter: Enable/disable use of 'src-filter' to match destinations for the reverse SNAT rule.
            extip: IPv6 address or address range on the external interface that you want to map to an address or address range on the destination network.
            mappedip: Mapped IPv6 address range in the format startIP-endIP.
            nat_source_vip: Enable to perform SNAT on traffic from mappedip to the extip for all egress interfaces.
            ndp_reply: Enable/disable this FortiGate unit's ability to respond to NDP requests for this virtual IP address (default = enable).
            portforward: Enable port forwarding.
            protocol: Protocol to use when forwarding packets.
            extport: Incoming port number range that you want to map to a port number range on the destination network.
            mappedport: Port number range on the destination network to which the external port number range is mapped.
            color: Color of icon on the GUI.
            ldb_method: Method used to distribute sessions to real servers.
            server_type: Protocol to be load balanced by the virtual server (also called the server load balance virtual IP).
            http_redirect: Enable/disable redirection of HTTP to HTTPS.
            persistence: Configure how to make sure that clients connect to the same server every time they make a request that is part of the same session.
            h2_support: Enable/disable HTTP2 support (default = enable).
            h3_support: Enable/disable HTTP3/QUIC support (default = disable).
            quic: QUIC setting.
            nat66: Enable/disable DNAT66.
            nat64: Enable/disable DNAT64.
            add_nat64_route: Enable/disable adding NAT64 route.
            empty_cert_action: Action for an empty client certificate.
            user_agent_detect: Enable/disable detecting device type by HTTP user-agent if no client certificate is provided.
            client_cert: Enable/disable requesting client certificate.
            realservers: Select the real servers that this server load balancing VIP will distribute traffic to.
                Default format: [{'ip': '192.168.1.10'}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'ip': '192.168.1.10'}] (recommended)
            http_cookie_domain_from_host: Enable/disable use of HTTP cookie domain from host field in HTTP.
            http_cookie_domain: Domain that HTTP cookie persistence should apply to.
            http_cookie_path: Limit HTTP cookie persistence to the specified path.
            http_cookie_generation: Generation of HTTP cookie to be accepted. Changing invalidates all existing cookies.
            http_cookie_age: Time in minutes that client web browsers should keep a cookie. Default is 60 minutes. 0 = no time limit.
            http_cookie_share: Control sharing of cookies across virtual servers. Use of same-ip means a cookie from one virtual server can be used by another. Disable stops cookie sharing.
            https_cookie_secure: Enable/disable verification that inserted HTTPS cookies are secure.
            http_multiplex: Enable/disable HTTP multiplexing.
            http_ip_header: For HTTP multiplexing, enable to add the original client IP address in the X-Forwarded-For HTTP header.
            http_ip_header_name: For HTTP multiplexing, enter a custom HTTPS header name. The original client IP address is added to this header. If empty, X-Forwarded-For is used.
            outlook_web_access: Enable to add the Front-End-Https header for Microsoft Outlook Web Access.
            weblogic_server: Enable to add an HTTP header to indicate SSL offloading for a WebLogic server.
            websphere_server: Enable to add an HTTP header to indicate SSL offloading for a WebSphere server.
            ssl_mode: Apply SSL offloading between the client and the FortiGate (half) or from the client to the FortiGate and from the FortiGate to the server (full).
            ssl_certificate: Name of the certificate to use for SSL handshake.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ssl_dh_bits: Number of bits to use in the Diffie-Hellman exchange for RSA encryption of SSL sessions.
            ssl_algorithm: Permitted encryption algorithms for SSL sessions according to encryption strength.
            ssl_cipher_suites: SSL/TLS cipher suites acceptable from a client, ordered by priority.
                Default format: [{'cipher': 'TLS-AES-128-GCM-SHA256'}]
                Supported formats:
                  - Single string: "value" → [{'priority': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'priority': 'val1'}, ...]
                  - List of dicts: [{'cipher': 'TLS-AES-128-GCM-SHA256'}] (recommended)
            ssl_server_renegotiation: Enable/disable secure renegotiation to comply with RFC 5746.
            ssl_server_algorithm: Permitted encryption algorithms for the server side of SSL full mode sessions according to encryption strength.
            ssl_server_cipher_suites: SSL/TLS cipher suites to offer to a server, ordered by priority.
                Default format: [{'cipher': 'TLS-AES-128-GCM-SHA256'}]
                Supported formats:
                  - Single string: "value" → [{'priority': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'priority': 'val1'}, ...]
                  - List of dicts: [{'cipher': 'TLS-AES-128-GCM-SHA256'}] (recommended)
            ssl_pfs: Select the cipher suites that can be used for SSL perfect forward secrecy (PFS). Applies to both client and server sessions.
            ssl_min_version: Lowest SSL/TLS version acceptable from a client.
            ssl_max_version: Highest SSL/TLS version acceptable from a client.
            ssl_server_min_version: Lowest SSL/TLS version acceptable from a server. Use the client setting by default.
            ssl_server_max_version: Highest SSL/TLS version acceptable from a server. Use the client setting by default.
            ssl_accept_ffdhe_groups: Enable/disable FFDHE cipher suite for SSL key exchange.
            ssl_send_empty_frags: Enable/disable sending empty fragments to avoid CBC IV attacks (SSL 3.0 & TLS 1.0 only). May need to be disabled for compatibility with older systems.
            ssl_client_fallback: Enable/disable support for preventing Downgrade Attacks on client connections (RFC 7507).
            ssl_client_renegotiation: Allow, deny, or require secure renegotiation of client sessions to comply with RFC 5746.
            ssl_client_session_state_type: How to expire SSL sessions for the segment of the SSL connection between the client and the FortiGate.
            ssl_client_session_state_timeout: Number of minutes to keep client to FortiGate SSL session state.
            ssl_client_session_state_max: Maximum number of client to FortiGate SSL session states to keep.
            ssl_client_rekey_count: Maximum length of data in MB before triggering a client rekey (0 = disable).
            ssl_server_session_state_type: How to expire SSL sessions for the segment of the SSL connection between the server and the FortiGate.
            ssl_server_session_state_timeout: Number of minutes to keep FortiGate to Server SSL session state.
            ssl_server_session_state_max: Maximum number of FortiGate to Server SSL session states to keep.
            ssl_http_location_conversion: Enable to replace HTTP with HTTPS in the reply's Location HTTP header field.
            ssl_http_match_host: Enable/disable HTTP host matching for location conversion.
            ssl_hpkp: Enable/disable including HPKP header in response.
            ssl_hpkp_primary: Certificate to generate primary HPKP pin from.
            ssl_hpkp_backup: Certificate to generate backup HPKP pin from.
            ssl_hpkp_age: Number of minutes the web browser should keep HPKP.
            ssl_hpkp_report_uri: URL to report HPKP violations to.
            ssl_hpkp_include_subdomains: Indicate that HPKP header applies to all subdomains.
            ssl_hsts: Enable/disable including HSTS header in response.
            ssl_hsts_age: Number of seconds the client should honor the HSTS setting.
            ssl_hsts_include_subdomains: Indicate that HSTS header applies to all subdomains.
            monitor: Name of the health check monitor to use when polling to determine a virtual server's connectivity status.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            max_embryonic_connections: Maximum number of incomplete connections.
            embedded_ipv4_address: Enable/disable use of the lower 32 bits of the external IPv6 address as mapped IPv4 address.
            ipv4_mappedip: Range of mapped IP addresses. Specify the start IP address followed by a space and the end IP address.
            ipv4_mappedport: IPv4 port number range on the destination network to which the external port number range is mapped.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_vip6.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Vip6.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_vip6.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Vip6.required_fields()) }}
            
            Use Vip6.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if src_filter is not None:
            src_filter = normalize_table_field(
                src_filter,
                mkey="range",
                required_fields=['range'],
                field_name="src_filter",
                example="[{'range': 'value'}]",
            )
        if realservers is not None:
            realservers = normalize_table_field(
                realservers,
                mkey="id",
                required_fields=['ip'],
                field_name="realservers",
                example="[{'ip': '192.168.1.10'}]",
            )
        if ssl_certificate is not None:
            ssl_certificate = normalize_table_field(
                ssl_certificate,
                mkey="name",
                required_fields=['name'],
                field_name="ssl_certificate",
                example="[{'name': 'value'}]",
            )
        if ssl_cipher_suites is not None:
            ssl_cipher_suites = normalize_table_field(
                ssl_cipher_suites,
                mkey="priority",
                required_fields=['cipher'],
                field_name="ssl_cipher_suites",
                example="[{'cipher': 'TLS-AES-128-GCM-SHA256'}]",
            )
        if ssl_server_cipher_suites is not None:
            ssl_server_cipher_suites = normalize_table_field(
                ssl_server_cipher_suites,
                mkey="priority",
                required_fields=['cipher'],
                field_name="ssl_server_cipher_suites",
                example="[{'cipher': 'TLS-AES-128-GCM-SHA256'}]",
            )
        if monitor is not None:
            monitor = normalize_table_field(
                monitor,
                mkey="name",
                required_fields=['name'],
                field_name="monitor",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            id=id,
            uuid=uuid,
            comment=comment,
            type=type,
            src_filter=src_filter,
            src_vip_filter=src_vip_filter,
            extip=extip,
            mappedip=mappedip,
            nat_source_vip=nat_source_vip,
            ndp_reply=ndp_reply,
            portforward=portforward,
            protocol=protocol,
            extport=extport,
            mappedport=mappedport,
            color=color,
            ldb_method=ldb_method,
            server_type=server_type,
            http_redirect=http_redirect,
            persistence=persistence,
            h2_support=h2_support,
            h3_support=h3_support,
            quic=quic,
            nat66=nat66,
            nat64=nat64,
            add_nat64_route=add_nat64_route,
            empty_cert_action=empty_cert_action,
            user_agent_detect=user_agent_detect,
            client_cert=client_cert,
            realservers=realservers,
            http_cookie_domain_from_host=http_cookie_domain_from_host,
            http_cookie_domain=http_cookie_domain,
            http_cookie_path=http_cookie_path,
            http_cookie_generation=http_cookie_generation,
            http_cookie_age=http_cookie_age,
            http_cookie_share=http_cookie_share,
            https_cookie_secure=https_cookie_secure,
            http_multiplex=http_multiplex,
            http_ip_header=http_ip_header,
            http_ip_header_name=http_ip_header_name,
            outlook_web_access=outlook_web_access,
            weblogic_server=weblogic_server,
            websphere_server=websphere_server,
            ssl_mode=ssl_mode,
            ssl_certificate=ssl_certificate,
            ssl_dh_bits=ssl_dh_bits,
            ssl_algorithm=ssl_algorithm,
            ssl_cipher_suites=ssl_cipher_suites,
            ssl_server_renegotiation=ssl_server_renegotiation,
            ssl_server_algorithm=ssl_server_algorithm,
            ssl_server_cipher_suites=ssl_server_cipher_suites,
            ssl_pfs=ssl_pfs,
            ssl_min_version=ssl_min_version,
            ssl_max_version=ssl_max_version,
            ssl_server_min_version=ssl_server_min_version,
            ssl_server_max_version=ssl_server_max_version,
            ssl_accept_ffdhe_groups=ssl_accept_ffdhe_groups,
            ssl_send_empty_frags=ssl_send_empty_frags,
            ssl_client_fallback=ssl_client_fallback,
            ssl_client_renegotiation=ssl_client_renegotiation,
            ssl_client_session_state_type=ssl_client_session_state_type,
            ssl_client_session_state_timeout=ssl_client_session_state_timeout,
            ssl_client_session_state_max=ssl_client_session_state_max,
            ssl_client_rekey_count=ssl_client_rekey_count,
            ssl_server_session_state_type=ssl_server_session_state_type,
            ssl_server_session_state_timeout=ssl_server_session_state_timeout,
            ssl_server_session_state_max=ssl_server_session_state_max,
            ssl_http_location_conversion=ssl_http_location_conversion,
            ssl_http_match_host=ssl_http_match_host,
            ssl_hpkp=ssl_hpkp,
            ssl_hpkp_primary=ssl_hpkp_primary,
            ssl_hpkp_backup=ssl_hpkp_backup,
            ssl_hpkp_age=ssl_hpkp_age,
            ssl_hpkp_report_uri=ssl_hpkp_report_uri,
            ssl_hpkp_include_subdomains=ssl_hpkp_include_subdomains,
            ssl_hsts=ssl_hsts,
            ssl_hsts_age=ssl_hsts_age,
            ssl_hsts_include_subdomains=ssl_hsts_include_subdomains,
            monitor=monitor,
            max_embryonic_connections=max_embryonic_connections,
            embedded_ipv4_address=embedded_ipv4_address,
            ipv4_mappedip=ipv4_mappedip,
            ipv4_mappedport=ipv4_mappedport,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.vip6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/vip6",
            )

        endpoint = "/firewall/vip6"
        
        # Add explicit query parameters for POST
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_nkey is not None:
            params["nkey"] = q_nkey
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )

    # ========================================================================
    # DELETE Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def delete(
        self,
        name: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete firewall/vip6 object.

        Configure virtual IP for IPv6.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_vip6.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/firewall/vip6/" + str(name)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/vip6 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_vip6.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_vip6.exists(name=1):
            ...     fgt.api.cmdb.firewall_vip6.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        comment: str | None = None,
        type: Literal["static-nat", "server-load-balance", "access-proxy"] | None = None,
        src_filter: str | list[str] | list[dict[str, Any]] | None = None,
        src_vip_filter: Literal["disable", "enable"] | None = None,
        extip: str | None = None,
        mappedip: str | None = None,
        nat_source_vip: Literal["disable", "enable"] | None = None,
        ndp_reply: Literal["disable", "enable"] | None = None,
        portforward: Literal["disable", "enable"] | None = None,
        protocol: Literal["tcp", "udp", "sctp"] | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        color: int | None = None,
        ldb_method: Literal["static", "round-robin", "weighted", "least-session", "least-rtt", "first-alive", "http-host"] | None = None,
        server_type: Literal["http", "https", "imaps", "pop3s", "smtps", "ssl", "tcp", "udp", "ip"] | None = None,
        http_redirect: Literal["enable", "disable"] | None = None,
        persistence: Literal["none", "http-cookie", "ssl-session-id"] | None = None,
        h2_support: Literal["enable", "disable"] | None = None,
        h3_support: Literal["enable", "disable"] | None = None,
        quic: str | None = None,
        nat66: Literal["disable", "enable"] | None = None,
        nat64: Literal["disable", "enable"] | None = None,
        add_nat64_route: Literal["disable", "enable"] | None = None,
        empty_cert_action: Literal["accept", "block", "accept-unmanageable"] | None = None,
        user_agent_detect: Literal["disable", "enable"] | None = None,
        client_cert: Literal["disable", "enable"] | None = None,
        realservers: str | list[str] | list[dict[str, Any]] | None = None,
        http_cookie_domain_from_host: Literal["disable", "enable"] | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: Literal["disable", "same-ip"] | None = None,
        https_cookie_secure: Literal["disable", "enable"] | None = None,
        http_multiplex: Literal["enable", "disable"] | None = None,
        http_ip_header: Literal["enable", "disable"] | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: Literal["disable", "enable"] | None = None,
        weblogic_server: Literal["disable", "enable"] | None = None,
        websphere_server: Literal["disable", "enable"] | None = None,
        ssl_mode: Literal["half", "full"] | None = None,
        ssl_certificate: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_dh_bits: Literal["768", "1024", "1536", "2048", "3072", "4096"] | None = None,
        ssl_algorithm: Literal["high", "medium", "low", "custom"] | None = None,
        ssl_cipher_suites: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_server_renegotiation: Literal["enable", "disable"] | None = None,
        ssl_server_algorithm: Literal["high", "medium", "low", "custom", "client"] | None = None,
        ssl_server_cipher_suites: str | list[str] | list[dict[str, Any]] | None = None,
        ssl_pfs: Literal["require", "deny", "allow"] | None = None,
        ssl_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3"] | None = None,
        ssl_server_min_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_server_max_version: Literal["ssl-3.0", "tls-1.0", "tls-1.1", "tls-1.2", "tls-1.3", "client"] | None = None,
        ssl_accept_ffdhe_groups: Literal["enable", "disable"] | None = None,
        ssl_send_empty_frags: Literal["enable", "disable"] | None = None,
        ssl_client_fallback: Literal["disable", "enable"] | None = None,
        ssl_client_renegotiation: Literal["allow", "deny", "secure"] | None = None,
        ssl_client_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_session_state_type: Literal["disable", "time", "count", "both"] | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: Literal["enable", "disable"] | None = None,
        ssl_http_match_host: Literal["enable", "disable"] | None = None,
        ssl_hpkp: Literal["disable", "enable", "report-only"] | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: Literal["disable", "enable"] | None = None,
        ssl_hsts: Literal["disable", "enable"] | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: Literal["disable", "enable"] | None = None,
        monitor: str | list[str] | list[dict[str, Any]] | None = None,
        max_embryonic_connections: int | None = None,
        embedded_ipv4_address: Literal["disable", "enable"] | None = None,
        ipv4_mappedip: str | None = None,
        ipv4_mappedport: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update firewall/vip6 object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            id: Field id
            uuid: Field uuid
            comment: Field comment
            type: Field type
            src_filter: Field src-filter
            src_vip_filter: Field src-vip-filter
            extip: Field extip
            mappedip: Field mappedip
            nat_source_vip: Field nat-source-vip
            ndp_reply: Field ndp-reply
            portforward: Field portforward
            protocol: Field protocol
            extport: Field extport
            mappedport: Field mappedport
            color: Field color
            ldb_method: Field ldb-method
            server_type: Field server-type
            http_redirect: Field http-redirect
            persistence: Field persistence
            h2_support: Field h2-support
            h3_support: Field h3-support
            quic: Field quic
            nat66: Field nat66
            nat64: Field nat64
            add_nat64_route: Field add-nat64-route
            empty_cert_action: Field empty-cert-action
            user_agent_detect: Field user-agent-detect
            client_cert: Field client-cert
            realservers: Field realservers
            http_cookie_domain_from_host: Field http-cookie-domain-from-host
            http_cookie_domain: Field http-cookie-domain
            http_cookie_path: Field http-cookie-path
            http_cookie_generation: Field http-cookie-generation
            http_cookie_age: Field http-cookie-age
            http_cookie_share: Field http-cookie-share
            https_cookie_secure: Field https-cookie-secure
            http_multiplex: Field http-multiplex
            http_ip_header: Field http-ip-header
            http_ip_header_name: Field http-ip-header-name
            outlook_web_access: Field outlook-web-access
            weblogic_server: Field weblogic-server
            websphere_server: Field websphere-server
            ssl_mode: Field ssl-mode
            ssl_certificate: Field ssl-certificate
            ssl_dh_bits: Field ssl-dh-bits
            ssl_algorithm: Field ssl-algorithm
            ssl_cipher_suites: Field ssl-cipher-suites
            ssl_server_renegotiation: Field ssl-server-renegotiation
            ssl_server_algorithm: Field ssl-server-algorithm
            ssl_server_cipher_suites: Field ssl-server-cipher-suites
            ssl_pfs: Field ssl-pfs
            ssl_min_version: Field ssl-min-version
            ssl_max_version: Field ssl-max-version
            ssl_server_min_version: Field ssl-server-min-version
            ssl_server_max_version: Field ssl-server-max-version
            ssl_accept_ffdhe_groups: Field ssl-accept-ffdhe-groups
            ssl_send_empty_frags: Field ssl-send-empty-frags
            ssl_client_fallback: Field ssl-client-fallback
            ssl_client_renegotiation: Field ssl-client-renegotiation
            ssl_client_session_state_type: Field ssl-client-session-state-type
            ssl_client_session_state_timeout: Field ssl-client-session-state-timeout
            ssl_client_session_state_max: Field ssl-client-session-state-max
            ssl_client_rekey_count: Field ssl-client-rekey-count
            ssl_server_session_state_type: Field ssl-server-session-state-type
            ssl_server_session_state_timeout: Field ssl-server-session-state-timeout
            ssl_server_session_state_max: Field ssl-server-session-state-max
            ssl_http_location_conversion: Field ssl-http-location-conversion
            ssl_http_match_host: Field ssl-http-match-host
            ssl_hpkp: Field ssl-hpkp
            ssl_hpkp_primary: Field ssl-hpkp-primary
            ssl_hpkp_backup: Field ssl-hpkp-backup
            ssl_hpkp_age: Field ssl-hpkp-age
            ssl_hpkp_report_uri: Field ssl-hpkp-report-uri
            ssl_hpkp_include_subdomains: Field ssl-hpkp-include-subdomains
            ssl_hsts: Field ssl-hsts
            ssl_hsts_age: Field ssl-hsts-age
            ssl_hsts_include_subdomains: Field ssl-hsts-include-subdomains
            monitor: Field monitor
            max_embryonic_connections: Field max-embryonic-connections
            embedded_ipv4_address: Field embedded-ipv4-address
            ipv4_mappedip: Field ipv4-mappedip
            ipv4_mappedport: Field ipv4-mappedport
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.firewall_vip6.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_vip6.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_vip6.set(payload_dict=obj_data)
            >>> # Safely applies configuration regardless of current state

        Note:
            This method internally calls exists() then either post() or put().
            For performance-critical code with known state, call post() or put() directly.

        See Also:
            - post(): Create new object
            - put(): Update existing object
            - exists(): Check existence manually
        """
        # Build payload using helper function with auto-normalization
        payload_data = build_api_payload(
            name=name,
            id=id,
            uuid=uuid,
            comment=comment,
            type=type,
            src_filter=src_filter,
            src_vip_filter=src_vip_filter,
            extip=extip,
            mappedip=mappedip,
            nat_source_vip=nat_source_vip,
            ndp_reply=ndp_reply,
            portforward=portforward,
            protocol=protocol,
            extport=extport,
            mappedport=mappedport,
            color=color,
            ldb_method=ldb_method,
            server_type=server_type,
            http_redirect=http_redirect,
            persistence=persistence,
            h2_support=h2_support,
            h3_support=h3_support,
            quic=quic,
            nat66=nat66,
            nat64=nat64,
            add_nat64_route=add_nat64_route,
            empty_cert_action=empty_cert_action,
            user_agent_detect=user_agent_detect,
            client_cert=client_cert,
            realservers=realservers,
            http_cookie_domain_from_host=http_cookie_domain_from_host,
            http_cookie_domain=http_cookie_domain,
            http_cookie_path=http_cookie_path,
            http_cookie_generation=http_cookie_generation,
            http_cookie_age=http_cookie_age,
            http_cookie_share=http_cookie_share,
            https_cookie_secure=https_cookie_secure,
            http_multiplex=http_multiplex,
            http_ip_header=http_ip_header,
            http_ip_header_name=http_ip_header_name,
            outlook_web_access=outlook_web_access,
            weblogic_server=weblogic_server,
            websphere_server=websphere_server,
            ssl_mode=ssl_mode,
            ssl_certificate=ssl_certificate,
            ssl_dh_bits=ssl_dh_bits,
            ssl_algorithm=ssl_algorithm,
            ssl_cipher_suites=ssl_cipher_suites,
            ssl_server_renegotiation=ssl_server_renegotiation,
            ssl_server_algorithm=ssl_server_algorithm,
            ssl_server_cipher_suites=ssl_server_cipher_suites,
            ssl_pfs=ssl_pfs,
            ssl_min_version=ssl_min_version,
            ssl_max_version=ssl_max_version,
            ssl_server_min_version=ssl_server_min_version,
            ssl_server_max_version=ssl_server_max_version,
            ssl_accept_ffdhe_groups=ssl_accept_ffdhe_groups,
            ssl_send_empty_frags=ssl_send_empty_frags,
            ssl_client_fallback=ssl_client_fallback,
            ssl_client_renegotiation=ssl_client_renegotiation,
            ssl_client_session_state_type=ssl_client_session_state_type,
            ssl_client_session_state_timeout=ssl_client_session_state_timeout,
            ssl_client_session_state_max=ssl_client_session_state_max,
            ssl_client_rekey_count=ssl_client_rekey_count,
            ssl_server_session_state_type=ssl_server_session_state_type,
            ssl_server_session_state_timeout=ssl_server_session_state_timeout,
            ssl_server_session_state_max=ssl_server_session_state_max,
            ssl_http_location_conversion=ssl_http_location_conversion,
            ssl_http_match_host=ssl_http_match_host,
            ssl_hpkp=ssl_hpkp,
            ssl_hpkp_primary=ssl_hpkp_primary,
            ssl_hpkp_backup=ssl_hpkp_backup,
            ssl_hpkp_age=ssl_hpkp_age,
            ssl_hpkp_report_uri=ssl_hpkp_report_uri,
            ssl_hpkp_include_subdomains=ssl_hpkp_include_subdomains,
            ssl_hsts=ssl_hsts,
            ssl_hsts_age=ssl_hsts_age,
            ssl_hsts_include_subdomains=ssl_hsts_include_subdomains,
            monitor=monitor,
            max_embryonic_connections=max_embryonic_connections,
            embedded_ipv4_address=embedded_ipv4_address,
            ipv4_mappedip=ipv4_mappedip,
            ipv4_mappedport=ipv4_mappedport,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("name")
        if not mkey_value:
            raise ValueError("name is required for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_data, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_data, vdom=vdom, **kwargs)

    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move firewall/vip6 object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_name: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.firewall_vip6.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/vip6",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone firewall/vip6 object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Identifier of object to clone
            new_name: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.firewall_vip6.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/vip6",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if firewall/vip6 object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.firewall_vip6.exists(name=1):
            ...     fgt.api.cmdb.firewall_vip6.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

