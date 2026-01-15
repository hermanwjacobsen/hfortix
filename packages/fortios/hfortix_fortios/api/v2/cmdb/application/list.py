"""
FortiOS CMDB - Application list

Configuration endpoint for managing cmdb application/list objects.

API Endpoints:
    GET    /cmdb/application/list
    POST   /cmdb/application/list
    PUT    /cmdb/application/list/{identifier}
    DELETE /cmdb/application/list/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.application_list.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.application_list.post(
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

class List(CRUDEndpoint, MetadataMixin):
    """List Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "list"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "entries": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "default_network_services": {
            "mkey": "id",
            "required_fields": ['id', 'port'],
            "example": "[{'id': 1, 'port': 1}]",
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
        """Initialize List endpoint."""
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
        Retrieve application/list configuration.

        Configure application control lists.

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
            >>> # Get all application/list objects
            >>> result = fgt.api.cmdb.application_list.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific application/list by name
            >>> result = fgt.api.cmdb.application_list.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.application_list.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.application_list.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.application_list.get_schema()

        See Also:
            - post(): Create new application/list object
            - put(): Update existing application/list object
            - delete(): Remove application/list object
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
            endpoint = "/application/list/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/application/list"
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
            >>> schema = fgt.api.cmdb.application_list.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.application_list.get_schema(format="json-schema")
        
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
        comment: str | None = None,
        replacemsg_group: str | None = None,
        extended_log: Literal["enable", "disable"] | None = None,
        other_application_action: Literal["pass", "block"] | None = None,
        app_replacemsg: Literal["disable", "enable"] | None = None,
        other_application_log: Literal["disable", "enable"] | None = None,
        enforce_default_app_port: Literal["disable", "enable"] | None = None,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = None,
        unknown_application_action: Literal["pass", "block"] | None = None,
        unknown_application_log: Literal["disable", "enable"] | None = None,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = None,
        deep_app_inspection: Literal["disable", "enable"] | None = None,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = None,
        entries: str | list[str] | list[dict[str, Any]] | None = None,
        control_default_network_services: Literal["disable", "enable"] | None = None,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing application/list object.

        Configure application control lists.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: List name.
            comment: Comments.
            replacemsg_group: Replacement message group.
            extended_log: Enable/disable extended logging.
            other_application_action: Action for other applications.
            app_replacemsg: Enable/disable replacement messages for blocked applications.
            other_application_log: Enable/disable logging for other applications.
            enforce_default_app_port: Enable/disable default application port enforcement for allowed applications.
            force_inclusion_ssl_di_sigs: Enable/disable forced inclusion of SSL deep inspection signatures.
            unknown_application_action: Pass or block traffic from unknown applications.
            unknown_application_log: Enable/disable logging for unknown applications.
            p2p_block_list: P2P applications to be block listed.
            deep_app_inspection: Enable/disable deep application inspection.
            options: Basic application protocol signatures allowed by default.
            entries: Application list entries.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            control_default_network_services: Enable/disable enforcement of protocols over selected ports.
            default_network_services: Default network service entries.
                Default format: [{'id': 1, 'port': 1}]
                Required format: List of dicts with keys: id, port
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
            >>> result = fgt.api.cmdb.application_list.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.application_list.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if entries is not None:
            entries = normalize_table_field(
                entries,
                mkey="id",
                required_fields=['id'],
                field_name="entries",
                example="[{'id': 1}]",
            )
        if default_network_services is not None:
            default_network_services = normalize_table_field(
                default_network_services,
                mkey="id",
                required_fields=['id', 'port'],
                field_name="default_network_services",
                example="[{'id': 1, 'port': 1}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            comment=comment,
            replacemsg_group=replacemsg_group,
            extended_log=extended_log,
            other_application_action=other_application_action,
            app_replacemsg=app_replacemsg,
            other_application_log=other_application_log,
            enforce_default_app_port=enforce_default_app_port,
            force_inclusion_ssl_di_sigs=force_inclusion_ssl_di_sigs,
            unknown_application_action=unknown_application_action,
            unknown_application_log=unknown_application_log,
            p2p_block_list=p2p_block_list,
            deep_app_inspection=deep_app_inspection,
            options=options,
            entries=entries,
            control_default_network_services=control_default_network_services,
            default_network_services=default_network_services,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.list import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/application/list",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/application/list/" + str(name_value)

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
        comment: str | None = None,
        replacemsg_group: str | None = None,
        extended_log: Literal["enable", "disable"] | None = None,
        other_application_action: Literal["pass", "block"] | None = None,
        app_replacemsg: Literal["disable", "enable"] | None = None,
        other_application_log: Literal["disable", "enable"] | None = None,
        enforce_default_app_port: Literal["disable", "enable"] | None = None,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = None,
        unknown_application_action: Literal["pass", "block"] | None = None,
        unknown_application_log: Literal["disable", "enable"] | None = None,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | None = None,
        deep_app_inspection: Literal["disable", "enable"] | None = None,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | None = None,
        entries: str | list[str] | list[dict[str, Any]] | None = None,
        control_default_network_services: Literal["disable", "enable"] | None = None,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new application/list object.

        Configure application control lists.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: List name.
            comment: Comments.
            replacemsg_group: Replacement message group.
            extended_log: Enable/disable extended logging.
            other_application_action: Action for other applications.
            app_replacemsg: Enable/disable replacement messages for blocked applications.
            other_application_log: Enable/disable logging for other applications.
            enforce_default_app_port: Enable/disable default application port enforcement for allowed applications.
            force_inclusion_ssl_di_sigs: Enable/disable forced inclusion of SSL deep inspection signatures.
            unknown_application_action: Pass or block traffic from unknown applications.
            unknown_application_log: Enable/disable logging for unknown applications.
            p2p_block_list: P2P applications to be block listed.
            deep_app_inspection: Enable/disable deep application inspection.
            options: Basic application protocol signatures allowed by default.
            entries: Application list entries.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            control_default_network_services: Enable/disable enforcement of protocols over selected ports.
            default_network_services: Default network service entries.
                Default format: [{'id': 1, 'port': 1}]
                Required format: List of dicts with keys: id, port
                  (String format not allowed due to multiple required fields)
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.application_list.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = List.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.application_list.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(List.required_fields()) }}
            
            Use List.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if entries is not None:
            entries = normalize_table_field(
                entries,
                mkey="id",
                required_fields=['id'],
                field_name="entries",
                example="[{'id': 1}]",
            )
        if default_network_services is not None:
            default_network_services = normalize_table_field(
                default_network_services,
                mkey="id",
                required_fields=['id', 'port'],
                field_name="default_network_services",
                example="[{'id': 1, 'port': 1}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            comment=comment,
            replacemsg_group=replacemsg_group,
            extended_log=extended_log,
            other_application_action=other_application_action,
            app_replacemsg=app_replacemsg,
            other_application_log=other_application_log,
            enforce_default_app_port=enforce_default_app_port,
            force_inclusion_ssl_di_sigs=force_inclusion_ssl_di_sigs,
            unknown_application_action=unknown_application_action,
            unknown_application_log=unknown_application_log,
            p2p_block_list=p2p_block_list,
            deep_app_inspection=deep_app_inspection,
            options=options,
            entries=entries,
            control_default_network_services=control_default_network_services,
            default_network_services=default_network_services,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.list import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/application/list",
            )

        endpoint = "/application/list"
        
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
        Delete application/list object.

        Configure application control lists.

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
            >>> result = fgt.api.cmdb.application_list.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/application/list/" + str(name)

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
        Check if application/list object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.application_list.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.application_list.exists(name=1):
            ...     fgt.api.cmdb.application_list.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/application/list"
        endpoint = f"{endpoint}/{name}"
        
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
        name: str | None = None,
        comment: str | None = None,
        replacemsg_group: str | None = None,
        extended_log: Literal["enable", "disable"] | None = None,
        other_application_action: Literal["pass", "block"] | None = None,
        app_replacemsg: Literal["disable", "enable"] | None = None,
        other_application_log: Literal["disable", "enable"] | None = None,
        enforce_default_app_port: Literal["disable", "enable"] | None = None,
        force_inclusion_ssl_di_sigs: Literal["disable", "enable"] | None = None,
        unknown_application_action: Literal["pass", "block"] | None = None,
        unknown_application_log: Literal["disable", "enable"] | None = None,
        p2p_block_list: Literal["skype", "edonkey", "bittorrent"] | list[str] | list[dict[str, Any]] | None = None,
        deep_app_inspection: Literal["disable", "enable"] | None = None,
        options: Literal["allow-dns", "allow-icmp", "allow-http", "allow-ssl"] | list[str] | list[dict[str, Any]] | None = None,
        entries: str | list[str] | list[dict[str, Any]] | None = None,
        control_default_network_services: Literal["disable", "enable"] | None = None,
        default_network_services: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update application/list object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            comment: Field comment
            replacemsg_group: Field replacemsg-group
            extended_log: Field extended-log
            other_application_action: Field other-application-action
            app_replacemsg: Field app-replacemsg
            other_application_log: Field other-application-log
            enforce_default_app_port: Field enforce-default-app-port
            force_inclusion_ssl_di_sigs: Field force-inclusion-ssl-di-sigs
            unknown_application_action: Field unknown-application-action
            unknown_application_log: Field unknown-application-log
            p2p_block_list: Field p2p-block-list
            deep_app_inspection: Field deep-app-inspection
            options: Field options
            entries: Field entries
            control_default_network_services: Field control-default-network-services
            default_network_services: Field default-network-services
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.application_list.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.application_list.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.application_list.set(payload_dict=obj_data)
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
            comment=comment,
            replacemsg_group=replacemsg_group,
            extended_log=extended_log,
            other_application_action=other_application_action,
            app_replacemsg=app_replacemsg,
            other_application_log=other_application_log,
            enforce_default_app_port=enforce_default_app_port,
            force_inclusion_ssl_di_sigs=force_inclusion_ssl_di_sigs,
            unknown_application_action=unknown_application_action,
            unknown_application_log=unknown_application_log,
            p2p_block_list=p2p_block_list,
            deep_app_inspection=deep_app_inspection,
            options=options,
            entries=entries,
            control_default_network_services=control_default_network_services,
            default_network_services=default_network_services,
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
        Move application/list object to a new position.
        
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
            >>> fgt.api.cmdb.application_list.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/application/list",
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
        Clone application/list object.
        
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
            >>> fgt.api.cmdb.application_list.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/application/list",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


