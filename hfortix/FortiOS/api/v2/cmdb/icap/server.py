"""
FortiOS CMDB - Cmdb Icap Server

Configuration endpoint for managing cmdb icap server objects.

API Endpoints:
    GET    /cmdb/icap/server
    POST   /cmdb/icap/server
    GET    /cmdb/icap/server
    PUT    /cmdb/icap/server/{identifier}
    DELETE /cmdb/icap/server/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.icap.server.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.icap.server.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.icap.server.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.icap.server.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.icap.server.delete(name="item_name")

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


class Server:
    """
    Server Operations.

    Provides CRUD operations for FortiOS server configuration.

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
        Initialize Server endpoint.

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
            endpoint = f"/icap/server/{name}"
        else:
            endpoint = "/icap/server"
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
        addr_type: str | None = None,
        ip_address: str | None = None,
        ip6_address: str | None = None,
        fqdn: str | None = None,
        port: int | None = None,
        max_connections: int | None = None,
        secure: str | None = None,
        ssl_cert: str | None = None,
        healthcheck: str | None = None,
        healthcheck_service: str | None = None,
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
            name: Server name. (optional)
            addr_type: Address type of the remote ICAP server: IPv4, IPv6 or
            FQDN. (optional)
            ip_address: IPv4 address of the ICAP server. (optional)
            ip6_address: IPv6 address of the ICAP server. (optional)
            fqdn: ICAP remote server Fully Qualified Domain Name (FQDN).
            (optional)
            port: ICAP server port. (optional)
            max_connections: Maximum number of concurrent connections to ICAP
            server (unlimited = 0, default = 100). Must not be less than
            wad-worker-count. (optional)
            secure: Enable/disable secure connection to ICAP server. (optional)
            ssl_cert: CA certificate name. (optional)
            healthcheck: Enable/disable ICAP remote server health checking.
            Attempts to connect to the remote ICAP server to verify that the
            server is operating normally. (optional)
            healthcheck_service: ICAP Service name to use for health checks.
            (optional)
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
        endpoint = f"/icap/server/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if addr_type is not None:
            data_payload["addr-type"] = addr_type
        if ip_address is not None:
            data_payload["ip-address"] = ip_address
        if ip6_address is not None:
            data_payload["ip6-address"] = ip6_address
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if port is not None:
            data_payload["port"] = port
        if max_connections is not None:
            data_payload["max-connections"] = max_connections
        if secure is not None:
            data_payload["secure"] = secure
        if ssl_cert is not None:
            data_payload["ssl-cert"] = ssl_cert
        if healthcheck is not None:
            data_payload["healthcheck"] = healthcheck
        if healthcheck_service is not None:
            data_payload["healthcheck-service"] = healthcheck_service
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
        endpoint = f"/icap/server/{name}"
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
        addr_type: str | None = None,
        ip_address: str | None = None,
        ip6_address: str | None = None,
        fqdn: str | None = None,
        port: int | None = None,
        max_connections: int | None = None,
        secure: str | None = None,
        ssl_cert: str | None = None,
        healthcheck: str | None = None,
        healthcheck_service: str | None = None,
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
            name: Server name. (optional)
            addr_type: Address type of the remote ICAP server: IPv4, IPv6 or
            FQDN. (optional)
            ip_address: IPv4 address of the ICAP server. (optional)
            ip6_address: IPv6 address of the ICAP server. (optional)
            fqdn: ICAP remote server Fully Qualified Domain Name (FQDN).
            (optional)
            port: ICAP server port. (optional)
            max_connections: Maximum number of concurrent connections to ICAP
            server (unlimited = 0, default = 100). Must not be less than
            wad-worker-count. (optional)
            secure: Enable/disable secure connection to ICAP server. (optional)
            ssl_cert: CA certificate name. (optional)
            healthcheck: Enable/disable ICAP remote server health checking.
            Attempts to connect to the remote ICAP server to verify that the
            server is operating normally. (optional)
            healthcheck_service: ICAP Service name to use for health checks.
            (optional)
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
        endpoint = "/icap/server"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if addr_type is not None:
            data_payload["addr-type"] = addr_type
        if ip_address is not None:
            data_payload["ip-address"] = ip_address
        if ip6_address is not None:
            data_payload["ip6-address"] = ip6_address
        if fqdn is not None:
            data_payload["fqdn"] = fqdn
        if port is not None:
            data_payload["port"] = port
        if max_connections is not None:
            data_payload["max-connections"] = max_connections
        if secure is not None:
            data_payload["secure"] = secure
        if ssl_cert is not None:
            data_payload["ssl-cert"] = ssl_cert
        if healthcheck is not None:
            data_payload["healthcheck"] = healthcheck
        if healthcheck_service is not None:
            data_payload["healthcheck-service"] = healthcheck_service
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
