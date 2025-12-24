"""
FortiOS CMDB - Cmdb System Pppoe Interface

Configuration endpoint for managing cmdb system pppoe interface objects.

API Endpoints:
    GET    /cmdb/system/pppoe_interface
    POST   /cmdb/system/pppoe_interface
    GET    /cmdb/system/pppoe_interface
    PUT    /cmdb/system/pppoe_interface/{identifier}
    DELETE /cmdb/system/pppoe_interface/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.pppoe_interface.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.pppoe_interface.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.pppoe_interface.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.pppoe_interface.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.pppoe_interface.delete(name="item_name")

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


class PppoeInterface:
    """
    Pppoeinterface Operations.

    Provides CRUD operations for FortiOS pppoeinterface configuration.

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
        Initialize PppoeInterface endpoint.

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
            endpoint = f"/system/pppoe-interface/{name}"
        else:
            endpoint = "/system/pppoe-interface"
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
        dial_on_demand: str | None = None,
        ipv6: str | None = None,
        device: str | None = None,
        username: str | None = None,
        password: str | None = None,
        pppoe_egress_cos: str | None = None,
        auth_type: str | None = None,
        ipunnumbered: str | None = None,
        pppoe_unnumbered_negotiate: str | None = None,
        idle_timeout: int | None = None,
        multilink: str | None = None,
        mrru: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
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
            name: Name of the PPPoE interface. (optional)
            dial_on_demand: Enable/disable dial on demand to dial the PPPoE
            interface when packets are routed to the PPPoE interface.
            (optional)
            ipv6: Enable/disable IPv6 Control Protocol (IPv6CP). (optional)
            device: Name for the physical interface. (optional)
            username: User name. (optional)
            password: Enter the password. (optional)
            pppoe_egress_cos: CoS in VLAN tag for outgoing PPPoE/PPP packets.
            (optional)
            auth_type: PPP authentication type to use. (optional)
            ipunnumbered: PPPoE unnumbered IP. (optional)
            pppoe_unnumbered_negotiate: Enable/disable PPPoE unnumbered
            negotiation. (optional)
            idle_timeout: PPPoE auto disconnect after idle timeout
            (0-4294967295 sec). (optional)
            multilink: Enable/disable PPP multilink support. (optional)
            mrru: PPP MRRU (296 - 65535, default = 1500). (optional)
            disc_retry_timeout: PPPoE discovery init timeout value in
            (0-4294967295 sec). (optional)
            padt_retry_timeout: PPPoE terminate timeout value in (0-4294967295
            sec). (optional)
            service_name: PPPoE service name. (optional)
            ac_name: PPPoE AC name. (optional)
            lcp_echo_interval: Time in seconds between PPPoE Link Control
            Protocol (LCP) echo requests. (optional)
            lcp_max_echo_fails: Maximum missed LCP echo messages before
            disconnect. (optional)
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
        endpoint = f"/system/pppoe-interface/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if dial_on_demand is not None:
            data_payload["dial-on-demand"] = dial_on_demand
        if ipv6 is not None:
            data_payload["ipv6"] = ipv6
        if device is not None:
            data_payload["device"] = device
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if pppoe_egress_cos is not None:
            data_payload["pppoe-egress-cos"] = pppoe_egress_cos
        if auth_type is not None:
            data_payload["auth-type"] = auth_type
        if ipunnumbered is not None:
            data_payload["ipunnumbered"] = ipunnumbered
        if pppoe_unnumbered_negotiate is not None:
            data_payload["pppoe-unnumbered-negotiate"] = (
                pppoe_unnumbered_negotiate
            )
        if idle_timeout is not None:
            data_payload["idle-timeout"] = idle_timeout
        if multilink is not None:
            data_payload["multilink"] = multilink
        if mrru is not None:
            data_payload["mrru"] = mrru
        if disc_retry_timeout is not None:
            data_payload["disc-retry-timeout"] = disc_retry_timeout
        if padt_retry_timeout is not None:
            data_payload["padt-retry-timeout"] = padt_retry_timeout
        if service_name is not None:
            data_payload["service-name"] = service_name
        if ac_name is not None:
            data_payload["ac-name"] = ac_name
        if lcp_echo_interval is not None:
            data_payload["lcp-echo-interval"] = lcp_echo_interval
        if lcp_max_echo_fails is not None:
            data_payload["lcp-max-echo-fails"] = lcp_max_echo_fails
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
        endpoint = f"/system/pppoe-interface/{name}"
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
        dial_on_demand: str | None = None,
        ipv6: str | None = None,
        device: str | None = None,
        username: str | None = None,
        password: str | None = None,
        pppoe_egress_cos: str | None = None,
        auth_type: str | None = None,
        ipunnumbered: str | None = None,
        pppoe_unnumbered_negotiate: str | None = None,
        idle_timeout: int | None = None,
        multilink: str | None = None,
        mrru: int | None = None,
        disc_retry_timeout: int | None = None,
        padt_retry_timeout: int | None = None,
        service_name: str | None = None,
        ac_name: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
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
            name: Name of the PPPoE interface. (optional)
            dial_on_demand: Enable/disable dial on demand to dial the PPPoE
            interface when packets are routed to the PPPoE interface.
            (optional)
            ipv6: Enable/disable IPv6 Control Protocol (IPv6CP). (optional)
            device: Name for the physical interface. (optional)
            username: User name. (optional)
            password: Enter the password. (optional)
            pppoe_egress_cos: CoS in VLAN tag for outgoing PPPoE/PPP packets.
            (optional)
            auth_type: PPP authentication type to use. (optional)
            ipunnumbered: PPPoE unnumbered IP. (optional)
            pppoe_unnumbered_negotiate: Enable/disable PPPoE unnumbered
            negotiation. (optional)
            idle_timeout: PPPoE auto disconnect after idle timeout
            (0-4294967295 sec). (optional)
            multilink: Enable/disable PPP multilink support. (optional)
            mrru: PPP MRRU (296 - 65535, default = 1500). (optional)
            disc_retry_timeout: PPPoE discovery init timeout value in
            (0-4294967295 sec). (optional)
            padt_retry_timeout: PPPoE terminate timeout value in (0-4294967295
            sec). (optional)
            service_name: PPPoE service name. (optional)
            ac_name: PPPoE AC name. (optional)
            lcp_echo_interval: Time in seconds between PPPoE Link Control
            Protocol (LCP) echo requests. (optional)
            lcp_max_echo_fails: Maximum missed LCP echo messages before
            disconnect. (optional)
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
        endpoint = "/system/pppoe-interface"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if dial_on_demand is not None:
            data_payload["dial-on-demand"] = dial_on_demand
        if ipv6 is not None:
            data_payload["ipv6"] = ipv6
        if device is not None:
            data_payload["device"] = device
        if username is not None:
            data_payload["username"] = username
        if password is not None:
            data_payload["password"] = password
        if pppoe_egress_cos is not None:
            data_payload["pppoe-egress-cos"] = pppoe_egress_cos
        if auth_type is not None:
            data_payload["auth-type"] = auth_type
        if ipunnumbered is not None:
            data_payload["ipunnumbered"] = ipunnumbered
        if pppoe_unnumbered_negotiate is not None:
            data_payload["pppoe-unnumbered-negotiate"] = (
                pppoe_unnumbered_negotiate
            )
        if idle_timeout is not None:
            data_payload["idle-timeout"] = idle_timeout
        if multilink is not None:
            data_payload["multilink"] = multilink
        if mrru is not None:
            data_payload["mrru"] = mrru
        if disc_retry_timeout is not None:
            data_payload["disc-retry-timeout"] = disc_retry_timeout
        if padt_retry_timeout is not None:
            data_payload["padt-retry-timeout"] = padt_retry_timeout
        if service_name is not None:
            data_payload["service-name"] = service_name
        if ac_name is not None:
            data_payload["ac-name"] = ac_name
        if lcp_echo_interval is not None:
            data_payload["lcp-echo-interval"] = lcp_echo_interval
        if lcp_max_echo_fails is not None:
            data_payload["lcp-max-echo-fails"] = lcp_max_echo_fails
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
