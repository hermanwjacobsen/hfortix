"""
FortiOS CMDB - System replacemsg utm

Configuration endpoint for managing cmdb system/replacemsg/utm objects.

📖 **Read-Only Reference Table**
   This endpoint provides read-only reference data (e.g., geography, timezone).
   - GET operations return all available data
   - POST/PUT/DELETE operations are not supported
   - Querying by identifier returns all items (filter is ignored)

API Endpoints:
    GET    /cmdb/system/replacemsg/utm

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_replacemsg_utm.get()

Important:
    - This is a **read-only** endpoint (reference data only)
    - Use **GET** to retrieve available options
    - Creation/modification/deletion not supported
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

# Import cache for readonly reference data
from hfortix_core.cache import readonly_cache

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Utm(CRUDEndpoint, MetadataMixin):
    """Utm Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "utm"
    
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
        """Initialize Utm endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        msg_type: str | None = None,
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
        Retrieve system/replacemsg/utm configuration.

        Replacement messages.

        Args:
            msg_type: String identifier to retrieve specific object.
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
            >>> # Get all system/replacemsg/utm objects
            >>> result = fgt.api.cmdb.system_replacemsg_utm.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/replacemsg/utm by msg-type
            >>> result = fgt.api.cmdb.system_replacemsg_utm.get(msg_type=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_replacemsg_utm.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_replacemsg_utm.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_replacemsg_utm.get_schema()

        See Also:
            - post(): Create new system/replacemsg/utm object
            - put(): Update existing system/replacemsg/utm object
            - delete(): Remove system/replacemsg/utm object
            - exists(): Check if object exists
            - get_schema(): Get endpoint schema/metadata
        """
        # Check cache for readonly reference data (24hr TTL)
        cache_key = f"cmdb/system/replacemsg/utm"
        
        # Only use cache for full list queries (no identifier, no filters)
        is_list_query = msg_type is None and not filter and not payload_dict
        
        if is_list_query:
            cached_data = readonly_cache.get(cache_key)
            if cached_data is not None:
                # Return cached data
                return cached_data
        
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
        
        if msg_type:
            endpoint = "/system.replacemsg/utm/" + str(msg_type)
            unwrap_single = True
        else:
            endpoint = "/system.replacemsg/utm"
            unwrap_single = False
        
        
        # Fetch data and cache if this is a list query
        response = self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, unwrap_single=unwrap_single
        )
        
        # Cache the response for list queries
        if is_list_query:
            if isinstance(response, dict):
                readonly_cache.set(cache_key, response)
            # For async responses, we can't cache easily without awaiting
            # User will benefit from cache on subsequent sync calls
        
        return response

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
            >>> schema = fgt.api.cmdb.system_replacemsg_utm.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_replacemsg_utm.get_schema(format="json-schema")
        
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
        msg_type: str | None = None,
        buffer: str | None = None,
        header: Literal["none", "http", "8bit"] | None = None,
        format: Literal["none", "text", "html"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/replacemsg/utm object.

        Replacement messages.

        Args:
            payload_dict: Object data as dict. Must include msg-type (primary key).
            msg_type: Message type.
            buffer: Message string.
            header: Header flag.
            format: Format flag.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If msg-type is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_replacemsg_utm.put(
            ...     msg_type=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "msg-type": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_replacemsg_utm.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            msg_type=msg_type,
            buffer=buffer,
            header=header,
            format=format,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.utm import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/replacemsg/utm",
            )
        
        msg_type_value = payload_data.get("msg-type")
        if not msg_type_value:
            raise ValueError("msg-type is required for PUT")
        endpoint = "/system.replacemsg/utm/" + str(msg_type_value)

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
        msg_type: str | None = None,
        buffer: str | None = None,
        header: Literal["none", "http", "8bit"] | None = None,
        format: Literal["none", "text", "html"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new system/replacemsg/utm object.

        Replacement messages.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            msg_type: Message type.
            buffer: Message string.
            header: Header flag.
            format: Format flag.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_replacemsg_utm.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created msg-type: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Utm.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_replacemsg_utm.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Utm.required_fields()) }}
            
            Use Utm.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            msg_type=msg_type,
            buffer=buffer,
            header=header,
            format=format,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.utm import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/replacemsg/utm",
            )

        endpoint = "/system.replacemsg/utm"
        
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
        msg_type: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete system/replacemsg/utm object.

        Replacement messages.

        Args:
            msg_type: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If msg-type is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_replacemsg_utm.delete(msg_type=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not msg_type:
            raise ValueError("msg-type is required for DELETE")
        endpoint = "/system.replacemsg/utm/" + str(msg_type)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        msg_type: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/replacemsg/utm object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            msg_type: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_replacemsg_utm.exists(msg_type=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_replacemsg_utm.exists(msg_type=1):
            ...     fgt.api.cmdb.system_replacemsg_utm.delete(msg_type=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # For readonly endpoints, check by fetching all items and scanning
        # This is necessary because readonly endpoints don't support direct ID queries
        result = self.get(vdom=vdom)
        response = result.raw if hasattr(result, 'raw') else result
        
        if isinstance(response, dict):
            # Synchronous response
            if not is_success(response):
                return False
            
            results = response.get("results", [])
            if not isinstance(results, list):
                return False
            
            # Scan for matching identifier
            return any(
                item.get("msg-type") == msg_type
                for item in results
            )
        else:
            # Asynchronous response
            async def _check() -> bool:
                r = await response
                if not is_success(r):
                    return False
                
                results = r.get("results", [])
                if not isinstance(results, list):
                    return False
                
                return any(
                    item.get("msg-type") == msg_type
                    for item in results
                )
            return _check()


    def set(
        self,
        payload_dict: dict[str, Any] | None = None,
        msg_type: str | None = None,
        buffer: str | None = None,
        header: Literal["none", "http", "8bit"] | None = None,
        format: Literal["none", "text", "html"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/replacemsg/utm object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (msg-type) in the payload.

        Args:
            payload_dict: Resource data including msg-type (primary key)
            msg_type: Field msg-type
            buffer: Field buffer
            header: Field header
            format: Field format
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If msg-type is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.system_replacemsg_utm.set(
            ...     msg_type=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "msg-type": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_replacemsg_utm.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_replacemsg_utm.set(payload_dict=obj_data)
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
            msg_type=msg_type,
            buffer=buffer,
            header=header,
            format=format,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("msg-type")
        if not mkey_value:
            raise ValueError("msg-type is required for set()")
        
        # Check if resource exists
        if self.exists(msg_type=mkey_value, vdom=vdom):
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
        msg_type: str,
        action: Literal["before", "after"],
        reference_msg_type: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/replacemsg/utm object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            msg_type: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_msg_type: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_replacemsg_utm.move(
            ...     msg_type=100,
            ...     action="before",
            ...     reference_msg_type=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system.replacemsg/utm",
            params={
                "msg-type": msg_type,
                "action": "move",
                action: reference_msg_type,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        msg_type: str,
        new_msg_type: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/replacemsg/utm object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            msg_type: Identifier of object to clone
            new_msg_type: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_replacemsg_utm.clone(
            ...     msg_type=1,
            ...     new_msg_type=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system.replacemsg/utm",
            params={
                "msg-type": msg_type,
                "new_msg-type": new_msg_type,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


