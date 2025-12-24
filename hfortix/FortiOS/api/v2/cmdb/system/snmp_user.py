"""
FortiOS CMDB - Cmdb System Snmp User

Configuration endpoint for managing cmdb system snmp user objects.

API Endpoints:
    GET    /cmdb/system/snmp_user
    POST   /cmdb/system/snmp_user
    GET    /cmdb/system/snmp_user
    PUT    /cmdb/system/snmp_user/{identifier}
    DELETE /cmdb/system/snmp_user/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.snmp_user.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.snmp_user.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.snmp_user.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.snmp_user.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.snmp_user.delete(name="item_name")

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


class SnmpUser:
    """
    Snmpuser Operations.

    Provides CRUD operations for FortiOS snmpuser configuration.

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
        Initialize SnmpUser endpoint.

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
            endpoint = f"/system.snmp/user/{name}"
        else:
            endpoint = "/system.snmp/user"
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
        trap_status: str | None = None,
        trap_lport: int | None = None,
        trap_rport: int | None = None,
        queries: str | None = None,
        query_port: int | None = None,
        notify_hosts: str | None = None,
        notify_hosts6: str | None = None,
        source_ip: str | None = None,
        source_ipv6: str | None = None,
        ha_direct: str | None = None,
        events: str | None = None,
        mib_view: str | None = None,
        vdoms: list | None = None,
        security_level: str | None = None,
        auth_proto: str | None = None,
        auth_pwd: str | None = None,
        priv_proto: str | None = None,
        priv_pwd: str | None = None,
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
            name: SNMP user name. (optional)
            status: Enable/disable this SNMP user. (optional)
            trap_status: Enable/disable traps for this SNMP user. (optional)
            trap_lport: SNMPv3 local trap port (default = 162). (optional)
            trap_rport: SNMPv3 trap remote port (default = 162). (optional)
            queries: Enable/disable SNMP queries for this user. (optional)
            query_port: SNMPv3 query port (default = 161). (optional)
            notify_hosts: SNMP managers to send notifications (traps) to.
            (optional)
            notify_hosts6: IPv6 SNMP managers to send notifications (traps) to.
            (optional)
            source_ip: Source IP for SNMP trap. (optional)
            source_ipv6: Source IPv6 for SNMP trap. (optional)
            ha_direct: Enable/disable direct management of HA cluster members.
            (optional)
            events: SNMP notifications (traps) to send. (optional)
            mib_view: SNMP access control MIB view. (optional)
            vdoms: SNMP access control VDOMs. (optional)
            security_level: Security level for message authentication and
            encryption. (optional)
            auth_proto: Authentication protocol. (optional)
            auth_pwd: Password for authentication protocol. (optional)
            priv_proto: Privacy (encryption) protocol. (optional)
            priv_pwd: Password for privacy (encryption) protocol. (optional)
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
        endpoint = f"/system.snmp/user/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if trap_status is not None:
            data_payload["trap-status"] = trap_status
        if trap_lport is not None:
            data_payload["trap-lport"] = trap_lport
        if trap_rport is not None:
            data_payload["trap-rport"] = trap_rport
        if queries is not None:
            data_payload["queries"] = queries
        if query_port is not None:
            data_payload["query-port"] = query_port
        if notify_hosts is not None:
            data_payload["notify-hosts"] = notify_hosts
        if notify_hosts6 is not None:
            data_payload["notify-hosts6"] = notify_hosts6
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ipv6 is not None:
            data_payload["source-ipv6"] = source_ipv6
        if ha_direct is not None:
            data_payload["ha-direct"] = ha_direct
        if events is not None:
            data_payload["events"] = events
        if mib_view is not None:
            data_payload["mib-view"] = mib_view
        if vdoms is not None:
            data_payload["vdoms"] = vdoms
        if security_level is not None:
            data_payload["security-level"] = security_level
        if auth_proto is not None:
            data_payload["auth-proto"] = auth_proto
        if auth_pwd is not None:
            data_payload["auth-pwd"] = auth_pwd
        if priv_proto is not None:
            data_payload["priv-proto"] = priv_proto
        if priv_pwd is not None:
            data_payload["priv-pwd"] = priv_pwd
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
        endpoint = f"/system.snmp/user/{name}"
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
        trap_status: str | None = None,
        trap_lport: int | None = None,
        trap_rport: int | None = None,
        queries: str | None = None,
        query_port: int | None = None,
        notify_hosts: str | None = None,
        notify_hosts6: str | None = None,
        source_ip: str | None = None,
        source_ipv6: str | None = None,
        ha_direct: str | None = None,
        events: str | None = None,
        mib_view: str | None = None,
        vdoms: list | None = None,
        security_level: str | None = None,
        auth_proto: str | None = None,
        auth_pwd: str | None = None,
        priv_proto: str | None = None,
        priv_pwd: str | None = None,
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
            name: SNMP user name. (optional)
            status: Enable/disable this SNMP user. (optional)
            trap_status: Enable/disable traps for this SNMP user. (optional)
            trap_lport: SNMPv3 local trap port (default = 162). (optional)
            trap_rport: SNMPv3 trap remote port (default = 162). (optional)
            queries: Enable/disable SNMP queries for this user. (optional)
            query_port: SNMPv3 query port (default = 161). (optional)
            notify_hosts: SNMP managers to send notifications (traps) to.
            (optional)
            notify_hosts6: IPv6 SNMP managers to send notifications (traps) to.
            (optional)
            source_ip: Source IP for SNMP trap. (optional)
            source_ipv6: Source IPv6 for SNMP trap. (optional)
            ha_direct: Enable/disable direct management of HA cluster members.
            (optional)
            events: SNMP notifications (traps) to send. (optional)
            mib_view: SNMP access control MIB view. (optional)
            vdoms: SNMP access control VDOMs. (optional)
            security_level: Security level for message authentication and
            encryption. (optional)
            auth_proto: Authentication protocol. (optional)
            auth_pwd: Password for authentication protocol. (optional)
            priv_proto: Privacy (encryption) protocol. (optional)
            priv_pwd: Password for privacy (encryption) protocol. (optional)
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
        endpoint = "/system.snmp/user"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if status is not None:
            data_payload["status"] = status
        if trap_status is not None:
            data_payload["trap-status"] = trap_status
        if trap_lport is not None:
            data_payload["trap-lport"] = trap_lport
        if trap_rport is not None:
            data_payload["trap-rport"] = trap_rport
        if queries is not None:
            data_payload["queries"] = queries
        if query_port is not None:
            data_payload["query-port"] = query_port
        if notify_hosts is not None:
            data_payload["notify-hosts"] = notify_hosts
        if notify_hosts6 is not None:
            data_payload["notify-hosts6"] = notify_hosts6
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ipv6 is not None:
            data_payload["source-ipv6"] = source_ipv6
        if ha_direct is not None:
            data_payload["ha-direct"] = ha_direct
        if events is not None:
            data_payload["events"] = events
        if mib_view is not None:
            data_payload["mib-view"] = mib_view
        if vdoms is not None:
            data_payload["vdoms"] = vdoms
        if security_level is not None:
            data_payload["security-level"] = security_level
        if auth_proto is not None:
            data_payload["auth-proto"] = auth_proto
        if auth_pwd is not None:
            data_payload["auth-pwd"] = auth_pwd
        if priv_proto is not None:
            data_payload["priv-proto"] = priv_proto
        if priv_pwd is not None:
            data_payload["priv-pwd"] = priv_pwd
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
