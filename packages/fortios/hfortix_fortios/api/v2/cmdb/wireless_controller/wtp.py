"""
FortiOS CMDB - Wireless_controller wtp

Configuration endpoint for managing cmdb wireless_controller/wtp objects.

API Endpoints:
    GET    /cmdb/wireless_controller/wtp
    POST   /cmdb/wireless_controller/wtp
    PUT    /cmdb/wireless_controller/wtp/{identifier}
    DELETE /cmdb/wireless_controller/wtp/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_wtp.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.wireless_controller_wtp.post(
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

class Wtp(CRUDEndpoint, MetadataMixin):
    """Wtp Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "wtp"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "split_tunneling_acl": {
            "mkey": "id",
            "required_fields": ['dest-ip'],
            "example": "[{'dest-ip': 'value'}]",
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
        """Initialize Wtp endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        wtp_id: str | None = None,
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
        Retrieve wireless_controller/wtp configuration.

        Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

        Args:
            wtp_id: String identifier to retrieve specific object.
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
            >>> # Get all wireless_controller/wtp objects
            >>> result = fgt.api.cmdb.wireless_controller_wtp.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/wtp by wtp-id
            >>> result = fgt.api.cmdb.wireless_controller_wtp.get(wtp_id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_wtp.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.wireless_controller_wtp.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.wireless_controller_wtp.get_schema()

        See Also:
            - post(): Create new wireless_controller/wtp object
            - put(): Update existing wireless_controller/wtp object
            - delete(): Remove wireless_controller/wtp object
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
        
        if wtp_id:
            endpoint = "/wireless-controller/wtp/" + str(wtp_id)
            unwrap_single = True
        else:
            endpoint = "/wireless-controller/wtp"
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
            >>> schema = fgt.api.cmdb.wireless_controller_wtp.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.wireless_controller_wtp.get_schema(format="json-schema")
        
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
        wtp_id: str | None = None,
        index: int | None = None,
        uuid: str | None = None,
        admin: Literal["discovered", "disable", "enable"] | None = None,
        name: str | None = None,
        location: str | None = None,
        comment: str | None = None,
        region: str | None = None,
        region_x: str | None = None,
        region_y: str | None = None,
        firmware_provision: str | None = None,
        firmware_provision_latest: Literal["disable", "once"] | None = None,
        wtp_profile: str | None = None,
        apcfg_profile: str | None = None,
        bonjour_profile: str | None = None,
        ble_major_id: int | None = None,
        ble_minor_id: int | None = None,
        override_led_state: Literal["enable", "disable"] | None = None,
        led_state: Literal["enable", "disable"] | None = None,
        override_wan_port_mode: Literal["enable", "disable"] | None = None,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = None,
        override_ip_fragment: Literal["enable", "disable"] | None = None,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        override_split_tunnel: Literal["enable", "disable"] | None = None,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = None,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = None,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = None,
        override_lan: Literal["enable", "disable"] | None = None,
        lan: str | None = None,
        override_allowaccess: Literal["enable", "disable"] | None = None,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = None,
        override_login_passwd_change: Literal["enable", "disable"] | None = None,
        login_passwd_change: Literal["yes", "default", "no"] | None = None,
        login_passwd: Any | None = None,
        override_default_mesh_root: Literal["enable", "disable"] | None = None,
        default_mesh_root: Literal["enable", "disable"] | None = None,
        radio_1: str | None = None,
        radio_2: str | None = None,
        radio_3: str | None = None,
        radio_4: str | None = None,
        image_download: Literal["enable", "disable"] | None = None,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        coordinate_latitude: str | None = None,
        coordinate_longitude: str | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing wireless_controller/wtp object.

        Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

        Args:
            payload_dict: Object data as dict. Must include wtp-id (primary key).
            wtp_id: WTP ID.
            index: Index (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            admin: Configure how the FortiGate operating as a wireless controller discovers and manages this WTP, AP or FortiAP.
            name: WTP, AP or FortiAP configuration name.
            location: Field for describing the physical location of the WTP, AP or FortiAP.
            comment: Comment.
            region: Region name WTP is associated with.
            region_x: Relative horizontal region coordinate (between 0 and 1).
            region_y: Relative vertical region coordinate (between 0 and 1).
            firmware_provision: Firmware version to provision to this FortiAP on bootup (major.minor.build, i.e. 6.2.1234).
            firmware_provision_latest: Enable/disable one-time automatic provisioning of the latest firmware version.
            wtp_profile: WTP profile name to apply to this WTP, AP or FortiAP.
            apcfg_profile: AP local configuration profile name.
            bonjour_profile: Bonjour profile name.
            ble_major_id: Override BLE Major ID.
            ble_minor_id: Override BLE Minor ID.
            override_led_state: Enable to override the profile LED state setting for this FortiAP. You must enable this option to use the led-state command to turn off the FortiAP's LEDs.
            led_state: Enable to allow the FortiAPs LEDs to light. Disable to keep the LEDs off. You may want to keep the LEDs off so they are not distracting in low light areas etc.
            override_wan_port_mode: Enable/disable overriding the wan-port-mode in the WTP profile.
            wan_port_mode: Enable/disable using the FortiAP WAN port as a LAN port.
            override_ip_fragment: Enable/disable overriding the WTP profile IP fragment prevention setting.
            ip_fragment_preventing: Method(s) by which IP fragmentation is prevented for control and data packets through CAPWAP tunnel (default = tcp-mss-adjust).
            tun_mtu_uplink: The maximum transmission unit (MTU) of uplink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; default = 0).
            tun_mtu_downlink: The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; default = 0).
            override_split_tunnel: Enable/disable overriding the WTP profile split tunneling setting.
            split_tunneling_acl_path: Split tunneling ACL path is local/tunnel.
            split_tunneling_acl_local_ap_subnet: Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable).
            split_tunneling_acl: Split tunneling ACL filter list.
                Default format: [{'dest-ip': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'dest-ip': 'value'}] (recommended)
            override_lan: Enable to override the WTP profile LAN port setting.
            lan: WTP LAN port mapping.
            override_allowaccess: Enable to override the WTP profile management access configuration.
            allowaccess: Control management access to the managed WTP, FortiAP, or AP. Separate entries with a space.
            override_login_passwd_change: Enable to override the WTP profile login-password (administrator password) setting.
            login_passwd_change: Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no).
            login_passwd: Set the managed WTP, FortiAP, or AP's administrator password.
            override_default_mesh_root: Enable to override the WTP profile default mesh root SSID setting.
            default_mesh_root: Configure default mesh root SSID when it is not included by radio's SSID configuration.
            radio_1: Configuration options for radio 1.
            radio_2: Configuration options for radio 2.
            radio_3: Configuration options for radio 3.
            radio_4: Configuration options for radio 4.
            image_download: Enable/disable WTP image download.
            mesh_bridge_enable: Enable/disable mesh Ethernet bridge when WTP is configured as a mesh branch/leaf AP.
            purdue_level: Purdue Level of this WTP.
            coordinate_latitude: WTP latitude coordinate.
            coordinate_longitude: WTP longitude coordinate.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If wtp-id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_wtp.put(
            ...     wtp_id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "wtp-id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_wtp.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if split_tunneling_acl is not None:
            split_tunneling_acl = normalize_table_field(
                split_tunneling_acl,
                mkey="id",
                required_fields=['dest-ip'],
                field_name="split_tunneling_acl",
                example="[{'dest-ip': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            wtp_id=wtp_id,
            index=index,
            uuid=uuid,
            admin=admin,
            name=name,
            location=location,
            comment=comment,
            region=region,
            region_x=region_x,
            region_y=region_y,
            firmware_provision=firmware_provision,
            firmware_provision_latest=firmware_provision_latest,
            wtp_profile=wtp_profile,
            apcfg_profile=apcfg_profile,
            bonjour_profile=bonjour_profile,
            ble_major_id=ble_major_id,
            ble_minor_id=ble_minor_id,
            override_led_state=override_led_state,
            led_state=led_state,
            override_wan_port_mode=override_wan_port_mode,
            wan_port_mode=wan_port_mode,
            override_ip_fragment=override_ip_fragment,
            ip_fragment_preventing=ip_fragment_preventing,
            tun_mtu_uplink=tun_mtu_uplink,
            tun_mtu_downlink=tun_mtu_downlink,
            override_split_tunnel=override_split_tunnel,
            split_tunneling_acl_path=split_tunneling_acl_path,
            split_tunneling_acl_local_ap_subnet=split_tunneling_acl_local_ap_subnet,
            split_tunneling_acl=split_tunneling_acl,
            override_lan=override_lan,
            lan=lan,
            override_allowaccess=override_allowaccess,
            allowaccess=allowaccess,
            override_login_passwd_change=override_login_passwd_change,
            login_passwd_change=login_passwd_change,
            login_passwd=login_passwd,
            override_default_mesh_root=override_default_mesh_root,
            default_mesh_root=default_mesh_root,
            radio_1=radio_1,
            radio_2=radio_2,
            radio_3=radio_3,
            radio_4=radio_4,
            image_download=image_download,
            mesh_bridge_enable=mesh_bridge_enable,
            purdue_level=purdue_level,
            coordinate_latitude=coordinate_latitude,
            coordinate_longitude=coordinate_longitude,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.wtp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wtp",
            )
        
        wtp_id_value = payload_data.get("wtp-id")
        if not wtp_id_value:
            raise ValueError("wtp-id is required for PUT")
        endpoint = "/wireless-controller/wtp/" + str(wtp_id_value)

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
        wtp_id: str | None = None,
        index: int | None = None,
        uuid: str | None = None,
        admin: Literal["discovered", "disable", "enable"] | None = None,
        name: str | None = None,
        location: str | None = None,
        comment: str | None = None,
        region: str | None = None,
        region_x: str | None = None,
        region_y: str | None = None,
        firmware_provision: str | None = None,
        firmware_provision_latest: Literal["disable", "once"] | None = None,
        wtp_profile: str | None = None,
        apcfg_profile: str | None = None,
        bonjour_profile: str | None = None,
        ble_major_id: int | None = None,
        ble_minor_id: int | None = None,
        override_led_state: Literal["enable", "disable"] | None = None,
        led_state: Literal["enable", "disable"] | None = None,
        override_wan_port_mode: Literal["enable", "disable"] | None = None,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = None,
        override_ip_fragment: Literal["enable", "disable"] | None = None,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        override_split_tunnel: Literal["enable", "disable"] | None = None,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = None,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = None,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = None,
        override_lan: Literal["enable", "disable"] | None = None,
        lan: str | None = None,
        override_allowaccess: Literal["enable", "disable"] | None = None,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | None = None,
        override_login_passwd_change: Literal["enable", "disable"] | None = None,
        login_passwd_change: Literal["yes", "default", "no"] | None = None,
        login_passwd: Any | None = None,
        override_default_mesh_root: Literal["enable", "disable"] | None = None,
        default_mesh_root: Literal["enable", "disable"] | None = None,
        radio_1: str | None = None,
        radio_2: str | None = None,
        radio_3: str | None = None,
        radio_4: str | None = None,
        image_download: Literal["enable", "disable"] | None = None,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        coordinate_latitude: str | None = None,
        coordinate_longitude: str | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new wireless_controller/wtp object.

        Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            wtp_id: WTP ID.
            index: Index (0 - 4294967295).
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
            admin: Configure how the FortiGate operating as a wireless controller discovers and manages this WTP, AP or FortiAP.
            name: WTP, AP or FortiAP configuration name.
            location: Field for describing the physical location of the WTP, AP or FortiAP.
            comment: Comment.
            region: Region name WTP is associated with.
            region_x: Relative horizontal region coordinate (between 0 and 1).
            region_y: Relative vertical region coordinate (between 0 and 1).
            firmware_provision: Firmware version to provision to this FortiAP on bootup (major.minor.build, i.e. 6.2.1234).
            firmware_provision_latest: Enable/disable one-time automatic provisioning of the latest firmware version.
            wtp_profile: WTP profile name to apply to this WTP, AP or FortiAP.
            apcfg_profile: AP local configuration profile name.
            bonjour_profile: Bonjour profile name.
            ble_major_id: Override BLE Major ID.
            ble_minor_id: Override BLE Minor ID.
            override_led_state: Enable to override the profile LED state setting for this FortiAP. You must enable this option to use the led-state command to turn off the FortiAP's LEDs.
            led_state: Enable to allow the FortiAPs LEDs to light. Disable to keep the LEDs off. You may want to keep the LEDs off so they are not distracting in low light areas etc.
            override_wan_port_mode: Enable/disable overriding the wan-port-mode in the WTP profile.
            wan_port_mode: Enable/disable using the FortiAP WAN port as a LAN port.
            override_ip_fragment: Enable/disable overriding the WTP profile IP fragment prevention setting.
            ip_fragment_preventing: Method(s) by which IP fragmentation is prevented for control and data packets through CAPWAP tunnel (default = tcp-mss-adjust).
            tun_mtu_uplink: The maximum transmission unit (MTU) of uplink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; default = 0).
            tun_mtu_downlink: The MTU of downlink CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of FortiAP; default = 0).
            override_split_tunnel: Enable/disable overriding the WTP profile split tunneling setting.
            split_tunneling_acl_path: Split tunneling ACL path is local/tunnel.
            split_tunneling_acl_local_ap_subnet: Enable/disable automatically adding local subnetwork of FortiAP to split-tunneling ACL (default = disable).
            split_tunneling_acl: Split tunneling ACL filter list.
                Default format: [{'dest-ip': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'dest-ip': 'value'}] (recommended)
            override_lan: Enable to override the WTP profile LAN port setting.
            lan: WTP LAN port mapping.
            override_allowaccess: Enable to override the WTP profile management access configuration.
            allowaccess: Control management access to the managed WTP, FortiAP, or AP. Separate entries with a space.
            override_login_passwd_change: Enable to override the WTP profile login-password (administrator password) setting.
            login_passwd_change: Change or reset the administrator password of a managed WTP, FortiAP or AP (yes, default, or no, default = no).
            login_passwd: Set the managed WTP, FortiAP, or AP's administrator password.
            override_default_mesh_root: Enable to override the WTP profile default mesh root SSID setting.
            default_mesh_root: Configure default mesh root SSID when it is not included by radio's SSID configuration.
            radio_1: Configuration options for radio 1.
            radio_2: Configuration options for radio 2.
            radio_3: Configuration options for radio 3.
            radio_4: Configuration options for radio 4.
            image_download: Enable/disable WTP image download.
            mesh_bridge_enable: Enable/disable mesh Ethernet bridge when WTP is configured as a mesh branch/leaf AP.
            purdue_level: Purdue Level of this WTP.
            coordinate_latitude: WTP latitude coordinate.
            coordinate_longitude: WTP longitude coordinate.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_wtp.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created wtp-id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Wtp.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_wtp.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Wtp.required_fields()) }}
            
            Use Wtp.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if split_tunneling_acl is not None:
            split_tunneling_acl = normalize_table_field(
                split_tunneling_acl,
                mkey="id",
                required_fields=['dest-ip'],
                field_name="split_tunneling_acl",
                example="[{'dest-ip': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            wtp_id=wtp_id,
            index=index,
            uuid=uuid,
            admin=admin,
            name=name,
            location=location,
            comment=comment,
            region=region,
            region_x=region_x,
            region_y=region_y,
            firmware_provision=firmware_provision,
            firmware_provision_latest=firmware_provision_latest,
            wtp_profile=wtp_profile,
            apcfg_profile=apcfg_profile,
            bonjour_profile=bonjour_profile,
            ble_major_id=ble_major_id,
            ble_minor_id=ble_minor_id,
            override_led_state=override_led_state,
            led_state=led_state,
            override_wan_port_mode=override_wan_port_mode,
            wan_port_mode=wan_port_mode,
            override_ip_fragment=override_ip_fragment,
            ip_fragment_preventing=ip_fragment_preventing,
            tun_mtu_uplink=tun_mtu_uplink,
            tun_mtu_downlink=tun_mtu_downlink,
            override_split_tunnel=override_split_tunnel,
            split_tunneling_acl_path=split_tunneling_acl_path,
            split_tunneling_acl_local_ap_subnet=split_tunneling_acl_local_ap_subnet,
            split_tunneling_acl=split_tunneling_acl,
            override_lan=override_lan,
            lan=lan,
            override_allowaccess=override_allowaccess,
            allowaccess=allowaccess,
            override_login_passwd_change=override_login_passwd_change,
            login_passwd_change=login_passwd_change,
            login_passwd=login_passwd,
            override_default_mesh_root=override_default_mesh_root,
            default_mesh_root=default_mesh_root,
            radio_1=radio_1,
            radio_2=radio_2,
            radio_3=radio_3,
            radio_4=radio_4,
            image_download=image_download,
            mesh_bridge_enable=mesh_bridge_enable,
            purdue_level=purdue_level,
            coordinate_latitude=coordinate_latitude,
            coordinate_longitude=coordinate_longitude,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.wtp import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wtp",
            )

        endpoint = "/wireless-controller/wtp"
        
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
        wtp_id: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete wireless_controller/wtp object.

        Configure Wireless Termination Points (WTPs), that is, FortiAPs or APs to be managed by FortiGate.

        Args:
            wtp_id: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If wtp-id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.wireless_controller_wtp.delete(wtp_id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not wtp_id:
            raise ValueError("wtp-id is required for DELETE")
        endpoint = "/wireless-controller/wtp/" + str(wtp_id)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        wtp_id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if wireless_controller/wtp object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            wtp_id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_wtp.exists(wtp_id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_wtp.exists(wtp_id=1):
            ...     fgt.api.cmdb.wireless_controller_wtp.delete(wtp_id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                wtp_id=wtp_id,
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
        wtp_id: str | None = None,
        index: int | None = None,
        uuid: str | None = None,
        admin: Literal["discovered", "disable", "enable"] | None = None,
        name: str | None = None,
        location: str | None = None,
        comment: str | None = None,
        region: str | None = None,
        region_x: str | None = None,
        region_y: str | None = None,
        firmware_provision: str | None = None,
        firmware_provision_latest: Literal["disable", "once"] | None = None,
        wtp_profile: str | None = None,
        apcfg_profile: str | None = None,
        bonjour_profile: str | None = None,
        ble_major_id: int | None = None,
        ble_minor_id: int | None = None,
        override_led_state: Literal["enable", "disable"] | None = None,
        led_state: Literal["enable", "disable"] | None = None,
        override_wan_port_mode: Literal["enable", "disable"] | None = None,
        wan_port_mode: Literal["wan-lan", "wan-only"] | None = None,
        override_ip_fragment: Literal["enable", "disable"] | None = None,
        ip_fragment_preventing: Literal["tcp-mss-adjust", "icmp-unreachable"] | list[str] | list[dict[str, Any]] | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        override_split_tunnel: Literal["enable", "disable"] | None = None,
        split_tunneling_acl_path: Literal["tunnel", "local"] | None = None,
        split_tunneling_acl_local_ap_subnet: Literal["enable", "disable"] | None = None,
        split_tunneling_acl: str | list[str] | list[dict[str, Any]] | None = None,
        override_lan: Literal["enable", "disable"] | None = None,
        lan: str | None = None,
        override_allowaccess: Literal["enable", "disable"] | None = None,
        allowaccess: Literal["https", "ssh", "snmp"] | list[str] | list[dict[str, Any]] | None = None,
        override_login_passwd_change: Literal["enable", "disable"] | None = None,
        login_passwd_change: Literal["yes", "default", "no"] | None = None,
        login_passwd: Any | None = None,
        override_default_mesh_root: Literal["enable", "disable"] | None = None,
        default_mesh_root: Literal["enable", "disable"] | None = None,
        radio_1: str | None = None,
        radio_2: str | None = None,
        radio_3: str | None = None,
        radio_4: str | None = None,
        image_download: Literal["enable", "disable"] | None = None,
        mesh_bridge_enable: Literal["default", "enable", "disable"] | None = None,
        purdue_level: Literal["1", "1.5", "2", "2.5", "3", "3.5", "4", "5", "5.5"] | None = None,
        coordinate_latitude: str | None = None,
        coordinate_longitude: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update wireless_controller/wtp object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (wtp-id) in the payload.

        Args:
            payload_dict: Resource data including wtp-id (primary key)
            wtp_id: Field wtp-id
            index: Field index
            uuid: Field uuid
            admin: Field admin
            name: Field name
            location: Field location
            comment: Field comment
            region: Field region
            region_x: Field region-x
            region_y: Field region-y
            firmware_provision: Field firmware-provision
            firmware_provision_latest: Field firmware-provision-latest
            wtp_profile: Field wtp-profile
            apcfg_profile: Field apcfg-profile
            bonjour_profile: Field bonjour-profile
            ble_major_id: Field ble-major-id
            ble_minor_id: Field ble-minor-id
            override_led_state: Field override-led-state
            led_state: Field led-state
            override_wan_port_mode: Field override-wan-port-mode
            wan_port_mode: Field wan-port-mode
            override_ip_fragment: Field override-ip-fragment
            ip_fragment_preventing: Field ip-fragment-preventing
            tun_mtu_uplink: Field tun-mtu-uplink
            tun_mtu_downlink: Field tun-mtu-downlink
            override_split_tunnel: Field override-split-tunnel
            split_tunneling_acl_path: Field split-tunneling-acl-path
            split_tunneling_acl_local_ap_subnet: Field split-tunneling-acl-local-ap-subnet
            split_tunneling_acl: Field split-tunneling-acl
            override_lan: Field override-lan
            lan: Field lan
            override_allowaccess: Field override-allowaccess
            allowaccess: Field allowaccess
            override_login_passwd_change: Field override-login-passwd-change
            login_passwd_change: Field login-passwd-change
            login_passwd: Field login-passwd
            override_default_mesh_root: Field override-default-mesh-root
            default_mesh_root: Field default-mesh-root
            radio_1: Field radio-1
            radio_2: Field radio-2
            radio_3: Field radio-3
            radio_4: Field radio-4
            image_download: Field image-download
            mesh_bridge_enable: Field mesh-bridge-enable
            purdue_level: Field purdue-level
            coordinate_latitude: Field coordinate-latitude
            coordinate_longitude: Field coordinate-longitude
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If wtp-id is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.wireless_controller_wtp.set(
            ...     wtp_id=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "wtp-id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_wtp.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_wtp.set(payload_dict=obj_data)
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
            wtp_id=wtp_id,
            index=index,
            uuid=uuid,
            admin=admin,
            name=name,
            location=location,
            comment=comment,
            region=region,
            region_x=region_x,
            region_y=region_y,
            firmware_provision=firmware_provision,
            firmware_provision_latest=firmware_provision_latest,
            wtp_profile=wtp_profile,
            apcfg_profile=apcfg_profile,
            bonjour_profile=bonjour_profile,
            ble_major_id=ble_major_id,
            ble_minor_id=ble_minor_id,
            override_led_state=override_led_state,
            led_state=led_state,
            override_wan_port_mode=override_wan_port_mode,
            wan_port_mode=wan_port_mode,
            override_ip_fragment=override_ip_fragment,
            ip_fragment_preventing=ip_fragment_preventing,
            tun_mtu_uplink=tun_mtu_uplink,
            tun_mtu_downlink=tun_mtu_downlink,
            override_split_tunnel=override_split_tunnel,
            split_tunneling_acl_path=split_tunneling_acl_path,
            split_tunneling_acl_local_ap_subnet=split_tunneling_acl_local_ap_subnet,
            split_tunneling_acl=split_tunneling_acl,
            override_lan=override_lan,
            lan=lan,
            override_allowaccess=override_allowaccess,
            allowaccess=allowaccess,
            override_login_passwd_change=override_login_passwd_change,
            login_passwd_change=login_passwd_change,
            login_passwd=login_passwd,
            override_default_mesh_root=override_default_mesh_root,
            default_mesh_root=default_mesh_root,
            radio_1=radio_1,
            radio_2=radio_2,
            radio_3=radio_3,
            radio_4=radio_4,
            image_download=image_download,
            mesh_bridge_enable=mesh_bridge_enable,
            purdue_level=purdue_level,
            coordinate_latitude=coordinate_latitude,
            coordinate_longitude=coordinate_longitude,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("wtp-id")
        if not mkey_value:
            raise ValueError("wtp-id is required for set()")
        
        # Check if resource exists
        if self.exists(wtp_id=mkey_value, vdom=vdom):
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
        wtp_id: str,
        action: Literal["before", "after"],
        reference_wtp_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move wireless_controller/wtp object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            wtp_id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_wtp_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.wireless_controller_wtp.move(
            ...     wtp_id=100,
            ...     action="before",
            ...     reference_wtp_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller/wtp",
            params={
                "wtp-id": wtp_id,
                "action": "move",
                action: reference_wtp_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        wtp_id: str,
        new_wtp_id: str,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone wireless_controller/wtp object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            wtp_id: Identifier of object to clone
            new_wtp_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.wireless_controller_wtp.clone(
            ...     wtp_id=1,
            ...     new_wtp_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller/wtp",
            params={
                "wtp-id": wtp_id,
                "new_wtp-id": new_wtp_id,
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
        wtp_id: str,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if wireless_controller/wtp object exists.
        
        Args:
            wtp_id: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.wireless_controller_wtp.exists(wtp_id=1):
            ...     fgt.api.cmdb.wireless_controller_wtp.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                wtp_id=wtp_id,
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

