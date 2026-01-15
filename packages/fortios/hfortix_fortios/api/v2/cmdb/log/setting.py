"""
FortiOS CMDB - Log setting

Configuration endpoint for managing cmdb log/setting objects.

API Endpoints:
    GET    /cmdb/log/setting
    POST   /cmdb/log/setting
    PUT    /cmdb/log/setting/{identifier}
    DELETE /cmdb/log/setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_setting.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.log_setting.post(
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

class Setting(CRUDEndpoint, MetadataMixin):
    """Setting Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "setting"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "custom_log_fields": {
            "mkey": "field-id",
            "required_fields": ['field-id'],
            "example": "[{'field-id': 'value'}]",
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
        """Initialize Setting endpoint."""
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
        Retrieve log/setting configuration.

        Configure general log settings.

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
            >>> # Get all log/setting objects
            >>> result = fgt.api.cmdb.log_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_setting.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.log_setting.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.log_setting.get_schema()

        See Also:
            - post(): Create new log/setting object
            - put(): Update existing log/setting object
            - delete(): Remove log/setting object
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
            endpoint = f"/log/setting/{name}"
            unwrap_single = True
        else:
            endpoint = "/log/setting"
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
            >>> schema = fgt.api.cmdb.log_setting.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.log_setting.get_schema(format="json-schema")
        
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
        resolve_ip: Literal["enable", "disable"] | None = None,
        resolve_port: Literal["enable", "disable"] | None = None,
        log_user_in_upper: Literal["enable", "disable"] | None = None,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = None,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = None,
        extended_log: Literal["enable", "disable"] | None = None,
        local_in_allow: Literal["enable", "disable"] | None = None,
        local_in_deny_unicast: Literal["enable", "disable"] | None = None,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = None,
        local_in_policy_log: Literal["enable", "disable"] | None = None,
        local_out: Literal["enable", "disable"] | None = None,
        local_out_ioc_detection: Literal["enable", "disable"] | None = None,
        daemon_log: Literal["enable", "disable"] | None = None,
        neighbor_event: Literal["enable", "disable"] | None = None,
        brief_traffic_format: Literal["enable", "disable"] | None = None,
        user_anonymize: Literal["enable", "disable"] | None = None,
        expolicy_implicit_log: Literal["enable", "disable"] | None = None,
        log_policy_comment: Literal["enable", "disable"] | None = None,
        faz_override: Literal["enable", "disable"] | None = None,
        syslog_override: Literal["enable", "disable"] | None = None,
        rest_api_set: Literal["enable", "disable"] | None = None,
        rest_api_get: Literal["enable", "disable"] | None = None,
        rest_api_performance: Literal["enable", "disable"] | None = None,
        long_live_session_stat: Literal["enable", "disable"] | None = None,
        extended_utm_log: Literal["enable", "disable"] | None = None,
        zone_name: Literal["enable", "disable"] | None = None,
        web_svc_perf: Literal["enable", "disable"] | None = None,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = None,
        anonymization_hash: str | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing log/setting object.

        Configure general log settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            resolve_ip: Enable/disable adding resolved domain names to traffic logs if possible.
            resolve_port: Enable/disable adding resolved service names to traffic logs.
            log_user_in_upper: Enable/disable logs with user-in-upper.
            fwpolicy_implicit_log: Enable/disable implicit firewall policy logging.
            fwpolicy6_implicit_log: Enable/disable implicit firewall policy6 logging.
            extended_log: Enable/disable extended traffic logging.
            local_in_allow: Enable/disable local-in-allow logging.
            local_in_deny_unicast: Enable/disable local-in-deny-unicast logging.
            local_in_deny_broadcast: Enable/disable local-in-deny-broadcast logging.
            local_in_policy_log: Enable/disable local-in-policy logging.
            local_out: Enable/disable local-out logging.
            local_out_ioc_detection: Enable/disable local-out traffic IoC detection. Requires local-out to be enabled.
            daemon_log: Enable/disable daemon logging.
            neighbor_event: Enable/disable neighbor event logging.
            brief_traffic_format: Enable/disable brief format traffic logging.
            user_anonymize: Enable/disable anonymizing user names in log messages.
            expolicy_implicit_log: Enable/disable proxy firewall implicit policy logging.
            log_policy_comment: Enable/disable inserting policy comments into traffic logs.
            faz_override: Enable/disable override FortiAnalyzer settings.
            syslog_override: Enable/disable override Syslog settings.
            rest_api_set: Enable/disable REST API POST/PUT/DELETE request logging.
            rest_api_get: Enable/disable REST API GET request logging.
            rest_api_performance: Enable/disable REST API memory and performance stats in rest-api-get/set logs.
            long_live_session_stat: Enable/disable long-live-session statistics logging.
            extended_utm_log: Enable/disable extended UTM logging.
            zone_name: Enable/disable zone name logging.
            web_svc_perf: Enable/disable web-svc performance logging.
            custom_log_fields: Custom fields to append to all log messages.
                Default format: [{'field-id': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'field-id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'field-id': 'val1'}, ...]
                  - List of dicts: [{'field-id': 'value'}] (recommended)
            anonymization_hash: User name anonymization hash salt.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if custom_log_fields is not None:
            custom_log_fields = normalize_table_field(
                custom_log_fields,
                mkey="field-id",
                required_fields=['field-id'],
                field_name="custom_log_fields",
                example="[{'field-id': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            resolve_ip=resolve_ip,
            resolve_port=resolve_port,
            log_user_in_upper=log_user_in_upper,
            fwpolicy_implicit_log=fwpolicy_implicit_log,
            fwpolicy6_implicit_log=fwpolicy6_implicit_log,
            extended_log=extended_log,
            local_in_allow=local_in_allow,
            local_in_deny_unicast=local_in_deny_unicast,
            local_in_deny_broadcast=local_in_deny_broadcast,
            local_in_policy_log=local_in_policy_log,
            local_out=local_out,
            local_out_ioc_detection=local_out_ioc_detection,
            daemon_log=daemon_log,
            neighbor_event=neighbor_event,
            brief_traffic_format=brief_traffic_format,
            user_anonymize=user_anonymize,
            expolicy_implicit_log=expolicy_implicit_log,
            log_policy_comment=log_policy_comment,
            faz_override=faz_override,
            syslog_override=syslog_override,
            rest_api_set=rest_api_set,
            rest_api_get=rest_api_get,
            rest_api_performance=rest_api_performance,
            long_live_session_stat=long_live_session_stat,
            extended_utm_log=extended_utm_log,
            zone_name=zone_name,
            web_svc_perf=web_svc_perf,
            custom_log_fields=custom_log_fields,
            anonymization_hash=anonymization_hash,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/setting",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/log/setting"

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
        Move log/setting object to a new position.
        
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
            >>> fgt.api.cmdb.log_setting.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/log/setting",
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
        Clone log/setting object.
        
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
            >>> fgt.api.cmdb.log_setting.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/log/setting",
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
        Check if log/setting object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.log_setting.exists(name="myobj"):
            ...     fgt.api.cmdb.log_setting.post(payload_dict=data)
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

