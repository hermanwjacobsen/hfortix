"""
FortiOS CMDB - Router Static

Configure IPv4 static routing tables.

API Endpoints:
    GET    /api/v2/cmdb/router/static           - List all / Get specific
    POST   /api/v2/cmdb/router/static           - Create
    PUT    /api/v2/cmdb/router/static/{seq-num}   - Update
    DELETE /api/v2/cmdb/router/static/{seq-num}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Static:
    """Router IPv4 static routes endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Router Static endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all IPv4 static routes.

        Args:
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict with list of static routes

        Examples:
            >>> # List all static routes
            >>> result = fgt.api.cmdb.router.static.list()
            >>> for route in result['results']:
            ...     print(f"Seq: {route['seq-num']}, Dst: {route.get('dst')}, Gateway: {route.get('gateway')}")
        """
        return self.get(vdom=vdom, **kwargs)

    def get(
        self,
        seq_num: Optional[int] = None,
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[dict] = None,
        acs: Optional[int] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get IPv4 static route(s) - List all or get specific.

        Args:
            seq_num: Sequence number (if specified, gets single route)
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned result are in ascending order
            search: Filter objects by search value
            scope: Scope level (global, vdom, or both)
            datasource: Enable to include datasource information
            with_meta: Enable to include meta information
            skip: Enable to call CLI skip operator
            format: List of property names to include in results
            action: Special action (datasource, stats, schema, etc.)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # List all static routes
            >>> result = fgt.api.cmdb.router.static.get()

            >>> # Get specific static route by sequence number
            >>> result = fgt.api.cmdb.router.static.get(seq_num=1)

            >>> # Get with specific format
            >>> result = fgt.api.cmdb.router.static.get(format=['seq-num', 'dst', 'gateway', 'device'])
        """
        params = {}
        param_map = {
            "attr": attr,
            "count": count,
            "skip_to_datasource": skip_to_datasource,
            "acs": acs,
            "search": search,
            "scope": scope,
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = "router/static"
        if seq_num is not None:
            path = f"{path}/{encode_path_component(str(seq_num))}"

        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        seq_num: Optional[int] = None,
        status: Optional[str] = None,
        dst: Optional[str] = None,
        src: Optional[str] = None,
        gateway: Optional[str] = None,
        preferred_source: Optional[str] = None,
        distance: Optional[int] = None,
        weight: Optional[int] = None,
        priority: Optional[int] = None,
        device: Optional[str] = None,
        comment: Optional[str] = None,
        blackhole: Optional[str] = None,
        dynamic_gateway: Optional[str] = None,
        sdwan_zone: Optional[list] = None,
        dstaddr: Optional[str] = None,
        internet_service: Optional[int] = None,
        internet_service_custom: Optional[str] = None,
        internet_service_fortiguard: Optional[str] = None,
        link_monitor_exempt: Optional[str] = None,
        tag: Optional[int] = None,
        vrf: Optional[int] = None,
        bfd: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create IPv4 static route.

        Supports three usage patterns:
        1. Dictionary: create(data_dict={'dst': '10.0.0.0/8', 'gateway': '192.168.1.1', ...})
        2. Keywords: create(dst='10.0.0.0/8', gateway='192.168.1.1', device='port1')
        3. Mixed: create(data_dict={...}, gateway='override')

        Args:
            data_dict: Complete route dictionary (Python snake_case keys)
            seq_num: Sequence number (0-4294967295)
            status: Enable/disable this static route ('enable', 'disable')
            dst: Destination IP and mask for this route (e.g., '10.0.0.0/8')
            src: Source prefix for this route
            gateway: Gateway IP for this route
            preferred_source: Preferred source IP for this route
            distance: Administrative distance (1-255, default depends on route type)
            weight: Administrative weight (0-255)
            priority: Administrative priority (1-65535)
            device: Gateway out interface or tunnel (max 35 chars)
            comment: Optional comments (max 255 chars)
            blackhole: Enable/disable black hole ('enable', 'disable')
            dynamic_gateway: Enable use of dynamic gateway from DHCP/PPP ('enable', 'disable')
            sdwan_zone: List of SD-WAN zones [{'name': 'zone1'}, ...]
            dstaddr: Name of firewall address or address group (max 79 chars)
            internet_service: Application ID in Internet service database (0-4294967295)
            internet_service_custom: Application name in Internet service custom database (max 64 chars)
            internet_service_fortiguard: Application name in Internet service fortiguard database (max 64 chars)
            link_monitor_exempt: Keep route when link monitor down ('enable', 'disable')
            tag: Route tag (0-4294967295)
            vrf: Virtual Routing Forwarding ID (0-511)
            bfd: Enable/disable BFD ('enable', 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # POST - Create basic static route
            >>> result = fgt.api.cmdb.router.static.create(
            ...     dst='10.0.0.0/8',
            ...     gateway='192.168.1.1',
            ...     device='port1'
            ... )

            >>> # POST - Create with priority and comment
            >>> result = fgt.api.cmdb.router.static.create(
            ...     dst='0.0.0.0/0',
            ...     gateway='192.168.1.254',
            ...     device='wan1',
            ...     priority=10,
            ...     comment='Default route via WAN1'
            ... )

            >>> # Use dictionary for complex configuration
            >>> route_config = {
            ...     'dst': '172.16.0.0/12',
            ...     'gateway': '10.0.0.1',
            ...     'device': 'internal',
            ...     'distance': 10,
            ...     'comment': 'Private network route'
            ... }
            >>> result = fgt.api.cmdb.router.static.create(data_dict=route_config)
        """
        # Start with data_dict or empty dict
        data = data_dict.copy() if data_dict else {}

        # Map Python parameter names to API field names
        param_map = {
            "seq_num": "seq-num",
            "preferred_source": "preferred-source",
            "dynamic_gateway": "dynamic-gateway",
            "sdwan_zone": "sdwan-zone",
            "internet_service": "internet-service",
            "internet_service_custom": "internet-service-custom",
            "internet_service_fortiguard": "internet-service-fortiguard",
            "link_monitor_exempt": "link-monitor-exempt",
        }

        # Apply individual parameters (override data_dict if provided)
        if seq_num is not None:
            data[param_map["seq_num"]] = seq_num
        if status is not None:
            data["status"] = status
        if dst is not None:
            data["dst"] = dst
        if src is not None:
            data["src"] = src
        if gateway is not None:
            data["gateway"] = gateway
        if preferred_source is not None:
            data[param_map["preferred_source"]] = preferred_source
        if distance is not None:
            data["distance"] = distance
        if weight is not None:
            data["weight"] = weight
        if priority is not None:
            data["priority"] = priority
        if device is not None:
            data["device"] = device
        if comment is not None:
            data["comment"] = comment
        if blackhole is not None:
            data["blackhole"] = blackhole
        if dynamic_gateway is not None:
            data[param_map["dynamic_gateway"]] = dynamic_gateway
        if sdwan_zone is not None:
            data[param_map["sdwan_zone"]] = sdwan_zone
        if dstaddr is not None:
            data["dstaddr"] = dstaddr
        if internet_service is not None:
            data[param_map["internet_service"]] = internet_service
        if internet_service_custom is not None:
            data[param_map["internet_service_custom"]] = internet_service_custom
        if internet_service_fortiguard is not None:
            data[param_map["internet_service_fortiguard"]] = internet_service_fortiguard
        if link_monitor_exempt is not None:
            data[param_map["link_monitor_exempt"]] = link_monitor_exempt
        if tag is not None:
            data["tag"] = tag
        if vrf is not None:
            data["vrf"] = vrf
        if bfd is not None:
            data["bfd"] = bfd

        # Add any additional kwargs
        data.update(kwargs)

        return self._client.post("cmdb", "router/static", data=data, vdom=vdom)

    def put(
        self,
        seq_num: int,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        dst: Optional[str] = None,
        src: Optional[str] = None,
        gateway: Optional[str] = None,
        preferred_source: Optional[str] = None,
        distance: Optional[int] = None,
        weight: Optional[int] = None,
        priority: Optional[int] = None,
        device: Optional[str] = None,
        comment: Optional[str] = None,
        blackhole: Optional[str] = None,
        dynamic_gateway: Optional[str] = None,
        sdwan_zone: Optional[list] = None,
        dstaddr: Optional[str] = None,
        internet_service: Optional[int] = None,
        internet_service_custom: Optional[str] = None,
        internet_service_fortiguard: Optional[str] = None,
        link_monitor_exempt: Optional[str] = None,
        tag: Optional[int] = None,
        vrf: Optional[int] = None,
        bfd: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update IPv4 static route.

        Supports three usage patterns:
        1. Dictionary: update(1, data_dict={'gateway': '192.168.1.2', 'comment': 'Updated'})
        2. Keywords: update(1, gateway='192.168.1.2', comment='Updated')
        3. Mixed: update(1, data_dict={...}, gateway='override')

        Args:
            seq_num: Sequence number of the route to update (required)
            data_dict: Complete route dictionary (Python snake_case keys)
            status: Enable/disable this static route ('enable', 'disable')
            dst: Destination IP and mask for this route
            src: Source prefix for this route
            gateway: Gateway IP for this route
            preferred_source: Preferred source IP for this route
            distance: Administrative distance (1-255)
            weight: Administrative weight (0-255)
            priority: Administrative priority (1-65535)
            device: Gateway out interface or tunnel (max 35 chars)
            comment: Optional comments (max 255 chars)
            blackhole: Enable/disable black hole ('enable', 'disable')
            dynamic_gateway: Enable use of dynamic gateway from DHCP/PPP ('enable', 'disable')
            sdwan_zone: List of SD-WAN zones [{'name': 'zone1'}, ...]
            dstaddr: Name of firewall address or address group (max 79 chars)
            internet_service: Application ID in Internet service database (0-4294967295)
            internet_service_custom: Application name in Internet service custom database (max 64 chars)
            internet_service_fortiguard: Application name in Internet service fortiguard database (max 64 chars)
            link_monitor_exempt: Keep route when link monitor down ('enable', 'disable')
            tag: Route tag (0-4294967295)
            vrf: Virtual Routing Forwarding ID (0-511)
            bfd: Enable/disable BFD ('enable', 'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # PUT - Update gateway
            >>> result = fgt.api.cmdb.router.static.update(
            ...     seq_num=1,
            ...     gateway='192.168.1.254'
            ... )

            >>> # PUT - Update multiple fields
            >>> result = fgt.api.cmdb.router.static.update(
            ...     seq_num=1,
            ...     priority=20,
            ...     comment='Updated priority',
            ...     distance=15
            ... )
        """
        # Start with data_dict or empty dict
        data = data_dict.copy() if data_dict else {}

        # Map Python parameter names to API field names
        param_map = {
            "seq_num": "seq-num",
            "preferred_source": "preferred-source",
            "dynamic_gateway": "dynamic-gateway",
            "sdwan_zone": "sdwan-zone",
            "internet_service": "internet-service",
            "internet_service_custom": "internet-service-custom",
            "internet_service_fortiguard": "internet-service-fortiguard",
            "link_monitor_exempt": "link-monitor-exempt",
        }

        # Apply individual parameters (override data_dict if provided)
        if status is not None:
            data["status"] = status
        if dst is not None:
            data["dst"] = dst
        if src is not None:
            data["src"] = src
        if gateway is not None:
            data["gateway"] = gateway
        if preferred_source is not None:
            data[param_map["preferred_source"]] = preferred_source
        if distance is not None:
            data["distance"] = distance
        if weight is not None:
            data["weight"] = weight
        if priority is not None:
            data["priority"] = priority
        if device is not None:
            data["device"] = device
        if comment is not None:
            data["comment"] = comment
        if blackhole is not None:
            data["blackhole"] = blackhole
        if dynamic_gateway is not None:
            data[param_map["dynamic_gateway"]] = dynamic_gateway
        if sdwan_zone is not None:
            data[param_map["sdwan_zone"]] = sdwan_zone
        if dstaddr is not None:
            data["dstaddr"] = dstaddr
        if internet_service is not None:
            data[param_map["internet_service"]] = internet_service
        if internet_service_custom is not None:
            data[param_map["internet_service_custom"]] = internet_service_custom
        if internet_service_fortiguard is not None:
            data[param_map["internet_service_fortiguard"]] = internet_service_fortiguard
        if link_monitor_exempt is not None:
            data[param_map["link_monitor_exempt"]] = link_monitor_exempt
        if tag is not None:
            data["tag"] = tag
        if vrf is not None:
            data["vrf"] = vrf
        if bfd is not None:
            data["bfd"] = bfd

        # Add any additional kwargs
        data.update(kwargs)

        path = f"router/static/{encode_path_component(str(seq_num))}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(
        self, seq_num: int, vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete IPv4 static route.

        Args:
            seq_num: Sequence number of the route to delete
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete static route
            >>> result = fgt.api.cmdb.router.static.delete(seq_num=1)
        """
        path = f"router/static/{encode_path_component(str(seq_num))}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, seq_num: int, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if static route exists.

        Args:
            seq_num: Sequence number of the route
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if route exists, False otherwise

        Examples:
            >>> # Check if route exists
            >>> if fgt.api.cmdb.router.static.exists(seq_num=1):
            ...     print("Route exists")
        """
        try:
            self.get(seq_num=seq_num, vdom=vdom)
            return True
        except Exception:
            return False
