"""
FortiOS CMDB - Cmdb Wireless Controller Wtp

Configuration endpoint for managing cmdb wireless controller wtp objects.

API Endpoints:
    GET    /cmdb/wireless-controller/wtp
    POST   /cmdb/wireless-controller/wtp
    GET    /cmdb/wireless-controller/wtp
    PUT    /cmdb/wireless-controller/wtp/{identifier}
    DELETE /cmdb/wireless-controller/wtp/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.wtp.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.wireless_controller.wtp.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.wtp.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.wtp.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.wireless_controller.wtp.delete(name="item_name")

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


class Wtp:
    """
    Wtp Operations.

    Provides CRUD operations for FortiOS wtp configuration.

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
        Initialize Wtp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        wtp_id: str | None = None,
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
            wtp_id: Object identifier (optional for list, required for
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
        if wtp_id:
            endpoint = f"/wireless-controller/wtp/{wtp_id}"
        else:
            endpoint = "/wireless-controller/wtp"
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
        wtp_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        index: int | None = None,
        uuid: str | None = None,
        admin: str | None = None,
        name: str | None = None,
        location: str | None = None,
        comment: str | None = None,
        region: str | None = None,
        region_x: str | None = None,
        region_y: str | None = None,
        firmware_provision: str | None = None,
        firmware_provision_latest: str | None = None,
        wtp_profile: str | None = None,
        apcfg_profile: str | None = None,
        bonjour_profile: str | None = None,
        ble_major_id: int | None = None,
        ble_minor_id: int | None = None,
        override_led_state: str | None = None,
        led_state: str | None = None,
        override_wan_port_mode: str | None = None,
        wan_port_mode: str | None = None,
        override_ip_fragment: str | None = None,
        ip_fragment_preventing: str | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        override_split_tunnel: str | None = None,
        split_tunneling_acl_path: str | None = None,
        split_tunneling_acl_local_ap_subnet: str | None = None,
        split_tunneling_acl: list | None = None,
        override_lan: str | None = None,
        lan: list | None = None,
        override_allowaccess: str | None = None,
        allowaccess: str | None = None,
        override_login_passwd_change: str | None = None,
        login_passwd_change: str | None = None,
        login_passwd: str | None = None,
        override_default_mesh_root: str | None = None,
        default_mesh_root: str | None = None,
        radio_1: list | None = None,
        radio_2: list | None = None,
        radio_3: list | None = None,
        radio_4: list | None = None,
        image_download: str | None = None,
        mesh_bridge_enable: str | None = None,
        purdue_level: str | None = None,
        coordinate_latitude: str | None = None,
        coordinate_longitude: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            wtp_id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            wtp_id: WTP ID. (optional)
            index: Index (0 - 4294967295). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            admin: Configure how the FortiGate operating as a wireless
            controller discovers and manages this WTP, AP or FortiAP.
            (optional)
            name: WTP, AP or FortiAP configuration name. (optional)
            location: Field for describing the physical location of the WTP, AP
            or FortiAP. (optional)
            comment: Comment. (optional)
            region: Region name WTP is associated with. (optional)
            region_x: Relative horizontal region coordinate (between 0 and 1).
            (optional)
            region_y: Relative vertical region coordinate (between 0 and 1).
            (optional)
            firmware_provision: Firmware version to provision to this FortiAP
            on bootup (major.minor.build, i.e. 6.2.1234). (optional)
            firmware_provision_latest: Enable/disable one-time automatic
            provisioning of the latest firmware version. (optional)
            wtp_profile: WTP profile name to apply to this WTP, AP or FortiAP.
            (optional)
            apcfg_profile: AP local configuration profile name. (optional)
            bonjour_profile: Bonjour profile name. (optional)
            ble_major_id: Override BLE Major ID. (optional)
            ble_minor_id: Override BLE Minor ID. (optional)
            override_led_state: Enable to override the profile LED state
            setting for this FortiAP. You must enable this option to use the
            led-state command to turn off the FortiAP's LEDs. (optional)
            led_state: Enable to allow the FortiAPs LEDs to light. Disable to
            keep the LEDs off. You may want to keep the LEDs off so they are
            not distracting in low light areas etc. (optional)
            override_wan_port_mode: Enable/disable overriding the wan-port-mode
            in the WTP profile. (optional)
            wan_port_mode: Enable/disable using the FortiAP WAN port as a LAN
            port. (optional)
            override_ip_fragment: Enable/disable overriding the WTP profile IP
            fragment prevention setting. (optional)
            ip_fragment_preventing: Method(s) by which IP fragmentation is
            prevented for control and data packets through CAPWAP tunnel
            (default = tcp-mss-adjust). (optional)
            tun_mtu_uplink: The maximum transmission unit (MTU) of uplink
            CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of
            FortiAP; default = 0). (optional)
            tun_mtu_downlink: The MTU of downlink CAPWAP tunnel (576 - 1500
            bytes or 0; 0 means the local MTU of FortiAP; default = 0).
            (optional)
            override_split_tunnel: Enable/disable overriding the WTP profile
            split tunneling setting. (optional)
            split_tunneling_acl_path: Split tunneling ACL path is local/tunnel.
            (optional)
            split_tunneling_acl_local_ap_subnet: Enable/disable automatically
            adding local subnetwork of FortiAP to split-tunneling ACL (default
            = disable). (optional)
            split_tunneling_acl: Split tunneling ACL filter list. (optional)
            override_lan: Enable to override the WTP profile LAN port setting.
            (optional)
            lan: WTP LAN port mapping. (optional)
            override_allowaccess: Enable to override the WTP profile management
            access configuration. (optional)
            allowaccess: Control management access to the managed WTP, FortiAP,
            or AP. Separate entries with a space. (optional)
            override_login_passwd_change: Enable to override the WTP profile
            login-password (administrator password) setting. (optional)
            login_passwd_change: Change or reset the administrator password of
            a managed WTP, FortiAP or AP (yes, default, or no, default = no).
            (optional)
            login_passwd: Set the managed WTP, FortiAP, or AP's administrator
            password. (optional)
            override_default_mesh_root: Enable to override the WTP profile
            default mesh root SSID setting. (optional)
            default_mesh_root: Configure default mesh root SSID when it is not
            included by radio's SSID configuration. (optional)
            radio_1: Configuration options for radio 1. (optional)
            radio_2: Configuration options for radio 2. (optional)
            radio_3: Configuration options for radio 3. (optional)
            radio_4: Configuration options for radio 4. (optional)
            image_download: Enable/disable WTP image download. (optional)
            mesh_bridge_enable: Enable/disable mesh Ethernet bridge when WTP is
            configured as a mesh branch/leaf AP. (optional)
            purdue_level: Purdue Level of this WTP. (optional)
            coordinate_latitude: WTP latitude coordinate. (optional)
            coordinate_longitude: WTP longitude coordinate. (optional)
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
        if not wtp_id:
            raise ValueError("wtp_id is required for put()")
        endpoint = f"/wireless-controller/wtp/{wtp_id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if wtp_id is not None:
            data_payload["wtp-id"] = wtp_id
        if index is not None:
            data_payload["index"] = index
        if uuid is not None:
            data_payload["uuid"] = uuid
        if admin is not None:
            data_payload["admin"] = admin
        if name is not None:
            data_payload["name"] = name
        if location is not None:
            data_payload["location"] = location
        if comment is not None:
            data_payload["comment"] = comment
        if region is not None:
            data_payload["region"] = region
        if region_x is not None:
            data_payload["region-x"] = region_x
        if region_y is not None:
            data_payload["region-y"] = region_y
        if firmware_provision is not None:
            data_payload["firmware-provision"] = firmware_provision
        if firmware_provision_latest is not None:
            data_payload["firmware-provision-latest"] = (
                firmware_provision_latest
            )
        if wtp_profile is not None:
            data_payload["wtp-profile"] = wtp_profile
        if apcfg_profile is not None:
            data_payload["apcfg-profile"] = apcfg_profile
        if bonjour_profile is not None:
            data_payload["bonjour-profile"] = bonjour_profile
        if ble_major_id is not None:
            data_payload["ble-major-id"] = ble_major_id
        if ble_minor_id is not None:
            data_payload["ble-minor-id"] = ble_minor_id
        if override_led_state is not None:
            data_payload["override-led-state"] = override_led_state
        if led_state is not None:
            data_payload["led-state"] = led_state
        if override_wan_port_mode is not None:
            data_payload["override-wan-port-mode"] = override_wan_port_mode
        if wan_port_mode is not None:
            data_payload["wan-port-mode"] = wan_port_mode
        if override_ip_fragment is not None:
            data_payload["override-ip-fragment"] = override_ip_fragment
        if ip_fragment_preventing is not None:
            data_payload["ip-fragment-preventing"] = ip_fragment_preventing
        if tun_mtu_uplink is not None:
            data_payload["tun-mtu-uplink"] = tun_mtu_uplink
        if tun_mtu_downlink is not None:
            data_payload["tun-mtu-downlink"] = tun_mtu_downlink
        if override_split_tunnel is not None:
            data_payload["override-split-tunnel"] = override_split_tunnel
        if split_tunneling_acl_path is not None:
            data_payload["split-tunneling-acl-path"] = split_tunneling_acl_path
        if split_tunneling_acl_local_ap_subnet is not None:
            data_payload["split-tunneling-acl-local-ap-subnet"] = (
                split_tunneling_acl_local_ap_subnet
            )
        if split_tunneling_acl is not None:
            data_payload["split-tunneling-acl"] = split_tunneling_acl
        if override_lan is not None:
            data_payload["override-lan"] = override_lan
        if lan is not None:
            data_payload["lan"] = lan
        if override_allowaccess is not None:
            data_payload["override-allowaccess"] = override_allowaccess
        if allowaccess is not None:
            data_payload["allowaccess"] = allowaccess
        if override_login_passwd_change is not None:
            data_payload["override-login-passwd-change"] = (
                override_login_passwd_change
            )
        if login_passwd_change is not None:
            data_payload["login-passwd-change"] = login_passwd_change
        if login_passwd is not None:
            data_payload["login-passwd"] = login_passwd
        if override_default_mesh_root is not None:
            data_payload["override-default-mesh-root"] = (
                override_default_mesh_root
            )
        if default_mesh_root is not None:
            data_payload["default-mesh-root"] = default_mesh_root
        if radio_1 is not None:
            data_payload["radio-1"] = radio_1
        if radio_2 is not None:
            data_payload["radio-2"] = radio_2
        if radio_3 is not None:
            data_payload["radio-3"] = radio_3
        if radio_4 is not None:
            data_payload["radio-4"] = radio_4
        if image_download is not None:
            data_payload["image-download"] = image_download
        if mesh_bridge_enable is not None:
            data_payload["mesh-bridge-enable"] = mesh_bridge_enable
        if purdue_level is not None:
            data_payload["purdue-level"] = purdue_level
        if coordinate_latitude is not None:
            data_payload["coordinate-latitude"] = coordinate_latitude
        if coordinate_longitude is not None:
            data_payload["coordinate-longitude"] = coordinate_longitude
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        wtp_id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            wtp_id: Object identifier (required)
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
        if not wtp_id:
            raise ValueError("wtp_id is required for delete()")
        endpoint = f"/wireless-controller/wtp/{wtp_id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        wtp_id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            wtp_id: Object identifier
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
        result = self.get(wtp_id=wtp_id, vdom=vdom)

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
        wtp_id: str | None = None,
        index: int | None = None,
        uuid: str | None = None,
        admin: str | None = None,
        name: str | None = None,
        location: str | None = None,
        comment: str | None = None,
        region: str | None = None,
        region_x: str | None = None,
        region_y: str | None = None,
        firmware_provision: str | None = None,
        firmware_provision_latest: str | None = None,
        wtp_profile: str | None = None,
        apcfg_profile: str | None = None,
        bonjour_profile: str | None = None,
        ble_major_id: int | None = None,
        ble_minor_id: int | None = None,
        override_led_state: str | None = None,
        led_state: str | None = None,
        override_wan_port_mode: str | None = None,
        wan_port_mode: str | None = None,
        override_ip_fragment: str | None = None,
        ip_fragment_preventing: str | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        override_split_tunnel: str | None = None,
        split_tunneling_acl_path: str | None = None,
        split_tunneling_acl_local_ap_subnet: str | None = None,
        split_tunneling_acl: list | None = None,
        override_lan: str | None = None,
        lan: list | None = None,
        override_allowaccess: str | None = None,
        allowaccess: str | None = None,
        override_login_passwd_change: str | None = None,
        login_passwd_change: str | None = None,
        login_passwd: str | None = None,
        override_default_mesh_root: str | None = None,
        default_mesh_root: str | None = None,
        radio_1: list | None = None,
        radio_2: list | None = None,
        radio_3: list | None = None,
        radio_4: list | None = None,
        image_download: str | None = None,
        mesh_bridge_enable: str | None = None,
        purdue_level: str | None = None,
        coordinate_latitude: str | None = None,
        coordinate_longitude: str | None = None,
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
            wtp_id: WTP ID. (optional)
            index: Index (0 - 4294967295). (optional)
            uuid: Universally Unique Identifier (UUID; automatically assigned
            but can be manually reset). (optional)
            admin: Configure how the FortiGate operating as a wireless
            controller discovers and manages this WTP, AP or FortiAP.
            (optional)
            name: WTP, AP or FortiAP configuration name. (optional)
            location: Field for describing the physical location of the WTP, AP
            or FortiAP. (optional)
            comment: Comment. (optional)
            region: Region name WTP is associated with. (optional)
            region_x: Relative horizontal region coordinate (between 0 and 1).
            (optional)
            region_y: Relative vertical region coordinate (between 0 and 1).
            (optional)
            firmware_provision: Firmware version to provision to this FortiAP
            on bootup (major.minor.build, i.e. 6.2.1234). (optional)
            firmware_provision_latest: Enable/disable one-time automatic
            provisioning of the latest firmware version. (optional)
            wtp_profile: WTP profile name to apply to this WTP, AP or FortiAP.
            (optional)
            apcfg_profile: AP local configuration profile name. (optional)
            bonjour_profile: Bonjour profile name. (optional)
            ble_major_id: Override BLE Major ID. (optional)
            ble_minor_id: Override BLE Minor ID. (optional)
            override_led_state: Enable to override the profile LED state
            setting for this FortiAP. You must enable this option to use the
            led-state command to turn off the FortiAP's LEDs. (optional)
            led_state: Enable to allow the FortiAPs LEDs to light. Disable to
            keep the LEDs off. You may want to keep the LEDs off so they are
            not distracting in low light areas etc. (optional)
            override_wan_port_mode: Enable/disable overriding the wan-port-mode
            in the WTP profile. (optional)
            wan_port_mode: Enable/disable using the FortiAP WAN port as a LAN
            port. (optional)
            override_ip_fragment: Enable/disable overriding the WTP profile IP
            fragment prevention setting. (optional)
            ip_fragment_preventing: Method(s) by which IP fragmentation is
            prevented for control and data packets through CAPWAP tunnel
            (default = tcp-mss-adjust). (optional)
            tun_mtu_uplink: The maximum transmission unit (MTU) of uplink
            CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of
            FortiAP; default = 0). (optional)
            tun_mtu_downlink: The MTU of downlink CAPWAP tunnel (576 - 1500
            bytes or 0; 0 means the local MTU of FortiAP; default = 0).
            (optional)
            override_split_tunnel: Enable/disable overriding the WTP profile
            split tunneling setting. (optional)
            split_tunneling_acl_path: Split tunneling ACL path is local/tunnel.
            (optional)
            split_tunneling_acl_local_ap_subnet: Enable/disable automatically
            adding local subnetwork of FortiAP to split-tunneling ACL (default
            = disable). (optional)
            split_tunneling_acl: Split tunneling ACL filter list. (optional)
            override_lan: Enable to override the WTP profile LAN port setting.
            (optional)
            lan: WTP LAN port mapping. (optional)
            override_allowaccess: Enable to override the WTP profile management
            access configuration. (optional)
            allowaccess: Control management access to the managed WTP, FortiAP,
            or AP. Separate entries with a space. (optional)
            override_login_passwd_change: Enable to override the WTP profile
            login-password (administrator password) setting. (optional)
            login_passwd_change: Change or reset the administrator password of
            a managed WTP, FortiAP or AP (yes, default, or no, default = no).
            (optional)
            login_passwd: Set the managed WTP, FortiAP, or AP's administrator
            password. (optional)
            override_default_mesh_root: Enable to override the WTP profile
            default mesh root SSID setting. (optional)
            default_mesh_root: Configure default mesh root SSID when it is not
            included by radio's SSID configuration. (optional)
            radio_1: Configuration options for radio 1. (optional)
            radio_2: Configuration options for radio 2. (optional)
            radio_3: Configuration options for radio 3. (optional)
            radio_4: Configuration options for radio 4. (optional)
            image_download: Enable/disable WTP image download. (optional)
            mesh_bridge_enable: Enable/disable mesh Ethernet bridge when WTP is
            configured as a mesh branch/leaf AP. (optional)
            purdue_level: Purdue Level of this WTP. (optional)
            coordinate_latitude: WTP latitude coordinate. (optional)
            coordinate_longitude: WTP longitude coordinate. (optional)
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
        endpoint = "/wireless-controller/wtp"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if wtp_id is not None:
            data_payload["wtp-id"] = wtp_id
        if index is not None:
            data_payload["index"] = index
        if uuid is not None:
            data_payload["uuid"] = uuid
        if admin is not None:
            data_payload["admin"] = admin
        if name is not None:
            data_payload["name"] = name
        if location is not None:
            data_payload["location"] = location
        if comment is not None:
            data_payload["comment"] = comment
        if region is not None:
            data_payload["region"] = region
        if region_x is not None:
            data_payload["region-x"] = region_x
        if region_y is not None:
            data_payload["region-y"] = region_y
        if firmware_provision is not None:
            data_payload["firmware-provision"] = firmware_provision
        if firmware_provision_latest is not None:
            data_payload["firmware-provision-latest"] = (
                firmware_provision_latest
            )
        if wtp_profile is not None:
            data_payload["wtp-profile"] = wtp_profile
        if apcfg_profile is not None:
            data_payload["apcfg-profile"] = apcfg_profile
        if bonjour_profile is not None:
            data_payload["bonjour-profile"] = bonjour_profile
        if ble_major_id is not None:
            data_payload["ble-major-id"] = ble_major_id
        if ble_minor_id is not None:
            data_payload["ble-minor-id"] = ble_minor_id
        if override_led_state is not None:
            data_payload["override-led-state"] = override_led_state
        if led_state is not None:
            data_payload["led-state"] = led_state
        if override_wan_port_mode is not None:
            data_payload["override-wan-port-mode"] = override_wan_port_mode
        if wan_port_mode is not None:
            data_payload["wan-port-mode"] = wan_port_mode
        if override_ip_fragment is not None:
            data_payload["override-ip-fragment"] = override_ip_fragment
        if ip_fragment_preventing is not None:
            data_payload["ip-fragment-preventing"] = ip_fragment_preventing
        if tun_mtu_uplink is not None:
            data_payload["tun-mtu-uplink"] = tun_mtu_uplink
        if tun_mtu_downlink is not None:
            data_payload["tun-mtu-downlink"] = tun_mtu_downlink
        if override_split_tunnel is not None:
            data_payload["override-split-tunnel"] = override_split_tunnel
        if split_tunneling_acl_path is not None:
            data_payload["split-tunneling-acl-path"] = split_tunneling_acl_path
        if split_tunneling_acl_local_ap_subnet is not None:
            data_payload["split-tunneling-acl-local-ap-subnet"] = (
                split_tunneling_acl_local_ap_subnet
            )
        if split_tunneling_acl is not None:
            data_payload["split-tunneling-acl"] = split_tunneling_acl
        if override_lan is not None:
            data_payload["override-lan"] = override_lan
        if lan is not None:
            data_payload["lan"] = lan
        if override_allowaccess is not None:
            data_payload["override-allowaccess"] = override_allowaccess
        if allowaccess is not None:
            data_payload["allowaccess"] = allowaccess
        if override_login_passwd_change is not None:
            data_payload["override-login-passwd-change"] = (
                override_login_passwd_change
            )
        if login_passwd_change is not None:
            data_payload["login-passwd-change"] = login_passwd_change
        if login_passwd is not None:
            data_payload["login-passwd"] = login_passwd
        if override_default_mesh_root is not None:
            data_payload["override-default-mesh-root"] = (
                override_default_mesh_root
            )
        if default_mesh_root is not None:
            data_payload["default-mesh-root"] = default_mesh_root
        if radio_1 is not None:
            data_payload["radio-1"] = radio_1
        if radio_2 is not None:
            data_payload["radio-2"] = radio_2
        if radio_3 is not None:
            data_payload["radio-3"] = radio_3
        if radio_4 is not None:
            data_payload["radio-4"] = radio_4
        if image_download is not None:
            data_payload["image-download"] = image_download
        if mesh_bridge_enable is not None:
            data_payload["mesh-bridge-enable"] = mesh_bridge_enable
        if purdue_level is not None:
            data_payload["purdue-level"] = purdue_level
        if coordinate_latitude is not None:
            data_payload["coordinate-latitude"] = coordinate_latitude
        if coordinate_longitude is not None:
            data_payload["coordinate-longitude"] = coordinate_longitude
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
