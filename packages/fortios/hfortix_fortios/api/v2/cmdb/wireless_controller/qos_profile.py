"""
FortiOS CMDB - Wireless_controller qos_profile

Configuration endpoint for managing cmdb wireless_controller/qos_profile objects.

API Endpoints:
    GET    /cmdb/wireless_controller/qos_profile
    POST   /cmdb/wireless_controller/qos_profile
    PUT    /cmdb/wireless_controller/qos_profile/{identifier}
    DELETE /cmdb/wireless_controller/qos_profile/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_qos_profile.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.wireless_controller_qos_profile.post(
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

class QosProfile(CRUDEndpoint, MetadataMixin):
    """QosProfile Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "qos_profile"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "dscp_wmm_vo": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "dscp_wmm_vi": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "dscp_wmm_be": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
        },
        "dscp_wmm_bk": {
            "mkey": "id",
            "required_fields": ['id'],
            "example": "[{'id': 1}]",
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
        """Initialize QosProfile endpoint."""
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
        Retrieve wireless_controller/qos_profile configuration.

        Configure WiFi quality of service (QoS) profiles.

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
            >>> # Get all wireless_controller/qos_profile objects
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/qos_profile by name
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.wireless_controller_qos_profile.get_schema()

        See Also:
            - post(): Create new wireless_controller/qos_profile object
            - put(): Update existing wireless_controller/qos_profile object
            - delete(): Remove wireless_controller/qos_profile object
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
            endpoint = "/wireless-controller/qos-profile/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/wireless-controller/qos-profile"
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
            >>> schema = fgt.api.cmdb.wireless_controller_qos_profile.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.wireless_controller_qos_profile.get_schema(format="json-schema")
        
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
        uplink: int | None = None,
        downlink: int | None = None,
        uplink_sta: int | None = None,
        downlink_sta: int | None = None,
        burst: Literal["enable", "disable"] | None = None,
        wmm: Literal["enable", "disable"] | None = None,
        wmm_uapsd: Literal["enable", "disable"] | None = None,
        call_admission_control: Literal["enable", "disable"] | None = None,
        call_capacity: int | None = None,
        bandwidth_admission_control: Literal["enable", "disable"] | None = None,
        bandwidth_capacity: int | None = None,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = None,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = None,
        wmm_dscp_marking: Literal["enable", "disable"] | None = None,
        wmm_vo_dscp: int | None = None,
        wmm_vi_dscp: int | None = None,
        wmm_be_dscp: int | None = None,
        wmm_bk_dscp: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing wireless_controller/qos_profile object.

        Configure WiFi quality of service (QoS) profiles.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: WiFi QoS profile name.
            comment: Comment.
            uplink: Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            downlink: Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            uplink_sta: Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).
            downlink_sta: Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).
            burst: Enable/disable client rate burst.
            wmm: Enable/disable WiFi multi-media (WMM) control.
            wmm_uapsd: Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.
            call_admission_control: Enable/disable WMM call admission control.
            call_capacity: Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10).
            bandwidth_admission_control: Enable/disable WMM bandwidth admission control.
            bandwidth_capacity: Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).
            dscp_wmm_mapping: Enable/disable Differentiated Services Code Point (DSCP) mapping.
            dscp_wmm_vo: DSCP mapping for voice access (default = 48 56).
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            dscp_wmm_vi: DSCP mapping for video access (default = 32 40).
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            dscp_wmm_be: DSCP mapping for best effort access (default = 0 24).
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            dscp_wmm_bk: DSCP mapping for background access (default = 8 16).
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            wmm_dscp_marking: Enable/disable WMM Differentiated Services Code Point (DSCP) marking.
            wmm_vo_dscp: DSCP marking for voice access (default = 48).
            wmm_vi_dscp: DSCP marking for video access (default = 32).
            wmm_be_dscp: DSCP marking for best effort access (default = 0).
            wmm_bk_dscp: DSCP marking for background access (default = 8).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if dscp_wmm_vo is not None:
            dscp_wmm_vo = normalize_table_field(
                dscp_wmm_vo,
                mkey="id",
                required_fields=['id'],
                field_name="dscp_wmm_vo",
                example="[{'id': 1}]",
            )
        if dscp_wmm_vi is not None:
            dscp_wmm_vi = normalize_table_field(
                dscp_wmm_vi,
                mkey="id",
                required_fields=['id'],
                field_name="dscp_wmm_vi",
                example="[{'id': 1}]",
            )
        if dscp_wmm_be is not None:
            dscp_wmm_be = normalize_table_field(
                dscp_wmm_be,
                mkey="id",
                required_fields=['id'],
                field_name="dscp_wmm_be",
                example="[{'id': 1}]",
            )
        if dscp_wmm_bk is not None:
            dscp_wmm_bk = normalize_table_field(
                dscp_wmm_bk,
                mkey="id",
                required_fields=['id'],
                field_name="dscp_wmm_bk",
                example="[{'id': 1}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            comment=comment,
            uplink=uplink,
            downlink=downlink,
            uplink_sta=uplink_sta,
            downlink_sta=downlink_sta,
            burst=burst,
            wmm=wmm,
            wmm_uapsd=wmm_uapsd,
            call_admission_control=call_admission_control,
            call_capacity=call_capacity,
            bandwidth_admission_control=bandwidth_admission_control,
            bandwidth_capacity=bandwidth_capacity,
            dscp_wmm_mapping=dscp_wmm_mapping,
            dscp_wmm_vo=dscp_wmm_vo,
            dscp_wmm_vi=dscp_wmm_vi,
            dscp_wmm_be=dscp_wmm_be,
            dscp_wmm_bk=dscp_wmm_bk,
            wmm_dscp_marking=wmm_dscp_marking,
            wmm_vo_dscp=wmm_vo_dscp,
            wmm_vi_dscp=wmm_vi_dscp,
            wmm_be_dscp=wmm_be_dscp,
            wmm_bk_dscp=wmm_bk_dscp,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.qos_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/qos_profile",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller/qos-profile/" + str(name_value)

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
        uplink: int | None = None,
        downlink: int | None = None,
        uplink_sta: int | None = None,
        downlink_sta: int | None = None,
        burst: Literal["enable", "disable"] | None = None,
        wmm: Literal["enable", "disable"] | None = None,
        wmm_uapsd: Literal["enable", "disable"] | None = None,
        call_admission_control: Literal["enable", "disable"] | None = None,
        call_capacity: int | None = None,
        bandwidth_admission_control: Literal["enable", "disable"] | None = None,
        bandwidth_capacity: int | None = None,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = None,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = None,
        wmm_dscp_marking: Literal["enable", "disable"] | None = None,
        wmm_vo_dscp: int | None = None,
        wmm_vi_dscp: int | None = None,
        wmm_be_dscp: int | None = None,
        wmm_bk_dscp: int | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new wireless_controller/qos_profile object.

        Configure WiFi quality of service (QoS) profiles.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: WiFi QoS profile name.
            comment: Comment.
            uplink: Maximum uplink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            downlink: Maximum downlink bandwidth for Virtual Access Points (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            uplink_sta: Maximum uplink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).
            downlink_sta: Maximum downlink bandwidth for clients (0 - 2097152 Kbps, default = 0, 0 means no limit).
            burst: Enable/disable client rate burst.
            wmm: Enable/disable WiFi multi-media (WMM) control.
            wmm_uapsd: Enable/disable WMM Unscheduled Automatic Power Save Delivery (U-APSD) power save mode.
            call_admission_control: Enable/disable WMM call admission control.
            call_capacity: Maximum number of Voice over WLAN (VoWLAN) phones allowed (0 - 60, default = 10).
            bandwidth_admission_control: Enable/disable WMM bandwidth admission control.
            bandwidth_capacity: Maximum bandwidth capacity allowed (1 - 600000 Kbps, default = 2000).
            dscp_wmm_mapping: Enable/disable Differentiated Services Code Point (DSCP) mapping.
            dscp_wmm_vo: DSCP mapping for voice access (default = 48 56).
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            dscp_wmm_vi: DSCP mapping for video access (default = 32 40).
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            dscp_wmm_be: DSCP mapping for best effort access (default = 0 24).
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            dscp_wmm_bk: DSCP mapping for background access (default = 8 16).
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            wmm_dscp_marking: Enable/disable WMM Differentiated Services Code Point (DSCP) marking.
            wmm_vo_dscp: DSCP marking for voice access (default = 48).
            wmm_vi_dscp: DSCP marking for video access (default = 32).
            wmm_be_dscp: DSCP marking for best effort access (default = 0).
            wmm_bk_dscp: DSCP marking for background access (default = 8).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = QosProfile.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(QosProfile.required_fields()) }}
            
            Use QosProfile.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if dscp_wmm_vo is not None:
            dscp_wmm_vo = normalize_table_field(
                dscp_wmm_vo,
                mkey="id",
                required_fields=['id'],
                field_name="dscp_wmm_vo",
                example="[{'id': 1}]",
            )
        if dscp_wmm_vi is not None:
            dscp_wmm_vi = normalize_table_field(
                dscp_wmm_vi,
                mkey="id",
                required_fields=['id'],
                field_name="dscp_wmm_vi",
                example="[{'id': 1}]",
            )
        if dscp_wmm_be is not None:
            dscp_wmm_be = normalize_table_field(
                dscp_wmm_be,
                mkey="id",
                required_fields=['id'],
                field_name="dscp_wmm_be",
                example="[{'id': 1}]",
            )
        if dscp_wmm_bk is not None:
            dscp_wmm_bk = normalize_table_field(
                dscp_wmm_bk,
                mkey="id",
                required_fields=['id'],
                field_name="dscp_wmm_bk",
                example="[{'id': 1}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            comment=comment,
            uplink=uplink,
            downlink=downlink,
            uplink_sta=uplink_sta,
            downlink_sta=downlink_sta,
            burst=burst,
            wmm=wmm,
            wmm_uapsd=wmm_uapsd,
            call_admission_control=call_admission_control,
            call_capacity=call_capacity,
            bandwidth_admission_control=bandwidth_admission_control,
            bandwidth_capacity=bandwidth_capacity,
            dscp_wmm_mapping=dscp_wmm_mapping,
            dscp_wmm_vo=dscp_wmm_vo,
            dscp_wmm_vi=dscp_wmm_vi,
            dscp_wmm_be=dscp_wmm_be,
            dscp_wmm_bk=dscp_wmm_bk,
            wmm_dscp_marking=wmm_dscp_marking,
            wmm_vo_dscp=wmm_vo_dscp,
            wmm_vi_dscp=wmm_vi_dscp,
            wmm_be_dscp=wmm_be_dscp,
            wmm_bk_dscp=wmm_bk_dscp,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.qos_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/qos_profile",
            )

        endpoint = "/wireless-controller/qos-profile"
        
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
        Delete wireless_controller/qos_profile object.

        Configure WiFi quality of service (QoS) profiles.

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
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller/qos-profile/" + str(name)

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
        Check if wireless_controller/qos_profile object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_qos_profile.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_qos_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_qos_profile.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Use direct request with silent error handling to avoid logging 404s
        # This is expected behavior for exists() - 404 just means "doesn't exist"
        endpoint = "/wireless_controller/qos_profile"
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
        uplink: int | None = None,
        downlink: int | None = None,
        uplink_sta: int | None = None,
        downlink_sta: int | None = None,
        burst: Literal["enable", "disable"] | None = None,
        wmm: Literal["enable", "disable"] | None = None,
        wmm_uapsd: Literal["enable", "disable"] | None = None,
        call_admission_control: Literal["enable", "disable"] | None = None,
        call_capacity: int | None = None,
        bandwidth_admission_control: Literal["enable", "disable"] | None = None,
        bandwidth_capacity: int | None = None,
        dscp_wmm_mapping: Literal["enable", "disable"] | None = None,
        dscp_wmm_vo: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_vi: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_be: str | list[str] | list[dict[str, Any]] | None = None,
        dscp_wmm_bk: str | list[str] | list[dict[str, Any]] | None = None,
        wmm_dscp_marking: Literal["enable", "disable"] | None = None,
        wmm_vo_dscp: int | None = None,
        wmm_vi_dscp: int | None = None,
        wmm_be_dscp: int | None = None,
        wmm_bk_dscp: int | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update wireless_controller/qos_profile object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            comment: Field comment
            uplink: Field uplink
            downlink: Field downlink
            uplink_sta: Field uplink-sta
            downlink_sta: Field downlink-sta
            burst: Field burst
            wmm: Field wmm
            wmm_uapsd: Field wmm-uapsd
            call_admission_control: Field call-admission-control
            call_capacity: Field call-capacity
            bandwidth_admission_control: Field bandwidth-admission-control
            bandwidth_capacity: Field bandwidth-capacity
            dscp_wmm_mapping: Field dscp-wmm-mapping
            dscp_wmm_vo: Field dscp-wmm-vo
            dscp_wmm_vi: Field dscp-wmm-vi
            dscp_wmm_be: Field dscp-wmm-be
            dscp_wmm_bk: Field dscp-wmm-bk
            wmm_dscp_marking: Field wmm-dscp-marking
            wmm_vo_dscp: Field wmm-vo-dscp
            wmm_vi_dscp: Field wmm-vi-dscp
            wmm_be_dscp: Field wmm-be-dscp
            wmm_bk_dscp: Field wmm-bk-dscp
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_qos_profile.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_qos_profile.set(payload_dict=obj_data)
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
            uplink=uplink,
            downlink=downlink,
            uplink_sta=uplink_sta,
            downlink_sta=downlink_sta,
            burst=burst,
            wmm=wmm,
            wmm_uapsd=wmm_uapsd,
            call_admission_control=call_admission_control,
            call_capacity=call_capacity,
            bandwidth_admission_control=bandwidth_admission_control,
            bandwidth_capacity=bandwidth_capacity,
            dscp_wmm_mapping=dscp_wmm_mapping,
            dscp_wmm_vo=dscp_wmm_vo,
            dscp_wmm_vi=dscp_wmm_vi,
            dscp_wmm_be=dscp_wmm_be,
            dscp_wmm_bk=dscp_wmm_bk,
            wmm_dscp_marking=wmm_dscp_marking,
            wmm_vo_dscp=wmm_vo_dscp,
            wmm_vi_dscp=wmm_vi_dscp,
            wmm_be_dscp=wmm_be_dscp,
            wmm_bk_dscp=wmm_bk_dscp,
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
        Move wireless_controller/qos_profile object to a new position.
        
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
            >>> fgt.api.cmdb.wireless_controller_qos_profile.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller/qos-profile",
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
        Clone wireless_controller/qos_profile object.
        
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
            >>> fgt.api.cmdb.wireless_controller_qos_profile.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller/qos-profile",
            params={
                "name": name,
                "new_name": new_name,
                "action": "clone",
                "vdom": vdom,
                **kwargs,
            },
        )


