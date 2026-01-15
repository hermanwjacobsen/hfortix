"""
FortiOS CMDB - Wireless_controller vap

Configuration endpoint for managing cmdb wireless_controller/vap objects.

API Endpoints:
    GET    /cmdb/wireless_controller/vap
    POST   /cmdb/wireless_controller/vap
    PUT    /cmdb/wireless_controller/vap/{identifier}
    DELETE /cmdb/wireless_controller/vap/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller_vap.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.wireless_controller_vap.post(
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

class Vap(CRUDEndpoint, MetadataMixin):
    """Vap Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "vap"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "radius_mac_auth_usergroups": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "usergroup": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "selected_usergroups": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "schedule": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "vlan_name": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "vlan_pool": {
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
        """Initialize Vap endpoint."""
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
        Retrieve wireless_controller/vap configuration.

        Configure Virtual Access Points (VAPs).

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
            >>> # Get all wireless_controller/vap objects
            >>> result = fgt.api.cmdb.wireless_controller_vap.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific wireless_controller/vap by name
            >>> result = fgt.api.cmdb.wireless_controller_vap.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.wireless_controller_vap.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.wireless_controller_vap.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.wireless_controller_vap.get_schema()

        See Also:
            - post(): Create new wireless_controller/vap object
            - put(): Update existing wireless_controller/vap object
            - delete(): Remove wireless_controller/vap object
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
            endpoint = "/wireless-controller/vap/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/wireless-controller/vap"
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
            >>> schema = fgt.api.cmdb.wireless_controller_vap.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.wireless_controller_vap.get_schema(format="json-schema")
        
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
        pre_auth: Literal["enable", "disable"] | None = None,
        external_pre_auth: Literal["enable", "disable"] | None = None,
        mesh_backhaul: Literal["enable", "disable"] | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: Literal["enable", "disable"] | None = None,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = None,
        pmf: Literal["disable", "enable", "optional"] | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: Literal["disable", "enable"] | None = None,
        okc: Literal["disable", "enable"] | None = None,
        mbo: Literal["disable", "enable"] | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = None,
        x80211k: Literal["disable", "enable"] | None = None,
        x80211v: Literal["disable", "enable"] | None = None,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = None,
        fast_bss_transition: Literal["disable", "enable"] | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: Literal["disable", "enable"] | None = None,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = None,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = None,
        owe_transition: Literal["disable", "enable"] | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = None,
        eapol_key_retries: Literal["disable", "enable"] | None = None,
        tkip_counter_measure: Literal["enable", "disable"] | None = None,
        external_web: str | None = None,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_case: Literal["uppercase", "lowercase"] | None = None,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = None,
        mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_mac_auth: Literal["enable", "disable"] | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        auth: Literal["radius", "usergroup"] | None = None,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = None,
        keyindex: int | None = None,
        key: Any | None = None,
        passphrase: Any | None = None,
        sae_password: Any | None = None,
        sae_h2e_only: Literal["enable", "disable"] | None = None,
        sae_hnp_only: Literal["enable", "disable"] | None = None,
        sae_pk: Literal["enable", "disable"] | None = None,
        sae_private_key: str | None = None,
        akm24_only: Literal["disable", "enable"] | None = None,
        radius_server: str | None = None,
        nas_filter_rule: Literal["enable", "disable"] | None = None,
        domain_name_stripping: Literal["disable", "enable"] | None = None,
        mlo: Literal["disable", "enable"] | None = None,
        local_standalone: Literal["enable", "disable"] | None = None,
        local_standalone_nat: Literal["enable", "disable"] | None = None,
        ip: Any | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: Literal["enable", "disable"] | None = None,
        local_standalone_dns_ip: str | list[str] | None = None,
        local_lan_partition: Literal["enable", "disable"] | None = None,
        local_bridging: Literal["enable", "disable"] | None = None,
        local_lan: Literal["allow", "deny"] | None = None,
        local_authentication: Literal["enable", "disable"] | None = None,
        usergroup: str | list[str] | list[dict[str, Any]] | None = None,
        captive_portal: Literal["enable", "disable"] | None = None,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: str | None = None,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = None,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: Literal["enable", "disable"] | None = None,
        schedule: str | list[str] | list[dict[str, Any]] | None = None,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = None,
        high_efficiency: Literal["enable", "disable"] | None = None,
        target_wake_time: Literal["enable", "disable"] | None = None,
        port_macauth: Literal["disable", "radius", "address-group"] | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: Literal["enable", "disable"] | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: Literal["enable", "disable"] | None = None,
        nac: Literal["enable", "disable"] | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: Literal["enable", "disable"] | None = None,
        dynamic_vlan: Literal["enable", "disable"] | None = None,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = None,
        multicast_enhance: Literal["enable", "disable"] | None = None,
        igmp_snooping: Literal["enable", "disable"] | None = None,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = None,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = None,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: Literal["enable", "disable"] | None = None,
        probe_resp_suppression: Literal["enable", "disable"] | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: Literal["enable", "disable"] | None = None,
        quarantine: Literal["enable", "disable"] | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = None,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = None,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = None,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = None,
        ptk_rekey: Literal["enable", "disable"] | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: Literal["enable", "disable"] | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: Literal["enable", "disable"] | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = None,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = None,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = None,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        utm_log: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = None,
        address_group: str | None = None,
        address_group_policy: Literal["disable", "allow", "deny"] | None = None,
        sticky_client_remove: Literal["enable", "disable"] | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = None,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = None,
        osen: Literal["enable", "disable"] | None = None,
        application_detection_engine: Literal["enable", "disable"] | None = None,
        application_dscp_marking: Literal["enable", "disable"] | None = None,
        application_report_intv: int | None = None,
        l3_roaming: Literal["enable", "disable"] | None = None,
        l3_roaming_mode: Literal["direct", "indirect"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing wireless_controller/vap object.

        Configure Virtual Access Points (VAPs).

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: Virtual AP name.
            pre_auth: Enable/disable pre-authentication, where supported by clients (default = enable).
            external_pre_auth: Enable/disable pre-authentication with external APs not managed by the FortiGate (default = disable).
            mesh_backhaul: Enable/disable using this VAP as a WiFi mesh backhaul (default = disable). This entry is only available when security is set to a WPA type or open.
            atf_weight: Airtime weight in percentage (default = 20).
            max_clients: Maximum number of clients that can connect simultaneously to the VAP (default = 0, meaning no limitation).
            max_clients_ap: Maximum number of clients that can connect simultaneously to the VAP per AP radio (default = 0, meaning no limitation).
            ssid: IEEE 802.11 service set identifier (SSID) for the wireless interface. Users who wish to use the wireless network must configure their computers to access this SSID name.
            broadcast_ssid: Enable/disable broadcasting the SSID (default = enable).
            security: Security mode for the wireless interface (default = wpa2-only-personal).
            pmf: Protected Management Frames (PMF) support (default = disable).
            pmf_assoc_comeback_timeout: Protected Management Frames (PMF) comeback maximum timeout (1-20 sec).
            pmf_sa_query_retry_timeout: Protected Management Frames (PMF) SA query retry timeout interval (1 - 5 100s of msec).
            beacon_protection: Enable/disable beacon protection support (default = disable).
            okc: Enable/disable Opportunistic Key Caching (OKC) (default = enable).
            mbo: Enable/disable Multiband Operation (default = disable).
            gas_comeback_delay: GAS comeback delay (0 or 100 - 10000 milliseconds, default = 500).
            gas_fragmentation_limit: GAS fragmentation limit (512 - 4096, default = 1024).
            mbo_cell_data_conn_pref: MBO cell data connection preference (0, 1, or 255, default = 1).
            x80211k: Enable/disable 802.11k assisted roaming (default = enable).
            x80211v: Enable/disable 802.11v assisted roaming (default = enable).
            neighbor_report_dual_band: Enable/disable dual-band neighbor report (default = disable).
            fast_bss_transition: Enable/disable 802.11r Fast BSS Transition (FT) (default = disable).
            ft_mobility_domain: Mobility domain identifier in FT (1 - 65535, default = 1000).
            ft_r0_key_lifetime: Lifetime of the PMK-R0 key in FT, 1-65535 minutes.
            ft_over_ds: Enable/disable FT over the Distribution System (DS).
            sae_groups: SAE-Groups.
            owe_groups: OWE-Groups.
            owe_transition: Enable/disable OWE transition mode support.
            owe_transition_ssid: OWE transition mode peer SSID.
            additional_akms: Additional AKMs.
            eapol_key_retries: Enable/disable retransmission of EAPOL-Key frames (message 3/4 and group message 1/2) (default = enable).
            tkip_counter_measure: Enable/disable TKIP counter measure.
            external_web: URL of external authentication web server.
            external_web_format: URL query parameter detection (default = auto-detect).
            external_logout: URL of external authentication logout server.
            mac_username_delimiter: MAC authentication username delimiter (default = hyphen).
            mac_password_delimiter: MAC authentication password delimiter (default = hyphen).
            mac_calling_station_delimiter: MAC calling station delimiter (default = hyphen).
            mac_called_station_delimiter: MAC called station delimiter (default = hyphen).
            mac_case: MAC case (default = uppercase).
            called_station_id_type: The format type of RADIUS attribute Called-Station-Id (default = mac).
            mac_auth_bypass: Enable/disable MAC authentication bypass.
            radius_mac_auth: Enable/disable RADIUS-based MAC authentication of clients (default = disable).
            radius_mac_auth_server: RADIUS-based MAC authentication server.
            radius_mac_auth_block_interval: Don't send RADIUS MAC auth request again if the client has been rejected within specific interval (0 or 30 - 864000 seconds, default = 0, 0 to disable blocking).
            radius_mac_mpsk_auth: Enable/disable RADIUS-based MAC authentication of clients for MPSK authentication (default = disable).
            radius_mac_mpsk_timeout: RADIUS MAC MPSK cache timeout interval (0 or 300 - 864000, default = 86400, 0 to disable caching).
            radius_mac_auth_usergroups: Selective user groups that are permitted for RADIUS mac authentication.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            auth: Authentication protocol.
            encrypt: Encryption protocol to use (only available when security is set to a WPA type).
            keyindex: WEP key index (1 - 4).
            key: WEP Key.
            passphrase: WPA pre-shared key (PSK) to be used to authenticate WiFi users.
            sae_password: WPA3 SAE password to be used to authenticate WiFi users.
            sae_h2e_only: Use hash-to-element-only mechanism for PWE derivation (default = disable).
            sae_hnp_only: Use hunting-and-pecking-only mechanism for PWE derivation (default = disable).
            sae_pk: Enable/disable WPA3 SAE-PK (default = disable).
            sae_private_key: Private key used for WPA3 SAE-PK authentication.
            akm24_only: WPA3 SAE using group-dependent hash only (default = disable).
            radius_server: RADIUS server to be used to authenticate WiFi users.
            nas_filter_rule: Enable/disable NAS filter rule support (default = disable).
            domain_name_stripping: Enable/disable stripping domain name from identity (default = disable).
            mlo: Enable/disable WiFi7 Multi-Link-Operation (default = disable).
            local_standalone: Enable/disable AP local standalone (default = disable).
            local_standalone_nat: Enable/disable AP local standalone NAT mode.
            ip: IP address and subnet mask for the local standalone NAT subnet.
            dhcp_lease_time: DHCP lease time in seconds for NAT IP address.
            local_standalone_dns: Enable/disable AP local standalone DNS.
            local_standalone_dns_ip: IPv4 addresses for the local standalone DNS.
            local_lan_partition: Enable/disable segregating client traffic to local LAN side (default = disable).
            local_bridging: Enable/disable bridging of wireless and Ethernet interfaces on the FortiAP (default = disable).
            local_lan: Allow/deny traffic destined for a Class A, B, or C private IP address (default = allow).
            local_authentication: Enable/disable AP local authentication.
            usergroup: Firewall user group to be used to authenticate WiFi users.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            captive_portal: Enable/disable captive portal.
            captive_network_assistant_bypass: Enable/disable Captive Network Assistant bypass.
            portal_message_override_group: Replacement message group for this VAP (only available when security is set to a captive portal type).
            portal_message_overrides: Individual message overrides.
            portal_type: Captive portal functionality. Configure how the captive portal authenticates users and whether it includes a disclaimer.
            selected_usergroups: Selective user groups that are permitted to authenticate.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            security_exempt_list: Optional security exempt list for captive portal authentication.
            security_redirect_url: Optional URL for redirecting users after they pass captive portal authentication.
            auth_cert: HTTPS server certificate.
            auth_portal_addr: Address of captive portal.
            intra_vap_privacy: Enable/disable blocking communication between clients on the same SSID (called intra-SSID privacy) (default = disable).
            schedule: Firewall schedules for enabling this VAP on the FortiAP. This VAP will be enabled when at least one of the schedules is valid. Separate multiple schedule names with a space.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ldpc: VAP low-density parity-check (LDPC) coding configuration.
            high_efficiency: Enable/disable 802.11ax high efficiency (default = enable).
            target_wake_time: Enable/disable 802.11ax target wake time (default = enable).
            port_macauth: Enable/disable LAN port MAC authentication (default = disable).
            port_macauth_timeout: LAN port MAC authentication idle timeout value (default = 600 sec).
            port_macauth_reauth_timeout: LAN port MAC authentication re-authentication timeout value (default = 7200 sec).
            bss_color_partial: Enable/disable 802.11ax partial BSS color (default = enable).
            mpsk_profile: MPSK profile name.
            split_tunneling: Enable/disable split tunneling (default = disable).
            nac: Enable/disable network access control.
            nac_profile: NAC profile name.
            vlanid: Optional VLAN ID.
            vlan_auto: Enable/disable automatic management of SSID VLAN interface.
            dynamic_vlan: Enable/disable dynamic VLAN assignment.
            captive_portal_fw_accounting: Enable/disable RADIUS accounting for captive portal firewall authentication session.
            captive_portal_ac_name: Local-bridging captive portal ac-name.
            captive_portal_auth_timeout: Hard timeout - AP will always clear the session after timeout regardless of traffic (0 - 864000 sec, default = 0).
            multicast_rate: Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0).
            multicast_enhance: Enable/disable converting multicast to unicast to improve performance (default = disable).
            igmp_snooping: Enable/disable IGMP snooping.
            dhcp_address_enforcement: Enable/disable DHCP address enforcement (default = disable).
            broadcast_suppression: Optional suppression of broadcast messages. For example, you can keep DHCP messages, ARP broadcasts, and so on off of the wireless network.
            ipv6_rules: Optional rules of IPv6 packets. For example, you can keep RA, RS and so on off of the wireless network.
            me_disable_thresh: Disable multicast enhancement when this many clients are receiving multicast traffic.
            mu_mimo: Enable/disable Multi-user MIMO (default = enable).
            probe_resp_suppression: Enable/disable probe response suppression (to ignore weak signals) (default = disable).
            probe_resp_threshold: Minimum signal level/threshold in dBm required for the AP response to probe requests (-95 to -20, default = -80).
            radio_sensitivity: Enable/disable software radio sensitivity (to ignore weak signals) (default = disable).
            quarantine: Enable/disable station quarantine (default = disable).
            radio_5g_threshold: Minimum signal level/threshold in dBm required for the AP response to receive a packet in 5G band(-95 to -20, default = -76).
            radio_2g_threshold: Minimum signal level/threshold in dBm required for the AP response to receive a packet in 2.4G band (-95 to -20, default = -79).
            vlan_name: Table for mapping VLAN name to VLAN ID.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            vlan_pooling: Enable/disable VLAN pooling, to allow grouping of multiple wireless controller VLANs into VLAN pools (default = disable). When set to wtp-group, VLAN pooling occurs with VLAN assignment by wtp-group.
            vlan_pool: VLAN pool.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            dhcp_option43_insertion: Enable/disable insertion of DHCP option 43 (default = enable).
            dhcp_option82_insertion: Enable/disable DHCP option 82 insert (default = disable).
            dhcp_option82_circuit_id_insertion: Enable/disable DHCP option 82 circuit-id insert (default = disable).
            dhcp_option82_remote_id_insertion: Enable/disable DHCP option 82 remote-id insert (default = disable).
            ptk_rekey: Enable/disable PTK rekey for WPA-Enterprise security.
            ptk_rekey_intv: PTK rekey interval (600 - 864000 sec, default = 86400).
            gtk_rekey: Enable/disable GTK rekey for WPA security.
            gtk_rekey_intv: GTK rekey interval (600 - 864000 sec, default = 86400).
            eap_reauth: Enable/disable EAP re-authentication for WPA-Enterprise security.
            eap_reauth_intv: EAP re-authentication interval (1800 - 864000 sec, default = 86400).
            roaming_acct_interim_update: Enable/disable using accounting interim update instead of accounting start/stop on roaming for WPA-Enterprise security.
            qos_profile: Quality of service profile name.
            hotspot20_profile: Hotspot 2.0 profile name.
            access_control_list: Profile name for access-control-list.
            primary_wag_profile: Primary wireless access gateway profile name.
            secondary_wag_profile: Secondary wireless access gateway profile name.
            tunnel_echo_interval: The time interval to send echo to both primary and secondary tunnel peers (1 - 65535 sec, default = 300).
            tunnel_fallback_interval: The time interval for secondary tunnel to fall back to primary tunnel (0 - 65535 sec, default = 7200).
            rates_11a: Allowed data rates for 802.11a.
            rates_11bg: Allowed data rates for 802.11b/g.
            rates_11n_ss12: Allowed data rates for 802.11n with 1 or 2 spatial streams.
            rates_11n_ss34: Allowed data rates for 802.11n with 3 or 4 spatial streams.
            rates_11ac_mcs_map: Comma separated list of max supported VHT MCS for spatial streams 1 through 8.
            rates_11ax_mcs_map: Comma separated list of max supported HE MCS for spatial streams 1 through 8.
            rates_11be_mcs_map: Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 20MHz/40MHz/80MHz bandwidth.
            rates_11be_mcs_map_160: Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 160MHz bandwidth.
            rates_11be_mcs_map_320: Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 320MHz bandwidth.
            utm_profile: UTM profile name.
            utm_status: Enable to add one or more security profiles (AV, IPS, etc.) to the VAP.
            utm_log: Enable/disable UTM logging.
            ips_sensor: IPS sensor name.
            application_list: Application control list name.
            antivirus_profile: AntiVirus profile name.
            webfilter_profile: WebFilter profile name.
            scan_botnet_connections: Block or monitor connections to Botnet servers or disable Botnet scanning.
            address_group: Firewall Address Group Name.
            address_group_policy: Configure MAC address filtering policy for MAC addresses that are in the address-group.
            sticky_client_remove: Enable/disable sticky client remove to maintain good signal level clients in SSID (default = disable).
            sticky_client_threshold_5g: Minimum signal level/threshold in dBm required for the 5G client to be serviced by the AP (-95 to -20, default = -76).
            sticky_client_threshold_2g: Minimum signal level/threshold in dBm required for the 2G client to be serviced by the AP (-95 to -20, default = -79).
            sticky_client_threshold_6g: Minimum signal level/threshold in dBm required for the 6G client to be serviced by the AP (-95 to -20, default = -76).
            bstm_rssi_disassoc_timer: Time interval for client to voluntarily leave AP before forcing a disassociation due to low RSSI (0 to 2000, default = 200).
            bstm_load_balancing_disassoc_timer: Time interval for client to voluntarily leave AP before forcing a disassociation due to AP load-balancing (0 to 30, default = 10).
            bstm_disassociation_imminent: Enable/disable forcing of disassociation after the BSTM request timer has been reached (default = enable).
            beacon_advertising: Fortinet beacon advertising IE data   (default = empty).
            osen: Enable/disable OSEN as part of key management (default = disable).
            application_detection_engine: Enable/disable application detection engine (default = disable).
            application_dscp_marking: Enable/disable application attribute based DSCP marking (default = disable).
            application_report_intv: Application report interval (30 - 864000 sec, default = 120).
            l3_roaming: Enable/disable layer 3 roaming (default = disable).
            l3_roaming_mode: Select the way that layer 3 roaming traffic is passed (default = direct).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.wireless_controller_vap.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_vap.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if radius_mac_auth_usergroups is not None:
            radius_mac_auth_usergroups = normalize_table_field(
                radius_mac_auth_usergroups,
                mkey="name",
                required_fields=['name'],
                field_name="radius_mac_auth_usergroups",
                example="[{'name': 'value'}]",
            )
        if usergroup is not None:
            usergroup = normalize_table_field(
                usergroup,
                mkey="name",
                required_fields=['name'],
                field_name="usergroup",
                example="[{'name': 'value'}]",
            )
        if selected_usergroups is not None:
            selected_usergroups = normalize_table_field(
                selected_usergroups,
                mkey="name",
                required_fields=['name'],
                field_name="selected_usergroups",
                example="[{'name': 'value'}]",
            )
        if schedule is not None:
            schedule = normalize_table_field(
                schedule,
                mkey="name",
                required_fields=['name'],
                field_name="schedule",
                example="[{'name': 'value'}]",
            )
        if vlan_name is not None:
            vlan_name = normalize_table_field(
                vlan_name,
                mkey="name",
                required_fields=['name'],
                field_name="vlan_name",
                example="[{'name': 'value'}]",
            )
        if vlan_pool is not None:
            vlan_pool = normalize_table_field(
                vlan_pool,
                mkey="id",
                required_fields=['id'],
                field_name="vlan_pool",
                example="[{'id': 1}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            pre_auth=pre_auth,
            external_pre_auth=external_pre_auth,
            mesh_backhaul=mesh_backhaul,
            atf_weight=atf_weight,
            max_clients=max_clients,
            max_clients_ap=max_clients_ap,
            ssid=ssid,
            broadcast_ssid=broadcast_ssid,
            security=security,
            pmf=pmf,
            pmf_assoc_comeback_timeout=pmf_assoc_comeback_timeout,
            pmf_sa_query_retry_timeout=pmf_sa_query_retry_timeout,
            beacon_protection=beacon_protection,
            okc=okc,
            mbo=mbo,
            gas_comeback_delay=gas_comeback_delay,
            gas_fragmentation_limit=gas_fragmentation_limit,
            mbo_cell_data_conn_pref=mbo_cell_data_conn_pref,
            x80211k=x80211k,
            x80211v=x80211v,
            neighbor_report_dual_band=neighbor_report_dual_band,
            fast_bss_transition=fast_bss_transition,
            ft_mobility_domain=ft_mobility_domain,
            ft_r0_key_lifetime=ft_r0_key_lifetime,
            ft_over_ds=ft_over_ds,
            sae_groups=sae_groups,
            owe_groups=owe_groups,
            owe_transition=owe_transition,
            owe_transition_ssid=owe_transition_ssid,
            additional_akms=additional_akms,
            eapol_key_retries=eapol_key_retries,
            tkip_counter_measure=tkip_counter_measure,
            external_web=external_web,
            external_web_format=external_web_format,
            external_logout=external_logout,
            mac_username_delimiter=mac_username_delimiter,
            mac_password_delimiter=mac_password_delimiter,
            mac_calling_station_delimiter=mac_calling_station_delimiter,
            mac_called_station_delimiter=mac_called_station_delimiter,
            mac_case=mac_case,
            called_station_id_type=called_station_id_type,
            mac_auth_bypass=mac_auth_bypass,
            radius_mac_auth=radius_mac_auth,
            radius_mac_auth_server=radius_mac_auth_server,
            radius_mac_auth_block_interval=radius_mac_auth_block_interval,
            radius_mac_mpsk_auth=radius_mac_mpsk_auth,
            radius_mac_mpsk_timeout=radius_mac_mpsk_timeout,
            radius_mac_auth_usergroups=radius_mac_auth_usergroups,
            auth=auth,
            encrypt=encrypt,
            keyindex=keyindex,
            key=key,
            passphrase=passphrase,
            sae_password=sae_password,
            sae_h2e_only=sae_h2e_only,
            sae_hnp_only=sae_hnp_only,
            sae_pk=sae_pk,
            sae_private_key=sae_private_key,
            akm24_only=akm24_only,
            radius_server=radius_server,
            nas_filter_rule=nas_filter_rule,
            domain_name_stripping=domain_name_stripping,
            mlo=mlo,
            local_standalone=local_standalone,
            local_standalone_nat=local_standalone_nat,
            ip=ip,
            dhcp_lease_time=dhcp_lease_time,
            local_standalone_dns=local_standalone_dns,
            local_standalone_dns_ip=local_standalone_dns_ip,
            local_lan_partition=local_lan_partition,
            local_bridging=local_bridging,
            local_lan=local_lan,
            local_authentication=local_authentication,
            usergroup=usergroup,
            captive_portal=captive_portal,
            captive_network_assistant_bypass=captive_network_assistant_bypass,
            portal_message_override_group=portal_message_override_group,
            portal_message_overrides=portal_message_overrides,
            portal_type=portal_type,
            selected_usergroups=selected_usergroups,
            security_exempt_list=security_exempt_list,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            intra_vap_privacy=intra_vap_privacy,
            schedule=schedule,
            ldpc=ldpc,
            high_efficiency=high_efficiency,
            target_wake_time=target_wake_time,
            port_macauth=port_macauth,
            port_macauth_timeout=port_macauth_timeout,
            port_macauth_reauth_timeout=port_macauth_reauth_timeout,
            bss_color_partial=bss_color_partial,
            mpsk_profile=mpsk_profile,
            split_tunneling=split_tunneling,
            nac=nac,
            nac_profile=nac_profile,
            vlanid=vlanid,
            vlan_auto=vlan_auto,
            dynamic_vlan=dynamic_vlan,
            captive_portal_fw_accounting=captive_portal_fw_accounting,
            captive_portal_ac_name=captive_portal_ac_name,
            captive_portal_auth_timeout=captive_portal_auth_timeout,
            multicast_rate=multicast_rate,
            multicast_enhance=multicast_enhance,
            igmp_snooping=igmp_snooping,
            dhcp_address_enforcement=dhcp_address_enforcement,
            broadcast_suppression=broadcast_suppression,
            ipv6_rules=ipv6_rules,
            me_disable_thresh=me_disable_thresh,
            mu_mimo=mu_mimo,
            probe_resp_suppression=probe_resp_suppression,
            probe_resp_threshold=probe_resp_threshold,
            radio_sensitivity=radio_sensitivity,
            quarantine=quarantine,
            radio_5g_threshold=radio_5g_threshold,
            radio_2g_threshold=radio_2g_threshold,
            vlan_name=vlan_name,
            vlan_pooling=vlan_pooling,
            vlan_pool=vlan_pool,
            dhcp_option43_insertion=dhcp_option43_insertion,
            dhcp_option82_insertion=dhcp_option82_insertion,
            dhcp_option82_circuit_id_insertion=dhcp_option82_circuit_id_insertion,
            dhcp_option82_remote_id_insertion=dhcp_option82_remote_id_insertion,
            ptk_rekey=ptk_rekey,
            ptk_rekey_intv=ptk_rekey_intv,
            gtk_rekey=gtk_rekey,
            gtk_rekey_intv=gtk_rekey_intv,
            eap_reauth=eap_reauth,
            eap_reauth_intv=eap_reauth_intv,
            roaming_acct_interim_update=roaming_acct_interim_update,
            qos_profile=qos_profile,
            hotspot20_profile=hotspot20_profile,
            access_control_list=access_control_list,
            primary_wag_profile=primary_wag_profile,
            secondary_wag_profile=secondary_wag_profile,
            tunnel_echo_interval=tunnel_echo_interval,
            tunnel_fallback_interval=tunnel_fallback_interval,
            rates_11a=rates_11a,
            rates_11bg=rates_11bg,
            rates_11n_ss12=rates_11n_ss12,
            rates_11n_ss34=rates_11n_ss34,
            rates_11ac_mcs_map=rates_11ac_mcs_map,
            rates_11ax_mcs_map=rates_11ax_mcs_map,
            rates_11be_mcs_map=rates_11be_mcs_map,
            rates_11be_mcs_map_160=rates_11be_mcs_map_160,
            rates_11be_mcs_map_320=rates_11be_mcs_map_320,
            utm_profile=utm_profile,
            utm_status=utm_status,
            utm_log=utm_log,
            ips_sensor=ips_sensor,
            application_list=application_list,
            antivirus_profile=antivirus_profile,
            webfilter_profile=webfilter_profile,
            scan_botnet_connections=scan_botnet_connections,
            address_group=address_group,
            address_group_policy=address_group_policy,
            sticky_client_remove=sticky_client_remove,
            sticky_client_threshold_5g=sticky_client_threshold_5g,
            sticky_client_threshold_2g=sticky_client_threshold_2g,
            sticky_client_threshold_6g=sticky_client_threshold_6g,
            bstm_rssi_disassoc_timer=bstm_rssi_disassoc_timer,
            bstm_load_balancing_disassoc_timer=bstm_load_balancing_disassoc_timer,
            bstm_disassociation_imminent=bstm_disassociation_imminent,
            beacon_advertising=beacon_advertising,
            osen=osen,
            application_detection_engine=application_detection_engine,
            application_dscp_marking=application_dscp_marking,
            application_report_intv=application_report_intv,
            l3_roaming=l3_roaming,
            l3_roaming_mode=l3_roaming_mode,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.vap import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/vap",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/wireless-controller/vap/" + str(name_value)

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
        pre_auth: Literal["enable", "disable"] | None = None,
        external_pre_auth: Literal["enable", "disable"] | None = None,
        mesh_backhaul: Literal["enable", "disable"] | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: Literal["enable", "disable"] | None = None,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = None,
        pmf: Literal["disable", "enable", "optional"] | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: Literal["disable", "enable"] | None = None,
        okc: Literal["disable", "enable"] | None = None,
        mbo: Literal["disable", "enable"] | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = None,
        x80211k: Literal["disable", "enable"] | None = None,
        x80211v: Literal["disable", "enable"] | None = None,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = None,
        fast_bss_transition: Literal["disable", "enable"] | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: Literal["disable", "enable"] | None = None,
        sae_groups: Literal["19", "20", "21"] | list[str] | None = None,
        owe_groups: Literal["19", "20", "21"] | list[str] | None = None,
        owe_transition: Literal["disable", "enable"] | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: Literal["akm6", "akm24"] | list[str] | None = None,
        eapol_key_retries: Literal["disable", "enable"] | None = None,
        tkip_counter_measure: Literal["enable", "disable"] | None = None,
        external_web: str | None = None,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_case: Literal["uppercase", "lowercase"] | None = None,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = None,
        mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_mac_auth: Literal["enable", "disable"] | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        auth: Literal["radius", "usergroup"] | None = None,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = None,
        keyindex: int | None = None,
        key: Any | None = None,
        passphrase: Any | None = None,
        sae_password: Any | None = None,
        sae_h2e_only: Literal["enable", "disable"] | None = None,
        sae_hnp_only: Literal["enable", "disable"] | None = None,
        sae_pk: Literal["enable", "disable"] | None = None,
        sae_private_key: str | None = None,
        akm24_only: Literal["disable", "enable"] | None = None,
        radius_server: str | None = None,
        nas_filter_rule: Literal["enable", "disable"] | None = None,
        domain_name_stripping: Literal["disable", "enable"] | None = None,
        mlo: Literal["disable", "enable"] | None = None,
        local_standalone: Literal["enable", "disable"] | None = None,
        local_standalone_nat: Literal["enable", "disable"] | None = None,
        ip: Any | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: Literal["enable", "disable"] | None = None,
        local_standalone_dns_ip: str | list[str] | None = None,
        local_lan_partition: Literal["enable", "disable"] | None = None,
        local_bridging: Literal["enable", "disable"] | None = None,
        local_lan: Literal["allow", "deny"] | None = None,
        local_authentication: Literal["enable", "disable"] | None = None,
        usergroup: str | list[str] | list[dict[str, Any]] | None = None,
        captive_portal: Literal["enable", "disable"] | None = None,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: str | None = None,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = None,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: Literal["enable", "disable"] | None = None,
        schedule: str | list[str] | list[dict[str, Any]] | None = None,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = None,
        high_efficiency: Literal["enable", "disable"] | None = None,
        target_wake_time: Literal["enable", "disable"] | None = None,
        port_macauth: Literal["disable", "radius", "address-group"] | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: Literal["enable", "disable"] | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: Literal["enable", "disable"] | None = None,
        nac: Literal["enable", "disable"] | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: Literal["enable", "disable"] | None = None,
        dynamic_vlan: Literal["enable", "disable"] | None = None,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = None,
        multicast_enhance: Literal["enable", "disable"] | None = None,
        igmp_snooping: Literal["enable", "disable"] | None = None,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = None,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | None = None,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: Literal["enable", "disable"] | None = None,
        probe_resp_suppression: Literal["enable", "disable"] | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: Literal["enable", "disable"] | None = None,
        quarantine: Literal["enable", "disable"] | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = None,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = None,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = None,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = None,
        ptk_rekey: Literal["enable", "disable"] | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: Literal["enable", "disable"] | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: Literal["enable", "disable"] | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = None,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | None = None,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | None = None,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        utm_log: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = None,
        address_group: str | None = None,
        address_group_policy: Literal["disable", "allow", "deny"] | None = None,
        sticky_client_remove: Literal["enable", "disable"] | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = None,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | None = None,
        osen: Literal["enable", "disable"] | None = None,
        application_detection_engine: Literal["enable", "disable"] | None = None,
        application_dscp_marking: Literal["enable", "disable"] | None = None,
        application_report_intv: int | None = None,
        l3_roaming: Literal["enable", "disable"] | None = None,
        l3_roaming_mode: Literal["direct", "indirect"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new wireless_controller/vap object.

        Configure Virtual Access Points (VAPs).

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: Virtual AP name.
            pre_auth: Enable/disable pre-authentication, where supported by clients (default = enable).
            external_pre_auth: Enable/disable pre-authentication with external APs not managed by the FortiGate (default = disable).
            mesh_backhaul: Enable/disable using this VAP as a WiFi mesh backhaul (default = disable). This entry is only available when security is set to a WPA type or open.
            atf_weight: Airtime weight in percentage (default = 20).
            max_clients: Maximum number of clients that can connect simultaneously to the VAP (default = 0, meaning no limitation).
            max_clients_ap: Maximum number of clients that can connect simultaneously to the VAP per AP radio (default = 0, meaning no limitation).
            ssid: IEEE 802.11 service set identifier (SSID) for the wireless interface. Users who wish to use the wireless network must configure their computers to access this SSID name.
            broadcast_ssid: Enable/disable broadcasting the SSID (default = enable).
            security: Security mode for the wireless interface (default = wpa2-only-personal).
            pmf: Protected Management Frames (PMF) support (default = disable).
            pmf_assoc_comeback_timeout: Protected Management Frames (PMF) comeback maximum timeout (1-20 sec).
            pmf_sa_query_retry_timeout: Protected Management Frames (PMF) SA query retry timeout interval (1 - 5 100s of msec).
            beacon_protection: Enable/disable beacon protection support (default = disable).
            okc: Enable/disable Opportunistic Key Caching (OKC) (default = enable).
            mbo: Enable/disable Multiband Operation (default = disable).
            gas_comeback_delay: GAS comeback delay (0 or 100 - 10000 milliseconds, default = 500).
            gas_fragmentation_limit: GAS fragmentation limit (512 - 4096, default = 1024).
            mbo_cell_data_conn_pref: MBO cell data connection preference (0, 1, or 255, default = 1).
            x80211k: Enable/disable 802.11k assisted roaming (default = enable).
            x80211v: Enable/disable 802.11v assisted roaming (default = enable).
            neighbor_report_dual_band: Enable/disable dual-band neighbor report (default = disable).
            fast_bss_transition: Enable/disable 802.11r Fast BSS Transition (FT) (default = disable).
            ft_mobility_domain: Mobility domain identifier in FT (1 - 65535, default = 1000).
            ft_r0_key_lifetime: Lifetime of the PMK-R0 key in FT, 1-65535 minutes.
            ft_over_ds: Enable/disable FT over the Distribution System (DS).
            sae_groups: SAE-Groups.
            owe_groups: OWE-Groups.
            owe_transition: Enable/disable OWE transition mode support.
            owe_transition_ssid: OWE transition mode peer SSID.
            additional_akms: Additional AKMs.
            eapol_key_retries: Enable/disable retransmission of EAPOL-Key frames (message 3/4 and group message 1/2) (default = enable).
            tkip_counter_measure: Enable/disable TKIP counter measure.
            external_web: URL of external authentication web server.
            external_web_format: URL query parameter detection (default = auto-detect).
            external_logout: URL of external authentication logout server.
            mac_username_delimiter: MAC authentication username delimiter (default = hyphen).
            mac_password_delimiter: MAC authentication password delimiter (default = hyphen).
            mac_calling_station_delimiter: MAC calling station delimiter (default = hyphen).
            mac_called_station_delimiter: MAC called station delimiter (default = hyphen).
            mac_case: MAC case (default = uppercase).
            called_station_id_type: The format type of RADIUS attribute Called-Station-Id (default = mac).
            mac_auth_bypass: Enable/disable MAC authentication bypass.
            radius_mac_auth: Enable/disable RADIUS-based MAC authentication of clients (default = disable).
            radius_mac_auth_server: RADIUS-based MAC authentication server.
            radius_mac_auth_block_interval: Don't send RADIUS MAC auth request again if the client has been rejected within specific interval (0 or 30 - 864000 seconds, default = 0, 0 to disable blocking).
            radius_mac_mpsk_auth: Enable/disable RADIUS-based MAC authentication of clients for MPSK authentication (default = disable).
            radius_mac_mpsk_timeout: RADIUS MAC MPSK cache timeout interval (0 or 300 - 864000, default = 86400, 0 to disable caching).
            radius_mac_auth_usergroups: Selective user groups that are permitted for RADIUS mac authentication.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            auth: Authentication protocol.
            encrypt: Encryption protocol to use (only available when security is set to a WPA type).
            keyindex: WEP key index (1 - 4).
            key: WEP Key.
            passphrase: WPA pre-shared key (PSK) to be used to authenticate WiFi users.
            sae_password: WPA3 SAE password to be used to authenticate WiFi users.
            sae_h2e_only: Use hash-to-element-only mechanism for PWE derivation (default = disable).
            sae_hnp_only: Use hunting-and-pecking-only mechanism for PWE derivation (default = disable).
            sae_pk: Enable/disable WPA3 SAE-PK (default = disable).
            sae_private_key: Private key used for WPA3 SAE-PK authentication.
            akm24_only: WPA3 SAE using group-dependent hash only (default = disable).
            radius_server: RADIUS server to be used to authenticate WiFi users.
            nas_filter_rule: Enable/disable NAS filter rule support (default = disable).
            domain_name_stripping: Enable/disable stripping domain name from identity (default = disable).
            mlo: Enable/disable WiFi7 Multi-Link-Operation (default = disable).
            local_standalone: Enable/disable AP local standalone (default = disable).
            local_standalone_nat: Enable/disable AP local standalone NAT mode.
            ip: IP address and subnet mask for the local standalone NAT subnet.
            dhcp_lease_time: DHCP lease time in seconds for NAT IP address.
            local_standalone_dns: Enable/disable AP local standalone DNS.
            local_standalone_dns_ip: IPv4 addresses for the local standalone DNS.
            local_lan_partition: Enable/disable segregating client traffic to local LAN side (default = disable).
            local_bridging: Enable/disable bridging of wireless and Ethernet interfaces on the FortiAP (default = disable).
            local_lan: Allow/deny traffic destined for a Class A, B, or C private IP address (default = allow).
            local_authentication: Enable/disable AP local authentication.
            usergroup: Firewall user group to be used to authenticate WiFi users.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            captive_portal: Enable/disable captive portal.
            captive_network_assistant_bypass: Enable/disable Captive Network Assistant bypass.
            portal_message_override_group: Replacement message group for this VAP (only available when security is set to a captive portal type).
            portal_message_overrides: Individual message overrides.
            portal_type: Captive portal functionality. Configure how the captive portal authenticates users and whether it includes a disclaimer.
            selected_usergroups: Selective user groups that are permitted to authenticate.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            security_exempt_list: Optional security exempt list for captive portal authentication.
            security_redirect_url: Optional URL for redirecting users after they pass captive portal authentication.
            auth_cert: HTTPS server certificate.
            auth_portal_addr: Address of captive portal.
            intra_vap_privacy: Enable/disable blocking communication between clients on the same SSID (called intra-SSID privacy) (default = disable).
            schedule: Firewall schedules for enabling this VAP on the FortiAP. This VAP will be enabled when at least one of the schedules is valid. Separate multiple schedule names with a space.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            ldpc: VAP low-density parity-check (LDPC) coding configuration.
            high_efficiency: Enable/disable 802.11ax high efficiency (default = enable).
            target_wake_time: Enable/disable 802.11ax target wake time (default = enable).
            port_macauth: Enable/disable LAN port MAC authentication (default = disable).
            port_macauth_timeout: LAN port MAC authentication idle timeout value (default = 600 sec).
            port_macauth_reauth_timeout: LAN port MAC authentication re-authentication timeout value (default = 7200 sec).
            bss_color_partial: Enable/disable 802.11ax partial BSS color (default = enable).
            mpsk_profile: MPSK profile name.
            split_tunneling: Enable/disable split tunneling (default = disable).
            nac: Enable/disable network access control.
            nac_profile: NAC profile name.
            vlanid: Optional VLAN ID.
            vlan_auto: Enable/disable automatic management of SSID VLAN interface.
            dynamic_vlan: Enable/disable dynamic VLAN assignment.
            captive_portal_fw_accounting: Enable/disable RADIUS accounting for captive portal firewall authentication session.
            captive_portal_ac_name: Local-bridging captive portal ac-name.
            captive_portal_auth_timeout: Hard timeout - AP will always clear the session after timeout regardless of traffic (0 - 864000 sec, default = 0).
            multicast_rate: Multicast rate (0, 6000, 12000, or 24000 kbps, default = 0).
            multicast_enhance: Enable/disable converting multicast to unicast to improve performance (default = disable).
            igmp_snooping: Enable/disable IGMP snooping.
            dhcp_address_enforcement: Enable/disable DHCP address enforcement (default = disable).
            broadcast_suppression: Optional suppression of broadcast messages. For example, you can keep DHCP messages, ARP broadcasts, and so on off of the wireless network.
            ipv6_rules: Optional rules of IPv6 packets. For example, you can keep RA, RS and so on off of the wireless network.
            me_disable_thresh: Disable multicast enhancement when this many clients are receiving multicast traffic.
            mu_mimo: Enable/disable Multi-user MIMO (default = enable).
            probe_resp_suppression: Enable/disable probe response suppression (to ignore weak signals) (default = disable).
            probe_resp_threshold: Minimum signal level/threshold in dBm required for the AP response to probe requests (-95 to -20, default = -80).
            radio_sensitivity: Enable/disable software radio sensitivity (to ignore weak signals) (default = disable).
            quarantine: Enable/disable station quarantine (default = disable).
            radio_5g_threshold: Minimum signal level/threshold in dBm required for the AP response to receive a packet in 5G band(-95 to -20, default = -76).
            radio_2g_threshold: Minimum signal level/threshold in dBm required for the AP response to receive a packet in 2.4G band (-95 to -20, default = -79).
            vlan_name: Table for mapping VLAN name to VLAN ID.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            vlan_pooling: Enable/disable VLAN pooling, to allow grouping of multiple wireless controller VLANs into VLAN pools (default = disable). When set to wtp-group, VLAN pooling occurs with VLAN assignment by wtp-group.
            vlan_pool: VLAN pool.
                Default format: [{'id': 1}]
                Supported formats:
                  - Single string: "value" → [{'id': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'id': 'val1'}, ...]
                  - List of dicts: [{'id': 1}] (recommended)
            dhcp_option43_insertion: Enable/disable insertion of DHCP option 43 (default = enable).
            dhcp_option82_insertion: Enable/disable DHCP option 82 insert (default = disable).
            dhcp_option82_circuit_id_insertion: Enable/disable DHCP option 82 circuit-id insert (default = disable).
            dhcp_option82_remote_id_insertion: Enable/disable DHCP option 82 remote-id insert (default = disable).
            ptk_rekey: Enable/disable PTK rekey for WPA-Enterprise security.
            ptk_rekey_intv: PTK rekey interval (600 - 864000 sec, default = 86400).
            gtk_rekey: Enable/disable GTK rekey for WPA security.
            gtk_rekey_intv: GTK rekey interval (600 - 864000 sec, default = 86400).
            eap_reauth: Enable/disable EAP re-authentication for WPA-Enterprise security.
            eap_reauth_intv: EAP re-authentication interval (1800 - 864000 sec, default = 86400).
            roaming_acct_interim_update: Enable/disable using accounting interim update instead of accounting start/stop on roaming for WPA-Enterprise security.
            qos_profile: Quality of service profile name.
            hotspot20_profile: Hotspot 2.0 profile name.
            access_control_list: Profile name for access-control-list.
            primary_wag_profile: Primary wireless access gateway profile name.
            secondary_wag_profile: Secondary wireless access gateway profile name.
            tunnel_echo_interval: The time interval to send echo to both primary and secondary tunnel peers (1 - 65535 sec, default = 300).
            tunnel_fallback_interval: The time interval for secondary tunnel to fall back to primary tunnel (0 - 65535 sec, default = 7200).
            rates_11a: Allowed data rates for 802.11a.
            rates_11bg: Allowed data rates for 802.11b/g.
            rates_11n_ss12: Allowed data rates for 802.11n with 1 or 2 spatial streams.
            rates_11n_ss34: Allowed data rates for 802.11n with 3 or 4 spatial streams.
            rates_11ac_mcs_map: Comma separated list of max supported VHT MCS for spatial streams 1 through 8.
            rates_11ax_mcs_map: Comma separated list of max supported HE MCS for spatial streams 1 through 8.
            rates_11be_mcs_map: Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 20MHz/40MHz/80MHz bandwidth.
            rates_11be_mcs_map_160: Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 160MHz bandwidth.
            rates_11be_mcs_map_320: Comma separated list of max nss that supports EHT-MCS 0-9, 10-11, 12-13 for 320MHz bandwidth.
            utm_profile: UTM profile name.
            utm_status: Enable to add one or more security profiles (AV, IPS, etc.) to the VAP.
            utm_log: Enable/disable UTM logging.
            ips_sensor: IPS sensor name.
            application_list: Application control list name.
            antivirus_profile: AntiVirus profile name.
            webfilter_profile: WebFilter profile name.
            scan_botnet_connections: Block or monitor connections to Botnet servers or disable Botnet scanning.
            address_group: Firewall Address Group Name.
            address_group_policy: Configure MAC address filtering policy for MAC addresses that are in the address-group.
            sticky_client_remove: Enable/disable sticky client remove to maintain good signal level clients in SSID (default = disable).
            sticky_client_threshold_5g: Minimum signal level/threshold in dBm required for the 5G client to be serviced by the AP (-95 to -20, default = -76).
            sticky_client_threshold_2g: Minimum signal level/threshold in dBm required for the 2G client to be serviced by the AP (-95 to -20, default = -79).
            sticky_client_threshold_6g: Minimum signal level/threshold in dBm required for the 6G client to be serviced by the AP (-95 to -20, default = -76).
            bstm_rssi_disassoc_timer: Time interval for client to voluntarily leave AP before forcing a disassociation due to low RSSI (0 to 2000, default = 200).
            bstm_load_balancing_disassoc_timer: Time interval for client to voluntarily leave AP before forcing a disassociation due to AP load-balancing (0 to 30, default = 10).
            bstm_disassociation_imminent: Enable/disable forcing of disassociation after the BSTM request timer has been reached (default = enable).
            beacon_advertising: Fortinet beacon advertising IE data   (default = empty).
            osen: Enable/disable OSEN as part of key management (default = disable).
            application_detection_engine: Enable/disable application detection engine (default = disable).
            application_dscp_marking: Enable/disable application attribute based DSCP marking (default = disable).
            application_report_intv: Application report interval (30 - 864000 sec, default = 120).
            l3_roaming: Enable/disable layer 3 roaming (default = disable).
            l3_roaming_mode: Select the way that layer 3 roaming traffic is passed (default = direct).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.wireless_controller_vap.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Vap.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.wireless_controller_vap.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Vap.required_fields()) }}
            
            Use Vap.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if radius_mac_auth_usergroups is not None:
            radius_mac_auth_usergroups = normalize_table_field(
                radius_mac_auth_usergroups,
                mkey="name",
                required_fields=['name'],
                field_name="radius_mac_auth_usergroups",
                example="[{'name': 'value'}]",
            )
        if usergroup is not None:
            usergroup = normalize_table_field(
                usergroup,
                mkey="name",
                required_fields=['name'],
                field_name="usergroup",
                example="[{'name': 'value'}]",
            )
        if selected_usergroups is not None:
            selected_usergroups = normalize_table_field(
                selected_usergroups,
                mkey="name",
                required_fields=['name'],
                field_name="selected_usergroups",
                example="[{'name': 'value'}]",
            )
        if schedule is not None:
            schedule = normalize_table_field(
                schedule,
                mkey="name",
                required_fields=['name'],
                field_name="schedule",
                example="[{'name': 'value'}]",
            )
        if vlan_name is not None:
            vlan_name = normalize_table_field(
                vlan_name,
                mkey="name",
                required_fields=['name'],
                field_name="vlan_name",
                example="[{'name': 'value'}]",
            )
        if vlan_pool is not None:
            vlan_pool = normalize_table_field(
                vlan_pool,
                mkey="id",
                required_fields=['id'],
                field_name="vlan_pool",
                example="[{'id': 1}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            pre_auth=pre_auth,
            external_pre_auth=external_pre_auth,
            mesh_backhaul=mesh_backhaul,
            atf_weight=atf_weight,
            max_clients=max_clients,
            max_clients_ap=max_clients_ap,
            ssid=ssid,
            broadcast_ssid=broadcast_ssid,
            security=security,
            pmf=pmf,
            pmf_assoc_comeback_timeout=pmf_assoc_comeback_timeout,
            pmf_sa_query_retry_timeout=pmf_sa_query_retry_timeout,
            beacon_protection=beacon_protection,
            okc=okc,
            mbo=mbo,
            gas_comeback_delay=gas_comeback_delay,
            gas_fragmentation_limit=gas_fragmentation_limit,
            mbo_cell_data_conn_pref=mbo_cell_data_conn_pref,
            x80211k=x80211k,
            x80211v=x80211v,
            neighbor_report_dual_band=neighbor_report_dual_band,
            fast_bss_transition=fast_bss_transition,
            ft_mobility_domain=ft_mobility_domain,
            ft_r0_key_lifetime=ft_r0_key_lifetime,
            ft_over_ds=ft_over_ds,
            sae_groups=sae_groups,
            owe_groups=owe_groups,
            owe_transition=owe_transition,
            owe_transition_ssid=owe_transition_ssid,
            additional_akms=additional_akms,
            eapol_key_retries=eapol_key_retries,
            tkip_counter_measure=tkip_counter_measure,
            external_web=external_web,
            external_web_format=external_web_format,
            external_logout=external_logout,
            mac_username_delimiter=mac_username_delimiter,
            mac_password_delimiter=mac_password_delimiter,
            mac_calling_station_delimiter=mac_calling_station_delimiter,
            mac_called_station_delimiter=mac_called_station_delimiter,
            mac_case=mac_case,
            called_station_id_type=called_station_id_type,
            mac_auth_bypass=mac_auth_bypass,
            radius_mac_auth=radius_mac_auth,
            radius_mac_auth_server=radius_mac_auth_server,
            radius_mac_auth_block_interval=radius_mac_auth_block_interval,
            radius_mac_mpsk_auth=radius_mac_mpsk_auth,
            radius_mac_mpsk_timeout=radius_mac_mpsk_timeout,
            radius_mac_auth_usergroups=radius_mac_auth_usergroups,
            auth=auth,
            encrypt=encrypt,
            keyindex=keyindex,
            key=key,
            passphrase=passphrase,
            sae_password=sae_password,
            sae_h2e_only=sae_h2e_only,
            sae_hnp_only=sae_hnp_only,
            sae_pk=sae_pk,
            sae_private_key=sae_private_key,
            akm24_only=akm24_only,
            radius_server=radius_server,
            nas_filter_rule=nas_filter_rule,
            domain_name_stripping=domain_name_stripping,
            mlo=mlo,
            local_standalone=local_standalone,
            local_standalone_nat=local_standalone_nat,
            ip=ip,
            dhcp_lease_time=dhcp_lease_time,
            local_standalone_dns=local_standalone_dns,
            local_standalone_dns_ip=local_standalone_dns_ip,
            local_lan_partition=local_lan_partition,
            local_bridging=local_bridging,
            local_lan=local_lan,
            local_authentication=local_authentication,
            usergroup=usergroup,
            captive_portal=captive_portal,
            captive_network_assistant_bypass=captive_network_assistant_bypass,
            portal_message_override_group=portal_message_override_group,
            portal_message_overrides=portal_message_overrides,
            portal_type=portal_type,
            selected_usergroups=selected_usergroups,
            security_exempt_list=security_exempt_list,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            intra_vap_privacy=intra_vap_privacy,
            schedule=schedule,
            ldpc=ldpc,
            high_efficiency=high_efficiency,
            target_wake_time=target_wake_time,
            port_macauth=port_macauth,
            port_macauth_timeout=port_macauth_timeout,
            port_macauth_reauth_timeout=port_macauth_reauth_timeout,
            bss_color_partial=bss_color_partial,
            mpsk_profile=mpsk_profile,
            split_tunneling=split_tunneling,
            nac=nac,
            nac_profile=nac_profile,
            vlanid=vlanid,
            vlan_auto=vlan_auto,
            dynamic_vlan=dynamic_vlan,
            captive_portal_fw_accounting=captive_portal_fw_accounting,
            captive_portal_ac_name=captive_portal_ac_name,
            captive_portal_auth_timeout=captive_portal_auth_timeout,
            multicast_rate=multicast_rate,
            multicast_enhance=multicast_enhance,
            igmp_snooping=igmp_snooping,
            dhcp_address_enforcement=dhcp_address_enforcement,
            broadcast_suppression=broadcast_suppression,
            ipv6_rules=ipv6_rules,
            me_disable_thresh=me_disable_thresh,
            mu_mimo=mu_mimo,
            probe_resp_suppression=probe_resp_suppression,
            probe_resp_threshold=probe_resp_threshold,
            radio_sensitivity=radio_sensitivity,
            quarantine=quarantine,
            radio_5g_threshold=radio_5g_threshold,
            radio_2g_threshold=radio_2g_threshold,
            vlan_name=vlan_name,
            vlan_pooling=vlan_pooling,
            vlan_pool=vlan_pool,
            dhcp_option43_insertion=dhcp_option43_insertion,
            dhcp_option82_insertion=dhcp_option82_insertion,
            dhcp_option82_circuit_id_insertion=dhcp_option82_circuit_id_insertion,
            dhcp_option82_remote_id_insertion=dhcp_option82_remote_id_insertion,
            ptk_rekey=ptk_rekey,
            ptk_rekey_intv=ptk_rekey_intv,
            gtk_rekey=gtk_rekey,
            gtk_rekey_intv=gtk_rekey_intv,
            eap_reauth=eap_reauth,
            eap_reauth_intv=eap_reauth_intv,
            roaming_acct_interim_update=roaming_acct_interim_update,
            qos_profile=qos_profile,
            hotspot20_profile=hotspot20_profile,
            access_control_list=access_control_list,
            primary_wag_profile=primary_wag_profile,
            secondary_wag_profile=secondary_wag_profile,
            tunnel_echo_interval=tunnel_echo_interval,
            tunnel_fallback_interval=tunnel_fallback_interval,
            rates_11a=rates_11a,
            rates_11bg=rates_11bg,
            rates_11n_ss12=rates_11n_ss12,
            rates_11n_ss34=rates_11n_ss34,
            rates_11ac_mcs_map=rates_11ac_mcs_map,
            rates_11ax_mcs_map=rates_11ax_mcs_map,
            rates_11be_mcs_map=rates_11be_mcs_map,
            rates_11be_mcs_map_160=rates_11be_mcs_map_160,
            rates_11be_mcs_map_320=rates_11be_mcs_map_320,
            utm_profile=utm_profile,
            utm_status=utm_status,
            utm_log=utm_log,
            ips_sensor=ips_sensor,
            application_list=application_list,
            antivirus_profile=antivirus_profile,
            webfilter_profile=webfilter_profile,
            scan_botnet_connections=scan_botnet_connections,
            address_group=address_group,
            address_group_policy=address_group_policy,
            sticky_client_remove=sticky_client_remove,
            sticky_client_threshold_5g=sticky_client_threshold_5g,
            sticky_client_threshold_2g=sticky_client_threshold_2g,
            sticky_client_threshold_6g=sticky_client_threshold_6g,
            bstm_rssi_disassoc_timer=bstm_rssi_disassoc_timer,
            bstm_load_balancing_disassoc_timer=bstm_load_balancing_disassoc_timer,
            bstm_disassociation_imminent=bstm_disassociation_imminent,
            beacon_advertising=beacon_advertising,
            osen=osen,
            application_detection_engine=application_detection_engine,
            application_dscp_marking=application_dscp_marking,
            application_report_intv=application_report_intv,
            l3_roaming=l3_roaming,
            l3_roaming_mode=l3_roaming_mode,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.vap import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/wireless_controller/vap",
            )

        endpoint = "/wireless-controller/vap"
        
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
        Delete wireless_controller/vap object.

        Configure Virtual Access Points (VAPs).

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
            >>> result = fgt.api.cmdb.wireless_controller_vap.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/wireless-controller/vap/" + str(name)

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
        Check if wireless_controller/vap object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.wireless_controller_vap.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.wireless_controller_vap.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_vap.delete(name=1)

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
        pre_auth: Literal["enable", "disable"] | None = None,
        external_pre_auth: Literal["enable", "disable"] | None = None,
        mesh_backhaul: Literal["enable", "disable"] | None = None,
        atf_weight: int | None = None,
        max_clients: int | None = None,
        max_clients_ap: int | None = None,
        ssid: str | None = None,
        broadcast_ssid: Literal["enable", "disable"] | None = None,
        security: Literal["open", "wep64", "wep128", "wpa-personal", "wpa-enterprise", "wpa-only-personal", "wpa-only-enterprise", "wpa2-only-personal", "wpa2-only-enterprise", "wpa3-enterprise", "wpa3-only-enterprise", "wpa3-enterprise-transition", "wpa3-sae", "wpa3-sae-transition", "owe", "osen"] | None = None,
        pmf: Literal["disable", "enable", "optional"] | None = None,
        pmf_assoc_comeback_timeout: int | None = None,
        pmf_sa_query_retry_timeout: int | None = None,
        beacon_protection: Literal["disable", "enable"] | None = None,
        okc: Literal["disable", "enable"] | None = None,
        mbo: Literal["disable", "enable"] | None = None,
        gas_comeback_delay: int | None = None,
        gas_fragmentation_limit: int | None = None,
        mbo_cell_data_conn_pref: Literal["excluded", "prefer-not", "prefer-use"] | None = None,
        x80211k: Literal["disable", "enable"] | None = None,
        x80211v: Literal["disable", "enable"] | None = None,
        neighbor_report_dual_band: Literal["disable", "enable"] | None = None,
        fast_bss_transition: Literal["disable", "enable"] | None = None,
        ft_mobility_domain: int | None = None,
        ft_r0_key_lifetime: int | None = None,
        ft_over_ds: Literal["disable", "enable"] | None = None,
        sae_groups: Literal["19", "20", "21"] | list[str] | list[dict[str, Any]] | None = None,
        owe_groups: Literal["19", "20", "21"] | list[str] | list[dict[str, Any]] | None = None,
        owe_transition: Literal["disable", "enable"] | None = None,
        owe_transition_ssid: str | None = None,
        additional_akms: Literal["akm6", "akm24"] | list[str] | list[dict[str, Any]] | None = None,
        eapol_key_retries: Literal["disable", "enable"] | None = None,
        tkip_counter_measure: Literal["enable", "disable"] | None = None,
        external_web: str | None = None,
        external_web_format: Literal["auto-detect", "no-query-string", "partial-query-string"] | None = None,
        external_logout: str | None = None,
        mac_username_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_password_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_calling_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_called_station_delimiter: Literal["hyphen", "single-hyphen", "colon", "none"] | None = None,
        mac_case: Literal["uppercase", "lowercase"] | None = None,
        called_station_id_type: Literal["mac", "ip", "apname"] | None = None,
        mac_auth_bypass: Literal["enable", "disable"] | None = None,
        radius_mac_auth: Literal["enable", "disable"] | None = None,
        radius_mac_auth_server: str | None = None,
        radius_mac_auth_block_interval: int | None = None,
        radius_mac_mpsk_auth: Literal["enable", "disable"] | None = None,
        radius_mac_mpsk_timeout: int | None = None,
        radius_mac_auth_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        auth: Literal["radius", "usergroup"] | None = None,
        encrypt: Literal["TKIP", "AES", "TKIP-AES"] | None = None,
        keyindex: int | None = None,
        key: Any | None = None,
        passphrase: Any | None = None,
        sae_password: Any | None = None,
        sae_h2e_only: Literal["enable", "disable"] | None = None,
        sae_hnp_only: Literal["enable", "disable"] | None = None,
        sae_pk: Literal["enable", "disable"] | None = None,
        sae_private_key: str | None = None,
        akm24_only: Literal["disable", "enable"] | None = None,
        radius_server: str | None = None,
        nas_filter_rule: Literal["enable", "disable"] | None = None,
        domain_name_stripping: Literal["disable", "enable"] | None = None,
        mlo: Literal["disable", "enable"] | None = None,
        local_standalone: Literal["enable", "disable"] | None = None,
        local_standalone_nat: Literal["enable", "disable"] | None = None,
        ip: Any | None = None,
        dhcp_lease_time: int | None = None,
        local_standalone_dns: Literal["enable", "disable"] | None = None,
        local_standalone_dns_ip: str | list[str] | list[dict[str, Any]] | None = None,
        local_lan_partition: Literal["enable", "disable"] | None = None,
        local_bridging: Literal["enable", "disable"] | None = None,
        local_lan: Literal["allow", "deny"] | None = None,
        local_authentication: Literal["enable", "disable"] | None = None,
        usergroup: str | list[str] | list[dict[str, Any]] | None = None,
        captive_portal: Literal["enable", "disable"] | None = None,
        captive_network_assistant_bypass: Literal["enable", "disable"] | None = None,
        portal_message_override_group: str | None = None,
        portal_message_overrides: str | None = None,
        portal_type: Literal["auth", "auth+disclaimer", "disclaimer", "email-collect", "cmcc", "cmcc-macauth", "auth-mac", "external-auth", "external-macauth"] | None = None,
        selected_usergroups: str | list[str] | list[dict[str, Any]] | None = None,
        security_exempt_list: str | None = None,
        security_redirect_url: str | None = None,
        auth_cert: str | None = None,
        auth_portal_addr: str | None = None,
        intra_vap_privacy: Literal["enable", "disable"] | None = None,
        schedule: str | list[str] | list[dict[str, Any]] | None = None,
        ldpc: Literal["disable", "rx", "tx", "rxtx"] | None = None,
        high_efficiency: Literal["enable", "disable"] | None = None,
        target_wake_time: Literal["enable", "disable"] | None = None,
        port_macauth: Literal["disable", "radius", "address-group"] | None = None,
        port_macauth_timeout: int | None = None,
        port_macauth_reauth_timeout: int | None = None,
        bss_color_partial: Literal["enable", "disable"] | None = None,
        mpsk_profile: str | None = None,
        split_tunneling: Literal["enable", "disable"] | None = None,
        nac: Literal["enable", "disable"] | None = None,
        nac_profile: str | None = None,
        vlanid: int | None = None,
        vlan_auto: Literal["enable", "disable"] | None = None,
        dynamic_vlan: Literal["enable", "disable"] | None = None,
        captive_portal_fw_accounting: Literal["enable", "disable"] | None = None,
        captive_portal_ac_name: str | None = None,
        captive_portal_auth_timeout: int | None = None,
        multicast_rate: Literal["0", "6000", "12000", "24000"] | None = None,
        multicast_enhance: Literal["enable", "disable"] | None = None,
        igmp_snooping: Literal["enable", "disable"] | None = None,
        dhcp_address_enforcement: Literal["enable", "disable"] | None = None,
        broadcast_suppression: Literal["dhcp-up", "dhcp-down", "dhcp-starvation", "dhcp-ucast", "arp-known", "arp-unknown", "arp-reply", "arp-poison", "arp-proxy", "netbios-ns", "netbios-ds", "ipv6", "all-other-mc", "all-other-bc"] | list[str] | list[dict[str, Any]] | None = None,
        ipv6_rules: Literal["drop-icmp6ra", "drop-icmp6rs", "drop-llmnr6", "drop-icmp6mld2", "drop-dhcp6s", "drop-dhcp6c", "ndp-proxy", "drop-ns-dad", "drop-ns-nondad"] | list[str] | list[dict[str, Any]] | None = None,
        me_disable_thresh: int | None = None,
        mu_mimo: Literal["enable", "disable"] | None = None,
        probe_resp_suppression: Literal["enable", "disable"] | None = None,
        probe_resp_threshold: str | None = None,
        radio_sensitivity: Literal["enable", "disable"] | None = None,
        quarantine: Literal["enable", "disable"] | None = None,
        radio_5g_threshold: str | None = None,
        radio_2g_threshold: str | None = None,
        vlan_name: str | list[str] | list[dict[str, Any]] | None = None,
        vlan_pooling: Literal["wtp-group", "round-robin", "hash", "disable"] | None = None,
        vlan_pool: str | list[str] | list[dict[str, Any]] | None = None,
        dhcp_option43_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_insertion: Literal["enable", "disable"] | None = None,
        dhcp_option82_circuit_id_insertion: Literal["style-1", "style-2", "style-3", "disable"] | None = None,
        dhcp_option82_remote_id_insertion: Literal["style-1", "disable"] | None = None,
        ptk_rekey: Literal["enable", "disable"] | None = None,
        ptk_rekey_intv: int | None = None,
        gtk_rekey: Literal["enable", "disable"] | None = None,
        gtk_rekey_intv: int | None = None,
        eap_reauth: Literal["enable", "disable"] | None = None,
        eap_reauth_intv: int | None = None,
        roaming_acct_interim_update: Literal["enable", "disable"] | None = None,
        qos_profile: str | None = None,
        hotspot20_profile: str | None = None,
        access_control_list: str | None = None,
        primary_wag_profile: str | None = None,
        secondary_wag_profile: str | None = None,
        tunnel_echo_interval: int | None = None,
        tunnel_fallback_interval: int | None = None,
        rates_11a: Literal["6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11bg: Literal["1", "1-basic", "2", "2-basic", "5.5", "5.5-basic", "11", "11-basic", "6", "6-basic", "9", "9-basic", "12", "12-basic", "18", "18-basic", "24", "24-basic", "36", "36-basic", "48", "48-basic", "54", "54-basic"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11n_ss12: Literal["mcs0/1", "mcs1/1", "mcs2/1", "mcs3/1", "mcs4/1", "mcs5/1", "mcs6/1", "mcs7/1", "mcs8/2", "mcs9/2", "mcs10/2", "mcs11/2", "mcs12/2", "mcs13/2", "mcs14/2", "mcs15/2"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11n_ss34: Literal["mcs16/3", "mcs17/3", "mcs18/3", "mcs19/3", "mcs20/3", "mcs21/3", "mcs22/3", "mcs23/3", "mcs24/4", "mcs25/4", "mcs26/4", "mcs27/4", "mcs28/4", "mcs29/4", "mcs30/4", "mcs31/4"] | list[str] | list[dict[str, Any]] | None = None,
        rates_11ac_mcs_map: str | None = None,
        rates_11ax_mcs_map: str | None = None,
        rates_11be_mcs_map: str | None = None,
        rates_11be_mcs_map_160: str | None = None,
        rates_11be_mcs_map_320: str | None = None,
        utm_profile: str | None = None,
        utm_status: Literal["enable", "disable"] | None = None,
        utm_log: Literal["enable", "disable"] | None = None,
        ips_sensor: str | None = None,
        application_list: str | None = None,
        antivirus_profile: str | None = None,
        webfilter_profile: str | None = None,
        scan_botnet_connections: Literal["disable", "monitor", "block"] | None = None,
        address_group: str | None = None,
        address_group_policy: Literal["disable", "allow", "deny"] | None = None,
        sticky_client_remove: Literal["enable", "disable"] | None = None,
        sticky_client_threshold_5g: str | None = None,
        sticky_client_threshold_2g: str | None = None,
        sticky_client_threshold_6g: str | None = None,
        bstm_rssi_disassoc_timer: int | None = None,
        bstm_load_balancing_disassoc_timer: int | None = None,
        bstm_disassociation_imminent: Literal["enable", "disable"] | None = None,
        beacon_advertising: Literal["name", "model", "serial-number"] | list[str] | list[dict[str, Any]] | None = None,
        osen: Literal["enable", "disable"] | None = None,
        application_detection_engine: Literal["enable", "disable"] | None = None,
        application_dscp_marking: Literal["enable", "disable"] | None = None,
        application_report_intv: int | None = None,
        l3_roaming: Literal["enable", "disable"] | None = None,
        l3_roaming_mode: Literal["direct", "indirect"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update wireless_controller/vap object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            pre_auth: Field pre-auth
            external_pre_auth: Field external-pre-auth
            mesh_backhaul: Field mesh-backhaul
            atf_weight: Field atf-weight
            max_clients: Field max-clients
            max_clients_ap: Field max-clients-ap
            ssid: Field ssid
            broadcast_ssid: Field broadcast-ssid
            security: Field security
            pmf: Field pmf
            pmf_assoc_comeback_timeout: Field pmf-assoc-comeback-timeout
            pmf_sa_query_retry_timeout: Field pmf-sa-query-retry-timeout
            beacon_protection: Field beacon-protection
            okc: Field okc
            mbo: Field mbo
            gas_comeback_delay: Field gas-comeback-delay
            gas_fragmentation_limit: Field gas-fragmentation-limit
            mbo_cell_data_conn_pref: Field mbo-cell-data-conn-pref
            x80211k: Field 80211k
            x80211v: Field 80211v
            neighbor_report_dual_band: Field neighbor-report-dual-band
            fast_bss_transition: Field fast-bss-transition
            ft_mobility_domain: Field ft-mobility-domain
            ft_r0_key_lifetime: Field ft-r0-key-lifetime
            ft_over_ds: Field ft-over-ds
            sae_groups: Field sae-groups
            owe_groups: Field owe-groups
            owe_transition: Field owe-transition
            owe_transition_ssid: Field owe-transition-ssid
            additional_akms: Field additional-akms
            eapol_key_retries: Field eapol-key-retries
            tkip_counter_measure: Field tkip-counter-measure
            external_web: Field external-web
            external_web_format: Field external-web-format
            external_logout: Field external-logout
            mac_username_delimiter: Field mac-username-delimiter
            mac_password_delimiter: Field mac-password-delimiter
            mac_calling_station_delimiter: Field mac-calling-station-delimiter
            mac_called_station_delimiter: Field mac-called-station-delimiter
            mac_case: Field mac-case
            called_station_id_type: Field called-station-id-type
            mac_auth_bypass: Field mac-auth-bypass
            radius_mac_auth: Field radius-mac-auth
            radius_mac_auth_server: Field radius-mac-auth-server
            radius_mac_auth_block_interval: Field radius-mac-auth-block-interval
            radius_mac_mpsk_auth: Field radius-mac-mpsk-auth
            radius_mac_mpsk_timeout: Field radius-mac-mpsk-timeout
            radius_mac_auth_usergroups: Field radius-mac-auth-usergroups
            auth: Field auth
            encrypt: Field encrypt
            keyindex: Field keyindex
            key: Field key
            passphrase: Field passphrase
            sae_password: Field sae-password
            sae_h2e_only: Field sae-h2e-only
            sae_hnp_only: Field sae-hnp-only
            sae_pk: Field sae-pk
            sae_private_key: Field sae-private-key
            akm24_only: Field akm24-only
            radius_server: Field radius-server
            nas_filter_rule: Field nas-filter-rule
            domain_name_stripping: Field domain-name-stripping
            mlo: Field mlo
            local_standalone: Field local-standalone
            local_standalone_nat: Field local-standalone-nat
            ip: Field ip
            dhcp_lease_time: Field dhcp-lease-time
            local_standalone_dns: Field local-standalone-dns
            local_standalone_dns_ip: Field local-standalone-dns-ip
            local_lan_partition: Field local-lan-partition
            local_bridging: Field local-bridging
            local_lan: Field local-lan
            local_authentication: Field local-authentication
            usergroup: Field usergroup
            captive_portal: Field captive-portal
            captive_network_assistant_bypass: Field captive-network-assistant-bypass
            portal_message_override_group: Field portal-message-override-group
            portal_message_overrides: Field portal-message-overrides
            portal_type: Field portal-type
            selected_usergroups: Field selected-usergroups
            security_exempt_list: Field security-exempt-list
            security_redirect_url: Field security-redirect-url
            auth_cert: Field auth-cert
            auth_portal_addr: Field auth-portal-addr
            intra_vap_privacy: Field intra-vap-privacy
            schedule: Field schedule
            ldpc: Field ldpc
            high_efficiency: Field high-efficiency
            target_wake_time: Field target-wake-time
            port_macauth: Field port-macauth
            port_macauth_timeout: Field port-macauth-timeout
            port_macauth_reauth_timeout: Field port-macauth-reauth-timeout
            bss_color_partial: Field bss-color-partial
            mpsk_profile: Field mpsk-profile
            split_tunneling: Field split-tunneling
            nac: Field nac
            nac_profile: Field nac-profile
            vlanid: Field vlanid
            vlan_auto: Field vlan-auto
            dynamic_vlan: Field dynamic-vlan
            captive_portal_fw_accounting: Field captive-portal-fw-accounting
            captive_portal_ac_name: Field captive-portal-ac-name
            captive_portal_auth_timeout: Field captive-portal-auth-timeout
            multicast_rate: Field multicast-rate
            multicast_enhance: Field multicast-enhance
            igmp_snooping: Field igmp-snooping
            dhcp_address_enforcement: Field dhcp-address-enforcement
            broadcast_suppression: Field broadcast-suppression
            ipv6_rules: Field ipv6-rules
            me_disable_thresh: Field me-disable-thresh
            mu_mimo: Field mu-mimo
            probe_resp_suppression: Field probe-resp-suppression
            probe_resp_threshold: Field probe-resp-threshold
            radio_sensitivity: Field radio-sensitivity
            quarantine: Field quarantine
            radio_5g_threshold: Field radio-5g-threshold
            radio_2g_threshold: Field radio-2g-threshold
            vlan_name: Field vlan-name
            vlan_pooling: Field vlan-pooling
            vlan_pool: Field vlan-pool
            dhcp_option43_insertion: Field dhcp-option43-insertion
            dhcp_option82_insertion: Field dhcp-option82-insertion
            dhcp_option82_circuit_id_insertion: Field dhcp-option82-circuit-id-insertion
            dhcp_option82_remote_id_insertion: Field dhcp-option82-remote-id-insertion
            ptk_rekey: Field ptk-rekey
            ptk_rekey_intv: Field ptk-rekey-intv
            gtk_rekey: Field gtk-rekey
            gtk_rekey_intv: Field gtk-rekey-intv
            eap_reauth: Field eap-reauth
            eap_reauth_intv: Field eap-reauth-intv
            roaming_acct_interim_update: Field roaming-acct-interim-update
            qos_profile: Field qos-profile
            hotspot20_profile: Field hotspot20-profile
            access_control_list: Field access-control-list
            primary_wag_profile: Field primary-wag-profile
            secondary_wag_profile: Field secondary-wag-profile
            tunnel_echo_interval: Field tunnel-echo-interval
            tunnel_fallback_interval: Field tunnel-fallback-interval
            rates_11a: Field rates-11a
            rates_11bg: Field rates-11bg
            rates_11n_ss12: Field rates-11n-ss12
            rates_11n_ss34: Field rates-11n-ss34
            rates_11ac_mcs_map: Field rates-11ac-mcs-map
            rates_11ax_mcs_map: Field rates-11ax-mcs-map
            rates_11be_mcs_map: Field rates-11be-mcs-map
            rates_11be_mcs_map_160: Field rates-11be-mcs-map-160
            rates_11be_mcs_map_320: Field rates-11be-mcs-map-320
            utm_profile: Field utm-profile
            utm_status: Field utm-status
            utm_log: Field utm-log
            ips_sensor: Field ips-sensor
            application_list: Field application-list
            antivirus_profile: Field antivirus-profile
            webfilter_profile: Field webfilter-profile
            scan_botnet_connections: Field scan-botnet-connections
            address_group: Field address-group
            address_group_policy: Field address-group-policy
            sticky_client_remove: Field sticky-client-remove
            sticky_client_threshold_5g: Field sticky-client-threshold-5g
            sticky_client_threshold_2g: Field sticky-client-threshold-2g
            sticky_client_threshold_6g: Field sticky-client-threshold-6g
            bstm_rssi_disassoc_timer: Field bstm-rssi-disassoc-timer
            bstm_load_balancing_disassoc_timer: Field bstm-load-balancing-disassoc-timer
            bstm_disassociation_imminent: Field bstm-disassociation-imminent
            beacon_advertising: Field beacon-advertising
            osen: Field osen
            application_detection_engine: Field application-detection-engine
            application_dscp_marking: Field application-dscp-marking
            application_report_intv: Field application-report-intv
            l3_roaming: Field l3-roaming
            l3_roaming_mode: Field l3-roaming-mode
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.wireless_controller_vap.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.wireless_controller_vap.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.wireless_controller_vap.set(payload_dict=obj_data)
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
            pre_auth=pre_auth,
            external_pre_auth=external_pre_auth,
            mesh_backhaul=mesh_backhaul,
            atf_weight=atf_weight,
            max_clients=max_clients,
            max_clients_ap=max_clients_ap,
            ssid=ssid,
            broadcast_ssid=broadcast_ssid,
            security=security,
            pmf=pmf,
            pmf_assoc_comeback_timeout=pmf_assoc_comeback_timeout,
            pmf_sa_query_retry_timeout=pmf_sa_query_retry_timeout,
            beacon_protection=beacon_protection,
            okc=okc,
            mbo=mbo,
            gas_comeback_delay=gas_comeback_delay,
            gas_fragmentation_limit=gas_fragmentation_limit,
            mbo_cell_data_conn_pref=mbo_cell_data_conn_pref,
            x80211k=x80211k,
            x80211v=x80211v,
            neighbor_report_dual_band=neighbor_report_dual_band,
            fast_bss_transition=fast_bss_transition,
            ft_mobility_domain=ft_mobility_domain,
            ft_r0_key_lifetime=ft_r0_key_lifetime,
            ft_over_ds=ft_over_ds,
            sae_groups=sae_groups,
            owe_groups=owe_groups,
            owe_transition=owe_transition,
            owe_transition_ssid=owe_transition_ssid,
            additional_akms=additional_akms,
            eapol_key_retries=eapol_key_retries,
            tkip_counter_measure=tkip_counter_measure,
            external_web=external_web,
            external_web_format=external_web_format,
            external_logout=external_logout,
            mac_username_delimiter=mac_username_delimiter,
            mac_password_delimiter=mac_password_delimiter,
            mac_calling_station_delimiter=mac_calling_station_delimiter,
            mac_called_station_delimiter=mac_called_station_delimiter,
            mac_case=mac_case,
            called_station_id_type=called_station_id_type,
            mac_auth_bypass=mac_auth_bypass,
            radius_mac_auth=radius_mac_auth,
            radius_mac_auth_server=radius_mac_auth_server,
            radius_mac_auth_block_interval=radius_mac_auth_block_interval,
            radius_mac_mpsk_auth=radius_mac_mpsk_auth,
            radius_mac_mpsk_timeout=radius_mac_mpsk_timeout,
            radius_mac_auth_usergroups=radius_mac_auth_usergroups,
            auth=auth,
            encrypt=encrypt,
            keyindex=keyindex,
            key=key,
            passphrase=passphrase,
            sae_password=sae_password,
            sae_h2e_only=sae_h2e_only,
            sae_hnp_only=sae_hnp_only,
            sae_pk=sae_pk,
            sae_private_key=sae_private_key,
            akm24_only=akm24_only,
            radius_server=radius_server,
            nas_filter_rule=nas_filter_rule,
            domain_name_stripping=domain_name_stripping,
            mlo=mlo,
            local_standalone=local_standalone,
            local_standalone_nat=local_standalone_nat,
            ip=ip,
            dhcp_lease_time=dhcp_lease_time,
            local_standalone_dns=local_standalone_dns,
            local_standalone_dns_ip=local_standalone_dns_ip,
            local_lan_partition=local_lan_partition,
            local_bridging=local_bridging,
            local_lan=local_lan,
            local_authentication=local_authentication,
            usergroup=usergroup,
            captive_portal=captive_portal,
            captive_network_assistant_bypass=captive_network_assistant_bypass,
            portal_message_override_group=portal_message_override_group,
            portal_message_overrides=portal_message_overrides,
            portal_type=portal_type,
            selected_usergroups=selected_usergroups,
            security_exempt_list=security_exempt_list,
            security_redirect_url=security_redirect_url,
            auth_cert=auth_cert,
            auth_portal_addr=auth_portal_addr,
            intra_vap_privacy=intra_vap_privacy,
            schedule=schedule,
            ldpc=ldpc,
            high_efficiency=high_efficiency,
            target_wake_time=target_wake_time,
            port_macauth=port_macauth,
            port_macauth_timeout=port_macauth_timeout,
            port_macauth_reauth_timeout=port_macauth_reauth_timeout,
            bss_color_partial=bss_color_partial,
            mpsk_profile=mpsk_profile,
            split_tunneling=split_tunneling,
            nac=nac,
            nac_profile=nac_profile,
            vlanid=vlanid,
            vlan_auto=vlan_auto,
            dynamic_vlan=dynamic_vlan,
            captive_portal_fw_accounting=captive_portal_fw_accounting,
            captive_portal_ac_name=captive_portal_ac_name,
            captive_portal_auth_timeout=captive_portal_auth_timeout,
            multicast_rate=multicast_rate,
            multicast_enhance=multicast_enhance,
            igmp_snooping=igmp_snooping,
            dhcp_address_enforcement=dhcp_address_enforcement,
            broadcast_suppression=broadcast_suppression,
            ipv6_rules=ipv6_rules,
            me_disable_thresh=me_disable_thresh,
            mu_mimo=mu_mimo,
            probe_resp_suppression=probe_resp_suppression,
            probe_resp_threshold=probe_resp_threshold,
            radio_sensitivity=radio_sensitivity,
            quarantine=quarantine,
            radio_5g_threshold=radio_5g_threshold,
            radio_2g_threshold=radio_2g_threshold,
            vlan_name=vlan_name,
            vlan_pooling=vlan_pooling,
            vlan_pool=vlan_pool,
            dhcp_option43_insertion=dhcp_option43_insertion,
            dhcp_option82_insertion=dhcp_option82_insertion,
            dhcp_option82_circuit_id_insertion=dhcp_option82_circuit_id_insertion,
            dhcp_option82_remote_id_insertion=dhcp_option82_remote_id_insertion,
            ptk_rekey=ptk_rekey,
            ptk_rekey_intv=ptk_rekey_intv,
            gtk_rekey=gtk_rekey,
            gtk_rekey_intv=gtk_rekey_intv,
            eap_reauth=eap_reauth,
            eap_reauth_intv=eap_reauth_intv,
            roaming_acct_interim_update=roaming_acct_interim_update,
            qos_profile=qos_profile,
            hotspot20_profile=hotspot20_profile,
            access_control_list=access_control_list,
            primary_wag_profile=primary_wag_profile,
            secondary_wag_profile=secondary_wag_profile,
            tunnel_echo_interval=tunnel_echo_interval,
            tunnel_fallback_interval=tunnel_fallback_interval,
            rates_11a=rates_11a,
            rates_11bg=rates_11bg,
            rates_11n_ss12=rates_11n_ss12,
            rates_11n_ss34=rates_11n_ss34,
            rates_11ac_mcs_map=rates_11ac_mcs_map,
            rates_11ax_mcs_map=rates_11ax_mcs_map,
            rates_11be_mcs_map=rates_11be_mcs_map,
            rates_11be_mcs_map_160=rates_11be_mcs_map_160,
            rates_11be_mcs_map_320=rates_11be_mcs_map_320,
            utm_profile=utm_profile,
            utm_status=utm_status,
            utm_log=utm_log,
            ips_sensor=ips_sensor,
            application_list=application_list,
            antivirus_profile=antivirus_profile,
            webfilter_profile=webfilter_profile,
            scan_botnet_connections=scan_botnet_connections,
            address_group=address_group,
            address_group_policy=address_group_policy,
            sticky_client_remove=sticky_client_remove,
            sticky_client_threshold_5g=sticky_client_threshold_5g,
            sticky_client_threshold_2g=sticky_client_threshold_2g,
            sticky_client_threshold_6g=sticky_client_threshold_6g,
            bstm_rssi_disassoc_timer=bstm_rssi_disassoc_timer,
            bstm_load_balancing_disassoc_timer=bstm_load_balancing_disassoc_timer,
            bstm_disassociation_imminent=bstm_disassociation_imminent,
            beacon_advertising=beacon_advertising,
            osen=osen,
            application_detection_engine=application_detection_engine,
            application_dscp_marking=application_dscp_marking,
            application_report_intv=application_report_intv,
            l3_roaming=l3_roaming,
            l3_roaming_mode=l3_roaming_mode,
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
        Move wireless_controller/vap object to a new position.
        
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
            >>> fgt.api.cmdb.wireless_controller_vap.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/wireless-controller/vap",
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
        Clone wireless_controller/vap object.
        
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
            >>> fgt.api.cmdb.wireless_controller_vap.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/wireless-controller/vap",
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
        Check if wireless_controller/vap object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.wireless_controller_vap.exists(name=1):
            ...     fgt.api.cmdb.wireless_controller_vap.post(payload_dict=data)
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

