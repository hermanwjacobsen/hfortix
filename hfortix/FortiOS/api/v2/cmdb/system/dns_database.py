"""
FortiOS CMDB - Cmdb System Dns Database

Configuration endpoint for managing cmdb system dns database objects.

API Endpoints:
    GET    /cmdb/system/dns_database
    POST   /cmdb/system/dns_database
    GET    /cmdb/system/dns_database
    PUT    /cmdb/system/dns_database/{identifier}
    DELETE /cmdb/system/dns_database/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.dns_database.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.dns_database.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.dns_database.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.dns_database.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.dns_database.delete(name="item_name")

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


class DnsDatabase:
    """
    Dnsdatabase Operations.

    Provides CRUD operations for FortiOS dnsdatabase configuration.

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
        Initialize DnsDatabase endpoint.

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
            endpoint = f"/system/dns-database/{name}"
        else:
            endpoint = "/system/dns-database"
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
        status: str | None = None,
        domain: str | None = None,
        allow_transfer: str | None = None,
        type: str | None = None,
        view: str | None = None,
        ip_primary: str | None = None,
        primary_name: str | None = None,
        contact: str | None = None,
        ttl: int | None = None,
        authoritative: str | None = None,
        forwarder: str | None = None,
        forwarder6: str | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        source_ip_interface: str | None = None,
        rr_max: int | None = None,
        dns_entry: list | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            name: Zone name. (optional)
            status: Enable/disable this DNS zone. (optional)
            domain: Domain name. (optional)
            allow_transfer: DNS zone transfer IP address list. (optional)
            type: Zone type (primary to manage entries directly, secondary to
            import entries from other zones). (optional)
            view: Zone view (public to serve public clients, shadow to serve
            internal clients). (optional)
            ip_primary: IP address of primary DNS server. Entries in this
            primary DNS server and imported into the DNS zone. (optional)
            primary_name: Domain name of the default DNS server for this zone.
            (optional)
            contact: Email address of the administrator for this zone. You can
            specify only the username, such as admin or the full email address,
            such as admin@test.com When using only a username, the domain of
            the email will be this zone. (optional)
            ttl: Default time-to-live value for the entries of this DNS zone (0
            - 2147483647 sec, default = 86400). (optional)
            authoritative: Enable/disable authoritative zone. (optional)
            forwarder: DNS zone forwarder IP address list. (optional)
            forwarder6: Forwarder IPv6 address. (optional)
            source_ip: Source IP for forwarding to DNS server. (optional)
            source_ip6: IPv6 source IP address for forwarding to DNS server.
            (optional)
            source_ip_interface: IP address of the specified interface as the
            source IP address. (optional)
            rr_max: Maximum number of resource records (10 - 65536, 0 means
            infinite). (optional)
            dns_entry: DNS entry. (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = f"/system/dns-database/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if domain is not None:
            data_payload["domain"] = domain
        if allow_transfer is not None:
            data_payload["allow-transfer"] = allow_transfer
        if type is not None:
            data_payload["type"] = type
        if view is not None:
            data_payload["view"] = view
        if ip_primary is not None:
            data_payload["ip-primary"] = ip_primary
        if primary_name is not None:
            data_payload["primary-name"] = primary_name
        if contact is not None:
            data_payload["contact"] = contact
        if ttl is not None:
            data_payload["ttl"] = ttl
        if authoritative is not None:
            data_payload["authoritative"] = authoritative
        if forwarder is not None:
            data_payload["forwarder"] = forwarder
        if forwarder6 is not None:
            data_payload["forwarder6"] = forwarder6
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip6 is not None:
            data_payload["source-ip6"] = source_ip6
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if rr_max is not None:
            data_payload["rr-max"] = rr_max
        if dns_entry is not None:
            data_payload["dns-entry"] = dns_entry
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
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
        endpoint = f"/system/dns-database/{name}"
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
        status: str | None = None,
        domain: str | None = None,
        allow_transfer: str | None = None,
        type: str | None = None,
        view: str | None = None,
        ip_primary: str | None = None,
        primary_name: str | None = None,
        contact: str | None = None,
        ttl: int | None = None,
        authoritative: str | None = None,
        forwarder: str | None = None,
        forwarder6: str | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        source_ip_interface: str | None = None,
        rr_max: int | None = None,
        dns_entry: list | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            name: Zone name. (optional)
            status: Enable/disable this DNS zone. (optional)
            domain: Domain name. (optional)
            allow_transfer: DNS zone transfer IP address list. (optional)
            type: Zone type (primary to manage entries directly, secondary to
            import entries from other zones). (optional)
            view: Zone view (public to serve public clients, shadow to serve
            internal clients). (optional)
            ip_primary: IP address of primary DNS server. Entries in this
            primary DNS server and imported into the DNS zone. (optional)
            primary_name: Domain name of the default DNS server for this zone.
            (optional)
            contact: Email address of the administrator for this zone. You can
            specify only the username, such as admin or the full email address,
            such as admin@test.com When using only a username, the domain of
            the email will be this zone. (optional)
            ttl: Default time-to-live value for the entries of this DNS zone (0
            - 2147483647 sec, default = 86400). (optional)
            authoritative: Enable/disable authoritative zone. (optional)
            forwarder: DNS zone forwarder IP address list. (optional)
            forwarder6: Forwarder IPv6 address. (optional)
            source_ip: Source IP for forwarding to DNS server. (optional)
            source_ip6: IPv6 source IP address for forwarding to DNS server.
            (optional)
            source_ip_interface: IP address of the specified interface as the
            source IP address. (optional)
            rr_max: Maximum number of resource records (10 - 65536, 0 means
            infinite). (optional)
            dns_entry: DNS entry. (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = "/system/dns-database"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if domain is not None:
            data_payload["domain"] = domain
        if allow_transfer is not None:
            data_payload["allow-transfer"] = allow_transfer
        if type is not None:
            data_payload["type"] = type
        if view is not None:
            data_payload["view"] = view
        if ip_primary is not None:
            data_payload["ip-primary"] = ip_primary
        if primary_name is not None:
            data_payload["primary-name"] = primary_name
        if contact is not None:
            data_payload["contact"] = contact
        if ttl is not None:
            data_payload["ttl"] = ttl
        if authoritative is not None:
            data_payload["authoritative"] = authoritative
        if forwarder is not None:
            data_payload["forwarder"] = forwarder
        if forwarder6 is not None:
            data_payload["forwarder6"] = forwarder6
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip6 is not None:
            data_payload["source-ip6"] = source_ip6
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if rr_max is not None:
            data_payload["rr-max"] = rr_max
        if dns_entry is not None:
            data_payload["dns-entry"] = dns_entry
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
