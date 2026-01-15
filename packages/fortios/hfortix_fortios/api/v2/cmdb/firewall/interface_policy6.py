"""
FortiOS CMDB - Firewall interface_policy6

Configuration endpoint for managing cmdb firewall/interface_policy6 objects.

API Endpoints:
    GET    /cmdb/firewall/interface_policy6
    POST   /cmdb/firewall/interface_policy6
    PUT    /cmdb/firewall/interface_policy6/{identifier}
    DELETE /cmdb/firewall/interface_policy6/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall_interface_policy6.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.firewall_interface_policy6.post(
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

class InterfacePolicy6(CRUDEndpoint, MetadataMixin):
    """InterfacePolicy6 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "interface_policy6"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "srcaddr6": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "dstaddr6": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "service6": {
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
        """Initialize InterfacePolicy6 endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        policyid: int | None = None,
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
        Retrieve firewall/interface_policy6 configuration.

        Configure IPv6 interface policies.

        Args:
            policyid: Integer identifier to retrieve specific object.
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
            >>> # Get all firewall/interface_policy6 objects
            >>> result = fgt.api.cmdb.firewall_interface_policy6.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific firewall/interface_policy6 by policyid
            >>> result = fgt.api.cmdb.firewall_interface_policy6.get(policyid=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.firewall_interface_policy6.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.firewall_interface_policy6.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.firewall_interface_policy6.get_schema()

        See Also:
            - post(): Create new firewall/interface_policy6 object
            - put(): Update existing firewall/interface_policy6 object
            - delete(): Remove firewall/interface_policy6 object
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
        
        if policyid:
            endpoint = "/firewall/interface-policy6/" + str(policyid)
            unwrap_single = True
        else:
            endpoint = "/firewall/interface-policy6"
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
            >>> schema = fgt.api.cmdb.firewall_interface_policy6.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.firewall_interface_policy6.get_schema(format="json-schema")
        
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
        policyid: int | None = None,
        uuid: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        interface: str | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        service6: str | list[str] | list[dict[str, Any]] | None = None,
        application_list_status: Literal["enable", "disable"] | None = None,
        application_list: str | None = None,
        ips_sensor_status: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        dsri: Literal["enable", "disable"] | None = None,
        av_profile_status: Literal["enable", "disable"] | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: Literal["enable", "disable"] | None = None,
        webfilter_profile: str | None = None,
        casb_profile_status: Literal["enable", "disable"] | None = None,
        casb_profile: str | None = None,
        emailfilter_profile_status: Literal["enable", "disable"] | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: Literal["enable", "disable"] | None = None,
        dlp_profile: str | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing firewall/interface_policy6 object.

        Configure IPv6 interface policies.

        Args:
            payload_dict: Object data as dict. Must include policyid (primary key).
            policyid: Policy ID (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            status: Enable/disable this policy.
            comments: Comments.
            logtraffic: Logging type to be used in this policy (Options: all | utm | disable, Default: utm).
            interface: Monitored interface name from available interfaces.
            srcaddr6: IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6: IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            service6: Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            application_list_status: Enable/disable application control.
            application_list: Application list name.
            ips_sensor_status: Enable/disable IPS.
            ips_sensor: IPS sensor name.
            dsri: Enable/disable DSRI.
            av_profile_status: Enable/disable antivirus.
            av_profile: Antivirus profile.
            webfilter_profile_status: Enable/disable web filtering.
            webfilter_profile: Web filter profile.
            casb_profile_status: Enable/disable CASB.
            casb_profile: CASB profile.
            emailfilter_profile_status: Enable/disable email filter.
            emailfilter_profile: Email filter profile.
            dlp_profile_status: Enable/disable DLP.
            dlp_profile: DLP profile name.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.firewall_interface_policy6.put(
            ...     policyid=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.firewall_interface_policy6.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if srcaddr6 is not None:
            srcaddr6 = normalize_table_field(
                srcaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="srcaddr6",
                example="[{'name': 'value'}]",
            )
        if dstaddr6 is not None:
            dstaddr6 = normalize_table_field(
                dstaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="dstaddr6",
                example="[{'name': 'value'}]",
            )
        if service6 is not None:
            service6 = normalize_table_field(
                service6,
                mkey="name",
                required_fields=['name'],
                field_name="service6",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            policyid=policyid,
            uuid=uuid,
            status=status,
            comments=comments,
            logtraffic=logtraffic,
            interface=interface,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            service6=service6,
            application_list_status=application_list_status,
            application_list=application_list,
            ips_sensor_status=ips_sensor_status,
            ips_sensor=ips_sensor,
            dsri=dsri,
            av_profile_status=av_profile_status,
            av_profile=av_profile,
            webfilter_profile_status=webfilter_profile_status,
            webfilter_profile=webfilter_profile,
            casb_profile_status=casb_profile_status,
            casb_profile=casb_profile,
            emailfilter_profile_status=emailfilter_profile_status,
            emailfilter_profile=emailfilter_profile,
            dlp_profile_status=dlp_profile_status,
            dlp_profile=dlp_profile,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.interface_policy6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/interface_policy6",
            )
        
        policyid_value = payload_data.get("policyid")
        if not policyid_value:
            raise ValueError("policyid is required for PUT")
        endpoint = "/firewall/interface-policy6/" + str(policyid_value)

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
        policyid: int | None = None,
        uuid: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        interface: str | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        service6: str | list[str] | list[dict[str, Any]] | None = None,
        application_list_status: Literal["enable", "disable"] | None = None,
        application_list: str | None = None,
        ips_sensor_status: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        dsri: Literal["enable", "disable"] | None = None,
        av_profile_status: Literal["enable", "disable"] | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: Literal["enable", "disable"] | None = None,
        webfilter_profile: str | None = None,
        casb_profile_status: Literal["enable", "disable"] | None = None,
        casb_profile: str | None = None,
        emailfilter_profile_status: Literal["enable", "disable"] | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: Literal["enable", "disable"] | None = None,
        dlp_profile: str | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new firewall/interface_policy6 object.

        Configure IPv6 interface policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            policyid: Policy ID (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            status: Enable/disable this policy.
            comments: Comments.
            logtraffic: Logging type to be used in this policy (Options: all | utm | disable, Default: utm).
            interface: Monitored interface name from available interfaces.
            srcaddr6: IPv6 address object to limit traffic monitoring to network traffic sent from the specified address or range.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            dstaddr6: IPv6 address object to limit traffic monitoring to network traffic sent to the specified address or range.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            service6: Service name.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            application_list_status: Enable/disable application control.
            application_list: Application list name.
            ips_sensor_status: Enable/disable IPS.
            ips_sensor: IPS sensor name.
            dsri: Enable/disable DSRI.
            av_profile_status: Enable/disable antivirus.
            av_profile: Antivirus profile.
            webfilter_profile_status: Enable/disable web filtering.
            webfilter_profile: Web filter profile.
            casb_profile_status: Enable/disable CASB.
            casb_profile: CASB profile.
            emailfilter_profile_status: Enable/disable email filter.
            emailfilter_profile: Email filter profile.
            dlp_profile_status: Enable/disable DLP.
            dlp_profile: DLP profile name.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.firewall_interface_policy6.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created policyid: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = InterfacePolicy6.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.firewall_interface_policy6.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(InterfacePolicy6.required_fields()) }}
            
            Use InterfacePolicy6.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if srcaddr6 is not None:
            srcaddr6 = normalize_table_field(
                srcaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="srcaddr6",
                example="[{'name': 'value'}]",
            )
        if dstaddr6 is not None:
            dstaddr6 = normalize_table_field(
                dstaddr6,
                mkey="name",
                required_fields=['name'],
                field_name="dstaddr6",
                example="[{'name': 'value'}]",
            )
        if service6 is not None:
            service6 = normalize_table_field(
                service6,
                mkey="name",
                required_fields=['name'],
                field_name="service6",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            policyid=policyid,
            uuid=uuid,
            status=status,
            comments=comments,
            logtraffic=logtraffic,
            interface=interface,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            service6=service6,
            application_list_status=application_list_status,
            application_list=application_list,
            ips_sensor_status=ips_sensor_status,
            ips_sensor=ips_sensor,
            dsri=dsri,
            av_profile_status=av_profile_status,
            av_profile=av_profile,
            webfilter_profile_status=webfilter_profile_status,
            webfilter_profile=webfilter_profile,
            casb_profile_status=casb_profile_status,
            casb_profile=casb_profile,
            emailfilter_profile_status=emailfilter_profile_status,
            emailfilter_profile=emailfilter_profile,
            dlp_profile_status=dlp_profile_status,
            dlp_profile=dlp_profile,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.interface_policy6 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/firewall/interface_policy6",
            )

        endpoint = "/firewall/interface-policy6"
        
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
        policyid: int | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete firewall/interface_policy6 object.

        Configure IPv6 interface policies.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If policyid is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.firewall_interface_policy6.delete(policyid=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not policyid:
            raise ValueError("policyid is required for DELETE")
        endpoint = "/firewall/interface-policy6/" + str(policyid)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        policyid: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if firewall/interface_policy6 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            policyid: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.firewall_interface_policy6.exists(policyid=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.firewall_interface_policy6.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_interface_policy6.delete(policyid=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                policyid=policyid,
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
        policyid: int | None = None,
        uuid: str | None = None,
        status: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        logtraffic: Literal["all", "utm", "disable"] | None = None,
        interface: str | None = None,
        srcaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        dstaddr6: str | list[str] | list[dict[str, Any]] | None = None,
        service6: str | list[str] | list[dict[str, Any]] | None = None,
        application_list_status: Literal["enable", "disable"] | None = None,
        application_list: str | None = None,
        ips_sensor_status: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        dsri: Literal["enable", "disable"] | None = None,
        av_profile_status: Literal["enable", "disable"] | None = None,
        av_profile: str | None = None,
        webfilter_profile_status: Literal["enable", "disable"] | None = None,
        webfilter_profile: str | None = None,
        casb_profile_status: Literal["enable", "disable"] | None = None,
        casb_profile: str | None = None,
        emailfilter_profile_status: Literal["enable", "disable"] | None = None,
        emailfilter_profile: str | None = None,
        dlp_profile_status: Literal["enable", "disable"] | None = None,
        dlp_profile: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update firewall/interface_policy6 object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (policyid) in the payload.

        Args:
            payload_dict: Resource data including policyid (primary key)
            policyid: Field policyid
            uuid: Field uuid
            status: Field status
            comments: Field comments
            logtraffic: Field logtraffic
            interface: Field interface
            srcaddr6: Field srcaddr6
            dstaddr6: Field dstaddr6
            service6: Field service6
            application_list_status: Field application-list-status
            application_list: Field application-list
            ips_sensor_status: Field ips-sensor-status
            ips_sensor: Field ips-sensor
            dsri: Field dsri
            av_profile_status: Field av-profile-status
            av_profile: Field av-profile
            webfilter_profile_status: Field webfilter-profile-status
            webfilter_profile: Field webfilter-profile
            casb_profile_status: Field casb-profile-status
            casb_profile: Field casb-profile
            emailfilter_profile_status: Field emailfilter-profile-status
            emailfilter_profile: Field emailfilter-profile
            dlp_profile_status: Field dlp-profile-status
            dlp_profile: Field dlp-profile
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If policyid is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.firewall_interface_policy6.set(
            ...     policyid=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "policyid": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.firewall_interface_policy6.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.firewall_interface_policy6.set(payload_dict=obj_data)
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
            policyid=policyid,
            uuid=uuid,
            status=status,
            comments=comments,
            logtraffic=logtraffic,
            interface=interface,
            srcaddr6=srcaddr6,
            dstaddr6=dstaddr6,
            service6=service6,
            application_list_status=application_list_status,
            application_list=application_list,
            ips_sensor_status=ips_sensor_status,
            ips_sensor=ips_sensor,
            dsri=dsri,
            av_profile_status=av_profile_status,
            av_profile=av_profile,
            webfilter_profile_status=webfilter_profile_status,
            webfilter_profile=webfilter_profile,
            casb_profile_status=casb_profile_status,
            casb_profile=casb_profile,
            emailfilter_profile_status=emailfilter_profile_status,
            emailfilter_profile=emailfilter_profile,
            dlp_profile_status=dlp_profile_status,
            dlp_profile=dlp_profile,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("policyid")
        if not mkey_value:
            raise ValueError("policyid is required for set()")
        
        # Check if resource exists
        if self.exists(policyid=mkey_value, vdom=vdom):
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
        policyid: int,
        action: Literal["before", "after"],
        reference_policyid: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move firewall/interface_policy6 object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            policyid: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_policyid: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.firewall_interface_policy6.move(
            ...     policyid=100,
            ...     action="before",
            ...     reference_policyid=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/firewall/interface-policy6",
            params={
                "policyid": policyid,
                "action": "move",
                action: reference_policyid,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        policyid: int,
        new_policyid: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone firewall/interface_policy6 object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            policyid: Identifier of object to clone
            new_policyid: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.firewall_interface_policy6.clone(
            ...     policyid=1,
            ...     new_policyid=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/firewall/interface-policy6",
            params={
                "policyid": policyid,
                "new_policyid": new_policyid,
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
        policyid: int,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if firewall/interface_policy6 object exists.
        
        Args:
            policyid: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.firewall_interface_policy6.exists(policyid=1):
            ...     fgt.api.cmdb.firewall_interface_policy6.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                policyid=policyid,
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

