"""
FortiOS CMDB - Router static

Configuration endpoint for managing cmdb router/static objects.

API Endpoints:
    GET    /cmdb/router/static
    POST   /cmdb/router/static
    PUT    /cmdb/router/static/{identifier}
    DELETE /cmdb/router/static/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_static.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.router_static.post(
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

class Static(CRUDEndpoint, MetadataMixin):
    """Static Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "static"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "sdwan_zone": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
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
        """Initialize Static endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        seq_num: int | None = None,
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
        Retrieve router/static configuration.

        Configure IPv4 static routing tables.

        Args:
            seq_num: Integer identifier to retrieve specific object.
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
            >>> # Get all router/static objects
            >>> result = fgt.api.cmdb.router_static.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific router/static by seq-num
            >>> result = fgt.api.cmdb.router_static.get(seq_num=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_static.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.router_static.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.router_static.get_schema()

        See Also:
            - post(): Create new router/static object
            - put(): Update existing router/static object
            - delete(): Remove router/static object
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
        
        if seq_num:
            endpoint = "/router/static/" + str(seq_num)
            unwrap_single = True
        else:
            endpoint = "/router/static"
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
            >>> schema = fgt.api.cmdb.router_static.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.router_static.get_schema(format="json-schema")
        
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
        seq_num: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        dst: str | None = None,
        src: str | None = None,
        gateway: str | None = None,
        preferred_source: str | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        device: str | None = None,
        comment: str | None = None,
        blackhole: Literal["enable", "disable"] | None = None,
        dynamic_gateway: Literal["enable", "disable"] | None = None,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | None = None,
        internet_service: int | None = None,
        internet_service_custom: str | None = None,
        internet_service_fortiguard: str | None = None,
        link_monitor_exempt: Literal["enable", "disable"] | None = None,
        tag: int | None = None,
        vrf: int | None = None,
        bfd: Literal["enable", "disable"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing router/static object.

        Configure IPv4 static routing tables.

        Args:
            payload_dict: Object data as dict. Must include seq-num (primary key).
            seq_num: Sequence number.
            status: Enable/disable this static route.
            dst: Destination IP and mask for this route.
            src: Source prefix for this route.
            gateway: Gateway IP for this route.
            preferred_source: Preferred source IP for this route.
            distance: Administrative distance (1 - 255).
            weight: Administrative weight (0 - 255).
            priority: Administrative priority (1 - 65535).
            device: Gateway out interface or tunnel.
            comment: Optional comments.
            blackhole: Enable/disable black hole.
            dynamic_gateway: Enable use of dynamic gateway retrieved from a DHCP or PPP server.
            sdwan_zone: Choose SD-WAN Zone.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr: Name of firewall address or address group.
            internet_service: Application ID in the Internet service database.
            internet_service_custom: Application name in the Internet service custom database.
            internet_service_fortiguard: Application name in the Internet service fortiguard database.
            link_monitor_exempt: Enable/disable withdrawal of this static route when link monitor or health check is down.
            tag: Route tag.
            vrf: Virtual Routing Forwarding ID.
            bfd: Enable/disable Bidirectional Forwarding Detection (BFD).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If seq-num is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_static.put(
            ...     seq_num=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "seq-num": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_static.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if sdwan_zone is not None:
            sdwan_zone = normalize_table_field(
                sdwan_zone,
                mkey="name",
                required_fields=['name'],
                field_name="sdwan_zone",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            seq_num=seq_num,
            status=status,
            dst=dst,
            src=src,
            gateway=gateway,
            preferred_source=preferred_source,
            distance=distance,
            weight=weight,
            priority=priority,
            device=device,
            comment=comment,
            blackhole=blackhole,
            dynamic_gateway=dynamic_gateway,
            sdwan_zone=sdwan_zone,
            dstaddr=dstaddr,
            internet_service=internet_service,
            internet_service_custom=internet_service_custom,
            internet_service_fortiguard=internet_service_fortiguard,
            link_monitor_exempt=link_monitor_exempt,
            tag=tag,
            vrf=vrf,
            bfd=bfd,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.static import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/static",
            )
        
        seq_num_value = payload_data.get("seq-num")
        if not seq_num_value:
            raise ValueError("seq-num is required for PUT")
        endpoint = "/router/static/" + str(seq_num_value)

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
        seq_num: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        dst: str | None = None,
        src: str | None = None,
        gateway: str | None = None,
        preferred_source: str | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        device: str | None = None,
        comment: str | None = None,
        blackhole: Literal["enable", "disable"] | None = None,
        dynamic_gateway: Literal["enable", "disable"] | None = None,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | None = None,
        internet_service: int | None = None,
        internet_service_custom: str | None = None,
        internet_service_fortiguard: str | None = None,
        link_monitor_exempt: Literal["enable", "disable"] | None = None,
        tag: int | None = None,
        vrf: int | None = None,
        bfd: Literal["enable", "disable"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new router/static object.

        Configure IPv4 static routing tables.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            seq_num: Sequence number.
            status: Enable/disable this static route.
            dst: Destination IP and mask for this route.
            src: Source prefix for this route.
            gateway: Gateway IP for this route.
            preferred_source: Preferred source IP for this route.
            distance: Administrative distance (1 - 255).
            weight: Administrative weight (0 - 255).
            priority: Administrative priority (1 - 65535).
            device: Gateway out interface or tunnel.
            comment: Optional comments.
            blackhole: Enable/disable black hole.
            dynamic_gateway: Enable use of dynamic gateway retrieved from a DHCP or PPP server.
            sdwan_zone: Choose SD-WAN Zone.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr: Name of firewall address or address group.
            internet_service: Application ID in the Internet service database.
            internet_service_custom: Application name in the Internet service custom database.
            internet_service_fortiguard: Application name in the Internet service fortiguard database.
            link_monitor_exempt: Enable/disable withdrawal of this static route when link monitor or health check is down.
            tag: Route tag.
            vrf: Virtual Routing Forwarding ID.
            bfd: Enable/disable Bidirectional Forwarding Detection (BFD).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.router_static.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created seq-num: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Static.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.router_static.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Static.required_fields()) }}
            
            Use Static.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if sdwan_zone is not None:
            sdwan_zone = normalize_table_field(
                sdwan_zone,
                mkey="name",
                required_fields=['name'],
                field_name="sdwan_zone",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            seq_num=seq_num,
            status=status,
            dst=dst,
            src=src,
            gateway=gateway,
            preferred_source=preferred_source,
            distance=distance,
            weight=weight,
            priority=priority,
            device=device,
            comment=comment,
            blackhole=blackhole,
            dynamic_gateway=dynamic_gateway,
            sdwan_zone=sdwan_zone,
            dstaddr=dstaddr,
            internet_service=internet_service,
            internet_service_custom=internet_service_custom,
            internet_service_fortiguard=internet_service_fortiguard,
            link_monitor_exempt=link_monitor_exempt,
            tag=tag,
            vrf=vrf,
            bfd=bfd,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.static import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/static",
            )

        endpoint = "/router/static"
        
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
        seq_num: int | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete router/static object.

        Configure IPv4 static routing tables.

        Args:
            seq_num: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If seq-num is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.router_static.delete(seq_num=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not seq_num:
            raise ValueError("seq-num is required for DELETE")
        endpoint = "/router/static/" + str(seq_num)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        seq_num: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if router/static object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            seq_num: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.router_static.exists(seq_num=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.router_static.exists(seq_num=1):
            ...     fgt.api.cmdb.router_static.delete(seq_num=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/router/static"
        endpoint = f"{endpoint}/{seq_num}"
        
        # Make request with silent=True to suppress 404 error logging
        # (404 is expected when checking existence - it just means "doesn't exist")
        # Use _wrapped_client to access the underlying HTTPClient directly
        # (self._client is ResponseProcessingClient, _wrapped_client is HTTPClient)
        try:
            result = self._client._wrapped_client.get(
                "cmdb",
                endpoint,
                params=None,
                vdom=vdom,
                raw_json=True,
                silent=True,
            )
            
            if isinstance(result, dict):
                # Synchronous response - check status
                return result.get("status") == "success"
            else:
                # Asynchronous response
                async def _check() -> bool:
                    r = await result
                    return r.get("status") == "success"
                return _check()
        except Exception:
            # Any error (404, network, etc.) means we can't confirm existence
            return False


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        seq_num: int | None = None,
        status: Literal["enable", "disable"] | None = None,
        dst: str | None = None,
        src: str | None = None,
        gateway: str | None = None,
        preferred_source: str | None = None,
        distance: int | None = None,
        weight: int | None = None,
        priority: int | None = None,
        device: str | None = None,
        comment: str | None = None,
        blackhole: Literal["enable", "disable"] | None = None,
        dynamic_gateway: Literal["enable", "disable"] | None = None,
        sdwan_zone: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr: str | None = None,
        internet_service: int | None = None,
        internet_service_custom: str | None = None,
        internet_service_fortiguard: str | None = None,
        link_monitor_exempt: Literal["enable", "disable"] | None = None,
        tag: int | None = None,
        vrf: int | None = None,
        bfd: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update router/static object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (seq-num) in the payload.

        Args:
            payload_dict: Resource data including seq-num (primary key)
            seq_num: Field seq-num
            status: Field status
            dst: Field dst
            src: Field src
            gateway: Field gateway
            preferred_source: Field preferred-source
            distance: Field distance
            weight: Field weight
            priority: Field priority
            device: Field device
            comment: Field comment
            blackhole: Field blackhole
            dynamic_gateway: Field dynamic-gateway
            sdwan_zone: Field sdwan-zone
            dstaddr: Field dstaddr
            internet_service: Field internet-service
            internet_service_custom: Field internet-service-custom
            internet_service_fortiguard: Field internet-service-fortiguard
            link_monitor_exempt: Field link-monitor-exempt
            tag: Field tag
            vrf: Field vrf
            bfd: Field bfd
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If seq-num is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.router_static.set(
            ...     seq_num=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "seq-num": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.router_static.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.router_static.set(payload_dict=obj_data)
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
            seq_num=seq_num,
            status=status,
            dst=dst,
            src=src,
            gateway=gateway,
            preferred_source=preferred_source,
            distance=distance,
            weight=weight,
            priority=priority,
            device=device,
            comment=comment,
            blackhole=blackhole,
            dynamic_gateway=dynamic_gateway,
            sdwan_zone=sdwan_zone,
            dstaddr=dstaddr,
            internet_service=internet_service,
            internet_service_custom=internet_service_custom,
            internet_service_fortiguard=internet_service_fortiguard,
            link_monitor_exempt=link_monitor_exempt,
            tag=tag,
            vrf=vrf,
            bfd=bfd,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("seq-num")
        if not mkey_value:
            raise ValueError("seq-num is required for set()")
        
        # Check if resource exists
        if self.exists(seq_num=mkey_value, vdom=vdom):
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
        seq_num: int,
        action: Literal["before", "after"],
        reference_seq_num: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move router/static object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            seq_num: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_seq_num: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.router_static.move(
            ...     seq_num=100,
            ...     action="before",
            ...     reference_seq_num=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/router/static",
            params={
                "seq-num": seq_num,
                "action": "move",
                action: reference_seq_num,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        seq_num: int,
        new_seq_num: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone router/static object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            seq_num: Identifier of object to clone
            new_seq_num: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.router_static.clone(
            ...     seq_num=1,
            ...     new_seq_num=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/router/static",
            params={
                "seq-num": seq_num,
                "new_seq-num": new_seq_num,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


