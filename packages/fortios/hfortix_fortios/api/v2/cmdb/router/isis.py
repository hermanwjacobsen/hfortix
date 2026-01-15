"""
FortiOS CMDB - Router isis

Configuration endpoint for managing cmdb router/isis objects.

API Endpoints:
    GET    /cmdb/router/isis
    POST   /cmdb/router/isis
    PUT    /cmdb/router/isis/{identifier}
    DELETE /cmdb/router/isis/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.router_isis.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.router_isis.post(
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

class Isis(CRUDEndpoint, MetadataMixin):
    """Isis Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "isis"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "isis_net": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "isis_interface": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "summary_address": {
            "mkey": "id",
            "required_fields": ['prefix'],
            "example": "[{'prefix': 'value'}]",
        },
        "summary_address6": {
            "mkey": "id",
            "required_fields": ['prefix6'],
            "example": "[{'prefix6': 'value'}]",
        },
        "redistribute": {
            "mkey": "protocol",
            "required_fields": ['protocol'],
            "example": "[{'protocol': 'value'}]",
        },
        "redistribute6": {
            "mkey": "protocol",
            "required_fields": ['protocol'],
            "example": "[{'protocol': 'value'}]",
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
        """Initialize Isis endpoint."""
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
        Retrieve router/isis configuration.

        Configure IS-IS.

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
            >>> # Get all router/isis objects
            >>> result = fgt.api.cmdb.router_isis.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.router_isis.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.router_isis.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.router_isis.get_schema()

        See Also:
            - post(): Create new router/isis object
            - put(): Update existing router/isis object
            - delete(): Remove router/isis object
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
            endpoint = f"/router/isis/{name}"
            unwrap_single = True
        else:
            endpoint = "/router/isis"
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
            >>> schema = fgt.api.cmdb.router_isis.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.router_isis.get_schema(format="json-schema")
        
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
        is_type: Literal["level-1-2", "level-1", "level-2-only"] | None = None,
        adv_passive_only: Literal["enable", "disable"] | None = None,
        adv_passive_only6: Literal["enable", "disable"] | None = None,
        auth_mode_l1: Literal["password", "md5"] | None = None,
        auth_mode_l2: Literal["password", "md5"] | None = None,
        auth_password_l1: Any | None = None,
        auth_password_l2: Any | None = None,
        auth_keychain_l1: str | None = None,
        auth_keychain_l2: str | None = None,
        auth_sendonly_l1: Literal["enable", "disable"] | None = None,
        auth_sendonly_l2: Literal["enable", "disable"] | None = None,
        ignore_lsp_errors: Literal["enable", "disable"] | None = None,
        lsp_gen_interval_l1: int | None = None,
        lsp_gen_interval_l2: int | None = None,
        lsp_refresh_interval: int | None = None,
        max_lsp_lifetime: int | None = None,
        spf_interval_exp_l1: str | None = None,
        spf_interval_exp_l2: str | None = None,
        dynamic_hostname: Literal["enable", "disable"] | None = None,
        adjacency_check: Literal["enable", "disable"] | None = None,
        adjacency_check6: Literal["enable", "disable"] | None = None,
        overload_bit: Literal["enable", "disable"] | None = None,
        overload_bit_suppress: Literal["external", "interlevel"] | list[str] | None = None,
        overload_bit_on_startup: int | None = None,
        default_originate: Literal["enable", "disable"] | None = None,
        default_originate6: Literal["enable", "disable"] | None = None,
        metric_style: Literal["narrow", "wide", "transition", "narrow-transition", "narrow-transition-l1", "narrow-transition-l2", "wide-l1", "wide-l2", "wide-transition", "wide-transition-l1", "wide-transition-l2", "transition-l1", "transition-l2"] | None = None,
        redistribute_l1: Literal["enable", "disable"] | None = None,
        redistribute_l1_list: str | None = None,
        redistribute_l2: Literal["enable", "disable"] | None = None,
        redistribute_l2_list: str | None = None,
        redistribute6_l1: Literal["enable", "disable"] | None = None,
        redistribute6_l1_list: str | None = None,
        redistribute6_l2: Literal["enable", "disable"] | None = None,
        redistribute6_l2_list: str | None = None,
        isis_net: str | list[str] | list[dict[str, Any]] | None = None,
        isis_interface: str | list[str] | list[dict[str, Any]] | None = None,
        summary_address: str | list[str] | list[dict[str, Any]] | None = None,
        summary_address6: str | list[str] | list[dict[str, Any]] | None = None,
        redistribute: str | list[str] | list[dict[str, Any]] | None = None,
        redistribute6: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing router/isis object.

        Configure IS-IS.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            is_type: IS type.
            adv_passive_only: Enable/disable IS-IS advertisement of passive interfaces only.
            adv_passive_only6: Enable/disable IPv6 IS-IS advertisement of passive interfaces only.
            auth_mode_l1: Level 1 authentication mode.
            auth_mode_l2: Level 2 authentication mode.
            auth_password_l1: Authentication password for level 1 PDUs.
            auth_password_l2: Authentication password for level 2 PDUs.
            auth_keychain_l1: Authentication key-chain for level 1 PDUs.
            auth_keychain_l2: Authentication key-chain for level 2 PDUs.
            auth_sendonly_l1: Enable/disable level 1 authentication send-only.
            auth_sendonly_l2: Enable/disable level 2 authentication send-only.
            ignore_lsp_errors: Enable/disable ignoring of LSP errors with bad checksums.
            lsp_gen_interval_l1: Minimum interval for level 1 LSP regenerating.
            lsp_gen_interval_l2: Minimum interval for level 2 LSP regenerating.
            lsp_refresh_interval: LSP refresh time in seconds.
            max_lsp_lifetime: Maximum LSP lifetime in seconds.
            spf_interval_exp_l1: Level 1 SPF calculation delay.
            spf_interval_exp_l2: Level 2 SPF calculation delay.
            dynamic_hostname: Enable/disable dynamic hostname.
            adjacency_check: Enable/disable adjacency check.
            adjacency_check6: Enable/disable IPv6 adjacency check.
            overload_bit: Enable/disable signal other routers not to use us in SPF.
            overload_bit_suppress: Suppress overload-bit for the specific prefixes.
            overload_bit_on_startup: Overload-bit only temporarily after reboot.
            default_originate: Enable/disable distribution of default route information.
            default_originate6: Enable/disable distribution of default IPv6 route information.
            metric_style: Use old-style (ISO 10589) or new-style packet formats.
            redistribute_l1: Enable/disable redistribution of level 1 routes into level 2.
            redistribute_l1_list: Access-list for route redistribution from l1 to l2.
            redistribute_l2: Enable/disable redistribution of level 2 routes into level 1.
            redistribute_l2_list: Access-list for route redistribution from l2 to l1.
            redistribute6_l1: Enable/disable redistribution of level 1 IPv6 routes into level 2.
            redistribute6_l1_list: Access-list for IPv6 route redistribution from l1 to l2.
            redistribute6_l2: Enable/disable redistribution of level 2 IPv6 routes into level 1.
            redistribute6_l2_list: Access-list for IPv6 route redistribution from l2 to l1.
            isis_net: IS-IS net configuration.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            isis_interface: IS-IS interface configuration.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            summary_address: IS-IS summary addresses.
                Default format: [{'prefix': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'prefix': 'value'}] (recommended)
            summary_address6: IS-IS IPv6 summary address.
                Default format: [{'prefix6': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'prefix6': 'value'}] (recommended)
            redistribute: IS-IS redistribute protocols.
                Default format: [{'protocol': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'protocol': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'protocol': 'val1'}, ...]
                  - List of dicts: [{'protocol': 'value'}] (recommended)
            redistribute6: IS-IS IPv6 redistribution for routing protocols.
                Default format: [{'protocol': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'protocol': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'protocol': 'val1'}, ...]
                  - List of dicts: [{'protocol': 'value'}] (recommended)
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.router_isis.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.router_isis.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if isis_net is not None:
            isis_net = normalize_table_field(
                isis_net,
                mkey="id",
                required_fields=['id'],
                field_name="isis_net",
                example="[{'id': 1}]",
            )
        if isis_interface is not None:
            isis_interface = normalize_table_field(
                isis_interface,
                mkey="name",
                required_fields=['name'],
                field_name="isis_interface",
                example="[{'name': 'value'}]",
            )
        if summary_address is not None:
            summary_address = normalize_table_field(
                summary_address,
                mkey="id",
                required_fields=['prefix'],
                field_name="summary_address",
                example="[{'prefix': 'value'}]",
            )
        if summary_address6 is not None:
            summary_address6 = normalize_table_field(
                summary_address6,
                mkey="id",
                required_fields=['prefix6'],
                field_name="summary_address6",
                example="[{'prefix6': 'value'}]",
            )
        if redistribute is not None:
            redistribute = normalize_table_field(
                redistribute,
                mkey="protocol",
                required_fields=['protocol'],
                field_name="redistribute",
                example="[{'protocol': 'value'}]",
            )
        if redistribute6 is not None:
            redistribute6 = normalize_table_field(
                redistribute6,
                mkey="protocol",
                required_fields=['protocol'],
                field_name="redistribute6",
                example="[{'protocol': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            is_type=is_type,
            adv_passive_only=adv_passive_only,
            adv_passive_only6=adv_passive_only6,
            auth_mode_l1=auth_mode_l1,
            auth_mode_l2=auth_mode_l2,
            auth_password_l1=auth_password_l1,
            auth_password_l2=auth_password_l2,
            auth_keychain_l1=auth_keychain_l1,
            auth_keychain_l2=auth_keychain_l2,
            auth_sendonly_l1=auth_sendonly_l1,
            auth_sendonly_l2=auth_sendonly_l2,
            ignore_lsp_errors=ignore_lsp_errors,
            lsp_gen_interval_l1=lsp_gen_interval_l1,
            lsp_gen_interval_l2=lsp_gen_interval_l2,
            lsp_refresh_interval=lsp_refresh_interval,
            max_lsp_lifetime=max_lsp_lifetime,
            spf_interval_exp_l1=spf_interval_exp_l1,
            spf_interval_exp_l2=spf_interval_exp_l2,
            dynamic_hostname=dynamic_hostname,
            adjacency_check=adjacency_check,
            adjacency_check6=adjacency_check6,
            overload_bit=overload_bit,
            overload_bit_suppress=overload_bit_suppress,
            overload_bit_on_startup=overload_bit_on_startup,
            default_originate=default_originate,
            default_originate6=default_originate6,
            metric_style=metric_style,
            redistribute_l1=redistribute_l1,
            redistribute_l1_list=redistribute_l1_list,
            redistribute_l2=redistribute_l2,
            redistribute_l2_list=redistribute_l2_list,
            redistribute6_l1=redistribute6_l1,
            redistribute6_l1_list=redistribute6_l1_list,
            redistribute6_l2=redistribute6_l2,
            redistribute6_l2_list=redistribute6_l2_list,
            isis_net=isis_net,
            isis_interface=isis_interface,
            summary_address=summary_address,
            summary_address6=summary_address6,
            redistribute=redistribute,
            redistribute6=redistribute6,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.isis import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/router/isis",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/router/isis"

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
        Move router/isis object to a new position.
        
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
            >>> fgt.api.cmdb.router_isis.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/router/isis",
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
        Clone router/isis object.
        
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
            >>> fgt.api.cmdb.router_isis.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/router/isis",
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
        Check if router/isis object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.router_isis.exists(name="myobj"):
            ...     fgt.api.cmdb.router_isis.post(payload_dict=data)
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/router/isis"
        endpoint = f"{endpoint}/{quote_path_param(name)}"
        
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

