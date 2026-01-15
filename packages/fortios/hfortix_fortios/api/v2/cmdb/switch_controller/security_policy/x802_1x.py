"""
FortiOS CMDB - Switch_controller security_policy x802_1x

Configuration endpoint for managing cmdb switch_controller/security_policy/x802_1x objects.

API Endpoints:
    GET    /cmdb/switch_controller/security_policy/x802_1x
    POST   /cmdb/switch_controller/security_policy/x802_1x
    PUT    /cmdb/switch_controller/security_policy/x802_1x/{identifier}
    DELETE /cmdb/switch_controller/security_policy/x802_1x/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.post(
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

class X8021x(CRUDEndpoint, MetadataMixin):
    """X8021x Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "x802_1x"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "user_group": {
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
        """Initialize X8021x endpoint."""
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
        Retrieve switch_controller/security_policy/x802_1x configuration.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

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
            >>> # Get all switch_controller/security_policy/x802_1x objects
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific switch_controller/security_policy/x802_1x by name
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get_schema()

        See Also:
            - post(): Create new switch_controller/security_policy/x802_1x object
            - put(): Update existing switch_controller/security_policy/x802_1x object
            - delete(): Remove switch_controller/security_policy/x802_1x object
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
            endpoint = "/switch-controller.security-policy/802-1X/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/switch-controller.security-policy/802-1X"
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
            >>> schema = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.switch_controller_security_policy_x802_1x.get_schema(format="json-schema")
        
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
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = None,
        user_group: str | list[str] | list[dict[str, Any]] | None = None,
        mac_auth_bypass: Literal["disable", "enable"] | None = None,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = None,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = None,
        open_auth: Literal["disable", "enable"] | None = None,
        eap_passthru: Literal["disable", "enable"] | None = None,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = None,
        guest_vlan: Literal["disable", "enable"] | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: Literal["disable", "enable"] | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: Literal["disable", "enable"] | None = None,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = None,
        policy_type: Literal["802.1X"] | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: Literal["disable", "enable"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing switch_controller/security_policy/x802_1x object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Policy name.
            security_mode: Port or MAC based 802.1X security mode.
            user_group: Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            mac_auth_bypass: Enable/disable MAB for this policy.
            auth_order: Configure authentication order.
            auth_priority: Configure authentication priority.
            open_auth: Enable/disable open authentication for this policy.
            eap_passthru: Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass through ports for more flexible authentication.
            eap_auto_untagged_vlans: Enable/disable automatic inclusion of untagged VLANs.
            guest_vlan: Enable the guest VLAN feature to allow limited access to non-802.1X-compliant clients.
            guest_vlan_id: Guest VLAN name.
            guest_auth_delay: Guest authentication delay (1 - 900  sec, default = 30).
            auth_fail_vlan: Enable to allow limited access to clients that cannot authenticate.
            auth_fail_vlan_id: VLAN ID on which authentication failed.
            framevid_apply: Enable/disable the capability to apply the EAP/MAB frame VLAN to the port native VLAN.
            radius_timeout_overwrite: Enable to override the global RADIUS session timeout.
            policy_type: Policy type.
            authserver_timeout_period: Authentication server timeout period (3 - 15 sec, default = 3).
            authserver_timeout_vlan: Enable/disable the authentication server timeout VLAN to allow limited access when RADIUS is unavailable.
            authserver_timeout_vlanid: Authentication server timeout VLAN name.
            authserver_timeout_tagged: Configure timeout option for the tagged VLAN which allows limited access when the authentication server is unavailable.
            authserver_timeout_tagged_vlanid: Tagged VLAN name for which the timeout option is applied to (only one VLAN ID).
            dacl: Enable/disable dynamic access control list on this interface.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if user_group is not None:
            user_group = normalize_table_field(
                user_group,
                mkey="name",
                required_fields=['name'],
                field_name="user_group",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            security_mode=security_mode,
            user_group=user_group,
            mac_auth_bypass=mac_auth_bypass,
            auth_order=auth_order,
            auth_priority=auth_priority,
            open_auth=open_auth,
            eap_passthru=eap_passthru,
            eap_auto_untagged_vlans=eap_auto_untagged_vlans,
            guest_vlan=guest_vlan,
            guest_vlan_id=guest_vlan_id,
            guest_auth_delay=guest_auth_delay,
            auth_fail_vlan=auth_fail_vlan,
            auth_fail_vlan_id=auth_fail_vlan_id,
            framevid_apply=framevid_apply,
            radius_timeout_overwrite=radius_timeout_overwrite,
            policy_type=policy_type,
            authserver_timeout_period=authserver_timeout_period,
            authserver_timeout_vlan=authserver_timeout_vlan,
            authserver_timeout_vlanid=authserver_timeout_vlanid,
            authserver_timeout_tagged=authserver_timeout_tagged,
            authserver_timeout_tagged_vlanid=authserver_timeout_tagged_vlanid,
            dacl=dacl,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.x802_1x import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/security_policy/x802_1x",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/switch-controller.security-policy/802-1X/" + str(name_value)

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
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = None,
        user_group: str | list[str] | list[dict[str, Any]] | None = None,
        mac_auth_bypass: Literal["disable", "enable"] | None = None,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = None,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = None,
        open_auth: Literal["disable", "enable"] | None = None,
        eap_passthru: Literal["disable", "enable"] | None = None,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = None,
        guest_vlan: Literal["disable", "enable"] | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: Literal["disable", "enable"] | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: Literal["disable", "enable"] | None = None,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = None,
        policy_type: Literal["802.1X"] | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: Literal["disable", "enable"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new switch_controller/security_policy/x802_1x object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Policy name.
            security_mode: Port or MAC based 802.1X security mode.
            user_group: Name of user-group to assign to this MAC Authentication Bypass (MAB) policy.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            mac_auth_bypass: Enable/disable MAB for this policy.
            auth_order: Configure authentication order.
            auth_priority: Configure authentication priority.
            open_auth: Enable/disable open authentication for this policy.
            eap_passthru: Enable/disable EAP pass-through mode, allowing protocols (such as LLDP) to pass through ports for more flexible authentication.
            eap_auto_untagged_vlans: Enable/disable automatic inclusion of untagged VLANs.
            guest_vlan: Enable the guest VLAN feature to allow limited access to non-802.1X-compliant clients.
            guest_vlan_id: Guest VLAN name.
            guest_auth_delay: Guest authentication delay (1 - 900  sec, default = 30).
            auth_fail_vlan: Enable to allow limited access to clients that cannot authenticate.
            auth_fail_vlan_id: VLAN ID on which authentication failed.
            framevid_apply: Enable/disable the capability to apply the EAP/MAB frame VLAN to the port native VLAN.
            radius_timeout_overwrite: Enable to override the global RADIUS session timeout.
            policy_type: Policy type.
            authserver_timeout_period: Authentication server timeout period (3 - 15 sec, default = 3).
            authserver_timeout_vlan: Enable/disable the authentication server timeout VLAN to allow limited access when RADIUS is unavailable.
            authserver_timeout_vlanid: Authentication server timeout VLAN name.
            authserver_timeout_tagged: Configure timeout option for the tagged VLAN which allows limited access when the authentication server is unavailable.
            authserver_timeout_tagged_vlanid: Tagged VLAN name for which the timeout option is applied to (only one VLAN ID).
            dacl: Enable/disable dynamic access control list on this interface.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = X8021x.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(X8021x.required_fields()) }}
            
            Use X8021x.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if user_group is not None:
            user_group = normalize_table_field(
                user_group,
                mkey="name",
                required_fields=['name'],
                field_name="user_group",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            security_mode=security_mode,
            user_group=user_group,
            mac_auth_bypass=mac_auth_bypass,
            auth_order=auth_order,
            auth_priority=auth_priority,
            open_auth=open_auth,
            eap_passthru=eap_passthru,
            eap_auto_untagged_vlans=eap_auto_untagged_vlans,
            guest_vlan=guest_vlan,
            guest_vlan_id=guest_vlan_id,
            guest_auth_delay=guest_auth_delay,
            auth_fail_vlan=auth_fail_vlan,
            auth_fail_vlan_id=auth_fail_vlan_id,
            framevid_apply=framevid_apply,
            radius_timeout_overwrite=radius_timeout_overwrite,
            policy_type=policy_type,
            authserver_timeout_period=authserver_timeout_period,
            authserver_timeout_vlan=authserver_timeout_vlan,
            authserver_timeout_vlanid=authserver_timeout_vlanid,
            authserver_timeout_tagged=authserver_timeout_tagged,
            authserver_timeout_tagged_vlanid=authserver_timeout_tagged_vlanid,
            dacl=dacl,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.x802_1x import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/security_policy/x802_1x",
            )

        endpoint = "/switch-controller.security-policy/802-1X"
        
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
        Delete switch_controller/security_policy/x802_1x object.

        Configure 802.1x MAC Authentication Bypass (MAB) policies.

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
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/switch-controller.security-policy/802-1X/" + str(name)

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
        Check if switch_controller/security_policy/x802_1x object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.switch_controller_security_policy_x802_1x.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.switch_controller_security_policy_x802_1x.exists(name=1):
            ...     fgt.api.cmdb.switch_controller_security_policy_x802_1x.delete(name=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                name=name,
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
        name: str | None = None,
        security_mode: Literal["802.1X", "802.1X-mac-based"] | None = None,
        user_group: str | list[str] | list[dict[str, Any]] | None = None,
        mac_auth_bypass: Literal["disable", "enable"] | None = None,
        auth_order: Literal["dot1x-mab", "mab-dot1x", "mab"] | None = None,
        auth_priority: Literal["legacy", "dot1x-mab", "mab-dot1x"] | None = None,
        open_auth: Literal["disable", "enable"] | None = None,
        eap_passthru: Literal["disable", "enable"] | None = None,
        eap_auto_untagged_vlans: Literal["disable", "enable"] | None = None,
        guest_vlan: Literal["disable", "enable"] | None = None,
        guest_vlan_id: str | None = None,
        guest_auth_delay: int | None = None,
        auth_fail_vlan: Literal["disable", "enable"] | None = None,
        auth_fail_vlan_id: str | None = None,
        framevid_apply: Literal["disable", "enable"] | None = None,
        radius_timeout_overwrite: Literal["disable", "enable"] | None = None,
        policy_type: Literal["802.1X"] | None = None,
        authserver_timeout_period: int | None = None,
        authserver_timeout_vlan: Literal["disable", "enable"] | None = None,
        authserver_timeout_vlanid: str | None = None,
        authserver_timeout_tagged: Literal["disable", "lldp-voice", "static"] | None = None,
        authserver_timeout_tagged_vlanid: str | None = None,
        dacl: Literal["disable", "enable"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update switch_controller/security_policy/x802_1x object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            security_mode: Field security-mode
            user_group: Field user-group
            mac_auth_bypass: Field mac-auth-bypass
            auth_order: Field auth-order
            auth_priority: Field auth-priority
            open_auth: Field open-auth
            eap_passthru: Field eap-passthru
            eap_auto_untagged_vlans: Field eap-auto-untagged-vlans
            guest_vlan: Field guest-vlan
            guest_vlan_id: Field guest-vlan-id
            guest_auth_delay: Field guest-auth-delay
            auth_fail_vlan: Field auth-fail-vlan
            auth_fail_vlan_id: Field auth-fail-vlan-id
            framevid_apply: Field framevid-apply
            radius_timeout_overwrite: Field radius-timeout-overwrite
            policy_type: Field policy-type
            authserver_timeout_period: Field authserver-timeout-period
            authserver_timeout_vlan: Field authserver-timeout-vlan
            authserver_timeout_vlanid: Field authserver-timeout-vlanid
            authserver_timeout_tagged: Field authserver-timeout-tagged
            authserver_timeout_tagged_vlanid: Field authserver-timeout-tagged-vlanid
            dacl: Field dacl
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_security_policy_x802_1x.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.switch_controller_security_policy_x802_1x.set(payload_dict=obj_data)
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
            security_mode=security_mode,
            user_group=user_group,
            mac_auth_bypass=mac_auth_bypass,
            auth_order=auth_order,
            auth_priority=auth_priority,
            open_auth=open_auth,
            eap_passthru=eap_passthru,
            eap_auto_untagged_vlans=eap_auto_untagged_vlans,
            guest_vlan=guest_vlan,
            guest_vlan_id=guest_vlan_id,
            guest_auth_delay=guest_auth_delay,
            auth_fail_vlan=auth_fail_vlan,
            auth_fail_vlan_id=auth_fail_vlan_id,
            framevid_apply=framevid_apply,
            radius_timeout_overwrite=radius_timeout_overwrite,
            policy_type=policy_type,
            authserver_timeout_period=authserver_timeout_period,
            authserver_timeout_vlan=authserver_timeout_vlan,
            authserver_timeout_vlanid=authserver_timeout_vlanid,
            authserver_timeout_tagged=authserver_timeout_tagged,
            authserver_timeout_tagged_vlanid=authserver_timeout_tagged_vlanid,
            dacl=dacl,
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
        Move switch_controller/security_policy/x802_1x object to a new position.
        
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
            >>> fgt.api.cmdb.switch_controller_security_policy_x802_1x.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/switch-controller.security-policy/802-1X",
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
        Clone switch_controller/security_policy/x802_1x object.
        
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
            >>> fgt.api.cmdb.switch_controller_security_policy_x802_1x.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/switch-controller.security-policy/802-1X",
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
        Check if switch_controller/security_policy/x802_1x object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.switch_controller_security_policy_x802_1x.exists(name=1):
            ...     fgt.api.cmdb.switch_controller_security_policy_x802_1x.post(payload_dict=data)
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

