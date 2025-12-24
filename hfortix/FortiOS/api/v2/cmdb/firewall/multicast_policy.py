"""
FortiOS CMDB - Cmdb Firewall Multicast Policy

Configuration endpoint for managing cmdb firewall multicast policy objects.

API Endpoints:
    GET    /cmdb/firewall/multicast_policy
    POST   /cmdb/firewall/multicast_policy
    GET    /cmdb/firewall/multicast_policy
    PUT    /cmdb/firewall/multicast_policy/{identifier}
    DELETE /cmdb/firewall/multicast_policy/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.multicast_policy.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.multicast_policy.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.multicast_policy.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.multicast_policy.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.firewall.multicast_policy.delete(name="item_name")

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


class MulticastPolicy:
    """
    Multicastpolicy Operations.

    Provides CRUD operations for FortiOS multicastpolicy configuration.

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
        Initialize MulticastPolicy endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: str | None = None,
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
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/firewall/multicast-policy/{id}"
        else:
            endpoint = "/firewall/multicast-policy"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comments: str | None = None,
        status: str | None = None,
        srcintf: str | None = None,
        dstintf: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        snat: str | None = None,
        snat_ip: str | None = None,
        dnat: str | None = None,
        protocol: int | None = None,
        start_port: int | None = None,
        end_port: int | None = None,
        utm_status: str | None = None,
        ips_sensor: str | None = None,
        logtraffic: str | None = None,
        auto_asic_offload: str | None = None,
        traffic_shaper: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            id: Policy ID ((0 - 4294967294). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            name: Policy name. (optional)
            comments: Comment. (optional)
            status: Enable/disable this policy. (optional)
            srcintf: Source interface name. (optional)
            dstintf: Destination interface name. (optional)
            srcaddr: Source address objects. (optional)
            dstaddr: Destination address objects. (optional)
            snat: Enable/disable substitution of the outgoing interface IP
            address for the original source IP address (called source NAT or
            SNAT). (optional)
            snat_ip: IPv4 address to be used as the source address for NATed
            traffic. (optional)
            dnat: IPv4 DNAT address used for multicast destination addresses.
            (optional)
            protocol: Integer value for the protocol type as defined by IANA (0
            - 255, default = 0). (optional)
            start_port: Integer value for starting TCP/UDP/SCTP destination
            port in range (1 - 65535, default = 1). (optional)
            end_port: Integer value for ending TCP/UDP/SCTP destination port in
            range (1 - 65535, default = 1). (optional)
            utm_status: Enable to add an IPS security profile to the policy.
            (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security
            profile sessions. (optional)
            auto_asic_offload: Enable/disable offloading policy traffic for
            hardware acceleration. (optional)
            traffic_shaper: Traffic shaper to apply to traffic forwarded by the
            multicast policy. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/firewall/multicast-policy/{id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if id is not None:
            data_payload["id"] = id
        if uuid is not None:
            data_payload["uuid"] = uuid
        if name is not None:
            data_payload["name"] = name
        if comments is not None:
            data_payload["comments"] = comments
        if status is not None:
            data_payload["status"] = status
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if dstintf is not None:
            data_payload["dstint"] = dstintf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if snat is not None:
            data_payload["snat"] = snat
        if snat_ip is not None:
            data_payload["snat-ip"] = snat_ip
        if dnat is not None:
            data_payload["dnat"] = dnat
        if protocol is not None:
            data_payload["protocol"] = protocol
        if start_port is not None:
            data_payload["start-port"] = start_port
        if end_port is not None:
            data_payload["end-port"] = end_port
        if utm_status is not None:
            data_payload["utm-status"] = utm_status
        if ips_sensor is not None:
            data_payload["ips-sensor"] = ips_sensor
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if auto_asic_offload is not None:
            data_payload["auto-asic-offload"] = auto_asic_offload
        if traffic_shaper is not None:
            data_payload["traffic-shaper"] = traffic_shaper
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/firewall/multicast-policy/{id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            id: Object identifier
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
        result = self.get(id=id, vdom=vdom)

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
        id: int | None = None,
        uuid: str | None = None,
        name: str | None = None,
        comments: str | None = None,
        status: str | None = None,
        srcintf: str | None = None,
        dstintf: str | None = None,
        srcaddr: list | None = None,
        dstaddr: list | None = None,
        snat: str | None = None,
        snat_ip: str | None = None,
        dnat: str | None = None,
        protocol: int | None = None,
        start_port: int | None = None,
        end_port: int | None = None,
        utm_status: str | None = None,
        ips_sensor: str | None = None,
        logtraffic: str | None = None,
        auto_asic_offload: str | None = None,
        traffic_shaper: str | None = None,
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
            id: Policy ID ((0 - 4294967294). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            name: Policy name. (optional)
            comments: Comment. (optional)
            status: Enable/disable this policy. (optional)
            srcintf: Source interface name. (optional)
            dstintf: Destination interface name. (optional)
            srcaddr: Source address objects. (optional)
            dstaddr: Destination address objects. (optional)
            snat: Enable/disable substitution of the outgoing interface IP
            address for the original source IP address (called source NAT or
            SNAT). (optional)
            snat_ip: IPv4 address to be used as the source address for NATed
            traffic. (optional)
            dnat: IPv4 DNAT address used for multicast destination addresses.
            (optional)
            protocol: Integer value for the protocol type as defined by IANA (0
            - 255, default = 0). (optional)
            start_port: Integer value for starting TCP/UDP/SCTP destination
            port in range (1 - 65535, default = 1). (optional)
            end_port: Integer value for ending TCP/UDP/SCTP destination port in
            range (1 - 65535, default = 1). (optional)
            utm_status: Enable to add an IPS security profile to the policy.
            (optional)
            ips_sensor: Name of an existing IPS sensor. (optional)
            logtraffic: Enable or disable logging. Log all sessions or security
            profile sessions. (optional)
            auto_asic_offload: Enable/disable offloading policy traffic for
            hardware acceleration. (optional)
            traffic_shaper: Traffic shaper to apply to traffic forwarded by the
            multicast policy. (optional)
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
        endpoint = "/firewall/multicast-policy"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if id is not None:
            data_payload["id"] = id
        if uuid is not None:
            data_payload["uuid"] = uuid
        if name is not None:
            data_payload["name"] = name
        if comments is not None:
            data_payload["comments"] = comments
        if status is not None:
            data_payload["status"] = status
        if srcintf is not None:
            data_payload["srcint"] = srcintf
        if dstintf is not None:
            data_payload["dstint"] = dstintf
        if srcaddr is not None:
            data_payload["srcaddr"] = srcaddr
        if dstaddr is not None:
            data_payload["dstaddr"] = dstaddr
        if snat is not None:
            data_payload["snat"] = snat
        if snat_ip is not None:
            data_payload["snat-ip"] = snat_ip
        if dnat is not None:
            data_payload["dnat"] = dnat
        if protocol is not None:
            data_payload["protocol"] = protocol
        if start_port is not None:
            data_payload["start-port"] = start_port
        if end_port is not None:
            data_payload["end-port"] = end_port
        if utm_status is not None:
            data_payload["utm-status"] = utm_status
        if ips_sensor is not None:
            data_payload["ips-sensor"] = ips_sensor
        if logtraffic is not None:
            data_payload["logtraffic"] = logtraffic
        if auto_asic_offload is not None:
            data_payload["auto-asic-offload"] = auto_asic_offload
        if traffic_shaper is not None:
            data_payload["traffic-shaper"] = traffic_shaper
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
