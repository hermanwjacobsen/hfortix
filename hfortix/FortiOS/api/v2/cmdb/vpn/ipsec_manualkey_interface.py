"""
FortiOS CMDB - Cmdb Vpn Ipsec Manualkey Interface

Configuration endpoint for managing cmdb vpn ipsec manualkey interface objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec_manualkey_interface
    POST   /cmdb/vpn/ipsec_manualkey_interface
    GET    /cmdb/vpn/ipsec_manualkey_interface
    PUT    /cmdb/vpn/ipsec_manualkey_interface/{identifier}
    DELETE /cmdb/vpn/ipsec_manualkey_interface/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn.ipsec_manualkey_interface.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.vpn.ipsec_manualkey_interface.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.vpn.ipsec_manualkey_interface.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.vpn.ipsec_manualkey_interface.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.vpn.ipsec_manualkey_interface.delete(name="item_name")

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


class IpsecManualkeyInterface:
    """
    Ipsecmanualkeyinterface Operations.

    Provides CRUD operations for FortiOS ipsecmanualkeyinterface configuration.

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
        Initialize IpsecManualkeyInterface endpoint.

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
            endpoint = f"/vpn.ipsec/manualkey-interface/{name}"
        else:
            endpoint = "/vpn.ipsec/manualkey-interface"
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
        interface: str | None = None,
        ip_version: str | None = None,
        addr_type: str | None = None,
        remote_gw: str | None = None,
        remote_gw6: str | None = None,
        local_gw: str | None = None,
        local_gw6: str | None = None,
        auth_alg: str | None = None,
        enc_alg: str | None = None,
        auth_key: str | None = None,
        enc_key: str | None = None,
        local_spi: str | None = None,
        remote_spi: str | None = None,
        npu_offload: str | None = None,
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
            name: IPsec tunnel name. (optional)
            interface: Name of the physical, aggregate, or VLAN interface.
            (optional)
            ip_version: IP version to use for VPN interface. (optional)
            addr_type: IP version to use for IP packets. (optional)
            remote_gw: IPv4 address of the remote gateway's external interface.
            (optional)
            remote_gw6: Remote IPv6 address of VPN gateway. (optional)
            local_gw: IPv4 address of the local gateway's external interface.
            (optional)
            local_gw6: Local IPv6 address of VPN gateway. (optional)
            auth_alg: Authentication algorithm. Must be the same for both ends
            of the tunnel. (optional)
            enc_alg: Encryption algorithm. Must be the same for both ends of
            the tunnel. (optional)
            auth_key: Hexadecimal authentication key in 16-digit (8-byte)
            segments separated by hyphens. (optional)
            enc_key: Hexadecimal encryption key in 16-digit (8-byte) segments
            separated by hyphens. (optional)
            local_spi: Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns
            between two traffic streams with different encryption rules.
            (optional)
            remote_spi: Remote SPI, a hexadecimal 8-digit (4-byte) tag.
            Discerns between two traffic streams with different encryption
            rules. (optional)
            npu_offload: Enable/disable offloading IPsec VPN manual key
            sessions to NPUs. (optional)
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
        endpoint = f"/vpn.ipsec/manualkey-interface/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if interface is not None:
            data_payload["interface"] = interface
        if ip_version is not None:
            data_payload["ip-version"] = ip_version
        if addr_type is not None:
            data_payload["addr-type"] = addr_type
        if remote_gw is not None:
            data_payload["remote-gw"] = remote_gw
        if remote_gw6 is not None:
            data_payload["remote-gw6"] = remote_gw6
        if local_gw is not None:
            data_payload["local-gw"] = local_gw
        if local_gw6 is not None:
            data_payload["local-gw6"] = local_gw6
        if auth_alg is not None:
            data_payload["auth-alg"] = auth_alg
        if enc_alg is not None:
            data_payload["enc-alg"] = enc_alg
        if auth_key is not None:
            data_payload["auth-key"] = auth_key
        if enc_key is not None:
            data_payload["enc-key"] = enc_key
        if local_spi is not None:
            data_payload["local-spi"] = local_spi
        if remote_spi is not None:
            data_payload["remote-spi"] = remote_spi
        if npu_offload is not None:
            data_payload["npu-offload"] = npu_offload
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
        endpoint = f"/vpn.ipsec/manualkey-interface/{name}"
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
        interface: str | None = None,
        ip_version: str | None = None,
        addr_type: str | None = None,
        remote_gw: str | None = None,
        remote_gw6: str | None = None,
        local_gw: str | None = None,
        local_gw6: str | None = None,
        auth_alg: str | None = None,
        enc_alg: str | None = None,
        auth_key: str | None = None,
        enc_key: str | None = None,
        local_spi: str | None = None,
        remote_spi: str | None = None,
        npu_offload: str | None = None,
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
            name: IPsec tunnel name. (optional)
            interface: Name of the physical, aggregate, or VLAN interface.
            (optional)
            ip_version: IP version to use for VPN interface. (optional)
            addr_type: IP version to use for IP packets. (optional)
            remote_gw: IPv4 address of the remote gateway's external interface.
            (optional)
            remote_gw6: Remote IPv6 address of VPN gateway. (optional)
            local_gw: IPv4 address of the local gateway's external interface.
            (optional)
            local_gw6: Local IPv6 address of VPN gateway. (optional)
            auth_alg: Authentication algorithm. Must be the same for both ends
            of the tunnel. (optional)
            enc_alg: Encryption algorithm. Must be the same for both ends of
            the tunnel. (optional)
            auth_key: Hexadecimal authentication key in 16-digit (8-byte)
            segments separated by hyphens. (optional)
            enc_key: Hexadecimal encryption key in 16-digit (8-byte) segments
            separated by hyphens. (optional)
            local_spi: Local SPI, a hexadecimal 8-digit (4-byte) tag. Discerns
            between two traffic streams with different encryption rules.
            (optional)
            remote_spi: Remote SPI, a hexadecimal 8-digit (4-byte) tag.
            Discerns between two traffic streams with different encryption
            rules. (optional)
            npu_offload: Enable/disable offloading IPsec VPN manual key
            sessions to NPUs. (optional)
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
        endpoint = "/vpn.ipsec/manualkey-interface"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if interface is not None:
            data_payload["interface"] = interface
        if ip_version is not None:
            data_payload["ip-version"] = ip_version
        if addr_type is not None:
            data_payload["addr-type"] = addr_type
        if remote_gw is not None:
            data_payload["remote-gw"] = remote_gw
        if remote_gw6 is not None:
            data_payload["remote-gw6"] = remote_gw6
        if local_gw is not None:
            data_payload["local-gw"] = local_gw
        if local_gw6 is not None:
            data_payload["local-gw6"] = local_gw6
        if auth_alg is not None:
            data_payload["auth-alg"] = auth_alg
        if enc_alg is not None:
            data_payload["enc-alg"] = enc_alg
        if auth_key is not None:
            data_payload["auth-key"] = auth_key
        if enc_key is not None:
            data_payload["enc-key"] = enc_key
        if local_spi is not None:
            data_payload["local-spi"] = local_spi
        if remote_spi is not None:
            data_payload["remote-spi"] = remote_spi
        if npu_offload is not None:
            data_payload["npu-offload"] = npu_offload
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
