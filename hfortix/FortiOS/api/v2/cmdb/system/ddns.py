"""
FortiOS CMDB - Cmdb System Ddns

Configuration endpoint for managing cmdb system ddns objects.

API Endpoints:
    GET    /cmdb/system/ddns
    POST   /cmdb/system/ddns
    GET    /cmdb/system/ddns
    PUT    /cmdb/system/ddns/{identifier}
    DELETE /cmdb/system/ddns/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.ddns.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.ddns.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.ddns.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.ddns.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.ddns.delete(name="item_name")

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


class Ddns:
    """
    Ddns Operations.

    Provides CRUD operations for FortiOS ddns configuration.

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
        Initialize Ddns endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ddnsid: str | None = None,
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
            ddnsid: Object identifier (optional for list, required for
            specific)
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
        if ddnsid:
            endpoint = f"/system/ddns/{ddnsid}"
        else:
            endpoint = "/system/ddns"
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
        ddnsid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        ddns_server: str | None = None,
        addr_type: str | None = None,
        server_type: str | None = None,
        ddns_server_addr: list | None = None,
        ddns_zone: str | None = None,
        ddns_ttl: int | None = None,
        ddns_auth: str | None = None,
        ddns_keyname: str | None = None,
        ddns_key: str | None = None,
        ddns_domain: str | None = None,
        ddns_username: str | None = None,
        ddns_sn: str | None = None,
        ddns_password: str | None = None,
        use_public_ip: str | None = None,
        update_interval: int | None = None,
        clear_text: str | None = None,
        ssl_certificate: str | None = None,
        bound_ip: str | None = None,
        monitor_interface: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            ddnsid: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            ddnsid: DDNS ID. (optional)
            ddns_server: Select a DDNS service provider. (optional)
            addr_type: Address type of interface address in DDNS update.
            (optional)
            server_type: Address type of the DDNS server. (optional)
            ddns_server_addr: Generic DDNS server IP/FQDN list. (optional)
            ddns_zone: Zone of your domain name (for example, DDNS.com).
            (optional)
            ddns_ttl: Time-to-live for DDNS packets. (optional)
            ddns_auth: Enable/disable TSIG authentication for your DDNS server.
            (optional)
            ddns_keyname: DDNS update key name. (optional)
            ddns_key: DDNS update key (base 64 encoding). (optional)
            ddns_domain: Your fully qualified domain name. For example,
            yourname.ddns.com. (optional)
            ddns_username: DDNS user name. (optional)
            ddns_sn: DDNS Serial Number. (optional)
            ddns_password: DDNS password. (optional)
            use_public_ip: Enable/disable use of public IP address. (optional)
            update_interval: DDNS update interval (60 - 2592000 sec, 0 means
            default). (optional)
            clear_text: Enable/disable use of clear text connections.
            (optional)
            ssl_certificate: Name of local certificate for SSL connections.
            (optional)
            bound_ip: Bound IP address. (optional)
            monitor_interface: Monitored interface. (optional)
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
        if not ddnsid:
            raise ValueError("ddnsid is required for put()")
        endpoint = f"/system/ddns/{ddnsid}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if ddnsid is not None:
            data_payload["ddnsid"] = ddnsid
        if ddns_server is not None:
            data_payload["ddns-server"] = ddns_server
        if addr_type is not None:
            data_payload["addr-type"] = addr_type
        if server_type is not None:
            data_payload["server-type"] = server_type
        if ddns_server_addr is not None:
            data_payload["ddns-server-addr"] = ddns_server_addr
        if ddns_zone is not None:
            data_payload["ddns-zone"] = ddns_zone
        if ddns_ttl is not None:
            data_payload["ddns-ttl"] = ddns_ttl
        if ddns_auth is not None:
            data_payload["ddns-auth"] = ddns_auth
        if ddns_keyname is not None:
            data_payload["ddns-keyname"] = ddns_keyname
        if ddns_key is not None:
            data_payload["ddns-key"] = ddns_key
        if ddns_domain is not None:
            data_payload["ddns-domain"] = ddns_domain
        if ddns_username is not None:
            data_payload["ddns-username"] = ddns_username
        if ddns_sn is not None:
            data_payload["ddns-sn"] = ddns_sn
        if ddns_password is not None:
            data_payload["ddns-password"] = ddns_password
        if use_public_ip is not None:
            data_payload["use-public-ip"] = use_public_ip
        if update_interval is not None:
            data_payload["update-interval"] = update_interval
        if clear_text is not None:
            data_payload["clear-text"] = clear_text
        if ssl_certificate is not None:
            data_payload["ssl-certificate"] = ssl_certificate
        if bound_ip is not None:
            data_payload["bound-ip"] = bound_ip
        if monitor_interface is not None:
            data_payload["monitor-interface"] = monitor_interface
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        ddnsid: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            ddnsid: Object identifier (required)
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
        if not ddnsid:
            raise ValueError("ddnsid is required for delete()")
        endpoint = f"/system/ddns/{ddnsid}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        ddnsid: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            ddnsid: Object identifier
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
        result = self.get(ddnsid=ddnsid, vdom=vdom)

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
        ddnsid: int | None = None,
        ddns_server: str | None = None,
        addr_type: str | None = None,
        server_type: str | None = None,
        ddns_server_addr: list | None = None,
        ddns_zone: str | None = None,
        ddns_ttl: int | None = None,
        ddns_auth: str | None = None,
        ddns_keyname: str | None = None,
        ddns_key: str | None = None,
        ddns_domain: str | None = None,
        ddns_username: str | None = None,
        ddns_sn: str | None = None,
        ddns_password: str | None = None,
        use_public_ip: str | None = None,
        update_interval: int | None = None,
        clear_text: str | None = None,
        ssl_certificate: str | None = None,
        bound_ip: str | None = None,
        monitor_interface: list | None = None,
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
            ddnsid: DDNS ID. (optional)
            ddns_server: Select a DDNS service provider. (optional)
            addr_type: Address type of interface address in DDNS update.
            (optional)
            server_type: Address type of the DDNS server. (optional)
            ddns_server_addr: Generic DDNS server IP/FQDN list. (optional)
            ddns_zone: Zone of your domain name (for example, DDNS.com).
            (optional)
            ddns_ttl: Time-to-live for DDNS packets. (optional)
            ddns_auth: Enable/disable TSIG authentication for your DDNS server.
            (optional)
            ddns_keyname: DDNS update key name. (optional)
            ddns_key: DDNS update key (base 64 encoding). (optional)
            ddns_domain: Your fully qualified domain name. For example,
            yourname.ddns.com. (optional)
            ddns_username: DDNS user name. (optional)
            ddns_sn: DDNS Serial Number. (optional)
            ddns_password: DDNS password. (optional)
            use_public_ip: Enable/disable use of public IP address. (optional)
            update_interval: DDNS update interval (60 - 2592000 sec, 0 means
            default). (optional)
            clear_text: Enable/disable use of clear text connections.
            (optional)
            ssl_certificate: Name of local certificate for SSL connections.
            (optional)
            bound_ip: Bound IP address. (optional)
            monitor_interface: Monitored interface. (optional)
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
        endpoint = "/system/ddns"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if ddnsid is not None:
            data_payload["ddnsid"] = ddnsid
        if ddns_server is not None:
            data_payload["ddns-server"] = ddns_server
        if addr_type is not None:
            data_payload["addr-type"] = addr_type
        if server_type is not None:
            data_payload["server-type"] = server_type
        if ddns_server_addr is not None:
            data_payload["ddns-server-addr"] = ddns_server_addr
        if ddns_zone is not None:
            data_payload["ddns-zone"] = ddns_zone
        if ddns_ttl is not None:
            data_payload["ddns-ttl"] = ddns_ttl
        if ddns_auth is not None:
            data_payload["ddns-auth"] = ddns_auth
        if ddns_keyname is not None:
            data_payload["ddns-keyname"] = ddns_keyname
        if ddns_key is not None:
            data_payload["ddns-key"] = ddns_key
        if ddns_domain is not None:
            data_payload["ddns-domain"] = ddns_domain
        if ddns_username is not None:
            data_payload["ddns-username"] = ddns_username
        if ddns_sn is not None:
            data_payload["ddns-sn"] = ddns_sn
        if ddns_password is not None:
            data_payload["ddns-password"] = ddns_password
        if use_public_ip is not None:
            data_payload["use-public-ip"] = use_public_ip
        if update_interval is not None:
            data_payload["update-interval"] = update_interval
        if clear_text is not None:
            data_payload["clear-text"] = clear_text
        if ssl_certificate is not None:
            data_payload["ssl-certificate"] = ssl_certificate
        if bound_ip is not None:
            data_payload["bound-ip"] = bound_ip
        if monitor_interface is not None:
            data_payload["monitor-interface"] = monitor_interface
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
