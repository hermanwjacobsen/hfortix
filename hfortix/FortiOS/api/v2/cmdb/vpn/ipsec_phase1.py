"""
FortiOS CMDB - Cmdb Vpn Ipsec Phase1

Configuration endpoint for managing cmdb vpn ipsec phase1 objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec_phase1
    POST   /cmdb/vpn/ipsec_phase1
    GET    /cmdb/vpn/ipsec_phase1
    PUT    /cmdb/vpn/ipsec_phase1/{identifier}
    DELETE /cmdb/vpn/ipsec_phase1/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn.ipsec_phase1.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.vpn.ipsec_phase1.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.vpn.ipsec_phase1.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.vpn.ipsec_phase1.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.vpn.ipsec_phase1.delete(name="item_name")

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


class IpsecPhase1:
    """
    Ipsecphase1 Operations.

    Provides CRUD operations for FortiOS ipsecphase1 configuration.

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
        Initialize IpsecPhase1 endpoint.

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
            endpoint = f"/vpn.ipsec/phase1/{name}"
        else:
            endpoint = "/vpn.ipsec/phase1"
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
        type: str | None = None,
        interface: str | None = None,
        ike_version: str | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: list | None = None,
        authmethod: str | None = None,
        authmethod_remote: str | None = None,
        mode: str | None = None,
        peertype: str | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        mode_cfg: str | None = None,
        mode_cfg_allow_client_selector: str | None = None,
        assign_ip: str | None = None,
        assign_ip_from: str | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: str | None = None,
        ipv4_dns_server1: str | None = None,
        ipv4_dns_server2: str | None = None,
        ipv4_dns_server3: str | None = None,
        internal_domain_list: list | None = None,
        dns_suffix_search: list | None = None,
        ipv4_wins_server1: str | None = None,
        ipv4_wins_server2: str | None = None,
        ipv4_exclude_range: list | None = None,
        ipv4_split_include: str | None = None,
        split_include_service: str | None = None,
        ipv4_name: str | None = None,
        ipv6_start_ip: str | None = None,
        ipv6_end_ip: str | None = None,
        ipv6_prefix: int | None = None,
        ipv6_dns_server1: str | None = None,
        ipv6_dns_server2: str | None = None,
        ipv6_dns_server3: str | None = None,
        ipv6_exclude_range: list | None = None,
        ipv6_split_include: str | None = None,
        ipv6_name: str | None = None,
        ip_delay_interval: int | None = None,
        unity_support: str | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: str | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: str | None = None,
        client_auto_negotiate: str | None = None,
        client_keep_alive: str | None = None,
        backup_gateway: list | None = None,
        proposal: str | None = None,
        add_route: str | None = None,
        add_gw_route: str | None = None,
        psksecret: str | None = None,
        psksecret_remote: str | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: str | None = None,
        auto_negotiate: str | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: str | None = None,
        dpd: str | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: str | None = None,
        send_cert_chain: str | None = None,
        dhgrp: str | None = None,
        addke1: str | None = None,
        addke2: str | None = None,
        addke3: str | None = None,
        addke4: str | None = None,
        addke5: str | None = None,
        addke6: str | None = None,
        addke7: str | None = None,
        suite_b: str | None = None,
        eap: str | None = None,
        eap_identity: str | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: str | None = None,
        acct_verify: str | None = None,
        ppk: str | None = None,
        ppk_secret: str | None = None,
        ppk_identity: str | None = None,
        wizard_type: str | None = None,
        xauthtype: str | None = None,
        reauth: str | None = None,
        authusr: str | None = None,
        authpasswd: str | None = None,
        group_authentication: str | None = None,
        group_authentication_secret: str | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: str | None = None,
        idle_timeout: str | None = None,
        shared_idle_timeout: str | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: str | None = None,
        fgsp_sync: str | None = None,
        inbound_dscp_copy: str | None = None,
        nattraversal: str | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: str | None = None,
        azure_ad_autoconnect: str | None = None,
        client_resume: str | None = None,
        client_resume_interval: int | None = None,
        rekey: str | None = None,
        digital_signature_auth: str | None = None,
        signature_hash_alg: str | None = None,
        rsa_signature_format: str | None = None,
        rsa_signature_hash_override: str | None = None,
        enforce_unique_id: str | None = None,
        cert_id_validation: str | None = None,
        fec_egress: str | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: str | None = None,
        fec_redundant: int | None = None,
        fec_ingress: str | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: str | None = None,
        network_id: int | None = None,
        dev_id_notification: str | None = None,
        dev_id: str | None = None,
        loopback_asymroute: str | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: str | None = None,
        ipv6_auto_linklocal: str | None = None,
        ems_sn_check: str | None = None,
        cert_trust_store: str | None = None,
        qkd: str | None = None,
        qkd_hybrid: str | None = None,
        qkd_profile: str | None = None,
        transport: str | None = None,
        fortinet_esp: str | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: str | None = None,
        remote_gw_subnet: str | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: list | None = None,
        remote_gw6_match: str | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: str | None = None,
        cert_peer_username_strip: str | None = None,
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
            name: IPsec remote gateway name. (optional)
            type: Remote gateway type. (optional)
            interface: Local physical, aggregate, or VLAN outgoing interface.
            (optional)
            ike_version: IKE protocol version. (optional)
            remote_gw: Remote VPN gateway. (optional)
            local_gw: Local VPN gateway. (optional)
            remotegw_ddns: Domain name of remote gateway. For example,
            name.ddns.com. (optional)
            keylife: Time to wait in seconds before phase 1 encryption key
            expires. (optional)
            certificate: Names of up to 4 signed personal certificates.
            (optional)
            authmethod: Authentication method. (optional)
            authmethod_remote: Authentication method (remote side). (optional)
            mode: ID protection mode used to establish a secure channel.
            (optional)
            peertype: Accept this peer type. (optional)
            peerid: Accept this peer identity. (optional)
            usrgrp: User group name for dialup peers. (optional)
            peer: Accept this peer certificate. (optional)
            peergrp: Accept this peer certificate group. (optional)
            mode_cfg: Enable/disable configuration method. (optional)
            mode_cfg_allow_client_selector: Enable/disable mode-cfg client to
            use custom phase2 selectors. (optional)
            assign_ip: Enable/disable assignment of IP to IPsec interface via
            configuration method. (optional)
            assign_ip_from: Method by which the IP address will be assigned.
            (optional)
            ipv4_start_ip: Start of IPv4 range. (optional)
            ipv4_end_ip: End of IPv4 range. (optional)
            ipv4_netmask: IPv4 Netmask. (optional)
            dhcp_ra_giaddr: Relay agent gateway IP address to use in the giaddr
            field of DHCP requests. (optional)
            dhcp6_ra_linkaddr: Relay agent IPv6 link address to use in DHCP6
            requests. (optional)
            dns_mode: DNS server mode. (optional)
            ipv4_dns_server1: IPv4 DNS server 1. (optional)
            ipv4_dns_server2: IPv4 DNS server 2. (optional)
            ipv4_dns_server3: IPv4 DNS server 3. (optional)
            internal_domain_list: One or more internal domain names in quotes
            separated by spaces. (optional)
            dns_suffix_search: One or more DNS domain name suffixes in quotes
            separated by spaces. (optional)
            ipv4_wins_server1: WINS server 1. (optional)
            ipv4_wins_server2: WINS server 2. (optional)
            ipv4_exclude_range: Configuration Method IPv4 exclude ranges.
            (optional)
            ipv4_split_include: IPv4 split-include subnets. (optional)
            split_include_service: Split-include services. (optional)
            ipv4_name: IPv4 address name. (optional)
            ipv6_start_ip: Start of IPv6 range. (optional)
            ipv6_end_ip: End of IPv6 range. (optional)
            ipv6_prefix: IPv6 prefix. (optional)
            ipv6_dns_server1: IPv6 DNS server 1. (optional)
            ipv6_dns_server2: IPv6 DNS server 2. (optional)
            ipv6_dns_server3: IPv6 DNS server 3. (optional)
            ipv6_exclude_range: Configuration method IPv6 exclude ranges.
            (optional)
            ipv6_split_include: IPv6 split-include subnets. (optional)
            ipv6_name: IPv6 address name. (optional)
            ip_delay_interval: IP address reuse delay interval in seconds (0 -
            28800). (optional)
            unity_support: Enable/disable support for Cisco UNITY Configuration
            Method extensions. (optional)
            domain: Instruct unity clients about the single default DNS domain.
            (optional)
            banner: Message that unity client should display after connecting.
            (optional)
            include_local_lan: Enable/disable allow local LAN access on unity
            clients. (optional)
            ipv4_split_exclude: IPv4 subnets that should not be sent over the
            IPsec tunnel. (optional)
            ipv6_split_exclude: IPv6 subnets that should not be sent over the
            IPsec tunnel. (optional)
            save_password: Enable/disable saving XAuth username and password on
            VPN clients. (optional)
            client_auto_negotiate: Enable/disable allowing the VPN client to
            bring up the tunnel when there is no traffic. (optional)
            client_keep_alive: Enable/disable allowing the VPN client to keep
            the tunnel up when there is no traffic. (optional)
            backup_gateway: Instruct unity clients about the backup gateway
            address(es). (optional)
            proposal: Phase1 proposal. (optional)
            add_route: Enable/disable control addition of a route to peer
            destination selector. (optional)
            add_gw_route: Enable/disable automatically add a route to the
            remote gateway. (optional)
            psksecret: Pre-shared secret for PSK authentication (ASCII string
            or hexadecimal encoded with a leading 0x). (optional)
            psksecret_remote: Pre-shared secret for remote side PSK
            authentication (ASCII string or hexadecimal encoded with a leading
            0x). (optional)
            keepalive: NAT-T keep alive interval. (optional)
            distance: Distance for routes added by IKE (1 - 255). (optional)
            priority: Priority for routes added by IKE (1 - 65535). (optional)
            localid: Local ID. (optional)
            localid_type: Local ID type. (optional)
            auto_negotiate: Enable/disable automatic initiation of IKE SA
            negotiation. (optional)
            negotiate_timeout: IKE SA negotiation timeout in seconds (1 - 300).
            (optional)
            fragmentation: Enable/disable fragment IKE message on
            re-transmission. (optional)
            dpd: Dead Peer Detection mode. (optional)
            dpd_retrycount: Number of DPD retry attempts. (optional)
            dpd_retryinterval: DPD retry interval. (optional)
            comments: Comment. (optional)
            npu_offload: Enable/disable offloading NPU. (optional)
            send_cert_chain: Enable/disable sending certificate chain.
            (optional)
            dhgrp: DH group. (optional)
            addke1: ADDKE1 group. (optional)
            addke2: ADDKE2 group. (optional)
            addke3: ADDKE3 group. (optional)
            addke4: ADDKE4 group. (optional)
            addke5: ADDKE5 group. (optional)
            addke6: ADDKE6 group. (optional)
            addke7: ADDKE7 group. (optional)
            suite_b: Use Suite-B. (optional)
            eap: Enable/disable IKEv2 EAP authentication. (optional)
            eap_identity: IKEv2 EAP peer identity type. (optional)
            eap_exclude_peergrp: Peer group excluded from EAP authentication.
            (optional)
            eap_cert_auth: Enable/disable peer certificate authentication in
            addition to EAP if peer is a FortiClient endpoint. (optional)
            acct_verify: Enable/disable verification of RADIUS accounting
            record. (optional)
            ppk: Enable/disable IKEv2 Postquantum Preshared Key (PPK).
            (optional)
            ppk_secret: IKEv2 Postquantum Preshared Key (ASCII string or
            hexadecimal encoded with a leading 0x). (optional)
            ppk_identity: IKEv2 Postquantum Preshared Key Identity. (optional)
            wizard_type: GUI VPN Wizard Type. (optional)
            xauthtype: XAuth type. (optional)
            reauth: Enable/disable re-authentication upon IKE SA lifetime
            expiration. (optional)
            authusr: XAuth user name. (optional)
            authpasswd: XAuth password (max 35 characters). (optional)
            group_authentication: Enable/disable IKEv2 IDi group
            authentication. (optional)
            group_authentication_secret: Password for IKEv2 ID group
            authentication. ASCII string or hexadecimal indicated by a leading
            0x. (optional)
            authusrgrp: Authentication user group. (optional)
            mesh_selector_type: Add selectors containing subsets of the
            configuration depending on traffic. (optional)
            idle_timeout: Enable/disable IPsec tunnel idle timeout. (optional)
            shared_idle_timeout: Enable/disable IPsec tunnel shared idle
            timeout. (optional)
            idle_timeoutinterval: IPsec tunnel idle timeout in minutes (5 -
            43200). (optional)
            ha_sync_esp_seqno: Enable/disable sequence number jump ahead for
            IPsec HA. (optional)
            fgsp_sync: Enable/disable IPsec syncing of tunnels for FGSP IPsec.
            (optional)
            inbound_dscp_copy: Enable/disable copy the dscp in the ESP header
            to the inner IP Header. (optional)
            nattraversal: Enable/disable NAT traversal. (optional)
            fragmentation_mtu: IKE fragmentation MTU (500 - 16000). (optional)
            childless_ike: Enable/disable childless IKEv2 initiation (RFC
            6023). (optional)
            azure_ad_autoconnect: Enable/disable Azure AD Auto-Connect for
            FortiClient. (optional)
            client_resume: Enable/disable resumption of offline FortiClient
            sessions. When a FortiClient enabled laptop is closed or enters
            sleep/hibernate mode, enabling this feature allows FortiClient to
            keep the tunnel during this period, and allows users to immediately
            resume using the IPsec tunnel when the device wakes up. (optional)
            client_resume_interval: Maximum time in seconds during which a VPN
            client may resume using a tunnel after a client PC has entered
            sleep mode or temporarily lost its network connection (120 -
            172800, default = 7200). (optional)
            rekey: Enable/disable phase1 rekey. (optional)
            digital_signature_auth: Enable/disable IKEv2 Digital Signature
            Authentication (RFC 7427). (optional)
            signature_hash_alg: Digital Signature Authentication hash
            algorithms. (optional)
            rsa_signature_format: Digital Signature Authentication RSA
            signature format. (optional)
            rsa_signature_hash_override: Enable/disable IKEv2 RSA signature
            hash algorithm override. (optional)
            enforce_unique_id: Enable/disable peer ID uniqueness check.
            (optional)
            cert_id_validation: Enable/disable cross validation of peer ID and
            the identity in the peer's certificate as specified in RFC 4945.
            (optional)
            fec_egress: Enable/disable Forward Error Correction for egress
            IPsec traffic. (optional)
            fec_send_timeout: Timeout in milliseconds before sending Forward
            Error Correction packets (1 - 1000). (optional)
            fec_base: Number of base Forward Error Correction packets (1 - 20).
            (optional)
            fec_codec: Forward Error Correction encoding/decoding algorithm.
            (optional)
            fec_redundant: Number of redundant Forward Error Correction packets
            (1 - 5 for reed-solomon, 1 for xor). (optional)
            fec_ingress: Enable/disable Forward Error Correction for ingress
            IPsec traffic. (optional)
            fec_receive_timeout: Timeout in milliseconds before dropping
            Forward Error Correction packets (1 - 1000). (optional)
            fec_health_check: SD-WAN health check. (optional)
            fec_mapping_profile: Forward Error Correction (FEC) mapping
            profile. (optional)
            network_overlay: Enable/disable network overlays. (optional)
            network_id: VPN gateway network ID. (optional)
            dev_id_notification: Enable/disable device ID notification.
            (optional)
            dev_id: Device ID carried by the device ID notification. (optional)
            loopback_asymroute: Enable/disable asymmetric routing for IKE
            traffic on loopback interface. (optional)
            link_cost: VPN tunnel underlay link cost. (optional)
            kms: Key Management Services server. (optional)
            exchange_fgt_device_id: Enable/disable device identifier exchange
            with peer FortiGate units for use of VPN monitor data by
            FortiManager. (optional)
            ipv6_auto_linklocal: Enable/disable auto generation of IPv6
            link-local address using last 8 bytes of mode-cfg assigned IPv6
            address. (optional)
            ems_sn_check: Enable/disable verification of EMS serial number.
            (optional)
            cert_trust_store: CA certificate trust store. (optional)
            qkd: Enable/disable use of Quantum Key Distribution (QKD) server.
            (optional)
            qkd_hybrid: Enable/disable use of Quantum Key Distribution (QKD)
            hybrid keys. (optional)
            qkd_profile: Quantum Key Distribution (QKD) server profile.
            (optional)
            transport: Set IKE transport protocol. (optional)
            fortinet_esp: Enable/disable Fortinet ESP encapsulation. (optional)
            auto_transport_threshold: Timeout in seconds before falling back to
            next transport protocol. (optional)
            remote_gw_match: Set type of IPv4 remote gateway address matching.
            (optional)
            remote_gw_subnet: IPv4 address and subnet mask. (optional)
            remote_gw_start_ip: First IPv4 address in the range. (optional)
            remote_gw_end_ip: Last IPv4 address in the range. (optional)
            remote_gw_country: IPv4 addresses associated to a specific country.
            (optional)
            remote_gw_ztna_tags: IPv4 ZTNA posture tags. (optional)
            remote_gw6_match: Set type of IPv6 remote gateway address matching.
            (optional)
            remote_gw6_subnet: IPv6 address and prefix. (optional)
            remote_gw6_start_ip: First IPv6 address in the range. (optional)
            remote_gw6_end_ip: Last IPv6 address in the range. (optional)
            remote_gw6_country: IPv6 addresses associated to a specific
            country. (optional)
            cert_peer_username_validation: Enable/disable cross validation of
            peer username and the identity in the peer's certificate.
            (optional)
            cert_peer_username_strip: Enable/disable domain stripping on
            certificate identity. (optional)
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
        endpoint = f"/vpn.ipsec/phase1/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if type is not None:
            data_payload["type"] = type
        if interface is not None:
            data_payload["interface"] = interface
        if ike_version is not None:
            data_payload["ike-version"] = ike_version
        if remote_gw is not None:
            data_payload["remote-gw"] = remote_gw
        if local_gw is not None:
            data_payload["local-gw"] = local_gw
        if remotegw_ddns is not None:
            data_payload["remotegw-ddns"] = remotegw_ddns
        if keylife is not None:
            data_payload["keylife"] = keylife
        if certificate is not None:
            data_payload["certificate"] = certificate
        if authmethod is not None:
            data_payload["authmethod"] = authmethod
        if authmethod_remote is not None:
            data_payload["authmethod-remote"] = authmethod_remote
        if mode is not None:
            data_payload["mode"] = mode
        if peertype is not None:
            data_payload["peertype"] = peertype
        if peerid is not None:
            data_payload["peerid"] = peerid
        if usrgrp is not None:
            data_payload["usrgrp"] = usrgrp
        if peer is not None:
            data_payload["peer"] = peer
        if peergrp is not None:
            data_payload["peergrp"] = peergrp
        if mode_cfg is not None:
            data_payload["mode-cfg"] = mode_cfg
        if mode_cfg_allow_client_selector is not None:
            data_payload["mode-cfg-allow-client-selector"] = (
                mode_cfg_allow_client_selector
            )
        if assign_ip is not None:
            data_payload["assign-ip"] = assign_ip
        if assign_ip_from is not None:
            data_payload["assign-ip-from"] = assign_ip_from
        if ipv4_start_ip is not None:
            data_payload["ipv4-start-ip"] = ipv4_start_ip
        if ipv4_end_ip is not None:
            data_payload["ipv4-end-ip"] = ipv4_end_ip
        if ipv4_netmask is not None:
            data_payload["ipv4-netmask"] = ipv4_netmask
        if dhcp_ra_giaddr is not None:
            data_payload["dhcp-ra-giaddr"] = dhcp_ra_giaddr
        if dhcp6_ra_linkaddr is not None:
            data_payload["dhcp6-ra-linkaddr"] = dhcp6_ra_linkaddr
        if dns_mode is not None:
            data_payload["dns-mode"] = dns_mode
        if ipv4_dns_server1 is not None:
            data_payload["ipv4-dns-server1"] = ipv4_dns_server1
        if ipv4_dns_server2 is not None:
            data_payload["ipv4-dns-server2"] = ipv4_dns_server2
        if ipv4_dns_server3 is not None:
            data_payload["ipv4-dns-server3"] = ipv4_dns_server3
        if internal_domain_list is not None:
            data_payload["internal-domain-list"] = internal_domain_list
        if dns_suffix_search is not None:
            data_payload["dns-suffix-search"] = dns_suffix_search
        if ipv4_wins_server1 is not None:
            data_payload["ipv4-wins-server1"] = ipv4_wins_server1
        if ipv4_wins_server2 is not None:
            data_payload["ipv4-wins-server2"] = ipv4_wins_server2
        if ipv4_exclude_range is not None:
            data_payload["ipv4-exclude-range"] = ipv4_exclude_range
        if ipv4_split_include is not None:
            data_payload["ipv4-split-include"] = ipv4_split_include
        if split_include_service is not None:
            data_payload["split-include-service"] = split_include_service
        if ipv4_name is not None:
            data_payload["ipv4-name"] = ipv4_name
        if ipv6_start_ip is not None:
            data_payload["ipv6-start-ip"] = ipv6_start_ip
        if ipv6_end_ip is not None:
            data_payload["ipv6-end-ip"] = ipv6_end_ip
        if ipv6_prefix is not None:
            data_payload["ipv6-prefix"] = ipv6_prefix
        if ipv6_dns_server1 is not None:
            data_payload["ipv6-dns-server1"] = ipv6_dns_server1
        if ipv6_dns_server2 is not None:
            data_payload["ipv6-dns-server2"] = ipv6_dns_server2
        if ipv6_dns_server3 is not None:
            data_payload["ipv6-dns-server3"] = ipv6_dns_server3
        if ipv6_exclude_range is not None:
            data_payload["ipv6-exclude-range"] = ipv6_exclude_range
        if ipv6_split_include is not None:
            data_payload["ipv6-split-include"] = ipv6_split_include
        if ipv6_name is not None:
            data_payload["ipv6-name"] = ipv6_name
        if ip_delay_interval is not None:
            data_payload["ip-delay-interval"] = ip_delay_interval
        if unity_support is not None:
            data_payload["unity-support"] = unity_support
        if domain is not None:
            data_payload["domain"] = domain
        if banner is not None:
            data_payload["banner"] = banner
        if include_local_lan is not None:
            data_payload["include-local-lan"] = include_local_lan
        if ipv4_split_exclude is not None:
            data_payload["ipv4-split-exclude"] = ipv4_split_exclude
        if ipv6_split_exclude is not None:
            data_payload["ipv6-split-exclude"] = ipv6_split_exclude
        if save_password is not None:
            data_payload["save-password"] = save_password
        if client_auto_negotiate is not None:
            data_payload["client-auto-negotiate"] = client_auto_negotiate
        if client_keep_alive is not None:
            data_payload["client-keep-alive"] = client_keep_alive
        if backup_gateway is not None:
            data_payload["backup-gateway"] = backup_gateway
        if proposal is not None:
            data_payload["proposal"] = proposal
        if add_route is not None:
            data_payload["add-route"] = add_route
        if add_gw_route is not None:
            data_payload["add-gw-route"] = add_gw_route
        if psksecret is not None:
            data_payload["psksecret"] = psksecret
        if psksecret_remote is not None:
            data_payload["psksecret-remote"] = psksecret_remote
        if keepalive is not None:
            data_payload["keepalive"] = keepalive
        if distance is not None:
            data_payload["distance"] = distance
        if priority is not None:
            data_payload["priority"] = priority
        if localid is not None:
            data_payload["localid"] = localid
        if localid_type is not None:
            data_payload["localid-type"] = localid_type
        if auto_negotiate is not None:
            data_payload["auto-negotiate"] = auto_negotiate
        if negotiate_timeout is not None:
            data_payload["negotiate-timeout"] = negotiate_timeout
        if fragmentation is not None:
            data_payload["fragmentation"] = fragmentation
        if dpd is not None:
            data_payload["dpd"] = dpd
        if dpd_retrycount is not None:
            data_payload["dpd-retrycount"] = dpd_retrycount
        if dpd_retryinterval is not None:
            data_payload["dpd-retryinterval"] = dpd_retryinterval
        if comments is not None:
            data_payload["comments"] = comments
        if npu_offload is not None:
            data_payload["npu-offload"] = npu_offload
        if send_cert_chain is not None:
            data_payload["send-cert-chain"] = send_cert_chain
        if dhgrp is not None:
            data_payload["dhgrp"] = dhgrp
        if addke1 is not None:
            data_payload["addke1"] = addke1
        if addke2 is not None:
            data_payload["addke2"] = addke2
        if addke3 is not None:
            data_payload["addke3"] = addke3
        if addke4 is not None:
            data_payload["addke4"] = addke4
        if addke5 is not None:
            data_payload["addke5"] = addke5
        if addke6 is not None:
            data_payload["addke6"] = addke6
        if addke7 is not None:
            data_payload["addke7"] = addke7
        if suite_b is not None:
            data_payload["suite-b"] = suite_b
        if eap is not None:
            data_payload["eap"] = eap
        if eap_identity is not None:
            data_payload["eap-identity"] = eap_identity
        if eap_exclude_peergrp is not None:
            data_payload["eap-exclude-peergrp"] = eap_exclude_peergrp
        if eap_cert_auth is not None:
            data_payload["eap-cert-auth"] = eap_cert_auth
        if acct_verify is not None:
            data_payload["acct-verify"] = acct_verify
        if ppk is not None:
            data_payload["ppk"] = ppk
        if ppk_secret is not None:
            data_payload["ppk-secret"] = ppk_secret
        if ppk_identity is not None:
            data_payload["ppk-identity"] = ppk_identity
        if wizard_type is not None:
            data_payload["wizard-type"] = wizard_type
        if xauthtype is not None:
            data_payload["xauthtype"] = xauthtype
        if reauth is not None:
            data_payload["reauth"] = reauth
        if authusr is not None:
            data_payload["authusr"] = authusr
        if authpasswd is not None:
            data_payload["authpasswd"] = authpasswd
        if group_authentication is not None:
            data_payload["group-authentication"] = group_authentication
        if group_authentication_secret is not None:
            data_payload["group-authentication-secret"] = (
                group_authentication_secret
            )
        if authusrgrp is not None:
            data_payload["authusrgrp"] = authusrgrp
        if mesh_selector_type is not None:
            data_payload["mesh-selector-type"] = mesh_selector_type
        if idle_timeout is not None:
            data_payload["idle-timeout"] = idle_timeout
        if shared_idle_timeout is not None:
            data_payload["shared-idle-timeout"] = shared_idle_timeout
        if idle_timeoutinterval is not None:
            data_payload["idle-timeoutinterval"] = idle_timeoutinterval
        if ha_sync_esp_seqno is not None:
            data_payload["ha-sync-esp-seqno"] = ha_sync_esp_seqno
        if fgsp_sync is not None:
            data_payload["fgsp-sync"] = fgsp_sync
        if inbound_dscp_copy is not None:
            data_payload["inbound-dscp-copy"] = inbound_dscp_copy
        if nattraversal is not None:
            data_payload["nattraversal"] = nattraversal
        if fragmentation_mtu is not None:
            data_payload["fragmentation-mtu"] = fragmentation_mtu
        if childless_ike is not None:
            data_payload["childless-ike"] = childless_ike
        if azure_ad_autoconnect is not None:
            data_payload["azure-ad-autoconnect"] = azure_ad_autoconnect
        if client_resume is not None:
            data_payload["client-resume"] = client_resume
        if client_resume_interval is not None:
            data_payload["client-resume-interval"] = client_resume_interval
        if rekey is not None:
            data_payload["rekey"] = rekey
        if digital_signature_auth is not None:
            data_payload["digital-signature-auth"] = digital_signature_auth
        if signature_hash_alg is not None:
            data_payload["signature-hash-alg"] = signature_hash_alg
        if rsa_signature_format is not None:
            data_payload["rsa-signature-format"] = rsa_signature_format
        if rsa_signature_hash_override is not None:
            data_payload["rsa-signature-hash-override"] = (
                rsa_signature_hash_override
            )
        if enforce_unique_id is not None:
            data_payload["enforce-unique-id"] = enforce_unique_id
        if cert_id_validation is not None:
            data_payload["cert-id-validation"] = cert_id_validation
        if fec_egress is not None:
            data_payload["fec-egress"] = fec_egress
        if fec_send_timeout is not None:
            data_payload["fec-send-timeout"] = fec_send_timeout
        if fec_base is not None:
            data_payload["fec-base"] = fec_base
        if fec_codec is not None:
            data_payload["fec-codec"] = fec_codec
        if fec_redundant is not None:
            data_payload["fec-redundant"] = fec_redundant
        if fec_ingress is not None:
            data_payload["fec-ingress"] = fec_ingress
        if fec_receive_timeout is not None:
            data_payload["fec-receive-timeout"] = fec_receive_timeout
        if fec_health_check is not None:
            data_payload["fec-health-check"] = fec_health_check
        if fec_mapping_profile is not None:
            data_payload["fec-mapping-profile"] = fec_mapping_profile
        if network_overlay is not None:
            data_payload["network-overlay"] = network_overlay
        if network_id is not None:
            data_payload["network-id"] = network_id
        if dev_id_notification is not None:
            data_payload["dev-id-notification"] = dev_id_notification
        if dev_id is not None:
            data_payload["dev-id"] = dev_id
        if loopback_asymroute is not None:
            data_payload["loopback-asymroute"] = loopback_asymroute
        if link_cost is not None:
            data_payload["link-cost"] = link_cost
        if kms is not None:
            data_payload["kms"] = kms
        if exchange_fgt_device_id is not None:
            data_payload["exchange-fgt-device-id"] = exchange_fgt_device_id
        if ipv6_auto_linklocal is not None:
            data_payload["ipv6-auto-linklocal"] = ipv6_auto_linklocal
        if ems_sn_check is not None:
            data_payload["ems-sn-check"] = ems_sn_check
        if cert_trust_store is not None:
            data_payload["cert-trust-store"] = cert_trust_store
        if qkd is not None:
            data_payload["qkd"] = qkd
        if qkd_hybrid is not None:
            data_payload["qkd-hybrid"] = qkd_hybrid
        if qkd_profile is not None:
            data_payload["qkd-profile"] = qkd_profile
        if transport is not None:
            data_payload["transport"] = transport
        if fortinet_esp is not None:
            data_payload["fortinet-esp"] = fortinet_esp
        if auto_transport_threshold is not None:
            data_payload["auto-transport-threshold"] = auto_transport_threshold
        if remote_gw_match is not None:
            data_payload["remote-gw-match"] = remote_gw_match
        if remote_gw_subnet is not None:
            data_payload["remote-gw-subnet"] = remote_gw_subnet
        if remote_gw_start_ip is not None:
            data_payload["remote-gw-start-ip"] = remote_gw_start_ip
        if remote_gw_end_ip is not None:
            data_payload["remote-gw-end-ip"] = remote_gw_end_ip
        if remote_gw_country is not None:
            data_payload["remote-gw-country"] = remote_gw_country
        if remote_gw_ztna_tags is not None:
            data_payload["remote-gw-ztna-tags"] = remote_gw_ztna_tags
        if remote_gw6_match is not None:
            data_payload["remote-gw6-match"] = remote_gw6_match
        if remote_gw6_subnet is not None:
            data_payload["remote-gw6-subnet"] = remote_gw6_subnet
        if remote_gw6_start_ip is not None:
            data_payload["remote-gw6-start-ip"] = remote_gw6_start_ip
        if remote_gw6_end_ip is not None:
            data_payload["remote-gw6-end-ip"] = remote_gw6_end_ip
        if remote_gw6_country is not None:
            data_payload["remote-gw6-country"] = remote_gw6_country
        if cert_peer_username_validation is not None:
            data_payload["cert-peer-username-validation"] = (
                cert_peer_username_validation
            )
        if cert_peer_username_strip is not None:
            data_payload["cert-peer-username-strip"] = cert_peer_username_strip
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
        endpoint = f"/vpn.ipsec/phase1/{name}"
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
        type: str | None = None,
        interface: str | None = None,
        ike_version: str | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: list | None = None,
        authmethod: str | None = None,
        authmethod_remote: str | None = None,
        mode: str | None = None,
        peertype: str | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        mode_cfg: str | None = None,
        mode_cfg_allow_client_selector: str | None = None,
        assign_ip: str | None = None,
        assign_ip_from: str | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: str | None = None,
        ipv4_dns_server1: str | None = None,
        ipv4_dns_server2: str | None = None,
        ipv4_dns_server3: str | None = None,
        internal_domain_list: list | None = None,
        dns_suffix_search: list | None = None,
        ipv4_wins_server1: str | None = None,
        ipv4_wins_server2: str | None = None,
        ipv4_exclude_range: list | None = None,
        ipv4_split_include: str | None = None,
        split_include_service: str | None = None,
        ipv4_name: str | None = None,
        ipv6_start_ip: str | None = None,
        ipv6_end_ip: str | None = None,
        ipv6_prefix: int | None = None,
        ipv6_dns_server1: str | None = None,
        ipv6_dns_server2: str | None = None,
        ipv6_dns_server3: str | None = None,
        ipv6_exclude_range: list | None = None,
        ipv6_split_include: str | None = None,
        ipv6_name: str | None = None,
        ip_delay_interval: int | None = None,
        unity_support: str | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: str | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: str | None = None,
        client_auto_negotiate: str | None = None,
        client_keep_alive: str | None = None,
        backup_gateway: list | None = None,
        proposal: str | None = None,
        add_route: str | None = None,
        add_gw_route: str | None = None,
        psksecret: str | None = None,
        psksecret_remote: str | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: str | None = None,
        auto_negotiate: str | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: str | None = None,
        dpd: str | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: str | None = None,
        send_cert_chain: str | None = None,
        dhgrp: str | None = None,
        addke1: str | None = None,
        addke2: str | None = None,
        addke3: str | None = None,
        addke4: str | None = None,
        addke5: str | None = None,
        addke6: str | None = None,
        addke7: str | None = None,
        suite_b: str | None = None,
        eap: str | None = None,
        eap_identity: str | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: str | None = None,
        acct_verify: str | None = None,
        ppk: str | None = None,
        ppk_secret: str | None = None,
        ppk_identity: str | None = None,
        wizard_type: str | None = None,
        xauthtype: str | None = None,
        reauth: str | None = None,
        authusr: str | None = None,
        authpasswd: str | None = None,
        group_authentication: str | None = None,
        group_authentication_secret: str | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: str | None = None,
        idle_timeout: str | None = None,
        shared_idle_timeout: str | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: str | None = None,
        fgsp_sync: str | None = None,
        inbound_dscp_copy: str | None = None,
        nattraversal: str | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: str | None = None,
        azure_ad_autoconnect: str | None = None,
        client_resume: str | None = None,
        client_resume_interval: int | None = None,
        rekey: str | None = None,
        digital_signature_auth: str | None = None,
        signature_hash_alg: str | None = None,
        rsa_signature_format: str | None = None,
        rsa_signature_hash_override: str | None = None,
        enforce_unique_id: str | None = None,
        cert_id_validation: str | None = None,
        fec_egress: str | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: str | None = None,
        fec_redundant: int | None = None,
        fec_ingress: str | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: str | None = None,
        network_id: int | None = None,
        dev_id_notification: str | None = None,
        dev_id: str | None = None,
        loopback_asymroute: str | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: str | None = None,
        ipv6_auto_linklocal: str | None = None,
        ems_sn_check: str | None = None,
        cert_trust_store: str | None = None,
        qkd: str | None = None,
        qkd_hybrid: str | None = None,
        qkd_profile: str | None = None,
        transport: str | None = None,
        fortinet_esp: str | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: str | None = None,
        remote_gw_subnet: str | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: list | None = None,
        remote_gw6_match: str | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: str | None = None,
        cert_peer_username_strip: str | None = None,
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
            name: IPsec remote gateway name. (optional)
            type: Remote gateway type. (optional)
            interface: Local physical, aggregate, or VLAN outgoing interface.
            (optional)
            ike_version: IKE protocol version. (optional)
            remote_gw: Remote VPN gateway. (optional)
            local_gw: Local VPN gateway. (optional)
            remotegw_ddns: Domain name of remote gateway. For example,
            name.ddns.com. (optional)
            keylife: Time to wait in seconds before phase 1 encryption key
            expires. (optional)
            certificate: Names of up to 4 signed personal certificates.
            (optional)
            authmethod: Authentication method. (optional)
            authmethod_remote: Authentication method (remote side). (optional)
            mode: ID protection mode used to establish a secure channel.
            (optional)
            peertype: Accept this peer type. (optional)
            peerid: Accept this peer identity. (optional)
            usrgrp: User group name for dialup peers. (optional)
            peer: Accept this peer certificate. (optional)
            peergrp: Accept this peer certificate group. (optional)
            mode_cfg: Enable/disable configuration method. (optional)
            mode_cfg_allow_client_selector: Enable/disable mode-cfg client to
            use custom phase2 selectors. (optional)
            assign_ip: Enable/disable assignment of IP to IPsec interface via
            configuration method. (optional)
            assign_ip_from: Method by which the IP address will be assigned.
            (optional)
            ipv4_start_ip: Start of IPv4 range. (optional)
            ipv4_end_ip: End of IPv4 range. (optional)
            ipv4_netmask: IPv4 Netmask. (optional)
            dhcp_ra_giaddr: Relay agent gateway IP address to use in the giaddr
            field of DHCP requests. (optional)
            dhcp6_ra_linkaddr: Relay agent IPv6 link address to use in DHCP6
            requests. (optional)
            dns_mode: DNS server mode. (optional)
            ipv4_dns_server1: IPv4 DNS server 1. (optional)
            ipv4_dns_server2: IPv4 DNS server 2. (optional)
            ipv4_dns_server3: IPv4 DNS server 3. (optional)
            internal_domain_list: One or more internal domain names in quotes
            separated by spaces. (optional)
            dns_suffix_search: One or more DNS domain name suffixes in quotes
            separated by spaces. (optional)
            ipv4_wins_server1: WINS server 1. (optional)
            ipv4_wins_server2: WINS server 2. (optional)
            ipv4_exclude_range: Configuration Method IPv4 exclude ranges.
            (optional)
            ipv4_split_include: IPv4 split-include subnets. (optional)
            split_include_service: Split-include services. (optional)
            ipv4_name: IPv4 address name. (optional)
            ipv6_start_ip: Start of IPv6 range. (optional)
            ipv6_end_ip: End of IPv6 range. (optional)
            ipv6_prefix: IPv6 prefix. (optional)
            ipv6_dns_server1: IPv6 DNS server 1. (optional)
            ipv6_dns_server2: IPv6 DNS server 2. (optional)
            ipv6_dns_server3: IPv6 DNS server 3. (optional)
            ipv6_exclude_range: Configuration method IPv6 exclude ranges.
            (optional)
            ipv6_split_include: IPv6 split-include subnets. (optional)
            ipv6_name: IPv6 address name. (optional)
            ip_delay_interval: IP address reuse delay interval in seconds (0 -
            28800). (optional)
            unity_support: Enable/disable support for Cisco UNITY Configuration
            Method extensions. (optional)
            domain: Instruct unity clients about the single default DNS domain.
            (optional)
            banner: Message that unity client should display after connecting.
            (optional)
            include_local_lan: Enable/disable allow local LAN access on unity
            clients. (optional)
            ipv4_split_exclude: IPv4 subnets that should not be sent over the
            IPsec tunnel. (optional)
            ipv6_split_exclude: IPv6 subnets that should not be sent over the
            IPsec tunnel. (optional)
            save_password: Enable/disable saving XAuth username and password on
            VPN clients. (optional)
            client_auto_negotiate: Enable/disable allowing the VPN client to
            bring up the tunnel when there is no traffic. (optional)
            client_keep_alive: Enable/disable allowing the VPN client to keep
            the tunnel up when there is no traffic. (optional)
            backup_gateway: Instruct unity clients about the backup gateway
            address(es). (optional)
            proposal: Phase1 proposal. (optional)
            add_route: Enable/disable control addition of a route to peer
            destination selector. (optional)
            add_gw_route: Enable/disable automatically add a route to the
            remote gateway. (optional)
            psksecret: Pre-shared secret for PSK authentication (ASCII string
            or hexadecimal encoded with a leading 0x). (optional)
            psksecret_remote: Pre-shared secret for remote side PSK
            authentication (ASCII string or hexadecimal encoded with a leading
            0x). (optional)
            keepalive: NAT-T keep alive interval. (optional)
            distance: Distance for routes added by IKE (1 - 255). (optional)
            priority: Priority for routes added by IKE (1 - 65535). (optional)
            localid: Local ID. (optional)
            localid_type: Local ID type. (optional)
            auto_negotiate: Enable/disable automatic initiation of IKE SA
            negotiation. (optional)
            negotiate_timeout: IKE SA negotiation timeout in seconds (1 - 300).
            (optional)
            fragmentation: Enable/disable fragment IKE message on
            re-transmission. (optional)
            dpd: Dead Peer Detection mode. (optional)
            dpd_retrycount: Number of DPD retry attempts. (optional)
            dpd_retryinterval: DPD retry interval. (optional)
            comments: Comment. (optional)
            npu_offload: Enable/disable offloading NPU. (optional)
            send_cert_chain: Enable/disable sending certificate chain.
            (optional)
            dhgrp: DH group. (optional)
            addke1: ADDKE1 group. (optional)
            addke2: ADDKE2 group. (optional)
            addke3: ADDKE3 group. (optional)
            addke4: ADDKE4 group. (optional)
            addke5: ADDKE5 group. (optional)
            addke6: ADDKE6 group. (optional)
            addke7: ADDKE7 group. (optional)
            suite_b: Use Suite-B. (optional)
            eap: Enable/disable IKEv2 EAP authentication. (optional)
            eap_identity: IKEv2 EAP peer identity type. (optional)
            eap_exclude_peergrp: Peer group excluded from EAP authentication.
            (optional)
            eap_cert_auth: Enable/disable peer certificate authentication in
            addition to EAP if peer is a FortiClient endpoint. (optional)
            acct_verify: Enable/disable verification of RADIUS accounting
            record. (optional)
            ppk: Enable/disable IKEv2 Postquantum Preshared Key (PPK).
            (optional)
            ppk_secret: IKEv2 Postquantum Preshared Key (ASCII string or
            hexadecimal encoded with a leading 0x). (optional)
            ppk_identity: IKEv2 Postquantum Preshared Key Identity. (optional)
            wizard_type: GUI VPN Wizard Type. (optional)
            xauthtype: XAuth type. (optional)
            reauth: Enable/disable re-authentication upon IKE SA lifetime
            expiration. (optional)
            authusr: XAuth user name. (optional)
            authpasswd: XAuth password (max 35 characters). (optional)
            group_authentication: Enable/disable IKEv2 IDi group
            authentication. (optional)
            group_authentication_secret: Password for IKEv2 ID group
            authentication. ASCII string or hexadecimal indicated by a leading
            0x. (optional)
            authusrgrp: Authentication user group. (optional)
            mesh_selector_type: Add selectors containing subsets of the
            configuration depending on traffic. (optional)
            idle_timeout: Enable/disable IPsec tunnel idle timeout. (optional)
            shared_idle_timeout: Enable/disable IPsec tunnel shared idle
            timeout. (optional)
            idle_timeoutinterval: IPsec tunnel idle timeout in minutes (5 -
            43200). (optional)
            ha_sync_esp_seqno: Enable/disable sequence number jump ahead for
            IPsec HA. (optional)
            fgsp_sync: Enable/disable IPsec syncing of tunnels for FGSP IPsec.
            (optional)
            inbound_dscp_copy: Enable/disable copy the dscp in the ESP header
            to the inner IP Header. (optional)
            nattraversal: Enable/disable NAT traversal. (optional)
            fragmentation_mtu: IKE fragmentation MTU (500 - 16000). (optional)
            childless_ike: Enable/disable childless IKEv2 initiation (RFC
            6023). (optional)
            azure_ad_autoconnect: Enable/disable Azure AD Auto-Connect for
            FortiClient. (optional)
            client_resume: Enable/disable resumption of offline FortiClient
            sessions. When a FortiClient enabled laptop is closed or enters
            sleep/hibernate mode, enabling this feature allows FortiClient to
            keep the tunnel during this period, and allows users to immediately
            resume using the IPsec tunnel when the device wakes up. (optional)
            client_resume_interval: Maximum time in seconds during which a VPN
            client may resume using a tunnel after a client PC has entered
            sleep mode or temporarily lost its network connection (120 -
            172800, default = 7200). (optional)
            rekey: Enable/disable phase1 rekey. (optional)
            digital_signature_auth: Enable/disable IKEv2 Digital Signature
            Authentication (RFC 7427). (optional)
            signature_hash_alg: Digital Signature Authentication hash
            algorithms. (optional)
            rsa_signature_format: Digital Signature Authentication RSA
            signature format. (optional)
            rsa_signature_hash_override: Enable/disable IKEv2 RSA signature
            hash algorithm override. (optional)
            enforce_unique_id: Enable/disable peer ID uniqueness check.
            (optional)
            cert_id_validation: Enable/disable cross validation of peer ID and
            the identity in the peer's certificate as specified in RFC 4945.
            (optional)
            fec_egress: Enable/disable Forward Error Correction for egress
            IPsec traffic. (optional)
            fec_send_timeout: Timeout in milliseconds before sending Forward
            Error Correction packets (1 - 1000). (optional)
            fec_base: Number of base Forward Error Correction packets (1 - 20).
            (optional)
            fec_codec: Forward Error Correction encoding/decoding algorithm.
            (optional)
            fec_redundant: Number of redundant Forward Error Correction packets
            (1 - 5 for reed-solomon, 1 for xor). (optional)
            fec_ingress: Enable/disable Forward Error Correction for ingress
            IPsec traffic. (optional)
            fec_receive_timeout: Timeout in milliseconds before dropping
            Forward Error Correction packets (1 - 1000). (optional)
            fec_health_check: SD-WAN health check. (optional)
            fec_mapping_profile: Forward Error Correction (FEC) mapping
            profile. (optional)
            network_overlay: Enable/disable network overlays. (optional)
            network_id: VPN gateway network ID. (optional)
            dev_id_notification: Enable/disable device ID notification.
            (optional)
            dev_id: Device ID carried by the device ID notification. (optional)
            loopback_asymroute: Enable/disable asymmetric routing for IKE
            traffic on loopback interface. (optional)
            link_cost: VPN tunnel underlay link cost. (optional)
            kms: Key Management Services server. (optional)
            exchange_fgt_device_id: Enable/disable device identifier exchange
            with peer FortiGate units for use of VPN monitor data by
            FortiManager. (optional)
            ipv6_auto_linklocal: Enable/disable auto generation of IPv6
            link-local address using last 8 bytes of mode-cfg assigned IPv6
            address. (optional)
            ems_sn_check: Enable/disable verification of EMS serial number.
            (optional)
            cert_trust_store: CA certificate trust store. (optional)
            qkd: Enable/disable use of Quantum Key Distribution (QKD) server.
            (optional)
            qkd_hybrid: Enable/disable use of Quantum Key Distribution (QKD)
            hybrid keys. (optional)
            qkd_profile: Quantum Key Distribution (QKD) server profile.
            (optional)
            transport: Set IKE transport protocol. (optional)
            fortinet_esp: Enable/disable Fortinet ESP encapsulation. (optional)
            auto_transport_threshold: Timeout in seconds before falling back to
            next transport protocol. (optional)
            remote_gw_match: Set type of IPv4 remote gateway address matching.
            (optional)
            remote_gw_subnet: IPv4 address and subnet mask. (optional)
            remote_gw_start_ip: First IPv4 address in the range. (optional)
            remote_gw_end_ip: Last IPv4 address in the range. (optional)
            remote_gw_country: IPv4 addresses associated to a specific country.
            (optional)
            remote_gw_ztna_tags: IPv4 ZTNA posture tags. (optional)
            remote_gw6_match: Set type of IPv6 remote gateway address matching.
            (optional)
            remote_gw6_subnet: IPv6 address and prefix. (optional)
            remote_gw6_start_ip: First IPv6 address in the range. (optional)
            remote_gw6_end_ip: Last IPv6 address in the range. (optional)
            remote_gw6_country: IPv6 addresses associated to a specific
            country. (optional)
            cert_peer_username_validation: Enable/disable cross validation of
            peer username and the identity in the peer's certificate.
            (optional)
            cert_peer_username_strip: Enable/disable domain stripping on
            certificate identity. (optional)
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
        endpoint = "/vpn.ipsec/phase1"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if type is not None:
            data_payload["type"] = type
        if interface is not None:
            data_payload["interface"] = interface
        if ike_version is not None:
            data_payload["ike-version"] = ike_version
        if remote_gw is not None:
            data_payload["remote-gw"] = remote_gw
        if local_gw is not None:
            data_payload["local-gw"] = local_gw
        if remotegw_ddns is not None:
            data_payload["remotegw-ddns"] = remotegw_ddns
        if keylife is not None:
            data_payload["keylife"] = keylife
        if certificate is not None:
            data_payload["certificate"] = certificate
        if authmethod is not None:
            data_payload["authmethod"] = authmethod
        if authmethod_remote is not None:
            data_payload["authmethod-remote"] = authmethod_remote
        if mode is not None:
            data_payload["mode"] = mode
        if peertype is not None:
            data_payload["peertype"] = peertype
        if peerid is not None:
            data_payload["peerid"] = peerid
        if usrgrp is not None:
            data_payload["usrgrp"] = usrgrp
        if peer is not None:
            data_payload["peer"] = peer
        if peergrp is not None:
            data_payload["peergrp"] = peergrp
        if mode_cfg is not None:
            data_payload["mode-cfg"] = mode_cfg
        if mode_cfg_allow_client_selector is not None:
            data_payload["mode-cfg-allow-client-selector"] = (
                mode_cfg_allow_client_selector
            )
        if assign_ip is not None:
            data_payload["assign-ip"] = assign_ip
        if assign_ip_from is not None:
            data_payload["assign-ip-from"] = assign_ip_from
        if ipv4_start_ip is not None:
            data_payload["ipv4-start-ip"] = ipv4_start_ip
        if ipv4_end_ip is not None:
            data_payload["ipv4-end-ip"] = ipv4_end_ip
        if ipv4_netmask is not None:
            data_payload["ipv4-netmask"] = ipv4_netmask
        if dhcp_ra_giaddr is not None:
            data_payload["dhcp-ra-giaddr"] = dhcp_ra_giaddr
        if dhcp6_ra_linkaddr is not None:
            data_payload["dhcp6-ra-linkaddr"] = dhcp6_ra_linkaddr
        if dns_mode is not None:
            data_payload["dns-mode"] = dns_mode
        if ipv4_dns_server1 is not None:
            data_payload["ipv4-dns-server1"] = ipv4_dns_server1
        if ipv4_dns_server2 is not None:
            data_payload["ipv4-dns-server2"] = ipv4_dns_server2
        if ipv4_dns_server3 is not None:
            data_payload["ipv4-dns-server3"] = ipv4_dns_server3
        if internal_domain_list is not None:
            data_payload["internal-domain-list"] = internal_domain_list
        if dns_suffix_search is not None:
            data_payload["dns-suffix-search"] = dns_suffix_search
        if ipv4_wins_server1 is not None:
            data_payload["ipv4-wins-server1"] = ipv4_wins_server1
        if ipv4_wins_server2 is not None:
            data_payload["ipv4-wins-server2"] = ipv4_wins_server2
        if ipv4_exclude_range is not None:
            data_payload["ipv4-exclude-range"] = ipv4_exclude_range
        if ipv4_split_include is not None:
            data_payload["ipv4-split-include"] = ipv4_split_include
        if split_include_service is not None:
            data_payload["split-include-service"] = split_include_service
        if ipv4_name is not None:
            data_payload["ipv4-name"] = ipv4_name
        if ipv6_start_ip is not None:
            data_payload["ipv6-start-ip"] = ipv6_start_ip
        if ipv6_end_ip is not None:
            data_payload["ipv6-end-ip"] = ipv6_end_ip
        if ipv6_prefix is not None:
            data_payload["ipv6-prefix"] = ipv6_prefix
        if ipv6_dns_server1 is not None:
            data_payload["ipv6-dns-server1"] = ipv6_dns_server1
        if ipv6_dns_server2 is not None:
            data_payload["ipv6-dns-server2"] = ipv6_dns_server2
        if ipv6_dns_server3 is not None:
            data_payload["ipv6-dns-server3"] = ipv6_dns_server3
        if ipv6_exclude_range is not None:
            data_payload["ipv6-exclude-range"] = ipv6_exclude_range
        if ipv6_split_include is not None:
            data_payload["ipv6-split-include"] = ipv6_split_include
        if ipv6_name is not None:
            data_payload["ipv6-name"] = ipv6_name
        if ip_delay_interval is not None:
            data_payload["ip-delay-interval"] = ip_delay_interval
        if unity_support is not None:
            data_payload["unity-support"] = unity_support
        if domain is not None:
            data_payload["domain"] = domain
        if banner is not None:
            data_payload["banner"] = banner
        if include_local_lan is not None:
            data_payload["include-local-lan"] = include_local_lan
        if ipv4_split_exclude is not None:
            data_payload["ipv4-split-exclude"] = ipv4_split_exclude
        if ipv6_split_exclude is not None:
            data_payload["ipv6-split-exclude"] = ipv6_split_exclude
        if save_password is not None:
            data_payload["save-password"] = save_password
        if client_auto_negotiate is not None:
            data_payload["client-auto-negotiate"] = client_auto_negotiate
        if client_keep_alive is not None:
            data_payload["client-keep-alive"] = client_keep_alive
        if backup_gateway is not None:
            data_payload["backup-gateway"] = backup_gateway
        if proposal is not None:
            data_payload["proposal"] = proposal
        if add_route is not None:
            data_payload["add-route"] = add_route
        if add_gw_route is not None:
            data_payload["add-gw-route"] = add_gw_route
        if psksecret is not None:
            data_payload["psksecret"] = psksecret
        if psksecret_remote is not None:
            data_payload["psksecret-remote"] = psksecret_remote
        if keepalive is not None:
            data_payload["keepalive"] = keepalive
        if distance is not None:
            data_payload["distance"] = distance
        if priority is not None:
            data_payload["priority"] = priority
        if localid is not None:
            data_payload["localid"] = localid
        if localid_type is not None:
            data_payload["localid-type"] = localid_type
        if auto_negotiate is not None:
            data_payload["auto-negotiate"] = auto_negotiate
        if negotiate_timeout is not None:
            data_payload["negotiate-timeout"] = negotiate_timeout
        if fragmentation is not None:
            data_payload["fragmentation"] = fragmentation
        if dpd is not None:
            data_payload["dpd"] = dpd
        if dpd_retrycount is not None:
            data_payload["dpd-retrycount"] = dpd_retrycount
        if dpd_retryinterval is not None:
            data_payload["dpd-retryinterval"] = dpd_retryinterval
        if comments is not None:
            data_payload["comments"] = comments
        if npu_offload is not None:
            data_payload["npu-offload"] = npu_offload
        if send_cert_chain is not None:
            data_payload["send-cert-chain"] = send_cert_chain
        if dhgrp is not None:
            data_payload["dhgrp"] = dhgrp
        if addke1 is not None:
            data_payload["addke1"] = addke1
        if addke2 is not None:
            data_payload["addke2"] = addke2
        if addke3 is not None:
            data_payload["addke3"] = addke3
        if addke4 is not None:
            data_payload["addke4"] = addke4
        if addke5 is not None:
            data_payload["addke5"] = addke5
        if addke6 is not None:
            data_payload["addke6"] = addke6
        if addke7 is not None:
            data_payload["addke7"] = addke7
        if suite_b is not None:
            data_payload["suite-b"] = suite_b
        if eap is not None:
            data_payload["eap"] = eap
        if eap_identity is not None:
            data_payload["eap-identity"] = eap_identity
        if eap_exclude_peergrp is not None:
            data_payload["eap-exclude-peergrp"] = eap_exclude_peergrp
        if eap_cert_auth is not None:
            data_payload["eap-cert-auth"] = eap_cert_auth
        if acct_verify is not None:
            data_payload["acct-verify"] = acct_verify
        if ppk is not None:
            data_payload["ppk"] = ppk
        if ppk_secret is not None:
            data_payload["ppk-secret"] = ppk_secret
        if ppk_identity is not None:
            data_payload["ppk-identity"] = ppk_identity
        if wizard_type is not None:
            data_payload["wizard-type"] = wizard_type
        if xauthtype is not None:
            data_payload["xauthtype"] = xauthtype
        if reauth is not None:
            data_payload["reauth"] = reauth
        if authusr is not None:
            data_payload["authusr"] = authusr
        if authpasswd is not None:
            data_payload["authpasswd"] = authpasswd
        if group_authentication is not None:
            data_payload["group-authentication"] = group_authentication
        if group_authentication_secret is not None:
            data_payload["group-authentication-secret"] = (
                group_authentication_secret
            )
        if authusrgrp is not None:
            data_payload["authusrgrp"] = authusrgrp
        if mesh_selector_type is not None:
            data_payload["mesh-selector-type"] = mesh_selector_type
        if idle_timeout is not None:
            data_payload["idle-timeout"] = idle_timeout
        if shared_idle_timeout is not None:
            data_payload["shared-idle-timeout"] = shared_idle_timeout
        if idle_timeoutinterval is not None:
            data_payload["idle-timeoutinterval"] = idle_timeoutinterval
        if ha_sync_esp_seqno is not None:
            data_payload["ha-sync-esp-seqno"] = ha_sync_esp_seqno
        if fgsp_sync is not None:
            data_payload["fgsp-sync"] = fgsp_sync
        if inbound_dscp_copy is not None:
            data_payload["inbound-dscp-copy"] = inbound_dscp_copy
        if nattraversal is not None:
            data_payload["nattraversal"] = nattraversal
        if fragmentation_mtu is not None:
            data_payload["fragmentation-mtu"] = fragmentation_mtu
        if childless_ike is not None:
            data_payload["childless-ike"] = childless_ike
        if azure_ad_autoconnect is not None:
            data_payload["azure-ad-autoconnect"] = azure_ad_autoconnect
        if client_resume is not None:
            data_payload["client-resume"] = client_resume
        if client_resume_interval is not None:
            data_payload["client-resume-interval"] = client_resume_interval
        if rekey is not None:
            data_payload["rekey"] = rekey
        if digital_signature_auth is not None:
            data_payload["digital-signature-auth"] = digital_signature_auth
        if signature_hash_alg is not None:
            data_payload["signature-hash-alg"] = signature_hash_alg
        if rsa_signature_format is not None:
            data_payload["rsa-signature-format"] = rsa_signature_format
        if rsa_signature_hash_override is not None:
            data_payload["rsa-signature-hash-override"] = (
                rsa_signature_hash_override
            )
        if enforce_unique_id is not None:
            data_payload["enforce-unique-id"] = enforce_unique_id
        if cert_id_validation is not None:
            data_payload["cert-id-validation"] = cert_id_validation
        if fec_egress is not None:
            data_payload["fec-egress"] = fec_egress
        if fec_send_timeout is not None:
            data_payload["fec-send-timeout"] = fec_send_timeout
        if fec_base is not None:
            data_payload["fec-base"] = fec_base
        if fec_codec is not None:
            data_payload["fec-codec"] = fec_codec
        if fec_redundant is not None:
            data_payload["fec-redundant"] = fec_redundant
        if fec_ingress is not None:
            data_payload["fec-ingress"] = fec_ingress
        if fec_receive_timeout is not None:
            data_payload["fec-receive-timeout"] = fec_receive_timeout
        if fec_health_check is not None:
            data_payload["fec-health-check"] = fec_health_check
        if fec_mapping_profile is not None:
            data_payload["fec-mapping-profile"] = fec_mapping_profile
        if network_overlay is not None:
            data_payload["network-overlay"] = network_overlay
        if network_id is not None:
            data_payload["network-id"] = network_id
        if dev_id_notification is not None:
            data_payload["dev-id-notification"] = dev_id_notification
        if dev_id is not None:
            data_payload["dev-id"] = dev_id
        if loopback_asymroute is not None:
            data_payload["loopback-asymroute"] = loopback_asymroute
        if link_cost is not None:
            data_payload["link-cost"] = link_cost
        if kms is not None:
            data_payload["kms"] = kms
        if exchange_fgt_device_id is not None:
            data_payload["exchange-fgt-device-id"] = exchange_fgt_device_id
        if ipv6_auto_linklocal is not None:
            data_payload["ipv6-auto-linklocal"] = ipv6_auto_linklocal
        if ems_sn_check is not None:
            data_payload["ems-sn-check"] = ems_sn_check
        if cert_trust_store is not None:
            data_payload["cert-trust-store"] = cert_trust_store
        if qkd is not None:
            data_payload["qkd"] = qkd
        if qkd_hybrid is not None:
            data_payload["qkd-hybrid"] = qkd_hybrid
        if qkd_profile is not None:
            data_payload["qkd-profile"] = qkd_profile
        if transport is not None:
            data_payload["transport"] = transport
        if fortinet_esp is not None:
            data_payload["fortinet-esp"] = fortinet_esp
        if auto_transport_threshold is not None:
            data_payload["auto-transport-threshold"] = auto_transport_threshold
        if remote_gw_match is not None:
            data_payload["remote-gw-match"] = remote_gw_match
        if remote_gw_subnet is not None:
            data_payload["remote-gw-subnet"] = remote_gw_subnet
        if remote_gw_start_ip is not None:
            data_payload["remote-gw-start-ip"] = remote_gw_start_ip
        if remote_gw_end_ip is not None:
            data_payload["remote-gw-end-ip"] = remote_gw_end_ip
        if remote_gw_country is not None:
            data_payload["remote-gw-country"] = remote_gw_country
        if remote_gw_ztna_tags is not None:
            data_payload["remote-gw-ztna-tags"] = remote_gw_ztna_tags
        if remote_gw6_match is not None:
            data_payload["remote-gw6-match"] = remote_gw6_match
        if remote_gw6_subnet is not None:
            data_payload["remote-gw6-subnet"] = remote_gw6_subnet
        if remote_gw6_start_ip is not None:
            data_payload["remote-gw6-start-ip"] = remote_gw6_start_ip
        if remote_gw6_end_ip is not None:
            data_payload["remote-gw6-end-ip"] = remote_gw6_end_ip
        if remote_gw6_country is not None:
            data_payload["remote-gw6-country"] = remote_gw6_country
        if cert_peer_username_validation is not None:
            data_payload["cert-peer-username-validation"] = (
                cert_peer_username_validation
            )
        if cert_peer_username_strip is not None:
            data_payload["cert-peer-username-strip"] = cert_peer_username_strip
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
