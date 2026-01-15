"""
FortiOS CMDB - Log fortianalyzer override_setting

Configuration endpoint for managing cmdb log/fortianalyzer/override_setting objects.

API Endpoints:
    GET    /cmdb/log/fortianalyzer/override_setting
    POST   /cmdb/log/fortianalyzer/override_setting
    PUT    /cmdb/log/fortianalyzer/override_setting/{identifier}
    DELETE /cmdb/log/fortianalyzer/override_setting/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log_fortianalyzer_override_setting.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.log_fortianalyzer_override_setting.post(
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

class OverrideSetting(CRUDEndpoint, MetadataMixin):
    """OverrideSetting Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "override_setting"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "serial": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
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
        """Initialize OverrideSetting endpoint."""
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
        Retrieve log/fortianalyzer/override_setting configuration.

        Override FortiAnalyzer settings.

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
            >>> # Get all log/fortianalyzer/override_setting objects
            >>> result = fgt.api.cmdb.log_fortianalyzer_override_setting.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.log_fortianalyzer_override_setting.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.log_fortianalyzer_override_setting.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.log_fortianalyzer_override_setting.get_schema()

        See Also:
            - post(): Create new log/fortianalyzer/override_setting object
            - put(): Update existing log/fortianalyzer/override_setting object
            - delete(): Remove log/fortianalyzer/override_setting object
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
            endpoint = f"/log.fortianalyzer/override-setting/{name}"
            unwrap_single = True
        else:
            endpoint = "/log.fortianalyzer/override-setting"
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
            >>> schema = fgt.api.cmdb.log_fortianalyzer_override_setting.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.log_fortianalyzer_override_setting.get_schema(format="json-schema")
        
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
        use_management_vdom: Literal["enable", "disable"] | None = None,
        status: Literal["enable", "disable"] | None = None,
        ips_archive: Literal["enable", "disable"] | None = None,
        server: str | None = None,
        alt_server: str | None = None,
        fallback_to_primary: Literal["enable", "disable"] | None = None,
        certificate_verification: Literal["enable", "disable"] | None = None,
        serial: str | list[str] | list[dict[str, Any]] | None = None,
        server_cert_ca: str | None = None,
        preshared_key: str | None = None,
        access_config: Literal["enable", "disable"] | None = None,
        hmac_algorithm: Literal["sha256"] | None = None,
        enc_algorithm: Literal["high-medium", "high", "low"] | None = None,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = None,
        conn_timeout: int | None = None,
        monitor_keepalive_period: int | None = None,
        monitor_failure_retry_period: int | None = None,
        certificate: str | None = None,
        source_ip: str | None = None,
        upload_option: Literal["store-and-upload", "realtime", "1-minute", "5-minute"] | None = None,
        upload_interval: Literal["daily", "weekly", "monthly"] | None = None,
        upload_day: str | None = None,
        upload_time: str | None = None,
        reliable: Literal["enable", "disable"] | None = None,
        priority: Literal["default", "low"] | None = None,
        max_log_rate: int | None = None,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing log/fortianalyzer/override_setting object.

        Override FortiAnalyzer settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            use_management_vdom: Enable/disable use of management VDOM IP address as source IP for logs sent to FortiAnalyzer.
            status: Enable/disable logging to FortiAnalyzer.
            ips_archive: Enable/disable IPS packet archive logging.
            server: The remote FortiAnalyzer.
            alt_server: Alternate FortiAnalyzer.
            fallback_to_primary: Enable/disable this FortiGate unit to fallback to the primary FortiAnalyzer when it is available.
            certificate_verification: Enable/disable identity verification of FortiAnalyzer by use of certificate.
            serial: Serial numbers of the FortiAnalyzer.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            server_cert_ca: Mandatory CA on FortiGate in certificate chain of server.
            preshared_key: Preshared-key used for auto-authorization on FortiAnalyzer.
            access_config: Enable/disable FortiAnalyzer access to configuration and data.
            hmac_algorithm: OFTP login hash algorithm.
            enc_algorithm: Configure the level of SSL protection for secure communication with FortiAnalyzer.
            ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting).
            conn_timeout: FortiAnalyzer connection time-out in seconds (for status and log buffer).
            monitor_keepalive_period: Time between OFTP keepalives in seconds (for status and log buffer).
            monitor_failure_retry_period: Time between FortiAnalyzer connection retries in seconds (for status and log buffer).
            certificate: Certificate used to communicate with FortiAnalyzer.
            source_ip: Source IPv4 or IPv6 address used to communicate with FortiAnalyzer.
            upload_option: Enable/disable logging to hard disk and then uploading to FortiAnalyzer.
            upload_interval: Frequency to upload log files to FortiAnalyzer.
            upload_day: Day of week (month) to upload logs.
            upload_time: Time to upload logs (hh:mm).
            reliable: Enable/disable reliable logging to FortiAnalyzer.
            priority: Set log transmission priority.
            max_log_rate: FortiAnalyzer maximum log rate in MBps (0 = unlimited).
            interface_select_method: Specify how to select outgoing interface to reach server.
            interface: Specify outgoing interface to reach server.
            vrf_select: VRF ID used for connection to server.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.log_fortianalyzer_override_setting.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.log_fortianalyzer_override_setting.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if serial is not None:
            serial = normalize_table_field(
                serial,
                mkey="name",
                required_fields=['name'],
                field_name="serial",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            use_management_vdom=use_management_vdom,
            status=status,
            ips_archive=ips_archive,
            server=server,
            alt_server=alt_server,
            fallback_to_primary=fallback_to_primary,
            certificate_verification=certificate_verification,
            serial=serial,
            server_cert_ca=server_cert_ca,
            preshared_key=preshared_key,
            access_config=access_config,
            hmac_algorithm=hmac_algorithm,
            enc_algorithm=enc_algorithm,
            ssl_min_proto_version=ssl_min_proto_version,
            conn_timeout=conn_timeout,
            monitor_keepalive_period=monitor_keepalive_period,
            monitor_failure_retry_period=monitor_failure_retry_period,
            certificate=certificate,
            source_ip=source_ip,
            upload_option=upload_option,
            upload_interval=upload_interval,
            upload_day=upload_day,
            upload_time=upload_time,
            reliable=reliable,
            priority=priority,
            max_log_rate=max_log_rate,
            interface_select_method=interface_select_method,
            interface=interface,
            vrf_select=vrf_select,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.override_setting import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/log/fortianalyzer/override_setting",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/log.fortianalyzer/override-setting"

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
        Move log/fortianalyzer/override_setting object to a new position.
        
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
            >>> fgt.api.cmdb.log_fortianalyzer_override_setting.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/log.fortianalyzer/override-setting",
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
        Clone log/fortianalyzer/override_setting object.
        
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
            >>> fgt.api.cmdb.log_fortianalyzer_override_setting.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/log.fortianalyzer/override-setting",
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
        Check if log/fortianalyzer/override_setting object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.log_fortianalyzer_override_setting.exists(name="myobj"):
            ...     fgt.api.cmdb.log_fortianalyzer_override_setting.post(payload_dict=data)
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

