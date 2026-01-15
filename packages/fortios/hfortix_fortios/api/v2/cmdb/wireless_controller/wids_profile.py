"""
FortiOS CMDB - Wireless_controller wids_profile

Configuration endpoint for managing cmdb wireless_controller/wids_profile objects.

API Endpoints:
    GET    /cmdb/wireless_controller/wids_profile
    POST   /cmdb/wireless_controller/wids_profile
    PUT    /cmdb/wireless_controller/wids_profile/{identifier}
    DELETE /cmdb/wireless_controller/wids_profile/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_wids_profile.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.wireless_controller_wids_profile.post(
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

class WidsProfile(CRUDEndpoint, MetadataMixin):
    """WidsProfile Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "wids_profile"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "ap_scan_channel_list_2G_5G": {
            "mkey": "chan",
            "required_fields": ['chan'],
            "example": "[{'chan': 'value'}]",
        },
        "ap_scan_channel_list_6G": {
            "mkey": "chan",
            "required_fields": ['chan'],
            "example": "[{'chan': 'value'}]",
        },
        "ap_bgscan_disable_schedules": {
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
        """Initialize WidsProfile endpoint."""
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
        Retrieve wireless_controller/wids_profile configuration.

        Configure wireless intrusion detection system (WIDS) profiles.

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
            >>> # Get all wireless_controller/wids_profile objects
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/wids_profile by name
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.wireless_controller_wids_profile.get_schema()

        See Also:
            - post(): Create new wireless_controller/wids_profile object
            - put(): Update existing wireless_controller/wids_profile object
            - delete(): Remove wireless_controller/wids_profile object
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
            endpoint = "/wireless-controller/wids-profile/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/wireless-controller/wids-profile"
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
            >>> schema = fgt.api.cmdb.wireless_controller_wids_profile.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.wireless_controller_wids_profile.get_schema(format="json-schema")
        
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
        sensor_mode: Literal["disable", "foreign", "both"] | None = None,
        ap_scan: Literal["disable", "enable"] | None = None,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = None,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = None,
        ap_bgscan_period: int | None = None,
        ap_bgscan_intv: int | None = None,
        ap_bgscan_duration: int | None = None,
        ap_bgscan_idle: int | None = None,
        ap_bgscan_report_intv: int | None = None,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = None,
        ap_fgscan_report_intv: int | None = None,
        ap_scan_passive: Literal["enable", "disable"] | None = None,
        ap_scan_threshold: str | None = None,
        ap_auto_suppress: Literal["enable", "disable"] | None = None,
        wireless_bridge: Literal["enable", "disable"] | None = None,
        deauth_broadcast: Literal["enable", "disable"] | None = None,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = None,
        long_duration_attack: Literal["enable", "disable"] | None = None,
        long_duration_thresh: int | None = None,
        invalid_mac_oui: Literal["enable", "disable"] | None = None,
        weak_wep_iv: Literal["enable", "disable"] | None = None,
        auth_frame_flood: Literal["enable", "disable"] | None = None,
        auth_flood_time: int | None = None,
        auth_flood_thresh: int | None = None,
        assoc_frame_flood: Literal["enable", "disable"] | None = None,
        assoc_flood_time: int | None = None,
        assoc_flood_thresh: int | None = None,
        reassoc_flood: Literal["enable", "disable"] | None = None,
        reassoc_flood_time: int | None = None,
        reassoc_flood_thresh: int | None = None,
        probe_flood: Literal["enable", "disable"] | None = None,
        probe_flood_time: int | None = None,
        probe_flood_thresh: int | None = None,
        bcn_flood: Literal["enable", "disable"] | None = None,
        bcn_flood_time: int | None = None,
        bcn_flood_thresh: int | None = None,
        rts_flood: Literal["enable", "disable"] | None = None,
        rts_flood_time: int | None = None,
        rts_flood_thresh: int | None = None,
        cts_flood: Literal["enable", "disable"] | None = None,
        cts_flood_time: int | None = None,
        cts_flood_thresh: int | None = None,
        client_flood: Literal["enable", "disable"] | None = None,
        client_flood_time: int | None = None,
        client_flood_thresh: int | None = None,
        block_ack_flood: Literal["enable", "disable"] | None = None,
        block_ack_flood_time: int | None = None,
        block_ack_flood_thresh: int | None = None,
        pspoll_flood: Literal["enable", "disable"] | None = None,
        pspoll_flood_time: int | None = None,
        pspoll_flood_thresh: int | None = None,
        netstumbler: Literal["enable", "disable"] | None = None,
        netstumbler_time: int | None = None,
        netstumbler_thresh: int | None = None,
        wellenreiter: Literal["enable", "disable"] | None = None,
        wellenreiter_time: int | None = None,
        wellenreiter_thresh: int | None = None,
        spoofed_deauth: Literal["enable", "disable"] | None = None,
        asleap_attack: Literal["enable", "disable"] | None = None,
        eapol_start_flood: Literal["enable", "disable"] | None = None,
        eapol_start_thresh: int | None = None,
        eapol_start_intv: int | None = None,
        eapol_logoff_flood: Literal["enable", "disable"] | None = None,
        eapol_logoff_thresh: int | None = None,
        eapol_logoff_intv: int | None = None,
        eapol_succ_flood: Literal["enable", "disable"] | None = None,
        eapol_succ_thresh: int | None = None,
        eapol_succ_intv: int | None = None,
        eapol_fail_flood: Literal["enable", "disable"] | None = None,
        eapol_fail_thresh: int | None = None,
        eapol_fail_intv: int | None = None,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = None,
        eapol_pre_succ_thresh: int | None = None,
        eapol_pre_succ_intv: int | None = None,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = None,
        eapol_pre_fail_thresh: int | None = None,
        eapol_pre_fail_intv: int | None = None,
        deauth_unknown_src_thresh: int | None = None,
        windows_bridge: Literal["enable", "disable"] | None = None,
        disassoc_broadcast: Literal["enable", "disable"] | None = None,
        ap_spoofing: Literal["enable", "disable"] | None = None,
        chan_based_mitm: Literal["enable", "disable"] | None = None,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = None,
        adhoc_network: Literal["enable", "disable"] | None = None,
        eapol_key_overflow: Literal["enable", "disable"] | None = None,
        ap_impersonation: Literal["enable", "disable"] | None = None,
        invalid_addr_combination: Literal["enable", "disable"] | None = None,
        beacon_wrong_channel: Literal["enable", "disable"] | None = None,
        ht_greenfield: Literal["enable", "disable"] | None = None,
        overflow_ie: Literal["enable", "disable"] | None = None,
        malformed_ht_ie: Literal["enable", "disable"] | None = None,
        malformed_auth: Literal["enable", "disable"] | None = None,
        malformed_association: Literal["enable", "disable"] | None = None,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = None,
        valid_ssid_misuse: Literal["enable", "disable"] | None = None,
        valid_client_misassociation: Literal["enable", "disable"] | None = None,
        hotspotter_attack: Literal["enable", "disable"] | None = None,
        pwsave_dos_attack: Literal["enable", "disable"] | None = None,
        omerta_attack: Literal["enable", "disable"] | None = None,
        disconnect_station: Literal["enable", "disable"] | None = None,
        unencrypted_valid: Literal["enable", "disable"] | None = None,
        fata_jack: Literal["enable", "disable"] | None = None,
        risky_encryption: Literal["enable", "disable"] | None = None,
        fuzzed_beacon: Literal["enable", "disable"] | None = None,
        fuzzed_probe_request: Literal["enable", "disable"] | None = None,
        fuzzed_probe_response: Literal["enable", "disable"] | None = None,
        air_jack: Literal["enable", "disable"] | None = None,
        wpa_ft_attack: Literal["enable", "disable"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing wireless_controller/wids_profile object.

        Configure wireless intrusion detection system (WIDS) profiles.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: WIDS profile name.
            comment: Comment.
            sensor_mode: Scan nearby WiFi stations (default = disable).
            ap_scan: Enable/disable rogue AP detection.
            ap_scan_channel_list_2G_5G: Selected ap scan channel list for 2.4G and 5G bands.
                Default format: [{'chan': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'chan': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'chan': 'val1'}, ...]
                  - List of dicts: [{'chan': 'value'}] (recommended)
            ap_scan_channel_list_6G: Selected ap scan channel list for 6G band.
                Default format: [{'chan': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'chan': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'chan': 'val1'}, ...]
                  - List of dicts: [{'chan': 'value'}] (recommended)
            ap_bgscan_period: Period between background scans (10 - 3600 sec, default = 600).
            ap_bgscan_intv: Period between successive channel scans (1 - 600 sec, default = 3).
            ap_bgscan_duration: Listen time on scanning a channel (10 - 1000 msec, default = 30).
            ap_bgscan_idle: Wait time for channel inactivity before scanning this channel (0 - 1000 msec, default = 20).
            ap_bgscan_report_intv: Period between background scan reports (15 - 600 sec, default = 30).
            ap_bgscan_disable_schedules: Firewall schedules for turning off FortiAP radio background scan. Background scan will be disabled when at least one of the schedules is valid. Separate multiple schedule names with a space.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ap_fgscan_report_intv: Period between foreground scan reports (15 - 600 sec, default = 15).
            ap_scan_passive: Enable/disable passive scanning. Enable means do not send probe request on any channels (default = disable).
            ap_scan_threshold: Minimum signal level/threshold in dBm required for the AP to report detected rogue AP (-95 to -20, default = -90).
            ap_auto_suppress: Enable/disable on-wire rogue AP auto-suppression (default = disable).
            wireless_bridge: Enable/disable wireless bridge detection (default = disable).
            deauth_broadcast: Enable/disable broadcasting de-authentication detection (default = disable).
            null_ssid_probe_resp: Enable/disable null SSID probe response detection (default = disable).
            long_duration_attack: Enable/disable long duration attack detection based on user configured threshold (default = disable).
            long_duration_thresh: Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200).
            invalid_mac_oui: Enable/disable invalid MAC OUI detection.
            weak_wep_iv: Enable/disable weak WEP IV (Initialization Vector) detection (default = disable).
            auth_frame_flood: Enable/disable authentication frame flooding detection (default = disable).
            auth_flood_time: Number of seconds after which a station is considered not connected.
            auth_flood_thresh: The threshold value for authentication frame flooding.
            assoc_frame_flood: Enable/disable association frame flooding detection (default = disable).
            assoc_flood_time: Number of seconds after which a station is considered not connected.
            assoc_flood_thresh: The threshold value for association frame flooding.
            reassoc_flood: Enable/disable reassociation flood detection (default = disable).
            reassoc_flood_time: Detection Window Period.
            reassoc_flood_thresh: The threshold value for reassociation flood.
            probe_flood: Enable/disable probe flood detection (default = disable).
            probe_flood_time: Detection Window Period.
            probe_flood_thresh: The threshold value for probe flood.
            bcn_flood: Enable/disable bcn flood detection (default = disable).
            bcn_flood_time: Detection Window Period.
            bcn_flood_thresh: The threshold value for bcn flood.
            rts_flood: Enable/disable rts flood detection (default = disable).
            rts_flood_time: Detection Window Period.
            rts_flood_thresh: The threshold value for rts flood.
            cts_flood: Enable/disable cts flood detection (default = disable).
            cts_flood_time: Detection Window Period.
            cts_flood_thresh: The threshold value for cts flood.
            client_flood: Enable/disable client flood detection (default = disable).
            client_flood_time: Detection Window Period.
            client_flood_thresh: The threshold value for client flood.
            block_ack_flood: Enable/disable block_ack flood detection (default = disable).
            block_ack_flood_time: Detection Window Period.
            block_ack_flood_thresh: The threshold value for block_ack flood.
            pspoll_flood: Enable/disable pspoll flood detection (default = disable).
            pspoll_flood_time: Detection Window Period.
            pspoll_flood_thresh: The threshold value for pspoll flood.
            netstumbler: Enable/disable netstumbler detection (default = disable).
            netstumbler_time: Detection Window Period.
            netstumbler_thresh: The threshold value for netstumbler.
            wellenreiter: Enable/disable wellenreiter detection (default = disable).
            wellenreiter_time: Detection Window Period.
            wellenreiter_thresh: The threshold value for wellenreiter.
            spoofed_deauth: Enable/disable spoofed de-authentication attack detection (default = disable).
            asleap_attack: Enable/disable asleap attack detection (default = disable).
            eapol_start_flood: Enable/disable EAPOL-Start flooding (to AP) detection (default = disable).
            eapol_start_thresh: The threshold value for EAPOL-Start flooding in specified interval.
            eapol_start_intv: The detection interval for EAPOL-Start flooding (1 - 3600 sec).
            eapol_logoff_flood: Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable).
            eapol_logoff_thresh: The threshold value for EAPOL-Logoff flooding in specified interval.
            eapol_logoff_intv: The detection interval for EAPOL-Logoff flooding (1 - 3600 sec).
            eapol_succ_flood: Enable/disable EAPOL-Success flooding (to AP) detection (default = disable).
            eapol_succ_thresh: The threshold value for EAPOL-Success flooding in specified interval.
            eapol_succ_intv: The detection interval for EAPOL-Success flooding (1 - 3600 sec).
            eapol_fail_flood: Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable).
            eapol_fail_thresh: The threshold value for EAPOL-Failure flooding in specified interval.
            eapol_fail_intv: The detection interval for EAPOL-Failure flooding (1 - 3600 sec).
            eapol_pre_succ_flood: Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable).
            eapol_pre_succ_thresh: The threshold value for premature EAPOL-Success flooding in specified interval.
            eapol_pre_succ_intv: The detection interval for premature EAPOL-Success flooding (1 - 3600 sec).
            eapol_pre_fail_flood: Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable).
            eapol_pre_fail_thresh: The threshold value for premature EAPOL-Failure flooding in specified interval.
            eapol_pre_fail_intv: The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec).
            deauth_unknown_src_thresh: Threshold value per second to deauth unknown src for DoS attack (0: no limit).
            windows_bridge: Enable/disable windows bridge detection (default = disable).
            disassoc_broadcast: Enable/disable broadcast dis-association detection (default = disable).
            ap_spoofing: Enable/disable AP spoofing detection (default = disable).
            chan_based_mitm: Enable/disable channel based mitm detection (default = disable).
            adhoc_valid_ssid: Enable/disable adhoc using valid SSID detection (default = disable).
            adhoc_network: Enable/disable adhoc network detection (default = disable).
            eapol_key_overflow: Enable/disable overflow EAPOL key detection (default = disable).
            ap_impersonation: Enable/disable AP impersonation detection (default = disable).
            invalid_addr_combination: Enable/disable invalid address combination detection (default = disable).
            beacon_wrong_channel: Enable/disable beacon wrong channel detection (default = disable).
            ht_greenfield: Enable/disable HT greenfield detection (default = disable).
            overflow_ie: Enable/disable overflow IE detection (default = disable).
            malformed_ht_ie: Enable/disable malformed HT IE detection (default = disable).
            malformed_auth: Enable/disable malformed auth frame detection (default = disable).
            malformed_association: Enable/disable malformed association request detection (default = disable).
            ht_40mhz_intolerance: Enable/disable HT 40 MHz intolerance detection (default = disable).
            valid_ssid_misuse: Enable/disable valid SSID misuse detection (default = disable).
            valid_client_misassociation: Enable/disable valid client misassociation detection (default = disable).
            hotspotter_attack: Enable/disable hotspotter attack detection (default = disable).
            pwsave_dos_attack: Enable/disable power save DOS attack detection (default = disable).
            omerta_attack: Enable/disable omerta attack detection (default = disable).
            disconnect_station: Enable/disable disconnect station detection (default = disable).
            unencrypted_valid: Enable/disable unencrypted valid detection (default = disable).
            fata_jack: Enable/disable FATA-Jack detection (default = disable).
            risky_encryption: Enable/disable Risky Encryption detection (default = disable).
            fuzzed_beacon: Enable/disable fuzzed beacon detection (default = disable).
            fuzzed_probe_request: Enable/disable fuzzed probe request detection (default = disable).
            fuzzed_probe_response: Enable/disable fuzzed probe response detection (default = disable).
            air_jack: Enable/disable AirJack detection (default = disable).
            wpa_ft_attack: Enable/disable WPA FT attack detection (default = disable).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if ap_scan_channel_list_2G_5G is not None:
            ap_scan_channel_list_2G_5G = normalize_table_field(
                ap_scan_channel_list_2G_5G,
                mkey="chan",
                required_fields=['chan'],
                field_name="ap_scan_channel_list_2G_5G",
                example="[{'chan': 'value'}]",
            )
        if ap_scan_channel_list_6G is not None:
            ap_scan_channel_list_6G = normalize_table_field(
                ap_scan_channel_list_6G,
                mkey="chan",
                required_fields=['chan'],
                field_name="ap_scan_channel_list_6G",
                example="[{'chan': 'value'}]",
            )
        if ap_bgscan_disable_schedules is not None:
            ap_bgscan_disable_schedules = normalize_table_field(
                ap_bgscan_disable_schedules,
                mkey="name",
                required_fields=['name'],
                field_name="ap_bgscan_disable_schedules",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            comment=comment,
            sensor_mode=sensor_mode,
            ap_scan=ap_scan,
            ap_scan_channel_list_2G_5G=ap_scan_channel_list_2G_5G,
            ap_scan_channel_list_6G=ap_scan_channel_list_6G,
            ap_bgscan_period=ap_bgscan_period,
            ap_bgscan_intv=ap_bgscan_intv,
            ap_bgscan_duration=ap_bgscan_duration,
            ap_bgscan_idle=ap_bgscan_idle,
            ap_bgscan_report_intv=ap_bgscan_report_intv,
            ap_bgscan_disable_schedules=ap_bgscan_disable_schedules,
            ap_fgscan_report_intv=ap_fgscan_report_intv,
            ap_scan_passive=ap_scan_passive,
            ap_scan_threshold=ap_scan_threshold,
            ap_auto_suppress=ap_auto_suppress,
            wireless_bridge=wireless_bridge,
            deauth_broadcast=deauth_broadcast,
            null_ssid_probe_resp=null_ssid_probe_resp,
            long_duration_attack=long_duration_attack,
            long_duration_thresh=long_duration_thresh,
            invalid_mac_oui=invalid_mac_oui,
            weak_wep_iv=weak_wep_iv,
            auth_frame_flood=auth_frame_flood,
            auth_flood_time=auth_flood_time,
            auth_flood_thresh=auth_flood_thresh,
            assoc_frame_flood=assoc_frame_flood,
            assoc_flood_time=assoc_flood_time,
            assoc_flood_thresh=assoc_flood_thresh,
            reassoc_flood=reassoc_flood,
            reassoc_flood_time=reassoc_flood_time,
            reassoc_flood_thresh=reassoc_flood_thresh,
            probe_flood=probe_flood,
            probe_flood_time=probe_flood_time,
            probe_flood_thresh=probe_flood_thresh,
            bcn_flood=bcn_flood,
            bcn_flood_time=bcn_flood_time,
            bcn_flood_thresh=bcn_flood_thresh,
            rts_flood=rts_flood,
            rts_flood_time=rts_flood_time,
            rts_flood_thresh=rts_flood_thresh,
            cts_flood=cts_flood,
            cts_flood_time=cts_flood_time,
            cts_flood_thresh=cts_flood_thresh,
            client_flood=client_flood,
            client_flood_time=client_flood_time,
            client_flood_thresh=client_flood_thresh,
            block_ack_flood=block_ack_flood,
            block_ack_flood_time=block_ack_flood_time,
            block_ack_flood_thresh=block_ack_flood_thresh,
            pspoll_flood=pspoll_flood,
            pspoll_flood_time=pspoll_flood_time,
            pspoll_flood_thresh=pspoll_flood_thresh,
            netstumbler=netstumbler,
            netstumbler_time=netstumbler_time,
            netstumbler_thresh=netstumbler_thresh,
            wellenreiter=wellenreiter,
            wellenreiter_time=wellenreiter_time,
            wellenreiter_thresh=wellenreiter_thresh,
            spoofed_deauth=spoofed_deauth,
            asleap_attack=asleap_attack,
            eapol_start_flood=eapol_start_flood,
            eapol_start_thresh=eapol_start_thresh,
            eapol_start_intv=eapol_start_intv,
            eapol_logoff_flood=eapol_logoff_flood,
            eapol_logoff_thresh=eapol_logoff_thresh,
            eapol_logoff_intv=eapol_logoff_intv,
            eapol_succ_flood=eapol_succ_flood,
            eapol_succ_thresh=eapol_succ_thresh,
            eapol_succ_intv=eapol_succ_intv,
            eapol_fail_flood=eapol_fail_flood,
            eapol_fail_thresh=eapol_fail_thresh,
            eapol_fail_intv=eapol_fail_intv,
            eapol_pre_succ_flood=eapol_pre_succ_flood,
            eapol_pre_succ_thresh=eapol_pre_succ_thresh,
            eapol_pre_succ_intv=eapol_pre_succ_intv,
            eapol_pre_fail_flood=eapol_pre_fail_flood,
            eapol_pre_fail_thresh=eapol_pre_fail_thresh,
            eapol_pre_fail_intv=eapol_pre_fail_intv,
            deauth_unknown_src_thresh=deauth_unknown_src_thresh,
            windows_bridge=windows_bridge,
            disassoc_broadcast=disassoc_broadcast,
            ap_spoofing=ap_spoofing,
            chan_based_mitm=chan_based_mitm,
            adhoc_valid_ssid=adhoc_valid_ssid,
            adhoc_network=adhoc_network,
            eapol_key_overflow=eapol_key_overflow,
            ap_impersonation=ap_impersonation,
            invalid_addr_combination=invalid_addr_combination,
            beacon_wrong_channel=beacon_wrong_channel,
            ht_greenfield=ht_greenfield,
            overflow_ie=overflow_ie,
            malformed_ht_ie=malformed_ht_ie,
            malformed_auth=malformed_auth,
            malformed_association=malformed_association,
            ht_40mhz_intolerance=ht_40mhz_intolerance,
            valid_ssid_misuse=valid_ssid_misuse,
            valid_client_misassociation=valid_client_misassociation,
            hotspotter_attack=hotspotter_attack,
            pwsave_dos_attack=pwsave_dos_attack,
            omerta_attack=omerta_attack,
            disconnect_station=disconnect_station,
            unencrypted_valid=unencrypted_valid,
            fata_jack=fata_jack,
            risky_encryption=risky_encryption,
            fuzzed_beacon=fuzzed_beacon,
            fuzzed_probe_request=fuzzed_probe_request,
            fuzzed_probe_response=fuzzed_probe_response,
            air_jack=air_jack,
            wpa_ft_attack=wpa_ft_attack,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.wids_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wids_profile",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller/wids-profile/" + str(name_value)

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
        sensor_mode: Literal["disable", "foreign", "both"] | None = None,
        ap_scan: Literal["disable", "enable"] | None = None,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = None,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = None,
        ap_bgscan_period: int | None = None,
        ap_bgscan_intv: int | None = None,
        ap_bgscan_duration: int | None = None,
        ap_bgscan_idle: int | None = None,
        ap_bgscan_report_intv: int | None = None,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = None,
        ap_fgscan_report_intv: int | None = None,
        ap_scan_passive: Literal["enable", "disable"] | None = None,
        ap_scan_threshold: str | None = None,
        ap_auto_suppress: Literal["enable", "disable"] | None = None,
        wireless_bridge: Literal["enable", "disable"] | None = None,
        deauth_broadcast: Literal["enable", "disable"] | None = None,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = None,
        long_duration_attack: Literal["enable", "disable"] | None = None,
        long_duration_thresh: int | None = None,
        invalid_mac_oui: Literal["enable", "disable"] | None = None,
        weak_wep_iv: Literal["enable", "disable"] | None = None,
        auth_frame_flood: Literal["enable", "disable"] | None = None,
        auth_flood_time: int | None = None,
        auth_flood_thresh: int | None = None,
        assoc_frame_flood: Literal["enable", "disable"] | None = None,
        assoc_flood_time: int | None = None,
        assoc_flood_thresh: int | None = None,
        reassoc_flood: Literal["enable", "disable"] | None = None,
        reassoc_flood_time: int | None = None,
        reassoc_flood_thresh: int | None = None,
        probe_flood: Literal["enable", "disable"] | None = None,
        probe_flood_time: int | None = None,
        probe_flood_thresh: int | None = None,
        bcn_flood: Literal["enable", "disable"] | None = None,
        bcn_flood_time: int | None = None,
        bcn_flood_thresh: int | None = None,
        rts_flood: Literal["enable", "disable"] | None = None,
        rts_flood_time: int | None = None,
        rts_flood_thresh: int | None = None,
        cts_flood: Literal["enable", "disable"] | None = None,
        cts_flood_time: int | None = None,
        cts_flood_thresh: int | None = None,
        client_flood: Literal["enable", "disable"] | None = None,
        client_flood_time: int | None = None,
        client_flood_thresh: int | None = None,
        block_ack_flood: Literal["enable", "disable"] | None = None,
        block_ack_flood_time: int | None = None,
        block_ack_flood_thresh: int | None = None,
        pspoll_flood: Literal["enable", "disable"] | None = None,
        pspoll_flood_time: int | None = None,
        pspoll_flood_thresh: int | None = None,
        netstumbler: Literal["enable", "disable"] | None = None,
        netstumbler_time: int | None = None,
        netstumbler_thresh: int | None = None,
        wellenreiter: Literal["enable", "disable"] | None = None,
        wellenreiter_time: int | None = None,
        wellenreiter_thresh: int | None = None,
        spoofed_deauth: Literal["enable", "disable"] | None = None,
        asleap_attack: Literal["enable", "disable"] | None = None,
        eapol_start_flood: Literal["enable", "disable"] | None = None,
        eapol_start_thresh: int | None = None,
        eapol_start_intv: int | None = None,
        eapol_logoff_flood: Literal["enable", "disable"] | None = None,
        eapol_logoff_thresh: int | None = None,
        eapol_logoff_intv: int | None = None,
        eapol_succ_flood: Literal["enable", "disable"] | None = None,
        eapol_succ_thresh: int | None = None,
        eapol_succ_intv: int | None = None,
        eapol_fail_flood: Literal["enable", "disable"] | None = None,
        eapol_fail_thresh: int | None = None,
        eapol_fail_intv: int | None = None,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = None,
        eapol_pre_succ_thresh: int | None = None,
        eapol_pre_succ_intv: int | None = None,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = None,
        eapol_pre_fail_thresh: int | None = None,
        eapol_pre_fail_intv: int | None = None,
        deauth_unknown_src_thresh: int | None = None,
        windows_bridge: Literal["enable", "disable"] | None = None,
        disassoc_broadcast: Literal["enable", "disable"] | None = None,
        ap_spoofing: Literal["enable", "disable"] | None = None,
        chan_based_mitm: Literal["enable", "disable"] | None = None,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = None,
        adhoc_network: Literal["enable", "disable"] | None = None,
        eapol_key_overflow: Literal["enable", "disable"] | None = None,
        ap_impersonation: Literal["enable", "disable"] | None = None,
        invalid_addr_combination: Literal["enable", "disable"] | None = None,
        beacon_wrong_channel: Literal["enable", "disable"] | None = None,
        ht_greenfield: Literal["enable", "disable"] | None = None,
        overflow_ie: Literal["enable", "disable"] | None = None,
        malformed_ht_ie: Literal["enable", "disable"] | None = None,
        malformed_auth: Literal["enable", "disable"] | None = None,
        malformed_association: Literal["enable", "disable"] | None = None,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = None,
        valid_ssid_misuse: Literal["enable", "disable"] | None = None,
        valid_client_misassociation: Literal["enable", "disable"] | None = None,
        hotspotter_attack: Literal["enable", "disable"] | None = None,
        pwsave_dos_attack: Literal["enable", "disable"] | None = None,
        omerta_attack: Literal["enable", "disable"] | None = None,
        disconnect_station: Literal["enable", "disable"] | None = None,
        unencrypted_valid: Literal["enable", "disable"] | None = None,
        fata_jack: Literal["enable", "disable"] | None = None,
        risky_encryption: Literal["enable", "disable"] | None = None,
        fuzzed_beacon: Literal["enable", "disable"] | None = None,
        fuzzed_probe_request: Literal["enable", "disable"] | None = None,
        fuzzed_probe_response: Literal["enable", "disable"] | None = None,
        air_jack: Literal["enable", "disable"] | None = None,
        wpa_ft_attack: Literal["enable", "disable"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new wireless_controller/wids_profile object.

        Configure wireless intrusion detection system (WIDS) profiles.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: WIDS profile name.
            comment: Comment.
            sensor_mode: Scan nearby WiFi stations (default = disable).
            ap_scan: Enable/disable rogue AP detection.
            ap_scan_channel_list_2G_5G: Selected ap scan channel list for 2.4G and 5G bands.
                Default format: [{'chan': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'chan': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'chan': 'val1'}, ...]
                  - List of dicts: [{'chan': 'value'}] (recommended)
            ap_scan_channel_list_6G: Selected ap scan channel list for 6G band.
                Default format: [{'chan': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'chan': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'chan': 'val1'}, ...]
                  - List of dicts: [{'chan': 'value'}] (recommended)
            ap_bgscan_period: Period between background scans (10 - 3600 sec, default = 600).
            ap_bgscan_intv: Period between successive channel scans (1 - 600 sec, default = 3).
            ap_bgscan_duration: Listen time on scanning a channel (10 - 1000 msec, default = 30).
            ap_bgscan_idle: Wait time for channel inactivity before scanning this channel (0 - 1000 msec, default = 20).
            ap_bgscan_report_intv: Period between background scan reports (15 - 600 sec, default = 30).
            ap_bgscan_disable_schedules: Firewall schedules for turning off FortiAP radio background scan. Background scan will be disabled when at least one of the schedules is valid. Separate multiple schedule names with a space.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ap_fgscan_report_intv: Period between foreground scan reports (15 - 600 sec, default = 15).
            ap_scan_passive: Enable/disable passive scanning. Enable means do not send probe request on any channels (default = disable).
            ap_scan_threshold: Minimum signal level/threshold in dBm required for the AP to report detected rogue AP (-95 to -20, default = -90).
            ap_auto_suppress: Enable/disable on-wire rogue AP auto-suppression (default = disable).
            wireless_bridge: Enable/disable wireless bridge detection (default = disable).
            deauth_broadcast: Enable/disable broadcasting de-authentication detection (default = disable).
            null_ssid_probe_resp: Enable/disable null SSID probe response detection (default = disable).
            long_duration_attack: Enable/disable long duration attack detection based on user configured threshold (default = disable).
            long_duration_thresh: Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200).
            invalid_mac_oui: Enable/disable invalid MAC OUI detection.
            weak_wep_iv: Enable/disable weak WEP IV (Initialization Vector) detection (default = disable).
            auth_frame_flood: Enable/disable authentication frame flooding detection (default = disable).
            auth_flood_time: Number of seconds after which a station is considered not connected.
            auth_flood_thresh: The threshold value for authentication frame flooding.
            assoc_frame_flood: Enable/disable association frame flooding detection (default = disable).
            assoc_flood_time: Number of seconds after which a station is considered not connected.
            assoc_flood_thresh: The threshold value for association frame flooding.
            reassoc_flood: Enable/disable reassociation flood detection (default = disable).
            reassoc_flood_time: Detection Window Period.
            reassoc_flood_thresh: The threshold value for reassociation flood.
            probe_flood: Enable/disable probe flood detection (default = disable).
            probe_flood_time: Detection Window Period.
            probe_flood_thresh: The threshold value for probe flood.
            bcn_flood: Enable/disable bcn flood detection (default = disable).
            bcn_flood_time: Detection Window Period.
            bcn_flood_thresh: The threshold value for bcn flood.
            rts_flood: Enable/disable rts flood detection (default = disable).
            rts_flood_time: Detection Window Period.
            rts_flood_thresh: The threshold value for rts flood.
            cts_flood: Enable/disable cts flood detection (default = disable).
            cts_flood_time: Detection Window Period.
            cts_flood_thresh: The threshold value for cts flood.
            client_flood: Enable/disable client flood detection (default = disable).
            client_flood_time: Detection Window Period.
            client_flood_thresh: The threshold value for client flood.
            block_ack_flood: Enable/disable block_ack flood detection (default = disable).
            block_ack_flood_time: Detection Window Period.
            block_ack_flood_thresh: The threshold value for block_ack flood.
            pspoll_flood: Enable/disable pspoll flood detection (default = disable).
            pspoll_flood_time: Detection Window Period.
            pspoll_flood_thresh: The threshold value for pspoll flood.
            netstumbler: Enable/disable netstumbler detection (default = disable).
            netstumbler_time: Detection Window Period.
            netstumbler_thresh: The threshold value for netstumbler.
            wellenreiter: Enable/disable wellenreiter detection (default = disable).
            wellenreiter_time: Detection Window Period.
            wellenreiter_thresh: The threshold value for wellenreiter.
            spoofed_deauth: Enable/disable spoofed de-authentication attack detection (default = disable).
            asleap_attack: Enable/disable asleap attack detection (default = disable).
            eapol_start_flood: Enable/disable EAPOL-Start flooding (to AP) detection (default = disable).
            eapol_start_thresh: The threshold value for EAPOL-Start flooding in specified interval.
            eapol_start_intv: The detection interval for EAPOL-Start flooding (1 - 3600 sec).
            eapol_logoff_flood: Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable).
            eapol_logoff_thresh: The threshold value for EAPOL-Logoff flooding in specified interval.
            eapol_logoff_intv: The detection interval for EAPOL-Logoff flooding (1 - 3600 sec).
            eapol_succ_flood: Enable/disable EAPOL-Success flooding (to AP) detection (default = disable).
            eapol_succ_thresh: The threshold value for EAPOL-Success flooding in specified interval.
            eapol_succ_intv: The detection interval for EAPOL-Success flooding (1 - 3600 sec).
            eapol_fail_flood: Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable).
            eapol_fail_thresh: The threshold value for EAPOL-Failure flooding in specified interval.
            eapol_fail_intv: The detection interval for EAPOL-Failure flooding (1 - 3600 sec).
            eapol_pre_succ_flood: Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable).
            eapol_pre_succ_thresh: The threshold value for premature EAPOL-Success flooding in specified interval.
            eapol_pre_succ_intv: The detection interval for premature EAPOL-Success flooding (1 - 3600 sec).
            eapol_pre_fail_flood: Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable).
            eapol_pre_fail_thresh: The threshold value for premature EAPOL-Failure flooding in specified interval.
            eapol_pre_fail_intv: The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec).
            deauth_unknown_src_thresh: Threshold value per second to deauth unknown src for DoS attack (0: no limit).
            windows_bridge: Enable/disable windows bridge detection (default = disable).
            disassoc_broadcast: Enable/disable broadcast dis-association detection (default = disable).
            ap_spoofing: Enable/disable AP spoofing detection (default = disable).
            chan_based_mitm: Enable/disable channel based mitm detection (default = disable).
            adhoc_valid_ssid: Enable/disable adhoc using valid SSID detection (default = disable).
            adhoc_network: Enable/disable adhoc network detection (default = disable).
            eapol_key_overflow: Enable/disable overflow EAPOL key detection (default = disable).
            ap_impersonation: Enable/disable AP impersonation detection (default = disable).
            invalid_addr_combination: Enable/disable invalid address combination detection (default = disable).
            beacon_wrong_channel: Enable/disable beacon wrong channel detection (default = disable).
            ht_greenfield: Enable/disable HT greenfield detection (default = disable).
            overflow_ie: Enable/disable overflow IE detection (default = disable).
            malformed_ht_ie: Enable/disable malformed HT IE detection (default = disable).
            malformed_auth: Enable/disable malformed auth frame detection (default = disable).
            malformed_association: Enable/disable malformed association request detection (default = disable).
            ht_40mhz_intolerance: Enable/disable HT 40 MHz intolerance detection (default = disable).
            valid_ssid_misuse: Enable/disable valid SSID misuse detection (default = disable).
            valid_client_misassociation: Enable/disable valid client misassociation detection (default = disable).
            hotspotter_attack: Enable/disable hotspotter attack detection (default = disable).
            pwsave_dos_attack: Enable/disable power save DOS attack detection (default = disable).
            omerta_attack: Enable/disable omerta attack detection (default = disable).
            disconnect_station: Enable/disable disconnect station detection (default = disable).
            unencrypted_valid: Enable/disable unencrypted valid detection (default = disable).
            fata_jack: Enable/disable FATA-Jack detection (default = disable).
            risky_encryption: Enable/disable Risky Encryption detection (default = disable).
            fuzzed_beacon: Enable/disable fuzzed beacon detection (default = disable).
            fuzzed_probe_request: Enable/disable fuzzed probe request detection (default = disable).
            fuzzed_probe_response: Enable/disable fuzzed probe response detection (default = disable).
            air_jack: Enable/disable AirJack detection (default = disable).
            wpa_ft_attack: Enable/disable WPA FT attack detection (default = disable).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = WidsProfile.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(WidsProfile.required_fields()) }}
            
            Use WidsProfile.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if ap_scan_channel_list_2G_5G is not None:
            ap_scan_channel_list_2G_5G = normalize_table_field(
                ap_scan_channel_list_2G_5G,
                mkey="chan",
                required_fields=['chan'],
                field_name="ap_scan_channel_list_2G_5G",
                example="[{'chan': 'value'}]",
            )
        if ap_scan_channel_list_6G is not None:
            ap_scan_channel_list_6G = normalize_table_field(
                ap_scan_channel_list_6G,
                mkey="chan",
                required_fields=['chan'],
                field_name="ap_scan_channel_list_6G",
                example="[{'chan': 'value'}]",
            )
        if ap_bgscan_disable_schedules is not None:
            ap_bgscan_disable_schedules = normalize_table_field(
                ap_bgscan_disable_schedules,
                mkey="name",
                required_fields=['name'],
                field_name="ap_bgscan_disable_schedules",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            comment=comment,
            sensor_mode=sensor_mode,
            ap_scan=ap_scan,
            ap_scan_channel_list_2G_5G=ap_scan_channel_list_2G_5G,
            ap_scan_channel_list_6G=ap_scan_channel_list_6G,
            ap_bgscan_period=ap_bgscan_period,
            ap_bgscan_intv=ap_bgscan_intv,
            ap_bgscan_duration=ap_bgscan_duration,
            ap_bgscan_idle=ap_bgscan_idle,
            ap_bgscan_report_intv=ap_bgscan_report_intv,
            ap_bgscan_disable_schedules=ap_bgscan_disable_schedules,
            ap_fgscan_report_intv=ap_fgscan_report_intv,
            ap_scan_passive=ap_scan_passive,
            ap_scan_threshold=ap_scan_threshold,
            ap_auto_suppress=ap_auto_suppress,
            wireless_bridge=wireless_bridge,
            deauth_broadcast=deauth_broadcast,
            null_ssid_probe_resp=null_ssid_probe_resp,
            long_duration_attack=long_duration_attack,
            long_duration_thresh=long_duration_thresh,
            invalid_mac_oui=invalid_mac_oui,
            weak_wep_iv=weak_wep_iv,
            auth_frame_flood=auth_frame_flood,
            auth_flood_time=auth_flood_time,
            auth_flood_thresh=auth_flood_thresh,
            assoc_frame_flood=assoc_frame_flood,
            assoc_flood_time=assoc_flood_time,
            assoc_flood_thresh=assoc_flood_thresh,
            reassoc_flood=reassoc_flood,
            reassoc_flood_time=reassoc_flood_time,
            reassoc_flood_thresh=reassoc_flood_thresh,
            probe_flood=probe_flood,
            probe_flood_time=probe_flood_time,
            probe_flood_thresh=probe_flood_thresh,
            bcn_flood=bcn_flood,
            bcn_flood_time=bcn_flood_time,
            bcn_flood_thresh=bcn_flood_thresh,
            rts_flood=rts_flood,
            rts_flood_time=rts_flood_time,
            rts_flood_thresh=rts_flood_thresh,
            cts_flood=cts_flood,
            cts_flood_time=cts_flood_time,
            cts_flood_thresh=cts_flood_thresh,
            client_flood=client_flood,
            client_flood_time=client_flood_time,
            client_flood_thresh=client_flood_thresh,
            block_ack_flood=block_ack_flood,
            block_ack_flood_time=block_ack_flood_time,
            block_ack_flood_thresh=block_ack_flood_thresh,
            pspoll_flood=pspoll_flood,
            pspoll_flood_time=pspoll_flood_time,
            pspoll_flood_thresh=pspoll_flood_thresh,
            netstumbler=netstumbler,
            netstumbler_time=netstumbler_time,
            netstumbler_thresh=netstumbler_thresh,
            wellenreiter=wellenreiter,
            wellenreiter_time=wellenreiter_time,
            wellenreiter_thresh=wellenreiter_thresh,
            spoofed_deauth=spoofed_deauth,
            asleap_attack=asleap_attack,
            eapol_start_flood=eapol_start_flood,
            eapol_start_thresh=eapol_start_thresh,
            eapol_start_intv=eapol_start_intv,
            eapol_logoff_flood=eapol_logoff_flood,
            eapol_logoff_thresh=eapol_logoff_thresh,
            eapol_logoff_intv=eapol_logoff_intv,
            eapol_succ_flood=eapol_succ_flood,
            eapol_succ_thresh=eapol_succ_thresh,
            eapol_succ_intv=eapol_succ_intv,
            eapol_fail_flood=eapol_fail_flood,
            eapol_fail_thresh=eapol_fail_thresh,
            eapol_fail_intv=eapol_fail_intv,
            eapol_pre_succ_flood=eapol_pre_succ_flood,
            eapol_pre_succ_thresh=eapol_pre_succ_thresh,
            eapol_pre_succ_intv=eapol_pre_succ_intv,
            eapol_pre_fail_flood=eapol_pre_fail_flood,
            eapol_pre_fail_thresh=eapol_pre_fail_thresh,
            eapol_pre_fail_intv=eapol_pre_fail_intv,
            deauth_unknown_src_thresh=deauth_unknown_src_thresh,
            windows_bridge=windows_bridge,
            disassoc_broadcast=disassoc_broadcast,
            ap_spoofing=ap_spoofing,
            chan_based_mitm=chan_based_mitm,
            adhoc_valid_ssid=adhoc_valid_ssid,
            adhoc_network=adhoc_network,
            eapol_key_overflow=eapol_key_overflow,
            ap_impersonation=ap_impersonation,
            invalid_addr_combination=invalid_addr_combination,
            beacon_wrong_channel=beacon_wrong_channel,
            ht_greenfield=ht_greenfield,
            overflow_ie=overflow_ie,
            malformed_ht_ie=malformed_ht_ie,
            malformed_auth=malformed_auth,
            malformed_association=malformed_association,
            ht_40mhz_intolerance=ht_40mhz_intolerance,
            valid_ssid_misuse=valid_ssid_misuse,
            valid_client_misassociation=valid_client_misassociation,
            hotspotter_attack=hotspotter_attack,
            pwsave_dos_attack=pwsave_dos_attack,
            omerta_attack=omerta_attack,
            disconnect_station=disconnect_station,
            unencrypted_valid=unencrypted_valid,
            fata_jack=fata_jack,
            risky_encryption=risky_encryption,
            fuzzed_beacon=fuzzed_beacon,
            fuzzed_probe_request=fuzzed_probe_request,
            fuzzed_probe_response=fuzzed_probe_response,
            air_jack=air_jack,
            wpa_ft_attack=wpa_ft_attack,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.wids_profile import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/wids_profile",
            )

        endpoint = "/wireless-controller/wids-profile"
        
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
        Delete wireless_controller/wids_profile object.

        Configure wireless intrusion detection system (WIDS) profiles.

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
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller/wids-profile/" + str(name)

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
        Check if wireless_controller/wids_profile object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_wids_profile.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_wids_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_wids_profile.delete(name=1)

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
        comment: str | None = None,
        sensor_mode: Literal["disable", "foreign", "both"] | None = None,
        ap_scan: Literal["disable", "enable"] | None = None,
        ap_scan_channel_list_2G_5G: str | list[str] | list[dict[str, Any]] | None = None,
        ap_scan_channel_list_6G: str | list[str] | list[dict[str, Any]] | None = None,
        ap_bgscan_period: int | None = None,
        ap_bgscan_intv: int | None = None,
        ap_bgscan_duration: int | None = None,
        ap_bgscan_idle: int | None = None,
        ap_bgscan_report_intv: int | None = None,
        ap_bgscan_disable_schedules: str | list[str] | list[dict[str, Any]] | None = None,
        ap_fgscan_report_intv: int | None = None,
        ap_scan_passive: Literal["enable", "disable"] | None = None,
        ap_scan_threshold: str | None = None,
        ap_auto_suppress: Literal["enable", "disable"] | None = None,
        wireless_bridge: Literal["enable", "disable"] | None = None,
        deauth_broadcast: Literal["enable", "disable"] | None = None,
        null_ssid_probe_resp: Literal["enable", "disable"] | None = None,
        long_duration_attack: Literal["enable", "disable"] | None = None,
        long_duration_thresh: int | None = None,
        invalid_mac_oui: Literal["enable", "disable"] | None = None,
        weak_wep_iv: Literal["enable", "disable"] | None = None,
        auth_frame_flood: Literal["enable", "disable"] | None = None,
        auth_flood_time: int | None = None,
        auth_flood_thresh: int | None = None,
        assoc_frame_flood: Literal["enable", "disable"] | None = None,
        assoc_flood_time: int | None = None,
        assoc_flood_thresh: int | None = None,
        reassoc_flood: Literal["enable", "disable"] | None = None,
        reassoc_flood_time: int | None = None,
        reassoc_flood_thresh: int | None = None,
        probe_flood: Literal["enable", "disable"] | None = None,
        probe_flood_time: int | None = None,
        probe_flood_thresh: int | None = None,
        bcn_flood: Literal["enable", "disable"] | None = None,
        bcn_flood_time: int | None = None,
        bcn_flood_thresh: int | None = None,
        rts_flood: Literal["enable", "disable"] | None = None,
        rts_flood_time: int | None = None,
        rts_flood_thresh: int | None = None,
        cts_flood: Literal["enable", "disable"] | None = None,
        cts_flood_time: int | None = None,
        cts_flood_thresh: int | None = None,
        client_flood: Literal["enable", "disable"] | None = None,
        client_flood_time: int | None = None,
        client_flood_thresh: int | None = None,
        block_ack_flood: Literal["enable", "disable"] | None = None,
        block_ack_flood_time: int | None = None,
        block_ack_flood_thresh: int | None = None,
        pspoll_flood: Literal["enable", "disable"] | None = None,
        pspoll_flood_time: int | None = None,
        pspoll_flood_thresh: int | None = None,
        netstumbler: Literal["enable", "disable"] | None = None,
        netstumbler_time: int | None = None,
        netstumbler_thresh: int | None = None,
        wellenreiter: Literal["enable", "disable"] | None = None,
        wellenreiter_time: int | None = None,
        wellenreiter_thresh: int | None = None,
        spoofed_deauth: Literal["enable", "disable"] | None = None,
        asleap_attack: Literal["enable", "disable"] | None = None,
        eapol_start_flood: Literal["enable", "disable"] | None = None,
        eapol_start_thresh: int | None = None,
        eapol_start_intv: int | None = None,
        eapol_logoff_flood: Literal["enable", "disable"] | None = None,
        eapol_logoff_thresh: int | None = None,
        eapol_logoff_intv: int | None = None,
        eapol_succ_flood: Literal["enable", "disable"] | None = None,
        eapol_succ_thresh: int | None = None,
        eapol_succ_intv: int | None = None,
        eapol_fail_flood: Literal["enable", "disable"] | None = None,
        eapol_fail_thresh: int | None = None,
        eapol_fail_intv: int | None = None,
        eapol_pre_succ_flood: Literal["enable", "disable"] | None = None,
        eapol_pre_succ_thresh: int | None = None,
        eapol_pre_succ_intv: int | None = None,
        eapol_pre_fail_flood: Literal["enable", "disable"] | None = None,
        eapol_pre_fail_thresh: int | None = None,
        eapol_pre_fail_intv: int | None = None,
        deauth_unknown_src_thresh: int | None = None,
        windows_bridge: Literal["enable", "disable"] | None = None,
        disassoc_broadcast: Literal["enable", "disable"] | None = None,
        ap_spoofing: Literal["enable", "disable"] | None = None,
        chan_based_mitm: Literal["enable", "disable"] | None = None,
        adhoc_valid_ssid: Literal["enable", "disable"] | None = None,
        adhoc_network: Literal["enable", "disable"] | None = None,
        eapol_key_overflow: Literal["enable", "disable"] | None = None,
        ap_impersonation: Literal["enable", "disable"] | None = None,
        invalid_addr_combination: Literal["enable", "disable"] | None = None,
        beacon_wrong_channel: Literal["enable", "disable"] | None = None,
        ht_greenfield: Literal["enable", "disable"] | None = None,
        overflow_ie: Literal["enable", "disable"] | None = None,
        malformed_ht_ie: Literal["enable", "disable"] | None = None,
        malformed_auth: Literal["enable", "disable"] | None = None,
        malformed_association: Literal["enable", "disable"] | None = None,
        ht_40mhz_intolerance: Literal["enable", "disable"] | None = None,
        valid_ssid_misuse: Literal["enable", "disable"] | None = None,
        valid_client_misassociation: Literal["enable", "disable"] | None = None,
        hotspotter_attack: Literal["enable", "disable"] | None = None,
        pwsave_dos_attack: Literal["enable", "disable"] | None = None,
        omerta_attack: Literal["enable", "disable"] | None = None,
        disconnect_station: Literal["enable", "disable"] | None = None,
        unencrypted_valid: Literal["enable", "disable"] | None = None,
        fata_jack: Literal["enable", "disable"] | None = None,
        risky_encryption: Literal["enable", "disable"] | None = None,
        fuzzed_beacon: Literal["enable", "disable"] | None = None,
        fuzzed_probe_request: Literal["enable", "disable"] | None = None,
        fuzzed_probe_response: Literal["enable", "disable"] | None = None,
        air_jack: Literal["enable", "disable"] | None = None,
        wpa_ft_attack: Literal["enable", "disable"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update wireless_controller/wids_profile object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            comment: Field comment
            sensor_mode: Field sensor-mode
            ap_scan: Field ap-scan
            ap_scan_channel_list_2G_5G: Field ap-scan-channel-list-2G-5G
            ap_scan_channel_list_6G: Field ap-scan-channel-list-6G
            ap_bgscan_period: Field ap-bgscan-period
            ap_bgscan_intv: Field ap-bgscan-intv
            ap_bgscan_duration: Field ap-bgscan-duration
            ap_bgscan_idle: Field ap-bgscan-idle
            ap_bgscan_report_intv: Field ap-bgscan-report-intv
            ap_bgscan_disable_schedules: Field ap-bgscan-disable-schedules
            ap_fgscan_report_intv: Field ap-fgscan-report-intv
            ap_scan_passive: Field ap-scan-passive
            ap_scan_threshold: Field ap-scan-threshold
            ap_auto_suppress: Field ap-auto-suppress
            wireless_bridge: Field wireless-bridge
            deauth_broadcast: Field deauth-broadcast
            null_ssid_probe_resp: Field null-ssid-probe-resp
            long_duration_attack: Field long-duration-attack
            long_duration_thresh: Field long-duration-thresh
            invalid_mac_oui: Field invalid-mac-oui
            weak_wep_iv: Field weak-wep-iv
            auth_frame_flood: Field auth-frame-flood
            auth_flood_time: Field auth-flood-time
            auth_flood_thresh: Field auth-flood-thresh
            assoc_frame_flood: Field assoc-frame-flood
            assoc_flood_time: Field assoc-flood-time
            assoc_flood_thresh: Field assoc-flood-thresh
            reassoc_flood: Field reassoc-flood
            reassoc_flood_time: Field reassoc-flood-time
            reassoc_flood_thresh: Field reassoc-flood-thresh
            probe_flood: Field probe-flood
            probe_flood_time: Field probe-flood-time
            probe_flood_thresh: Field probe-flood-thresh
            bcn_flood: Field bcn-flood
            bcn_flood_time: Field bcn-flood-time
            bcn_flood_thresh: Field bcn-flood-thresh
            rts_flood: Field rts-flood
            rts_flood_time: Field rts-flood-time
            rts_flood_thresh: Field rts-flood-thresh
            cts_flood: Field cts-flood
            cts_flood_time: Field cts-flood-time
            cts_flood_thresh: Field cts-flood-thresh
            client_flood: Field client-flood
            client_flood_time: Field client-flood-time
            client_flood_thresh: Field client-flood-thresh
            block_ack_flood: Field block_ack-flood
            block_ack_flood_time: Field block_ack-flood-time
            block_ack_flood_thresh: Field block_ack-flood-thresh
            pspoll_flood: Field pspoll-flood
            pspoll_flood_time: Field pspoll-flood-time
            pspoll_flood_thresh: Field pspoll-flood-thresh
            netstumbler: Field netstumbler
            netstumbler_time: Field netstumbler-time
            netstumbler_thresh: Field netstumbler-thresh
            wellenreiter: Field wellenreiter
            wellenreiter_time: Field wellenreiter-time
            wellenreiter_thresh: Field wellenreiter-thresh
            spoofed_deauth: Field spoofed-deauth
            asleap_attack: Field asleap-attack
            eapol_start_flood: Field eapol-start-flood
            eapol_start_thresh: Field eapol-start-thresh
            eapol_start_intv: Field eapol-start-intv
            eapol_logoff_flood: Field eapol-logoff-flood
            eapol_logoff_thresh: Field eapol-logoff-thresh
            eapol_logoff_intv: Field eapol-logoff-intv
            eapol_succ_flood: Field eapol-succ-flood
            eapol_succ_thresh: Field eapol-succ-thresh
            eapol_succ_intv: Field eapol-succ-intv
            eapol_fail_flood: Field eapol-fail-flood
            eapol_fail_thresh: Field eapol-fail-thresh
            eapol_fail_intv: Field eapol-fail-intv
            eapol_pre_succ_flood: Field eapol-pre-succ-flood
            eapol_pre_succ_thresh: Field eapol-pre-succ-thresh
            eapol_pre_succ_intv: Field eapol-pre-succ-intv
            eapol_pre_fail_flood: Field eapol-pre-fail-flood
            eapol_pre_fail_thresh: Field eapol-pre-fail-thresh
            eapol_pre_fail_intv: Field eapol-pre-fail-intv
            deauth_unknown_src_thresh: Field deauth-unknown-src-thresh
            windows_bridge: Field windows-bridge
            disassoc_broadcast: Field disassoc-broadcast
            ap_spoofing: Field ap-spoofing
            chan_based_mitm: Field chan-based-mitm
            adhoc_valid_ssid: Field adhoc-valid-ssid
            adhoc_network: Field adhoc-network
            eapol_key_overflow: Field eapol-key-overflow
            ap_impersonation: Field ap-impersonation
            invalid_addr_combination: Field invalid-addr-combination
            beacon_wrong_channel: Field beacon-wrong-channel
            ht_greenfield: Field ht-greenfield
            overflow_ie: Field overflow-ie
            malformed_ht_ie: Field malformed-ht-ie
            malformed_auth: Field malformed-auth
            malformed_association: Field malformed-association
            ht_40mhz_intolerance: Field ht-40mhz-intolerance
            valid_ssid_misuse: Field valid-ssid-misuse
            valid_client_misassociation: Field valid-client-misassociation
            hotspotter_attack: Field hotspotter-attack
            pwsave_dos_attack: Field pwsave-dos-attack
            omerta_attack: Field omerta-attack
            disconnect_station: Field disconnect-station
            unencrypted_valid: Field unencrypted-valid
            fata_jack: Field fata-jack
            risky_encryption: Field risky-encryption
            fuzzed_beacon: Field fuzzed-beacon
            fuzzed_probe_request: Field fuzzed-probe-request
            fuzzed_probe_response: Field fuzzed-probe-response
            air_jack: Field air-jack
            wpa_ft_attack: Field wpa-ft-attack
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_wids_profile.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_wids_profile.set(payload_dict=obj_data)
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
            sensor_mode=sensor_mode,
            ap_scan=ap_scan,
            ap_scan_channel_list_2G_5G=ap_scan_channel_list_2G_5G,
            ap_scan_channel_list_6G=ap_scan_channel_list_6G,
            ap_bgscan_period=ap_bgscan_period,
            ap_bgscan_intv=ap_bgscan_intv,
            ap_bgscan_duration=ap_bgscan_duration,
            ap_bgscan_idle=ap_bgscan_idle,
            ap_bgscan_report_intv=ap_bgscan_report_intv,
            ap_bgscan_disable_schedules=ap_bgscan_disable_schedules,
            ap_fgscan_report_intv=ap_fgscan_report_intv,
            ap_scan_passive=ap_scan_passive,
            ap_scan_threshold=ap_scan_threshold,
            ap_auto_suppress=ap_auto_suppress,
            wireless_bridge=wireless_bridge,
            deauth_broadcast=deauth_broadcast,
            null_ssid_probe_resp=null_ssid_probe_resp,
            long_duration_attack=long_duration_attack,
            long_duration_thresh=long_duration_thresh,
            invalid_mac_oui=invalid_mac_oui,
            weak_wep_iv=weak_wep_iv,
            auth_frame_flood=auth_frame_flood,
            auth_flood_time=auth_flood_time,
            auth_flood_thresh=auth_flood_thresh,
            assoc_frame_flood=assoc_frame_flood,
            assoc_flood_time=assoc_flood_time,
            assoc_flood_thresh=assoc_flood_thresh,
            reassoc_flood=reassoc_flood,
            reassoc_flood_time=reassoc_flood_time,
            reassoc_flood_thresh=reassoc_flood_thresh,
            probe_flood=probe_flood,
            probe_flood_time=probe_flood_time,
            probe_flood_thresh=probe_flood_thresh,
            bcn_flood=bcn_flood,
            bcn_flood_time=bcn_flood_time,
            bcn_flood_thresh=bcn_flood_thresh,
            rts_flood=rts_flood,
            rts_flood_time=rts_flood_time,
            rts_flood_thresh=rts_flood_thresh,
            cts_flood=cts_flood,
            cts_flood_time=cts_flood_time,
            cts_flood_thresh=cts_flood_thresh,
            client_flood=client_flood,
            client_flood_time=client_flood_time,
            client_flood_thresh=client_flood_thresh,
            block_ack_flood=block_ack_flood,
            block_ack_flood_time=block_ack_flood_time,
            block_ack_flood_thresh=block_ack_flood_thresh,
            pspoll_flood=pspoll_flood,
            pspoll_flood_time=pspoll_flood_time,
            pspoll_flood_thresh=pspoll_flood_thresh,
            netstumbler=netstumbler,
            netstumbler_time=netstumbler_time,
            netstumbler_thresh=netstumbler_thresh,
            wellenreiter=wellenreiter,
            wellenreiter_time=wellenreiter_time,
            wellenreiter_thresh=wellenreiter_thresh,
            spoofed_deauth=spoofed_deauth,
            asleap_attack=asleap_attack,
            eapol_start_flood=eapol_start_flood,
            eapol_start_thresh=eapol_start_thresh,
            eapol_start_intv=eapol_start_intv,
            eapol_logoff_flood=eapol_logoff_flood,
            eapol_logoff_thresh=eapol_logoff_thresh,
            eapol_logoff_intv=eapol_logoff_intv,
            eapol_succ_flood=eapol_succ_flood,
            eapol_succ_thresh=eapol_succ_thresh,
            eapol_succ_intv=eapol_succ_intv,
            eapol_fail_flood=eapol_fail_flood,
            eapol_fail_thresh=eapol_fail_thresh,
            eapol_fail_intv=eapol_fail_intv,
            eapol_pre_succ_flood=eapol_pre_succ_flood,
            eapol_pre_succ_thresh=eapol_pre_succ_thresh,
            eapol_pre_succ_intv=eapol_pre_succ_intv,
            eapol_pre_fail_flood=eapol_pre_fail_flood,
            eapol_pre_fail_thresh=eapol_pre_fail_thresh,
            eapol_pre_fail_intv=eapol_pre_fail_intv,
            deauth_unknown_src_thresh=deauth_unknown_src_thresh,
            windows_bridge=windows_bridge,
            disassoc_broadcast=disassoc_broadcast,
            ap_spoofing=ap_spoofing,
            chan_based_mitm=chan_based_mitm,
            adhoc_valid_ssid=adhoc_valid_ssid,
            adhoc_network=adhoc_network,
            eapol_key_overflow=eapol_key_overflow,
            ap_impersonation=ap_impersonation,
            invalid_addr_combination=invalid_addr_combination,
            beacon_wrong_channel=beacon_wrong_channel,
            ht_greenfield=ht_greenfield,
            overflow_ie=overflow_ie,
            malformed_ht_ie=malformed_ht_ie,
            malformed_auth=malformed_auth,
            malformed_association=malformed_association,
            ht_40mhz_intolerance=ht_40mhz_intolerance,
            valid_ssid_misuse=valid_ssid_misuse,
            valid_client_misassociation=valid_client_misassociation,
            hotspotter_attack=hotspotter_attack,
            pwsave_dos_attack=pwsave_dos_attack,
            omerta_attack=omerta_attack,
            disconnect_station=disconnect_station,
            unencrypted_valid=unencrypted_valid,
            fata_jack=fata_jack,
            risky_encryption=risky_encryption,
            fuzzed_beacon=fuzzed_beacon,
            fuzzed_probe_request=fuzzed_probe_request,
            fuzzed_probe_response=fuzzed_probe_response,
            air_jack=air_jack,
            wpa_ft_attack=wpa_ft_attack,
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
        Move wireless_controller/wids_profile object to a new position.
        
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
            >>> fgt.api.cmdb.wireless_controller_wids_profile.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller/wids-profile",
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
        Clone wireless_controller/wids_profile object.
        
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
            >>> fgt.api.cmdb.wireless_controller_wids_profile.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller/wids-profile",
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
        Check if wireless_controller/wids_profile object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.wireless_controller_wids_profile.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_wids_profile.post(payload_dict=data)
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

