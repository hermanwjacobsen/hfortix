"""
FortiOS CMDB - System link_monitor

Configuration endpoint for managing cmdb system/link_monitor objects.

API Endpoints:
    GET    /cmdb/system/link_monitor
    POST   /cmdb/system/link_monitor
    PUT    /cmdb/system/link_monitor/{identifier}
    DELETE /cmdb/system/link_monitor/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_link_monitor.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_link_monitor.post(
    ...     name="example",
    ...     srcintf="port1",  # Auto-converted to [{'name': 'port1'}]
    ...     dstintf=["port2", "port3"],  # Auto-converted to list of dicts
    ... )

Important:
    - Use **POST** to create new objects
    - Use **PUT** to update existing objects
    - Use **GET** to retrieve configuration
    - Use **DELETE** to remove objects
    - **Auto-normalization**: List fields accept strings or lists, automatically
      converted to FortiOS format [{'name': '...'}]
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine
    from hfortix_core.http.interface import IHTTPClient
    from hfortix_fortios.models import FortiObject

# Import helper functions from central _helpers module
from hfortix_fortios._helpers import (
    build_api_payload,
    build_cmdb_payload,  # Keep for backward compatibility / manual usage
    is_success,
    normalize_table_field,  # For table field normalization
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class LinkMonitor(CRUDEndpoint, MetadataMixin):
    """LinkMonitor Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "link_monitor"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "server": {
            "mkey": "address",
            "required_fields": ['address'],
            "example": "[{'address': 'value'}]",
        },
        "route": {
            "mkey": "subnet",
            "required_fields": ['subnet'],
            "example": "[{'subnet': 'value'}]",
        },
        "server_list": {
            "mkey": "id",
            "required_fields": ['id', 'dst'],
            "example": "[{'id': 1, 'dst': 'value'}]",
        },
    }
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = True
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = True
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize LinkMonitor endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        name: str | None = None,
        filter: list[str] | None = None,
        count: int | None = None,
        start: int | None = None,
        q_datasource: bool | None = None,
        q_skip_to: int | None = None,
        q_with_meta: bool | None = None,
        q_with_contents_hash: bool | None = None,
        q_skip: bool | None = None,
        q_format: list[str] | None = None,
        q_key: str | None = None,
        q_pattern: str | None = None,
        q_scope: str | None = None,
        q_exclude_default_values: bool | None = None,
        q_datasource_format: dict[str, Any] | None = None,
        q_unfiltered_count: int | None = None,
        q_stat_items: str | None = None,
        q_primary_keys: str | None = None,
        q_action: Literal["default", "schema"] | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Retrieve system/link_monitor configuration.

        Configure Link Health Monitor.

        Args:
            name: String identifier to retrieve specific object.
                If None, returns all objects.
            filter: List of filter expressions to limit results.
                Each filter uses format: "field==value" or "field!=value"
                Operators: ==, !=, =@ (contains), !@ (not contains), <=, <, >=, >
                Multiple filters use AND logic. For OR, use comma in single string.
                Example: ["name==test", "status==enable"] or ["name==test,name==prod"]
            count: Maximum number of entries to return (pagination).
            start: Starting entry index for pagination (0-based).
            payload_dict: Additional query parameters for advanced options:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include metadata about each object
                - with_contents_hash (bool): Include checksum of object contents
                - format (list[str]): Property names to include (e.g., ["policyid", "srcintf"])
                - scope (str): Query scope - "global", "vdom", or "both"
                - action (str): Special actions - "schema", "default"
                See FortiOS REST API documentation for complete list.
            vdom: Virtual domain name. Use True for global, string for specific VDOM, None for default.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance or list of FortiObject instances. Returns Coroutine if using async client.
            Use .dict, .json, or .raw properties to access as dictionary.
            
            Response structure:
                - http_method: GET
                - results: Configuration object(s)
                - vdom: Virtual domain
                - path: API path
                - name: Object name (single object queries)
                - status: success/error
                - http_status: HTTP status code
                - build: FortiOS build number

        Examples:
            >>> # Get all system/link_monitor objects
            >>> result = fgt.api.cmdb.system_link_monitor.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/link_monitor by name
            >>> result = fgt.api.cmdb.system_link_monitor.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_link_monitor.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_link_monitor.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_link_monitor.get_schema()

        See Also:
            - post(): Create new system/link_monitor object
            - put(): Update existing system/link_monitor object
            - delete(): Remove system/link_monitor object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Add explicit query parameters
        if filter is not None:
            params["filter"] = filter
        if count is not None:
            params["count"] = count
        if start is not None:
            params["start"] = start
        if q_datasource is not None:
            params["datasource"] = q_datasource
        if q_skip_to is not None:
            params["skip_to"] = q_skip_to
        if q_with_meta is not None:
            params["with_meta"] = q_with_meta
        if q_with_contents_hash is not None:
            params["with_contents_hash"] = q_with_contents_hash
        if q_skip is not None:
            params["skip"] = q_skip
        if q_format is not None:
            params["format"] = q_format
        if q_key is not None:
            params["key"] = q_key
        if q_pattern is not None:
            params["pattern"] = q_pattern
        if q_scope is not None:
            params["scope"] = q_scope
        if q_exclude_default_values is not None:
            params["exclude-default-values"] = q_exclude_default_values
        if q_datasource_format is not None:
            params["datasource_format"] = q_datasource_format
        if q_unfiltered_count is not None:
            params["unfiltered_count"] = q_unfiltered_count
        if q_stat_items is not None:
            params["stat-items"] = q_stat_items
        if q_primary_keys is not None:
            params["primary_keys"] = q_primary_keys
        if q_action is not None:
            params["action"] = q_action
        
        if name:
            endpoint = "/system/link-monitor/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/system/link-monitor"
            unwrap_single = False
        
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
        )

    def get_schema(
        self,
        vdom: str | None = None,
        format: str = "schema",
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get schema/metadata for this endpoint.
        
        Returns the FortiOS schema definition including available fields,
        their types, required vs optional properties, enum values, nested
        structures, and default values.
        
        This queries the live firewall for its current schema, which may
        vary between FortiOS versions.
        
        Args:
            vdom: Virtual domain. None uses default VDOM.
            format: Schema format - "schema" (FortiOS native) or "json-schema" (JSON Schema standard).
                Defaults to "schema".
                
        Returns:
            Schema definition as dict. Returns Coroutine if using async client.
            
        Example:
            >>> # Get FortiOS native schema
            >>> schema = fgt.api.cmdb.system_link_monitor.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_link_monitor.get_schema(format="json-schema")
        
        Note:
            Not all endpoints support all schema formats. The "schema" format
            is most widely supported.
        """
        return self.get(action=format, vdom=vdom)


    # ========================================================================
    # PUT Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        addr_mode: Literal["ipv4", "ipv6"] | None = None,
        srcintf: str | None = None,
        server_config: Literal["default", "individual"] | None = None,
        server_type: Literal["static", "dynamic"] | None = None,
        server: str | list[str] | list[dict[str, Any]] | None = None,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = None,
        port: int | None = None,
        gateway_ip: str | None = None,
        gateway_ip6: str | None = None,
        route: str | list[str] | list[dict[str, Any]] | None = None,
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
        security_mode: Literal["none", "authentication"] | None = None,
        password: Any | None = None,
        packet_size: int | None = None,
        ha_priority: int | None = None,
        fail_weight: int | None = None,
        update_cascade_interface: Literal["enable", "disable"] | None = None,
        update_static_route: Literal["enable", "disable"] | None = None,
        update_policy_route: Literal["enable", "disable"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        diffservcode: str | None = None,
        class_id: int | None = None,
        service_detection: Literal["enable", "disable"] | None = None,
        server_list: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/link_monitor object.

        Configure Link Health Monitor.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Link monitor name.
            addr_mode: Address mode (IPv4 or IPv6).
            srcintf: Interface that receives the traffic to be monitored.
            server_config: Mode of server configuration.
            server_type: Server type (static or dynamic).
            server: IP address of the server(s) to be monitored.
                Default format: [{'address': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'address': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'address': 'val1'}, ...]
                  - List of dicts: [{'address': 'value'}] (recommended)
            protocol: Protocols used to monitor the server.
            port: Port number of the traffic to be used to monitor the server.
            gateway_ip: Gateway IP address used to probe the server.
            gateway_ip6: Gateway IPv6 address used to probe the server.
            route: Subnet to monitor.
                Default format: [{'subnet': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'subnet': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'subnet': 'val1'}, ...]
                  - List of dicts: [{'subnet': 'value'}] (recommended)
            source_ip: Source IP address used in packet to the server.
            source_ip6: Source IPv6 address used in packet to the server.
            http_get: If you are monitoring an HTML server you can send an HTTP-GET request with a custom string. Use this option to define the string.
            http_agent: String in the http-agent field in the HTTP header.
            http_match: String that you expect to see in the HTTP-GET requests of the traffic to be monitored.
            interval: Detection interval in milliseconds (20 - 3600 * 1000 msec, default = 500).
            probe_timeout: Time to wait before a probe packet is considered lost (20 - 5000 msec, default = 500).
            failtime: Number of retry attempts before the server is considered down (1 - 3600, default = 5).
            recoverytime: Number of successful responses received before server is considered recovered (1 - 3600, default = 5).
            probe_count: Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).
            security_mode: Twamp controller security mode.
            password: TWAMP controller password in authentication mode.
            packet_size: Packet size of a TWAMP test session (124/158 - 1024).
            ha_priority: HA election priority (1 - 50).
            fail_weight: Threshold weight to trigger link failure alert.
            update_cascade_interface: Enable/disable update cascade interface.
            update_static_route: Enable/disable updating the static route.
            update_policy_route: Enable/disable updating the policy route.
            status: Enable/disable this link monitor.
            diffservcode: Differentiated services code point (DSCP) in the IP header of the probe packet.
            class_id: Traffic class ID.
            service_detection: Only use monitor to read quality values. If enabled, static routes and cascade interfaces will not be updated.
            server_list: Servers for link-monitor to monitor.
                Default format: [{'id': 1, 'dst': 'value'}]
                Required format: List of dicts with keys: id, dst
                  (String format not allowed due to multiple required fields)
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_link_monitor.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_link_monitor.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if server is not None:
            server = normalize_table_field(
                server,
                mkey="address",
                required_fields=['address'],
                field_name="server",
                example="[{'address': 'value'}]",
            )
        if route is not None:
            route = normalize_table_field(
                route,
                mkey="subnet",
                required_fields=['subnet'],
                field_name="route",
                example="[{'subnet': 'value'}]",
            )
        if server_list is not None:
            server_list = normalize_table_field(
                server_list,
                mkey="id",
                required_fields=['id', 'dst'],
                field_name="server_list",
                example="[{'id': 1, 'dst': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            addr_mode=addr_mode,
            srcintf=srcintf,
            server_config=server_config,
            server_type=server_type,
            server=server,
            protocol=protocol,
            port=port,
            gateway_ip=gateway_ip,
            gateway_ip6=gateway_ip6,
            route=route,
            source_ip=source_ip,
            source_ip6=source_ip6,
            http_get=http_get,
            http_agent=http_agent,
            http_match=http_match,
            interval=interval,
            probe_timeout=probe_timeout,
            failtime=failtime,
            recoverytime=recoverytime,
            probe_count=probe_count,
            security_mode=security_mode,
            password=password,
            packet_size=packet_size,
            ha_priority=ha_priority,
            fail_weight=fail_weight,
            update_cascade_interface=update_cascade_interface,
            update_static_route=update_static_route,
            update_policy_route=update_policy_route,
            status=status,
            diffservcode=diffservcode,
            class_id=class_id,
            service_detection=service_detection,
            server_list=server_list,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.link_monitor import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/link_monitor",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/system/link-monitor/" + str(name_value)

        # Add explicit query parameters for PUT
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_before is not None:
            params["before"] = q_before
        if q_after is not None:
            params["after"] = q_after
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.put(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )

    # ========================================================================
    # POST Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        addr_mode: Literal["ipv4", "ipv6"] | None = None,
        srcintf: str | None = None,
        server_config: Literal["default", "individual"] | None = None,
        server_type: Literal["static", "dynamic"] | None = None,
        server: str | list[str] | list[dict[str, Any]] | None = None,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | None = None,
        port: int | None = None,
        gateway_ip: str | None = None,
        gateway_ip6: str | None = None,
        route: str | list[str] | list[dict[str, Any]] | None = None,
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
        security_mode: Literal["none", "authentication"] | None = None,
        password: Any | None = None,
        packet_size: int | None = None,
        ha_priority: int | None = None,
        fail_weight: int | None = None,
        update_cascade_interface: Literal["enable", "disable"] | None = None,
        update_static_route: Literal["enable", "disable"] | None = None,
        update_policy_route: Literal["enable", "disable"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        diffservcode: str | None = None,
        class_id: int | None = None,
        service_detection: Literal["enable", "disable"] | None = None,
        server_list: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new system/link_monitor object.

        Configure Link Health Monitor.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Link monitor name.
            addr_mode: Address mode (IPv4 or IPv6).
            srcintf: Interface that receives the traffic to be monitored.
            server_config: Mode of server configuration.
            server_type: Server type (static or dynamic).
            server: IP address of the server(s) to be monitored.
                Default format: [{'address': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'address': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'address': 'val1'}, ...]
                  - List of dicts: [{'address': 'value'}] (recommended)
            protocol: Protocols used to monitor the server.
            port: Port number of the traffic to be used to monitor the server.
            gateway_ip: Gateway IP address used to probe the server.
            gateway_ip6: Gateway IPv6 address used to probe the server.
            route: Subnet to monitor.
                Default format: [{'subnet': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'subnet': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'subnet': 'val1'}, ...]
                  - List of dicts: [{'subnet': 'value'}] (recommended)
            source_ip: Source IP address used in packet to the server.
            source_ip6: Source IPv6 address used in packet to the server.
            http_get: If you are monitoring an HTML server you can send an HTTP-GET request with a custom string. Use this option to define the string.
            http_agent: String in the http-agent field in the HTTP header.
            http_match: String that you expect to see in the HTTP-GET requests of the traffic to be monitored.
            interval: Detection interval in milliseconds (20 - 3600 * 1000 msec, default = 500).
            probe_timeout: Time to wait before a probe packet is considered lost (20 - 5000 msec, default = 500).
            failtime: Number of retry attempts before the server is considered down (1 - 3600, default = 5).
            recoverytime: Number of successful responses received before server is considered recovered (1 - 3600, default = 5).
            probe_count: Number of most recent probes that should be used to calculate latency and jitter (5 - 30, default = 30).
            security_mode: Twamp controller security mode.
            password: TWAMP controller password in authentication mode.
            packet_size: Packet size of a TWAMP test session (124/158 - 1024).
            ha_priority: HA election priority (1 - 50).
            fail_weight: Threshold weight to trigger link failure alert.
            update_cascade_interface: Enable/disable update cascade interface.
            update_static_route: Enable/disable updating the static route.
            update_policy_route: Enable/disable updating the policy route.
            status: Enable/disable this link monitor.
            diffservcode: Differentiated services code point (DSCP) in the IP header of the probe packet.
            class_id: Traffic class ID.
            service_detection: Only use monitor to read quality values. If enabled, static routes and cascade interfaces will not be updated.
            server_list: Servers for link-monitor to monitor.
                Default format: [{'id': 1, 'dst': 'value'}]
                Required format: List of dicts with keys: id, dst
                  (String format not allowed due to multiple required fields)
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_link_monitor.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = LinkMonitor.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_link_monitor.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(LinkMonitor.required_fields()) }}
            
            Use LinkMonitor.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if server is not None:
            server = normalize_table_field(
                server,
                mkey="address",
                required_fields=['address'],
                field_name="server",
                example="[{'address': 'value'}]",
            )
        if route is not None:
            route = normalize_table_field(
                route,
                mkey="subnet",
                required_fields=['subnet'],
                field_name="route",
                example="[{'subnet': 'value'}]",
            )
        if server_list is not None:
            server_list = normalize_table_field(
                server_list,
                mkey="id",
                required_fields=['id', 'dst'],
                field_name="server_list",
                example="[{'id': 1, 'dst': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            addr_mode=addr_mode,
            srcintf=srcintf,
            server_config=server_config,
            server_type=server_type,
            server=server,
            protocol=protocol,
            port=port,
            gateway_ip=gateway_ip,
            gateway_ip6=gateway_ip6,
            route=route,
            source_ip=source_ip,
            source_ip6=source_ip6,
            http_get=http_get,
            http_agent=http_agent,
            http_match=http_match,
            interval=interval,
            probe_timeout=probe_timeout,
            failtime=failtime,
            recoverytime=recoverytime,
            probe_count=probe_count,
            security_mode=security_mode,
            password=password,
            packet_size=packet_size,
            ha_priority=ha_priority,
            fail_weight=fail_weight,
            update_cascade_interface=update_cascade_interface,
            update_static_route=update_static_route,
            update_policy_route=update_policy_route,
            status=status,
            diffservcode=diffservcode,
            class_id=class_id,
            service_detection=service_detection,
            server_list=server_list,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.link_monitor import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/link_monitor",
            )

        endpoint = "/system/link-monitor"
        
        # Add explicit query parameters for POST
        params: dict[str, Any] = {}
        if q_action is not None:
            params["action"] = q_action
        if q_nkey is not None:
            params["nkey"] = q_nkey
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.post(
            "cmdb", endpoint, data=payload_data, params=params, vdom=vdom
        )

    # ========================================================================
    # DELETE Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def delete(
        self,
        name: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete system/link_monitor object.

        Configure Link Health Monitor.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_link_monitor.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/system/link-monitor/" + str(name)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/link_monitor object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_link_monitor.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_link_monitor.exists(name=1):
            ...     fgt.api.cmdb.system_link_monitor.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            
            if isinstance(response, dict):
                # Synchronous response - check status
                return is_success(response)
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await response
                    return is_success(r)
                return _check()
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        name: str | None = None,
        addr_mode: Literal["ipv4", "ipv6"] | None = None,
        srcintf: str | None = None,
        server_config: Literal["default", "individual"] | None = None,
        server_type: Literal["static", "dynamic"] | None = None,
        server: str | list[str] | list[dict[str, Any]] | None = None,
        protocol: Literal["ping", "tcp-echo", "udp-echo", "http", "https", "twamp"] | list[str] | list[dict[str, Any]] | None = None,
        port: int | None = None,
        gateway_ip: str | None = None,
        gateway_ip6: str | None = None,
        route: str | list[str] | list[dict[str, Any]] | None = None,
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
        security_mode: Literal["none", "authentication"] | None = None,
        password: Any | None = None,
        packet_size: int | None = None,
        ha_priority: int | None = None,
        fail_weight: int | None = None,
        update_cascade_interface: Literal["enable", "disable"] | None = None,
        update_static_route: Literal["enable", "disable"] | None = None,
        update_policy_route: Literal["enable", "disable"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        diffservcode: str | None = None,
        class_id: int | None = None,
        service_detection: Literal["enable", "disable"] | None = None,
        server_list: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/link_monitor object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            addr_mode: Field addr-mode
            srcintf: Field srcintf
            server_config: Field server-config
            server_type: Field server-type
            server: Field server
            protocol: Field protocol
            port: Field port
            gateway_ip: Field gateway-ip
            gateway_ip6: Field gateway-ip6
            route: Field route
            source_ip: Field source-ip
            source_ip6: Field source-ip6
            http_get: Field http-get
            http_agent: Field http-agent
            http_match: Field http-match
            interval: Field interval
            probe_timeout: Field probe-timeout
            failtime: Field failtime
            recoverytime: Field recoverytime
            probe_count: Field probe-count
            security_mode: Field security-mode
            password: Field password
            packet_size: Field packet-size
            ha_priority: Field ha-priority
            fail_weight: Field fail-weight
            update_cascade_interface: Field update-cascade-interface
            update_static_route: Field update-static-route
            update_policy_route: Field update-policy-route
            status: Field status
            diffservcode: Field diffservcode
            class_id: Field class-id
            service_detection: Field service-detection
            server_list: Field server-list
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.system_link_monitor.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_link_monitor.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_link_monitor.set(payload_dict=obj_data)
            >>> # Safely applies configuration regardless of current state

        Note:
            This method internally calls exists() then either post() or put().
            For performance-critical code with known state, call post() or put() directly.

        See Also:
            - post(): Create new object
            - put(): Update existing object
            - exists(): Check existence manually
        """
        # Build payload using helper function with auto-normalization
        payload_data = build_api_payload(
            name=name,
            addr_mode=addr_mode,
            srcintf=srcintf,
            server_config=server_config,
            server_type=server_type,
            server=server,
            protocol=protocol,
            port=port,
            gateway_ip=gateway_ip,
            gateway_ip6=gateway_ip6,
            route=route,
            source_ip=source_ip,
            source_ip6=source_ip6,
            http_get=http_get,
            http_agent=http_agent,
            http_match=http_match,
            interval=interval,
            probe_timeout=probe_timeout,
            failtime=failtime,
            recoverytime=recoverytime,
            probe_count=probe_count,
            security_mode=security_mode,
            password=password,
            packet_size=packet_size,
            ha_priority=ha_priority,
            fail_weight=fail_weight,
            update_cascade_interface=update_cascade_interface,
            update_static_route=update_static_route,
            update_policy_route=update_policy_route,
            status=status,
            diffservcode=diffservcode,
            class_id=class_id,
            service_detection=service_detection,
            server_list=server_list,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("name")
        if not mkey_value:
            raise ValueError("name is required for set()")
        
        # Check if resource exists
        if self.exists(name=mkey_value, vdom=vdom):
            # Update existing resource
            return self.put(payload_dict=payload_data, vdom=vdom, **kwargs)
        else:
            # Create new resource
            return self.post(payload_dict=payload_data, vdom=vdom, **kwargs)

    # ========================================================================
    # Action: Move
    # ========================================================================
    
    def move(
        self,
        name: str,
        action: Literal["before", "after"],
        reference_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/link_monitor object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_name: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_link_monitor.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/link-monitor",
            params={
                "name": name,
                "action": "move",
                action: reference_name,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        name: str,
        new_name: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/link_monitor object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Identifier of object to clone
            new_name: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_link_monitor.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/link-monitor",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Helper: Check Existence
    # ========================================================================
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/link_monitor object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_link_monitor.exists(name=1):
            ...     fgt.api.cmdb.system_link_monitor.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
                vdom=vdom
            )
            response = result.raw if hasattr(result, 'raw') else result
            # Check if response indicates success
            return is_success(response)
        except Exception as e:
            # 404 means object doesn't exist - return False
            # Any other error should be re-raised
            error_str = str(e)
            if '404' in error_str or 'Not Found' in error_str or 'ResourceNotFoundError' in str(type(e)):
                return False
            raise

