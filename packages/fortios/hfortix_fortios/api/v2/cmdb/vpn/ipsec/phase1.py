"""
FortiOS CMDB - Vpn ipsec phase1

Configuration endpoint for managing cmdb vpn/ipsec/phase1 objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec/phase1
    POST   /cmdb/vpn/ipsec/phase1
    PUT    /cmdb/vpn/ipsec/phase1/{identifier}
    DELETE /cmdb/vpn/ipsec/phase1/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_ipsec_phase1.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.vpn_ipsec_phase1.post(
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

class Phase1(CRUDEndpoint, MetadataMixin):
    """Phase1 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "phase1"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "certificate": {
            "mkey": "name",
            "required_fields": ['name'],
            "example": "[{'name': 'value'}]",
        },
        "internal_domain_list": {
            "mkey": "domain-name",
            "required_fields": ['domain-name'],
            "example": "[{'domain-name': 'value'}]",
        },
        "dns_suffix_search": {
            "mkey": "dns-suffix",
            "required_fields": ['dns-suffix'],
            "example": "[{'dns-suffix': 'value'}]",
        },
        "ipv4_exclude_range": {
            "mkey": "id",
            "required_fields": ['id', 'start-ip', 'end-ip'],
            "example": "[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
        },
        "ipv6_exclude_range": {
            "mkey": "id",
            "required_fields": ['id', 'start-ip', 'end-ip'],
            "example": "[{'id': 1, 'start-ip': 'value', 'end-ip': 'value'}]",
        },
        "backup_gateway": {
            "mkey": "address",
            "required_fields": ['address'],
            "example": "[{'address': 'value'}]",
        },
        "remote_gw_ztna_tags": {
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
        """Initialize Phase1 endpoint."""
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
        Retrieve vpn/ipsec/phase1 configuration.

        Configure VPN remote gateway.

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
            >>> # Get all vpn/ipsec/phase1 objects
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific vpn/ipsec/phase1 by name
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase1.get_schema()

        See Also:
            - post(): Create new vpn/ipsec/phase1 object
            - put(): Update existing vpn/ipsec/phase1 object
            - delete(): Remove vpn/ipsec/phase1 object
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
            endpoint = "/vpn.ipsec/phase1/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/vpn.ipsec/phase1"
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
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase1.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.vpn_ipsec_phase1.get_schema(format="json-schema")
        
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
        type: Literal["static", "dynamic", "ddns"] | None = None,
        interface: str | None = None,
        ike_version: Literal["1", "2"] | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list[str] | list[dict[str, Any]] | None = None,
        authmethod: Literal["psk", "signature"] | None = None,
        authmethod_remote: Literal["psk", "signature"] | None = None,
        mode: Literal["aggressive", "main"] | None = None,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        mode_cfg: Literal["disable", "enable"] | None = None,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = None,
        assign_ip: Literal["disable", "enable"] | None = None,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: Literal["manual", "auto"] | None = None,
        ipv4_dns_server1: str | None = None,
        ipv4_dns_server2: str | None = None,
        ipv4_dns_server3: str | None = None,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = None,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = None,
        ipv4_wins_server1: str | None = None,
        ipv4_wins_server2: str | None = None,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        ipv4_split_include: str | None = None,
        split_include_service: str | None = None,
        ipv4_name: str | None = None,
        ipv6_start_ip: str | None = None,
        ipv6_end_ip: str | None = None,
        ipv6_prefix: int | None = None,
        ipv6_dns_server1: str | None = None,
        ipv6_dns_server2: str | None = None,
        ipv6_dns_server3: str | None = None,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        ipv6_split_include: str | None = None,
        ipv6_name: str | None = None,
        ip_delay_interval: int | None = None,
        unity_support: Literal["disable", "enable"] | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: Literal["disable", "enable"] | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: Literal["disable", "enable"] | None = None,
        client_auto_negotiate: Literal["disable", "enable"] | None = None,
        client_keep_alive: Literal["disable", "enable"] | None = None,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = None,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = None,
        add_route: Literal["disable", "enable"] | None = None,
        add_gw_route: Literal["enable", "disable"] | None = None,
        psksecret: Any | None = None,
        psksecret_remote: Any | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = None,
        auto_negotiate: Literal["enable", "disable"] | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: Literal["enable", "disable"] | None = None,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: Literal["enable", "disable"] | None = None,
        send_cert_chain: Literal["enable", "disable"] | None = None,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = None,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = None,
        eap: Literal["enable", "disable"] | None = None,
        eap_identity: Literal["use-id-payload", "send-request"] | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: Literal["enable", "disable"] | None = None,
        acct_verify: Literal["enable", "disable"] | None = None,
        ppk: Literal["disable", "allow", "require"] | None = None,
        ppk_secret: Any | None = None,
        ppk_identity: str | None = None,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = None,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = None,
        reauth: Literal["disable", "enable"] | None = None,
        authusr: str | None = None,
        authpasswd: Any | None = None,
        group_authentication: Literal["enable", "disable"] | None = None,
        group_authentication_secret: Any | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = None,
        idle_timeout: Literal["enable", "disable"] | None = None,
        shared_idle_timeout: Literal["enable", "disable"] | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = None,
        fgsp_sync: Literal["enable", "disable"] | None = None,
        inbound_dscp_copy: Literal["enable", "disable"] | None = None,
        nattraversal: Literal["enable", "disable", "forced"] | None = None,
        esn: Literal["require", "allow", "disable"] | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: Literal["enable", "disable"] | None = None,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = None,
        client_resume: Literal["enable", "disable"] | None = None,
        client_resume_interval: int | None = None,
        rekey: Literal["enable", "disable"] | None = None,
        digital_signature_auth: Literal["enable", "disable"] | None = None,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = None,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = None,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = None,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = None,
        cert_id_validation: Literal["enable", "disable"] | None = None,
        fec_egress: Literal["enable", "disable"] | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: Literal["rs", "xor"] | None = None,
        fec_redundant: int | None = None,
        fec_ingress: Literal["enable", "disable"] | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: Literal["disable", "enable"] | None = None,
        network_id: int | None = None,
        dev_id_notification: Literal["disable", "enable"] | None = None,
        dev_id: str | None = None,
        loopback_asymroute: Literal["enable", "disable"] | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = None,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = None,
        ems_sn_check: Literal["enable", "disable"] | None = None,
        cert_trust_store: Literal["local", "ems"] | None = None,
        qkd: Literal["disable", "allow", "require"] | None = None,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = None,
        qkd_profile: str | None = None,
        transport: Literal["udp", "auto", "tcp"] | None = None,
        fortinet_esp: Literal["enable", "disable"] | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = None,
        remote_gw_subnet: Any | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = None,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = None,
        cert_peer_username_strip: Literal["disable", "enable"] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing vpn/ipsec/phase1 object.

        Configure VPN remote gateway.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: IPsec remote gateway name.
            type: Remote gateway type.
            interface: Local physical, aggregate, or VLAN outgoing interface.
            ike_version: IKE protocol version.
            remote_gw: Remote VPN gateway.
            local_gw: Local VPN gateway.
            remotegw_ddns: Domain name of remote gateway. For example, name.ddns.com.
            keylife: Time to wait in seconds before phase 1 encryption key expires.
            certificate: Names of up to 4 signed personal certificates.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            authmethod: Authentication method.
            authmethod_remote: Authentication method (remote side).
            mode: ID protection mode used to establish a secure channel.
            peertype: Accept this peer type.
            peerid: Accept this peer identity.
            usrgrp: User group name for dialup peers.
            peer: Accept this peer certificate.
            peergrp: Accept this peer certificate group.
            mode_cfg: Enable/disable configuration method.
            mode_cfg_allow_client_selector: Enable/disable mode-cfg client to use custom phase2 selectors.
            assign_ip: Enable/disable assignment of IP to IPsec interface via configuration method.
            assign_ip_from: Method by which the IP address will be assigned.
            ipv4_start_ip: Start of IPv4 range.
            ipv4_end_ip: End of IPv4 range.
            ipv4_netmask: IPv4 Netmask.
            dhcp_ra_giaddr: Relay agent gateway IP address to use in the giaddr field of DHCP requests.
            dhcp6_ra_linkaddr: Relay agent IPv6 link address to use in DHCP6 requests.
            dns_mode: DNS server mode.
            ipv4_dns_server1: IPv4 DNS server 1.
            ipv4_dns_server2: IPv4 DNS server 2.
            ipv4_dns_server3: IPv4 DNS server 3.
            internal_domain_list: One or more internal domain names in quotes separated by spaces.
                Default format: [{'domain-name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'domain-name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'domain-name': 'val1'}, ...]
                  - List of dicts: [{'domain-name': 'value'}] (recommended)
            dns_suffix_search: One or more DNS domain name suffixes in quotes separated by spaces.
                Default format: [{'dns-suffix': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'dns-suffix': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'dns-suffix': 'val1'}, ...]
                  - List of dicts: [{'dns-suffix': 'value'}] (recommended)
            ipv4_wins_server1: WINS server 1.
            ipv4_wins_server2: WINS server 2.
            ipv4_exclude_range: Configuration Method IPv4 exclude ranges.
                Default format: [{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]
                Required format: List of dicts with keys: id, start-ip, end-ip
                  (String format not allowed due to multiple required fields)
            ipv4_split_include: IPv4 split-include subnets.
            split_include_service: Split-include services.
            ipv4_name: IPv4 address name.
            ipv6_start_ip: Start of IPv6 range.
            ipv6_end_ip: End of IPv6 range.
            ipv6_prefix: IPv6 prefix.
            ipv6_dns_server1: IPv6 DNS server 1.
            ipv6_dns_server2: IPv6 DNS server 2.
            ipv6_dns_server3: IPv6 DNS server 3.
            ipv6_exclude_range: Configuration method IPv6 exclude ranges.
                Default format: [{'id': 1, 'start-ip': 'value', 'end-ip': 'value'}]
                Required format: List of dicts with keys: id, start-ip, end-ip
                  (String format not allowed due to multiple required fields)
            ipv6_split_include: IPv6 split-include subnets.
            ipv6_name: IPv6 address name.
            ip_delay_interval: IP address reuse delay interval in seconds (0 - 28800).
            unity_support: Enable/disable support for Cisco UNITY Configuration Method extensions.
            domain: Instruct unity clients about the single default DNS domain.
            banner: Message that unity client should display after connecting.
            include_local_lan: Enable/disable allow local LAN access on unity clients.
            ipv4_split_exclude: IPv4 subnets that should not be sent over the IPsec tunnel.
            ipv6_split_exclude: IPv6 subnets that should not be sent over the IPsec tunnel.
            save_password: Enable/disable saving XAuth username and password on VPN clients.
            client_auto_negotiate: Enable/disable allowing the VPN client to bring up the tunnel when there is no traffic.
            client_keep_alive: Enable/disable allowing the VPN client to keep the tunnel up when there is no traffic.
            backup_gateway: Instruct unity clients about the backup gateway address(es).
                Default format: [{'address': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'address': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'address': 'val1'}, ...]
                  - List of dicts: [{'address': 'value'}] (recommended)
            proposal: Phase1 proposal.
            add_route: Enable/disable control addition of a route to peer destination selector.
            add_gw_route: Enable/disable automatically add a route to the remote gateway.
            psksecret: Pre-shared secret for PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).
            psksecret_remote: Pre-shared secret for remote side PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).
            keepalive: NAT-T keep alive interval.
            distance: Distance for routes added by IKE (1 - 255).
            priority: Priority for routes added by IKE (1 - 65535).
            localid: Local ID.
            localid_type: Local ID type.
            auto_negotiate: Enable/disable automatic initiation of IKE SA negotiation.
            negotiate_timeout: IKE SA negotiation timeout in seconds (1 - 300).
            fragmentation: Enable/disable fragment IKE message on re-transmission.
            dpd: Dead Peer Detection mode.
            dpd_retrycount: Number of DPD retry attempts.
            dpd_retryinterval: DPD retry interval.
            comments: Comment.
            npu_offload: Enable/disable offloading NPU.
            send_cert_chain: Enable/disable sending certificate chain.
            dhgrp: DH group.
            addke1: ADDKE1 group.
            addke2: ADDKE2 group.
            addke3: ADDKE3 group.
            addke4: ADDKE4 group.
            addke5: ADDKE5 group.
            addke6: ADDKE6 group.
            addke7: ADDKE7 group.
            suite_b: Use Suite-B.
            eap: Enable/disable IKEv2 EAP authentication.
            eap_identity: IKEv2 EAP peer identity type.
            eap_exclude_peergrp: Peer group excluded from EAP authentication.
            eap_cert_auth: Enable/disable peer certificate authentication in addition to EAP if peer is a FortiClient endpoint.
            acct_verify: Enable/disable verification of RADIUS accounting record.
            ppk: Enable/disable IKEv2 Postquantum Preshared Key (PPK).
            ppk_secret: IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).
            ppk_identity: IKEv2 Postquantum Preshared Key Identity.
            wizard_type: GUI VPN Wizard Type.
            xauthtype: XAuth type.
            reauth: Enable/disable re-authentication upon IKE SA lifetime expiration.
            authusr: XAuth user name.
            authpasswd: XAuth password (max 35 characters).
            group_authentication: Enable/disable IKEv2 IDi group authentication.
            group_authentication_secret: Password for IKEv2 ID group authentication. ASCII string or hexadecimal indicated by a leading 0x.
            authusrgrp: Authentication user group.
            mesh_selector_type: Add selectors containing subsets of the configuration depending on traffic.
            idle_timeout: Enable/disable IPsec tunnel idle timeout.
            shared_idle_timeout: Enable/disable IPsec tunnel shared idle timeout.
            idle_timeoutinterval: IPsec tunnel idle timeout in minutes (5 - 43200).
            ha_sync_esp_seqno: Enable/disable sequence number jump ahead for IPsec HA.
            fgsp_sync: Enable/disable IPsec syncing of tunnels for FGSP IPsec.
            inbound_dscp_copy: Enable/disable copy the dscp in the ESP header to the inner IP Header.
            nattraversal: Enable/disable NAT traversal.
            esn: Extended sequence number (ESN) negotiation.
            fragmentation_mtu: IKE fragmentation MTU (500 - 16000).
            childless_ike: Enable/disable childless IKEv2 initiation (RFC 6023).
            azure_ad_autoconnect: Enable/disable Azure AD Auto-Connect for FortiClient.
            client_resume: Enable/disable resumption of offline FortiClient sessions.  When a FortiClient enabled laptop is closed or enters sleep/hibernate mode, enabling this feature allows FortiClient to keep the tunnel during this period, and allows users to immediately resume using the IPsec tunnel when the device wakes up.
            client_resume_interval: Maximum time in seconds during which a VPN client may resume using a tunnel after a client PC has entered sleep mode or temporarily lost its network connection (120 - 172800, default = 7200).
            rekey: Enable/disable phase1 rekey.
            digital_signature_auth: Enable/disable IKEv2 Digital Signature Authentication (RFC 7427).
            signature_hash_alg: Digital Signature Authentication hash algorithms.
            rsa_signature_format: Digital Signature Authentication RSA signature format.
            rsa_signature_hash_override: Enable/disable IKEv2 RSA signature hash algorithm override.
            enforce_unique_id: Enable/disable peer ID uniqueness check.
            cert_id_validation: Enable/disable cross validation of peer ID and the identity in the peer's certificate as specified in RFC 4945.
            fec_egress: Enable/disable Forward Error Correction for egress IPsec traffic.
            fec_send_timeout: Timeout in milliseconds before sending Forward Error Correction packets (1 - 1000).
            fec_base: Number of base Forward Error Correction packets (1 - 20).
            fec_codec: Forward Error Correction encoding/decoding algorithm.
            fec_redundant: Number of redundant Forward Error Correction packets (1 - 5 for reed-solomon, 1 for xor).
            fec_ingress: Enable/disable Forward Error Correction for ingress IPsec traffic.
            fec_receive_timeout: Timeout in milliseconds before dropping Forward Error Correction packets (1 - 1000).
            fec_health_check: SD-WAN health check.
            fec_mapping_profile: Forward Error Correction (FEC) mapping profile.
            network_overlay: Enable/disable network overlays.
            network_id: VPN gateway network ID.
            dev_id_notification: Enable/disable device ID notification.
            dev_id: Device ID carried by the device ID notification.
            loopback_asymroute: Enable/disable asymmetric routing for IKE traffic on loopback interface.
            link_cost: VPN tunnel underlay link cost.
            kms: Key Management Services server.
            exchange_fgt_device_id: Enable/disable device identifier exchange with peer FortiGate units for use of VPN monitor data by FortiManager.
            ipv6_auto_linklocal: Enable/disable auto generation of IPv6 link-local address using last 8 bytes of mode-cfg assigned IPv6 address.
            ems_sn_check: Enable/disable verification of EMS serial number.
            cert_trust_store: CA certificate trust store.
            qkd: Enable/disable use of Quantum Key Distribution (QKD) server.
            qkd_hybrid: Enable/disable use of Quantum Key Distribution (QKD) hybrid keys.
            qkd_profile: Quantum Key Distribution (QKD) server profile.
            transport: Set IKE transport protocol.
            fortinet_esp: Enable/disable Fortinet ESP encapsulation.
            auto_transport_threshold: Timeout in seconds before falling back to next transport protocol.
            remote_gw_match: Set type of IPv4 remote gateway address matching.
            remote_gw_subnet: IPv4 address and subnet mask.
            remote_gw_start_ip: First IPv4 address in the range.
            remote_gw_end_ip: Last IPv4 address in the range.
            remote_gw_country: IPv4 addresses associated to a specific country.
            remote_gw_ztna_tags: IPv4 ZTNA posture tags.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            remote_gw6_match: Set type of IPv6 remote gateway address matching.
            remote_gw6_subnet: IPv6 address and prefix.
            remote_gw6_start_ip: First IPv6 address in the range.
            remote_gw6_end_ip: Last IPv6 address in the range.
            remote_gw6_country: IPv6 addresses associated to a specific country.
            cert_peer_username_validation: Enable/disable cross validation of peer username and the identity in the peer's certificate.
            cert_peer_username_strip: Enable/disable domain stripping on certificate identity.
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if certificate is not None:
            certificate = normalize_table_field(
                certificate,
                mkey="name",
                required_fields=['name'],
                field_name="certificate",
                example="[{'name': 'value'}]",
            )
        if internal_domain_list is not None:
            internal_domain_list = normalize_table_field(
                internal_domain_list,
                mkey="domain-name",
                required_fields=['domain-name'],
                field_name="internal_domain_list",
                example="[{'domain-name': 'value'}]",
            )
        if dns_suffix_search is not None:
            dns_suffix_search = normalize_table_field(
                dns_suffix_search,
                mkey="dns-suffix",
                required_fields=['dns-suffix'],
                field_name="dns_suffix_search",
                example="[{'dns-suffix': 'value'}]",
            )
        if ipv4_exclude_range is not None:
            ipv4_exclude_range = normalize_table_field(
                ipv4_exclude_range,
                mkey="id",
                required_fields=['id', 'start-ip', 'end-ip'],
                field_name="ipv4_exclude_range",
                example="[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
            )
        if ipv6_exclude_range is not None:
            ipv6_exclude_range = normalize_table_field(
                ipv6_exclude_range,
                mkey="id",
                required_fields=['id', 'start-ip', 'end-ip'],
                field_name="ipv6_exclude_range",
                example="[{'id': 1, 'start-ip': 'value', 'end-ip': 'value'}]",
            )
        if backup_gateway is not None:
            backup_gateway = normalize_table_field(
                backup_gateway,
                mkey="address",
                required_fields=['address'],
                field_name="backup_gateway",
                example="[{'address': 'value'}]",
            )
        if remote_gw_ztna_tags is not None:
            remote_gw_ztna_tags = normalize_table_field(
                remote_gw_ztna_tags,
                mkey="name",
                required_fields=['name'],
                field_name="remote_gw_ztna_tags",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            type=type,
            interface=interface,
            ike_version=ike_version,
            remote_gw=remote_gw,
            local_gw=local_gw,
            remotegw_ddns=remotegw_ddns,
            keylife=keylife,
            certificate=certificate,
            authmethod=authmethod,
            authmethod_remote=authmethod_remote,
            mode=mode,
            peertype=peertype,
            peerid=peerid,
            usrgrp=usrgrp,
            peer=peer,
            peergrp=peergrp,
            mode_cfg=mode_cfg,
            mode_cfg_allow_client_selector=mode_cfg_allow_client_selector,
            assign_ip=assign_ip,
            assign_ip_from=assign_ip_from,
            ipv4_start_ip=ipv4_start_ip,
            ipv4_end_ip=ipv4_end_ip,
            ipv4_netmask=ipv4_netmask,
            dhcp_ra_giaddr=dhcp_ra_giaddr,
            dhcp6_ra_linkaddr=dhcp6_ra_linkaddr,
            dns_mode=dns_mode,
            ipv4_dns_server1=ipv4_dns_server1,
            ipv4_dns_server2=ipv4_dns_server2,
            ipv4_dns_server3=ipv4_dns_server3,
            internal_domain_list=internal_domain_list,
            dns_suffix_search=dns_suffix_search,
            ipv4_wins_server1=ipv4_wins_server1,
            ipv4_wins_server2=ipv4_wins_server2,
            ipv4_exclude_range=ipv4_exclude_range,
            ipv4_split_include=ipv4_split_include,
            split_include_service=split_include_service,
            ipv4_name=ipv4_name,
            ipv6_start_ip=ipv6_start_ip,
            ipv6_end_ip=ipv6_end_ip,
            ipv6_prefix=ipv6_prefix,
            ipv6_dns_server1=ipv6_dns_server1,
            ipv6_dns_server2=ipv6_dns_server2,
            ipv6_dns_server3=ipv6_dns_server3,
            ipv6_exclude_range=ipv6_exclude_range,
            ipv6_split_include=ipv6_split_include,
            ipv6_name=ipv6_name,
            ip_delay_interval=ip_delay_interval,
            unity_support=unity_support,
            domain=domain,
            banner=banner,
            include_local_lan=include_local_lan,
            ipv4_split_exclude=ipv4_split_exclude,
            ipv6_split_exclude=ipv6_split_exclude,
            save_password=save_password,
            client_auto_negotiate=client_auto_negotiate,
            client_keep_alive=client_keep_alive,
            backup_gateway=backup_gateway,
            proposal=proposal,
            add_route=add_route,
            add_gw_route=add_gw_route,
            psksecret=psksecret,
            psksecret_remote=psksecret_remote,
            keepalive=keepalive,
            distance=distance,
            priority=priority,
            localid=localid,
            localid_type=localid_type,
            auto_negotiate=auto_negotiate,
            negotiate_timeout=negotiate_timeout,
            fragmentation=fragmentation,
            dpd=dpd,
            dpd_retrycount=dpd_retrycount,
            dpd_retryinterval=dpd_retryinterval,
            comments=comments,
            npu_offload=npu_offload,
            send_cert_chain=send_cert_chain,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            suite_b=suite_b,
            eap=eap,
            eap_identity=eap_identity,
            eap_exclude_peergrp=eap_exclude_peergrp,
            eap_cert_auth=eap_cert_auth,
            acct_verify=acct_verify,
            ppk=ppk,
            ppk_secret=ppk_secret,
            ppk_identity=ppk_identity,
            wizard_type=wizard_type,
            xauthtype=xauthtype,
            reauth=reauth,
            authusr=authusr,
            authpasswd=authpasswd,
            group_authentication=group_authentication,
            group_authentication_secret=group_authentication_secret,
            authusrgrp=authusrgrp,
            mesh_selector_type=mesh_selector_type,
            idle_timeout=idle_timeout,
            shared_idle_timeout=shared_idle_timeout,
            idle_timeoutinterval=idle_timeoutinterval,
            ha_sync_esp_seqno=ha_sync_esp_seqno,
            fgsp_sync=fgsp_sync,
            inbound_dscp_copy=inbound_dscp_copy,
            nattraversal=nattraversal,
            esn=esn,
            fragmentation_mtu=fragmentation_mtu,
            childless_ike=childless_ike,
            azure_ad_autoconnect=azure_ad_autoconnect,
            client_resume=client_resume,
            client_resume_interval=client_resume_interval,
            rekey=rekey,
            digital_signature_auth=digital_signature_auth,
            signature_hash_alg=signature_hash_alg,
            rsa_signature_format=rsa_signature_format,
            rsa_signature_hash_override=rsa_signature_hash_override,
            enforce_unique_id=enforce_unique_id,
            cert_id_validation=cert_id_validation,
            fec_egress=fec_egress,
            fec_send_timeout=fec_send_timeout,
            fec_base=fec_base,
            fec_codec=fec_codec,
            fec_redundant=fec_redundant,
            fec_ingress=fec_ingress,
            fec_receive_timeout=fec_receive_timeout,
            fec_health_check=fec_health_check,
            fec_mapping_profile=fec_mapping_profile,
            network_overlay=network_overlay,
            network_id=network_id,
            dev_id_notification=dev_id_notification,
            dev_id=dev_id,
            loopback_asymroute=loopback_asymroute,
            link_cost=link_cost,
            kms=kms,
            exchange_fgt_device_id=exchange_fgt_device_id,
            ipv6_auto_linklocal=ipv6_auto_linklocal,
            ems_sn_check=ems_sn_check,
            cert_trust_store=cert_trust_store,
            qkd=qkd,
            qkd_hybrid=qkd_hybrid,
            qkd_profile=qkd_profile,
            transport=transport,
            fortinet_esp=fortinet_esp,
            auto_transport_threshold=auto_transport_threshold,
            remote_gw_match=remote_gw_match,
            remote_gw_subnet=remote_gw_subnet,
            remote_gw_start_ip=remote_gw_start_ip,
            remote_gw_end_ip=remote_gw_end_ip,
            remote_gw_country=remote_gw_country,
            remote_gw_ztna_tags=remote_gw_ztna_tags,
            remote_gw6_match=remote_gw6_match,
            remote_gw6_subnet=remote_gw6_subnet,
            remote_gw6_start_ip=remote_gw6_start_ip,
            remote_gw6_end_ip=remote_gw6_end_ip,
            remote_gw6_country=remote_gw6_country,
            cert_peer_username_validation=cert_peer_username_validation,
            cert_peer_username_strip=cert_peer_username_strip,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.phase1 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase1",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/vpn.ipsec/phase1/" + str(name_value)

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
        type: Literal["static", "dynamic", "ddns"] | None = None,
        interface: str | None = None,
        ike_version: Literal["1", "2"] | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list[str] | list[dict[str, Any]] | None = None,
        authmethod: Literal["psk", "signature"] | None = None,
        authmethod_remote: Literal["psk", "signature"] | None = None,
        mode: Literal["aggressive", "main"] | None = None,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        mode_cfg: Literal["disable", "enable"] | None = None,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = None,
        assign_ip: Literal["disable", "enable"] | None = None,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: Literal["manual", "auto"] | None = None,
        ipv4_dns_server1: str | None = None,
        ipv4_dns_server2: str | None = None,
        ipv4_dns_server3: str | None = None,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = None,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = None,
        ipv4_wins_server1: str | None = None,
        ipv4_wins_server2: str | None = None,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        ipv4_split_include: str | None = None,
        split_include_service: str | None = None,
        ipv4_name: str | None = None,
        ipv6_start_ip: str | None = None,
        ipv6_end_ip: str | None = None,
        ipv6_prefix: int | None = None,
        ipv6_dns_server1: str | None = None,
        ipv6_dns_server2: str | None = None,
        ipv6_dns_server3: str | None = None,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        ipv6_split_include: str | None = None,
        ipv6_name: str | None = None,
        ip_delay_interval: int | None = None,
        unity_support: Literal["disable", "enable"] | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: Literal["disable", "enable"] | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: Literal["disable", "enable"] | None = None,
        client_auto_negotiate: Literal["disable", "enable"] | None = None,
        client_keep_alive: Literal["disable", "enable"] | None = None,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = None,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = None,
        add_route: Literal["disable", "enable"] | None = None,
        add_gw_route: Literal["enable", "disable"] | None = None,
        psksecret: Any | None = None,
        psksecret_remote: Any | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = None,
        auto_negotiate: Literal["enable", "disable"] | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: Literal["enable", "disable"] | None = None,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: Literal["enable", "disable"] | None = None,
        send_cert_chain: Literal["enable", "disable"] | None = None,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = None,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = None,
        eap: Literal["enable", "disable"] | None = None,
        eap_identity: Literal["use-id-payload", "send-request"] | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: Literal["enable", "disable"] | None = None,
        acct_verify: Literal["enable", "disable"] | None = None,
        ppk: Literal["disable", "allow", "require"] | None = None,
        ppk_secret: Any | None = None,
        ppk_identity: str | None = None,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = None,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = None,
        reauth: Literal["disable", "enable"] | None = None,
        authusr: str | None = None,
        authpasswd: Any | None = None,
        group_authentication: Literal["enable", "disable"] | None = None,
        group_authentication_secret: Any | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = None,
        idle_timeout: Literal["enable", "disable"] | None = None,
        shared_idle_timeout: Literal["enable", "disable"] | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = None,
        fgsp_sync: Literal["enable", "disable"] | None = None,
        inbound_dscp_copy: Literal["enable", "disable"] | None = None,
        nattraversal: Literal["enable", "disable", "forced"] | None = None,
        esn: Literal["require", "allow", "disable"] | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: Literal["enable", "disable"] | None = None,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = None,
        client_resume: Literal["enable", "disable"] | None = None,
        client_resume_interval: int | None = None,
        rekey: Literal["enable", "disable"] | None = None,
        digital_signature_auth: Literal["enable", "disable"] | None = None,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | None = None,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = None,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = None,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = None,
        cert_id_validation: Literal["enable", "disable"] | None = None,
        fec_egress: Literal["enable", "disable"] | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: Literal["rs", "xor"] | None = None,
        fec_redundant: int | None = None,
        fec_ingress: Literal["enable", "disable"] | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: Literal["disable", "enable"] | None = None,
        network_id: int | None = None,
        dev_id_notification: Literal["disable", "enable"] | None = None,
        dev_id: str | None = None,
        loopback_asymroute: Literal["enable", "disable"] | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = None,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = None,
        ems_sn_check: Literal["enable", "disable"] | None = None,
        cert_trust_store: Literal["local", "ems"] | None = None,
        qkd: Literal["disable", "allow", "require"] | None = None,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = None,
        qkd_profile: str | None = None,
        transport: Literal["udp", "auto", "tcp"] | None = None,
        fortinet_esp: Literal["enable", "disable"] | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = None,
        remote_gw_subnet: Any | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = None,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = None,
        cert_peer_username_strip: Literal["disable", "enable"] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new vpn/ipsec/phase1 object.

        Configure VPN remote gateway.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: IPsec remote gateway name.
            type: Remote gateway type.
            interface: Local physical, aggregate, or VLAN outgoing interface.
            ike_version: IKE protocol version.
            remote_gw: Remote VPN gateway.
            local_gw: Local VPN gateway.
            remotegw_ddns: Domain name of remote gateway. For example, name.ddns.com.
            keylife: Time to wait in seconds before phase 1 encryption key expires.
            certificate: Names of up to 4 signed personal certificates.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            authmethod: Authentication method.
            authmethod_remote: Authentication method (remote side).
            mode: ID protection mode used to establish a secure channel.
            peertype: Accept this peer type.
            peerid: Accept this peer identity.
            usrgrp: User group name for dialup peers.
            peer: Accept this peer certificate.
            peergrp: Accept this peer certificate group.
            mode_cfg: Enable/disable configuration method.
            mode_cfg_allow_client_selector: Enable/disable mode-cfg client to use custom phase2 selectors.
            assign_ip: Enable/disable assignment of IP to IPsec interface via configuration method.
            assign_ip_from: Method by which the IP address will be assigned.
            ipv4_start_ip: Start of IPv4 range.
            ipv4_end_ip: End of IPv4 range.
            ipv4_netmask: IPv4 Netmask.
            dhcp_ra_giaddr: Relay agent gateway IP address to use in the giaddr field of DHCP requests.
            dhcp6_ra_linkaddr: Relay agent IPv6 link address to use in DHCP6 requests.
            dns_mode: DNS server mode.
            ipv4_dns_server1: IPv4 DNS server 1.
            ipv4_dns_server2: IPv4 DNS server 2.
            ipv4_dns_server3: IPv4 DNS server 3.
            internal_domain_list: One or more internal domain names in quotes separated by spaces.
                Default format: [{'domain-name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'domain-name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'domain-name': 'val1'}, ...]
                  - List of dicts: [{'domain-name': 'value'}] (recommended)
            dns_suffix_search: One or more DNS domain name suffixes in quotes separated by spaces.
                Default format: [{'dns-suffix': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'dns-suffix': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'dns-suffix': 'val1'}, ...]
                  - List of dicts: [{'dns-suffix': 'value'}] (recommended)
            ipv4_wins_server1: WINS server 1.
            ipv4_wins_server2: WINS server 2.
            ipv4_exclude_range: Configuration Method IPv4 exclude ranges.
                Default format: [{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]
                Required format: List of dicts with keys: id, start-ip, end-ip
                  (String format not allowed due to multiple required fields)
            ipv4_split_include: IPv4 split-include subnets.
            split_include_service: Split-include services.
            ipv4_name: IPv4 address name.
            ipv6_start_ip: Start of IPv6 range.
            ipv6_end_ip: End of IPv6 range.
            ipv6_prefix: IPv6 prefix.
            ipv6_dns_server1: IPv6 DNS server 1.
            ipv6_dns_server2: IPv6 DNS server 2.
            ipv6_dns_server3: IPv6 DNS server 3.
            ipv6_exclude_range: Configuration method IPv6 exclude ranges.
                Default format: [{'id': 1, 'start-ip': 'value', 'end-ip': 'value'}]
                Required format: List of dicts with keys: id, start-ip, end-ip
                  (String format not allowed due to multiple required fields)
            ipv6_split_include: IPv6 split-include subnets.
            ipv6_name: IPv6 address name.
            ip_delay_interval: IP address reuse delay interval in seconds (0 - 28800).
            unity_support: Enable/disable support for Cisco UNITY Configuration Method extensions.
            domain: Instruct unity clients about the single default DNS domain.
            banner: Message that unity client should display after connecting.
            include_local_lan: Enable/disable allow local LAN access on unity clients.
            ipv4_split_exclude: IPv4 subnets that should not be sent over the IPsec tunnel.
            ipv6_split_exclude: IPv6 subnets that should not be sent over the IPsec tunnel.
            save_password: Enable/disable saving XAuth username and password on VPN clients.
            client_auto_negotiate: Enable/disable allowing the VPN client to bring up the tunnel when there is no traffic.
            client_keep_alive: Enable/disable allowing the VPN client to keep the tunnel up when there is no traffic.
            backup_gateway: Instruct unity clients about the backup gateway address(es).
                Default format: [{'address': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'address': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'address': 'val1'}, ...]
                  - List of dicts: [{'address': 'value'}] (recommended)
            proposal: Phase1 proposal.
            add_route: Enable/disable control addition of a route to peer destination selector.
            add_gw_route: Enable/disable automatically add a route to the remote gateway.
            psksecret: Pre-shared secret for PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).
            psksecret_remote: Pre-shared secret for remote side PSK authentication (ASCII string or hexadecimal encoded with a leading 0x).
            keepalive: NAT-T keep alive interval.
            distance: Distance for routes added by IKE (1 - 255).
            priority: Priority for routes added by IKE (1 - 65535).
            localid: Local ID.
            localid_type: Local ID type.
            auto_negotiate: Enable/disable automatic initiation of IKE SA negotiation.
            negotiate_timeout: IKE SA negotiation timeout in seconds (1 - 300).
            fragmentation: Enable/disable fragment IKE message on re-transmission.
            dpd: Dead Peer Detection mode.
            dpd_retrycount: Number of DPD retry attempts.
            dpd_retryinterval: DPD retry interval.
            comments: Comment.
            npu_offload: Enable/disable offloading NPU.
            send_cert_chain: Enable/disable sending certificate chain.
            dhgrp: DH group.
            addke1: ADDKE1 group.
            addke2: ADDKE2 group.
            addke3: ADDKE3 group.
            addke4: ADDKE4 group.
            addke5: ADDKE5 group.
            addke6: ADDKE6 group.
            addke7: ADDKE7 group.
            suite_b: Use Suite-B.
            eap: Enable/disable IKEv2 EAP authentication.
            eap_identity: IKEv2 EAP peer identity type.
            eap_exclude_peergrp: Peer group excluded from EAP authentication.
            eap_cert_auth: Enable/disable peer certificate authentication in addition to EAP if peer is a FortiClient endpoint.
            acct_verify: Enable/disable verification of RADIUS accounting record.
            ppk: Enable/disable IKEv2 Postquantum Preshared Key (PPK).
            ppk_secret: IKEv2 Postquantum Preshared Key (ASCII string or hexadecimal encoded with a leading 0x).
            ppk_identity: IKEv2 Postquantum Preshared Key Identity.
            wizard_type: GUI VPN Wizard Type.
            xauthtype: XAuth type.
            reauth: Enable/disable re-authentication upon IKE SA lifetime expiration.
            authusr: XAuth user name.
            authpasswd: XAuth password (max 35 characters).
            group_authentication: Enable/disable IKEv2 IDi group authentication.
            group_authentication_secret: Password for IKEv2 ID group authentication. ASCII string or hexadecimal indicated by a leading 0x.
            authusrgrp: Authentication user group.
            mesh_selector_type: Add selectors containing subsets of the configuration depending on traffic.
            idle_timeout: Enable/disable IPsec tunnel idle timeout.
            shared_idle_timeout: Enable/disable IPsec tunnel shared idle timeout.
            idle_timeoutinterval: IPsec tunnel idle timeout in minutes (5 - 43200).
            ha_sync_esp_seqno: Enable/disable sequence number jump ahead for IPsec HA.
            fgsp_sync: Enable/disable IPsec syncing of tunnels for FGSP IPsec.
            inbound_dscp_copy: Enable/disable copy the dscp in the ESP header to the inner IP Header.
            nattraversal: Enable/disable NAT traversal.
            esn: Extended sequence number (ESN) negotiation.
            fragmentation_mtu: IKE fragmentation MTU (500 - 16000).
            childless_ike: Enable/disable childless IKEv2 initiation (RFC 6023).
            azure_ad_autoconnect: Enable/disable Azure AD Auto-Connect for FortiClient.
            client_resume: Enable/disable resumption of offline FortiClient sessions.  When a FortiClient enabled laptop is closed or enters sleep/hibernate mode, enabling this feature allows FortiClient to keep the tunnel during this period, and allows users to immediately resume using the IPsec tunnel when the device wakes up.
            client_resume_interval: Maximum time in seconds during which a VPN client may resume using a tunnel after a client PC has entered sleep mode or temporarily lost its network connection (120 - 172800, default = 7200).
            rekey: Enable/disable phase1 rekey.
            digital_signature_auth: Enable/disable IKEv2 Digital Signature Authentication (RFC 7427).
            signature_hash_alg: Digital Signature Authentication hash algorithms.
            rsa_signature_format: Digital Signature Authentication RSA signature format.
            rsa_signature_hash_override: Enable/disable IKEv2 RSA signature hash algorithm override.
            enforce_unique_id: Enable/disable peer ID uniqueness check.
            cert_id_validation: Enable/disable cross validation of peer ID and the identity in the peer's certificate as specified in RFC 4945.
            fec_egress: Enable/disable Forward Error Correction for egress IPsec traffic.
            fec_send_timeout: Timeout in milliseconds before sending Forward Error Correction packets (1 - 1000).
            fec_base: Number of base Forward Error Correction packets (1 - 20).
            fec_codec: Forward Error Correction encoding/decoding algorithm.
            fec_redundant: Number of redundant Forward Error Correction packets (1 - 5 for reed-solomon, 1 for xor).
            fec_ingress: Enable/disable Forward Error Correction for ingress IPsec traffic.
            fec_receive_timeout: Timeout in milliseconds before dropping Forward Error Correction packets (1 - 1000).
            fec_health_check: SD-WAN health check.
            fec_mapping_profile: Forward Error Correction (FEC) mapping profile.
            network_overlay: Enable/disable network overlays.
            network_id: VPN gateway network ID.
            dev_id_notification: Enable/disable device ID notification.
            dev_id: Device ID carried by the device ID notification.
            loopback_asymroute: Enable/disable asymmetric routing for IKE traffic on loopback interface.
            link_cost: VPN tunnel underlay link cost.
            kms: Key Management Services server.
            exchange_fgt_device_id: Enable/disable device identifier exchange with peer FortiGate units for use of VPN monitor data by FortiManager.
            ipv6_auto_linklocal: Enable/disable auto generation of IPv6 link-local address using last 8 bytes of mode-cfg assigned IPv6 address.
            ems_sn_check: Enable/disable verification of EMS serial number.
            cert_trust_store: CA certificate trust store.
            qkd: Enable/disable use of Quantum Key Distribution (QKD) server.
            qkd_hybrid: Enable/disable use of Quantum Key Distribution (QKD) hybrid keys.
            qkd_profile: Quantum Key Distribution (QKD) server profile.
            transport: Set IKE transport protocol.
            fortinet_esp: Enable/disable Fortinet ESP encapsulation.
            auto_transport_threshold: Timeout in seconds before falling back to next transport protocol.
            remote_gw_match: Set type of IPv4 remote gateway address matching.
            remote_gw_subnet: IPv4 address and subnet mask.
            remote_gw_start_ip: First IPv4 address in the range.
            remote_gw_end_ip: Last IPv4 address in the range.
            remote_gw_country: IPv4 addresses associated to a specific country.
            remote_gw_ztna_tags: IPv4 ZTNA posture tags.
                Default format: [{'name': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'name': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'name': 'val1'}, ...]
                  - List of dicts: [{'name': 'value'}] (recommended)
            remote_gw6_match: Set type of IPv6 remote gateway address matching.
            remote_gw6_subnet: IPv6 address and prefix.
            remote_gw6_start_ip: First IPv6 address in the range.
            remote_gw6_end_ip: Last IPv6 address in the range.
            remote_gw6_country: IPv6 addresses associated to a specific country.
            cert_peer_username_validation: Enable/disable cross validation of peer username and the identity in the peer's certificate.
            cert_peer_username_strip: Enable/disable domain stripping on certificate identity.
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Phase1.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Phase1.required_fields()) }}
            
            Use Phase1.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if certificate is not None:
            certificate = normalize_table_field(
                certificate,
                mkey="name",
                required_fields=['name'],
                field_name="certificate",
                example="[{'name': 'value'}]",
            )
        if internal_domain_list is not None:
            internal_domain_list = normalize_table_field(
                internal_domain_list,
                mkey="domain-name",
                required_fields=['domain-name'],
                field_name="internal_domain_list",
                example="[{'domain-name': 'value'}]",
            )
        if dns_suffix_search is not None:
            dns_suffix_search = normalize_table_field(
                dns_suffix_search,
                mkey="dns-suffix",
                required_fields=['dns-suffix'],
                field_name="dns_suffix_search",
                example="[{'dns-suffix': 'value'}]",
            )
        if ipv4_exclude_range is not None:
            ipv4_exclude_range = normalize_table_field(
                ipv4_exclude_range,
                mkey="id",
                required_fields=['id', 'start-ip', 'end-ip'],
                field_name="ipv4_exclude_range",
                example="[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
            )
        if ipv6_exclude_range is not None:
            ipv6_exclude_range = normalize_table_field(
                ipv6_exclude_range,
                mkey="id",
                required_fields=['id', 'start-ip', 'end-ip'],
                field_name="ipv6_exclude_range",
                example="[{'id': 1, 'start-ip': 'value', 'end-ip': 'value'}]",
            )
        if backup_gateway is not None:
            backup_gateway = normalize_table_field(
                backup_gateway,
                mkey="address",
                required_fields=['address'],
                field_name="backup_gateway",
                example="[{'address': 'value'}]",
            )
        if remote_gw_ztna_tags is not None:
            remote_gw_ztna_tags = normalize_table_field(
                remote_gw_ztna_tags,
                mkey="name",
                required_fields=['name'],
                field_name="remote_gw_ztna_tags",
                example="[{'name': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            type=type,
            interface=interface,
            ike_version=ike_version,
            remote_gw=remote_gw,
            local_gw=local_gw,
            remotegw_ddns=remotegw_ddns,
            keylife=keylife,
            certificate=certificate,
            authmethod=authmethod,
            authmethod_remote=authmethod_remote,
            mode=mode,
            peertype=peertype,
            peerid=peerid,
            usrgrp=usrgrp,
            peer=peer,
            peergrp=peergrp,
            mode_cfg=mode_cfg,
            mode_cfg_allow_client_selector=mode_cfg_allow_client_selector,
            assign_ip=assign_ip,
            assign_ip_from=assign_ip_from,
            ipv4_start_ip=ipv4_start_ip,
            ipv4_end_ip=ipv4_end_ip,
            ipv4_netmask=ipv4_netmask,
            dhcp_ra_giaddr=dhcp_ra_giaddr,
            dhcp6_ra_linkaddr=dhcp6_ra_linkaddr,
            dns_mode=dns_mode,
            ipv4_dns_server1=ipv4_dns_server1,
            ipv4_dns_server2=ipv4_dns_server2,
            ipv4_dns_server3=ipv4_dns_server3,
            internal_domain_list=internal_domain_list,
            dns_suffix_search=dns_suffix_search,
            ipv4_wins_server1=ipv4_wins_server1,
            ipv4_wins_server2=ipv4_wins_server2,
            ipv4_exclude_range=ipv4_exclude_range,
            ipv4_split_include=ipv4_split_include,
            split_include_service=split_include_service,
            ipv4_name=ipv4_name,
            ipv6_start_ip=ipv6_start_ip,
            ipv6_end_ip=ipv6_end_ip,
            ipv6_prefix=ipv6_prefix,
            ipv6_dns_server1=ipv6_dns_server1,
            ipv6_dns_server2=ipv6_dns_server2,
            ipv6_dns_server3=ipv6_dns_server3,
            ipv6_exclude_range=ipv6_exclude_range,
            ipv6_split_include=ipv6_split_include,
            ipv6_name=ipv6_name,
            ip_delay_interval=ip_delay_interval,
            unity_support=unity_support,
            domain=domain,
            banner=banner,
            include_local_lan=include_local_lan,
            ipv4_split_exclude=ipv4_split_exclude,
            ipv6_split_exclude=ipv6_split_exclude,
            save_password=save_password,
            client_auto_negotiate=client_auto_negotiate,
            client_keep_alive=client_keep_alive,
            backup_gateway=backup_gateway,
            proposal=proposal,
            add_route=add_route,
            add_gw_route=add_gw_route,
            psksecret=psksecret,
            psksecret_remote=psksecret_remote,
            keepalive=keepalive,
            distance=distance,
            priority=priority,
            localid=localid,
            localid_type=localid_type,
            auto_negotiate=auto_negotiate,
            negotiate_timeout=negotiate_timeout,
            fragmentation=fragmentation,
            dpd=dpd,
            dpd_retrycount=dpd_retrycount,
            dpd_retryinterval=dpd_retryinterval,
            comments=comments,
            npu_offload=npu_offload,
            send_cert_chain=send_cert_chain,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            suite_b=suite_b,
            eap=eap,
            eap_identity=eap_identity,
            eap_exclude_peergrp=eap_exclude_peergrp,
            eap_cert_auth=eap_cert_auth,
            acct_verify=acct_verify,
            ppk=ppk,
            ppk_secret=ppk_secret,
            ppk_identity=ppk_identity,
            wizard_type=wizard_type,
            xauthtype=xauthtype,
            reauth=reauth,
            authusr=authusr,
            authpasswd=authpasswd,
            group_authentication=group_authentication,
            group_authentication_secret=group_authentication_secret,
            authusrgrp=authusrgrp,
            mesh_selector_type=mesh_selector_type,
            idle_timeout=idle_timeout,
            shared_idle_timeout=shared_idle_timeout,
            idle_timeoutinterval=idle_timeoutinterval,
            ha_sync_esp_seqno=ha_sync_esp_seqno,
            fgsp_sync=fgsp_sync,
            inbound_dscp_copy=inbound_dscp_copy,
            nattraversal=nattraversal,
            esn=esn,
            fragmentation_mtu=fragmentation_mtu,
            childless_ike=childless_ike,
            azure_ad_autoconnect=azure_ad_autoconnect,
            client_resume=client_resume,
            client_resume_interval=client_resume_interval,
            rekey=rekey,
            digital_signature_auth=digital_signature_auth,
            signature_hash_alg=signature_hash_alg,
            rsa_signature_format=rsa_signature_format,
            rsa_signature_hash_override=rsa_signature_hash_override,
            enforce_unique_id=enforce_unique_id,
            cert_id_validation=cert_id_validation,
            fec_egress=fec_egress,
            fec_send_timeout=fec_send_timeout,
            fec_base=fec_base,
            fec_codec=fec_codec,
            fec_redundant=fec_redundant,
            fec_ingress=fec_ingress,
            fec_receive_timeout=fec_receive_timeout,
            fec_health_check=fec_health_check,
            fec_mapping_profile=fec_mapping_profile,
            network_overlay=network_overlay,
            network_id=network_id,
            dev_id_notification=dev_id_notification,
            dev_id=dev_id,
            loopback_asymroute=loopback_asymroute,
            link_cost=link_cost,
            kms=kms,
            exchange_fgt_device_id=exchange_fgt_device_id,
            ipv6_auto_linklocal=ipv6_auto_linklocal,
            ems_sn_check=ems_sn_check,
            cert_trust_store=cert_trust_store,
            qkd=qkd,
            qkd_hybrid=qkd_hybrid,
            qkd_profile=qkd_profile,
            transport=transport,
            fortinet_esp=fortinet_esp,
            auto_transport_threshold=auto_transport_threshold,
            remote_gw_match=remote_gw_match,
            remote_gw_subnet=remote_gw_subnet,
            remote_gw_start_ip=remote_gw_start_ip,
            remote_gw_end_ip=remote_gw_end_ip,
            remote_gw_country=remote_gw_country,
            remote_gw_ztna_tags=remote_gw_ztna_tags,
            remote_gw6_match=remote_gw6_match,
            remote_gw6_subnet=remote_gw6_subnet,
            remote_gw6_start_ip=remote_gw6_start_ip,
            remote_gw6_end_ip=remote_gw6_end_ip,
            remote_gw6_country=remote_gw6_country,
            cert_peer_username_validation=cert_peer_username_validation,
            cert_peer_username_strip=cert_peer_username_strip,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.phase1 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase1",
            )

        endpoint = "/vpn.ipsec/phase1"
        
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
        Delete vpn/ipsec/phase1 object.

        Configure VPN remote gateway.

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/vpn.ipsec/phase1/" + str(name)

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
        Check if vpn/ipsec/phase1 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.vpn_ipsec_phase1.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.vpn_ipsec_phase1.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase1.delete(name=1)

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
        type: Literal["static", "dynamic", "ddns"] | None = None,
        interface: str | None = None,
        ike_version: Literal["1", "2"] | None = None,
        remote_gw: str | None = None,
        local_gw: str | None = None,
        remotegw_ddns: str | None = None,
        keylife: int | None = None,
        certificate: str | list[str] | list[dict[str, Any]] | None = None,
        authmethod: Literal["psk", "signature"] | None = None,
        authmethod_remote: Literal["psk", "signature"] | None = None,
        mode: Literal["aggressive", "main"] | None = None,
        peertype: Literal["any", "one", "dialup", "peer", "peergrp"] | None = None,
        peerid: str | None = None,
        usrgrp: str | None = None,
        peer: str | None = None,
        peergrp: str | None = None,
        mode_cfg: Literal["disable", "enable"] | None = None,
        mode_cfg_allow_client_selector: Literal["disable", "enable"] | None = None,
        assign_ip: Literal["disable", "enable"] | None = None,
        assign_ip_from: Literal["range", "usrgrp", "dhcp", "name"] | None = None,
        ipv4_start_ip: str | None = None,
        ipv4_end_ip: str | None = None,
        ipv4_netmask: str | None = None,
        dhcp_ra_giaddr: str | None = None,
        dhcp6_ra_linkaddr: str | None = None,
        dns_mode: Literal["manual", "auto"] | None = None,
        ipv4_dns_server1: str | None = None,
        ipv4_dns_server2: str | None = None,
        ipv4_dns_server3: str | None = None,
        internal_domain_list: str | list[str] | list[dict[str, Any]] | None = None,
        dns_suffix_search: str | list[str] | list[dict[str, Any]] | None = None,
        ipv4_wins_server1: str | None = None,
        ipv4_wins_server2: str | None = None,
        ipv4_exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        ipv4_split_include: str | None = None,
        split_include_service: str | None = None,
        ipv4_name: str | None = None,
        ipv6_start_ip: str | None = None,
        ipv6_end_ip: str | None = None,
        ipv6_prefix: int | None = None,
        ipv6_dns_server1: str | None = None,
        ipv6_dns_server2: str | None = None,
        ipv6_dns_server3: str | None = None,
        ipv6_exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        ipv6_split_include: str | None = None,
        ipv6_name: str | None = None,
        ip_delay_interval: int | None = None,
        unity_support: Literal["disable", "enable"] | None = None,
        domain: str | None = None,
        banner: str | None = None,
        include_local_lan: Literal["disable", "enable"] | None = None,
        ipv4_split_exclude: str | None = None,
        ipv6_split_exclude: str | None = None,
        save_password: Literal["disable", "enable"] | None = None,
        client_auto_negotiate: Literal["disable", "enable"] | None = None,
        client_keep_alive: Literal["disable", "enable"] | None = None,
        backup_gateway: str | list[str] | list[dict[str, Any]] | None = None,
        proposal: Literal["des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm-prfsha1", "aes128gcm-prfsha256", "aes128gcm-prfsha384", "aes128gcm-prfsha512", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm-prfsha1", "aes256gcm-prfsha256", "aes256gcm-prfsha384", "aes256gcm-prfsha512", "chacha20poly1305-prfsha1", "chacha20poly1305-prfsha256", "chacha20poly1305-prfsha384", "chacha20poly1305-prfsha512", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | list[dict[str, Any]] | None = None,
        add_route: Literal["disable", "enable"] | None = None,
        add_gw_route: Literal["enable", "disable"] | None = None,
        psksecret: Any | None = None,
        psksecret_remote: Any | None = None,
        keepalive: int | None = None,
        distance: int | None = None,
        priority: int | None = None,
        localid: str | None = None,
        localid_type: Literal["auto", "fqdn", "user-fqdn", "keyid", "address", "asn1dn"] | None = None,
        auto_negotiate: Literal["enable", "disable"] | None = None,
        negotiate_timeout: int | None = None,
        fragmentation: Literal["enable", "disable"] | None = None,
        dpd: Literal["disable", "on-idle", "on-demand"] | None = None,
        dpd_retrycount: int | None = None,
        dpd_retryinterval: str | None = None,
        comments: str | None = None,
        npu_offload: Literal["enable", "disable"] | None = None,
        send_cert_chain: Literal["enable", "disable"] | None = None,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | list[dict[str, Any]] | None = None,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        suite_b: Literal["disable", "suite-b-gcm-128", "suite-b-gcm-256"] | None = None,
        eap: Literal["enable", "disable"] | None = None,
        eap_identity: Literal["use-id-payload", "send-request"] | None = None,
        eap_exclude_peergrp: str | None = None,
        eap_cert_auth: Literal["enable", "disable"] | None = None,
        acct_verify: Literal["enable", "disable"] | None = None,
        ppk: Literal["disable", "allow", "require"] | None = None,
        ppk_secret: Any | None = None,
        ppk_identity: str | None = None,
        wizard_type: Literal["custom", "dialup-forticlient", "dialup-ios", "dialup-android", "dialup-windows", "dialup-cisco", "static-fortigate", "dialup-fortigate", "static-cisco", "dialup-cisco-fw", "simplified-static-fortigate", "hub-fortigate-auto-discovery", "spoke-fortigate-auto-discovery", "fabric-overlay-orchestrator"] | None = None,
        xauthtype: Literal["disable", "client", "pap", "chap", "auto"] | None = None,
        reauth: Literal["disable", "enable"] | None = None,
        authusr: str | None = None,
        authpasswd: Any | None = None,
        group_authentication: Literal["enable", "disable"] | None = None,
        group_authentication_secret: Any | None = None,
        authusrgrp: str | None = None,
        mesh_selector_type: Literal["disable", "subnet", "host"] | None = None,
        idle_timeout: Literal["enable", "disable"] | None = None,
        shared_idle_timeout: Literal["enable", "disable"] | None = None,
        idle_timeoutinterval: int | None = None,
        ha_sync_esp_seqno: Literal["enable", "disable"] | None = None,
        fgsp_sync: Literal["enable", "disable"] | None = None,
        inbound_dscp_copy: Literal["enable", "disable"] | None = None,
        nattraversal: Literal["enable", "disable", "forced"] | None = None,
        esn: Literal["require", "allow", "disable"] | None = None,
        fragmentation_mtu: int | None = None,
        childless_ike: Literal["enable", "disable"] | None = None,
        azure_ad_autoconnect: Literal["enable", "disable"] | None = None,
        client_resume: Literal["enable", "disable"] | None = None,
        client_resume_interval: int | None = None,
        rekey: Literal["enable", "disable"] | None = None,
        digital_signature_auth: Literal["enable", "disable"] | None = None,
        signature_hash_alg: Literal["sha1", "sha2-256", "sha2-384", "sha2-512"] | list[str] | list[dict[str, Any]] | None = None,
        rsa_signature_format: Literal["pkcs1", "pss"] | None = None,
        rsa_signature_hash_override: Literal["enable", "disable"] | None = None,
        enforce_unique_id: Literal["disable", "keep-new", "keep-old"] | None = None,
        cert_id_validation: Literal["enable", "disable"] | None = None,
        fec_egress: Literal["enable", "disable"] | None = None,
        fec_send_timeout: int | None = None,
        fec_base: int | None = None,
        fec_codec: Literal["rs", "xor"] | None = None,
        fec_redundant: int | None = None,
        fec_ingress: Literal["enable", "disable"] | None = None,
        fec_receive_timeout: int | None = None,
        fec_health_check: str | None = None,
        fec_mapping_profile: str | None = None,
        network_overlay: Literal["disable", "enable"] | None = None,
        network_id: int | None = None,
        dev_id_notification: Literal["disable", "enable"] | None = None,
        dev_id: str | None = None,
        loopback_asymroute: Literal["enable", "disable"] | None = None,
        link_cost: int | None = None,
        kms: str | None = None,
        exchange_fgt_device_id: Literal["enable", "disable"] | None = None,
        ipv6_auto_linklocal: Literal["enable", "disable"] | None = None,
        ems_sn_check: Literal["enable", "disable"] | None = None,
        cert_trust_store: Literal["local", "ems"] | None = None,
        qkd: Literal["disable", "allow", "require"] | None = None,
        qkd_hybrid: Literal["disable", "allow", "require"] | None = None,
        qkd_profile: str | None = None,
        transport: Literal["udp", "auto", "tcp"] | None = None,
        fortinet_esp: Literal["enable", "disable"] | None = None,
        auto_transport_threshold: int | None = None,
        remote_gw_match: Literal["any", "ipmask", "iprange", "geography", "ztna"] | None = None,
        remote_gw_subnet: Any | None = None,
        remote_gw_start_ip: str | None = None,
        remote_gw_end_ip: str | None = None,
        remote_gw_country: str | None = None,
        remote_gw_ztna_tags: str | list[str] | list[dict[str, Any]] | None = None,
        remote_gw6_match: Literal["any", "ipprefix", "iprange", "geography"] | None = None,
        remote_gw6_subnet: str | None = None,
        remote_gw6_start_ip: str | None = None,
        remote_gw6_end_ip: str | None = None,
        remote_gw6_country: str | None = None,
        cert_peer_username_validation: Literal["none", "othername", "rfc822name", "cn"] | None = None,
        cert_peer_username_strip: Literal["disable", "enable"] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update vpn/ipsec/phase1 object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            type: Field type
            interface: Field interface
            ike_version: Field ike-version
            remote_gw: Field remote-gw
            local_gw: Field local-gw
            remotegw_ddns: Field remotegw-ddns
            keylife: Field keylife
            certificate: Field certificate
            authmethod: Field authmethod
            authmethod_remote: Field authmethod-remote
            mode: Field mode
            peertype: Field peertype
            peerid: Field peerid
            usrgrp: Field usrgrp
            peer: Field peer
            peergrp: Field peergrp
            mode_cfg: Field mode-cfg
            mode_cfg_allow_client_selector: Field mode-cfg-allow-client-selector
            assign_ip: Field assign-ip
            assign_ip_from: Field assign-ip-from
            ipv4_start_ip: Field ipv4-start-ip
            ipv4_end_ip: Field ipv4-end-ip
            ipv4_netmask: Field ipv4-netmask
            dhcp_ra_giaddr: Field dhcp-ra-giaddr
            dhcp6_ra_linkaddr: Field dhcp6-ra-linkaddr
            dns_mode: Field dns-mode
            ipv4_dns_server1: Field ipv4-dns-server1
            ipv4_dns_server2: Field ipv4-dns-server2
            ipv4_dns_server3: Field ipv4-dns-server3
            internal_domain_list: Field internal-domain-list
            dns_suffix_search: Field dns-suffix-search
            ipv4_wins_server1: Field ipv4-wins-server1
            ipv4_wins_server2: Field ipv4-wins-server2
            ipv4_exclude_range: Field ipv4-exclude-range
            ipv4_split_include: Field ipv4-split-include
            split_include_service: Field split-include-service
            ipv4_name: Field ipv4-name
            ipv6_start_ip: Field ipv6-start-ip
            ipv6_end_ip: Field ipv6-end-ip
            ipv6_prefix: Field ipv6-prefix
            ipv6_dns_server1: Field ipv6-dns-server1
            ipv6_dns_server2: Field ipv6-dns-server2
            ipv6_dns_server3: Field ipv6-dns-server3
            ipv6_exclude_range: Field ipv6-exclude-range
            ipv6_split_include: Field ipv6-split-include
            ipv6_name: Field ipv6-name
            ip_delay_interval: Field ip-delay-interval
            unity_support: Field unity-support
            domain: Field domain
            banner: Field banner
            include_local_lan: Field include-local-lan
            ipv4_split_exclude: Field ipv4-split-exclude
            ipv6_split_exclude: Field ipv6-split-exclude
            save_password: Field save-password
            client_auto_negotiate: Field client-auto-negotiate
            client_keep_alive: Field client-keep-alive
            backup_gateway: Field backup-gateway
            proposal: Field proposal
            add_route: Field add-route
            add_gw_route: Field add-gw-route
            psksecret: Field psksecret
            psksecret_remote: Field psksecret-remote
            keepalive: Field keepalive
            distance: Field distance
            priority: Field priority
            localid: Field localid
            localid_type: Field localid-type
            auto_negotiate: Field auto-negotiate
            negotiate_timeout: Field negotiate-timeout
            fragmentation: Field fragmentation
            dpd: Field dpd
            dpd_retrycount: Field dpd-retrycount
            dpd_retryinterval: Field dpd-retryinterval
            comments: Field comments
            npu_offload: Field npu-offload
            send_cert_chain: Field send-cert-chain
            dhgrp: Field dhgrp
            addke1: Field addke1
            addke2: Field addke2
            addke3: Field addke3
            addke4: Field addke4
            addke5: Field addke5
            addke6: Field addke6
            addke7: Field addke7
            suite_b: Field suite-b
            eap: Field eap
            eap_identity: Field eap-identity
            eap_exclude_peergrp: Field eap-exclude-peergrp
            eap_cert_auth: Field eap-cert-auth
            acct_verify: Field acct-verify
            ppk: Field ppk
            ppk_secret: Field ppk-secret
            ppk_identity: Field ppk-identity
            wizard_type: Field wizard-type
            xauthtype: Field xauthtype
            reauth: Field reauth
            authusr: Field authusr
            authpasswd: Field authpasswd
            group_authentication: Field group-authentication
            group_authentication_secret: Field group-authentication-secret
            authusrgrp: Field authusrgrp
            mesh_selector_type: Field mesh-selector-type
            idle_timeout: Field idle-timeout
            shared_idle_timeout: Field shared-idle-timeout
            idle_timeoutinterval: Field idle-timeoutinterval
            ha_sync_esp_seqno: Field ha-sync-esp-seqno
            fgsp_sync: Field fgsp-sync
            inbound_dscp_copy: Field inbound-dscp-copy
            nattraversal: Field nattraversal
            esn: Field esn
            fragmentation_mtu: Field fragmentation-mtu
            childless_ike: Field childless-ike
            azure_ad_autoconnect: Field azure-ad-autoconnect
            client_resume: Field client-resume
            client_resume_interval: Field client-resume-interval
            rekey: Field rekey
            digital_signature_auth: Field digital-signature-auth
            signature_hash_alg: Field signature-hash-alg
            rsa_signature_format: Field rsa-signature-format
            rsa_signature_hash_override: Field rsa-signature-hash-override
            enforce_unique_id: Field enforce-unique-id
            cert_id_validation: Field cert-id-validation
            fec_egress: Field fec-egress
            fec_send_timeout: Field fec-send-timeout
            fec_base: Field fec-base
            fec_codec: Field fec-codec
            fec_redundant: Field fec-redundant
            fec_ingress: Field fec-ingress
            fec_receive_timeout: Field fec-receive-timeout
            fec_health_check: Field fec-health-check
            fec_mapping_profile: Field fec-mapping-profile
            network_overlay: Field network-overlay
            network_id: Field network-id
            dev_id_notification: Field dev-id-notification
            dev_id: Field dev-id
            loopback_asymroute: Field loopback-asymroute
            link_cost: Field link-cost
            kms: Field kms
            exchange_fgt_device_id: Field exchange-fgt-device-id
            ipv6_auto_linklocal: Field ipv6-auto-linklocal
            ems_sn_check: Field ems-sn-check
            cert_trust_store: Field cert-trust-store
            qkd: Field qkd
            qkd_hybrid: Field qkd-hybrid
            qkd_profile: Field qkd-profile
            transport: Field transport
            fortinet_esp: Field fortinet-esp
            auto_transport_threshold: Field auto-transport-threshold
            remote_gw_match: Field remote-gw-match
            remote_gw_subnet: Field remote-gw-subnet
            remote_gw_start_ip: Field remote-gw-start-ip
            remote_gw_end_ip: Field remote-gw-end-ip
            remote_gw_country: Field remote-gw-country
            remote_gw_ztna_tags: Field remote-gw-ztna-tags
            remote_gw6_match: Field remote-gw6-match
            remote_gw6_subnet: Field remote-gw6-subnet
            remote_gw6_start_ip: Field remote-gw6-start-ip
            remote_gw6_end_ip: Field remote-gw6-end-ip
            remote_gw6_country: Field remote-gw6-country
            cert_peer_username_validation: Field cert-peer-username-validation
            cert_peer_username_strip: Field cert-peer-username-strip
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.vpn_ipsec_phase1.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.vpn_ipsec_phase1.set(payload_dict=obj_data)
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
            type=type,
            interface=interface,
            ike_version=ike_version,
            remote_gw=remote_gw,
            local_gw=local_gw,
            remotegw_ddns=remotegw_ddns,
            keylife=keylife,
            certificate=certificate,
            authmethod=authmethod,
            authmethod_remote=authmethod_remote,
            mode=mode,
            peertype=peertype,
            peerid=peerid,
            usrgrp=usrgrp,
            peer=peer,
            peergrp=peergrp,
            mode_cfg=mode_cfg,
            mode_cfg_allow_client_selector=mode_cfg_allow_client_selector,
            assign_ip=assign_ip,
            assign_ip_from=assign_ip_from,
            ipv4_start_ip=ipv4_start_ip,
            ipv4_end_ip=ipv4_end_ip,
            ipv4_netmask=ipv4_netmask,
            dhcp_ra_giaddr=dhcp_ra_giaddr,
            dhcp6_ra_linkaddr=dhcp6_ra_linkaddr,
            dns_mode=dns_mode,
            ipv4_dns_server1=ipv4_dns_server1,
            ipv4_dns_server2=ipv4_dns_server2,
            ipv4_dns_server3=ipv4_dns_server3,
            internal_domain_list=internal_domain_list,
            dns_suffix_search=dns_suffix_search,
            ipv4_wins_server1=ipv4_wins_server1,
            ipv4_wins_server2=ipv4_wins_server2,
            ipv4_exclude_range=ipv4_exclude_range,
            ipv4_split_include=ipv4_split_include,
            split_include_service=split_include_service,
            ipv4_name=ipv4_name,
            ipv6_start_ip=ipv6_start_ip,
            ipv6_end_ip=ipv6_end_ip,
            ipv6_prefix=ipv6_prefix,
            ipv6_dns_server1=ipv6_dns_server1,
            ipv6_dns_server2=ipv6_dns_server2,
            ipv6_dns_server3=ipv6_dns_server3,
            ipv6_exclude_range=ipv6_exclude_range,
            ipv6_split_include=ipv6_split_include,
            ipv6_name=ipv6_name,
            ip_delay_interval=ip_delay_interval,
            unity_support=unity_support,
            domain=domain,
            banner=banner,
            include_local_lan=include_local_lan,
            ipv4_split_exclude=ipv4_split_exclude,
            ipv6_split_exclude=ipv6_split_exclude,
            save_password=save_password,
            client_auto_negotiate=client_auto_negotiate,
            client_keep_alive=client_keep_alive,
            backup_gateway=backup_gateway,
            proposal=proposal,
            add_route=add_route,
            add_gw_route=add_gw_route,
            psksecret=psksecret,
            psksecret_remote=psksecret_remote,
            keepalive=keepalive,
            distance=distance,
            priority=priority,
            localid=localid,
            localid_type=localid_type,
            auto_negotiate=auto_negotiate,
            negotiate_timeout=negotiate_timeout,
            fragmentation=fragmentation,
            dpd=dpd,
            dpd_retrycount=dpd_retrycount,
            dpd_retryinterval=dpd_retryinterval,
            comments=comments,
            npu_offload=npu_offload,
            send_cert_chain=send_cert_chain,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            suite_b=suite_b,
            eap=eap,
            eap_identity=eap_identity,
            eap_exclude_peergrp=eap_exclude_peergrp,
            eap_cert_auth=eap_cert_auth,
            acct_verify=acct_verify,
            ppk=ppk,
            ppk_secret=ppk_secret,
            ppk_identity=ppk_identity,
            wizard_type=wizard_type,
            xauthtype=xauthtype,
            reauth=reauth,
            authusr=authusr,
            authpasswd=authpasswd,
            group_authentication=group_authentication,
            group_authentication_secret=group_authentication_secret,
            authusrgrp=authusrgrp,
            mesh_selector_type=mesh_selector_type,
            idle_timeout=idle_timeout,
            shared_idle_timeout=shared_idle_timeout,
            idle_timeoutinterval=idle_timeoutinterval,
            ha_sync_esp_seqno=ha_sync_esp_seqno,
            fgsp_sync=fgsp_sync,
            inbound_dscp_copy=inbound_dscp_copy,
            nattraversal=nattraversal,
            esn=esn,
            fragmentation_mtu=fragmentation_mtu,
            childless_ike=childless_ike,
            azure_ad_autoconnect=azure_ad_autoconnect,
            client_resume=client_resume,
            client_resume_interval=client_resume_interval,
            rekey=rekey,
            digital_signature_auth=digital_signature_auth,
            signature_hash_alg=signature_hash_alg,
            rsa_signature_format=rsa_signature_format,
            rsa_signature_hash_override=rsa_signature_hash_override,
            enforce_unique_id=enforce_unique_id,
            cert_id_validation=cert_id_validation,
            fec_egress=fec_egress,
            fec_send_timeout=fec_send_timeout,
            fec_base=fec_base,
            fec_codec=fec_codec,
            fec_redundant=fec_redundant,
            fec_ingress=fec_ingress,
            fec_receive_timeout=fec_receive_timeout,
            fec_health_check=fec_health_check,
            fec_mapping_profile=fec_mapping_profile,
            network_overlay=network_overlay,
            network_id=network_id,
            dev_id_notification=dev_id_notification,
            dev_id=dev_id,
            loopback_asymroute=loopback_asymroute,
            link_cost=link_cost,
            kms=kms,
            exchange_fgt_device_id=exchange_fgt_device_id,
            ipv6_auto_linklocal=ipv6_auto_linklocal,
            ems_sn_check=ems_sn_check,
            cert_trust_store=cert_trust_store,
            qkd=qkd,
            qkd_hybrid=qkd_hybrid,
            qkd_profile=qkd_profile,
            transport=transport,
            fortinet_esp=fortinet_esp,
            auto_transport_threshold=auto_transport_threshold,
            remote_gw_match=remote_gw_match,
            remote_gw_subnet=remote_gw_subnet,
            remote_gw_start_ip=remote_gw_start_ip,
            remote_gw_end_ip=remote_gw_end_ip,
            remote_gw_country=remote_gw_country,
            remote_gw_ztna_tags=remote_gw_ztna_tags,
            remote_gw6_match=remote_gw6_match,
            remote_gw6_subnet=remote_gw6_subnet,
            remote_gw6_start_ip=remote_gw6_start_ip,
            remote_gw6_end_ip=remote_gw6_end_ip,
            remote_gw6_country=remote_gw6_country,
            cert_peer_username_validation=cert_peer_username_validation,
            cert_peer_username_strip=cert_peer_username_strip,
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
        Move vpn/ipsec/phase1 object to a new position.
        
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
            >>> fgt.api.cmdb.vpn_ipsec_phase1.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/vpn.ipsec/phase1",
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
        Clone vpn/ipsec/phase1 object.
        
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
            >>> fgt.api.cmdb.vpn_ipsec_phase1.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/vpn.ipsec/phase1",
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
        Check if vpn/ipsec/phase1 object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.vpn_ipsec_phase1.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase1.post(payload_dict=data)
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

