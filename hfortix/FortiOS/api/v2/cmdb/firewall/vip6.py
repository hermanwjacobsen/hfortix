"""
FortiOS CMDB - Cmdb Firewall Vip6

Configuration endpoint for managing cmdb firewall vip6 objects.

API Endpoints:
    GET    /cmdb/firewall/vip6
    POST   /cmdb/firewall/vip6
    GET    /cmdb/firewall/vip6
    PUT    /cmdb/firewall/vip6/{identifier}
    DELETE /cmdb/firewall/vip6/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.vip6.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.vip6.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.vip6.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.vip6.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.vip6.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Vip6:
    """
    Vip6 Operations.

    Provides CRUD operations for FortiOS vip6 configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Vip6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if name:
            endpoint = f"/firewall/vip6/{name}"
        else:
            endpoint = "/firewall/vip6"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        comment: str | None = None,
        type: str | None = None,
        src_filter: list | None = None,
        src_vip_filter: str | None = None,
        extip: str | None = None,
        mappedip: str | None = None,
        nat_source_vip: str | None = None,
        ndp_reply: str | None = None,
        portforward: str | None = None,
        protocol: str | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        color: int | None = None,
        ldb_method: str | None = None,
        server_type: str | None = None,
        http_redirect: str | None = None,
        persistence: str | None = None,
        h2_support: str | None = None,
        h3_support: str | None = None,
        quic: list | None = None,
        nat66: str | None = None,
        nat64: str | None = None,
        add_nat64_route: str | None = None,
        empty_cert_action: str | None = None,
        user_agent_detect: str | None = None,
        client_cert: str | None = None,
        realservers: list | None = None,
        http_cookie_domain_from_host: str | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: str | None = None,
        https_cookie_secure: str | None = None,
        http_multiplex: str | None = None,
        http_ip_header: str | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: str | None = None,
        weblogic_server: str | None = None,
        websphere_server: str | None = None,
        ssl_mode: str | None = None,
        ssl_certificate: list | None = None,
        ssl_dh_bits: str | None = None,
        ssl_algorithm: str | None = None,
        ssl_cipher_suites: list | None = None,
        ssl_server_renegotiation: str | None = None,
        ssl_server_algorithm: str | None = None,
        ssl_server_cipher_suites: list | None = None,
        ssl_pfs: str | None = None,
        ssl_min_version: str | None = None,
        ssl_max_version: str | None = None,
        ssl_server_min_version: str | None = None,
        ssl_server_max_version: str | None = None,
        ssl_accept_ffdhe_groups: str | None = None,
        ssl_send_empty_frags: str | None = None,
        ssl_client_fallback: str | None = None,
        ssl_client_renegotiation: str | None = None,
        ssl_client_session_state_type: str | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_session_state_type: str | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: str | None = None,
        ssl_http_match_host: str | None = None,
        ssl_hpkp: str | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: str | None = None,
        ssl_hsts: str | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: str | None = None,
        monitor: list | None = None,
        max_embryonic_connections: int | None = None,
        embedded_ipv4_address: str | None = None,
        ipv4_mappedip: str | None = None,
        ipv4_mappedport: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: Virtual ip6 name. (optional)
            id: Custom defined ID. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            comment: Comment. (optional)
            type: Configure a static NAT server load balance VIP or access
            proxy. (optional)
            src_filter: Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate
            addresses with spaces. (optional)
            src_vip_filter: Enable/disable use of 'src-filter' to match
            destinations for the reverse SNAT rule. (optional)
            extip: IPv6 address or address range on the external interface that
            you want to map to an address or address range on the destination
            network. (optional)
            mappedip: Mapped IPv6 address range in the format startIP-endIP.
            (optional)
            nat_source_vip: Enable to perform SNAT on traffic from mappedip to
            the extip for all egress interfaces. (optional)
            ndp_reply: Enable/disable this FortiGate unit's ability to respond
            to NDP requests for this virtual IP address (default = enable).
            (optional)
            portforward: Enable port forwarding. (optional)
            protocol: Protocol to use when forwarding packets. (optional)
            extport: Incoming port number range that you want to map to a port
            number range on the destination network. (optional)
            mappedport: Port number range on the destination network to which
            the external port number range is mapped. (optional)
            color: Color of icon on the GUI. (optional)
            ldb_method: Method used to distribute sessions to real servers.
            (optional)
            server_type: Protocol to be load balanced by the virtual server
            (also called the server load balance virtual IP). (optional)
            http_redirect: Enable/disable redirection of HTTP to HTTPS.
            (optional)
            persistence: Configure how to make sure that clients connect to the
            same server every time they make a request that is part of the same
            session. (optional)
            h2_support: Enable/disable HTTP2 support (default = enable).
            (optional)
            h3_support: Enable/disable HTTP3/QUIC support (default = disable).
            (optional)
            quic: QUIC setting. (optional)
            nat66: Enable/disable DNAT66. (optional)
            nat64: Enable/disable DNAT64. (optional)
            add_nat64_route: Enable/disable adding NAT64 route. (optional)
            empty_cert_action: Action for an empty client certificate.
            (optional)
            user_agent_detect: Enable/disable detecting device type by HTTP
            user-agent if no client certificate is provided. (optional)
            client_cert: Enable/disable requesting client certificate.
            (optional)
            realservers: Select the real servers that this server load
            balancing VIP will distribute traffic to. (optional)
            http_cookie_domain_from_host: Enable/disable use of HTTP cookie
            domain from host field in HTTP. (optional)
            http_cookie_domain: Domain that HTTP cookie persistence should
            apply to. (optional)
            http_cookie_path: Limit HTTP cookie persistence to the specified
            path. (optional)
            http_cookie_generation: Generation of HTTP cookie to be accepted.
            Changing invalidates all existing cookies. (optional)
            http_cookie_age: Time in minutes that client web browsers should
            keep a cookie. Default is 60 minutes. 0 = no time limit. (optional)
            http_cookie_share: Control sharing of cookies across virtual
            servers. Use of same-ip means a cookie from one virtual server can
            be used by another. Disable stops cookie sharing. (optional)
            https_cookie_secure: Enable/disable verification that inserted
            HTTPS cookies are secure. (optional)
            http_multiplex: Enable/disable HTTP multiplexing. (optional)
            http_ip_header: For HTTP multiplexing, enable to add the original
            client IP address in the X-Forwarded-For HTTP header. (optional)
            http_ip_header_name: For HTTP multiplexing, enter a custom HTTPS
            header name. The original client IP address is added to this
            header. If empty, X-Forwarded-For is used. (optional)
            outlook_web_access: Enable to add the Front-End-Https header for
            Microsoft Outlook Web Access. (optional)
            weblogic_server: Enable to add an HTTP header to indicate SSL
            offloading for a WebLogic server. (optional)
            websphere_server: Enable to add an HTTP header to indicate SSL
            offloading for a WebSphere server. (optional)
            ssl_mode: Apply SSL offloading between the client and the FortiGate
            (half) or from the client to the FortiGate and from the FortiGate
            to the server (full). (optional)
            ssl_certificate: Name of the certificate to use for SSL handshake.
            (optional)
            ssl_dh_bits: Number of bits to use in the Diffie-Hellman exchange
            for RSA encryption of SSL sessions. (optional)
            ssl_algorithm: Permitted encryption algorithms for SSL sessions
            according to encryption strength. (optional)
            ssl_cipher_suites: SSL/TLS cipher suites acceptable from a client,
            ordered by priority. (optional)
            ssl_server_renegotiation: Enable/disable secure renegotiation to
            comply with RFC 5746. (optional)
            ssl_server_algorithm: Permitted encryption algorithms for the
            server side of SSL full mode sessions according to encryption
            strength. (optional)
            ssl_server_cipher_suites: SSL/TLS cipher suites to offer to a
            server, ordered by priority. (optional)
            ssl_pfs: Select the cipher suites that can be used for SSL perfect
            forward secrecy (PFS). Applies to both client and server sessions.
            (optional)
            ssl_min_version: Lowest SSL/TLS version acceptable from a client.
            (optional)
            ssl_max_version: Highest SSL/TLS version acceptable from a client.
            (optional)
            ssl_server_min_version: Lowest SSL/TLS version acceptable from a
            server. Use the client setting by default. (optional)
            ssl_server_max_version: Highest SSL/TLS version acceptable from a
            server. Use the client setting by default. (optional)
            ssl_accept_ffdhe_groups: Enable/disable FFDHE cipher suite for SSL
            key exchange. (optional)
            ssl_send_empty_frags: Enable/disable sending empty fragments to
            avoid CBC IV attacks (SSL 3.0 & TLS 1.0 only). May need to be
            disabled for compatibility with older systems. (optional)
            ssl_client_fallback: Enable/disable support for preventing
            Downgrade Attacks on client connections (RFC 7507). (optional)
            ssl_client_renegotiation: Allow, deny, or require secure
            renegotiation of client sessions to comply with RFC 5746.
            (optional)
            ssl_client_session_state_type: How to expire SSL sessions for the
            segment of the SSL connection between the client and the FortiGate.
            (optional)
            ssl_client_session_state_timeout: Number of minutes to keep client
            to FortiGate SSL session state. (optional)
            ssl_client_session_state_max: Maximum number of client to FortiGate
            SSL session states to keep. (optional)
            ssl_client_rekey_count: Maximum length of data in MB before
            triggering a client rekey (0 = disable). (optional)
            ssl_server_session_state_type: How to expire SSL sessions for the
            segment of the SSL connection between the server and the FortiGate.
            (optional)
            ssl_server_session_state_timeout: Number of minutes to keep
            FortiGate to Server SSL session state. (optional)
            ssl_server_session_state_max: Maximum number of FortiGate to Server
            SSL session states to keep. (optional)
            ssl_http_location_conversion: Enable to replace HTTP with HTTPS in
            the reply's Location HTTP header field. (optional)
            ssl_http_match_host: Enable/disable HTTP host matching for location
            conversion. (optional)
            ssl_hpkp: Enable/disable including HPKP header in response.
            (optional)
            ssl_hpkp_primary: Certificate to generate primary HPKP pin from.
            (optional)
            ssl_hpkp_backup: Certificate to generate backup HPKP pin from.
            (optional)
            ssl_hpkp_age: Number of minutes the web browser should keep HPKP.
            (optional)
            ssl_hpkp_report_uri: URL to report HPKP violations to. (optional)
            ssl_hpkp_include_subdomains: Indicate that HPKP header applies to
            all subdomains. (optional)
            ssl_hsts: Enable/disable including HSTS header in response.
            (optional)
            ssl_hsts_age: Number of seconds the client should honor the HSTS
            setting. (optional)
            ssl_hsts_include_subdomains: Indicate that HSTS header applies to
            all subdomains. (optional)
            monitor: Name of the health check monitor to use when polling to
            determine a virtual server's connectivity status. (optional)
            max_embryonic_connections: Maximum number of incomplete
            connections. (optional)
            embedded_ipv4_address: Enable/disable use of the lower 32 bits of
            the external IPv6 address as mapped IPv4 address. (optional)
            ipv4_mappedip: Range of mapped IP addresses. Specify the start IP
            address followed by a space and the end IP address. (optional)
            ipv4_mappedport: IPv4 port number range on the destination network
            to which the external port number range is mapped. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/firewall/vip6/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if id is not None:
            data_payload["id"] = id
        if uuid is not None:
            data_payload["uuid"] = uuid
        if comment is not None:
            data_payload["comment"] = comment
        if type is not None:
            data_payload["type"] = type
        if src_filter is not None:
            data_payload["src-filter"] = src_filter
        if src_vip_filter is not None:
            data_payload["src-vip-filter"] = src_vip_filter
        if extip is not None:
            data_payload["extip"] = extip
        if mappedip is not None:
            data_payload["mappedip"] = mappedip
        if nat_source_vip is not None:
            data_payload["nat-source-vip"] = nat_source_vip
        if ndp_reply is not None:
            data_payload["ndp-reply"] = ndp_reply
        if portforward is not None:
            data_payload["portforward"] = portforward
        if protocol is not None:
            data_payload["protocol"] = protocol
        if extport is not None:
            data_payload["extport"] = extport
        if mappedport is not None:
            data_payload["mappedport"] = mappedport
        if color is not None:
            data_payload["color"] = color
        if ldb_method is not None:
            data_payload["ldb-method"] = ldb_method
        if server_type is not None:
            data_payload["server-type"] = server_type
        if http_redirect is not None:
            data_payload["http-redirect"] = http_redirect
        if persistence is not None:
            data_payload["persistence"] = persistence
        if h2_support is not None:
            data_payload["h2-support"] = h2_support
        if h3_support is not None:
            data_payload["h3-support"] = h3_support
        if quic is not None:
            data_payload["quic"] = quic
        if nat66 is not None:
            data_payload["nat66"] = nat66
        if nat64 is not None:
            data_payload["nat64"] = nat64
        if add_nat64_route is not None:
            data_payload["add-nat64-route"] = add_nat64_route
        if empty_cert_action is not None:
            data_payload["empty-cert-action"] = empty_cert_action
        if user_agent_detect is not None:
            data_payload["user-agent-detect"] = user_agent_detect
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if realservers is not None:
            data_payload["realservers"] = realservers
        if http_cookie_domain_from_host is not None:
            data_payload["http-cookie-domain-from-host"] = (
                http_cookie_domain_from_host
            )
        if http_cookie_domain is not None:
            data_payload["http-cookie-domain"] = http_cookie_domain
        if http_cookie_path is not None:
            data_payload["http-cookie-path"] = http_cookie_path
        if http_cookie_generation is not None:
            data_payload["http-cookie-generation"] = http_cookie_generation
        if http_cookie_age is not None:
            data_payload["http-cookie-age"] = http_cookie_age
        if http_cookie_share is not None:
            data_payload["http-cookie-share"] = http_cookie_share
        if https_cookie_secure is not None:
            data_payload["https-cookie-secure"] = https_cookie_secure
        if http_multiplex is not None:
            data_payload["http-multiplex"] = http_multiplex
        if http_ip_header is not None:
            data_payload["http-ip-header"] = http_ip_header
        if http_ip_header_name is not None:
            data_payload["http-ip-header-name"] = http_ip_header_name
        if outlook_web_access is not None:
            data_payload["outlook-web-access"] = outlook_web_access
        if weblogic_server is not None:
            data_payload["weblogic-server"] = weblogic_server
        if websphere_server is not None:
            data_payload["websphere-server"] = websphere_server
        if ssl_mode is not None:
            data_payload["ssl-mode"] = ssl_mode
        if ssl_certificate is not None:
            data_payload["ssl-certificate"] = ssl_certificate
        if ssl_dh_bits is not None:
            data_payload["ssl-dh-bits"] = ssl_dh_bits
        if ssl_algorithm is not None:
            data_payload["ssl-algorithm"] = ssl_algorithm
        if ssl_cipher_suites is not None:
            data_payload["ssl-cipher-suites"] = ssl_cipher_suites
        if ssl_server_renegotiation is not None:
            data_payload["ssl-server-renegotiation"] = ssl_server_renegotiation
        if ssl_server_algorithm is not None:
            data_payload["ssl-server-algorithm"] = ssl_server_algorithm
        if ssl_server_cipher_suites is not None:
            data_payload["ssl-server-cipher-suites"] = ssl_server_cipher_suites
        if ssl_pfs is not None:
            data_payload["ssl-pfs"] = ssl_pfs
        if ssl_min_version is not None:
            data_payload["ssl-min-version"] = ssl_min_version
        if ssl_max_version is not None:
            data_payload["ssl-max-version"] = ssl_max_version
        if ssl_server_min_version is not None:
            data_payload["ssl-server-min-version"] = ssl_server_min_version
        if ssl_server_max_version is not None:
            data_payload["ssl-server-max-version"] = ssl_server_max_version
        if ssl_accept_ffdhe_groups is not None:
            data_payload["ssl-accept-ffdhe-groups"] = ssl_accept_ffdhe_groups
        if ssl_send_empty_frags is not None:
            data_payload["ssl-send-empty-frags"] = ssl_send_empty_frags
        if ssl_client_fallback is not None:
            data_payload["ssl-client-fallback"] = ssl_client_fallback
        if ssl_client_renegotiation is not None:
            data_payload["ssl-client-renegotiation"] = ssl_client_renegotiation
        if ssl_client_session_state_type is not None:
            data_payload["ssl-client-session-state-type"] = (
                ssl_client_session_state_type
            )
        if ssl_client_session_state_timeout is not None:
            data_payload["ssl-client-session-state-timeout"] = (
                ssl_client_session_state_timeout
            )
        if ssl_client_session_state_max is not None:
            data_payload["ssl-client-session-state-max"] = (
                ssl_client_session_state_max
            )
        if ssl_client_rekey_count is not None:
            data_payload["ssl-client-rekey-count"] = ssl_client_rekey_count
        if ssl_server_session_state_type is not None:
            data_payload["ssl-server-session-state-type"] = (
                ssl_server_session_state_type
            )
        if ssl_server_session_state_timeout is not None:
            data_payload["ssl-server-session-state-timeout"] = (
                ssl_server_session_state_timeout
            )
        if ssl_server_session_state_max is not None:
            data_payload["ssl-server-session-state-max"] = (
                ssl_server_session_state_max
            )
        if ssl_http_location_conversion is not None:
            data_payload["ssl-http-location-conversion"] = (
                ssl_http_location_conversion
            )
        if ssl_http_match_host is not None:
            data_payload["ssl-http-match-host"] = ssl_http_match_host
        if ssl_hpkp is not None:
            data_payload["ssl-hpkp"] = ssl_hpkp
        if ssl_hpkp_primary is not None:
            data_payload["ssl-hpkp-primary"] = ssl_hpkp_primary
        if ssl_hpkp_backup is not None:
            data_payload["ssl-hpkp-backup"] = ssl_hpkp_backup
        if ssl_hpkp_age is not None:
            data_payload["ssl-hpkp-age"] = ssl_hpkp_age
        if ssl_hpkp_report_uri is not None:
            data_payload["ssl-hpkp-report-uri"] = ssl_hpkp_report_uri
        if ssl_hpkp_include_subdomains is not None:
            data_payload["ssl-hpkp-include-subdomains"] = (
                ssl_hpkp_include_subdomains
            )
        if ssl_hsts is not None:
            data_payload["ssl-hsts"] = ssl_hsts
        if ssl_hsts_age is not None:
            data_payload["ssl-hsts-age"] = ssl_hsts_age
        if ssl_hsts_include_subdomains is not None:
            data_payload["ssl-hsts-include-subdomains"] = (
                ssl_hsts_include_subdomains
            )
        if monitor is not None:
            data_payload["monitor"] = monitor
        if max_embryonic_connections is not None:
            data_payload["max-embryonic-connections"] = (
                max_embryonic_connections
            )
        if embedded_ipv4_address is not None:
            data_payload["embedded-ipv4-address"] = embedded_ipv4_address
        if ipv4_mappedip is not None:
            data_payload["ipv4-mappedip"] = ipv4_mappedip
        if ipv4_mappedport is not None:
            data_payload["ipv4-mappedport"] = ipv4_mappedport
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/firewall/vip6/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            True if object exists, False otherwise

        Example:
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect

        from hfortix.FortiOS.exceptions_forti import ResourceNotFoundError

        # Call get() - returns dict (sync) or coroutine (async)
        result = self.get(name=name, vdom=vdom)

        # Check if async mode
        if inspect.iscoroutine(result):

            async def _async():
                try:
                    # Runtime check confirms result is a coroutine, cast for
                    # mypy
                    await cast(Coroutine[Any, Any, dict[str, Any]], result)
                    return True
                except ResourceNotFoundError:
                    return False

            # Type ignore justified: mypy can't verify Union return type
            # narrowing

            return _async()
        # Sync mode - get() already executed, no exception means it exists
        return True

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        id: int | None = None,
        uuid: str | None = None,
        comment: str | None = None,
        type: str | None = None,
        src_filter: list | None = None,
        src_vip_filter: str | None = None,
        extip: str | None = None,
        mappedip: str | None = None,
        nat_source_vip: str | None = None,
        ndp_reply: str | None = None,
        portforward: str | None = None,
        protocol: str | None = None,
        extport: str | None = None,
        mappedport: str | None = None,
        color: int | None = None,
        ldb_method: str | None = None,
        server_type: str | None = None,
        http_redirect: str | None = None,
        persistence: str | None = None,
        h2_support: str | None = None,
        h3_support: str | None = None,
        quic: list | None = None,
        nat66: str | None = None,
        nat64: str | None = None,
        add_nat64_route: str | None = None,
        empty_cert_action: str | None = None,
        user_agent_detect: str | None = None,
        client_cert: str | None = None,
        realservers: list | None = None,
        http_cookie_domain_from_host: str | None = None,
        http_cookie_domain: str | None = None,
        http_cookie_path: str | None = None,
        http_cookie_generation: int | None = None,
        http_cookie_age: int | None = None,
        http_cookie_share: str | None = None,
        https_cookie_secure: str | None = None,
        http_multiplex: str | None = None,
        http_ip_header: str | None = None,
        http_ip_header_name: str | None = None,
        outlook_web_access: str | None = None,
        weblogic_server: str | None = None,
        websphere_server: str | None = None,
        ssl_mode: str | None = None,
        ssl_certificate: list | None = None,
        ssl_dh_bits: str | None = None,
        ssl_algorithm: str | None = None,
        ssl_cipher_suites: list | None = None,
        ssl_server_renegotiation: str | None = None,
        ssl_server_algorithm: str | None = None,
        ssl_server_cipher_suites: list | None = None,
        ssl_pfs: str | None = None,
        ssl_min_version: str | None = None,
        ssl_max_version: str | None = None,
        ssl_server_min_version: str | None = None,
        ssl_server_max_version: str | None = None,
        ssl_accept_ffdhe_groups: str | None = None,
        ssl_send_empty_frags: str | None = None,
        ssl_client_fallback: str | None = None,
        ssl_client_renegotiation: str | None = None,
        ssl_client_session_state_type: str | None = None,
        ssl_client_session_state_timeout: int | None = None,
        ssl_client_session_state_max: int | None = None,
        ssl_client_rekey_count: int | None = None,
        ssl_server_session_state_type: str | None = None,
        ssl_server_session_state_timeout: int | None = None,
        ssl_server_session_state_max: int | None = None,
        ssl_http_location_conversion: str | None = None,
        ssl_http_match_host: str | None = None,
        ssl_hpkp: str | None = None,
        ssl_hpkp_primary: str | None = None,
        ssl_hpkp_backup: str | None = None,
        ssl_hpkp_age: int | None = None,
        ssl_hpkp_report_uri: str | None = None,
        ssl_hpkp_include_subdomains: str | None = None,
        ssl_hsts: str | None = None,
        ssl_hsts_age: int | None = None,
        ssl_hsts_include_subdomains: str | None = None,
        monitor: list | None = None,
        max_embryonic_connections: int | None = None,
        embedded_ipv4_address: str | None = None,
        ipv4_mappedip: str | None = None,
        ipv4_mappedport: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: Virtual ip6 name. (optional)
            id: Custom defined ID. (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            comment: Comment. (optional)
            type: Configure a static NAT server load balance VIP or access
            proxy. (optional)
            src_filter: Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate
            addresses with spaces. (optional)
            src_vip_filter: Enable/disable use of 'src-filter' to match
            destinations for the reverse SNAT rule. (optional)
            extip: IPv6 address or address range on the external interface that
            you want to map to an address or address range on the destination
            network. (optional)
            mappedip: Mapped IPv6 address range in the format startIP-endIP.
            (optional)
            nat_source_vip: Enable to perform SNAT on traffic from mappedip to
            the extip for all egress interfaces. (optional)
            ndp_reply: Enable/disable this FortiGate unit's ability to respond
            to NDP requests for this virtual IP address (default = enable).
            (optional)
            portforward: Enable port forwarding. (optional)
            protocol: Protocol to use when forwarding packets. (optional)
            extport: Incoming port number range that you want to map to a port
            number range on the destination network. (optional)
            mappedport: Port number range on the destination network to which
            the external port number range is mapped. (optional)
            color: Color of icon on the GUI. (optional)
            ldb_method: Method used to distribute sessions to real servers.
            (optional)
            server_type: Protocol to be load balanced by the virtual server
            (also called the server load balance virtual IP). (optional)
            http_redirect: Enable/disable redirection of HTTP to HTTPS.
            (optional)
            persistence: Configure how to make sure that clients connect to the
            same server every time they make a request that is part of the same
            session. (optional)
            h2_support: Enable/disable HTTP2 support (default = enable).
            (optional)
            h3_support: Enable/disable HTTP3/QUIC support (default = disable).
            (optional)
            quic: QUIC setting. (optional)
            nat66: Enable/disable DNAT66. (optional)
            nat64: Enable/disable DNAT64. (optional)
            add_nat64_route: Enable/disable adding NAT64 route. (optional)
            empty_cert_action: Action for an empty client certificate.
            (optional)
            user_agent_detect: Enable/disable detecting device type by HTTP
            user-agent if no client certificate is provided. (optional)
            client_cert: Enable/disable requesting client certificate.
            (optional)
            realservers: Select the real servers that this server load
            balancing VIP will distribute traffic to. (optional)
            http_cookie_domain_from_host: Enable/disable use of HTTP cookie
            domain from host field in HTTP. (optional)
            http_cookie_domain: Domain that HTTP cookie persistence should
            apply to. (optional)
            http_cookie_path: Limit HTTP cookie persistence to the specified
            path. (optional)
            http_cookie_generation: Generation of HTTP cookie to be accepted.
            Changing invalidates all existing cookies. (optional)
            http_cookie_age: Time in minutes that client web browsers should
            keep a cookie. Default is 60 minutes. 0 = no time limit. (optional)
            http_cookie_share: Control sharing of cookies across virtual
            servers. Use of same-ip means a cookie from one virtual server can
            be used by another. Disable stops cookie sharing. (optional)
            https_cookie_secure: Enable/disable verification that inserted
            HTTPS cookies are secure. (optional)
            http_multiplex: Enable/disable HTTP multiplexing. (optional)
            http_ip_header: For HTTP multiplexing, enable to add the original
            client IP address in the X-Forwarded-For HTTP header. (optional)
            http_ip_header_name: For HTTP multiplexing, enter a custom HTTPS
            header name. The original client IP address is added to this
            header. If empty, X-Forwarded-For is used. (optional)
            outlook_web_access: Enable to add the Front-End-Https header for
            Microsoft Outlook Web Access. (optional)
            weblogic_server: Enable to add an HTTP header to indicate SSL
            offloading for a WebLogic server. (optional)
            websphere_server: Enable to add an HTTP header to indicate SSL
            offloading for a WebSphere server. (optional)
            ssl_mode: Apply SSL offloading between the client and the FortiGate
            (half) or from the client to the FortiGate and from the FortiGate
            to the server (full). (optional)
            ssl_certificate: Name of the certificate to use for SSL handshake.
            (optional)
            ssl_dh_bits: Number of bits to use in the Diffie-Hellman exchange
            for RSA encryption of SSL sessions. (optional)
            ssl_algorithm: Permitted encryption algorithms for SSL sessions
            according to encryption strength. (optional)
            ssl_cipher_suites: SSL/TLS cipher suites acceptable from a client,
            ordered by priority. (optional)
            ssl_server_renegotiation: Enable/disable secure renegotiation to
            comply with RFC 5746. (optional)
            ssl_server_algorithm: Permitted encryption algorithms for the
            server side of SSL full mode sessions according to encryption
            strength. (optional)
            ssl_server_cipher_suites: SSL/TLS cipher suites to offer to a
            server, ordered by priority. (optional)
            ssl_pfs: Select the cipher suites that can be used for SSL perfect
            forward secrecy (PFS). Applies to both client and server sessions.
            (optional)
            ssl_min_version: Lowest SSL/TLS version acceptable from a client.
            (optional)
            ssl_max_version: Highest SSL/TLS version acceptable from a client.
            (optional)
            ssl_server_min_version: Lowest SSL/TLS version acceptable from a
            server. Use the client setting by default. (optional)
            ssl_server_max_version: Highest SSL/TLS version acceptable from a
            server. Use the client setting by default. (optional)
            ssl_accept_ffdhe_groups: Enable/disable FFDHE cipher suite for SSL
            key exchange. (optional)
            ssl_send_empty_frags: Enable/disable sending empty fragments to
            avoid CBC IV attacks (SSL 3.0 & TLS 1.0 only). May need to be
            disabled for compatibility with older systems. (optional)
            ssl_client_fallback: Enable/disable support for preventing
            Downgrade Attacks on client connections (RFC 7507). (optional)
            ssl_client_renegotiation: Allow, deny, or require secure
            renegotiation of client sessions to comply with RFC 5746.
            (optional)
            ssl_client_session_state_type: How to expire SSL sessions for the
            segment of the SSL connection between the client and the FortiGate.
            (optional)
            ssl_client_session_state_timeout: Number of minutes to keep client
            to FortiGate SSL session state. (optional)
            ssl_client_session_state_max: Maximum number of client to FortiGate
            SSL session states to keep. (optional)
            ssl_client_rekey_count: Maximum length of data in MB before
            triggering a client rekey (0 = disable). (optional)
            ssl_server_session_state_type: How to expire SSL sessions for the
            segment of the SSL connection between the server and the FortiGate.
            (optional)
            ssl_server_session_state_timeout: Number of minutes to keep
            FortiGate to Server SSL session state. (optional)
            ssl_server_session_state_max: Maximum number of FortiGate to Server
            SSL session states to keep. (optional)
            ssl_http_location_conversion: Enable to replace HTTP with HTTPS in
            the reply's Location HTTP header field. (optional)
            ssl_http_match_host: Enable/disable HTTP host matching for location
            conversion. (optional)
            ssl_hpkp: Enable/disable including HPKP header in response.
            (optional)
            ssl_hpkp_primary: Certificate to generate primary HPKP pin from.
            (optional)
            ssl_hpkp_backup: Certificate to generate backup HPKP pin from.
            (optional)
            ssl_hpkp_age: Number of minutes the web browser should keep HPKP.
            (optional)
            ssl_hpkp_report_uri: URL to report HPKP violations to. (optional)
            ssl_hpkp_include_subdomains: Indicate that HPKP header applies to
            all subdomains. (optional)
            ssl_hsts: Enable/disable including HSTS header in response.
            (optional)
            ssl_hsts_age: Number of seconds the client should honor the HSTS
            setting. (optional)
            ssl_hsts_include_subdomains: Indicate that HSTS header applies to
            all subdomains. (optional)
            monitor: Name of the health check monitor to use when polling to
            determine a virtual server's connectivity status. (optional)
            max_embryonic_connections: Maximum number of incomplete
            connections. (optional)
            embedded_ipv4_address: Enable/disable use of the lower 32 bits of
            the external IPv6 address as mapped IPv4 address. (optional)
            ipv4_mappedip: Range of mapped IP addresses. Specify the start IP
            address followed by a space and the end IP address. (optional)
            ipv4_mappedport: IPv4 port number range on the destination network
            to which the external port number range is mapped. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/firewall/vip6"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if id is not None:
            data_payload["id"] = id
        if uuid is not None:
            data_payload["uuid"] = uuid
        if comment is not None:
            data_payload["comment"] = comment
        if type is not None:
            data_payload["type"] = type
        if src_filter is not None:
            data_payload["src-filter"] = src_filter
        if src_vip_filter is not None:
            data_payload["src-vip-filter"] = src_vip_filter
        if extip is not None:
            data_payload["extip"] = extip
        if mappedip is not None:
            data_payload["mappedip"] = mappedip
        if nat_source_vip is not None:
            data_payload["nat-source-vip"] = nat_source_vip
        if ndp_reply is not None:
            data_payload["ndp-reply"] = ndp_reply
        if portforward is not None:
            data_payload["portforward"] = portforward
        if protocol is not None:
            data_payload["protocol"] = protocol
        if extport is not None:
            data_payload["extport"] = extport
        if mappedport is not None:
            data_payload["mappedport"] = mappedport
        if color is not None:
            data_payload["color"] = color
        if ldb_method is not None:
            data_payload["ldb-method"] = ldb_method
        if server_type is not None:
            data_payload["server-type"] = server_type
        if http_redirect is not None:
            data_payload["http-redirect"] = http_redirect
        if persistence is not None:
            data_payload["persistence"] = persistence
        if h2_support is not None:
            data_payload["h2-support"] = h2_support
        if h3_support is not None:
            data_payload["h3-support"] = h3_support
        if quic is not None:
            data_payload["quic"] = quic
        if nat66 is not None:
            data_payload["nat66"] = nat66
        if nat64 is not None:
            data_payload["nat64"] = nat64
        if add_nat64_route is not None:
            data_payload["add-nat64-route"] = add_nat64_route
        if empty_cert_action is not None:
            data_payload["empty-cert-action"] = empty_cert_action
        if user_agent_detect is not None:
            data_payload["user-agent-detect"] = user_agent_detect
        if client_cert is not None:
            data_payload["client-cert"] = client_cert
        if realservers is not None:
            data_payload["realservers"] = realservers
        if http_cookie_domain_from_host is not None:
            data_payload["http-cookie-domain-from-host"] = (
                http_cookie_domain_from_host
            )
        if http_cookie_domain is not None:
            data_payload["http-cookie-domain"] = http_cookie_domain
        if http_cookie_path is not None:
            data_payload["http-cookie-path"] = http_cookie_path
        if http_cookie_generation is not None:
            data_payload["http-cookie-generation"] = http_cookie_generation
        if http_cookie_age is not None:
            data_payload["http-cookie-age"] = http_cookie_age
        if http_cookie_share is not None:
            data_payload["http-cookie-share"] = http_cookie_share
        if https_cookie_secure is not None:
            data_payload["https-cookie-secure"] = https_cookie_secure
        if http_multiplex is not None:
            data_payload["http-multiplex"] = http_multiplex
        if http_ip_header is not None:
            data_payload["http-ip-header"] = http_ip_header
        if http_ip_header_name is not None:
            data_payload["http-ip-header-name"] = http_ip_header_name
        if outlook_web_access is not None:
            data_payload["outlook-web-access"] = outlook_web_access
        if weblogic_server is not None:
            data_payload["weblogic-server"] = weblogic_server
        if websphere_server is not None:
            data_payload["websphere-server"] = websphere_server
        if ssl_mode is not None:
            data_payload["ssl-mode"] = ssl_mode
        if ssl_certificate is not None:
            data_payload["ssl-certificate"] = ssl_certificate
        if ssl_dh_bits is not None:
            data_payload["ssl-dh-bits"] = ssl_dh_bits
        if ssl_algorithm is not None:
            data_payload["ssl-algorithm"] = ssl_algorithm
        if ssl_cipher_suites is not None:
            data_payload["ssl-cipher-suites"] = ssl_cipher_suites
        if ssl_server_renegotiation is not None:
            data_payload["ssl-server-renegotiation"] = ssl_server_renegotiation
        if ssl_server_algorithm is not None:
            data_payload["ssl-server-algorithm"] = ssl_server_algorithm
        if ssl_server_cipher_suites is not None:
            data_payload["ssl-server-cipher-suites"] = ssl_server_cipher_suites
        if ssl_pfs is not None:
            data_payload["ssl-pfs"] = ssl_pfs
        if ssl_min_version is not None:
            data_payload["ssl-min-version"] = ssl_min_version
        if ssl_max_version is not None:
            data_payload["ssl-max-version"] = ssl_max_version
        if ssl_server_min_version is not None:
            data_payload["ssl-server-min-version"] = ssl_server_min_version
        if ssl_server_max_version is not None:
            data_payload["ssl-server-max-version"] = ssl_server_max_version
        if ssl_accept_ffdhe_groups is not None:
            data_payload["ssl-accept-ffdhe-groups"] = ssl_accept_ffdhe_groups
        if ssl_send_empty_frags is not None:
            data_payload["ssl-send-empty-frags"] = ssl_send_empty_frags
        if ssl_client_fallback is not None:
            data_payload["ssl-client-fallback"] = ssl_client_fallback
        if ssl_client_renegotiation is not None:
            data_payload["ssl-client-renegotiation"] = ssl_client_renegotiation
        if ssl_client_session_state_type is not None:
            data_payload["ssl-client-session-state-type"] = (
                ssl_client_session_state_type
            )
        if ssl_client_session_state_timeout is not None:
            data_payload["ssl-client-session-state-timeout"] = (
                ssl_client_session_state_timeout
            )
        if ssl_client_session_state_max is not None:
            data_payload["ssl-client-session-state-max"] = (
                ssl_client_session_state_max
            )
        if ssl_client_rekey_count is not None:
            data_payload["ssl-client-rekey-count"] = ssl_client_rekey_count
        if ssl_server_session_state_type is not None:
            data_payload["ssl-server-session-state-type"] = (
                ssl_server_session_state_type
            )
        if ssl_server_session_state_timeout is not None:
            data_payload["ssl-server-session-state-timeout"] = (
                ssl_server_session_state_timeout
            )
        if ssl_server_session_state_max is not None:
            data_payload["ssl-server-session-state-max"] = (
                ssl_server_session_state_max
            )
        if ssl_http_location_conversion is not None:
            data_payload["ssl-http-location-conversion"] = (
                ssl_http_location_conversion
            )
        if ssl_http_match_host is not None:
            data_payload["ssl-http-match-host"] = ssl_http_match_host
        if ssl_hpkp is not None:
            data_payload["ssl-hpkp"] = ssl_hpkp
        if ssl_hpkp_primary is not None:
            data_payload["ssl-hpkp-primary"] = ssl_hpkp_primary
        if ssl_hpkp_backup is not None:
            data_payload["ssl-hpkp-backup"] = ssl_hpkp_backup
        if ssl_hpkp_age is not None:
            data_payload["ssl-hpkp-age"] = ssl_hpkp_age
        if ssl_hpkp_report_uri is not None:
            data_payload["ssl-hpkp-report-uri"] = ssl_hpkp_report_uri
        if ssl_hpkp_include_subdomains is not None:
            data_payload["ssl-hpkp-include-subdomains"] = (
                ssl_hpkp_include_subdomains
            )
        if ssl_hsts is not None:
            data_payload["ssl-hsts"] = ssl_hsts
        if ssl_hsts_age is not None:
            data_payload["ssl-hsts-age"] = ssl_hsts_age
        if ssl_hsts_include_subdomains is not None:
            data_payload["ssl-hsts-include-subdomains"] = (
                ssl_hsts_include_subdomains
            )
        if monitor is not None:
            data_payload["monitor"] = monitor
        if max_embryonic_connections is not None:
            data_payload["max-embryonic-connections"] = (
                max_embryonic_connections
            )
        if embedded_ipv4_address is not None:
            data_payload["embedded-ipv4-address"] = embedded_ipv4_address
        if ipv4_mappedip is not None:
            data_payload["ipv4-mappedip"] = ipv4_mappedip
        if ipv4_mappedport is not None:
            data_payload["ipv4-mappedport"] = ipv4_mappedport
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
