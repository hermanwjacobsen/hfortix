"""
FortiOS CMDB - Cmdb System Vdom Property

Configuration endpoint for managing cmdb system vdom property objects.

API Endpoints:
    GET    /cmdb/system/vdom_property
    POST   /cmdb/system/vdom_property
    GET    /cmdb/system/vdom_property
    PUT    /cmdb/system/vdom_property/{identifier}
    DELETE /cmdb/system/vdom_property/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.vdom_property.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.vdom_property.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.vdom_property.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.vdom_property.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.vdom_property.delete(name="item_name")

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


class VdomProperty:
    """
    Vdomproperty Operations.

    Provides CRUD operations for FortiOS vdomproperty configuration.

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
        Initialize VdomProperty endpoint.

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
            endpoint = f"/system/vdom-property/{name}"
        else:
            endpoint = "/system/vdom-property"
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
        description: str | None = None,
        snmp_index: int | None = None,
        session: str | None = None,
        ipsec_phase1: str | None = None,
        ipsec_phase2: str | None = None,
        ipsec_phase1_interface: str | None = None,
        ipsec_phase2_interface: str | None = None,
        dialup_tunnel: str | None = None,
        firewall_policy: str | None = None,
        firewall_address: str | None = None,
        firewall_addrgrp: str | None = None,
        custom_service: str | None = None,
        service_group: str | None = None,
        onetime_schedule: str | None = None,
        recurring_schedule: str | None = None,
        user: str | None = None,
        user_group: str | None = None,
        log_disk_quota: str | None = None,
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
            name: VDOM name. (optional)
            description: Description. (optional)
            snmp_index: Permanent SNMP Index of the virtual domain (1 -
            2147483647). (optional)
            session: Maximum guaranteed number of sessions. (optional)
            ipsec_phase1: Maximum guaranteed number of VPN IPsec phase 1
            tunnels. (optional)
            ipsec_phase2: Maximum guaranteed number of VPN IPsec phase 2
            tunnels. (optional)
            ipsec_phase1_interface: Maximum guaranteed number of VPN IPsec
            phase1 interface tunnels. (optional)
            ipsec_phase2_interface: Maximum guaranteed number of VPN IPsec
            phase2 interface tunnels. (optional)
            dialup_tunnel: Maximum guaranteed number of dial-up tunnels.
            (optional)
            firewall_policy: Maximum guaranteed number of firewall policies
            (policy, DoS-policy4, DoS-policy6, multicast). (optional)
            firewall_address: Maximum guaranteed number of firewall addresses
            (IPv4, IPv6, multicast). (optional)
            firewall_addrgrp: Maximum guaranteed number of firewall address
            groups (IPv4, IPv6). (optional)
            custom_service: Maximum guaranteed number of firewall custom
            services. (optional)
            service_group: Maximum guaranteed number of firewall service
            groups. (optional)
            onetime_schedule: Maximum guaranteed number of firewall one-time
            schedules.. (optional)
            recurring_schedule: Maximum guaranteed number of firewall recurring
            schedules. (optional)
            user: Maximum guaranteed number of local users. (optional)
            user_group: Maximum guaranteed number of user groups. (optional)
            log_disk_quota: Log disk quota in megabytes (MB). Range depends on
            how much disk space is available. (optional)
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
        endpoint = f"/system/vdom-property/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if snmp_index is not None:
            data_payload["snmp-index"] = snmp_index
        if session is not None:
            data_payload["session"] = session
        if ipsec_phase1 is not None:
            data_payload["ipsec-phase1"] = ipsec_phase1
        if ipsec_phase2 is not None:
            data_payload["ipsec-phase2"] = ipsec_phase2
        if ipsec_phase1_interface is not None:
            data_payload["ipsec-phase1-interface"] = ipsec_phase1_interface
        if ipsec_phase2_interface is not None:
            data_payload["ipsec-phase2-interface"] = ipsec_phase2_interface
        if dialup_tunnel is not None:
            data_payload["dialup-tunnel"] = dialup_tunnel
        if firewall_policy is not None:
            data_payload["firewall-policy"] = firewall_policy
        if firewall_address is not None:
            data_payload["firewall-address"] = firewall_address
        if firewall_addrgrp is not None:
            data_payload["firewall-addrgrp"] = firewall_addrgrp
        if custom_service is not None:
            data_payload["custom-service"] = custom_service
        if service_group is not None:
            data_payload["service-group"] = service_group
        if onetime_schedule is not None:
            data_payload["onetime-schedule"] = onetime_schedule
        if recurring_schedule is not None:
            data_payload["recurring-schedule"] = recurring_schedule
        if user is not None:
            data_payload["user"] = user
        if user_group is not None:
            data_payload["user-group"] = user_group
        if log_disk_quota is not None:
            data_payload["log-disk-quota"] = log_disk_quota
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
        endpoint = f"/system/vdom-property/{name}"
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
        description: str | None = None,
        snmp_index: int | None = None,
        session: str | None = None,
        ipsec_phase1: str | None = None,
        ipsec_phase2: str | None = None,
        ipsec_phase1_interface: str | None = None,
        ipsec_phase2_interface: str | None = None,
        dialup_tunnel: str | None = None,
        firewall_policy: str | None = None,
        firewall_address: str | None = None,
        firewall_addrgrp: str | None = None,
        custom_service: str | None = None,
        service_group: str | None = None,
        onetime_schedule: str | None = None,
        recurring_schedule: str | None = None,
        user: str | None = None,
        user_group: str | None = None,
        log_disk_quota: str | None = None,
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
            name: VDOM name. (optional)
            description: Description. (optional)
            snmp_index: Permanent SNMP Index of the virtual domain (1 -
            2147483647). (optional)
            session: Maximum guaranteed number of sessions. (optional)
            ipsec_phase1: Maximum guaranteed number of VPN IPsec phase 1
            tunnels. (optional)
            ipsec_phase2: Maximum guaranteed number of VPN IPsec phase 2
            tunnels. (optional)
            ipsec_phase1_interface: Maximum guaranteed number of VPN IPsec
            phase1 interface tunnels. (optional)
            ipsec_phase2_interface: Maximum guaranteed number of VPN IPsec
            phase2 interface tunnels. (optional)
            dialup_tunnel: Maximum guaranteed number of dial-up tunnels.
            (optional)
            firewall_policy: Maximum guaranteed number of firewall policies
            (policy, DoS-policy4, DoS-policy6, multicast). (optional)
            firewall_address: Maximum guaranteed number of firewall addresses
            (IPv4, IPv6, multicast). (optional)
            firewall_addrgrp: Maximum guaranteed number of firewall address
            groups (IPv4, IPv6). (optional)
            custom_service: Maximum guaranteed number of firewall custom
            services. (optional)
            service_group: Maximum guaranteed number of firewall service
            groups. (optional)
            onetime_schedule: Maximum guaranteed number of firewall one-time
            schedules.. (optional)
            recurring_schedule: Maximum guaranteed number of firewall recurring
            schedules. (optional)
            user: Maximum guaranteed number of local users. (optional)
            user_group: Maximum guaranteed number of user groups. (optional)
            log_disk_quota: Log disk quota in megabytes (MB). Range depends on
            how much disk space is available. (optional)
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
        endpoint = "/system/vdom-property"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if description is not None:
            data_payload["description"] = description
        if snmp_index is not None:
            data_payload["snmp-index"] = snmp_index
        if session is not None:
            data_payload["session"] = session
        if ipsec_phase1 is not None:
            data_payload["ipsec-phase1"] = ipsec_phase1
        if ipsec_phase2 is not None:
            data_payload["ipsec-phase2"] = ipsec_phase2
        if ipsec_phase1_interface is not None:
            data_payload["ipsec-phase1-interface"] = ipsec_phase1_interface
        if ipsec_phase2_interface is not None:
            data_payload["ipsec-phase2-interface"] = ipsec_phase2_interface
        if dialup_tunnel is not None:
            data_payload["dialup-tunnel"] = dialup_tunnel
        if firewall_policy is not None:
            data_payload["firewall-policy"] = firewall_policy
        if firewall_address is not None:
            data_payload["firewall-address"] = firewall_address
        if firewall_addrgrp is not None:
            data_payload["firewall-addrgrp"] = firewall_addrgrp
        if custom_service is not None:
            data_payload["custom-service"] = custom_service
        if service_group is not None:
            data_payload["service-group"] = service_group
        if onetime_schedule is not None:
            data_payload["onetime-schedule"] = onetime_schedule
        if recurring_schedule is not None:
            data_payload["recurring-schedule"] = recurring_schedule
        if user is not None:
            data_payload["user"] = user
        if user_group is not None:
            data_payload["user-group"] = user_group
        if log_disk_quota is not None:
            data_payload["log-disk-quota"] = log_disk_quota
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
