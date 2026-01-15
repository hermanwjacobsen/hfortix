"""
FortiOS CMDB - Router ospf6

Configuration endpoint for managing cmdb router/ospf6 objects.

API Endpoints:
    GET    /cmdb/router/ospf6
    POST   /cmdb/router/ospf6
    PUT    /cmdb/router/ospf6/{identifier}
    DELETE /cmdb/router/ospf6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_ospf6.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.router_ospf6.post(
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

class Ospf6(CRUDEndpoint, MetadataMixin):
    """Ospf6 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "ospf6"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "area": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "ospf6_interface": {
            "mkey": "name",
            "required_fields": ['area-id', 'interface'],
            "example": "[{'area-id': '192.168.1.10', 'interface': 'value'}]",
        },
        "redistribute": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "passive_interface": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "summary_address": {
            "mkey": "id",
            "required_fields": ['prefix6'],
            "example": "[{'prefix6': 'value'}]",
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
        """Initialize Ospf6 endpoint."""
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
        Retrieve router/ospf6 configuration.

        Configure IPv6 OSPF.

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
            >>> # Get all router/ospf6 objects
            >>> result = fgt.api.cmdb.router_ospf6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_ospf6.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.router_ospf6.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.router_ospf6.get_schema()

        See Also:
            - post(): Create new router/ospf6 object
            - put(): Update existing router/ospf6 object
            - delete(): Remove router/ospf6 object
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
            endpoint = f"/router/ospf6/{name}"
            unwrap_single = True
        else:
            endpoint = "/router/ospf6"
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
            >>> schema = fgt.api.cmdb.router_ospf6.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.router_ospf6.get_schema(format="json-schema")
        
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
        abr_type: Literal["cisco", "ibm", "standard"] | None = None,
        auto_cost_ref_bandwidth: int | None = None,
        default_information_originate: Literal["enable", "always", "disable"] | None = None,
        log_neighbour_changes: Literal["enable", "disable"] | None = None,
        default_information_metric: int | None = None,
        default_information_metric_type: Literal["1", "2"] | None = None,
        default_information_route_map: str | None = None,
        default_metric: int | None = None,
        router_id: str | None = None,
        spf_timers: str | None = None,
        bfd: Literal["enable", "disable"] | None = None,
        restart_mode: Literal["none", "graceful-restart"] | None = None,
        restart_period: int | None = None,
        restart_on_topology_change: Literal["enable", "disable"] | None = None,
        area: str | list[str] | list[dict[str, Any]] | None = None,
        ospf6_interface: str | list[str] | list[dict[str, Any]] | None = None,
        redistribute: str | list[str] | list[dict[str, Any]] | None = None,
        passive_interface: str | list[str] | list[dict[str, Any]] | None = None,
        summary_address: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing router/ospf6 object.

        Configure IPv6 OSPF.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            abr_type: Area border router type.
            auto_cost_ref_bandwidth: Reference bandwidth in terms of megabits per second.
            default_information_originate: Enable/disable generation of default route.
            log_neighbour_changes: Log OSPFv3 neighbor changes.
            default_information_metric: Default information metric.
            default_information_metric_type: Default information metric type.
            default_information_route_map: Default information route map.
            default_metric: Default metric of redistribute routes.
            router_id: A.B.C.D, in IPv4 address format.
            spf_timers: SPF calculation frequency.
            bfd: Enable/disable Bidirectional Forwarding Detection (BFD).
            restart_mode: OSPFv3 restart mode (graceful or none).
            restart_period: Graceful restart period in seconds.
            restart_on_topology_change: Enable/disable continuing graceful restart upon topology change.
            area: OSPF6 area configuration.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            ospf6_interface: OSPF6 interface configuration.
                Default format: [{'area-id': '192.168.1.10', 'interface': 'value'}]
                Required format: List of dicts with keys: area-id, interface
                  (String format not allowed due to multiple required fields)
            redistribute: Redistribute configuration.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            passive_interface: Passive interface configuration.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            summary_address: IPv6 address summary configuration.
                Default format: [{'prefix6': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'prefix6': 'value'}] (recommended)
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_ospf6.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_ospf6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if area is not None:
            area = normalize_table_field(
                area,
                mkey="id",
                required_fields=['id'],
                field_name="area",
                example="[{'id': 1}]",
            )
        if ospf6_interface is not None:
            ospf6_interface = normalize_table_field(
                ospf6_interface,
                mkey="name",
                required_fields=['area-id', 'interface'],
                field_name="ospf6_interface",
                example="[{'area-id': '192.168.1.10', 'interface': 'value'}]",
            )
        if redistribute is not None:
            redistribute = normalize_table_field(
                redistribute,
                mkey="name",
                required_fields=['name'],
                field_name="redistribute",
                example="[{'name': 'value'}]",
            )
        if passive_interface is not None:
            passive_interface = normalize_table_field(
                passive_interface,
                mkey="name",
                required_fields=['name'],
                field_name="passive_interface",
                example="[{'name': 'value'}]",
            )
        if summary_address is not None:
            summary_address = normalize_table_field(
                summary_address,
                mkey="id",
                required_fields=['prefix6'],
                field_name="summary_address",
                example="[{'prefix6': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            abr_type=abr_type,
            auto_cost_ref_bandwidth=auto_cost_ref_bandwidth,
            default_information_originate=default_information_originate,
            log_neighbour_changes=log_neighbour_changes,
            default_information_metric=default_information_metric,
            default_information_metric_type=default_information_metric_type,
            default_information_route_map=default_information_route_map,
            default_metric=default_metric,
            router_id=router_id,
            spf_timers=spf_timers,
            bfd=bfd,
            restart_mode=restart_mode,
            restart_period=restart_period,
            restart_on_topology_change=restart_on_topology_change,
            area=area,
            ospf6_interface=ospf6_interface,
            redistribute=redistribute,
            passive_interface=passive_interface,
            summary_address=summary_address,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.ospf6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/ospf6",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/router/ospf6"

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
        Move router/ospf6 object to a new position.
        
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
            >>> fgt.api.cmdb.router_ospf6.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/router/ospf6",
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
        Clone router/ospf6 object.
        
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
            >>> fgt.api.cmdb.router_ospf6.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/router/ospf6",
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
        Check if router/ospf6 object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.router_ospf6.exists(name="myobj"):
            ...     fgt.api.cmdb.router_ospf6.post(payload_dict=data)
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

