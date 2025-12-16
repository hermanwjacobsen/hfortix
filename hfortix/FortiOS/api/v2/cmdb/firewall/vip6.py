"""
FortiOS vip6 API wrapper.
Provides access to /api/v2/cmdb/firewall/vip6 endpoint.
"""

from typing import Any, Dict, List, Optional, Union


class Vip6:
    """
    Wrapper for firewall vip6 API endpoint.
    
    Manages vip6 configuration with full Swagger-spec parameter support.
    """
    
    def __init__(self, http_client: Any):
        """
        Initialize the Vip6 wrapper.
        
        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = 'firewall/vip6'
    
    def list(
        self,
        datasource: Optional[Any] = None,
        start: Optional[Any] = None,
        count: Optional[Any] = None,
        skip_to: Optional[Any] = None,
        with_meta: Optional[Any] = None,
        with_contents_hash: Optional[Any] = None,
        skip: Optional[Any] = None,
        format: Optional[Any] = None,
        filter: Optional[Any] = None,
        key: Optional[Any] = None,
        pattern: Optional[Any] = None,
        scope: Optional[Any] = None,
        exclude_default_values: Optional[Any] = None,
        datasource_format: Optional[Any] = None,
        unfiltered_count: Optional[Any] = None,
        stat_items: Optional[Any] = None,
        primary_keys: Optional[Any] = None,
        action: Optional[Any] = None,
        vdom: Optional[Any] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Retrieve a list of all vip6 entries.
        
        Args:
            datasource: Enable to include datasource information for each linked object.
            start: Starting entry index.
            count: Maximum number of entries to return.
            skip_to: Skip to Nth CMDB entry.
            with_meta: Enable to include meta information about each object (type id, referen
            with_contents_hash: Enable to include a checksum of each object's contents.
            skip: Enable to call CLI skip operator to hide skipped properties.
            format: List of property names to include in results, separated by | (i.e. pol
            filter: Filtering multiple key/value pairs
            key: If present, objects will be filtered on property with this name.
            pattern: If present, objects will be filtered on property with this value.
            scope: Scope [global|vdom|both*]
            exclude_default_values: Exclude properties/objects with default value
            datasource_format: A map of datasources to a string of attributes, separated by | (ie: po
            unfiltered_count: Maximum number of unfiltered entries to interate through.
            stat_items: Items to count occurrence in entire response (multiple items should be
            primary_keys: The primary key to find indexes for.
            action: default: Return the CLI default values for entire CLI tree.
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary with results list
        """
        params = {}
        
        if datasource is not None:
            params['datasource'] = datasource
        if start is not None:
            params['start'] = start
        if count is not None:
            params['count'] = count
        if skip_to is not None:
            params['skip_to'] = skip_to
        if with_meta is not None:
            params['with_meta'] = with_meta
        if with_contents_hash is not None:
            params['with_contents_hash'] = with_contents_hash
        if skip is not None:
            params['skip'] = skip
        if format is not None:
            params['format'] = format
        if filter is not None:
            params['filter'] = filter
        if key is not None:
            params['key'] = key
        if pattern is not None:
            params['pattern'] = pattern
        if scope is not None:
            params['scope'] = scope
        if exclude_default_values is not None:
            params['exclude-default-values'] = exclude_default_values
        if datasource_format is not None:
            params['datasource_format'] = datasource_format
        if unfiltered_count is not None:
            params['unfiltered_count'] = unfiltered_count
        if stat_items is not None:
            params['stat-items'] = stat_items
        if primary_keys is not None:
            params['primary_keys'] = primary_keys
        if action is not None:
            params['action'] = action
        if vdom is not None:
            params['vdom'] = vdom
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.get('cmdb', self.path, params=params, vdom=vdom)

    def get(
        self,
        mkey: Union[str, int],
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
        **kwargs
    ) -> Dict[str, Any]:
        """
        Retrieve a specific vip6 entry by its name.
        
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
            params['attr'] = attr
        if count is not None:
            params['count'] = count
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        if scope is not None:
            params['scope'] = scope
        if datasource is not None:
            params['datasource'] = datasource
        if with_meta is not None:
            params['with_meta'] = with_meta
        if skip is not None:
            params['skip'] = skip
        if format is not None:
            params['format'] = format
        if action is not None:
            params['action'] = action
        if vdom is not None:
            params['vdom'] = vdom
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.get('cmdb', f'{self.path}/{mkey_str}', params=params, vdom=vdom)

    def create(
        self,
        data: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        add_nat64_route: Optional[str] = None,
        client_cert: Optional[str] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        embedded_ipv4_address: Optional[str] = None,
        empty_cert_action: Optional[str] = None,
        extip: Optional[str] = None,
        extport: Optional[str] = None,
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
        http_redirect: Optional[str] = None,
        https_cookie_secure: Optional[str] = None,
        id: Optional[int] = None,
        ipv4_mappedip: Optional[str] = None,
        ipv4_mappedport: Optional[str] = None,
        ldb_method: Optional[str] = None,
        mappedip: Optional[str] = None,
        mappedport: Optional[str] = None,
        max_embryonic_connections: Optional[int] = None,
        monitor: Optional[list] = None,
        name: Optional[str] = None,
        nat_source_vip: Optional[str] = None,
        nat64: Optional[str] = None,
        nat66: Optional[str] = None,
        ndp_reply: Optional[str] = None,
        outlook_web_access: Optional[str] = None,
        persistence: Optional[str] = None,
        portforward: Optional[str] = None,
        protocol: Optional[str] = None,
        quic: Optional[list] = None,
        realservers: Optional[list] = None,
        server_type: Optional[str] = None,
        src_filter: Optional[list] = None,
        src_vip_filter: Optional[str] = None,
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
        type: Optional[str] = None,
        user_agent_detect: Optional[str] = None,
        uuid: Optional[str] = None,
        weblogic_server: Optional[str] = None,
        websphere_server: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a new vip6 entry.
        
        Supports two usage patterns:
        1. Pass data dict: create(data={"key": "value"}, vdom="root")
        2. Pass kwargs: create(key="value", vdom="root")
        
        Args:
            data: The configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            add-nat64-route (string) (enum: ['disable', 'enable']):
                Enable/disable adding NAT64 route.
            client-cert (string) (enum: ['disable', 'enable']):
                Enable/disable requesting client certificate.
            color (integer) (range: 0-32):
                Color of icon on the GUI.
            comment (string) (max_len: 255):
                Comment.
            embedded-ipv4-address (string) (enum: ['disable', 'enable']):
                Enable/disable use of the lower 32 bits of the external IPv6...
            empty-cert-action (string) (enum: ['accept', 'block', 'accept-unmanageable']):
                Action for an empty client certificate.
            extip (string):
                IPv6 address or address range on the external interface that...
            extport (string):
                Incoming port number range that you want to map to a port nu...
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
            http-redirect (string) (enum: ['enable', 'disable']):
                Enable/disable redirection of HTTP to HTTPS.
            https-cookie-secure (string) (enum: ['disable', 'enable']):
                Enable/disable verification that inserted HTTPS cookies are ...
            id (integer) (range: 0-65535):
                Custom defined ID.
            ipv4-mappedip (string):
                Range of mapped IP addresses. Specify the start IP address f...
            ipv4-mappedport (string):
                IPv4 port number range on the destination network to which t...
            ldb-method (string) (enum: ['static', 'round-robin', 'weighted']):
                Method used to distribute sessions to real servers.
            mappedip (string):
                Mapped IPv6 address range in the format startIP-endIP.
            mappedport (string):
                Port number range on the destination network to which the ex...
            max-embryonic-connections (integer) (range: 0-100000):
                Maximum number of incomplete connections.
            monitor (list[object]):
                Name of the health check monitor to use when polling to dete...
            name (string) (max_len: 79):
                Virtual ip6 name.
            nat-source-vip (string) (enum: ['disable', 'enable']):
                Enable to perform SNAT on traffic from mappedip to the extip...
            nat64 (string) (enum: ['disable', 'enable']):
                Enable/disable DNAT64.
            nat66 (string) (enum: ['disable', 'enable']):
                Enable/disable DNAT66.
            ndp-reply (string) (enum: ['disable', 'enable']):
                Enable/disable this FortiGate unit's ability to respond to N...
            outlook-web-access (string) (enum: ['disable', 'enable']):
                Enable to add the Front-End-Https header for Microsoft Outlo...
            persistence (string) (enum: ['none', 'http-cookie', 'ssl-session-id']):
                Configure how to make sure that clients connect to the same ...
            portforward (string) (enum: ['disable', 'enable']):
                Enable port forwarding.
            protocol (string) (enum: ['tcp', 'udp', 'sctp']):
                Protocol to use when forwarding packets.
            quic (list[object]):
                QUIC setting.
            realservers (list[object]):
                Select the real servers that this server load balancing VIP ...
            server-type (string) (enum: ['http', 'https', 'tcp']):
                Protocol to be load balanced by the virtual server (also cal...
            src-filter (list[object]):
                Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses wi...
            src-vip-filter (string) (enum: ['disable', 'enable']):
                Enable/disable use of 'src-filter' to match destinations for...
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
                Number of minutes the web browser should keep HPKP.
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
            type (string) (enum: ['static-nat', 'server-load-balance', 'access-proxy']):
                Configure a static NAT server load balance VIP or access pro...
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
        if data is None:
            data = {}
        if add_nat64_route is not None:
            data['add-nat64-route'] = add_nat64_route
        if client_cert is not None:
            data['client-cert'] = client_cert
        if color is not None:
            data['color'] = color
        if comment is not None:
            data['comment'] = comment
        if embedded_ipv4_address is not None:
            data['embedded-ipv4-address'] = embedded_ipv4_address
        if empty_cert_action is not None:
            data['empty-cert-action'] = empty_cert_action
        if extip is not None:
            data['extip'] = extip
        if extport is not None:
            data['extport'] = extport
        if h2_support is not None:
            data['h2-support'] = h2_support
        if h3_support is not None:
            data['h3-support'] = h3_support
        if http_cookie_age is not None:
            data['http-cookie-age'] = http_cookie_age
        if http_cookie_domain is not None:
            data['http-cookie-domain'] = http_cookie_domain
        if http_cookie_domain_from_host is not None:
            data['http-cookie-domain-from-host'] = http_cookie_domain_from_host
        if http_cookie_generation is not None:
            data['http-cookie-generation'] = http_cookie_generation
        if http_cookie_path is not None:
            data['http-cookie-path'] = http_cookie_path
        if http_cookie_share is not None:
            data['http-cookie-share'] = http_cookie_share
        if http_ip_header is not None:
            data['http-ip-header'] = http_ip_header
        if http_ip_header_name is not None:
            data['http-ip-header-name'] = http_ip_header_name
        if http_multiplex is not None:
            data['http-multiplex'] = http_multiplex
        if http_redirect is not None:
            data['http-redirect'] = http_redirect
        if https_cookie_secure is not None:
            data['https-cookie-secure'] = https_cookie_secure
        if id is not None:
            data['id'] = id
        if ipv4_mappedip is not None:
            data['ipv4-mappedip'] = ipv4_mappedip
        if ipv4_mappedport is not None:
            data['ipv4-mappedport'] = ipv4_mappedport
        if ldb_method is not None:
            data['ldb-method'] = ldb_method
        if mappedip is not None:
            data['mappedip'] = mappedip
        if mappedport is not None:
            data['mappedport'] = mappedport
        if max_embryonic_connections is not None:
            data['max-embryonic-connections'] = max_embryonic_connections
        if monitor is not None:
            data['monitor'] = monitor
        if name is not None:
            data['name'] = name
        if nat_source_vip is not None:
            data['nat-source-vip'] = nat_source_vip
        if nat64 is not None:
            data['nat64'] = nat64
        if nat66 is not None:
            data['nat66'] = nat66
        if ndp_reply is not None:
            data['ndp-reply'] = ndp_reply
        if outlook_web_access is not None:
            data['outlook-web-access'] = outlook_web_access
        if persistence is not None:
            data['persistence'] = persistence
        if portforward is not None:
            data['portforward'] = portforward
        if protocol is not None:
            data['protocol'] = protocol
        if quic is not None:
            data['quic'] = quic
        if realservers is not None:
            data['realservers'] = realservers
        if server_type is not None:
            data['server-type'] = server_type
        if src_filter is not None:
            data['src-filter'] = src_filter
        if src_vip_filter is not None:
            data['src-vip-filter'] = src_vip_filter
        if ssl_accept_ffdhe_groups is not None:
            data['ssl-accept-ffdhe-groups'] = ssl_accept_ffdhe_groups
        if ssl_algorithm is not None:
            data['ssl-algorithm'] = ssl_algorithm
        if ssl_certificate is not None:
            data['ssl-certificate'] = ssl_certificate
        if ssl_cipher_suites is not None:
            data['ssl-cipher-suites'] = ssl_cipher_suites
        if ssl_client_fallback is not None:
            data['ssl-client-fallback'] = ssl_client_fallback
        if ssl_client_rekey_count is not None:
            data['ssl-client-rekey-count'] = ssl_client_rekey_count
        if ssl_client_renegotiation is not None:
            data['ssl-client-renegotiation'] = ssl_client_renegotiation
        if ssl_client_session_state_max is not None:
            data['ssl-client-session-state-max'] = ssl_client_session_state_max
        if ssl_client_session_state_timeout is not None:
            data['ssl-client-session-state-timeout'] = ssl_client_session_state_timeout
        if ssl_client_session_state_type is not None:
            data['ssl-client-session-state-type'] = ssl_client_session_state_type
        if ssl_dh_bits is not None:
            data['ssl-dh-bits'] = ssl_dh_bits
        if ssl_hpkp is not None:
            data['ssl-hpkp'] = ssl_hpkp
        if ssl_hpkp_age is not None:
            data['ssl-hpkp-age'] = ssl_hpkp_age
        if ssl_hpkp_backup is not None:
            data['ssl-hpkp-backup'] = ssl_hpkp_backup
        if ssl_hpkp_include_subdomains is not None:
            data['ssl-hpkp-include-subdomains'] = ssl_hpkp_include_subdomains
        if ssl_hpkp_primary is not None:
            data['ssl-hpkp-primary'] = ssl_hpkp_primary
        if ssl_hpkp_report_uri is not None:
            data['ssl-hpkp-report-uri'] = ssl_hpkp_report_uri
        if ssl_hsts is not None:
            data['ssl-hsts'] = ssl_hsts
        if ssl_hsts_age is not None:
            data['ssl-hsts-age'] = ssl_hsts_age
        if ssl_hsts_include_subdomains is not None:
            data['ssl-hsts-include-subdomains'] = ssl_hsts_include_subdomains
        if ssl_http_location_conversion is not None:
            data['ssl-http-location-conversion'] = ssl_http_location_conversion
        if ssl_http_match_host is not None:
            data['ssl-http-match-host'] = ssl_http_match_host
        if ssl_max_version is not None:
            data['ssl-max-version'] = ssl_max_version
        if ssl_min_version is not None:
            data['ssl-min-version'] = ssl_min_version
        if ssl_mode is not None:
            data['ssl-mode'] = ssl_mode
        if ssl_pfs is not None:
            data['ssl-pfs'] = ssl_pfs
        if ssl_send_empty_frags is not None:
            data['ssl-send-empty-frags'] = ssl_send_empty_frags
        if ssl_server_algorithm is not None:
            data['ssl-server-algorithm'] = ssl_server_algorithm
        if ssl_server_cipher_suites is not None:
            data['ssl-server-cipher-suites'] = ssl_server_cipher_suites
        if ssl_server_max_version is not None:
            data['ssl-server-max-version'] = ssl_server_max_version
        if ssl_server_min_version is not None:
            data['ssl-server-min-version'] = ssl_server_min_version
        if ssl_server_renegotiation is not None:
            data['ssl-server-renegotiation'] = ssl_server_renegotiation
        if ssl_server_session_state_max is not None:
            data['ssl-server-session-state-max'] = ssl_server_session_state_max
        if ssl_server_session_state_timeout is not None:
            data['ssl-server-session-state-timeout'] = ssl_server_session_state_timeout
        if ssl_server_session_state_type is not None:
            data['ssl-server-session-state-type'] = ssl_server_session_state_type
        if type is not None:
            data['type'] = type
        if user_agent_detect is not None:
            data['user-agent-detect'] = user_agent_detect
        if uuid is not None:
            data['uuid'] = uuid
        if weblogic_server is not None:
            data['weblogic-server'] = weblogic_server
        if websphere_server is not None:
            data['websphere-server'] = websphere_server
        
        params = {}
        
        if vdom is not None:
            params['vdom'] = vdom
        if action is not None:
            params['action'] = action
        if nkey is not None:
            params['nkey'] = nkey
        if scope is not None:
            params['scope'] = scope
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.post('cmdb', self.path, data=data, params=params, vdom=vdom)

    def update(
        self,
        mkey: Union[str, int],
        data: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        add_nat64_route: Optional[str] = None,
        client_cert: Optional[str] = None,
        color: Optional[int] = None,
        comment: Optional[str] = None,
        embedded_ipv4_address: Optional[str] = None,
        empty_cert_action: Optional[str] = None,
        extip: Optional[str] = None,
        extport: Optional[str] = None,
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
        http_redirect: Optional[str] = None,
        https_cookie_secure: Optional[str] = None,
        id: Optional[int] = None,
        ipv4_mappedip: Optional[str] = None,
        ipv4_mappedport: Optional[str] = None,
        ldb_method: Optional[str] = None,
        mappedip: Optional[str] = None,
        mappedport: Optional[str] = None,
        max_embryonic_connections: Optional[int] = None,
        monitor: Optional[list] = None,
        name: Optional[str] = None,
        nat_source_vip: Optional[str] = None,
        nat64: Optional[str] = None,
        nat66: Optional[str] = None,
        ndp_reply: Optional[str] = None,
        outlook_web_access: Optional[str] = None,
        persistence: Optional[str] = None,
        portforward: Optional[str] = None,
        protocol: Optional[str] = None,
        quic: Optional[list] = None,
        realservers: Optional[list] = None,
        server_type: Optional[str] = None,
        src_filter: Optional[list] = None,
        src_vip_filter: Optional[str] = None,
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
        type: Optional[str] = None,
        user_agent_detect: Optional[str] = None,
        uuid: Optional[str] = None,
        weblogic_server: Optional[str] = None,
        websphere_server: Optional[str] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Update an existing vip6 entry.
        
        Supports two usage patterns:
        1. Pass data dict: update(mkey=123, data={"key": "value"}, vdom="root")
        2. Pass kwargs: update(mkey=123, key="value", vdom="root")
        
        Args:
            mkey: The name (primary key)
            data: The updated configuration data (optional if using kwargs)
            vdom: Specify the Virtual Domain(s) from which results are returned or chang
            action: If supported, an action can be specified.
            before: If *action=move*, use *before* to specify the ID of the resource that 
            after: If *action=move*, use *after* to specify the ID of the resource that t
            scope: Specify the Scope from which results are returned or changes are appli
            **kwargs: Additional parameters

        Body schema properties (can pass via data dict or as kwargs):

            add-nat64-route (string) (enum: ['disable', 'enable']):
                Enable/disable adding NAT64 route.
            client-cert (string) (enum: ['disable', 'enable']):
                Enable/disable requesting client certificate.
            color (integer) (range: 0-32):
                Color of icon on the GUI.
            comment (string) (max_len: 255):
                Comment.
            embedded-ipv4-address (string) (enum: ['disable', 'enable']):
                Enable/disable use of the lower 32 bits of the external IPv6...
            empty-cert-action (string) (enum: ['accept', 'block', 'accept-unmanageable']):
                Action for an empty client certificate.
            extip (string):
                IPv6 address or address range on the external interface that...
            extport (string):
                Incoming port number range that you want to map to a port nu...
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
            http-redirect (string) (enum: ['enable', 'disable']):
                Enable/disable redirection of HTTP to HTTPS.
            https-cookie-secure (string) (enum: ['disable', 'enable']):
                Enable/disable verification that inserted HTTPS cookies are ...
            id (integer) (range: 0-65535):
                Custom defined ID.
            ipv4-mappedip (string):
                Range of mapped IP addresses. Specify the start IP address f...
            ipv4-mappedport (string):
                IPv4 port number range on the destination network to which t...
            ldb-method (string) (enum: ['static', 'round-robin', 'weighted']):
                Method used to distribute sessions to real servers.
            mappedip (string):
                Mapped IPv6 address range in the format startIP-endIP.
            mappedport (string):
                Port number range on the destination network to which the ex...
            max-embryonic-connections (integer) (range: 0-100000):
                Maximum number of incomplete connections.
            monitor (list[object]):
                Name of the health check monitor to use when polling to dete...
            name (string) (max_len: 79):
                Virtual ip6 name.
            nat-source-vip (string) (enum: ['disable', 'enable']):
                Enable to perform SNAT on traffic from mappedip to the extip...
            nat64 (string) (enum: ['disable', 'enable']):
                Enable/disable DNAT64.
            nat66 (string) (enum: ['disable', 'enable']):
                Enable/disable DNAT66.
            ndp-reply (string) (enum: ['disable', 'enable']):
                Enable/disable this FortiGate unit's ability to respond to N...
            outlook-web-access (string) (enum: ['disable', 'enable']):
                Enable to add the Front-End-Https header for Microsoft Outlo...
            persistence (string) (enum: ['none', 'http-cookie', 'ssl-session-id']):
                Configure how to make sure that clients connect to the same ...
            portforward (string) (enum: ['disable', 'enable']):
                Enable port forwarding.
            protocol (string) (enum: ['tcp', 'udp', 'sctp']):
                Protocol to use when forwarding packets.
            quic (list[object]):
                QUIC setting.
            realservers (list[object]):
                Select the real servers that this server load balancing VIP ...
            server-type (string) (enum: ['http', 'https', 'tcp']):
                Protocol to be load balanced by the virtual server (also cal...
            src-filter (list[object]):
                Source IP6 filter (x:x:x:x:x:x:x:x/x). Separate addresses wi...
            src-vip-filter (string) (enum: ['disable', 'enable']):
                Enable/disable use of 'src-filter' to match destinations for...
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
                Number of minutes the web browser should keep HPKP.
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
            type (string) (enum: ['static-nat', 'server-load-balance', 'access-proxy']):
                Configure a static NAT server load balance VIP or access pro...
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
        if data is None:
            data = {}
        if add_nat64_route is not None:
            data['add-nat64-route'] = add_nat64_route
        if client_cert is not None:
            data['client-cert'] = client_cert
        if color is not None:
            data['color'] = color
        if comment is not None:
            data['comment'] = comment
        if embedded_ipv4_address is not None:
            data['embedded-ipv4-address'] = embedded_ipv4_address
        if empty_cert_action is not None:
            data['empty-cert-action'] = empty_cert_action
        if extip is not None:
            data['extip'] = extip
        if extport is not None:
            data['extport'] = extport
        if h2_support is not None:
            data['h2-support'] = h2_support
        if h3_support is not None:
            data['h3-support'] = h3_support
        if http_cookie_age is not None:
            data['http-cookie-age'] = http_cookie_age
        if http_cookie_domain is not None:
            data['http-cookie-domain'] = http_cookie_domain
        if http_cookie_domain_from_host is not None:
            data['http-cookie-domain-from-host'] = http_cookie_domain_from_host
        if http_cookie_generation is not None:
            data['http-cookie-generation'] = http_cookie_generation
        if http_cookie_path is not None:
            data['http-cookie-path'] = http_cookie_path
        if http_cookie_share is not None:
            data['http-cookie-share'] = http_cookie_share
        if http_ip_header is not None:
            data['http-ip-header'] = http_ip_header
        if http_ip_header_name is not None:
            data['http-ip-header-name'] = http_ip_header_name
        if http_multiplex is not None:
            data['http-multiplex'] = http_multiplex
        if http_redirect is not None:
            data['http-redirect'] = http_redirect
        if https_cookie_secure is not None:
            data['https-cookie-secure'] = https_cookie_secure
        if id is not None:
            data['id'] = id
        if ipv4_mappedip is not None:
            data['ipv4-mappedip'] = ipv4_mappedip
        if ipv4_mappedport is not None:
            data['ipv4-mappedport'] = ipv4_mappedport
        if ldb_method is not None:
            data['ldb-method'] = ldb_method
        if mappedip is not None:
            data['mappedip'] = mappedip
        if mappedport is not None:
            data['mappedport'] = mappedport
        if max_embryonic_connections is not None:
            data['max-embryonic-connections'] = max_embryonic_connections
        if monitor is not None:
            data['monitor'] = monitor
        if name is not None:
            data['name'] = name
        if nat_source_vip is not None:
            data['nat-source-vip'] = nat_source_vip
        if nat64 is not None:
            data['nat64'] = nat64
        if nat66 is not None:
            data['nat66'] = nat66
        if ndp_reply is not None:
            data['ndp-reply'] = ndp_reply
        if outlook_web_access is not None:
            data['outlook-web-access'] = outlook_web_access
        if persistence is not None:
            data['persistence'] = persistence
        if portforward is not None:
            data['portforward'] = portforward
        if protocol is not None:
            data['protocol'] = protocol
        if quic is not None:
            data['quic'] = quic
        if realservers is not None:
            data['realservers'] = realservers
        if server_type is not None:
            data['server-type'] = server_type
        if src_filter is not None:
            data['src-filter'] = src_filter
        if src_vip_filter is not None:
            data['src-vip-filter'] = src_vip_filter
        if ssl_accept_ffdhe_groups is not None:
            data['ssl-accept-ffdhe-groups'] = ssl_accept_ffdhe_groups
        if ssl_algorithm is not None:
            data['ssl-algorithm'] = ssl_algorithm
        if ssl_certificate is not None:
            data['ssl-certificate'] = ssl_certificate
        if ssl_cipher_suites is not None:
            data['ssl-cipher-suites'] = ssl_cipher_suites
        if ssl_client_fallback is not None:
            data['ssl-client-fallback'] = ssl_client_fallback
        if ssl_client_rekey_count is not None:
            data['ssl-client-rekey-count'] = ssl_client_rekey_count
        if ssl_client_renegotiation is not None:
            data['ssl-client-renegotiation'] = ssl_client_renegotiation
        if ssl_client_session_state_max is not None:
            data['ssl-client-session-state-max'] = ssl_client_session_state_max
        if ssl_client_session_state_timeout is not None:
            data['ssl-client-session-state-timeout'] = ssl_client_session_state_timeout
        if ssl_client_session_state_type is not None:
            data['ssl-client-session-state-type'] = ssl_client_session_state_type
        if ssl_dh_bits is not None:
            data['ssl-dh-bits'] = ssl_dh_bits
        if ssl_hpkp is not None:
            data['ssl-hpkp'] = ssl_hpkp
        if ssl_hpkp_age is not None:
            data['ssl-hpkp-age'] = ssl_hpkp_age
        if ssl_hpkp_backup is not None:
            data['ssl-hpkp-backup'] = ssl_hpkp_backup
        if ssl_hpkp_include_subdomains is not None:
            data['ssl-hpkp-include-subdomains'] = ssl_hpkp_include_subdomains
        if ssl_hpkp_primary is not None:
            data['ssl-hpkp-primary'] = ssl_hpkp_primary
        if ssl_hpkp_report_uri is not None:
            data['ssl-hpkp-report-uri'] = ssl_hpkp_report_uri
        if ssl_hsts is not None:
            data['ssl-hsts'] = ssl_hsts
        if ssl_hsts_age is not None:
            data['ssl-hsts-age'] = ssl_hsts_age
        if ssl_hsts_include_subdomains is not None:
            data['ssl-hsts-include-subdomains'] = ssl_hsts_include_subdomains
        if ssl_http_location_conversion is not None:
            data['ssl-http-location-conversion'] = ssl_http_location_conversion
        if ssl_http_match_host is not None:
            data['ssl-http-match-host'] = ssl_http_match_host
        if ssl_max_version is not None:
            data['ssl-max-version'] = ssl_max_version
        if ssl_min_version is not None:
            data['ssl-min-version'] = ssl_min_version
        if ssl_mode is not None:
            data['ssl-mode'] = ssl_mode
        if ssl_pfs is not None:
            data['ssl-pfs'] = ssl_pfs
        if ssl_send_empty_frags is not None:
            data['ssl-send-empty-frags'] = ssl_send_empty_frags
        if ssl_server_algorithm is not None:
            data['ssl-server-algorithm'] = ssl_server_algorithm
        if ssl_server_cipher_suites is not None:
            data['ssl-server-cipher-suites'] = ssl_server_cipher_suites
        if ssl_server_max_version is not None:
            data['ssl-server-max-version'] = ssl_server_max_version
        if ssl_server_min_version is not None:
            data['ssl-server-min-version'] = ssl_server_min_version
        if ssl_server_renegotiation is not None:
            data['ssl-server-renegotiation'] = ssl_server_renegotiation
        if ssl_server_session_state_max is not None:
            data['ssl-server-session-state-max'] = ssl_server_session_state_max
        if ssl_server_session_state_timeout is not None:
            data['ssl-server-session-state-timeout'] = ssl_server_session_state_timeout
        if ssl_server_session_state_type is not None:
            data['ssl-server-session-state-type'] = ssl_server_session_state_type
        if type is not None:
            data['type'] = type
        if user_agent_detect is not None:
            data['user-agent-detect'] = user_agent_detect
        if uuid is not None:
            data['uuid'] = uuid
        if weblogic_server is not None:
            data['weblogic-server'] = weblogic_server
        if websphere_server is not None:
            data['websphere-server'] = websphere_server
        
        params = {}
        
        if vdom is not None:
            params['vdom'] = vdom
        if action is not None:
            params['action'] = action
        if before is not None:
            params['before'] = before
        if after is not None:
            params['after'] = after
        if scope is not None:
            params['scope'] = scope
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.put('cmdb', f'{self.path}/{mkey_str}', data=data, params=params, vdom=vdom)

    def delete(
        self,
        mkey: Union[str, int],
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Delete a vip6 entry.
        
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
            params['vdom'] = vdom
        if scope is not None:
            params['scope'] = scope
        
        # Add any additional kwargs
        params.update(kwargs)
        
        # Extract vdom if present
        vdom = params.pop('vdom', None)
        
        return self._client.delete('cmdb', f'{self.path}/{mkey_str}', params=params, vdom=vdom)
