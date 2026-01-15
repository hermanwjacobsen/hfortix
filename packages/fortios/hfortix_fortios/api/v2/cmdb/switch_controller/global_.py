"""
FortiOS CMDB - Switch_controller global_

Configuration endpoint for managing cmdb switch_controller/global_ objects.

API Endpoints:
    GET    /cmdb/switch_controller/global_
    POST   /cmdb/switch_controller/global_
    PUT    /cmdb/switch_controller/global_/{identifier}
    DELETE /cmdb/switch_controller/global_/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller_global_.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.switch_controller_global_.post(
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

class Global(CRUDEndpoint, MetadataMixin):
    """Global Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "global_"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "disable_discovery": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "custom_command": {
            "mkey": "command-entry",
            "required_fields": ['command-name'],
            "example": "[{'command-name': 'value'}]",
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
        """Initialize Global endpoint."""
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
        Retrieve switch_controller/global_ configuration.

        Configure FortiSwitch global settings.

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
            >>> # Get all switch_controller/global_ objects
            >>> result = fgt.api.cmdb.switch_controller_global_.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.switch_controller_global_.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.switch_controller_global_.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.switch_controller_global_.get_schema()

        See Also:
            - post(): Create new switch_controller/global_ object
            - put(): Update existing switch_controller/global_ object
            - delete(): Remove switch_controller/global_ object
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
            endpoint = f"/switch-controller/global/{name}"
            unwrap_single = True
        else:
            endpoint = "/switch-controller/global"
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
            >>> schema = fgt.api.cmdb.switch_controller_global_.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.switch_controller_global_.get_schema(format="json-schema")
        
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
        mac_aging_interval: int | None = None,
        https_image_push: Literal["enable", "disable"] | None = None,
        vlan_all_mode: Literal["all", "defined"] | None = None,
        vlan_optimization: Literal["prune", "configured", "none"] | None = None,
        vlan_identity: Literal["description", "name"] | None = None,
        disable_discovery: str | list[str] | list[dict[str, Any]] | None = None,
        mac_retention_period: int | None = None,
        default_virtual_switch_vlan: str | None = None,
        dhcp_server_access_list: Literal["enable", "disable"] | None = None,
        dhcp_option82_format: Literal["ascii", "legacy"] | None = None,
        dhcp_option82_circuit_id: Literal["intfname", "vlan", "hostname", "mode", "description"] | list[str] | None = None,
        dhcp_option82_remote_id: Literal["mac", "hostname", "ip"] | list[str] | None = None,
        dhcp_snoop_client_req: Literal["drop-untrusted", "forward-untrusted"] | None = None,
        dhcp_snoop_client_db_exp: int | None = None,
        dhcp_snoop_db_per_port_learn_limit: int | None = None,
        log_mac_limit_violations: Literal["enable", "disable"] | None = None,
        mac_violation_timer: int | None = None,
        sn_dns_resolution: Literal["enable", "disable"] | None = None,
        mac_event_logging: Literal["enable", "disable"] | None = None,
        bounce_quarantined_link: Literal["disable", "enable"] | None = None,
        quarantine_mode: Literal["by-vlan", "by-redirect"] | None = None,
        update_user_device: Literal["mac-cache", "lldp", "dhcp-snooping", "l2-db", "l3-db"] | list[str] | None = None,
        custom_command: str | list[str] | list[dict[str, Any]] | None = None,
        fips_enforce: Literal["disable", "enable"] | None = None,
        firmware_provision_on_authorization: Literal["enable", "disable"] | None = None,
        switch_on_deauth: Literal["no-op", "factory-reset"] | None = None,
        firewall_auth_user_hold_period: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing switch_controller/global_ object.

        Configure FortiSwitch global settings.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            mac_aging_interval: Time after which an inactive MAC is aged out (10 - 1000000 sec, default = 300, 0 = disable).
            https_image_push: Enable/disable image push to FortiSwitch using HTTPS.
            vlan_all_mode: VLAN configuration mode, user-defined-vlans or all-possible-vlans.
            vlan_optimization: FortiLink VLAN optimization.
            vlan_identity: Identity of the VLAN. Commonly used for RADIUS Tunnel-Private-Group-Id.
            disable_discovery: Prevent this FortiSwitch from discovering.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            mac_retention_period: Time in hours after which an inactive MAC is removed from client DB (0 = aged out based on mac-aging-interval).
            default_virtual_switch_vlan: Default VLAN for ports when added to the virtual-switch.
            dhcp_server_access_list: Enable/disable DHCP snooping server access list.
            dhcp_option82_format: DHCP option-82 format string.
            dhcp_option82_circuit_id: List the parameters to be included to inform about client identification.
            dhcp_option82_remote_id: List the parameters to be included to inform about client identification.
            dhcp_snoop_client_req: Client DHCP packet broadcast mode.
            dhcp_snoop_client_db_exp: Expiry time for DHCP snooping server database entries (300 - 259200 sec, default = 86400 sec).
            dhcp_snoop_db_per_port_learn_limit: Per Interface dhcp-server entries learn limit (0 - 1024, default = 64).
            log_mac_limit_violations: Enable/disable logs for Learning Limit Violations.
            mac_violation_timer: Set timeout for Learning Limit Violations (0 = disabled).
            sn_dns_resolution: Enable/disable DNS resolution of the FortiSwitch unit's IP address with switch name.
            mac_event_logging: Enable/disable MAC address event logging.
            bounce_quarantined_link: Enable/disable bouncing (administratively bring the link down, up) of a switch port where a quarantined device was seen last. Helps to re-initiate the DHCP process for a device.
            quarantine_mode: Quarantine mode.
            update_user_device: Control which sources update the device user list.
            custom_command: List of custom commands to be pushed to all FortiSwitches in the VDOM.
                Default format: [{'command-name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'command-entry': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'command-entry': 'val1'}, ...]
                  - List of dicts: [{'command-name': 'value'}] (recommended)
            fips_enforce: Enable/disable enforcement of FIPS on managed FortiSwitch devices.
            firmware_provision_on_authorization: Enable/disable automatic provisioning of latest firmware on authorization.
            switch_on_deauth: No-operation/Factory-reset the managed FortiSwitch on deauthorization.
            firewall_auth_user_hold_period: Time period in minutes to hold firewall authenticated MAC users (5 - 1440, default = 5, disable = 0).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.switch_controller_global_.put(
            ...     name="existing-object",
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": "existing-object",
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.switch_controller_global_.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if disable_discovery is not None:
            disable_discovery = normalize_table_field(
                disable_discovery,
                mkey="name",
                required_fields=['name'],
                field_name="disable_discovery",
                example="[{'name': 'value'}]",
            )
        if custom_command is not None:
            custom_command = normalize_table_field(
                custom_command,
                mkey="command-entry",
                required_fields=['command-name'],
                field_name="custom_command",
                example="[{'command-name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            mac_aging_interval=mac_aging_interval,
            https_image_push=https_image_push,
            vlan_all_mode=vlan_all_mode,
            vlan_optimization=vlan_optimization,
            vlan_identity=vlan_identity,
            disable_discovery=disable_discovery,
            mac_retention_period=mac_retention_period,
            default_virtual_switch_vlan=default_virtual_switch_vlan,
            dhcp_server_access_list=dhcp_server_access_list,
            dhcp_option82_format=dhcp_option82_format,
            dhcp_option82_circuit_id=dhcp_option82_circuit_id,
            dhcp_option82_remote_id=dhcp_option82_remote_id,
            dhcp_snoop_client_req=dhcp_snoop_client_req,
            dhcp_snoop_client_db_exp=dhcp_snoop_client_db_exp,
            dhcp_snoop_db_per_port_learn_limit=dhcp_snoop_db_per_port_learn_limit,
            log_mac_limit_violations=log_mac_limit_violations,
            mac_violation_timer=mac_violation_timer,
            sn_dns_resolution=sn_dns_resolution,
            mac_event_logging=mac_event_logging,
            bounce_quarantined_link=bounce_quarantined_link,
            quarantine_mode=quarantine_mode,
            update_user_device=update_user_device,
            custom_command=custom_command,
            fips_enforce=fips_enforce,
            firmware_provision_on_authorization=firmware_provision_on_authorization,
            switch_on_deauth=switch_on_deauth,
            firewall_auth_user_hold_period=firewall_auth_user_hold_period,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.global_ import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/switch_controller/global_",
            )
        
        # Singleton endpoint - no identifier needed
        endpoint = "/switch-controller/global"

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
        Move switch_controller/global_ object to a new position.
        
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
            >>> fgt.api.cmdb.switch_controller_global_.move(
            ...     name="object1",
            ...     action="before",
            ...     reference_name="object2"
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/switch-controller/global",
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
        Clone switch_controller/global_ object.
        
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
            >>> fgt.api.cmdb.switch_controller_global_.clone(
            ...     name="template",
            ...     new_name="new-from-template"
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/switch-controller/global",
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
        Check if switch_controller/global_ object exists.
        
        Args:
            name: Name to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.switch_controller_global_.exists(name="myobj"):
            ...     fgt.api.cmdb.switch_controller_global_.post(payload_dict=data)
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

