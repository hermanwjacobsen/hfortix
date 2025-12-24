"""
FortiOS CMDB - Cmdb System Sdn Vpn

Configuration endpoint for managing cmdb system sdn vpn objects.

API Endpoints:
    GET    /cmdb/system/sdn_vpn
    POST   /cmdb/system/sdn_vpn
    GET    /cmdb/system/sdn_vpn
    PUT    /cmdb/system/sdn_vpn/{identifier}
    DELETE /cmdb/system/sdn_vpn/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.sdn_vpn.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.sdn_vpn.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.sdn_vpn.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.sdn_vpn.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.sdn_vpn.delete(name="item_name")

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


class SdnVpn:
    """
    Sdnvpn Operations.

    Provides CRUD operations for FortiOS sdnvpn configuration.

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
        Initialize SdnVpn endpoint.

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
            endpoint = f"/system/sdn-vpn/{name}"
        else:
            endpoint = "/system/sdn-vpn"
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
        sdn: str | None = None,
        remote_type: str | None = None,
        routing_type: str | None = None,
        vgw_id: str | None = None,
        tgw_id: str | None = None,
        subnet_id: str | None = None,
        bgp_as: int | None = None,
        cgw_gateway: str | None = None,
        nat_traversal: str | None = None,
        tunnel_interface: str | None = None,
        internal_interface: str | None = None,
        local_cidr: str | None = None,
        remote_cidr: str | None = None,
        cgw_name: str | None = None,
        psksecret: str | None = None,
        type: int | None = None,
        status: int | None = None,
        code: int | None = None,
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
            name: Public cloud VPN name. (optional)
            sdn: SDN connector name. (optional)
            remote_type: Type of remote device. (optional)
            routing_type: Type of routing. (optional)
            vgw_id: Virtual private gateway id. (optional)
            tgw_id: Transit gateway id. (optional)
            subnet_id: AWS subnet id for TGW route propagation. (optional)
            bgp_as: BGP Router AS number. (optional)
            cgw_gateway: Public IP address of the customer gateway. (optional)
            nat_traversal: Enable/disable use for NAT traversal. Please enable
            if your FortiGate device is behind a NAT/PAT device. (optional)
            tunnel_interface: Tunnel interface with public IP. (optional)
            internal_interface: Internal interface with local subnet.
            (optional)
            local_cidr: Local subnet address and subnet mask. (optional)
            remote_cidr: Remote subnet address and subnet mask. (optional)
            cgw_name: AWS customer gateway name to be created. (optional)
            psksecret: Pre-shared secret for PSK authentication. Auto-generated
            if not specified (optional)
            type: SDN VPN type. (optional)
            status: SDN VPN status. (optional)
            code: SDN VPN error code. (optional)
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
        endpoint = f"/system/sdn-vpn/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if sdn is not None:
            data_payload["sdn"] = sdn
        if remote_type is not None:
            data_payload["remote-type"] = remote_type
        if routing_type is not None:
            data_payload["routing-type"] = routing_type
        if vgw_id is not None:
            data_payload["vgw-id"] = vgw_id
        if tgw_id is not None:
            data_payload["tgw-id"] = tgw_id
        if subnet_id is not None:
            data_payload["subnet-id"] = subnet_id
        if bgp_as is not None:
            data_payload["bgp-as"] = bgp_as
        if cgw_gateway is not None:
            data_payload["cgw-gateway"] = cgw_gateway
        if nat_traversal is not None:
            data_payload["nat-traversal"] = nat_traversal
        if tunnel_interface is not None:
            data_payload["tunnel-interface"] = tunnel_interface
        if internal_interface is not None:
            data_payload["internal-interface"] = internal_interface
        if local_cidr is not None:
            data_payload["local-cidr"] = local_cidr
        if remote_cidr is not None:
            data_payload["remote-cidr"] = remote_cidr
        if cgw_name is not None:
            data_payload["cgw-name"] = cgw_name
        if psksecret is not None:
            data_payload["psksecret"] = psksecret
        if type is not None:
            data_payload["type"] = type
        if status is not None:
            data_payload["status"] = status
        if code is not None:
            data_payload["code"] = code
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
        endpoint = f"/system/sdn-vpn/{name}"
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
        sdn: str | None = None,
        remote_type: str | None = None,
        routing_type: str | None = None,
        vgw_id: str | None = None,
        tgw_id: str | None = None,
        subnet_id: str | None = None,
        bgp_as: int | None = None,
        cgw_gateway: str | None = None,
        nat_traversal: str | None = None,
        tunnel_interface: str | None = None,
        internal_interface: str | None = None,
        local_cidr: str | None = None,
        remote_cidr: str | None = None,
        cgw_name: str | None = None,
        psksecret: str | None = None,
        type: int | None = None,
        status: int | None = None,
        code: int | None = None,
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
            name: Public cloud VPN name. (optional)
            sdn: SDN connector name. (optional)
            remote_type: Type of remote device. (optional)
            routing_type: Type of routing. (optional)
            vgw_id: Virtual private gateway id. (optional)
            tgw_id: Transit gateway id. (optional)
            subnet_id: AWS subnet id for TGW route propagation. (optional)
            bgp_as: BGP Router AS number. (optional)
            cgw_gateway: Public IP address of the customer gateway. (optional)
            nat_traversal: Enable/disable use for NAT traversal. Please enable
            if your FortiGate device is behind a NAT/PAT device. (optional)
            tunnel_interface: Tunnel interface with public IP. (optional)
            internal_interface: Internal interface with local subnet.
            (optional)
            local_cidr: Local subnet address and subnet mask. (optional)
            remote_cidr: Remote subnet address and subnet mask. (optional)
            cgw_name: AWS customer gateway name to be created. (optional)
            psksecret: Pre-shared secret for PSK authentication. Auto-generated
            if not specified (optional)
            type: SDN VPN type. (optional)
            status: SDN VPN status. (optional)
            code: SDN VPN error code. (optional)
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
        endpoint = "/system/sdn-vpn"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if sdn is not None:
            data_payload["sdn"] = sdn
        if remote_type is not None:
            data_payload["remote-type"] = remote_type
        if routing_type is not None:
            data_payload["routing-type"] = routing_type
        if vgw_id is not None:
            data_payload["vgw-id"] = vgw_id
        if tgw_id is not None:
            data_payload["tgw-id"] = tgw_id
        if subnet_id is not None:
            data_payload["subnet-id"] = subnet_id
        if bgp_as is not None:
            data_payload["bgp-as"] = bgp_as
        if cgw_gateway is not None:
            data_payload["cgw-gateway"] = cgw_gateway
        if nat_traversal is not None:
            data_payload["nat-traversal"] = nat_traversal
        if tunnel_interface is not None:
            data_payload["tunnel-interface"] = tunnel_interface
        if internal_interface is not None:
            data_payload["internal-interface"] = internal_interface
        if local_cidr is not None:
            data_payload["local-cidr"] = local_cidr
        if remote_cidr is not None:
            data_payload["remote-cidr"] = remote_cidr
        if cgw_name is not None:
            data_payload["cgw-name"] = cgw_name
        if psksecret is not None:
            data_payload["psksecret"] = psksecret
        if type is not None:
            data_payload["type"] = type
        if status is not None:
            data_payload["status"] = status
        if code is not None:
            data_payload["code"] = code
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
