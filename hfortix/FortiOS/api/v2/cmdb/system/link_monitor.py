"""
FortiOS CMDB - System LinkMonitor

API Endpoints:
    GET    /system/link-monitor
    POST   /system/link-monitor
    GET    /system/link-monitor/{name}
    PUT    /system/link-monitor/{name}
    DELETE /system/link-monitor/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class LinkMonitor:
    """LinkMonitor operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LinkMonitor endpoint.

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
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false} (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if name:
            endpoint = f"/system/link-monitor/{name}"
        else:
            endpoint = "/system/link-monitor"
        if attr is not None:
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        addr_mode: str | None = None,
        srcintf: str | None = None,
        server_config: str | None = None,
        server_type: str | None = None,
        server: list | None = None,
        protocol: str | None = None,
        port: int | None = None,
        gateway_ip: str | None = None,
        gateway_ip6: str | None = None,
        route: list | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        http_get: str | None = None,
        http_agent: str | None = None,
        http_match: str | None = None,
        interval: int | None = None,
        probe_timeout: int | None = None,
        failtime: int | None = None,
        recoverytime: int | None = None,
        probe_count: int | None = None,
        security_mode: str | None = None,
        password: str | None = None,
        packet_size: int | None = None,
        ha_priority: int | None = None,
        fail_weight: int | None = None,
        update_cascade_interface: str | None = None,
        update_static_route: str | None = None,
        update_policy_route: str | None = None,
        status: str | None = None,
        diffservcode: str | None = None,
        class_id: int | None = None,
        service_detection: str | None = None,
        server_list: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: Link monitor name. (optional)
            addr_mode: Address mode (IPv4 or IPv6). (optional)
            srcintf: Interface that receives the traffic to be monitored. (optional)
            server_config: Mode of server configuration. (optional)
            server_type: Server type (static or dynamic). (optional)
            server: IP address of the server(s) to be monitored. (optional)
            protocol: Protocols used to monitor the server. (optional)
            port: Port number of the traffic to be used to monitor the server. (optional)
            gateway_ip: Gateway IP address used to probe the server. (optional)
            gateway_ip6: Gateway IPv6 address used to probe the server. (optional)
            route: Subnet to monitor. (optional)
            source_ip: Source IP address used in packet to the server. (optional)
            source_ip6: Source IPv6 address used in packet to the server. (optional)
            http_get: If you are monitoring an HTML server you can send an HTTP-GET request with a custom string. Use this option to define the string. (optional)
            http_agent: String in the http-agent field in the HTTP header. (optional)
            http_match: String that you expect to see in the HTTP-GET requests of the traffic to be monitored. (optional)
            interval: Detection interval in milliseconds (20 - 3600 * 1000 msec, default = 500). (optional)
            probe_timeout: Time to wait before a probe packet is considered lost (20 - 5000 msec, default = 500). (optional)
            failtime: Number of retry attempts before the server is considered down (1 - 3600, default = 5). (optional)
            recoverytime: Number of successful responses received before server is considered recovered (1 - 3600, default = 5). (optional)
            probe_count: Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30). (optional)
            security_mode: Twamp controller security mode. (optional)
            password: TWAMP controller password in authentication mode. (optional)
            packet_size: Packet size of a TWAMP test session (124/158 - 1024). (optional)
            ha_priority: HA election priority (1 - 50). (optional)
            fail_weight: Threshold weight to trigger link failure alert. (optional)
            update_cascade_interface: Enable/disable update cascade interface. (optional)
            update_static_route: Enable/disable updating the static route. (optional)
            update_policy_route: Enable/disable updating the policy route. (optional)
            status: Enable/disable this link monitor. (optional)
            diffservcode: Differentiated services code point (DSCP) in the IP header of the probe packet. (optional)
            class_id: Traffic class ID. (optional)
            service_detection: Only use monitor to read quality values. If enabled, static routes and cascade interfaces will not be updated. (optional)
            server_list: Servers for link-monitor to monitor. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/system/link-monitor/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if addr_mode is not None:
            data_payload['addr-mode'] = addr_mode
        if srcintf is not None:
            data_payload['srcintf'] = srcintf
        if server_config is not None:
            data_payload['server-config'] = server_config
        if server_type is not None:
            data_payload['server-type'] = server_type
        if server is not None:
            data_payload['server'] = server
        if protocol is not None:
            data_payload['protocol'] = protocol
        if port is not None:
            data_payload['port'] = port
        if gateway_ip is not None:
            data_payload['gateway-ip'] = gateway_ip
        if gateway_ip6 is not None:
            data_payload['gateway-ip6'] = gateway_ip6
        if route is not None:
            data_payload['route'] = route
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if source_ip6 is not None:
            data_payload['source-ip6'] = source_ip6
        if http_get is not None:
            data_payload['http-get'] = http_get
        if http_agent is not None:
            data_payload['http-agent'] = http_agent
        if http_match is not None:
            data_payload['http-match'] = http_match
        if interval is not None:
            data_payload['interval'] = interval
        if probe_timeout is not None:
            data_payload['probe-timeout'] = probe_timeout
        if failtime is not None:
            data_payload['failtime'] = failtime
        if recoverytime is not None:
            data_payload['recoverytime'] = recoverytime
        if probe_count is not None:
            data_payload['probe-count'] = probe_count
        if security_mode is not None:
            data_payload['security-mode'] = security_mode
        if password is not None:
            data_payload['password'] = password
        if packet_size is not None:
            data_payload['packet-size'] = packet_size
        if ha_priority is not None:
            data_payload['ha-priority'] = ha_priority
        if fail_weight is not None:
            data_payload['fail-weight'] = fail_weight
        if update_cascade_interface is not None:
            data_payload['update-cascade-interface'] = update_cascade_interface
        if update_static_route is not None:
            data_payload['update-static-route'] = update_static_route
        if update_policy_route is not None:
            data_payload['update-policy-route'] = update_policy_route
        if status is not None:
            data_payload['status'] = status
        if diffservcode is not None:
            data_payload['diffservcode'] = diffservcode
        if class_id is not None:
            data_payload['class-id'] = class_id
        if service_detection is not None:
            data_payload['service-detection'] = service_detection
        if server_list is not None:
            data_payload['server-list'] = server_list
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            name: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/system/link-monitor/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        addr_mode: str | None = None,
        srcintf: str | None = None,
        server_config: str | None = None,
        server_type: str | None = None,
        server: list | None = None,
        protocol: str | None = None,
        port: int | None = None,
        gateway_ip: str | None = None,
        gateway_ip6: str | None = None,
        route: list | None = None,
        source_ip: str | None = None,
        source_ip6: str | None = None,
        http_get: str | None = None,
        http_agent: str | None = None,
        http_match: str | None = None,
        interval: int | None = None,
        probe_timeout: int | None = None,
        failtime: int | None = None,
        recoverytime: int | None = None,
        probe_count: int | None = None,
        security_mode: str | None = None,
        password: str | None = None,
        packet_size: int | None = None,
        ha_priority: int | None = None,
        fail_weight: int | None = None,
        update_cascade_interface: str | None = None,
        update_static_route: str | None = None,
        update_policy_route: str | None = None,
        status: str | None = None,
        diffservcode: str | None = None,
        class_id: int | None = None,
        service_detection: str | None = None,
        server_list: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: Link monitor name. (optional)
            addr_mode: Address mode (IPv4 or IPv6). (optional)
            srcintf: Interface that receives the traffic to be monitored. (optional)
            server_config: Mode of server configuration. (optional)
            server_type: Server type (static or dynamic). (optional)
            server: IP address of the server(s) to be monitored. (optional)
            protocol: Protocols used to monitor the server. (optional)
            port: Port number of the traffic to be used to monitor the server. (optional)
            gateway_ip: Gateway IP address used to probe the server. (optional)
            gateway_ip6: Gateway IPv6 address used to probe the server. (optional)
            route: Subnet to monitor. (optional)
            source_ip: Source IP address used in packet to the server. (optional)
            source_ip6: Source IPv6 address used in packet to the server. (optional)
            http_get: If you are monitoring an HTML server you can send an HTTP-GET request with a custom string. Use this option to define the string. (optional)
            http_agent: String in the http-agent field in the HTTP header. (optional)
            http_match: String that you expect to see in the HTTP-GET requests of the traffic to be monitored. (optional)
            interval: Detection interval in milliseconds (20 - 3600 * 1000 msec, default = 500). (optional)
            probe_timeout: Time to wait before a probe packet is considered lost (20 - 5000 msec, default = 500). (optional)
            failtime: Number of retry attempts before the server is considered down (1 - 3600, default = 5). (optional)
            recoverytime: Number of successful responses received before server is considered recovered (1 - 3600, default = 5). (optional)
            probe_count: Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30). (optional)
            security_mode: Twamp controller security mode. (optional)
            password: TWAMP controller password in authentication mode. (optional)
            packet_size: Packet size of a TWAMP test session (124/158 - 1024). (optional)
            ha_priority: HA election priority (1 - 50). (optional)
            fail_weight: Threshold weight to trigger link failure alert. (optional)
            update_cascade_interface: Enable/disable update cascade interface. (optional)
            update_static_route: Enable/disable updating the static route. (optional)
            update_policy_route: Enable/disable updating the policy route. (optional)
            status: Enable/disable this link monitor. (optional)
            diffservcode: Differentiated services code point (DSCP) in the IP header of the probe packet. (optional)
            class_id: Traffic class ID. (optional)
            service_detection: Only use monitor to read quality values. If enabled, static routes and cascade interfaces will not be updated. (optional)
            server_list: Servers for link-monitor to monitor. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/system/link-monitor"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if addr_mode is not None:
            data_payload['addr-mode'] = addr_mode
        if srcintf is not None:
            data_payload['srcintf'] = srcintf
        if server_config is not None:
            data_payload['server-config'] = server_config
        if server_type is not None:
            data_payload['server-type'] = server_type
        if server is not None:
            data_payload['server'] = server
        if protocol is not None:
            data_payload['protocol'] = protocol
        if port is not None:
            data_payload['port'] = port
        if gateway_ip is not None:
            data_payload['gateway-ip'] = gateway_ip
        if gateway_ip6 is not None:
            data_payload['gateway-ip6'] = gateway_ip6
        if route is not None:
            data_payload['route'] = route
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if source_ip6 is not None:
            data_payload['source-ip6'] = source_ip6
        if http_get is not None:
            data_payload['http-get'] = http_get
        if http_agent is not None:
            data_payload['http-agent'] = http_agent
        if http_match is not None:
            data_payload['http-match'] = http_match
        if interval is not None:
            data_payload['interval'] = interval
        if probe_timeout is not None:
            data_payload['probe-timeout'] = probe_timeout
        if failtime is not None:
            data_payload['failtime'] = failtime
        if recoverytime is not None:
            data_payload['recoverytime'] = recoverytime
        if probe_count is not None:
            data_payload['probe-count'] = probe_count
        if security_mode is not None:
            data_payload['security-mode'] = security_mode
        if password is not None:
            data_payload['password'] = password
        if packet_size is not None:
            data_payload['packet-size'] = packet_size
        if ha_priority is not None:
            data_payload['ha-priority'] = ha_priority
        if fail_weight is not None:
            data_payload['fail-weight'] = fail_weight
        if update_cascade_interface is not None:
            data_payload['update-cascade-interface'] = update_cascade_interface
        if update_static_route is not None:
            data_payload['update-static-route'] = update_static_route
        if update_policy_route is not None:
            data_payload['update-policy-route'] = update_policy_route
        if status is not None:
            data_payload['status'] = status
        if diffservcode is not None:
            data_payload['diffservcode'] = diffservcode
        if class_id is not None:
            data_payload['class-id'] = class_id
        if service_detection is not None:
            data_payload['service-detection'] = service_detection
        if server_list is not None:
            data_payload['server-list'] = server_list
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
