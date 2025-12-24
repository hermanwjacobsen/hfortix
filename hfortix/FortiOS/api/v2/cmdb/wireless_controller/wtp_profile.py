"""
FortiOS CMDB - Cmdb Wireless Controller Wtp Profile

Configuration endpoint for managing cmdb wireless controller wtp profile
objects.

API Endpoints:
    GET    /cmdb/wireless-controller/wtp_profile
    POST   /cmdb/wireless-controller/wtp_profile
    GET    /cmdb/wireless-controller/wtp_profile
    PUT    /cmdb/wireless-controller/wtp_profile/{identifier}
    DELETE /cmdb/wireless-controller/wtp_profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.wtp_profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.wireless_controller.wtp_profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.wtp_profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.wtp_profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.wtp_profile.delete(name="item_name")

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


class WtpProfile:
    """
    Wtpprofile Operations.

    Provides CRUD operations for FortiOS wtpprofile configuration.

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
        Initialize WtpProfile endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
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
            name: Object identifier (optional for list, required for specific)
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
        if name:
            endpoint = f"/wireless-controller/wtp-profile/{name}"
        else:
            endpoint = "/wireless-controller/wtp-profile"
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
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        comment: str | None = None,
        platform: list | None = None,
        control_message_offload: str | None = None,
        bonjour_profile: str | None = None,
        apcfg_profile: str | None = None,
        apcfg_mesh: str | None = None,
        apcfg_mesh_ap_type: str | None = None,
        apcfg_mesh_ssid: str | None = None,
        apcfg_mesh_eth_bridge: str | None = None,
        ble_profile: str | None = None,
        lw_profile: str | None = None,
        syslog_profile: str | None = None,
        wan_port_mode: str | None = None,
        lan: list | None = None,
        energy_efficient_ethernet: str | None = None,
        led_state: str | None = None,
        led_schedules: list | None = None,
        dtls_policy: str | None = None,
        dtls_in_kernel: str | None = None,
        max_clients: int | None = None,
        handoff_rssi: int | None = None,
        handoff_sta_thresh: int | None = None,
        handoff_roaming: str | None = None,
        deny_mac_list: list | None = None,
        ap_country: str | None = None,
        ip_fragment_preventing: str | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        split_tunneling_acl_path: str | None = None,
        split_tunneling_acl_local_ap_subnet: str | None = None,
        split_tunneling_acl: list | None = None,
        allowaccess: str | None = None,
        login_passwd_change: str | None = None,
        login_passwd: str | None = None,
        lldp: str | None = None,
        poe_mode: str | None = None,
        usb_port: str | None = None,
        frequency_handoff: str | None = None,
        ap_handoff: str | None = None,
        default_mesh_root: str | None = None,
        radio_1: list | None = None,
        radio_2: list | None = None,
        radio_3: list | None = None,
        radio_4: list | None = None,
        lbs: list | None = None,
        ext_info_enable: str | None = None,
        indoor_outdoor_deployment: str | None = None,
        esl_ses_dongle: list | None = None,
        console_login: str | None = None,
        wan_port_auth: str | None = None,
        wan_port_auth_usrname: str | None = None,
        wan_port_auth_password: str | None = None,
        wan_port_auth_methods: str | None = None,
        wan_port_auth_macsec: str | None = None,
        apcfg_auto_cert: str | None = None,
        apcfg_auto_cert_enroll_protocol: str | None = None,
        apcfg_auto_cert_crypto_algo: str | None = None,
        apcfg_auto_cert_est_server: str | None = None,
        apcfg_auto_cert_est_ca_id: str | None = None,
        apcfg_auto_cert_est_http_username: str | None = None,
        apcfg_auto_cert_est_http_password: str | None = None,
        apcfg_auto_cert_est_subject: str | None = None,
        apcfg_auto_cert_est_subject_alt_name: str | None = None,
        apcfg_auto_cert_auto_regen_days: int | None = None,
        apcfg_auto_cert_est_https_ca: str | None = None,
        apcfg_auto_cert_scep_keytype: str | None = None,
        apcfg_auto_cert_scep_keysize: str | None = None,
        apcfg_auto_cert_scep_ec_name: str | None = None,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = None,
        apcfg_auto_cert_scep_url: str | None = None,
        apcfg_auto_cert_scep_password: str | None = None,
        apcfg_auto_cert_scep_ca_id: str | None = None,
        apcfg_auto_cert_scep_subject_alt_name: str | None = None,
        apcfg_auto_cert_scep_https_ca: str | None = None,
        unii_4_5ghz_band: str | None = None,
        admin_auth_tacacs_plus_: str | None = None,
        admin_restrict_local: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: WTP (or FortiAP or AP) profile name. (optional)
            comment: Comment. (optional)
            platform: WTP, FortiAP, or AP platform. (optional)
            control_message_offload: Enable/disable CAPWAP control message data
            channel offload. (optional)
            bonjour_profile: Bonjour profile name. (optional)
            apcfg_profile: AP local configuration profile name. (optional)
            apcfg_mesh: Enable/disable AP local mesh configuration (default =
            disable). (optional)
            apcfg_mesh_ap_type: Mesh AP Type (default = ethernet). (optional)
            apcfg_mesh_ssid: Mesh SSID (default = none). (optional)
            apcfg_mesh_eth_bridge: Enable/disable mesh ethernet bridge (default
            = disable). (optional)
            ble_profile: Bluetooth Low Energy profile name. (optional)
            lw_profile: LoRaWAN profile name. (optional)
            syslog_profile: System log server configuration profile name.
            (optional)
            wan_port_mode: Enable/disable using a WAN port as a LAN port.
            (optional)
            lan: WTP LAN port mapping. (optional)
            energy_efficient_ethernet: Enable/disable use of energy efficient
            Ethernet on WTP. (optional)
            led_state: Enable/disable use of LEDs on WTP (default = enable).
            (optional)
            led_schedules: Recurring firewall schedules for illuminating LEDs
            on the FortiAP. If led-state is enabled, LEDs will be visible when
            at least one of the schedules is valid. Separate multiple schedule
            names with a space. (optional)
            dtls_policy: WTP data channel DTLS policy (default = clear-text).
            (optional)
            dtls_in_kernel: Enable/disable data channel DTLS in kernel.
            (optional)
            max_clients: Maximum number of stations (STAs) supported by the WTP
            (default = 0, meaning no client limitation). (optional)
            handoff_rssi: Minimum received signal strength indicator (RSSI)
            value for handoff (20 - 30, default = 25). (optional)
            handoff_sta_thresh: Threshold value for AP handoff. (optional)
            handoff_roaming: Enable/disable client load balancing during
            roaming to avoid roaming delay (default = enable). (optional)
            deny_mac_list: List of MAC addresses that are denied access to this
            WTP, FortiAP, or AP. (optional)
            ap_country: Country in which this WTP, FortiAP, or AP will operate
            (default = NA, automatically use the country configured for the
            current VDOM). (optional)
            ip_fragment_preventing: Method(s) by which IP fragmentation is
            prevented for control and data packets through CAPWAP tunnel
            (default = tcp-mss-adjust). (optional)
            tun_mtu_uplink: The maximum transmission unit (MTU) of uplink
            CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of
            FortiAP; default = 0). (optional)
            tun_mtu_downlink: The MTU of downlink CAPWAP tunnel (576 - 1500
            bytes or 0; 0 means the local MTU of FortiAP; default = 0).
            (optional)
            split_tunneling_acl_path: Split tunneling ACL path is local/tunnel.
            (optional)
            split_tunneling_acl_local_ap_subnet: Enable/disable automatically
            adding local subnetwork of FortiAP to split-tunneling ACL (default
            = disable). (optional)
            split_tunneling_acl: Split tunneling ACL filter list. (optional)
            allowaccess: Control management access to the managed WTP, FortiAP,
            or AP. Separate entries with a space. (optional)
            login_passwd_change: Change or reset the administrator password of
            a managed WTP, FortiAP or AP (yes, default, or no, default = no).
            (optional)
            login_passwd: Set the managed WTP, FortiAP, or AP's administrator
            password. (optional)
            lldp: Enable/disable Link Layer Discovery Protocol (LLDP) for the
            WTP, FortiAP, or AP (default = enable). (optional)
            poe_mode: Set the WTP, FortiAP, or AP's PoE mode. (optional)
            usb_port: Enable/disable USB port of the WTP (default = enable).
            (optional)
            frequency_handoff: Enable/disable frequency handoff of clients to
            other channels (default = disable). (optional)
            ap_handoff: Enable/disable AP handoff of clients to other APs
            (default = disable). (optional)
            default_mesh_root: Configure default mesh root SSID when it is not
            included by radio's SSID configuration. (optional)
            radio_1: Configuration options for radio 1. (optional)
            radio_2: Configuration options for radio 2. (optional)
            radio_3: Configuration options for radio 3. (optional)
            radio_4: Configuration options for radio 4. (optional)
            lbs: Set various location based service (LBS) options. (optional)
            ext_info_enable: Enable/disable station/VAP/radio extension
            information. (optional)
            indoor_outdoor_deployment: Set to allow indoor/outdoor-only
            channels under regulatory rules (default = platform-determined).
            (optional)
            esl_ses_dongle: ESL SES-imagotag dongle configuration. (optional)
            console_login: Enable/disable FortiAP console login access (default
            = enable). (optional)
            wan_port_auth: Set WAN port authentication mode (default = none).
            (optional)
            wan_port_auth_usrname: Set WAN port 802.1x supplicant user name.
            (optional)
            wan_port_auth_password: Set WAN port 802.1x supplicant password.
            (optional)
            wan_port_auth_methods: WAN port 802.1x supplicant EAP methods
            (default = all). (optional)
            wan_port_auth_macsec: Enable/disable WAN port 802.1x supplicant
            MACsec policy (default = disable). (optional)
            apcfg_auto_cert: Enable/disable AP local auto cert configuration
            (default = disable). (optional)
            apcfg_auto_cert_enroll_protocol: Certificate enrollment protocol
            (default = none) (optional)
            apcfg_auto_cert_crypto_algo: Cryptography algorithm: rsa-1024,
            rsa-1536, rsa-2048, rsa-4096, ec-secp256r1, ec-secp384r1,
            ec-secp521r1 (default = ec-secp256r1) (optional)
            apcfg_auto_cert_est_server: Address and port for EST server (e.g. https://example.com:1234). (optional)
            apcfg_auto_cert_est_ca_id: CA identifier of the CA server for
            signing via EST. (optional)
            apcfg_auto_cert_est_http_username: HTTP Authentication username for
            signing via EST. (optional)
            apcfg_auto_cert_est_http_password: HTTP Authentication password for
            signing via EST. (optional)
            apcfg_auto_cert_est_subject: Subject e.g.
            "CN=User,DC=example,DC=COM" (default = CN=FortiAP,DC=local,DC=COM)
            (optional)
            apcfg_auto_cert_est_subject_alt_name: Subject alternative name
            (optional, e.g. "DNS:dns1.com,IP:192.168.1.99") (optional)
            apcfg_auto_cert_auto_regen_days: Number of days to wait before
            expiry of an updated local certificate is requested (0 = disabled)
            (default = 30). (optional)
            apcfg_auto_cert_est_https_ca: PEM format https CA Certificate.
            (optional)
            apcfg_auto_cert_scep_keytype: Key type (default = rsa) (optional)
            apcfg_auto_cert_scep_keysize: Key size: 1024, 1536, 2048, 4096
            (default 2048). (optional)
            apcfg_auto_cert_scep_ec_name: Elliptic curve name: secp256r1,
            secp384r1 and secp521r1. (default secp256r1). (optional)
            apcfg_auto_cert_scep_sub_fully_dn: Full DN of the subject (e.g
            C=US,ST=CA,L=Sunnyvale,O=Fortinet,OU=Dep1,emailAddress=test@example.com).
            There should be no space in between the attributes. Supported DN
            attributes (case-sensitive) are:C,ST,L,O,OU,emailAddress. The CN
            defaults to the device’s SN and cannot be changed. (optional)
            apcfg_auto_cert_scep_url: SCEP server URL. (optional)
            apcfg_auto_cert_scep_password: SCEP server challenge password for
            auto-regeneration. (optional)
            apcfg_auto_cert_scep_ca_id: CA identifier of the CA server for
            signing via SCEP. (optional)
            apcfg_auto_cert_scep_subject_alt_name: Subject alternative name
            (optional, e.g. "DNS:dns1.com,IP:192.168.1.99") (optional)
            apcfg_auto_cert_scep_https_ca: PEM format https CA Certificate.
            (optional)
            unii_4_5ghz_band: Enable/disable UNII-4 5Ghz band channels (default
            = disable). (optional)
            admin_auth_tacacs_plus_: Remote authentication server for admin
            user. (optional)
            admin_restrict_local: Enable/disable local admin authentication
            restriction when remote authenticator is up and running (default =
            disable). (optional)
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
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/wireless-controller/wtp-profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if platform is not None:
            data_payload["platform"] = platform
        if control_message_offload is not None:
            data_payload["control-message-offload"] = control_message_offload
        if bonjour_profile is not None:
            data_payload["bonjour-profile"] = bonjour_profile
        if apcfg_profile is not None:
            data_payload["apcfg-profile"] = apcfg_profile
        if apcfg_mesh is not None:
            data_payload["apcfg-mesh"] = apcfg_mesh
        if apcfg_mesh_ap_type is not None:
            data_payload["apcfg-mesh-ap-type"] = apcfg_mesh_ap_type
        if apcfg_mesh_ssid is not None:
            data_payload["apcfg-mesh-ssid"] = apcfg_mesh_ssid
        if apcfg_mesh_eth_bridge is not None:
            data_payload["apcfg-mesh-eth-bridge"] = apcfg_mesh_eth_bridge
        if ble_profile is not None:
            data_payload["ble-profile"] = ble_profile
        if lw_profile is not None:
            data_payload["lw-profile"] = lw_profile
        if syslog_profile is not None:
            data_payload["syslog-profile"] = syslog_profile
        if wan_port_mode is not None:
            data_payload["wan-port-mode"] = wan_port_mode
        if lan is not None:
            data_payload["lan"] = lan
        if energy_efficient_ethernet is not None:
            data_payload["energy-efficient-ethernet"] = (
                energy_efficient_ethernet
            )
        if led_state is not None:
            data_payload["led-state"] = led_state
        if led_schedules is not None:
            data_payload["led-schedules"] = led_schedules
        if dtls_policy is not None:
            data_payload["dtls-policy"] = dtls_policy
        if dtls_in_kernel is not None:
            data_payload["dtls-in-kernel"] = dtls_in_kernel
        if max_clients is not None:
            data_payload["max-clients"] = max_clients
        if handoff_rssi is not None:
            data_payload["handoff-rssi"] = handoff_rssi
        if handoff_sta_thresh is not None:
            data_payload["handoff-sta-thresh"] = handoff_sta_thresh
        if handoff_roaming is not None:
            data_payload["handoff-roaming"] = handoff_roaming
        if deny_mac_list is not None:
            data_payload["deny-mac-list"] = deny_mac_list
        if ap_country is not None:
            data_payload["ap-country"] = ap_country
        if ip_fragment_preventing is not None:
            data_payload["ip-fragment-preventing"] = ip_fragment_preventing
        if tun_mtu_uplink is not None:
            data_payload["tun-mtu-uplink"] = tun_mtu_uplink
        if tun_mtu_downlink is not None:
            data_payload["tun-mtu-downlink"] = tun_mtu_downlink
        if split_tunneling_acl_path is not None:
            data_payload["split-tunneling-acl-path"] = split_tunneling_acl_path
        if split_tunneling_acl_local_ap_subnet is not None:
            data_payload["split-tunneling-acl-local-ap-subnet"] = (
                split_tunneling_acl_local_ap_subnet
            )
        if split_tunneling_acl is not None:
            data_payload["split-tunneling-acl"] = split_tunneling_acl
        if allowaccess is not None:
            data_payload["allowaccess"] = allowaccess
        if login_passwd_change is not None:
            data_payload["login-passwd-change"] = login_passwd_change
        if login_passwd is not None:
            data_payload["login-passwd"] = login_passwd
        if lldp is not None:
            data_payload["lldp"] = lldp
        if poe_mode is not None:
            data_payload["poe-mode"] = poe_mode
        if usb_port is not None:
            data_payload["usb-port"] = usb_port
        if frequency_handoff is not None:
            data_payload["frequency-handof"] = frequency_handoff
        if ap_handoff is not None:
            data_payload["ap-handof"] = ap_handoff
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
        if lbs is not None:
            data_payload["lbs"] = lbs
        if ext_info_enable is not None:
            data_payload["ext-info-enable"] = ext_info_enable
        if indoor_outdoor_deployment is not None:
            data_payload["indoor-outdoor-deployment"] = (
                indoor_outdoor_deployment
            )
        if esl_ses_dongle is not None:
            data_payload["esl-ses-dongle"] = esl_ses_dongle
        if console_login is not None:
            data_payload["console-login"] = console_login
        if wan_port_auth is not None:
            data_payload["wan-port-auth"] = wan_port_auth
        if wan_port_auth_usrname is not None:
            data_payload["wan-port-auth-usrname"] = wan_port_auth_usrname
        if wan_port_auth_password is not None:
            data_payload["wan-port-auth-password"] = wan_port_auth_password
        if wan_port_auth_methods is not None:
            data_payload["wan-port-auth-methods"] = wan_port_auth_methods
        if wan_port_auth_macsec is not None:
            data_payload["wan-port-auth-macsec"] = wan_port_auth_macsec
        if apcfg_auto_cert is not None:
            data_payload["apcfg-auto-cert"] = apcfg_auto_cert
        if apcfg_auto_cert_enroll_protocol is not None:
            data_payload["apcfg-auto-cert-enroll-protocol"] = (
                apcfg_auto_cert_enroll_protocol
            )
        if apcfg_auto_cert_crypto_algo is not None:
            data_payload["apcfg-auto-cert-crypto-algo"] = (
                apcfg_auto_cert_crypto_algo
            )
        if apcfg_auto_cert_est_server is not None:
            data_payload["apcfg-auto-cert-est-server"] = (
                apcfg_auto_cert_est_server
            )
        if apcfg_auto_cert_est_ca_id is not None:
            data_payload["apcfg-auto-cert-est-ca-id"] = (
                apcfg_auto_cert_est_ca_id
            )
        if apcfg_auto_cert_est_http_username is not None:
            data_payload["apcfg-auto-cert-est-http-username"] = (
                apcfg_auto_cert_est_http_username
            )
        if apcfg_auto_cert_est_http_password is not None:
            data_payload["apcfg-auto-cert-est-http-password"] = (
                apcfg_auto_cert_est_http_password
            )
        if apcfg_auto_cert_est_subject is not None:
            data_payload["apcfg-auto-cert-est-subject"] = (
                apcfg_auto_cert_est_subject
            )
        if apcfg_auto_cert_est_subject_alt_name is not None:
            data_payload["apcfg-auto-cert-est-subject-alt-name"] = (
                apcfg_auto_cert_est_subject_alt_name
            )
        if apcfg_auto_cert_auto_regen_days is not None:
            data_payload["apcfg-auto-cert-auto-regen-days"] = (
                apcfg_auto_cert_auto_regen_days
            )
        if apcfg_auto_cert_est_https_ca is not None:
            data_payload["apcfg-auto-cert-est-https-ca"] = (
                apcfg_auto_cert_est_https_ca
            )
        if apcfg_auto_cert_scep_keytype is not None:
            data_payload["apcfg-auto-cert-scep-keytype"] = (
                apcfg_auto_cert_scep_keytype
            )
        if apcfg_auto_cert_scep_keysize is not None:
            data_payload["apcfg-auto-cert-scep-keysize"] = (
                apcfg_auto_cert_scep_keysize
            )
        if apcfg_auto_cert_scep_ec_name is not None:
            data_payload["apcfg-auto-cert-scep-ec-name"] = (
                apcfg_auto_cert_scep_ec_name
            )
        if apcfg_auto_cert_scep_sub_fully_dn is not None:
            data_payload["apcfg-auto-cert-scep-sub-fully-dn"] = (
                apcfg_auto_cert_scep_sub_fully_dn
            )
        if apcfg_auto_cert_scep_url is not None:
            data_payload["apcfg-auto-cert-scep-url"] = apcfg_auto_cert_scep_url
        if apcfg_auto_cert_scep_password is not None:
            data_payload["apcfg-auto-cert-scep-password"] = (
                apcfg_auto_cert_scep_password
            )
        if apcfg_auto_cert_scep_ca_id is not None:
            data_payload["apcfg-auto-cert-scep-ca-id"] = (
                apcfg_auto_cert_scep_ca_id
            )
        if apcfg_auto_cert_scep_subject_alt_name is not None:
            data_payload["apcfg-auto-cert-scep-subject-alt-name"] = (
                apcfg_auto_cert_scep_subject_alt_name
            )
        if apcfg_auto_cert_scep_https_ca is not None:
            data_payload["apcfg-auto-cert-scep-https-ca"] = (
                apcfg_auto_cert_scep_https_ca
            )
        if unii_4_5ghz_band is not None:
            data_payload["unii-4-5ghz-band"] = unii_4_5ghz_band
        if admin_auth_tacacs_plus_ is not None:
            data_payload["admin-auth-tacacs+"] = admin_auth_tacacs_plus_
        if admin_restrict_local is not None:
            data_payload["admin-restrict-local"] = admin_restrict_local
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
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
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/wireless-controller/wtp-profile/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
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
        result = self.get(name=name, vdom=vdom)

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
        name: str | None = None,
        comment: str | None = None,
        platform: list | None = None,
        control_message_offload: str | None = None,
        bonjour_profile: str | None = None,
        apcfg_profile: str | None = None,
        apcfg_mesh: str | None = None,
        apcfg_mesh_ap_type: str | None = None,
        apcfg_mesh_ssid: str | None = None,
        apcfg_mesh_eth_bridge: str | None = None,
        ble_profile: str | None = None,
        lw_profile: str | None = None,
        syslog_profile: str | None = None,
        wan_port_mode: str | None = None,
        lan: list | None = None,
        energy_efficient_ethernet: str | None = None,
        led_state: str | None = None,
        led_schedules: list | None = None,
        dtls_policy: str | None = None,
        dtls_in_kernel: str | None = None,
        max_clients: int | None = None,
        handoff_rssi: int | None = None,
        handoff_sta_thresh: int | None = None,
        handoff_roaming: str | None = None,
        deny_mac_list: list | None = None,
        ap_country: str | None = None,
        ip_fragment_preventing: str | None = None,
        tun_mtu_uplink: int | None = None,
        tun_mtu_downlink: int | None = None,
        split_tunneling_acl_path: str | None = None,
        split_tunneling_acl_local_ap_subnet: str | None = None,
        split_tunneling_acl: list | None = None,
        allowaccess: str | None = None,
        login_passwd_change: str | None = None,
        login_passwd: str | None = None,
        lldp: str | None = None,
        poe_mode: str | None = None,
        usb_port: str | None = None,
        frequency_handoff: str | None = None,
        ap_handoff: str | None = None,
        default_mesh_root: str | None = None,
        radio_1: list | None = None,
        radio_2: list | None = None,
        radio_3: list | None = None,
        radio_4: list | None = None,
        lbs: list | None = None,
        ext_info_enable: str | None = None,
        indoor_outdoor_deployment: str | None = None,
        esl_ses_dongle: list | None = None,
        console_login: str | None = None,
        wan_port_auth: str | None = None,
        wan_port_auth_usrname: str | None = None,
        wan_port_auth_password: str | None = None,
        wan_port_auth_methods: str | None = None,
        wan_port_auth_macsec: str | None = None,
        apcfg_auto_cert: str | None = None,
        apcfg_auto_cert_enroll_protocol: str | None = None,
        apcfg_auto_cert_crypto_algo: str | None = None,
        apcfg_auto_cert_est_server: str | None = None,
        apcfg_auto_cert_est_ca_id: str | None = None,
        apcfg_auto_cert_est_http_username: str | None = None,
        apcfg_auto_cert_est_http_password: str | None = None,
        apcfg_auto_cert_est_subject: str | None = None,
        apcfg_auto_cert_est_subject_alt_name: str | None = None,
        apcfg_auto_cert_auto_regen_days: int | None = None,
        apcfg_auto_cert_est_https_ca: str | None = None,
        apcfg_auto_cert_scep_keytype: str | None = None,
        apcfg_auto_cert_scep_keysize: str | None = None,
        apcfg_auto_cert_scep_ec_name: str | None = None,
        apcfg_auto_cert_scep_sub_fully_dn: str | None = None,
        apcfg_auto_cert_scep_url: str | None = None,
        apcfg_auto_cert_scep_password: str | None = None,
        apcfg_auto_cert_scep_ca_id: str | None = None,
        apcfg_auto_cert_scep_subject_alt_name: str | None = None,
        apcfg_auto_cert_scep_https_ca: str | None = None,
        unii_4_5ghz_band: str | None = None,
        admin_auth_tacacs_plus_: str | None = None,
        admin_restrict_local: str | None = None,
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
            name: WTP (or FortiAP or AP) profile name. (optional)
            comment: Comment. (optional)
            platform: WTP, FortiAP, or AP platform. (optional)
            control_message_offload: Enable/disable CAPWAP control message data
            channel offload. (optional)
            bonjour_profile: Bonjour profile name. (optional)
            apcfg_profile: AP local configuration profile name. (optional)
            apcfg_mesh: Enable/disable AP local mesh configuration (default =
            disable). (optional)
            apcfg_mesh_ap_type: Mesh AP Type (default = ethernet). (optional)
            apcfg_mesh_ssid: Mesh SSID (default = none). (optional)
            apcfg_mesh_eth_bridge: Enable/disable mesh ethernet bridge (default
            = disable). (optional)
            ble_profile: Bluetooth Low Energy profile name. (optional)
            lw_profile: LoRaWAN profile name. (optional)
            syslog_profile: System log server configuration profile name.
            (optional)
            wan_port_mode: Enable/disable using a WAN port as a LAN port.
            (optional)
            lan: WTP LAN port mapping. (optional)
            energy_efficient_ethernet: Enable/disable use of energy efficient
            Ethernet on WTP. (optional)
            led_state: Enable/disable use of LEDs on WTP (default = enable).
            (optional)
            led_schedules: Recurring firewall schedules for illuminating LEDs
            on the FortiAP. If led-state is enabled, LEDs will be visible when
            at least one of the schedules is valid. Separate multiple schedule
            names with a space. (optional)
            dtls_policy: WTP data channel DTLS policy (default = clear-text).
            (optional)
            dtls_in_kernel: Enable/disable data channel DTLS in kernel.
            (optional)
            max_clients: Maximum number of stations (STAs) supported by the WTP
            (default = 0, meaning no client limitation). (optional)
            handoff_rssi: Minimum received signal strength indicator (RSSI)
            value for handoff (20 - 30, default = 25). (optional)
            handoff_sta_thresh: Threshold value for AP handoff. (optional)
            handoff_roaming: Enable/disable client load balancing during
            roaming to avoid roaming delay (default = enable). (optional)
            deny_mac_list: List of MAC addresses that are denied access to this
            WTP, FortiAP, or AP. (optional)
            ap_country: Country in which this WTP, FortiAP, or AP will operate
            (default = NA, automatically use the country configured for the
            current VDOM). (optional)
            ip_fragment_preventing: Method(s) by which IP fragmentation is
            prevented for control and data packets through CAPWAP tunnel
            (default = tcp-mss-adjust). (optional)
            tun_mtu_uplink: The maximum transmission unit (MTU) of uplink
            CAPWAP tunnel (576 - 1500 bytes or 0; 0 means the local MTU of
            FortiAP; default = 0). (optional)
            tun_mtu_downlink: The MTU of downlink CAPWAP tunnel (576 - 1500
            bytes or 0; 0 means the local MTU of FortiAP; default = 0).
            (optional)
            split_tunneling_acl_path: Split tunneling ACL path is local/tunnel.
            (optional)
            split_tunneling_acl_local_ap_subnet: Enable/disable automatically
            adding local subnetwork of FortiAP to split-tunneling ACL (default
            = disable). (optional)
            split_tunneling_acl: Split tunneling ACL filter list. (optional)
            allowaccess: Control management access to the managed WTP, FortiAP,
            or AP. Separate entries with a space. (optional)
            login_passwd_change: Change or reset the administrator password of
            a managed WTP, FortiAP or AP (yes, default, or no, default = no).
            (optional)
            login_passwd: Set the managed WTP, FortiAP, or AP's administrator
            password. (optional)
            lldp: Enable/disable Link Layer Discovery Protocol (LLDP) for the
            WTP, FortiAP, or AP (default = enable). (optional)
            poe_mode: Set the WTP, FortiAP, or AP's PoE mode. (optional)
            usb_port: Enable/disable USB port of the WTP (default = enable).
            (optional)
            frequency_handoff: Enable/disable frequency handoff of clients to
            other channels (default = disable). (optional)
            ap_handoff: Enable/disable AP handoff of clients to other APs
            (default = disable). (optional)
            default_mesh_root: Configure default mesh root SSID when it is not
            included by radio's SSID configuration. (optional)
            radio_1: Configuration options for radio 1. (optional)
            radio_2: Configuration options for radio 2. (optional)
            radio_3: Configuration options for radio 3. (optional)
            radio_4: Configuration options for radio 4. (optional)
            lbs: Set various location based service (LBS) options. (optional)
            ext_info_enable: Enable/disable station/VAP/radio extension
            information. (optional)
            indoor_outdoor_deployment: Set to allow indoor/outdoor-only
            channels under regulatory rules (default = platform-determined).
            (optional)
            esl_ses_dongle: ESL SES-imagotag dongle configuration. (optional)
            console_login: Enable/disable FortiAP console login access (default
            = enable). (optional)
            wan_port_auth: Set WAN port authentication mode (default = none).
            (optional)
            wan_port_auth_usrname: Set WAN port 802.1x supplicant user name.
            (optional)
            wan_port_auth_password: Set WAN port 802.1x supplicant password.
            (optional)
            wan_port_auth_methods: WAN port 802.1x supplicant EAP methods
            (default = all). (optional)
            wan_port_auth_macsec: Enable/disable WAN port 802.1x supplicant
            MACsec policy (default = disable). (optional)
            apcfg_auto_cert: Enable/disable AP local auto cert configuration
            (default = disable). (optional)
            apcfg_auto_cert_enroll_protocol: Certificate enrollment protocol
            (default = none) (optional)
            apcfg_auto_cert_crypto_algo: Cryptography algorithm: rsa-1024,
            rsa-1536, rsa-2048, rsa-4096, ec-secp256r1, ec-secp384r1,
            ec-secp521r1 (default = ec-secp256r1) (optional)
            apcfg_auto_cert_est_server: Address and port for EST server (e.g. https://example.com:1234). (optional)
            apcfg_auto_cert_est_ca_id: CA identifier of the CA server for
            signing via EST. (optional)
            apcfg_auto_cert_est_http_username: HTTP Authentication username for
            signing via EST. (optional)
            apcfg_auto_cert_est_http_password: HTTP Authentication password for
            signing via EST. (optional)
            apcfg_auto_cert_est_subject: Subject e.g.
            "CN=User,DC=example,DC=COM" (default = CN=FortiAP,DC=local,DC=COM)
            (optional)
            apcfg_auto_cert_est_subject_alt_name: Subject alternative name
            (optional, e.g. "DNS:dns1.com,IP:192.168.1.99") (optional)
            apcfg_auto_cert_auto_regen_days: Number of days to wait before
            expiry of an updated local certificate is requested (0 = disabled)
            (default = 30). (optional)
            apcfg_auto_cert_est_https_ca: PEM format https CA Certificate.
            (optional)
            apcfg_auto_cert_scep_keytype: Key type (default = rsa) (optional)
            apcfg_auto_cert_scep_keysize: Key size: 1024, 1536, 2048, 4096
            (default 2048). (optional)
            apcfg_auto_cert_scep_ec_name: Elliptic curve name: secp256r1,
            secp384r1 and secp521r1. (default secp256r1). (optional)
            apcfg_auto_cert_scep_sub_fully_dn: Full DN of the subject (e.g
            C=US,ST=CA,L=Sunnyvale,O=Fortinet,OU=Dep1,emailAddress=test@example.com).
            There should be no space in between the attributes. Supported DN
            attributes (case-sensitive) are:C,ST,L,O,OU,emailAddress. The CN
            defaults to the device’s SN and cannot be changed. (optional)
            apcfg_auto_cert_scep_url: SCEP server URL. (optional)
            apcfg_auto_cert_scep_password: SCEP server challenge password for
            auto-regeneration. (optional)
            apcfg_auto_cert_scep_ca_id: CA identifier of the CA server for
            signing via SCEP. (optional)
            apcfg_auto_cert_scep_subject_alt_name: Subject alternative name
            (optional, e.g. "DNS:dns1.com,IP:192.168.1.99") (optional)
            apcfg_auto_cert_scep_https_ca: PEM format https CA Certificate.
            (optional)
            unii_4_5ghz_band: Enable/disable UNII-4 5Ghz band channels (default
            = disable). (optional)
            admin_auth_tacacs_plus_: Remote authentication server for admin
            user. (optional)
            admin_restrict_local: Enable/disable local admin authentication
            restriction when remote authenticator is up and running (default =
            disable). (optional)
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
        endpoint = "/wireless-controller/wtp-profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if platform is not None:
            data_payload["platform"] = platform
        if control_message_offload is not None:
            data_payload["control-message-offload"] = control_message_offload
        if bonjour_profile is not None:
            data_payload["bonjour-profile"] = bonjour_profile
        if apcfg_profile is not None:
            data_payload["apcfg-profile"] = apcfg_profile
        if apcfg_mesh is not None:
            data_payload["apcfg-mesh"] = apcfg_mesh
        if apcfg_mesh_ap_type is not None:
            data_payload["apcfg-mesh-ap-type"] = apcfg_mesh_ap_type
        if apcfg_mesh_ssid is not None:
            data_payload["apcfg-mesh-ssid"] = apcfg_mesh_ssid
        if apcfg_mesh_eth_bridge is not None:
            data_payload["apcfg-mesh-eth-bridge"] = apcfg_mesh_eth_bridge
        if ble_profile is not None:
            data_payload["ble-profile"] = ble_profile
        if lw_profile is not None:
            data_payload["lw-profile"] = lw_profile
        if syslog_profile is not None:
            data_payload["syslog-profile"] = syslog_profile
        if wan_port_mode is not None:
            data_payload["wan-port-mode"] = wan_port_mode
        if lan is not None:
            data_payload["lan"] = lan
        if energy_efficient_ethernet is not None:
            data_payload["energy-efficient-ethernet"] = (
                energy_efficient_ethernet
            )
        if led_state is not None:
            data_payload["led-state"] = led_state
        if led_schedules is not None:
            data_payload["led-schedules"] = led_schedules
        if dtls_policy is not None:
            data_payload["dtls-policy"] = dtls_policy
        if dtls_in_kernel is not None:
            data_payload["dtls-in-kernel"] = dtls_in_kernel
        if max_clients is not None:
            data_payload["max-clients"] = max_clients
        if handoff_rssi is not None:
            data_payload["handoff-rssi"] = handoff_rssi
        if handoff_sta_thresh is not None:
            data_payload["handoff-sta-thresh"] = handoff_sta_thresh
        if handoff_roaming is not None:
            data_payload["handoff-roaming"] = handoff_roaming
        if deny_mac_list is not None:
            data_payload["deny-mac-list"] = deny_mac_list
        if ap_country is not None:
            data_payload["ap-country"] = ap_country
        if ip_fragment_preventing is not None:
            data_payload["ip-fragment-preventing"] = ip_fragment_preventing
        if tun_mtu_uplink is not None:
            data_payload["tun-mtu-uplink"] = tun_mtu_uplink
        if tun_mtu_downlink is not None:
            data_payload["tun-mtu-downlink"] = tun_mtu_downlink
        if split_tunneling_acl_path is not None:
            data_payload["split-tunneling-acl-path"] = split_tunneling_acl_path
        if split_tunneling_acl_local_ap_subnet is not None:
            data_payload["split-tunneling-acl-local-ap-subnet"] = (
                split_tunneling_acl_local_ap_subnet
            )
        if split_tunneling_acl is not None:
            data_payload["split-tunneling-acl"] = split_tunneling_acl
        if allowaccess is not None:
            data_payload["allowaccess"] = allowaccess
        if login_passwd_change is not None:
            data_payload["login-passwd-change"] = login_passwd_change
        if login_passwd is not None:
            data_payload["login-passwd"] = login_passwd
        if lldp is not None:
            data_payload["lldp"] = lldp
        if poe_mode is not None:
            data_payload["poe-mode"] = poe_mode
        if usb_port is not None:
            data_payload["usb-port"] = usb_port
        if frequency_handoff is not None:
            data_payload["frequency-handof"] = frequency_handoff
        if ap_handoff is not None:
            data_payload["ap-handof"] = ap_handoff
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
        if lbs is not None:
            data_payload["lbs"] = lbs
        if ext_info_enable is not None:
            data_payload["ext-info-enable"] = ext_info_enable
        if indoor_outdoor_deployment is not None:
            data_payload["indoor-outdoor-deployment"] = (
                indoor_outdoor_deployment
            )
        if esl_ses_dongle is not None:
            data_payload["esl-ses-dongle"] = esl_ses_dongle
        if console_login is not None:
            data_payload["console-login"] = console_login
        if wan_port_auth is not None:
            data_payload["wan-port-auth"] = wan_port_auth
        if wan_port_auth_usrname is not None:
            data_payload["wan-port-auth-usrname"] = wan_port_auth_usrname
        if wan_port_auth_password is not None:
            data_payload["wan-port-auth-password"] = wan_port_auth_password
        if wan_port_auth_methods is not None:
            data_payload["wan-port-auth-methods"] = wan_port_auth_methods
        if wan_port_auth_macsec is not None:
            data_payload["wan-port-auth-macsec"] = wan_port_auth_macsec
        if apcfg_auto_cert is not None:
            data_payload["apcfg-auto-cert"] = apcfg_auto_cert
        if apcfg_auto_cert_enroll_protocol is not None:
            data_payload["apcfg-auto-cert-enroll-protocol"] = (
                apcfg_auto_cert_enroll_protocol
            )
        if apcfg_auto_cert_crypto_algo is not None:
            data_payload["apcfg-auto-cert-crypto-algo"] = (
                apcfg_auto_cert_crypto_algo
            )
        if apcfg_auto_cert_est_server is not None:
            data_payload["apcfg-auto-cert-est-server"] = (
                apcfg_auto_cert_est_server
            )
        if apcfg_auto_cert_est_ca_id is not None:
            data_payload["apcfg-auto-cert-est-ca-id"] = (
                apcfg_auto_cert_est_ca_id
            )
        if apcfg_auto_cert_est_http_username is not None:
            data_payload["apcfg-auto-cert-est-http-username"] = (
                apcfg_auto_cert_est_http_username
            )
        if apcfg_auto_cert_est_http_password is not None:
            data_payload["apcfg-auto-cert-est-http-password"] = (
                apcfg_auto_cert_est_http_password
            )
        if apcfg_auto_cert_est_subject is not None:
            data_payload["apcfg-auto-cert-est-subject"] = (
                apcfg_auto_cert_est_subject
            )
        if apcfg_auto_cert_est_subject_alt_name is not None:
            data_payload["apcfg-auto-cert-est-subject-alt-name"] = (
                apcfg_auto_cert_est_subject_alt_name
            )
        if apcfg_auto_cert_auto_regen_days is not None:
            data_payload["apcfg-auto-cert-auto-regen-days"] = (
                apcfg_auto_cert_auto_regen_days
            )
        if apcfg_auto_cert_est_https_ca is not None:
            data_payload["apcfg-auto-cert-est-https-ca"] = (
                apcfg_auto_cert_est_https_ca
            )
        if apcfg_auto_cert_scep_keytype is not None:
            data_payload["apcfg-auto-cert-scep-keytype"] = (
                apcfg_auto_cert_scep_keytype
            )
        if apcfg_auto_cert_scep_keysize is not None:
            data_payload["apcfg-auto-cert-scep-keysize"] = (
                apcfg_auto_cert_scep_keysize
            )
        if apcfg_auto_cert_scep_ec_name is not None:
            data_payload["apcfg-auto-cert-scep-ec-name"] = (
                apcfg_auto_cert_scep_ec_name
            )
        if apcfg_auto_cert_scep_sub_fully_dn is not None:
            data_payload["apcfg-auto-cert-scep-sub-fully-dn"] = (
                apcfg_auto_cert_scep_sub_fully_dn
            )
        if apcfg_auto_cert_scep_url is not None:
            data_payload["apcfg-auto-cert-scep-url"] = apcfg_auto_cert_scep_url
        if apcfg_auto_cert_scep_password is not None:
            data_payload["apcfg-auto-cert-scep-password"] = (
                apcfg_auto_cert_scep_password
            )
        if apcfg_auto_cert_scep_ca_id is not None:
            data_payload["apcfg-auto-cert-scep-ca-id"] = (
                apcfg_auto_cert_scep_ca_id
            )
        if apcfg_auto_cert_scep_subject_alt_name is not None:
            data_payload["apcfg-auto-cert-scep-subject-alt-name"] = (
                apcfg_auto_cert_scep_subject_alt_name
            )
        if apcfg_auto_cert_scep_https_ca is not None:
            data_payload["apcfg-auto-cert-scep-https-ca"] = (
                apcfg_auto_cert_scep_https_ca
            )
        if unii_4_5ghz_band is not None:
            data_payload["unii-4-5ghz-band"] = unii_4_5ghz_band
        if admin_auth_tacacs_plus_ is not None:
            data_payload["admin-auth-tacacs+"] = admin_auth_tacacs_plus_
        if admin_restrict_local is not None:
            data_payload["admin-restrict-local"] = admin_restrict_local
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
