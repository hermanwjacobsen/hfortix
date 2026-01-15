"""
FortiOS CMDB - System wccp

Configuration endpoint for managing cmdb system/wccp objects.

API Endpoints:
    GET    /cmdb/system/wccp
    POST   /cmdb/system/wccp
    PUT    /cmdb/system/wccp/{identifier}
    DELETE /cmdb/system/wccp/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_wccp.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_wccp.post(
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
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Wccp(CRUDEndpoint, MetadataMixin):
    """Wccp Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "wccp"
    
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
        """Initialize Wccp endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        service_id: str | None = None,
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
        Retrieve system/wccp configuration.

        Configure WCCP.

        Args:
            service_id: String identifier to retrieve specific object.
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
            >>> # Get all system/wccp objects
            >>> result = fgt.api.cmdb.system_wccp.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/wccp by service-id
            >>> result = fgt.api.cmdb.system_wccp.get(service_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_wccp.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_wccp.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_wccp.get_schema()

        See Also:
            - post(): Create new system/wccp object
            - put(): Update existing system/wccp object
            - delete(): Remove system/wccp object
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
        
        if service_id:
            endpoint = "/system/wccp/" + str(service_id)
            unwrap_single = True
        else:
            endpoint = "/system/wccp"
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
            >>> schema = fgt.api.cmdb.system_wccp.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_wccp.get_schema(format="json-schema")
        
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
        service_id: str | None = None,
        router_id: str | None = None,
        cache_id: str | None = None,
        group_address: Any | None = None,
        server_list: str | list[str] | None = None,
        router_list: str | list[str] | None = None,
        ports_defined: Literal["source", "destination"] | None = None,
        server_type: Literal["forward", "proxy"] | None = None,
        ports: str | list[str] | None = None,
        authentication: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        forward_method: Literal["GRE", "L2", "any"] | None = None,
        cache_engine_method: Literal["GRE", "L2"] | None = None,
        service_type: Literal["auto", "standard", "dynamic"] | None = None,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = None,
        priority: int | None = None,
        protocol: int | None = None,
        assignment_weight: int | None = None,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = None,
        return_method: Literal["GRE", "L2", "any"] | None = None,
        assignment_method: Literal["HASH", "MASK", "any"] | None = None,
        assignment_srcaddr_mask: Any | None = None,
        assignment_dstaddr_mask: Any | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/wccp object.

        Configure WCCP.

        Args:
            payload_dict: Object data as dict. Must include service-id (primary key).
            service_id: Service ID.
            router_id: IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.
            cache_id: IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.
            group_address: IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.
            server_list: IP addresses and netmasks for up to four cache servers.
            router_list: IP addresses of one or more WCCP routers.
            ports_defined: Match method.
            server_type: Cache server type.
            ports: Service ports.
            authentication: Enable/disable MD5 authentication.
            password: Password for MD5 authentication.
            forward_method: Method used to forward traffic to the cache servers.
            cache_engine_method: Method used to forward traffic to the routers or to return to the cache engine.
            service_type: WCCP service type used by the cache server for logical interception and redirection of traffic.
            primary_hash: Hash method.
            priority: Service priority.
            protocol: Service protocol.
            assignment_weight: Assignment of hash weight/ratio for the WCCP cache engine.
            assignment_bucket_format: Assignment bucket format for the WCCP cache engine.
            return_method: Method used to decline a redirected packet and return it to the FortiGate unit.
            assignment_method: Hash key assignment preference.
            assignment_srcaddr_mask: Assignment source address mask.
            assignment_dstaddr_mask: Assignment destination address mask.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If service-id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_wccp.put(
            ...     service_id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "service-id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_wccp.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            service_id=service_id,
            router_id=router_id,
            cache_id=cache_id,
            group_address=group_address,
            server_list=server_list,
            router_list=router_list,
            ports_defined=ports_defined,
            server_type=server_type,
            ports=ports,
            authentication=authentication,
            password=password,
            forward_method=forward_method,
            cache_engine_method=cache_engine_method,
            service_type=service_type,
            primary_hash=primary_hash,
            priority=priority,
            protocol=protocol,
            assignment_weight=assignment_weight,
            assignment_bucket_format=assignment_bucket_format,
            return_method=return_method,
            assignment_method=assignment_method,
            assignment_srcaddr_mask=assignment_srcaddr_mask,
            assignment_dstaddr_mask=assignment_dstaddr_mask,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.wccp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/wccp",
            )
        
        service_id_value = payload_data.get("service-id")
        if not service_id_value:
            raise ValueError("service-id is required for PUT")
        endpoint = "/system/wccp/" + str(service_id_value)

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
        service_id: str | None = None,
        router_id: str | None = None,
        cache_id: str | None = None,
        group_address: Any | None = None,
        server_list: str | list[str] | None = None,
        router_list: str | list[str] | None = None,
        ports_defined: Literal["source", "destination"] | None = None,
        server_type: Literal["forward", "proxy"] | None = None,
        ports: str | list[str] | None = None,
        authentication: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        forward_method: Literal["GRE", "L2", "any"] | None = None,
        cache_engine_method: Literal["GRE", "L2"] | None = None,
        service_type: Literal["auto", "standard", "dynamic"] | None = None,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | None = None,
        priority: int | None = None,
        protocol: int | None = None,
        assignment_weight: int | None = None,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = None,
        return_method: Literal["GRE", "L2", "any"] | None = None,
        assignment_method: Literal["HASH", "MASK", "any"] | None = None,
        assignment_srcaddr_mask: Any | None = None,
        assignment_dstaddr_mask: Any | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new system/wccp object.

        Configure WCCP.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            service_id: Service ID.
            router_id: IP address known to all cache engines. If all cache engines connect to the same FortiGate interface, use the default 0.0.0.0.
            cache_id: IP address known to all routers. If the addresses are the same, use the default 0.0.0.0.
            group_address: IP multicast address used by the cache routers. For the FortiGate to ignore multicast WCCP traffic, use the default 0.0.0.0.
            server_list: IP addresses and netmasks for up to four cache servers.
            router_list: IP addresses of one or more WCCP routers.
            ports_defined: Match method.
            server_type: Cache server type.
            ports: Service ports.
            authentication: Enable/disable MD5 authentication.
            password: Password for MD5 authentication.
            forward_method: Method used to forward traffic to the cache servers.
            cache_engine_method: Method used to forward traffic to the routers or to return to the cache engine.
            service_type: WCCP service type used by the cache server for logical interception and redirection of traffic.
            primary_hash: Hash method.
            priority: Service priority.
            protocol: Service protocol.
            assignment_weight: Assignment of hash weight/ratio for the WCCP cache engine.
            assignment_bucket_format: Assignment bucket format for the WCCP cache engine.
            return_method: Method used to decline a redirected packet and return it to the FortiGate unit.
            assignment_method: Hash key assignment preference.
            assignment_srcaddr_mask: Assignment source address mask.
            assignment_dstaddr_mask: Assignment destination address mask.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_wccp.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created service-id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Wccp.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_wccp.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Wccp.required_fields()) }}
            
            Use Wccp.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            service_id=service_id,
            router_id=router_id,
            cache_id=cache_id,
            group_address=group_address,
            server_list=server_list,
            router_list=router_list,
            ports_defined=ports_defined,
            server_type=server_type,
            ports=ports,
            authentication=authentication,
            password=password,
            forward_method=forward_method,
            cache_engine_method=cache_engine_method,
            service_type=service_type,
            primary_hash=primary_hash,
            priority=priority,
            protocol=protocol,
            assignment_weight=assignment_weight,
            assignment_bucket_format=assignment_bucket_format,
            return_method=return_method,
            assignment_method=assignment_method,
            assignment_srcaddr_mask=assignment_srcaddr_mask,
            assignment_dstaddr_mask=assignment_dstaddr_mask,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.wccp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/wccp",
            )

        endpoint = "/system/wccp"
        
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
        service_id: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete system/wccp object.

        Configure WCCP.

        Args:
            service_id: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If service-id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_wccp.delete(service_id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not service_id:
            raise ValueError("service-id is required for DELETE")
        endpoint = "/system/wccp/" + str(service_id)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        service_id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/wccp object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            service_id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_wccp.exists(service_id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_wccp.exists(service_id=1):
            ...     fgt.api.cmdb.system_wccp.delete(service_id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                service_id=service_id,
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
        service_id: str | None = None,
        router_id: str | None = None,
        cache_id: str | None = None,
        group_address: Any | None = None,
        server_list: str | list[str] | list[dict[str, Any]] | None = None,
        router_list: str | list[str] | list[dict[str, Any]] | None = None,
        ports_defined: Literal["source", "destination"] | None = None,
        server_type: Literal["forward", "proxy"] | None = None,
        ports: str | list[str] | list[dict[str, Any]] | None = None,
        authentication: Literal["enable", "disable"] | None = None,
        password: Any | None = None,
        forward_method: Literal["GRE", "L2", "any"] | None = None,
        cache_engine_method: Literal["GRE", "L2"] | None = None,
        service_type: Literal["auto", "standard", "dynamic"] | None = None,
        primary_hash: Literal["src-ip", "dst-ip", "src-port", "dst-port"] | list[str] | list[dict[str, Any]] | None = None,
        priority: int | None = None,
        protocol: int | None = None,
        assignment_weight: int | None = None,
        assignment_bucket_format: Literal["wccp-v2", "cisco-implementation"] | None = None,
        return_method: Literal["GRE", "L2", "any"] | None = None,
        assignment_method: Literal["HASH", "MASK", "any"] | None = None,
        assignment_srcaddr_mask: Any | None = None,
        assignment_dstaddr_mask: Any | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/wccp object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (service-id) in the payload.

        Args:
            payload_dict: Resource data including service-id (primary key)
            service_id: Field service-id
            router_id: Field router-id
            cache_id: Field cache-id
            group_address: Field group-address
            server_list: Field server-list
            router_list: Field router-list
            ports_defined: Field ports-defined
            server_type: Field server-type
            ports: Field ports
            authentication: Field authentication
            password: Field password
            forward_method: Field forward-method
            cache_engine_method: Field cache-engine-method
            service_type: Field service-type
            primary_hash: Field primary-hash
            priority: Field priority
            protocol: Field protocol
            assignment_weight: Field assignment-weight
            assignment_bucket_format: Field assignment-bucket-format
            return_method: Field return-method
            assignment_method: Field assignment-method
            assignment_srcaddr_mask: Field assignment-srcaddr-mask
            assignment_dstaddr_mask: Field assignment-dstaddr-mask
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If service-id is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.system_wccp.set(
            ...     service_id=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "service-id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_wccp.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_wccp.set(payload_dict=obj_data)
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
            service_id=service_id,
            router_id=router_id,
            cache_id=cache_id,
            group_address=group_address,
            server_list=server_list,
            router_list=router_list,
            ports_defined=ports_defined,
            server_type=server_type,
            ports=ports,
            authentication=authentication,
            password=password,
            forward_method=forward_method,
            cache_engine_method=cache_engine_method,
            service_type=service_type,
            primary_hash=primary_hash,
            priority=priority,
            protocol=protocol,
            assignment_weight=assignment_weight,
            assignment_bucket_format=assignment_bucket_format,
            return_method=return_method,
            assignment_method=assignment_method,
            assignment_srcaddr_mask=assignment_srcaddr_mask,
            assignment_dstaddr_mask=assignment_dstaddr_mask,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("service-id")
        if not mkey_value:
            raise ValueError("service-id is required for set()")
        
        # Check if resource exists
        if self.exists(service_id=mkey_value, vdom=vdom):
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
        service_id: str,
        action: Literal["before", "after"],
        reference_service_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/wccp object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            service_id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_service_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_wccp.move(
            ...     service_id=100,
            ...     action="before",
            ...     reference_service_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system/wccp",
            params={
                "service-id": service_id,
                "action": "move",
                action: reference_service_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        service_id: str,
        new_service_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/wccp object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            service_id: Identifier of object to clone
            new_service_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_wccp.clone(
            ...     service_id=1,
            ...     new_service_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system/wccp",
            params={
                "service-id": service_id,
                "new_service-id": new_service_id,
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
        service_id: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/wccp object exists.
        
        Args:
            service_id: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_wccp.exists(service_id=1):
            ...     fgt.api.cmdb.system_wccp.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                service_id=service_id,
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

