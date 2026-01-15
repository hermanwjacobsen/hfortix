"""
FortiOS CMDB - Router bgp

Configuration endpoint for managing cmdb router/bgp objects.

API Endpoints:
    GET    /cmdb/router/bgp
    POST   /cmdb/router/bgp
    PUT    /cmdb/router/bgp/{identifier}
    DELETE /cmdb/router/bgp/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_bgp.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.router_bgp.post(
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

class Bgp(CRUDEndpoint, MetadataMixin):
    """Bgp Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "bgp"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "confederation_peers": {
            "mkey": "peer",
            "required_fields": ['peer'],
            "example": "[{'peer': 'value'}]",
        },
        "aggregate_address": {
            "mkey": "id",
            "required_fields": ['id', 'prefix'],
            "example": "[{'id': 1, 'prefix': 'value'}]",
        },
        "aggregate_address6": {
            "mkey": "id",
            "required_fields": ['id', 'prefix6'],
            "example": "[{'id': 1, 'prefix6': 'value'}]",
        },
        "neighbor": {
            "mkey": "ip",
            "required_fields": ['ip', 'remote-as'],
            "example": "[{'ip': '192.168.1.10', 'remote-as': 'value'}]",
        },
        "neighbor_group": {
            "mkey": "name",
            "required_fields": ['name', 'remote-as', 'remote-as-filter'],
            "example": "[{'name': 'value', 'remote-as': 'value', 'remote-as-filter': 'value'}]",
        },
        "neighbor_range": {
            "mkey": "id",
            "required_fields": ['prefix', 'neighbor-group'],
            "example": "[{'prefix': 'value', 'neighbor-group': 'value'}]",
        },
        "neighbor_range6": {
            "mkey": "id",
            "required_fields": ['prefix6', 'neighbor-group'],
            "example": "[{'prefix6': 'value', 'neighbor-group': 'value'}]",
        },
        "network": {
            "mkey": "id",
            "required_fields": ['id', 'prefix'],
            "example": "[{'id': 1, 'prefix': 'value'}]",
        },
        "network6": {
            "mkey": "id",
            "required_fields": ['id', 'prefix6'],
            "example": "[{'id': 1, 'prefix6': 'value'}]",
        },
        "redistribute": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "redistribute6": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "admin_distance": {
            "mkey": "id",
            "required_fields": ['id', 'neighbour-prefix', 'distance'],
            "example": "[{'id': 1, 'neighbour-prefix': 'value', 'distance': 1}]",
        },
        "vrf": {
            "mkey": "vrf",
            "required_fields": ['vrf'],
            "example": "[{'vrf': 'value'}]",
        },
        "vrf6": {
            "mkey": "vrf",
            "required_fields": ['vrf'],
            "example": "[{'vrf': 'value'}]",
        },
    }
    
    # ========================================================================
    # Capabilities (from schema metadata)
    # ========================================================================
    SUPPORTS_CREATE = False
    SUPPORTS_READ = True
    SUPPORTS_UPDATE = True
    SUPPORTS_DELETE = False
    SUPPORTS_MOVE = True
    SUPPORTS_CLONE = True
    SUPPORTS_FILTERING = True
    SUPPORTS_PAGINATION = True
    SUPPORTS_SEARCH = False
    SUPPORTS_SORTING = False

    def __init__(self, client: "IHTTPClient"):
        """Initialize Bgp endpoint."""
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
        Retrieve router/bgp configuration.

        Configure BGP.

        Args:
            name: Name identifier to retrieve specific object. If None, returns all objects.
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
            >>> # Get all router/bgp objects
            >>> result = fgt.api.cmdb.router_bgp.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_bgp.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.router_bgp.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.router_bgp.get_schema()

        See Also:
            - post(): Create new router/bgp object
            - put(): Update existing router/bgp object
            - delete(): Remove router/bgp object
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
            endpoint = f"/router/bgp/{name}"
            unwrap_single = True
        else:
            endpoint = "/router/bgp"
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
            >>> schema = fgt.api.cmdb.router_bgp.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.router_bgp.get_schema(format="json-schema")
        
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
        asn: str | None = None,
        router_id: str | None = None,
        keepalive_timer: int | None = None,
        holdtime_timer: int | None = None,
        always_compare_med: Literal["enable", "disable"] | None = None,
        bestpath_as_path_ignore: Literal["enable", "disable"] | None = None,
        bestpath_cmp_confed_aspath: Literal["enable", "disable"] | None = None,
        bestpath_cmp_routerid: Literal["enable", "disable"] | None = None,
        bestpath_med_confed: Literal["enable", "disable"] | None = None,
        bestpath_med_missing_as_worst: Literal["enable", "disable"] | None = None,
        client_to_client_reflection: Literal["enable", "disable"] | None = None,
        dampening: Literal["enable", "disable"] | None = None,
        deterministic_med: Literal["enable", "disable"] | None = None,
        ebgp_multipath: Literal["enable", "disable"] | None = None,
        ibgp_multipath: Literal["enable", "disable"] | None = None,
        enforce_first_as: Literal["enable", "disable"] | None = None,
        fast_external_failover: Literal["enable", "disable"] | None = None,
        log_neighbour_changes: Literal["enable", "disable"] | None = None,
        network_import_check: Literal["enable", "disable"] | None = None,
        ignore_optional_capability: Literal["enable", "disable"] | None = None,
        additional_path: Literal["enable", "disable"] | None = None,
        additional_path6: Literal["enable", "disable"] | None = None,
        additional_path_vpnv4: Literal["enable", "disable"] | None = None,
        additional_path_vpnv6: Literal["enable", "disable"] | None = None,
        multipath_recursive_distance: Literal["enable", "disable"] | None = None,
        recursive_next_hop: Literal["enable", "disable"] | None = None,
        recursive_inherit_priority: Literal["enable", "disable"] | None = None,
        tag_resolve_mode: Literal["disable", "preferred", "merge", "merge-all"] | None = None,
        cluster_id: str | None = None,
        confederation_identifier: int | None = None,
        confederation_peers: str | list[str] | list[dict[str, Any]] | None = None,
        dampening_route_map: str | None = None,
        dampening_reachability_half_life: int | None = None,
        dampening_reuse: int | None = None,
        dampening_suppress: int | None = None,
        dampening_max_suppress_time: int | None = None,
        dampening_unreachability_half_life: int | None = None,
        default_local_preference: int | None = None,
        scan_time: int | None = None,
        distance_external: int | None = None,
        distance_internal: int | None = None,
        distance_local: int | None = None,
        synchronization: Literal["enable", "disable"] | None = None,
        graceful_restart: Literal["enable", "disable"] | None = None,
        graceful_restart_time: int | None = None,
        graceful_stalepath_time: int | None = None,
        graceful_update_delay: int | None = None,
        graceful_end_on_timer: Literal["enable", "disable"] | None = None,
        additional_path_select: int | None = None,
        additional_path_select6: int | None = None,
        additional_path_select_vpnv4: int | None = None,
        additional_path_select_vpnv6: int | None = None,
        cross_family_conditional_adv: Literal["enable", "disable"] | None = None,
        aggregate_address: str | list[str] | list[dict[str, Any]] | None = None,
        aggregate_address6: str | list[str] | list[dict[str, Any]] | None = None,
        neighbor: str | list[str] | list[dict[str, Any]] | None = None,
        neighbor_group: str | list[str] | list[dict[str, Any]] | None = None,
        neighbor_range: str | list[str] | list[dict[str, Any]] | None = None,
        neighbor_range6: str | list[str] | list[dict[str, Any]] | None = None,
        network: str | list[str] | list[dict[str, Any]] | None = None,
        network6: str | list[str] | list[dict[str, Any]] | None = None,
        redistribute: str | list[str] | list[dict[str, Any]] | None = None,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = None,
        admin_distance: str | list[str] | list[dict[str, Any]] | None = None,
        vrf: str | list[str] | list[dict[str, Any]] | None = None,
        vrf6: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing router/bgp object.

        Configure BGP.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            asn: Router AS number, asplain/asdot/asdot+ format, 0 to disable BGP.
            router_id: Router ID.
            keepalive_timer: Frequency to send keep alive requests.
            holdtime_timer: Number of seconds to mark peer as dead.
            always_compare_med: Enable/disable always compare MED.
            bestpath_as_path_ignore: Enable/disable ignore AS path.
            bestpath_cmp_confed_aspath: Enable/disable compare federation AS path length.
            bestpath_cmp_routerid: Enable/disable compare router ID for identical EBGP paths.
            bestpath_med_confed: Enable/disable compare MED among confederation paths.
            bestpath_med_missing_as_worst: Enable/disable treat missing MED as least preferred.
            client_to_client_reflection: Enable/disable client-to-client route reflection.
            dampening: Enable/disable route-flap dampening.
            deterministic_med: Enable/disable enforce deterministic comparison of MED.
            ebgp_multipath: Enable/disable EBGP multi-path.
            ibgp_multipath: Enable/disable IBGP multi-path.
            enforce_first_as: Enable/disable enforce first AS for EBGP routes.
            fast_external_failover: Enable/disable reset peer BGP session if link goes down.
            log_neighbour_changes: Log BGP neighbor changes.
            network_import_check: Enable/disable ensure BGP network route exists in IGP.
            ignore_optional_capability: Do not send unknown optional capability notification message.
            additional_path: Enable/disable selection of BGP IPv4 additional paths.
            additional_path6: Enable/disable selection of BGP IPv6 additional paths.
            additional_path_vpnv4: Enable/disable selection of BGP VPNv4 additional paths.
            additional_path_vpnv6: Enable/disable selection of BGP VPNv6 additional paths.
            multipath_recursive_distance: Enable/disable use of recursive distance to select multipath.
            recursive_next_hop: Enable/disable recursive resolution of next-hop using BGP route.
            recursive_inherit_priority: Enable/disable priority inheritance for recursive resolution.
            tag_resolve_mode: Configure tag-match mode. Resolves BGP routes with other routes containing the same tag.
            cluster_id: Route reflector cluster ID.
            confederation_identifier: Confederation identifier.
            confederation_peers: Confederation peers.
                Default format: [{'peer': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'peer': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'peer': 'val1'}, ...]
                  - List of dicts: [{'peer': 'value'}] (recommended)
            dampening_route_map: Criteria for dampening.
            dampening_reachability_half_life: Reachability half-life time for penalty (min).
            dampening_reuse: Threshold to reuse routes.
            dampening_suppress: Threshold to suppress routes.
            dampening_max_suppress_time: Maximum minutes a route can be suppressed.
            dampening_unreachability_half_life: Unreachability half-life time for penalty (min).
            default_local_preference: Default local preference.
            scan_time: Background scanner interval (sec), 0 to disable it.
            distance_external: Distance for routes external to the AS.
            distance_internal: Distance for routes internal to the AS.
            distance_local: Distance for routes local to the AS.
            synchronization: Enable/disable only advertise routes from iBGP if routes present in an IGP.
            graceful_restart: Enable/disable BGP graceful restart capabilities.
            graceful_restart_time: Time needed for neighbors to restart (sec).
            graceful_stalepath_time: Time to hold stale paths of restarting neighbor (sec).
            graceful_update_delay: Route advertisement/selection delay after restart (sec).
            graceful_end_on_timer: Enable/disable to exit graceful restart on timer only.
            additional_path_select: Number of additional paths to be selected for each IPv4 NLRI.
            additional_path_select6: Number of additional paths to be selected for each IPv6 NLRI.
            additional_path_select_vpnv4: Number of additional paths to be selected for each VPNv4 NLRI.
            additional_path_select_vpnv6: Number of additional paths to be selected for each VPNv6 NLRI.
            cross_family_conditional_adv: Enable/disable cross address family conditional advertisement.
            aggregate_address: BGP aggregate address table.
                Default format: [{'id': 1, 'prefix': 'value'}]
                Required format: List of dicts with keys: id, prefix
                  (String format not allowed due to multiple required fields)
            aggregate_address6: BGP IPv6 aggregate address table.
                Default format: [{'id': 1, 'prefix6': 'value'}]
                Required format: List of dicts with keys: id, prefix6
                  (String format not allowed due to multiple required fields)
            neighbor: BGP neighbor table.
                Default format: [{'ip': '192.168.1.10', 'remote-as': 'value'}]
                Required format: List of dicts with keys: ip, remote-as
                  (String format not allowed due to multiple required fields)
            neighbor_group: BGP neighbor group table.
                Default format: [{'name': 'value', 'remote-as': 'value', 'remote-as-filter': 'value'}]
                Required format: List of dicts with keys: name, remote-as, remote-as-filter
                  (String format not allowed due to multiple required fields)
            neighbor_range: BGP neighbor range table.
                Default format: [{'prefix': 'value', 'neighbor-group': 'value'}]
                Required format: List of dicts with keys: prefix, neighbor-group
                  (String format not allowed due to multiple required fields)
            neighbor_range6: BGP IPv6 neighbor range table.
                Default format: [{'prefix6': 'value', 'neighbor-group': 'value'}]
                Required format: List of dicts with keys: prefix6, neighbor-group
                  (String format not allowed due to multiple required fields)
            network: BGP network table.
                Default format: [{'id': 1, 'prefix': 'value'}]
                Required format: List of dicts with keys: id, prefix
                  (String format not allowed due to multiple required fields)
            network6: BGP IPv6 network table.
                Default format: [{'id': 1, 'prefix6': 'value'}]
                Required format: List of dicts with keys: id, prefix6
                  (String format not allowed due to multiple required fields)
            redistribute: BGP IPv4 redistribute table.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            redistribute6: BGP IPv6 redistribute table.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            admin_distance: Administrative distance modifications.
                Default format: [{'id': 1, 'neighbour-prefix': 'value', 'distance': 1}]
                Required format: List of dicts with keys: id, neighbour-prefix, distance
                  (String format not allowed due to multiple required fields)
            vrf: BGP VRF leaking table.
                Default format: [{'vrf': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'vrf': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'vrf': 'val1'}, ...]
                  - List of dicts: [{'vrf': 'value'}] (recommended)
            vrf6: BGP IPv6 VRF leaking table.
                Default format: [{'vrf': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'vrf': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'vrf': 'val1'}, ...]
                  - List of dicts: [{'vrf': 'value'}] (recommended)
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_bgp.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_bgp.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if confederation_peers is not None:
            confederation_peers = normalize_table_field(
                confederation_peers,
                mkey="peer",
                required_fields=['peer'],
                field_name="confederation_peers",
                example="[{'peer': 'value'}]",
            )
        if aggregate_address is not None:
            aggregate_address = normalize_table_field(
                aggregate_address,
                mkey="id",
                required_fields=['id', 'prefix'],
                field_name="aggregate_address",
                example="[{'id': 1, 'prefix': 'value'}]",
            )
        if aggregate_address6 is not None:
            aggregate_address6 = normalize_table_field(
                aggregate_address6,
                mkey="id",
                required_fields=['id', 'prefix6'],
                field_name="aggregate_address6",
                example="[{'id': 1, 'prefix6': 'value'}]",
            )
        if neighbor is not None:
            neighbor = normalize_table_field(
                neighbor,
                mkey="ip",
                required_fields=['ip', 'remote-as'],
                field_name="neighbor",
                example="[{'ip': '192.168.1.10', 'remote-as': 'value'}]",
            )
        if neighbor_group is not None:
            neighbor_group = normalize_table_field(
                neighbor_group,
                mkey="name",
                required_fields=['name', 'remote-as', 'remote-as-filter'],
                field_name="neighbor_group",
                example="[{'name': 'value', 'remote-as': 'value', 'remote-as-filter': 'value'}]",
            )
        if neighbor_range is not None:
            neighbor_range = normalize_table_field(
                neighbor_range,
                mkey="id",
                required_fields=['prefix', 'neighbor-group'],
                field_name="neighbor_range",
                example="[{'prefix': 'value', 'neighbor-group': 'value'}]",
            )
        if neighbor_range6 is not None:
            neighbor_range6 = normalize_table_field(
                neighbor_range6,
                mkey="id",
                required_fields=['prefix6', 'neighbor-group'],
                field_name="neighbor_range6",
                example="[{'prefix6': 'value', 'neighbor-group': 'value'}]",
            )
        if network is not None:
            network = normalize_table_field(
                network,
                mkey="id",
                required_fields=['id', 'prefix'],
                field_name="network",
                example="[{'id': 1, 'prefix': 'value'}]",
            )
        if network6 is not None:
            network6 = normalize_table_field(
                network6,
                mkey="id",
                required_fields=['id', 'prefix6'],
                field_name="network6",
                example="[{'id': 1, 'prefix6': 'value'}]",
            )
        if redistribute is not None:
            redistribute = normalize_table_field(
                redistribute,
                mkey="name",
                required_fields=['name'],
                field_name="redistribute",
                example="[{'name': 'value'}]",
            )
        if redistribute6 is not None:
            redistribute6 = normalize_table_field(
                redistribute6,
                mkey="name",
                required_fields=['name'],
                field_name="redistribute6",
                example="[{'name': 'value'}]",
            )
        if admin_distance is not None:
            admin_distance = normalize_table_field(
                admin_distance,
                mkey="id",
                required_fields=['id', 'neighbour-prefix', 'distance'],
                field_name="admin_distance",
                example="[{'id': 1, 'neighbour-prefix': 'value', 'distance': 1}]",
            )
        if vrf is not None:
            vrf = normalize_table_field(
                vrf,
                mkey="vrf",
                required_fields=['vrf'],
                field_name="vrf",
                example="[{'vrf': 'value'}]",
            )
        if vrf6 is not None:
            vrf6 = normalize_table_field(
                vrf6,
                mkey="vrf",
                required_fields=['vrf'],
                field_name="vrf6",
                example="[{'vrf': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            asn=asn,
            router_id=router_id,
            keepalive_timer=keepalive_timer,
            holdtime_timer=holdtime_timer,
            always_compare_med=always_compare_med,
            bestpath_as_path_ignore=bestpath_as_path_ignore,
            bestpath_cmp_confed_aspath=bestpath_cmp_confed_aspath,
            bestpath_cmp_routerid=bestpath_cmp_routerid,
            bestpath_med_confed=bestpath_med_confed,
            bestpath_med_missing_as_worst=bestpath_med_missing_as_worst,
            client_to_client_reflection=client_to_client_reflection,
            dampening=dampening,
            deterministic_med=deterministic_med,
            ebgp_multipath=ebgp_multipath,
            ibgp_multipath=ibgp_multipath,
            enforce_first_as=enforce_first_as,
            fast_external_failover=fast_external_failover,
            log_neighbour_changes=log_neighbour_changes,
            network_import_check=network_import_check,
            ignore_optional_capability=ignore_optional_capability,
            additional_path=additional_path,
            additional_path6=additional_path6,
            additional_path_vpnv4=additional_path_vpnv4,
            additional_path_vpnv6=additional_path_vpnv6,
            multipath_recursive_distance=multipath_recursive_distance,
            recursive_next_hop=recursive_next_hop,
            recursive_inherit_priority=recursive_inherit_priority,
            tag_resolve_mode=tag_resolve_mode,
            cluster_id=cluster_id,
            confederation_identifier=confederation_identifier,
            confederation_peers=confederation_peers,
            dampening_route_map=dampening_route_map,
            dampening_reachability_half_life=dampening_reachability_half_life,
            dampening_reuse=dampening_reuse,
            dampening_suppress=dampening_suppress,
            dampening_max_suppress_time=dampening_max_suppress_time,
            dampening_unreachability_half_life=dampening_unreachability_half_life,
            default_local_preference=default_local_preference,
            scan_time=scan_time,
            distance_external=distance_external,
            distance_internal=distance_internal,
            distance_local=distance_local,
            synchronization=synchronization,
            graceful_restart=graceful_restart,
            graceful_restart_time=graceful_restart_time,
            graceful_stalepath_time=graceful_stalepath_time,
            graceful_update_delay=graceful_update_delay,
            graceful_end_on_timer=graceful_end_on_timer,
            additional_path_select=additional_path_select,
            additional_path_select6=additional_path_select6,
            additional_path_select_vpnv4=additional_path_select_vpnv4,
            additional_path_select_vpnv6=additional_path_select_vpnv6,
            cross_family_conditional_adv=cross_family_conditional_adv,
            aggregate_address=aggregate_address,
            aggregate_address6=aggregate_address6,
            neighbor=neighbor,
            neighbor_group=neighbor_group,
            neighbor_range=neighbor_range,
            neighbor_range6=neighbor_range6,
            network=network,
            network6=network6,
            redistribute=redistribute,
            redistribute6=redistribute6,
            admin_distance=admin_distance,
            vrf=vrf,
            vrf6=vrf6,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.bgp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/bgp",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/router/bgp"

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
        Move router/bgp object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            name: Name of object to move
            action: Move "before" or "after" reference object
            reference_name: Name of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.router_bgp.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/router/bgp",
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
        Clone router/bgp object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            name: Name of object to clone
            new_name: Name for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.router_bgp.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/router/bgp",
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
        Check if router/bgp object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.router_bgp.exists(name="myobj"):
            ...     fgt.api.cmdb.router_bgp.post(payload_dict=data)
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

