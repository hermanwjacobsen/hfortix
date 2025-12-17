"""
FortiOS vip API wrapper.
Provides access to /api/v2/cmdb/firewall/vip endpoint.
"""

from typing import Any, Dict, List, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component


class Vip:
    """
    Wrapper for firewall vip API endpoint.

    Manages vip configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the Vip wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/vip"


    def get(
        self,
        mkey: Optional[Union[str, int]] = None,
        attr: Optional[Any] = None,
        count: Optional[Any] = None,
        skip_to_datasource: Optional[Any] = None,
        acs: Optional[Any] = None,
        search: Optional[Any] = None,
        scope: Optional[Any] = None,
        datasource: Optional[Any] = None,
        with_meta: Optional[Any] = None,
        skip: Optional[Any] = None,
        format: Optional[Any] = None,
        action: Optional[Any] = None,
        vdom: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a specific vip entry by its name.

        Args:
            mkey: The name (primary key)
            attr: Attribute name that references other table
            count: Maximum number of entries to return.
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address
            acs: If true, returned result are in ascending order.
            search: If present, the objects will be filtered by the search value.
            scope: Scope [global|vdom|both*]
            datasource: Enable to include datasource information for each linked object.
            with_meta: Enable to include meta information about each object (type id, referen
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by | (i.e. pol
            action: datasource: Return all applicable datasource entries for a specific at
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            **kwargs: Additional parameters

        Returns:
            API response dictionary with entry details
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        if attr is not None:
            params["attr"] = attr
        if count is not None:
            params["count"] = count
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        if scope is not None:
            params["scope"] = scope
        if datasource is not None:
            params["datasource"] = datasource
        if with_meta is not None:
            params["with_meta"] = with_meta
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if action is not None:
            params["action"] = action
        if vdom is not None:
            params["vdom"] = vdom

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.get(
            "cmdb", f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        add_nat46_route: Optional[str] = None,
        arp_reply: Optional[str] = None,
        client_cert: Optional[str] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        dns_mapping_ttl: Optional[int] = None,
        empty_cert_action: Optional[str] = None,
        extaddr: Optional[list] = None,
        extintf: Optional[str] = None,
        extip: Optional[str] = None,
        extport: Optional[str] = None,
        gratuitous_arp_interval: Optional[int] = None,
        gslb_domain_name: Optional[str] = None,
        gslb_hostname: Optional[str] = None,
        gslb_public_ips: Optional[list] = None,
        h2_support: Optional[str] = None,
        h3_support: Optional[str] = None,
        http_cookie_age: Optional[int] = None,
        http_cookie_domain: Optional[str] = None,
        http_cookie_domain_from_host: Optional[str] = None,
        http_cookie_generation: Optional[int] = None,
        http_cookie_path: Optional[str] = None,
        http_cookie_share: Optional[str] = None,
        http_ip_header: Optional[str] = None,
        http_ip_header_name: Optional[str] = None,
        http_multiplex: Optional[str] = None,
        http_multiplex_max_concurrent_request: Optional[int] = None,
        http_multiplex_max_request: Optional[int] = None,
        http_multiplex_ttl: Optional[int] = None,
        http_redirect: Optional[str] = None,
        https_cookie_secure: Optional[str] = None,
        id: Optional[int] = None,
        ipv6_mappedip: Optional[str] = None,
        ipv6_mappedport: Optional[str] = None,
        ldb_method: Optional[str] = None,
        mapped_addr: Optional[str] = None,
        mappedip: Optional[list] = None,
        mappedport: Optional[str] = None,
        max_embryonic_connections: Optional[int] = None,
        monitor: Optional[list] = None,
        name: Optional[str] = None,
        nat_source_vip: Optional[str] = None,
        nat44: Optional[str] = None,
        nat46: Optional[str] = None,
        one_click_gslb_server: Optional[str] = None,
        outlook_web_access: Optional[str] = None,
        persistence: Optional[str] = None,
        portforward: Optional[str] = None,
        portmapping_type: Optional[str] = None,
        protocol: Optional[str] = None,
        quic: Optional[list] = None,
        realservers: Optional[list] = None,
        server_type: Optional[str] = None,
        service: Optional[list] = None,
        src_filter: Optional[list] = None,
        src_vip_filter: Optional[str] = None,
        srcintf_filter: Optional[list] = None,
        ssl_accept_ffdhe_groups: Optional[str] = None,
        ssl_algorithm: Optional[str] = None,
        ssl_certificate: Optional[list] = None,
        ssl_cipher_suites: Optional[list] = None,
        ssl_client_fallback: Optional[str] = None,
        ssl_client_rekey_count: Optional[int] = None,
        ssl_client_renegotiation: Optional[str] = None,
        ssl_client_session_state_max: Optional[int] = None,
        ssl_client_session_state_timeout: Optional[int] = None,
        ssl_client_session_state_type: Optional[str] = None,
        ssl_dh_bits: Optional[str] = None,
        ssl_hpkp: Optional[str] = None,
        ssl_hpkp_age: Optional[int] = None,
        ssl_hpkp_backup: Optional[str] = None,
        ssl_hpkp_include_subdomains: Optional[str] = None,
        ssl_hpkp_primary: Optional[str] = None,
        ssl_hpkp_report_uri: Optional[str] = None,
        ssl_hsts: Optional[str] = None,
        ssl_hsts_age: Optional[int] = None,
        ssl_hsts_include_subdomains: Optional[str] = None,
        ssl_http_location_conversion: Optional[str] = None,
        ssl_http_match_host: Optional[str] = None,
        ssl_max_version: Optional[str] = None,
        ssl_min_version: Optional[str] = None,
        ssl_mode: Optional[str] = None,
        ssl_pfs: Optional[str] = None,
        ssl_send_empty_frags: Optional[str] = None,
        ssl_server_algorithm: Optional[str] = None,
        ssl_server_cipher_suites: Optional[list] = None,
        ssl_server_max_version: Optional[str] = None,
        ssl_server_min_version: Optional[str] = None,
        ssl_server_renegotiation: Optional[str] = None,
        ssl_server_session_state_max: Optional[int] = None,
        ssl_server_session_state_timeout: Optional[int] = None,
        ssl_server_session_state_type: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        user_agent_detect: Optional[str] = None,
        uuid: Optional[str] = None,
        weblogic_server: Optional[str] = None,
        websphere_server: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create vip entry.

        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: create(key="value", vdom="root")

        Args:
            payload_dict: The configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            add-nat46-route (string) (enum: ['disable', 'enable']):
                Enable/disable adding NAT46 route.
            arp-reply (string) (enum: ['disable', 'enable']):
                Enable to respond to ARP requests for this virtual IP addres...
            client-cert (string) (enum: ['disable', 'enable']):
                Enable/disable requesting client certificate.
            color (integer) (range: 0-32):
                Color of icon on the GUI.
            comment (string) (max_len: 255):
                Comment.
            dns-mapping-ttl (integer) (range: 0-604800):
                DNS mapping TTL (Set to zero to use TTL in DNS response, def...
            empty-cert-action (string) (enum: ['accept', 'block', 'accept-unmanageable']):
                Action for an empty client certificate.
            extaddr (list[object]):
                External FQDN address name.
            extintf (string) (max_len: 35):
                Interface connected to the source network that receives the ...
            extip (string):
                IP address or address range on the external interface that y...
            extport (string):
                Incoming port number range that you want to map to a port nu...
            gratuitous-arp-interval (integer) (range: 5-8640000):
                Enable to have the VIP send gratuitous ARPs. 0=disabled. Set...
            gslb-domain-name (string) (max_len: 255):
                Domain to use when integrating with FortiGSLB.
            gslb-hostname (string) (max_len: 35):
                Hostname to use within the configured FortiGSLB domain.
            gslb-public-ips (list[object]):
                Publicly accessible IP addresses for the FortiGSLB service.
            h2-support (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP2 support (default = enable).
            h3-support (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP3/QUIC support (default = disable).
            http-cookie-age (integer) (range: 0-525600):
                Time in minutes that client web browsers should keep a cooki...
            http-cookie-domain (string) (max_len: 35):
                Domain that HTTP cookie persistence should apply to.
            http-cookie-domain-from-host (string) (enum: ['disable', 'enable']):
                Enable/disable use of HTTP cookie domain from host field in ...
            http-cookie-generation (integer) (range: 0-4294967295):
                Generation of HTTP cookie to be accepted. Changing invalidat...
            http-cookie-path (string) (max_len: 35):
                Limit HTTP cookie persistence to the specified path.
            http-cookie-share (string) (enum: ['disable', 'same-ip']):
                Control sharing of cookies across virtual servers. Use of sa...
            http-ip-header (string) (enum: ['enable', 'disable']):
                For HTTP multiplexing, enable to add the original client IP ...
            http-ip-header-name (string) (max_len: 35):
                For HTTP multiplexing, enter a custom HTTPS header name. The...
            http-multiplex (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP multiplexing.
            http-multiplex-max-concurrent-request (integer) (range: 0-2147483647):
                Maximum number of concurrent requests that a multiplex serve...
            http-multiplex-max-request (integer) (range: 0-2147483647):
                Maximum number of requests that a multiplex server can handl...
            http-multiplex-ttl (integer) (range: 0-2147483647):
                Time-to-live for idle connections to servers.
            http-redirect (string) (enum: ['enable', 'disable']):
                Enable/disable redirection of HTTP to HTTPS.
            https-cookie-secure (string) (enum: ['disable', 'enable']):
                Enable/disable verification that inserted HTTPS cookies are ...
            id (integer) (range: 0-65535):
                Custom defined ID.
            ipv6-mappedip (string):
                Range of mapped IPv6 addresses. Specify the start IPv6 addre...
            ipv6-mappedport (string):
                IPv6 port number range on the destination network to which t...
            ldb-method (string) (enum: ['static', 'round-robin', 'weighted']):
                Method used to distribute sessions to real servers.
            mapped-addr (string) (max_len: 79):
                Mapped FQDN address name.
            mappedip (list[object]):
                IP address or address range on the destination network to wh...
            mappedport (string):
                Port number range on the destination network to which the ex...
            max-embryonic-connections (integer) (range: 0-100000):
                Maximum number of incomplete connections.
            monitor (list[object]):
                Name of the health check monitor to use when polling to dete...
            name (string) (max_len: 79):
                Virtual IP name.
            nat-source-vip (string) (enum: ['disable', 'enable']):
                Enable/disable forcing the source NAT mapped IP to the exter...
            nat44 (string) (enum: ['disable', 'enable']):
                Enable/disable NAT44.
            nat46 (string) (enum: ['disable', 'enable']):
                Enable/disable NAT46.
            one-click-gslb-server (string) (enum: ['disable', 'enable']):
                Enable/disable one click GSLB server integration with FortiG...
            outlook-web-access (string) (enum: ['disable', 'enable']):
                Enable to add the Front-End-Https header for Microsoft Outlo...
            persistence (string) (enum: ['none', 'http-cookie', 'ssl-session-id']):
                Configure how to make sure that clients connect to the same ...
            portforward (string) (enum: ['disable', 'enable']):
                Enable/disable port forwarding.
            portmapping-type (string) (enum: ['1-to-1', 'm-to-n']):
                Port mapping type.
            protocol (string) (enum: ['tcp', 'udp', 'sctp']):
                Protocol to use when forwarding packets.
            quic (list[object]):
                QUIC setting.
            realservers (list[object]):
                Select the real servers that this server load balancing VIP ...
            server-type (string) (enum: ['http', 'https', 'tcp']):
                Protocol to be load balanced by the virtual server (also cal...
            service (list[object]):
                Service name.
            src-filter (list[object]):
                Source address filter. Each address must be either an IP/sub...
            src-vip-filter (string) (enum: ['disable', 'enable']):
                Enable/disable use of 'src-filter' to match destinations for...
            srcintf-filter (list[object]):
                Interfaces to which the VIP applies. Separate the names with...
            ssl-accept-ffdhe-groups (string) (enum: ['enable', 'disable']):
                Enable/disable FFDHE cipher suite for SSL key exchange.
            ssl-algorithm (string) (enum: ['high', 'medium', 'low']):
                Permitted encryption algorithms for SSL sessions according t...
            ssl-certificate (list[object]):
                Name of the certificate to use for SSL handshake.
            ssl-cipher-suites (list[object]):
                SSL/TLS cipher suites acceptable from a client, ordered by p...
            ssl-client-fallback (string) (enum: ['disable', 'enable']):
                Enable/disable support for preventing Downgrade Attacks on c...
            ssl-client-rekey-count (integer) (range: 200-1048576):
                Maximum length of data in MB before triggering a client reke...
            ssl-client-renegotiation (string) (enum: ['allow', 'deny', 'secure']):
                Allow, deny, or require secure renegotiation of client sessi...
            ssl-client-session-state-max (integer) (range: 1-10000):
                Maximum number of client to FortiGate SSL session states to ...
            ssl-client-session-state-timeout (integer) (range: 1-14400):
                Number of minutes to keep client to FortiGate SSL session st...
            ssl-client-session-state-type (string) (enum: ['disable', 'time', 'count']):
                How to expire SSL sessions for the segment of the SSL connec...
            ssl-dh-bits (string) (enum: ['768', '1024', '1536']):
                Number of bits to use in the Diffie-Hellman exchange for RSA...
            ssl-hpkp (string) (enum: ['disable', 'enable', 'report-only']):
                Enable/disable including HPKP header in response.
            ssl-hpkp-age (integer) (range: 60-157680000):
                Number of seconds the client should honor the HPKP setting.
            ssl-hpkp-backup (string) (max_len: 79):
                Certificate to generate backup HPKP pin from.
            ssl-hpkp-include-subdomains (string) (enum: ['disable', 'enable']):
                Indicate that HPKP header applies to all subdomains.
            ssl-hpkp-primary (string) (max_len: 79):
                Certificate to generate primary HPKP pin from.
            ssl-hpkp-report-uri (string) (max_len: 255):
                URL to report HPKP violations to.
            ssl-hsts (string) (enum: ['disable', 'enable']):
                Enable/disable including HSTS header in response.
            ssl-hsts-age (integer) (range: 60-157680000):
                Number of seconds the client should honor the HSTS setting.
            ssl-hsts-include-subdomains (string) (enum: ['disable', 'enable']):
                Indicate that HSTS header applies to all subdomains.
            ssl-http-location-conversion (string) (enum: ['enable', 'disable']):
                Enable to replace HTTP with HTTPS in the reply's Location HT...
            ssl-http-match-host (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP host matching for location conversion.
            ssl-max-version (string) (enum: ['ssl-3.0', 'tls-1.0', 'tls-1.1']):
                Highest SSL/TLS version acceptable from a client.
            ssl-min-version (string) (enum: ['ssl-3.0', 'tls-1.0', 'tls-1.1']):
                Lowest SSL/TLS version acceptable from a client.
            ssl-mode (string) (enum: ['half', 'full']):
                Apply SSL offloading between the client and the FortiGate (h...
            ssl-pfs (string) (enum: ['require', 'deny', 'allow']):
                Select the cipher suites that can be used for SSL perfect fo...
            ssl-send-empty-frags (string) (enum: ['enable', 'disable']):
                Enable/disable sending empty fragments to avoid CBC IV attac...
            ssl-server-algorithm (string) (enum: ['high', 'medium', 'low']):
                Permitted encryption algorithms for the server side of SSL f...
            ssl-server-cipher-suites (list[object]):
                SSL/TLS cipher suites to offer to a server, ordered by prior...
            ssl-server-max-version (string) (enum: ['ssl-3.0', 'tls-1.0', 'tls-1.1']):
                Highest SSL/TLS version acceptable from a server. Use the cl...
            ssl-server-min-version (string) (enum: ['ssl-3.0', 'tls-1.0', 'tls-1.1']):
                Lowest SSL/TLS version acceptable from a server. Use the cli...
            ssl-server-renegotiation (string) (enum: ['enable', 'disable']):
                Enable/disable secure renegotiation to comply with RFC 5746.
            ssl-server-session-state-max (integer) (range: 1-10000):
                Maximum number of FortiGate to Server SSL session states to ...
            ssl-server-session-state-timeout (integer) (range: 1-14400):
                Number of minutes to keep FortiGate to Server SSL session st...
            ssl-server-session-state-type (string) (enum: ['disable', 'time', 'count']):
                How to expire SSL sessions for the segment of the SSL connec...
            status (string) (enum: ['disable', 'enable']):
                Enable/disable VIP.
            type (string) (enum: ['static-nat', 'load-balance', 'server-load-balance']):
                Configure a static NAT, load balance, server load balance, a...
            user-agent-detect (string) (enum: ['disable', 'enable']):
                Enable/disable detecting device type by HTTP user-agent if n...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            weblogic-server (string) (enum: ['disable', 'enable']):
                Enable to add an HTTP header to indicate SSL offloading for ...
            websphere-server (string) (enum: ['disable', 'enable']):
                Enable to add an HTTP header to indicate SSL offloading for ...

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if add_nat46_route is not None:
            payload_dict["add-nat46-route"] = add_nat46_route
        if arp_reply is not None:
            payload_dict["arp-reply"] = arp_reply
        if client_cert is not None:
            payload_dict["client-cert"] = client_cert
        if color is not None:
            payload_dict["color"] = color
        if comment is not None:
            payload_dict["comment"] = comment
        if dns_mapping_ttl is not None:
            payload_dict["dns-mapping-ttl"] = dns_mapping_ttl
        if empty_cert_action is not None:
            payload_dict["empty-cert-action"] = empty_cert_action
        if extaddr is not None:
            payload_dict["extaddr"] = extaddr
        if extintf is not None:
            payload_dict["extintf"] = extintf
        if extip is not None:
            payload_dict["extip"] = extip
        if extport is not None:
            payload_dict["extport"] = extport
        if gratuitous_arp_interval is not None:
            payload_dict["gratuitous-arp-interval"] = gratuitous_arp_interval
        if gslb_domain_name is not None:
            payload_dict["gslb-domain-name"] = gslb_domain_name
        if gslb_hostname is not None:
            payload_dict["gslb-hostname"] = gslb_hostname
        if gslb_public_ips is not None:
            payload_dict["gslb-public-ips"] = gslb_public_ips
        if h2_support is not None:
            payload_dict["h2-support"] = h2_support
        if h3_support is not None:
            payload_dict["h3-support"] = h3_support
        if http_cookie_age is not None:
            payload_dict["http-cookie-age"] = http_cookie_age
        if http_cookie_domain is not None:
            payload_dict["http-cookie-domain"] = http_cookie_domain
        if http_cookie_domain_from_host is not None:
            payload_dict["http-cookie-domain-from-host"] = http_cookie_domain_from_host
        if http_cookie_generation is not None:
            payload_dict["http-cookie-generation"] = http_cookie_generation
        if http_cookie_path is not None:
            payload_dict["http-cookie-path"] = http_cookie_path
        if http_cookie_share is not None:
            payload_dict["http-cookie-share"] = http_cookie_share
        if http_ip_header is not None:
            payload_dict["http-ip-header"] = http_ip_header
        if http_ip_header_name is not None:
            payload_dict["http-ip-header-name"] = http_ip_header_name
        if http_multiplex is not None:
            payload_dict["http-multiplex"] = http_multiplex
        if http_multiplex_max_concurrent_request is not None:
            payload_dict["http-multiplex-max-concurrent-request"] = (
                http_multiplex_max_concurrent_request
            )
        if http_multiplex_max_request is not None:
            payload_dict["http-multiplex-max-request"] = http_multiplex_max_request
        if http_multiplex_ttl is not None:
            payload_dict["http-multiplex-ttl"] = http_multiplex_ttl
        if http_redirect is not None:
            payload_dict["http-redirect"] = http_redirect
        if https_cookie_secure is not None:
            payload_dict["https-cookie-secure"] = https_cookie_secure
        if id is not None:
            payload_dict["id"] = id
        if ipv6_mappedip is not None:
            payload_dict["ipv6-mappedip"] = ipv6_mappedip
        if ipv6_mappedport is not None:
            payload_dict["ipv6-mappedport"] = ipv6_mappedport
        if ldb_method is not None:
            payload_dict["ldb-method"] = ldb_method
        if mapped_addr is not None:
            payload_dict["mapped-addr"] = mapped_addr
        if mappedip is not None:
            payload_dict["mappedip"] = mappedip
        if mappedport is not None:
            payload_dict["mappedport"] = mappedport
        if max_embryonic_connections is not None:
            payload_dict["max-embryonic-connections"] = max_embryonic_connections
        if monitor is not None:
            payload_dict["monitor"] = monitor
        if name is not None:
            payload_dict["name"] = name
        if nat_source_vip is not None:
            payload_dict["nat-source-vip"] = nat_source_vip
        if nat44 is not None:
            payload_dict["nat44"] = nat44
        if nat46 is not None:
            payload_dict["nat46"] = nat46
        if one_click_gslb_server is not None:
            payload_dict["one-click-gslb-server"] = one_click_gslb_server
        if outlook_web_access is not None:
            payload_dict["outlook-web-access"] = outlook_web_access
        if persistence is not None:
            payload_dict["persistence"] = persistence
        if portforward is not None:
            payload_dict["portforward"] = portforward
        if portmapping_type is not None:
            payload_dict["portmapping-type"] = portmapping_type
        if protocol is not None:
            payload_dict["protocol"] = protocol
        if quic is not None:
            payload_dict["quic"] = quic
        if realservers is not None:
            payload_dict["realservers"] = realservers
        if server_type is not None:
            payload_dict["server-type"] = server_type
        if service is not None:
            payload_dict["service"] = service
        if src_filter is not None:
            payload_dict["src-filter"] = src_filter
        if src_vip_filter is not None:
            payload_dict["src-vip-filter"] = src_vip_filter
        if srcintf_filter is not None:
            payload_dict["srcintf-filter"] = srcintf_filter
        if ssl_accept_ffdhe_groups is not None:
            payload_dict["ssl-accept-ffdhe-groups"] = ssl_accept_ffdhe_groups
        if ssl_algorithm is not None:
            payload_dict["ssl-algorithm"] = ssl_algorithm
        if ssl_certificate is not None:
            payload_dict["ssl-certificate"] = ssl_certificate
        if ssl_cipher_suites is not None:
            payload_dict["ssl-cipher-suites"] = ssl_cipher_suites
        if ssl_client_fallback is not None:
            payload_dict["ssl-client-fallback"] = ssl_client_fallback
        if ssl_client_rekey_count is not None:
            payload_dict["ssl-client-rekey-count"] = ssl_client_rekey_count
        if ssl_client_renegotiation is not None:
            payload_dict["ssl-client-renegotiation"] = ssl_client_renegotiation
        if ssl_client_session_state_max is not None:
            payload_dict["ssl-client-session-state-max"] = ssl_client_session_state_max
        if ssl_client_session_state_timeout is not None:
            payload_dict["ssl-client-session-state-timeout"] = ssl_client_session_state_timeout
        if ssl_client_session_state_type is not None:
            payload_dict["ssl-client-session-state-type"] = ssl_client_session_state_type
        if ssl_dh_bits is not None:
            payload_dict["ssl-dh-bits"] = ssl_dh_bits
        if ssl_hpkp is not None:
            payload_dict["ssl-hpkp"] = ssl_hpkp
        if ssl_hpkp_age is not None:
            payload_dict["ssl-hpkp-age"] = ssl_hpkp_age
        if ssl_hpkp_backup is not None:
            payload_dict["ssl-hpkp-backup"] = ssl_hpkp_backup
        if ssl_hpkp_include_subdomains is not None:
            payload_dict["ssl-hpkp-include-subdomains"] = ssl_hpkp_include_subdomains
        if ssl_hpkp_primary is not None:
            payload_dict["ssl-hpkp-primary"] = ssl_hpkp_primary
        if ssl_hpkp_report_uri is not None:
            payload_dict["ssl-hpkp-report-uri"] = ssl_hpkp_report_uri
        if ssl_hsts is not None:
            payload_dict["ssl-hsts"] = ssl_hsts
        if ssl_hsts_age is not None:
            payload_dict["ssl-hsts-age"] = ssl_hsts_age
        if ssl_hsts_include_subdomains is not None:
            payload_dict["ssl-hsts-include-subdomains"] = ssl_hsts_include_subdomains
        if ssl_http_location_conversion is not None:
            payload_dict["ssl-http-location-conversion"] = ssl_http_location_conversion
        if ssl_http_match_host is not None:
            payload_dict["ssl-http-match-host"] = ssl_http_match_host
        if ssl_max_version is not None:
            payload_dict["ssl-max-version"] = ssl_max_version
        if ssl_min_version is not None:
            payload_dict["ssl-min-version"] = ssl_min_version
        if ssl_mode is not None:
            payload_dict["ssl-mode"] = ssl_mode
        if ssl_pfs is not None:
            payload_dict["ssl-pfs"] = ssl_pfs
        if ssl_send_empty_frags is not None:
            payload_dict["ssl-send-empty-frags"] = ssl_send_empty_frags
        if ssl_server_algorithm is not None:
            payload_dict["ssl-server-algorithm"] = ssl_server_algorithm
        if ssl_server_cipher_suites is not None:
            payload_dict["ssl-server-cipher-suites"] = ssl_server_cipher_suites
        if ssl_server_max_version is not None:
            payload_dict["ssl-server-max-version"] = ssl_server_max_version
        if ssl_server_min_version is not None:
            payload_dict["ssl-server-min-version"] = ssl_server_min_version
        if ssl_server_renegotiation is not None:
            payload_dict["ssl-server-renegotiation"] = ssl_server_renegotiation
        if ssl_server_session_state_max is not None:
            payload_dict["ssl-server-session-state-max"] = ssl_server_session_state_max
        if ssl_server_session_state_timeout is not None:
            payload_dict["ssl-server-session-state-timeout"] = ssl_server_session_state_timeout
        if ssl_server_session_state_type is not None:
            payload_dict["ssl-server-session-state-type"] = ssl_server_session_state_type
        if status is not None:
            payload_dict["status"] = status
        if type is not None:
            payload_dict["type"] = type
        if user_agent_detect is not None:
            payload_dict["user-agent-detect"] = user_agent_detect
        if uuid is not None:
            payload_dict["uuid"] = uuid
        if weblogic_server is not None:
            payload_dict["weblogic-server"] = weblogic_server
        if websphere_server is not None:
            payload_dict["websphere-server"] = websphere_server

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if action is not None:
            params["action"] = action
        if nkey is not None:
            params["nkey"] = nkey
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.post(
            "cmdb", self.path, data=payload_dict, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        mkey: Optional[Union[str, int]] = None,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        add_nat46_route: Optional[str] = None,
        arp_reply: Optional[str] = None,
        client_cert: Optional[str] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        dns_mapping_ttl: Optional[int] = None,
        empty_cert_action: Optional[str] = None,
        extaddr: Optional[list] = None,
        extintf: Optional[str] = None,
        extip: Optional[str] = None,
        extport: Optional[str] = None,
        gratuitous_arp_interval: Optional[int] = None,
        gslb_domain_name: Optional[str] = None,
        gslb_hostname: Optional[str] = None,
        gslb_public_ips: Optional[list] = None,
        h2_support: Optional[str] = None,
        h3_support: Optional[str] = None,
        http_cookie_age: Optional[int] = None,
        http_cookie_domain: Optional[str] = None,
        http_cookie_domain_from_host: Optional[str] = None,
        http_cookie_generation: Optional[int] = None,
        http_cookie_path: Optional[str] = None,
        http_cookie_share: Optional[str] = None,
        http_ip_header: Optional[str] = None,
        http_ip_header_name: Optional[str] = None,
        http_multiplex: Optional[str] = None,
        http_multiplex_max_concurrent_request: Optional[int] = None,
        http_multiplex_max_request: Optional[int] = None,
        http_multiplex_ttl: Optional[int] = None,
        http_redirect: Optional[str] = None,
        https_cookie_secure: Optional[str] = None,
        id: Optional[int] = None,
        ipv6_mappedip: Optional[str] = None,
        ipv6_mappedport: Optional[str] = None,
        ldb_method: Optional[str] = None,
        mapped_addr: Optional[str] = None,
        mappedip: Optional[list] = None,
        mappedport: Optional[str] = None,
        max_embryonic_connections: Optional[int] = None,
        monitor: Optional[list] = None,
        name: Optional[str] = None,
        nat_source_vip: Optional[str] = None,
        nat44: Optional[str] = None,
        nat46: Optional[str] = None,
        one_click_gslb_server: Optional[str] = None,
        outlook_web_access: Optional[str] = None,
        persistence: Optional[str] = None,
        portforward: Optional[str] = None,
        portmapping_type: Optional[str] = None,
        protocol: Optional[str] = None,
        quic: Optional[list] = None,
        realservers: Optional[list] = None,
        server_type: Optional[str] = None,
        service: Optional[list] = None,
        src_filter: Optional[list] = None,
        src_vip_filter: Optional[str] = None,
        srcintf_filter: Optional[list] = None,
        ssl_accept_ffdhe_groups: Optional[str] = None,
        ssl_algorithm: Optional[str] = None,
        ssl_certificate: Optional[list] = None,
        ssl_cipher_suites: Optional[list] = None,
        ssl_client_fallback: Optional[str] = None,
        ssl_client_rekey_count: Optional[int] = None,
        ssl_client_renegotiation: Optional[str] = None,
        ssl_client_session_state_max: Optional[int] = None,
        ssl_client_session_state_timeout: Optional[int] = None,
        ssl_client_session_state_type: Optional[str] = None,
        ssl_dh_bits: Optional[str] = None,
        ssl_hpkp: Optional[str] = None,
        ssl_hpkp_age: Optional[int] = None,
        ssl_hpkp_backup: Optional[str] = None,
        ssl_hpkp_include_subdomains: Optional[str] = None,
        ssl_hpkp_primary: Optional[str] = None,
        ssl_hpkp_report_uri: Optional[str] = None,
        ssl_hsts: Optional[str] = None,
        ssl_hsts_age: Optional[int] = None,
        ssl_hsts_include_subdomains: Optional[str] = None,
        ssl_http_location_conversion: Optional[str] = None,
        ssl_http_match_host: Optional[str] = None,
        ssl_max_version: Optional[str] = None,
        ssl_min_version: Optional[str] = None,
        ssl_mode: Optional[str] = None,
        ssl_pfs: Optional[str] = None,
        ssl_send_empty_frags: Optional[str] = None,
        ssl_server_algorithm: Optional[str] = None,
        ssl_server_cipher_suites: Optional[list] = None,
        ssl_server_max_version: Optional[str] = None,
        ssl_server_min_version: Optional[str] = None,
        ssl_server_renegotiation: Optional[str] = None,
        ssl_server_session_state_max: Optional[int] = None,
        ssl_server_session_state_timeout: Optional[int] = None,
        ssl_server_session_state_type: Optional[str] = None,
        status: Optional[str] = None,
        type: Optional[str] = None,
        user_agent_detect: Optional[str] = None,
        uuid: Optional[str] = None,
        weblogic_server: Optional[str] = None,
        websphere_server: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update vip entry.

        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, payload_dict={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")

        Args:
            mkey: The name (primary key)
            payload_dict: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            add-nat46-route (string) (enum: ['disable', 'enable']):
                Enable/disable adding NAT46 route.
            arp-reply (string) (enum: ['disable', 'enable']):
                Enable to respond to ARP requests for this virtual IP addres...
            client-cert (string) (enum: ['disable', 'enable']):
                Enable/disable requesting client certificate.
            color (integer) (range: 0-32):
                Color of icon on the GUI.
            comment (string) (max_len: 255):
                Comment.
            dns-mapping-ttl (integer) (range: 0-604800):
                DNS mapping TTL (Set to zero to use TTL in DNS response, def...
            empty-cert-action (string) (enum: ['accept', 'block', 'accept-unmanageable']):
                Action for an empty client certificate.
            extaddr (list[object]):
                External FQDN address name.
            extintf (string) (max_len: 35):
                Interface connected to the source network that receives the ...
            extip (string):
                IP address or address range on the external interface that y...
            extport (string):
                Incoming port number range that you want to map to a port nu...
            gratuitous-arp-interval (integer) (range: 5-8640000):
                Enable to have the VIP send gratuitous ARPs. 0=disabled. Set...
            gslb-domain-name (string) (max_len: 255):
                Domain to use when integrating with FortiGSLB.
            gslb-hostname (string) (max_len: 35):
                Hostname to use within the configured FortiGSLB domain.
            gslb-public-ips (list[object]):
                Publicly accessible IP addresses for the FortiGSLB service.
            h2-support (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP2 support (default = enable).
            h3-support (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP3/QUIC support (default = disable).
            http-cookie-age (integer) (range: 0-525600):
                Time in minutes that client web browsers should keep a cooki...
            http-cookie-domain (string) (max_len: 35):
                Domain that HTTP cookie persistence should apply to.
            http-cookie-domain-from-host (string) (enum: ['disable', 'enable']):
                Enable/disable use of HTTP cookie domain from host field in ...
            http-cookie-generation (integer) (range: 0-4294967295):
                Generation of HTTP cookie to be accepted. Changing invalidat...
            http-cookie-path (string) (max_len: 35):
                Limit HTTP cookie persistence to the specified path.
            http-cookie-share (string) (enum: ['disable', 'same-ip']):
                Control sharing of cookies across virtual servers. Use of sa...
            http-ip-header (string) (enum: ['enable', 'disable']):
                For HTTP multiplexing, enable to add the original client IP ...
            http-ip-header-name (string) (max_len: 35):
                For HTTP multiplexing, enter a custom HTTPS header name. The...
            http-multiplex (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP multiplexing.
            http-multiplex-max-concurrent-request (integer) (range: 0-2147483647):
                Maximum number of concurrent requests that a multiplex serve...
            http-multiplex-max-request (integer) (range: 0-2147483647):
                Maximum number of requests that a multiplex server can handl...
            http-multiplex-ttl (integer) (range: 0-2147483647):
                Time-to-live for idle connections to servers.
            http-redirect (string) (enum: ['enable', 'disable']):
                Enable/disable redirection of HTTP to HTTPS.
            https-cookie-secure (string) (enum: ['disable', 'enable']):
                Enable/disable verification that inserted HTTPS cookies are ...
            id (integer) (range: 0-65535):
                Custom defined ID.
            ipv6-mappedip (string):
                Range of mapped IPv6 addresses. Specify the start IPv6 addre...
            ipv6-mappedport (string):
                IPv6 port number range on the destination network to which t...
            ldb-method (string) (enum: ['static', 'round-robin', 'weighted']):
                Method used to distribute sessions to real servers.
            mapped-addr (string) (max_len: 79):
                Mapped FQDN address name.
            mappedip (list[object]):
                IP address or address range on the destination network to wh...
            mappedport (string):
                Port number range on the destination network to which the ex...
            max-embryonic-connections (integer) (range: 0-100000):
                Maximum number of incomplete connections.
            monitor (list[object]):
                Name of the health check monitor to use when polling to dete...
            name (string) (max_len: 79):
                Virtual IP name.
            nat-source-vip (string) (enum: ['disable', 'enable']):
                Enable/disable forcing the source NAT mapped IP to the exter...
            nat44 (string) (enum: ['disable', 'enable']):
                Enable/disable NAT44.
            nat46 (string) (enum: ['disable', 'enable']):
                Enable/disable NAT46.
            one-click-gslb-server (string) (enum: ['disable', 'enable']):
                Enable/disable one click GSLB server integration with FortiG...
            outlook-web-access (string) (enum: ['disable', 'enable']):
                Enable to add the Front-End-Https header for Microsoft Outlo...
            persistence (string) (enum: ['none', 'http-cookie', 'ssl-session-id']):
                Configure how to make sure that clients connect to the same ...
            portforward (string) (enum: ['disable', 'enable']):
                Enable/disable port forwarding.
            portmapping-type (string) (enum: ['1-to-1', 'm-to-n']):
                Port mapping type.
            protocol (string) (enum: ['tcp', 'udp', 'sctp']):
                Protocol to use when forwarding packets.
            quic (list[object]):
                QUIC setting.
            realservers (list[object]):
                Select the real servers that this server load balancing VIP ...
            server-type (string) (enum: ['http', 'https', 'tcp']):
                Protocol to be load balanced by the virtual server (also cal...
            service (list[object]):
                Service name.
            src-filter (list[object]):
                Source address filter. Each address must be either an IP/sub...
            src-vip-filter (string) (enum: ['disable', 'enable']):
                Enable/disable use of 'src-filter' to match destinations for...
            srcintf-filter (list[object]):
                Interfaces to which the VIP applies. Separate the names with...
            ssl-accept-ffdhe-groups (string) (enum: ['enable', 'disable']):
                Enable/disable FFDHE cipher suite for SSL key exchange.
            ssl-algorithm (string) (enum: ['high', 'medium', 'low']):
                Permitted encryption algorithms for SSL sessions according t...
            ssl-certificate (list[object]):
                Name of the certificate to use for SSL handshake.
            ssl-cipher-suites (list[object]):
                SSL/TLS cipher suites acceptable from a client, ordered by p...
            ssl-client-fallback (string) (enum: ['disable', 'enable']):
                Enable/disable support for preventing Downgrade Attacks on c...
            ssl-client-rekey-count (integer) (range: 200-1048576):
                Maximum length of data in MB before triggering a client reke...
            ssl-client-renegotiation (string) (enum: ['allow', 'deny', 'secure']):
                Allow, deny, or require secure renegotiation of client sessi...
            ssl-client-session-state-max (integer) (range: 1-10000):
                Maximum number of client to FortiGate SSL session states to ...
            ssl-client-session-state-timeout (integer) (range: 1-14400):
                Number of minutes to keep client to FortiGate SSL session st...
            ssl-client-session-state-type (string) (enum: ['disable', 'time', 'count']):
                How to expire SSL sessions for the segment of the SSL connec...
            ssl-dh-bits (string) (enum: ['768', '1024', '1536']):
                Number of bits to use in the Diffie-Hellman exchange for RSA...
            ssl-hpkp (string) (enum: ['disable', 'enable', 'report-only']):
                Enable/disable including HPKP header in response.
            ssl-hpkp-age (integer) (range: 60-157680000):
                Number of seconds the client should honor the HPKP setting.
            ssl-hpkp-backup (string) (max_len: 79):
                Certificate to generate backup HPKP pin from.
            ssl-hpkp-include-subdomains (string) (enum: ['disable', 'enable']):
                Indicate that HPKP header applies to all subdomains.
            ssl-hpkp-primary (string) (max_len: 79):
                Certificate to generate primary HPKP pin from.
            ssl-hpkp-report-uri (string) (max_len: 255):
                URL to report HPKP violations to.
            ssl-hsts (string) (enum: ['disable', 'enable']):
                Enable/disable including HSTS header in response.
            ssl-hsts-age (integer) (range: 60-157680000):
                Number of seconds the client should honor the HSTS setting.
            ssl-hsts-include-subdomains (string) (enum: ['disable', 'enable']):
                Indicate that HSTS header applies to all subdomains.
            ssl-http-location-conversion (string) (enum: ['enable', 'disable']):
                Enable to replace HTTP with HTTPS in the reply's Location HT...
            ssl-http-match-host (string) (enum: ['enable', 'disable']):
                Enable/disable HTTP host matching for location conversion.
            ssl-max-version (string) (enum: ['ssl-3.0', 'tls-1.0', 'tls-1.1']):
                Highest SSL/TLS version acceptable from a client.
            ssl-min-version (string) (enum: ['ssl-3.0', 'tls-1.0', 'tls-1.1']):
                Lowest SSL/TLS version acceptable from a client.
            ssl-mode (string) (enum: ['half', 'full']):
                Apply SSL offloading between the client and the FortiGate (h...
            ssl-pfs (string) (enum: ['require', 'deny', 'allow']):
                Select the cipher suites that can be used for SSL perfect fo...
            ssl-send-empty-frags (string) (enum: ['enable', 'disable']):
                Enable/disable sending empty fragments to avoid CBC IV attac...
            ssl-server-algorithm (string) (enum: ['high', 'medium', 'low']):
                Permitted encryption algorithms for the server side of SSL f...
            ssl-server-cipher-suites (list[object]):
                SSL/TLS cipher suites to offer to a server, ordered by prior...
            ssl-server-max-version (string) (enum: ['ssl-3.0', 'tls-1.0', 'tls-1.1']):
                Highest SSL/TLS version acceptable from a server. Use the cl...
            ssl-server-min-version (string) (enum: ['ssl-3.0', 'tls-1.0', 'tls-1.1']):
                Lowest SSL/TLS version acceptable from a server. Use the cli...
            ssl-server-renegotiation (string) (enum: ['enable', 'disable']):
                Enable/disable secure renegotiation to comply with RFC 5746.
            ssl-server-session-state-max (integer) (range: 1-10000):
                Maximum number of FortiGate to Server SSL session states to ...
            ssl-server-session-state-timeout (integer) (range: 1-14400):
                Number of minutes to keep FortiGate to Server SSL session st...
            ssl-server-session-state-type (string) (enum: ['disable', 'time', 'count']):
                How to expire SSL sessions for the segment of the SSL connec...
            status (string) (enum: ['disable', 'enable']):
                Enable/disable VIP.
            type (string) (enum: ['static-nat', 'load-balance', 'server-load-balance']):
                Configure a static NAT, load balance, server load balance, a...
            user-agent-detect (string) (enum: ['disable', 'enable']):
                Enable/disable detecting device type by HTTP user-agent if n...
            uuid (string):
                Universally Unique Identifier (UUID; automatically assigned ...
            weblogic-server (string) (enum: ['disable', 'enable']):
                Enable to add an HTTP header to indicate SSL offloading for ...
            websphere-server (string) (enum: ['disable', 'enable']):
                Enable to add an HTTP header to indicate SSL offloading for ...

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if add_nat46_route is not None:
            payload_dict["add-nat46-route"] = add_nat46_route
        if arp_reply is not None:
            payload_dict["arp-reply"] = arp_reply
        if client_cert is not None:
            payload_dict["client-cert"] = client_cert
        if color is not None:
            payload_dict["color"] = color
        if comment is not None:
            payload_dict["comment"] = comment
        if dns_mapping_ttl is not None:
            payload_dict["dns-mapping-ttl"] = dns_mapping_ttl
        if empty_cert_action is not None:
            payload_dict["empty-cert-action"] = empty_cert_action
        if extaddr is not None:
            payload_dict["extaddr"] = extaddr
        if extintf is not None:
            payload_dict["extintf"] = extintf
        if extip is not None:
            payload_dict["extip"] = extip
        if extport is not None:
            payload_dict["extport"] = extport
        if gratuitous_arp_interval is not None:
            payload_dict["gratuitous-arp-interval"] = gratuitous_arp_interval
        if gslb_domain_name is not None:
            payload_dict["gslb-domain-name"] = gslb_domain_name
        if gslb_hostname is not None:
            payload_dict["gslb-hostname"] = gslb_hostname
        if gslb_public_ips is not None:
            payload_dict["gslb-public-ips"] = gslb_public_ips
        if h2_support is not None:
            payload_dict["h2-support"] = h2_support
        if h3_support is not None:
            payload_dict["h3-support"] = h3_support
        if http_cookie_age is not None:
            payload_dict["http-cookie-age"] = http_cookie_age
        if http_cookie_domain is not None:
            payload_dict["http-cookie-domain"] = http_cookie_domain
        if http_cookie_domain_from_host is not None:
            payload_dict["http-cookie-domain-from-host"] = http_cookie_domain_from_host
        if http_cookie_generation is not None:
            payload_dict["http-cookie-generation"] = http_cookie_generation
        if http_cookie_path is not None:
            payload_dict["http-cookie-path"] = http_cookie_path
        if http_cookie_share is not None:
            payload_dict["http-cookie-share"] = http_cookie_share
        if http_ip_header is not None:
            payload_dict["http-ip-header"] = http_ip_header
        if http_ip_header_name is not None:
            payload_dict["http-ip-header-name"] = http_ip_header_name
        if http_multiplex is not None:
            payload_dict["http-multiplex"] = http_multiplex
        if http_multiplex_max_concurrent_request is not None:
            payload_dict["http-multiplex-max-concurrent-request"] = (
                http_multiplex_max_concurrent_request
            )
        if http_multiplex_max_request is not None:
            payload_dict["http-multiplex-max-request"] = http_multiplex_max_request
        if http_multiplex_ttl is not None:
            payload_dict["http-multiplex-ttl"] = http_multiplex_ttl
        if http_redirect is not None:
            payload_dict["http-redirect"] = http_redirect
        if https_cookie_secure is not None:
            payload_dict["https-cookie-secure"] = https_cookie_secure
        if id is not None:
            payload_dict["id"] = id
        if ipv6_mappedip is not None:
            payload_dict["ipv6-mappedip"] = ipv6_mappedip
        if ipv6_mappedport is not None:
            payload_dict["ipv6-mappedport"] = ipv6_mappedport
        if ldb_method is not None:
            payload_dict["ldb-method"] = ldb_method
        if mapped_addr is not None:
            payload_dict["mapped-addr"] = mapped_addr
        if mappedip is not None:
            payload_dict["mappedip"] = mappedip
        if mappedport is not None:
            payload_dict["mappedport"] = mappedport
        if max_embryonic_connections is not None:
            payload_dict["max-embryonic-connections"] = max_embryonic_connections
        if monitor is not None:
            payload_dict["monitor"] = monitor
        if name is not None:
            payload_dict["name"] = name
        if nat_source_vip is not None:
            payload_dict["nat-source-vip"] = nat_source_vip
        if nat44 is not None:
            payload_dict["nat44"] = nat44
        if nat46 is not None:
            payload_dict["nat46"] = nat46
        if one_click_gslb_server is not None:
            payload_dict["one-click-gslb-server"] = one_click_gslb_server
        if outlook_web_access is not None:
            payload_dict["outlook-web-access"] = outlook_web_access
        if persistence is not None:
            payload_dict["persistence"] = persistence
        if portforward is not None:
            payload_dict["portforward"] = portforward
        if portmapping_type is not None:
            payload_dict["portmapping-type"] = portmapping_type
        if protocol is not None:
            payload_dict["protocol"] = protocol
        if quic is not None:
            payload_dict["quic"] = quic
        if realservers is not None:
            payload_dict["realservers"] = realservers
        if server_type is not None:
            payload_dict["server-type"] = server_type
        if service is not None:
            payload_dict["service"] = service
        if src_filter is not None:
            payload_dict["src-filter"] = src_filter
        if src_vip_filter is not None:
            payload_dict["src-vip-filter"] = src_vip_filter
        if srcintf_filter is not None:
            payload_dict["srcintf-filter"] = srcintf_filter
        if ssl_accept_ffdhe_groups is not None:
            payload_dict["ssl-accept-ffdhe-groups"] = ssl_accept_ffdhe_groups
        if ssl_algorithm is not None:
            payload_dict["ssl-algorithm"] = ssl_algorithm
        if ssl_certificate is not None:
            payload_dict["ssl-certificate"] = ssl_certificate
        if ssl_cipher_suites is not None:
            payload_dict["ssl-cipher-suites"] = ssl_cipher_suites
        if ssl_client_fallback is not None:
            payload_dict["ssl-client-fallback"] = ssl_client_fallback
        if ssl_client_rekey_count is not None:
            payload_dict["ssl-client-rekey-count"] = ssl_client_rekey_count
        if ssl_client_renegotiation is not None:
            payload_dict["ssl-client-renegotiation"] = ssl_client_renegotiation
        if ssl_client_session_state_max is not None:
            payload_dict["ssl-client-session-state-max"] = ssl_client_session_state_max
        if ssl_client_session_state_timeout is not None:
            payload_dict["ssl-client-session-state-timeout"] = ssl_client_session_state_timeout
        if ssl_client_session_state_type is not None:
            payload_dict["ssl-client-session-state-type"] = ssl_client_session_state_type
        if ssl_dh_bits is not None:
            payload_dict["ssl-dh-bits"] = ssl_dh_bits
        if ssl_hpkp is not None:
            payload_dict["ssl-hpkp"] = ssl_hpkp
        if ssl_hpkp_age is not None:
            payload_dict["ssl-hpkp-age"] = ssl_hpkp_age
        if ssl_hpkp_backup is not None:
            payload_dict["ssl-hpkp-backup"] = ssl_hpkp_backup
        if ssl_hpkp_include_subdomains is not None:
            payload_dict["ssl-hpkp-include-subdomains"] = ssl_hpkp_include_subdomains
        if ssl_hpkp_primary is not None:
            payload_dict["ssl-hpkp-primary"] = ssl_hpkp_primary
        if ssl_hpkp_report_uri is not None:
            payload_dict["ssl-hpkp-report-uri"] = ssl_hpkp_report_uri
        if ssl_hsts is not None:
            payload_dict["ssl-hsts"] = ssl_hsts
        if ssl_hsts_age is not None:
            payload_dict["ssl-hsts-age"] = ssl_hsts_age
        if ssl_hsts_include_subdomains is not None:
            payload_dict["ssl-hsts-include-subdomains"] = ssl_hsts_include_subdomains
        if ssl_http_location_conversion is not None:
            payload_dict["ssl-http-location-conversion"] = ssl_http_location_conversion
        if ssl_http_match_host is not None:
            payload_dict["ssl-http-match-host"] = ssl_http_match_host
        if ssl_max_version is not None:
            payload_dict["ssl-max-version"] = ssl_max_version
        if ssl_min_version is not None:
            payload_dict["ssl-min-version"] = ssl_min_version
        if ssl_mode is not None:
            payload_dict["ssl-mode"] = ssl_mode
        if ssl_pfs is not None:
            payload_dict["ssl-pfs"] = ssl_pfs
        if ssl_send_empty_frags is not None:
            payload_dict["ssl-send-empty-frags"] = ssl_send_empty_frags
        if ssl_server_algorithm is not None:
            payload_dict["ssl-server-algorithm"] = ssl_server_algorithm
        if ssl_server_cipher_suites is not None:
            payload_dict["ssl-server-cipher-suites"] = ssl_server_cipher_suites
        if ssl_server_max_version is not None:
            payload_dict["ssl-server-max-version"] = ssl_server_max_version
        if ssl_server_min_version is not None:
            payload_dict["ssl-server-min-version"] = ssl_server_min_version
        if ssl_server_renegotiation is not None:
            payload_dict["ssl-server-renegotiation"] = ssl_server_renegotiation
        if ssl_server_session_state_max is not None:
            payload_dict["ssl-server-session-state-max"] = ssl_server_session_state_max
        if ssl_server_session_state_timeout is not None:
            payload_dict["ssl-server-session-state-timeout"] = ssl_server_session_state_timeout
        if ssl_server_session_state_type is not None:
            payload_dict["ssl-server-session-state-type"] = ssl_server_session_state_type
        if status is not None:
            payload_dict["status"] = status
        if type is not None:
            payload_dict["type"] = type
        if user_agent_detect is not None:
            payload_dict["user-agent-detect"] = user_agent_detect
        if uuid is not None:
            payload_dict["uuid"] = uuid
        if weblogic_server is not None:
            payload_dict["weblogic-server"] = weblogic_server
        if websphere_server is not None:
            payload_dict["websphere-server"] = websphere_server

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if action is not None:
            params["action"] = action
        if before is not None:
            params["before"] = before
        if after is not None:
            params["after"] = after
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.put(
            "cmdb",
            f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path,
            data=payload_dict,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Optional[Union[str, int]] = None,
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete a vip entry.

        Args:
            mkey: The name (primary key)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Returns:
            API response dictionary
        """
        # Validate mkey
        if mkey is None:
            raise ValueError("mkey cannot be None")

        mkey_str = str(mkey)
        if not mkey_str:
            raise ValueError("mkey cannot be empty")

        params = {}

        if vdom is not None:
            params["vdom"] = vdom
        if scope is not None:
            params["scope"] = scope

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.delete(
            "cmdb", f"{self.path}/{encode_path_component(mkey)}" if mkey is not None else self.path, params=params, vdom=vdom, raw_json=raw_json
        )
