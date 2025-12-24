"""
FortiOS CMDB - Cmdb Firewall Ldb Monitor

Configuration endpoint for managing cmdb firewall ldb monitor objects.

API Endpoints:
    GET    /cmdb/firewall/ldb_monitor
    POST   /cmdb/firewall/ldb_monitor
    GET    /cmdb/firewall/ldb_monitor
    PUT    /cmdb/firewall/ldb_monitor/{identifier}
    DELETE /cmdb/firewall/ldb_monitor/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.ldb_monitor.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.ldb_monitor.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.ldb_monitor.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.ldb_monitor.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.ldb_monitor.delete(name="item_name")

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


class LdbMonitor:
    """
    Ldbmonitor Operations.

    Provides CRUD operations for FortiOS ldbmonitor configuration.

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
        Initialize LdbMonitor endpoint.

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
            endpoint = f"/firewall/ldb-monitor/{name}"
        else:
            endpoint = "/firewall/ldb-monitor"
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
        type: str | None = None,
        interval: int | None = None,
        timeout: int | None = None,
        retry: int | None = None,
        port: int | None = None,
        src_ip: str | None = None,
        http_get: str | None = None,
        http_match: str | None = None,
        http_max_redirects: int | None = None,
        dns_protocol: str | None = None,
        dns_request_domain: str | None = None,
        dns_match_ip: str | None = None,
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
            name: Monitor name. (optional)
            type: Select the Monitor type used by the health check monitor to
            check the health of the server (PING | TCP | HTTP | HTTPS | DNS).
            (optional)
            interval: Time between health checks (5 - 65535 sec, default = 10).
            (optional)
            timeout: Time to wait to receive response to a health check from a
            server. Reaching the timeout means the health check failed (1 - 255
            sec, default = 2). (optional)
            retry: Number health check attempts before the server is considered
            down (1 - 255, default = 3). (optional)
            port: Service port used to perform the health check. If 0, health
            check monitor inherits port configured for the server (0 - 65535,
            default = 0). (optional)
            src_ip: Source IP for ldb-monitor. (optional)
            http_get: Request URI used to send a GET request to check the
            health of an HTTP server. Optionally provide a hostname before the
            first '/' and it will be used as the HTTP Host Header. (optional)
            http_match: String to match the value expected in response to an
            HTTP-GET request. (optional)
            http_max_redirects: The maximum number of HTTP redirects to be
            allowed (0 - 5, default = 0). (optional)
            dns_protocol: Select the protocol used by the DNS health check
            monitor to check the health of the server (UDP | TCP). (optional)
            dns_request_domain: Fully qualified domain name to resolve for the
            DNS probe. (optional)
            dns_match_ip: Response IP expected from DNS server. (optional)
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
        endpoint = f"/firewall/ldb-monitor/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if type is not None:
            data_payload["type"] = type
        if interval is not None:
            data_payload["interval"] = interval
        if timeout is not None:
            data_payload["timeout"] = timeout
        if retry is not None:
            data_payload["retry"] = retry
        if port is not None:
            data_payload["port"] = port
        if src_ip is not None:
            data_payload["src-ip"] = src_ip
        if http_get is not None:
            data_payload["http-get"] = http_get
        if http_match is not None:
            data_payload["http-match"] = http_match
        if http_max_redirects is not None:
            data_payload["http-max-redirects"] = http_max_redirects
        if dns_protocol is not None:
            data_payload["dns-protocol"] = dns_protocol
        if dns_request_domain is not None:
            data_payload["dns-request-domain"] = dns_request_domain
        if dns_match_ip is not None:
            data_payload["dns-match-ip"] = dns_match_ip
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
        endpoint = f"/firewall/ldb-monitor/{name}"
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
        type: str | None = None,
        interval: int | None = None,
        timeout: int | None = None,
        retry: int | None = None,
        port: int | None = None,
        src_ip: str | None = None,
        http_get: str | None = None,
        http_match: str | None = None,
        http_max_redirects: int | None = None,
        dns_protocol: str | None = None,
        dns_request_domain: str | None = None,
        dns_match_ip: str | None = None,
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
            name: Monitor name. (optional)
            type: Select the Monitor type used by the health check monitor to
            check the health of the server (PING | TCP | HTTP | HTTPS | DNS).
            (optional)
            interval: Time between health checks (5 - 65535 sec, default = 10).
            (optional)
            timeout: Time to wait to receive response to a health check from a
            server. Reaching the timeout means the health check failed (1 - 255
            sec, default = 2). (optional)
            retry: Number health check attempts before the server is considered
            down (1 - 255, default = 3). (optional)
            port: Service port used to perform the health check. If 0, health
            check monitor inherits port configured for the server (0 - 65535,
            default = 0). (optional)
            src_ip: Source IP for ldb-monitor. (optional)
            http_get: Request URI used to send a GET request to check the
            health of an HTTP server. Optionally provide a hostname before the
            first '/' and it will be used as the HTTP Host Header. (optional)
            http_match: String to match the value expected in response to an
            HTTP-GET request. (optional)
            http_max_redirects: The maximum number of HTTP redirects to be
            allowed (0 - 5, default = 0). (optional)
            dns_protocol: Select the protocol used by the DNS health check
            monitor to check the health of the server (UDP | TCP). (optional)
            dns_request_domain: Fully qualified domain name to resolve for the
            DNS probe. (optional)
            dns_match_ip: Response IP expected from DNS server. (optional)
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
        endpoint = "/firewall/ldb-monitor"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if type is not None:
            data_payload["type"] = type
        if interval is not None:
            data_payload["interval"] = interval
        if timeout is not None:
            data_payload["timeout"] = timeout
        if retry is not None:
            data_payload["retry"] = retry
        if port is not None:
            data_payload["port"] = port
        if src_ip is not None:
            data_payload["src-ip"] = src_ip
        if http_get is not None:
            data_payload["http-get"] = http_get
        if http_match is not None:
            data_payload["http-match"] = http_match
        if http_max_redirects is not None:
            data_payload["http-max-redirects"] = http_max_redirects
        if dns_protocol is not None:
            data_payload["dns-protocol"] = dns_protocol
        if dns_request_domain is not None:
            data_payload["dns-request-domain"] = dns_request_domain
        if dns_match_ip is not None:
            data_payload["dns-match-ip"] = dns_match_ip
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
