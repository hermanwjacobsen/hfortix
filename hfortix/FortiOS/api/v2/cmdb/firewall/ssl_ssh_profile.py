"""
FortiOS ssl-ssh-profile API wrapper.
Provides access to /api/v2/cmdb/firewall/ssl-ssh-profile endpoint.
"""

from typing import Any, Dict, List, Optional, Union


class SslSshProfile:
    """
    Wrapper for firewall ssl-ssh-profile API endpoint.

    Manages ssl-ssh-profile configuration with full Swagger-spec parameter support.
    """

    def __init__(self, http_client: Any):
        """
        Initialize the SslSshProfile wrapper.

        Args:
            http_client: The HTTP client for API communication
        """
        self._client = http_client
        self.path = "firewall/ssl-ssh-profile"

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
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a list of all ssl-ssh-profile entries.

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
            params["datasource"] = datasource
        if start is not None:
            params["start"] = start
        if count is not None:
            params["count"] = count
        if skip_to is not None:
            params["skip_to"] = skip_to
        if with_meta is not None:
            params["with_meta"] = with_meta
        if with_contents_hash is not None:
            params["with_contents_hash"] = with_contents_hash
        if skip is not None:
            params["skip"] = skip
        if format is not None:
            params["format"] = format
        if filter is not None:
            params["filter"] = filter
        if key is not None:
            params["key"] = key
        if pattern is not None:
            params["pattern"] = pattern
        if scope is not None:
            params["scope"] = scope
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if datasource_format is not None:
            params["datasource_format"] = datasource_format
        if unfiltered_count is not None:
            params["unfiltered_count"] = unfiltered_count
        if stat_items is not None:
            params["stat-items"] = stat_items
        if primary_keys is not None:
            params["primary_keys"] = primary_keys
        if action is not None:
            params["action"] = action
        if vdom is not None:
            params["vdom"] = vdom

        # Add any additional kwargs
        params.update(kwargs)

        # Extract vdom if present
        vdom = params.pop("vdom", None)

        return self._client.get("cmdb", self.path, params=params, vdom=vdom, raw_json=raw_json)

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
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Retrieve a specific ssl-ssh-profile entry by its name.

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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        nkey: Optional[Any] = None,
        scope: Optional[Any] = None,
        allowlist: Optional[str] = None,
        block_blocklisted_certificates: Optional[str] = None,
        caname: Optional[str] = None,
        comment: Optional[str] = None,
        dot: Optional[list] = None,
        ech_outer_sni: Optional[list] = None,
        ftps: Optional[list] = None,
        https: Optional[list] = None,
        imaps: Optional[list] = None,
        mapi_over_https: Optional[str] = None,
        name: Optional[str] = None,
        pop3s: Optional[list] = None,
        rpc_over_https: Optional[str] = None,
        server_cert: Optional[list] = None,
        server_cert_mode: Optional[str] = None,
        smtps: Optional[list] = None,
        ssh: Optional[list] = None,
        ssl: Optional[list] = None,
        ssl_anomaly_log: Optional[str] = None,
        ssl_exempt: Optional[list] = None,
        ssl_exemption_ip_rating: Optional[str] = None,
        ssl_exemption_log: Optional[str] = None,
        ssl_handshake_log: Optional[str] = None,
        ssl_negotiation_log: Optional[str] = None,
        ssl_server: Optional[list] = None,
        ssl_server_cert_log: Optional[str] = None,
        supported_alpn: Optional[str] = None,
        untrusted_caname: Optional[str] = None,
        use_ssl_server: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Create a new ssl-ssh-profile entry.

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

            allowlist (string) (enum: ['enable', 'disable']):
                Enable/disable exempting servers by FortiGuard allowlist.
            block-blocklisted-certificates (string) (enum: ['disable', 'enable']):
                Enable/disable blocking SSL-based botnet communication by Fo...
            caname (string) (max_len: 35):
                CA certificate used by SSL Inspection.
            comment (string) (max_len: 255):
                Optional comments.
            dot (list[object]):
                Configure DNS over TLS options.
            ech-outer-sni (list[object]):
                ClientHelloOuter SNIs to be blocked.
            ftps (list[object]):
                Configure FTPS options.
            https (list[object]):
                Configure HTTPS options.
            imaps (list[object]):
                Configure IMAPS options.
            mapi-over-https (string) (enum: ['enable', 'disable']):
                Enable/disable inspection of MAPI over HTTPS.
            name (string) (max_len: 47):
                Name.
            pop3s (list[object]):
                Configure POP3S options.
            rpc-over-https (string) (enum: ['enable', 'disable']):
                Enable/disable inspection of RPC over HTTPS.
            server-cert (list[object]):
                Certificate used by SSL Inspection to replace server certifi...
            server-cert-mode (string) (enum: ['re-sign', 'replace']):
                Re-sign or replace the server's certificate.
            smtps (list[object]):
                Configure SMTPS options.
            ssh (list[object]):
                Configure SSH options.
            ssl (list[object]):
                Configure SSL options.
            ssl-anomaly-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of SSL anomalies.
            ssl-exempt (list[object]):
                Servers to exempt from SSL inspection.
            ssl-exemption-ip-rating (string) (enum: ['enable', 'disable']):
                Enable/disable IP based URL rating.
            ssl-exemption-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of SSL exemptions.
            ssl-handshake-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of TLS handshakes.
            ssl-negotiation-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of SSL negotiation events.
            ssl-server (list[object]):
                SSL server settings used for client certificate request.
            ssl-server-cert-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of server certificate information.
            supported-alpn (string) (enum: ['http1-1', 'http2', 'all']):
                Configure ALPN option.
            untrusted-caname (string) (max_len: 35):
                Untrusted CA certificate used by SSL Inspection.
            use-ssl-server (string) (enum: ['disable', 'enable']):
                Enable/disable the use of SSL server table for SSL offloadin...

        Returns:
            API response dictionary
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            payload_dict = {}
        if allowlist is not None:
            payload_dict["allowlist"] = allowlist
        if block_blocklisted_certificates is not None:
            payload_dict["block-blocklisted-certificates"] = block_blocklisted_certificates
        if caname is not None:
            payload_dict["caname"] = caname
        if comment is not None:
            payload_dict["comment"] = comment
        if dot is not None:
            payload_dict["dot"] = dot
        if ech_outer_sni is not None:
            payload_dict["ech-outer-sni"] = ech_outer_sni
        if ftps is not None:
            payload_dict["ftps"] = ftps
        if https is not None:
            payload_dict["https"] = https
        if imaps is not None:
            payload_dict["imaps"] = imaps
        if mapi_over_https is not None:
            payload_dict["mapi-over-https"] = mapi_over_https
        if name is not None:
            payload_dict["name"] = name
        if pop3s is not None:
            payload_dict["pop3s"] = pop3s
        if rpc_over_https is not None:
            payload_dict["rpc-over-https"] = rpc_over_https
        if server_cert is not None:
            payload_dict["server-cert"] = server_cert
        if server_cert_mode is not None:
            payload_dict["server-cert-mode"] = server_cert_mode
        if smtps is not None:
            payload_dict["smtps"] = smtps
        if ssh is not None:
            payload_dict["ssh"] = ssh
        if ssl is not None:
            payload_dict["ssl"] = ssl
        if ssl_anomaly_log is not None:
            payload_dict["ssl-anomaly-log"] = ssl_anomaly_log
        if ssl_exempt is not None:
            payload_dict["ssl-exempt"] = ssl_exempt
        if ssl_exemption_ip_rating is not None:
            payload_dict["ssl-exemption-ip-rating"] = ssl_exemption_ip_rating
        if ssl_exemption_log is not None:
            payload_dict["ssl-exemption-log"] = ssl_exemption_log
        if ssl_handshake_log is not None:
            payload_dict["ssl-handshake-log"] = ssl_handshake_log
        if ssl_negotiation_log is not None:
            payload_dict["ssl-negotiation-log"] = ssl_negotiation_log
        if ssl_server is not None:
            payload_dict["ssl-server"] = ssl_server
        if ssl_server_cert_log is not None:
            payload_dict["ssl-server-cert-log"] = ssl_server_cert_log
        if supported_alpn is not None:
            payload_dict["supported-alpn"] = supported_alpn
        if untrusted_caname is not None:
            payload_dict["untrusted-caname"] = untrusted_caname
        if use_ssl_server is not None:
            payload_dict["use-ssl-server"] = use_ssl_server

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

    def update(
        self,
        mkey: Union[str, int],
        payload_dict: Optional[Dict[str, Any]] = None,
        vdom: Optional[Any] = None,
        action: Optional[Any] = None,
        before: Optional[Any] = None,
        after: Optional[Any] = None,
        scope: Optional[Any] = None,
        allowlist: Optional[str] = None,
        block_blocklisted_certificates: Optional[str] = None,
        caname: Optional[str] = None,
        comment: Optional[str] = None,
        dot: Optional[list] = None,
        ech_outer_sni: Optional[list] = None,
        ftps: Optional[list] = None,
        https: Optional[list] = None,
        imaps: Optional[list] = None,
        mapi_over_https: Optional[str] = None,
        name: Optional[str] = None,
        pop3s: Optional[list] = None,
        rpc_over_https: Optional[str] = None,
        server_cert: Optional[list] = None,
        server_cert_mode: Optional[str] = None,
        smtps: Optional[list] = None,
        ssh: Optional[list] = None,
        ssl: Optional[list] = None,
        ssl_anomaly_log: Optional[str] = None,
        ssl_exempt: Optional[list] = None,
        ssl_exemption_ip_rating: Optional[str] = None,
        ssl_exemption_log: Optional[str] = None,
        ssl_handshake_log: Optional[str] = None,
        ssl_negotiation_log: Optional[str] = None,
        ssl_server: Optional[list] = None,
        ssl_server_cert_log: Optional[str] = None,
        supported_alpn: Optional[str] = None,
        untrusted_caname: Optional[str] = None,
        use_ssl_server: Optional[str] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Update an existing ssl-ssh-profile entry.

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

            allowlist (string) (enum: ['enable', 'disable']):
                Enable/disable exempting servers by FortiGuard allowlist.
            block-blocklisted-certificates (string) (enum: ['disable', 'enable']):
                Enable/disable blocking SSL-based botnet communication by Fo...
            caname (string) (max_len: 35):
                CA certificate used by SSL Inspection.
            comment (string) (max_len: 255):
                Optional comments.
            dot (list[object]):
                Configure DNS over TLS options.
            ech-outer-sni (list[object]):
                ClientHelloOuter SNIs to be blocked.
            ftps (list[object]):
                Configure FTPS options.
            https (list[object]):
                Configure HTTPS options.
            imaps (list[object]):
                Configure IMAPS options.
            mapi-over-https (string) (enum: ['enable', 'disable']):
                Enable/disable inspection of MAPI over HTTPS.
            name (string) (max_len: 47):
                Name.
            pop3s (list[object]):
                Configure POP3S options.
            rpc-over-https (string) (enum: ['enable', 'disable']):
                Enable/disable inspection of RPC over HTTPS.
            server-cert (list[object]):
                Certificate used by SSL Inspection to replace server certifi...
            server-cert-mode (string) (enum: ['re-sign', 'replace']):
                Re-sign or replace the server's certificate.
            smtps (list[object]):
                Configure SMTPS options.
            ssh (list[object]):
                Configure SSH options.
            ssl (list[object]):
                Configure SSL options.
            ssl-anomaly-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of SSL anomalies.
            ssl-exempt (list[object]):
                Servers to exempt from SSL inspection.
            ssl-exemption-ip-rating (string) (enum: ['enable', 'disable']):
                Enable/disable IP based URL rating.
            ssl-exemption-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of SSL exemptions.
            ssl-handshake-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of TLS handshakes.
            ssl-negotiation-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of SSL negotiation events.
            ssl-server (list[object]):
                SSL server settings used for client certificate request.
            ssl-server-cert-log (string) (enum: ['disable', 'enable']):
                Enable/disable logging of server certificate information.
            supported-alpn (string) (enum: ['http1-1', 'http2', 'all']):
                Configure ALPN option.
            untrusted-caname (string) (max_len: 35):
                Untrusted CA certificate used by SSL Inspection.
            use-ssl-server (string) (enum: ['disable', 'enable']):
                Enable/disable the use of SSL server table for SSL offloadin...

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
        if allowlist is not None:
            payload_dict["allowlist"] = allowlist
        if block_blocklisted_certificates is not None:
            payload_dict["block-blocklisted-certificates"] = block_blocklisted_certificates
        if caname is not None:
            payload_dict["caname"] = caname
        if comment is not None:
            payload_dict["comment"] = comment
        if dot is not None:
            payload_dict["dot"] = dot
        if ech_outer_sni is not None:
            payload_dict["ech-outer-sni"] = ech_outer_sni
        if ftps is not None:
            payload_dict["ftps"] = ftps
        if https is not None:
            payload_dict["https"] = https
        if imaps is not None:
            payload_dict["imaps"] = imaps
        if mapi_over_https is not None:
            payload_dict["mapi-over-https"] = mapi_over_https
        if name is not None:
            payload_dict["name"] = name
        if pop3s is not None:
            payload_dict["pop3s"] = pop3s
        if rpc_over_https is not None:
            payload_dict["rpc-over-https"] = rpc_over_https
        if server_cert is not None:
            payload_dict["server-cert"] = server_cert
        if server_cert_mode is not None:
            payload_dict["server-cert-mode"] = server_cert_mode
        if smtps is not None:
            payload_dict["smtps"] = smtps
        if ssh is not None:
            payload_dict["ssh"] = ssh
        if ssl is not None:
            payload_dict["ssl"] = ssl
        if ssl_anomaly_log is not None:
            payload_dict["ssl-anomaly-log"] = ssl_anomaly_log
        if ssl_exempt is not None:
            payload_dict["ssl-exempt"] = ssl_exempt
        if ssl_exemption_ip_rating is not None:
            payload_dict["ssl-exemption-ip-rating"] = ssl_exemption_ip_rating
        if ssl_exemption_log is not None:
            payload_dict["ssl-exemption-log"] = ssl_exemption_log
        if ssl_handshake_log is not None:
            payload_dict["ssl-handshake-log"] = ssl_handshake_log
        if ssl_negotiation_log is not None:
            payload_dict["ssl-negotiation-log"] = ssl_negotiation_log
        if ssl_server is not None:
            payload_dict["ssl-server"] = ssl_server
        if ssl_server_cert_log is not None:
            payload_dict["ssl-server-cert-log"] = ssl_server_cert_log
        if supported_alpn is not None:
            payload_dict["supported-alpn"] = supported_alpn
        if untrusted_caname is not None:
            payload_dict["untrusted-caname"] = untrusted_caname
        if use_ssl_server is not None:
            payload_dict["use-ssl-server"] = use_ssl_server

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
            f"{self.path}/{mkey_str}",
            data=payload_dict,
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        mkey: Union[str, int],
        vdom: Optional[Any] = None,
        scope: Optional[Any] = None,
        raw_json: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete a ssl-ssh-profile entry.

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
            "cmdb", f"{self.path}/{mkey_str}", params=params, vdom=vdom, raw_json=raw_json
        )
