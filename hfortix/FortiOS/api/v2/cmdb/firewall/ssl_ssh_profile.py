"""
FortiOS CMDB - Cmdb Firewall Ssl Ssh Profile

Configuration endpoint for managing cmdb firewall ssl ssh profile objects.

API Endpoints:
    GET    /cmdb/firewall/ssl_ssh_profile
    POST   /cmdb/firewall/ssl_ssh_profile
    GET    /cmdb/firewall/ssl_ssh_profile
    PUT    /cmdb/firewall/ssl_ssh_profile/{identifier}
    DELETE /cmdb/firewall/ssl_ssh_profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.ssl_ssh_profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.ssl_ssh_profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.ssl_ssh_profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.ssl_ssh_profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.ssl_ssh_profile.delete(name="item_name")

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


class SslSshProfile:
    """
    Sslsshprofile Operations.

    Provides CRUD operations for FortiOS sslsshprofile configuration.

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
        Initialize SslSshProfile endpoint.

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
            endpoint = f"/firewall/ssl-ssh-profile/{name}"
        else:
            endpoint = "/firewall/ssl-ssh-profile"
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
        comment: str | None = None,
        ssl: list | None = None,
        https: list | None = None,
        ftps: list | None = None,
        imaps: list | None = None,
        pop3s: list | None = None,
        smtps: list | None = None,
        ssh: list | None = None,
        dot: list | None = None,
        allowlist: str | None = None,
        block_blocklisted_certificates: str | None = None,
        ssl_exempt: list | None = None,
        ech_outer_sni: list | None = None,
        server_cert_mode: str | None = None,
        use_ssl_server: str | None = None,
        caname: str | None = None,
        untrusted_caname: str | None = None,
        server_cert: list | None = None,
        ssl_server: list | None = None,
        ssl_exemption_ip_rating: str | None = None,
        ssl_exemption_log: str | None = None,
        ssl_anomaly_log: str | None = None,
        ssl_negotiation_log: str | None = None,
        ssl_server_cert_log: str | None = None,
        ssl_handshake_log: str | None = None,
        rpc_over_https: str | None = None,
        mapi_over_https: str | None = None,
        supported_alpn: str | None = None,
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
            name: Name. (optional)
            comment: Optional comments. (optional)
            ssl: Configure SSL options. (optional)
            https: Configure HTTPS options. (optional)
            ftps: Configure FTPS options. (optional)
            imaps: Configure IMAPS options. (optional)
            pop3s: Configure POP3S options. (optional)
            smtps: Configure SMTPS options. (optional)
            ssh: Configure SSH options. (optional)
            dot: Configure DNS over TLS options. (optional)
            allowlist: Enable/disable exempting servers by FortiGuard
            allowlist. (optional)
            block_blocklisted_certificates: Enable/disable blocking SSL-based
            botnet communication by FortiGuard certificate blocklist.
            (optional)
            ssl_exempt: Servers to exempt from SSL inspection. (optional)
            ech_outer_sni: ClientHelloOuter SNIs to be blocked. (optional)
            server_cert_mode: Re-sign or replace the server's certificate.
            (optional)
            use_ssl_server: Enable/disable the use of SSL server table for SSL
            offloading. (optional)
            caname: CA certificate used by SSL Inspection. (optional)
            untrusted_caname: Untrusted CA certificate used by SSL Inspection.
            (optional)
            server_cert: Certificate used by SSL Inspection to replace server
            certificate. (optional)
            ssl_server: SSL server settings used for client certificate
            request. (optional)
            ssl_exemption_ip_rating: Enable/disable IP based URL rating.
            (optional)
            ssl_exemption_log: Enable/disable logging of SSL exemptions.
            (optional)
            ssl_anomaly_log: Enable/disable logging of SSL anomalies.
            (optional)
            ssl_negotiation_log: Enable/disable logging of SSL negotiation
            events. (optional)
            ssl_server_cert_log: Enable/disable logging of server certificate
            information. (optional)
            ssl_handshake_log: Enable/disable logging of TLS handshakes.
            (optional)
            rpc_over_https: Enable/disable inspection of RPC over HTTPS.
            (optional)
            mapi_over_https: Enable/disable inspection of MAPI over HTTPS.
            (optional)
            supported_alpn: Configure ALPN option. (optional)
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
        endpoint = f"/firewall/ssl-ssh-profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if ssl is not None:
            data_payload["ssl"] = ssl
        if https is not None:
            data_payload["https"] = https
        if ftps is not None:
            data_payload["ftps"] = ftps
        if imaps is not None:
            data_payload["imaps"] = imaps
        if pop3s is not None:
            data_payload["pop3s"] = pop3s
        if smtps is not None:
            data_payload["smtps"] = smtps
        if ssh is not None:
            data_payload["ssh"] = ssh
        if dot is not None:
            data_payload["dot"] = dot
        if allowlist is not None:
            data_payload["allowlist"] = allowlist
        if block_blocklisted_certificates is not None:
            data_payload["block-blocklisted-certificates"] = (
                block_blocklisted_certificates
            )
        if ssl_exempt is not None:
            data_payload["ssl-exempt"] = ssl_exempt
        if ech_outer_sni is not None:
            data_payload["ech-outer-sni"] = ech_outer_sni
        if server_cert_mode is not None:
            data_payload["server-cert-mode"] = server_cert_mode
        if use_ssl_server is not None:
            data_payload["use-ssl-server"] = use_ssl_server
        if caname is not None:
            data_payload["caname"] = caname
        if untrusted_caname is not None:
            data_payload["untrusted-caname"] = untrusted_caname
        if server_cert is not None:
            data_payload["server-cert"] = server_cert
        if ssl_server is not None:
            data_payload["ssl-server"] = ssl_server
        if ssl_exemption_ip_rating is not None:
            data_payload["ssl-exemption-ip-rating"] = ssl_exemption_ip_rating
        if ssl_exemption_log is not None:
            data_payload["ssl-exemption-log"] = ssl_exemption_log
        if ssl_anomaly_log is not None:
            data_payload["ssl-anomaly-log"] = ssl_anomaly_log
        if ssl_negotiation_log is not None:
            data_payload["ssl-negotiation-log"] = ssl_negotiation_log
        if ssl_server_cert_log is not None:
            data_payload["ssl-server-cert-log"] = ssl_server_cert_log
        if ssl_handshake_log is not None:
            data_payload["ssl-handshake-log"] = ssl_handshake_log
        if rpc_over_https is not None:
            data_payload["rpc-over-https"] = rpc_over_https
        if mapi_over_https is not None:
            data_payload["mapi-over-https"] = mapi_over_https
        if supported_alpn is not None:
            data_payload["supported-alpn"] = supported_alpn
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
        endpoint = f"/firewall/ssl-ssh-profile/{name}"
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
        comment: str | None = None,
        ssl: list | None = None,
        https: list | None = None,
        ftps: list | None = None,
        imaps: list | None = None,
        pop3s: list | None = None,
        smtps: list | None = None,
        ssh: list | None = None,
        dot: list | None = None,
        allowlist: str | None = None,
        block_blocklisted_certificates: str | None = None,
        ssl_exempt: list | None = None,
        ech_outer_sni: list | None = None,
        server_cert_mode: str | None = None,
        use_ssl_server: str | None = None,
        caname: str | None = None,
        untrusted_caname: str | None = None,
        server_cert: list | None = None,
        ssl_server: list | None = None,
        ssl_exemption_ip_rating: str | None = None,
        ssl_exemption_log: str | None = None,
        ssl_anomaly_log: str | None = None,
        ssl_negotiation_log: str | None = None,
        ssl_server_cert_log: str | None = None,
        ssl_handshake_log: str | None = None,
        rpc_over_https: str | None = None,
        mapi_over_https: str | None = None,
        supported_alpn: str | None = None,
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
            name: Name. (optional)
            comment: Optional comments. (optional)
            ssl: Configure SSL options. (optional)
            https: Configure HTTPS options. (optional)
            ftps: Configure FTPS options. (optional)
            imaps: Configure IMAPS options. (optional)
            pop3s: Configure POP3S options. (optional)
            smtps: Configure SMTPS options. (optional)
            ssh: Configure SSH options. (optional)
            dot: Configure DNS over TLS options. (optional)
            allowlist: Enable/disable exempting servers by FortiGuard
            allowlist. (optional)
            block_blocklisted_certificates: Enable/disable blocking SSL-based
            botnet communication by FortiGuard certificate blocklist.
            (optional)
            ssl_exempt: Servers to exempt from SSL inspection. (optional)
            ech_outer_sni: ClientHelloOuter SNIs to be blocked. (optional)
            server_cert_mode: Re-sign or replace the server's certificate.
            (optional)
            use_ssl_server: Enable/disable the use of SSL server table for SSL
            offloading. (optional)
            caname: CA certificate used by SSL Inspection. (optional)
            untrusted_caname: Untrusted CA certificate used by SSL Inspection.
            (optional)
            server_cert: Certificate used by SSL Inspection to replace server
            certificate. (optional)
            ssl_server: SSL server settings used for client certificate
            request. (optional)
            ssl_exemption_ip_rating: Enable/disable IP based URL rating.
            (optional)
            ssl_exemption_log: Enable/disable logging of SSL exemptions.
            (optional)
            ssl_anomaly_log: Enable/disable logging of SSL anomalies.
            (optional)
            ssl_negotiation_log: Enable/disable logging of SSL negotiation
            events. (optional)
            ssl_server_cert_log: Enable/disable logging of server certificate
            information. (optional)
            ssl_handshake_log: Enable/disable logging of TLS handshakes.
            (optional)
            rpc_over_https: Enable/disable inspection of RPC over HTTPS.
            (optional)
            mapi_over_https: Enable/disable inspection of MAPI over HTTPS.
            (optional)
            supported_alpn: Configure ALPN option. (optional)
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
        endpoint = "/firewall/ssl-ssh-profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if ssl is not None:
            data_payload["ssl"] = ssl
        if https is not None:
            data_payload["https"] = https
        if ftps is not None:
            data_payload["ftps"] = ftps
        if imaps is not None:
            data_payload["imaps"] = imaps
        if pop3s is not None:
            data_payload["pop3s"] = pop3s
        if smtps is not None:
            data_payload["smtps"] = smtps
        if ssh is not None:
            data_payload["ssh"] = ssh
        if dot is not None:
            data_payload["dot"] = dot
        if allowlist is not None:
            data_payload["allowlist"] = allowlist
        if block_blocklisted_certificates is not None:
            data_payload["block-blocklisted-certificates"] = (
                block_blocklisted_certificates
            )
        if ssl_exempt is not None:
            data_payload["ssl-exempt"] = ssl_exempt
        if ech_outer_sni is not None:
            data_payload["ech-outer-sni"] = ech_outer_sni
        if server_cert_mode is not None:
            data_payload["server-cert-mode"] = server_cert_mode
        if use_ssl_server is not None:
            data_payload["use-ssl-server"] = use_ssl_server
        if caname is not None:
            data_payload["caname"] = caname
        if untrusted_caname is not None:
            data_payload["untrusted-caname"] = untrusted_caname
        if server_cert is not None:
            data_payload["server-cert"] = server_cert
        if ssl_server is not None:
            data_payload["ssl-server"] = ssl_server
        if ssl_exemption_ip_rating is not None:
            data_payload["ssl-exemption-ip-rating"] = ssl_exemption_ip_rating
        if ssl_exemption_log is not None:
            data_payload["ssl-exemption-log"] = ssl_exemption_log
        if ssl_anomaly_log is not None:
            data_payload["ssl-anomaly-log"] = ssl_anomaly_log
        if ssl_negotiation_log is not None:
            data_payload["ssl-negotiation-log"] = ssl_negotiation_log
        if ssl_server_cert_log is not None:
            data_payload["ssl-server-cert-log"] = ssl_server_cert_log
        if ssl_handshake_log is not None:
            data_payload["ssl-handshake-log"] = ssl_handshake_log
        if rpc_over_https is not None:
            data_payload["rpc-over-https"] = rpc_over_https
        if mapi_over_https is not None:
            data_payload["mapi-over-https"] = mapi_over_https
        if supported_alpn is not None:
            data_payload["supported-alpn"] = supported_alpn
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
