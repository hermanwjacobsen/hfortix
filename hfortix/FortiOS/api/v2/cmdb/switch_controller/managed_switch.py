"""
FortiOS CMDB - Cmdb Switch Controller Managed Switch

Configuration endpoint for managing cmdb switch controller managed switch
objects.

API Endpoints:
    GET    /cmdb/switch-controller/managed_switch
    POST   /cmdb/switch-controller/managed_switch
    GET    /cmdb/switch-controller/managed_switch
    PUT    /cmdb/switch-controller/managed_switch/{identifier}
    DELETE /cmdb/switch-controller/managed_switch/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.switch_controller.managed_switch.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.switch_controller.managed_switch.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.switch_controller.managed_switch.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.switch_controller.managed_switch.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.switch_controller.managed_switch.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class ManagedSwitch:
    """
    Managedswitch Operations.

    Provides CRUD operations for FortiOS managedswitch configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ManagedSwitch endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        switch_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            switch_id: Object identifier (optional for list, required for
            specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if switch_id:
            endpoint = f"/switch-controller/managed-switch/{switch_id}"
        else:
            endpoint = "/switch-controller/managed-switch"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        switch_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        sn: str | None = None,
        description: str | None = None,
        switch_profile: str | None = None,
        access_profile: str | None = None,
        purdue_level: str | None = None,
        fsw_wan1_peer: str | None = None,
        fsw_wan1_admin: str | None = None,
        poe_pre_standard_detection: str | None = None,
        dhcp_server_access_list: str | None = None,
        poe_detection_type: int | None = None,
        max_poe_budget: int | None = None,
        directly_connected: int | None = None,
        version: int | None = None,
        max_allowed_trunk_members: int | None = None,
        pre_provisioned: int | None = None,
        l3_discovered: int | None = None,
        mgmt_mode: int | None = None,
        tunnel_discovered: int | None = None,
        tdr_supported: str | None = None,
        dynamic_capability: str | None = None,
        switch_device_tag: str | None = None,
        switch_dhcp_opt43_key: str | None = None,
        mclag_igmp_snooping_aware: str | None = None,
        dynamically_discovered: int | None = None,
        ptp_status: str | None = None,
        ptp_profile: str | None = None,
        radius_nas_ip_override: str | None = None,
        radius_nas_ip: str | None = None,
        route_offload: str | None = None,
        route_offload_mclag: str | None = None,
        route_offload_router: list | None = None,
        vlan: list | None = None,
        type: str | None = None,
        owner_vdom: str | None = None,
        flow_identity: str | None = None,
        staged_image_version: str | None = None,
        delayed_restart_trigger: int | None = None,
        firmware_provision: str | None = None,
        firmware_provision_version: str | None = None,
        firmware_provision_latest: str | None = None,
        ports: list | None = None,
        ip_source_guard: list | None = None,
        stp_settings: list | None = None,
        stp_instance: list | None = None,
        override_snmp_sysinfo: str | None = None,
        snmp_sysinfo: list | None = None,
        override_snmp_trap_threshold: str | None = None,
        snmp_trap_threshold: list | None = None,
        override_snmp_community: str | None = None,
        snmp_community: list | None = None,
        override_snmp_user: str | None = None,
        snmp_user: list | None = None,
        qos_drop_policy: str | None = None,
        qos_red_probability: int | None = None,
        switch_log: list | None = None,
        remote_log: list | None = None,
        storm_control: list | None = None,
        mirror: list | None = None,
        static_mac: list | None = None,
        custom_command: list | None = None,
        dhcp_snooping_static_client: list | None = None,
        igmp_snooping: list | None = None,
        _802_1X_settings: list | None = None,
        router_vrf: list | None = None,
        system_interface: list | None = None,
        router_static: list | None = None,
        system_dhcp_server: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            switch_id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            switch_id: Managed-switch name. (optional)
            sn: Managed-switch serial number. (optional)
            description: Description. (optional)
            switch_profile: FortiSwitch profile. (optional)
            access_profile: FortiSwitch access profile. (optional)
            purdue_level: Purdue Level of this FortiSwitch. (optional)
            fsw_wan1_peer: FortiSwitch WAN1 peer port. (optional)
            fsw_wan1_admin: FortiSwitch WAN1 admin status; enable to authorize
            the FortiSwitch as a managed switch. (optional)
            poe_pre_standard_detection: Enable/disable PoE pre-standard
            detection. (optional)
            dhcp_server_access_list: DHCP snooping server access list.
            (optional)
            poe_detection_type: PoE detection type for FortiSwitch. (optional)
            max_poe_budget: Max PoE budget for FortiSwitch. (optional)
            directly_connected: Directly connected FortiSwitch. (optional)
            version: FortiSwitch version. (optional)
            max_allowed_trunk_members: FortiSwitch maximum allowed trunk
            members. (optional)
            pre_provisioned: Pre-provisioned managed switch. (optional)
            l3_discovered: Layer 3 management discovered. (optional)
            mgmt_mode: FortiLink management mode. (optional)
            tunnel_discovered: SOCKS tunnel management discovered. (optional)
            tdr_supported: TDR supported. (optional)
            dynamic_capability: List of features this FortiSwitch supports (not
            configurable) that is sent to the FortiGate device for subsequent
            configuration initiated by the FortiGate device. (optional)
            switch_device_tag: User definable label/tag. (optional)
            switch_dhcp_opt43_key: DHCP option43 key. (optional)
            mclag_igmp_snooping_aware: Enable/disable MCLAG IGMP-snooping
            awareness. (optional)
            dynamically_discovered: Dynamically discovered FortiSwitch.
            (optional)
            ptp_status: Enable/disable PTP profile on this FortiSwitch.
            (optional)
            ptp_profile: PTP profile configuration. (optional)
            radius_nas_ip_override: Use locally defined NAS-IP. (optional)
            radius_nas_ip: NAS-IP address. (optional)
            route_offload: Enable/disable route offload on this FortiSwitch.
            (optional)
            route_offload_mclag: Enable/disable route offload MCLAG on this
            FortiSwitch. (optional)
            route_offload_router: Configure route offload MCLAG IP address.
            (optional)
            vlan: Configure VLAN assignment priority. (optional)
            type: Indication of switch type, physical or virtual. (optional)
            owner_vdom: VDOM which owner of port belongs to. (optional)
            flow_identity: Flow-tracking netflow ipfix switch identity in hex
            format(00000000-FFFFFFFF default=0). (optional)
            staged_image_version: Staged image version for FortiSwitch.
            (optional)
            delayed_restart_trigger: Delayed restart triggered for this
            FortiSwitch. (optional)
            firmware_provision: Enable/disable provisioning of firmware to
            FortiSwitches on join connection. (optional)
            firmware_provision_version: Firmware version to provision to this
            FortiSwitch on bootup (major.minor.build, i.e. 6.2.1234).
            (optional)
            firmware_provision_latest: Enable/disable one-time automatic
            provisioning of the latest firmware version. (optional)
            ports: Managed-switch port list. (optional)
            ip_source_guard: IP source guard. (optional)
            stp_settings: Configuration method to edit Spanning Tree Protocol
            (STP) settings used to prevent bridge loops. (optional)
            stp_instance: Configuration method to edit Spanning Tree Protocol
            (STP) instances. (optional)
            override_snmp_sysinfo: Enable/disable overriding the global SNMP
            system information. (optional)
            snmp_sysinfo: Configuration method to edit Simple Network
            Management Protocol (SNMP) system info. (optional)
            override_snmp_trap_threshold: Enable/disable overriding the global
            SNMP trap threshold values. (optional)
            snmp_trap_threshold: Configuration method to edit Simple Network
            Management Protocol (SNMP) trap threshold values. (optional)
            override_snmp_community: Enable/disable overriding the global SNMP
            communities. (optional)
            snmp_community: Configuration method to edit Simple Network
            Management Protocol (SNMP) communities. (optional)
            override_snmp_user: Enable/disable overriding the global SNMP
            users. (optional)
            snmp_user: Configuration method to edit Simple Network Management
            Protocol (SNMP) users. (optional)
            qos_drop_policy: Set QoS drop-policy. (optional)
            qos_red_probability: Set QoS RED/WRED drop probability. (optional)
            switch_log: Configuration method to edit FortiSwitch logging
            settings (logs are transferred to and inserted into the FortiGate
            event log). (optional)
            remote_log: Configure logging by FortiSwitch device to a remote
            syslog server. (optional)
            storm_control: Configuration method to edit FortiSwitch storm
            control for measuring traffic activity using data rates to prevent
            traffic disruption. (optional)
            mirror: Configuration method to edit FortiSwitch packet mirror.
            (optional)
            static_mac: Configuration method to edit FortiSwitch Static and
            Sticky MAC. (optional)
            custom_command: Configuration method to edit FortiSwitch commands
            to be pushed to this FortiSwitch device upon rebooting the
            FortiGate switch controller or the FortiSwitch. (optional)
            dhcp_snooping_static_client: Configure FortiSwitch DHCP snooping
            static clients. (optional)
            igmp_snooping: Configure FortiSwitch IGMP snooping global settings.
            (optional)
            _802_1X_settings: Configuration method to edit FortiSwitch 802.1X
            global settings. (optional)
            router_vrf: Configure VRF. (optional)
            system_interface: Configure system interface on FortiSwitch.
            (optional)
            router_static: Configure static routes. (optional)
            system_dhcp_server: Configure DHCP servers. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not switch_id:
            raise ValueError("switch_id is required for put()")
        endpoint = f"/switch-controller/managed-switch/{switch_id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if switch_id is not None:
            data_payload["switch-id"] = switch_id
        if sn is not None:
            data_payload["sn"] = sn
        if description is not None:
            data_payload["description"] = description
        if switch_profile is not None:
            data_payload["switch-profile"] = switch_profile
        if access_profile is not None:
            data_payload["access-profile"] = access_profile
        if purdue_level is not None:
            data_payload["purdue-level"] = purdue_level
        if fsw_wan1_peer is not None:
            data_payload["fsw-wan1-peer"] = fsw_wan1_peer
        if fsw_wan1_admin is not None:
            data_payload["fsw-wan1-admin"] = fsw_wan1_admin
        if poe_pre_standard_detection is not None:
            data_payload["poe-pre-standard-detection"] = (
                poe_pre_standard_detection
            )
        if dhcp_server_access_list is not None:
            data_payload["dhcp-server-access-list"] = dhcp_server_access_list
        if poe_detection_type is not None:
            data_payload["poe-detection-type"] = poe_detection_type
        if max_poe_budget is not None:
            data_payload["max-poe-budget"] = max_poe_budget
        if directly_connected is not None:
            data_payload["directly-connected"] = directly_connected
        if version is not None:
            data_payload["version"] = version
        if max_allowed_trunk_members is not None:
            data_payload["max-allowed-trunk-members"] = (
                max_allowed_trunk_members
            )
        if pre_provisioned is not None:
            data_payload["pre-provisioned"] = pre_provisioned
        if l3_discovered is not None:
            data_payload["l3-discovered"] = l3_discovered
        if mgmt_mode is not None:
            data_payload["mgmt-mode"] = mgmt_mode
        if tunnel_discovered is not None:
            data_payload["tunnel-discovered"] = tunnel_discovered
        if tdr_supported is not None:
            data_payload["tdr-supported"] = tdr_supported
        if dynamic_capability is not None:
            data_payload["dynamic-capability"] = dynamic_capability
        if switch_device_tag is not None:
            data_payload["switch-device-tag"] = switch_device_tag
        if switch_dhcp_opt43_key is not None:
            data_payload["switch-dhcp_opt43_key"] = switch_dhcp_opt43_key
        if mclag_igmp_snooping_aware is not None:
            data_payload["mclag-igmp-snooping-aware"] = (
                mclag_igmp_snooping_aware
            )
        if dynamically_discovered is not None:
            data_payload["dynamically-discovered"] = dynamically_discovered
        if ptp_status is not None:
            data_payload["ptp-status"] = ptp_status
        if ptp_profile is not None:
            data_payload["ptp-profile"] = ptp_profile
        if radius_nas_ip_override is not None:
            data_payload["radius-nas-ip-override"] = radius_nas_ip_override
        if radius_nas_ip is not None:
            data_payload["radius-nas-ip"] = radius_nas_ip
        if route_offload is not None:
            data_payload["route-offload"] = route_offload
        if route_offload_mclag is not None:
            data_payload["route-offload-mclag"] = route_offload_mclag
        if route_offload_router is not None:
            data_payload["route-offload-router"] = route_offload_router
        if vlan is not None:
            data_payload["vlan"] = vlan
        if type is not None:
            data_payload["type"] = type
        if owner_vdom is not None:
            data_payload["owner-vdom"] = owner_vdom
        if flow_identity is not None:
            data_payload["flow-identity"] = flow_identity
        if staged_image_version is not None:
            data_payload["staged-image-version"] = staged_image_version
        if delayed_restart_trigger is not None:
            data_payload["delayed-restart-trigger"] = delayed_restart_trigger
        if firmware_provision is not None:
            data_payload["firmware-provision"] = firmware_provision
        if firmware_provision_version is not None:
            data_payload["firmware-provision-version"] = (
                firmware_provision_version
            )
        if firmware_provision_latest is not None:
            data_payload["firmware-provision-latest"] = (
                firmware_provision_latest
            )
        if ports is not None:
            data_payload["ports"] = ports
        if ip_source_guard is not None:
            data_payload["ip-source-guard"] = ip_source_guard
        if stp_settings is not None:
            data_payload["stp-settings"] = stp_settings
        if stp_instance is not None:
            data_payload["stp-instance"] = stp_instance
        if override_snmp_sysinfo is not None:
            data_payload["override-snmp-sysinfo"] = override_snmp_sysinfo
        if snmp_sysinfo is not None:
            data_payload["snmp-sysinfo"] = snmp_sysinfo
        if override_snmp_trap_threshold is not None:
            data_payload["override-snmp-trap-threshold"] = (
                override_snmp_trap_threshold
            )
        if snmp_trap_threshold is not None:
            data_payload["snmp-trap-threshold"] = snmp_trap_threshold
        if override_snmp_community is not None:
            data_payload["override-snmp-community"] = override_snmp_community
        if snmp_community is not None:
            data_payload["snmp-community"] = snmp_community
        if override_snmp_user is not None:
            data_payload["override-snmp-user"] = override_snmp_user
        if snmp_user is not None:
            data_payload["snmp-user"] = snmp_user
        if qos_drop_policy is not None:
            data_payload["qos-drop-policy"] = qos_drop_policy
        if qos_red_probability is not None:
            data_payload["qos-red-probability"] = qos_red_probability
        if switch_log is not None:
            data_payload["switch-log"] = switch_log
        if remote_log is not None:
            data_payload["remote-log"] = remote_log
        if storm_control is not None:
            data_payload["storm-control"] = storm_control
        if mirror is not None:
            data_payload["mirror"] = mirror
        if static_mac is not None:
            data_payload["static-mac"] = static_mac
        if custom_command is not None:
            data_payload["custom-command"] = custom_command
        if dhcp_snooping_static_client is not None:
            data_payload["dhcp-snooping-static-client"] = (
                dhcp_snooping_static_client
            )
        if igmp_snooping is not None:
            data_payload["igmp-snooping"] = igmp_snooping
        if _802_1X_settings is not None:
            data_payload["802-1X-settings"] = _802_1X_settings
        if router_vrf is not None:
            data_payload["router-vr"] = router_vrf
        if system_interface is not None:
            data_payload["system-interface"] = system_interface
        if router_static is not None:
            data_payload["router-static"] = router_static
        if system_dhcp_server is not None:
            data_payload["system-dhcp-server"] = system_dhcp_server
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        switch_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            switch_id: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}

        # Build endpoint path
        if not switch_id:
            raise ValueError("switch_id is required for delete()")
        endpoint = f"/switch-controller/managed-switch/{switch_id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        switch_id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            switch_id: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            True if object exists, False otherwise

        Example:
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect

        from hfortix.FortiOS.exceptions_forti import ResourceNotFoundError

        # Call get() - returns dict (sync) or coroutine (async)
        result = self.get(switch_id=switch_id, vdom=vdom)

        # Check if async mode
        if inspect.iscoroutine(result):

            async def _async():
                try:
                    # Runtime check confirms result is a coroutine, cast for
                    # mypy
                    await cast(Coroutine[Any, Any, dict[str, Any]], result)
                    return True
                except ResourceNotFoundError:
                    return False

            # Type ignore justified: mypy can't verify Union return type
            # narrowing

            return _async()
        # Sync mode - get() already executed, no exception means it exists
        return True

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        switch_id: str | None = None,
        sn: str | None = None,
        description: str | None = None,
        switch_profile: str | None = None,
        access_profile: str | None = None,
        purdue_level: str | None = None,
        fsw_wan1_peer: str | None = None,
        fsw_wan1_admin: str | None = None,
        poe_pre_standard_detection: str | None = None,
        dhcp_server_access_list: str | None = None,
        poe_detection_type: int | None = None,
        max_poe_budget: int | None = None,
        directly_connected: int | None = None,
        version: int | None = None,
        max_allowed_trunk_members: int | None = None,
        pre_provisioned: int | None = None,
        l3_discovered: int | None = None,
        mgmt_mode: int | None = None,
        tunnel_discovered: int | None = None,
        tdr_supported: str | None = None,
        dynamic_capability: str | None = None,
        switch_device_tag: str | None = None,
        switch_dhcp_opt43_key: str | None = None,
        mclag_igmp_snooping_aware: str | None = None,
        dynamically_discovered: int | None = None,
        ptp_status: str | None = None,
        ptp_profile: str | None = None,
        radius_nas_ip_override: str | None = None,
        radius_nas_ip: str | None = None,
        route_offload: str | None = None,
        route_offload_mclag: str | None = None,
        route_offload_router: list | None = None,
        vlan: list | None = None,
        type: str | None = None,
        owner_vdom: str | None = None,
        flow_identity: str | None = None,
        staged_image_version: str | None = None,
        delayed_restart_trigger: int | None = None,
        firmware_provision: str | None = None,
        firmware_provision_version: str | None = None,
        firmware_provision_latest: str | None = None,
        ports: list | None = None,
        ip_source_guard: list | None = None,
        stp_settings: list | None = None,
        stp_instance: list | None = None,
        override_snmp_sysinfo: str | None = None,
        snmp_sysinfo: list | None = None,
        override_snmp_trap_threshold: str | None = None,
        snmp_trap_threshold: list | None = None,
        override_snmp_community: str | None = None,
        snmp_community: list | None = None,
        override_snmp_user: str | None = None,
        snmp_user: list | None = None,
        qos_drop_policy: str | None = None,
        qos_red_probability: int | None = None,
        switch_log: list | None = None,
        remote_log: list | None = None,
        storm_control: list | None = None,
        mirror: list | None = None,
        static_mac: list | None = None,
        custom_command: list | None = None,
        dhcp_snooping_static_client: list | None = None,
        igmp_snooping: list | None = None,
        _802_1X_settings: list | None = None,
        router_vrf: list | None = None,
        system_interface: list | None = None,
        router_static: list | None = None,
        system_dhcp_server: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            switch_id: Managed-switch name. (optional)
            sn: Managed-switch serial number. (optional)
            description: Description. (optional)
            switch_profile: FortiSwitch profile. (optional)
            access_profile: FortiSwitch access profile. (optional)
            purdue_level: Purdue Level of this FortiSwitch. (optional)
            fsw_wan1_peer: FortiSwitch WAN1 peer port. (optional)
            fsw_wan1_admin: FortiSwitch WAN1 admin status; enable to authorize
            the FortiSwitch as a managed switch. (optional)
            poe_pre_standard_detection: Enable/disable PoE pre-standard
            detection. (optional)
            dhcp_server_access_list: DHCP snooping server access list.
            (optional)
            poe_detection_type: PoE detection type for FortiSwitch. (optional)
            max_poe_budget: Max PoE budget for FortiSwitch. (optional)
            directly_connected: Directly connected FortiSwitch. (optional)
            version: FortiSwitch version. (optional)
            max_allowed_trunk_members: FortiSwitch maximum allowed trunk
            members. (optional)
            pre_provisioned: Pre-provisioned managed switch. (optional)
            l3_discovered: Layer 3 management discovered. (optional)
            mgmt_mode: FortiLink management mode. (optional)
            tunnel_discovered: SOCKS tunnel management discovered. (optional)
            tdr_supported: TDR supported. (optional)
            dynamic_capability: List of features this FortiSwitch supports (not
            configurable) that is sent to the FortiGate device for subsequent
            configuration initiated by the FortiGate device. (optional)
            switch_device_tag: User definable label/tag. (optional)
            switch_dhcp_opt43_key: DHCP option43 key. (optional)
            mclag_igmp_snooping_aware: Enable/disable MCLAG IGMP-snooping
            awareness. (optional)
            dynamically_discovered: Dynamically discovered FortiSwitch.
            (optional)
            ptp_status: Enable/disable PTP profile on this FortiSwitch.
            (optional)
            ptp_profile: PTP profile configuration. (optional)
            radius_nas_ip_override: Use locally defined NAS-IP. (optional)
            radius_nas_ip: NAS-IP address. (optional)
            route_offload: Enable/disable route offload on this FortiSwitch.
            (optional)
            route_offload_mclag: Enable/disable route offload MCLAG on this
            FortiSwitch. (optional)
            route_offload_router: Configure route offload MCLAG IP address.
            (optional)
            vlan: Configure VLAN assignment priority. (optional)
            type: Indication of switch type, physical or virtual. (optional)
            owner_vdom: VDOM which owner of port belongs to. (optional)
            flow_identity: Flow-tracking netflow ipfix switch identity in hex
            format(00000000-FFFFFFFF default=0). (optional)
            staged_image_version: Staged image version for FortiSwitch.
            (optional)
            delayed_restart_trigger: Delayed restart triggered for this
            FortiSwitch. (optional)
            firmware_provision: Enable/disable provisioning of firmware to
            FortiSwitches on join connection. (optional)
            firmware_provision_version: Firmware version to provision to this
            FortiSwitch on bootup (major.minor.build, i.e. 6.2.1234).
            (optional)
            firmware_provision_latest: Enable/disable one-time automatic
            provisioning of the latest firmware version. (optional)
            ports: Managed-switch port list. (optional)
            ip_source_guard: IP source guard. (optional)
            stp_settings: Configuration method to edit Spanning Tree Protocol
            (STP) settings used to prevent bridge loops. (optional)
            stp_instance: Configuration method to edit Spanning Tree Protocol
            (STP) instances. (optional)
            override_snmp_sysinfo: Enable/disable overriding the global SNMP
            system information. (optional)
            snmp_sysinfo: Configuration method to edit Simple Network
            Management Protocol (SNMP) system info. (optional)
            override_snmp_trap_threshold: Enable/disable overriding the global
            SNMP trap threshold values. (optional)
            snmp_trap_threshold: Configuration method to edit Simple Network
            Management Protocol (SNMP) trap threshold values. (optional)
            override_snmp_community: Enable/disable overriding the global SNMP
            communities. (optional)
            snmp_community: Configuration method to edit Simple Network
            Management Protocol (SNMP) communities. (optional)
            override_snmp_user: Enable/disable overriding the global SNMP
            users. (optional)
            snmp_user: Configuration method to edit Simple Network Management
            Protocol (SNMP) users. (optional)
            qos_drop_policy: Set QoS drop-policy. (optional)
            qos_red_probability: Set QoS RED/WRED drop probability. (optional)
            switch_log: Configuration method to edit FortiSwitch logging
            settings (logs are transferred to and inserted into the FortiGate
            event log). (optional)
            remote_log: Configure logging by FortiSwitch device to a remote
            syslog server. (optional)
            storm_control: Configuration method to edit FortiSwitch storm
            control for measuring traffic activity using data rates to prevent
            traffic disruption. (optional)
            mirror: Configuration method to edit FortiSwitch packet mirror.
            (optional)
            static_mac: Configuration method to edit FortiSwitch Static and
            Sticky MAC. (optional)
            custom_command: Configuration method to edit FortiSwitch commands
            to be pushed to this FortiSwitch device upon rebooting the
            FortiGate switch controller or the FortiSwitch. (optional)
            dhcp_snooping_static_client: Configure FortiSwitch DHCP snooping
            static clients. (optional)
            igmp_snooping: Configure FortiSwitch IGMP snooping global settings.
            (optional)
            _802_1X_settings: Configuration method to edit FortiSwitch 802.1X
            global settings. (optional)
            router_vrf: Configure VRF. (optional)
            system_interface: Configure system interface on FortiSwitch.
            (optional)
            router_static: Configure static routes. (optional)
            system_dhcp_server: Configure DHCP servers. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/switch-controller/managed-switch"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if switch_id is not None:
            data_payload["switch-id"] = switch_id
        if sn is not None:
            data_payload["sn"] = sn
        if description is not None:
            data_payload["description"] = description
        if switch_profile is not None:
            data_payload["switch-profile"] = switch_profile
        if access_profile is not None:
            data_payload["access-profile"] = access_profile
        if purdue_level is not None:
            data_payload["purdue-level"] = purdue_level
        if fsw_wan1_peer is not None:
            data_payload["fsw-wan1-peer"] = fsw_wan1_peer
        if fsw_wan1_admin is not None:
            data_payload["fsw-wan1-admin"] = fsw_wan1_admin
        if poe_pre_standard_detection is not None:
            data_payload["poe-pre-standard-detection"] = (
                poe_pre_standard_detection
            )
        if dhcp_server_access_list is not None:
            data_payload["dhcp-server-access-list"] = dhcp_server_access_list
        if poe_detection_type is not None:
            data_payload["poe-detection-type"] = poe_detection_type
        if max_poe_budget is not None:
            data_payload["max-poe-budget"] = max_poe_budget
        if directly_connected is not None:
            data_payload["directly-connected"] = directly_connected
        if version is not None:
            data_payload["version"] = version
        if max_allowed_trunk_members is not None:
            data_payload["max-allowed-trunk-members"] = (
                max_allowed_trunk_members
            )
        if pre_provisioned is not None:
            data_payload["pre-provisioned"] = pre_provisioned
        if l3_discovered is not None:
            data_payload["l3-discovered"] = l3_discovered
        if mgmt_mode is not None:
            data_payload["mgmt-mode"] = mgmt_mode
        if tunnel_discovered is not None:
            data_payload["tunnel-discovered"] = tunnel_discovered
        if tdr_supported is not None:
            data_payload["tdr-supported"] = tdr_supported
        if dynamic_capability is not None:
            data_payload["dynamic-capability"] = dynamic_capability
        if switch_device_tag is not None:
            data_payload["switch-device-tag"] = switch_device_tag
        if switch_dhcp_opt43_key is not None:
            data_payload["switch-dhcp_opt43_key"] = switch_dhcp_opt43_key
        if mclag_igmp_snooping_aware is not None:
            data_payload["mclag-igmp-snooping-aware"] = (
                mclag_igmp_snooping_aware
            )
        if dynamically_discovered is not None:
            data_payload["dynamically-discovered"] = dynamically_discovered
        if ptp_status is not None:
            data_payload["ptp-status"] = ptp_status
        if ptp_profile is not None:
            data_payload["ptp-profile"] = ptp_profile
        if radius_nas_ip_override is not None:
            data_payload["radius-nas-ip-override"] = radius_nas_ip_override
        if radius_nas_ip is not None:
            data_payload["radius-nas-ip"] = radius_nas_ip
        if route_offload is not None:
            data_payload["route-offload"] = route_offload
        if route_offload_mclag is not None:
            data_payload["route-offload-mclag"] = route_offload_mclag
        if route_offload_router is not None:
            data_payload["route-offload-router"] = route_offload_router
        if vlan is not None:
            data_payload["vlan"] = vlan
        if type is not None:
            data_payload["type"] = type
        if owner_vdom is not None:
            data_payload["owner-vdom"] = owner_vdom
        if flow_identity is not None:
            data_payload["flow-identity"] = flow_identity
        if staged_image_version is not None:
            data_payload["staged-image-version"] = staged_image_version
        if delayed_restart_trigger is not None:
            data_payload["delayed-restart-trigger"] = delayed_restart_trigger
        if firmware_provision is not None:
            data_payload["firmware-provision"] = firmware_provision
        if firmware_provision_version is not None:
            data_payload["firmware-provision-version"] = (
                firmware_provision_version
            )
        if firmware_provision_latest is not None:
            data_payload["firmware-provision-latest"] = (
                firmware_provision_latest
            )
        if ports is not None:
            data_payload["ports"] = ports
        if ip_source_guard is not None:
            data_payload["ip-source-guard"] = ip_source_guard
        if stp_settings is not None:
            data_payload["stp-settings"] = stp_settings
        if stp_instance is not None:
            data_payload["stp-instance"] = stp_instance
        if override_snmp_sysinfo is not None:
            data_payload["override-snmp-sysinfo"] = override_snmp_sysinfo
        if snmp_sysinfo is not None:
            data_payload["snmp-sysinfo"] = snmp_sysinfo
        if override_snmp_trap_threshold is not None:
            data_payload["override-snmp-trap-threshold"] = (
                override_snmp_trap_threshold
            )
        if snmp_trap_threshold is not None:
            data_payload["snmp-trap-threshold"] = snmp_trap_threshold
        if override_snmp_community is not None:
            data_payload["override-snmp-community"] = override_snmp_community
        if snmp_community is not None:
            data_payload["snmp-community"] = snmp_community
        if override_snmp_user is not None:
            data_payload["override-snmp-user"] = override_snmp_user
        if snmp_user is not None:
            data_payload["snmp-user"] = snmp_user
        if qos_drop_policy is not None:
            data_payload["qos-drop-policy"] = qos_drop_policy
        if qos_red_probability is not None:
            data_payload["qos-red-probability"] = qos_red_probability
        if switch_log is not None:
            data_payload["switch-log"] = switch_log
        if remote_log is not None:
            data_payload["remote-log"] = remote_log
        if storm_control is not None:
            data_payload["storm-control"] = storm_control
        if mirror is not None:
            data_payload["mirror"] = mirror
        if static_mac is not None:
            data_payload["static-mac"] = static_mac
        if custom_command is not None:
            data_payload["custom-command"] = custom_command
        if dhcp_snooping_static_client is not None:
            data_payload["dhcp-snooping-static-client"] = (
                dhcp_snooping_static_client
            )
        if igmp_snooping is not None:
            data_payload["igmp-snooping"] = igmp_snooping
        if _802_1X_settings is not None:
            data_payload["802-1X-settings"] = _802_1X_settings
        if router_vrf is not None:
            data_payload["router-vr"] = router_vrf
        if system_interface is not None:
            data_payload["system-interface"] = system_interface
        if router_static is not None:
            data_payload["router-static"] = router_static
        if system_dhcp_server is not None:
            data_payload["system-dhcp-server"] = system_dhcp_server
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
