"""
FortiOS CMDB - Vpn ipsec phase2

Configuration endpoint for managing cmdb vpn/ipsec/phase2 objects.

API Endpoints:
    GET    /cmdb/vpn/ipsec/phase2
    POST   /cmdb/vpn/ipsec/phase2
    PUT    /cmdb/vpn/ipsec/phase2/{identifier}
    DELETE /cmdb/vpn/ipsec/phase2/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn_ipsec_phase2.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.vpn_ipsec_phase2.post(
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
)
# Import metadata mixin for schema introspection
from hfortix_fortios._helpers.metadata_mixin import MetadataMixin

# Import Protocol-based type hints (eliminates need for local @overload decorators)
from hfortix_fortios._protocols import CRUDEndpoint

class Phase2(CRUDEndpoint, MetadataMixin):
    """Phase2 Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "phase2"
    
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
        """Initialize Phase2 endpoint."""
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
        Retrieve vpn/ipsec/phase2 configuration.

        Configure VPN autokey tunnel.

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
            >>> # Get all vpn/ipsec/phase2 objects
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific vpn/ipsec/phase2 by name
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.get(name=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase2.get_schema()

        See Also:
            - post(): Create new vpn/ipsec/phase2 object
            - put(): Update existing vpn/ipsec/phase2 object
            - delete(): Remove vpn/ipsec/phase2 object
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
            endpoint = "/vpn.ipsec/phase2/" + str(name)
            unwrap_single = True
        else:
            endpoint = "/vpn.ipsec/phase2"
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
            >>> schema = fgt.api.cmdb.vpn_ipsec_phase2.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.vpn_ipsec_phase2.get_schema(format="json-schema")
        
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
        phase1name: str | None = None,
        dhcp_ipsec: Literal["enable", "disable"] | None = None,
        use_natip: Literal["enable", "disable"] | None = None,
        selector_match: Literal["exact", "subset", "auto"] | None = None,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = None,
        pfs: Literal["enable", "disable"] | None = None,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = None,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        replay: Literal["enable", "disable"] | None = None,
        keepalive: Literal["enable", "disable"] | None = None,
        auto_negotiate: Literal["enable", "disable"] | None = None,
        add_route: Literal["phase1", "enable", "disable"] | None = None,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: Literal["seconds", "kbs", "both"] | None = None,
        single_source: Literal["enable", "disable"] | None = None,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = None,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = None,
        l2tp: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        initiator_ts_narrow: Literal["enable", "disable"] | None = None,
        diffserv: Literal["enable", "disable"] | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: Any | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: Any | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing vpn/ipsec/phase2 object.

        Configure VPN autokey tunnel.

        Args:
            payload_dict: Object data as dict. Must include name (primary key).
            name: IPsec tunnel name.
            phase1name: Phase 1 determines the options required for phase 2.
            dhcp_ipsec: Enable/disable DHCP-IPsec.
            use_natip: Enable to use the FortiGate public IP as the source selector when outbound NAT is used.
            selector_match: Match type to use when comparing selectors.
            proposal: Phase2 proposal.
            pfs: Enable/disable PFS feature.
            dhgrp: Phase2 DH group.
            addke1: phase2 ADDKE1 group.
            addke2: phase2 ADDKE2 group.
            addke3: phase2 ADDKE3 group.
            addke4: phase2 ADDKE4 group.
            addke5: phase2 ADDKE5 group.
            addke6: phase2 ADDKE6 group.
            addke7: phase2 ADDKE7 group.
            replay: Enable/disable replay detection.
            keepalive: Enable/disable keep alive.
            auto_negotiate: Enable/disable IPsec SA auto-negotiation.
            add_route: Enable/disable automatic route addition.
            inbound_dscp_copy: Enable/disable copying of the DSCP in the ESP header to the inner IP header.
            keylifeseconds: Phase2 key life in time in seconds (120 - 172800).
            keylifekbs: Phase2 key life in number of kilobytes of traffic (5120 - 4294967295).
            keylife_type: Keylife type.
            single_source: Enable/disable single source IP restriction.
            route_overlap: Action for overlapping routes.
            encapsulation: ESP encapsulation mode.
            l2tp: Enable/disable L2TP over IPsec.
            comments: Comment.
            initiator_ts_narrow: Enable/disable traffic selector narrowing for IKEv2 initiator.
            diffserv: Enable/disable applying DSCP value to the IPsec tunnel outer IP header.
            diffservcode: DSCP value to be applied to the IPsec tunnel outer IP header.
            protocol: Quick mode protocol selector (1 - 255 or 0 for all).
            src_name: Local proxy ID name.
            src_name6: Local proxy ID name.
            src_addr_type: Local proxy ID type.
            src_start_ip: Local proxy ID start.
            src_start_ip6: Local proxy ID IPv6 start.
            src_end_ip: Local proxy ID end.
            src_end_ip6: Local proxy ID IPv6 end.
            src_subnet: Local proxy ID subnet.
            src_subnet6: Local proxy ID IPv6 subnet.
            src_port: Quick mode source port (1 - 65535 or 0 for all).
            dst_name: Remote proxy ID name.
            dst_name6: Remote proxy ID name.
            dst_addr_type: Remote proxy ID type.
            dst_start_ip: Remote proxy ID IPv4 start.
            dst_start_ip6: Remote proxy ID IPv6 start.
            dst_end_ip: Remote proxy ID IPv4 end.
            dst_end_ip6: Remote proxy ID IPv6 end.
            dst_subnet: Remote proxy ID IPv4 subnet.
            dst_subnet6: Remote proxy ID IPv6 subnet.
            dst_port: Quick mode destination port (1 - 65535 or 0 for all).
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.put(
            ...     name=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            phase1name=phase1name,
            dhcp_ipsec=dhcp_ipsec,
            use_natip=use_natip,
            selector_match=selector_match,
            proposal=proposal,
            pfs=pfs,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            replay=replay,
            keepalive=keepalive,
            auto_negotiate=auto_negotiate,
            add_route=add_route,
            inbound_dscp_copy=inbound_dscp_copy,
            keylifeseconds=keylifeseconds,
            keylifekbs=keylifekbs,
            keylife_type=keylife_type,
            single_source=single_source,
            route_overlap=route_overlap,
            encapsulation=encapsulation,
            l2tp=l2tp,
            comments=comments,
            initiator_ts_narrow=initiator_ts_narrow,
            diffserv=diffserv,
            diffservcode=diffservcode,
            protocol=protocol,
            src_name=src_name,
            src_name6=src_name6,
            src_addr_type=src_addr_type,
            src_start_ip=src_start_ip,
            src_start_ip6=src_start_ip6,
            src_end_ip=src_end_ip,
            src_end_ip6=src_end_ip6,
            src_subnet=src_subnet,
            src_subnet6=src_subnet6,
            src_port=src_port,
            dst_name=dst_name,
            dst_name6=dst_name6,
            dst_addr_type=dst_addr_type,
            dst_start_ip=dst_start_ip,
            dst_start_ip6=dst_start_ip6,
            dst_end_ip=dst_end_ip,
            dst_end_ip6=dst_end_ip6,
            dst_subnet=dst_subnet,
            dst_subnet6=dst_subnet6,
            dst_port=dst_port,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.phase2 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase2",
            )
        
        name_value = payload_data.get("name")
        if not name_value:
            raise ValueError("name is required for PUT")
        endpoint = "/vpn.ipsec/phase2/" + str(name_value)

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
        phase1name: str | None = None,
        dhcp_ipsec: Literal["enable", "disable"] | None = None,
        use_natip: Literal["enable", "disable"] | None = None,
        selector_match: Literal["exact", "subset", "auto"] | None = None,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | None = None,
        pfs: Literal["enable", "disable"] | None = None,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | None = None,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | None = None,
        replay: Literal["enable", "disable"] | None = None,
        keepalive: Literal["enable", "disable"] | None = None,
        auto_negotiate: Literal["enable", "disable"] | None = None,
        add_route: Literal["phase1", "enable", "disable"] | None = None,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: Literal["seconds", "kbs", "both"] | None = None,
        single_source: Literal["enable", "disable"] | None = None,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = None,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = None,
        l2tp: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        initiator_ts_narrow: Literal["enable", "disable"] | None = None,
        diffserv: Literal["enable", "disable"] | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: Any | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: Any | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new vpn/ipsec/phase2 object.

        Configure VPN autokey tunnel.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            name: IPsec tunnel name.
            phase1name: Phase 1 determines the options required for phase 2.
            dhcp_ipsec: Enable/disable DHCP-IPsec.
            use_natip: Enable to use the FortiGate public IP as the source selector when outbound NAT is used.
            selector_match: Match type to use when comparing selectors.
            proposal: Phase2 proposal.
            pfs: Enable/disable PFS feature.
            dhgrp: Phase2 DH group.
            addke1: phase2 ADDKE1 group.
            addke2: phase2 ADDKE2 group.
            addke3: phase2 ADDKE3 group.
            addke4: phase2 ADDKE4 group.
            addke5: phase2 ADDKE5 group.
            addke6: phase2 ADDKE6 group.
            addke7: phase2 ADDKE7 group.
            replay: Enable/disable replay detection.
            keepalive: Enable/disable keep alive.
            auto_negotiate: Enable/disable IPsec SA auto-negotiation.
            add_route: Enable/disable automatic route addition.
            inbound_dscp_copy: Enable/disable copying of the DSCP in the ESP header to the inner IP header.
            keylifeseconds: Phase2 key life in time in seconds (120 - 172800).
            keylifekbs: Phase2 key life in number of kilobytes of traffic (5120 - 4294967295).
            keylife_type: Keylife type.
            single_source: Enable/disable single source IP restriction.
            route_overlap: Action for overlapping routes.
            encapsulation: ESP encapsulation mode.
            l2tp: Enable/disable L2TP over IPsec.
            comments: Comment.
            initiator_ts_narrow: Enable/disable traffic selector narrowing for IKEv2 initiator.
            diffserv: Enable/disable applying DSCP value to the IPsec tunnel outer IP header.
            diffservcode: DSCP value to be applied to the IPsec tunnel outer IP header.
            protocol: Quick mode protocol selector (1 - 255 or 0 for all).
            src_name: Local proxy ID name.
            src_name6: Local proxy ID name.
            src_addr_type: Local proxy ID type.
            src_start_ip: Local proxy ID start.
            src_start_ip6: Local proxy ID IPv6 start.
            src_end_ip: Local proxy ID end.
            src_end_ip6: Local proxy ID IPv6 end.
            src_subnet: Local proxy ID subnet.
            src_subnet6: Local proxy ID IPv6 subnet.
            src_port: Quick mode source port (1 - 65535 or 0 for all).
            dst_name: Remote proxy ID name.
            dst_name6: Remote proxy ID name.
            dst_addr_type: Remote proxy ID type.
            dst_start_ip: Remote proxy ID IPv4 start.
            dst_start_ip6: Remote proxy ID IPv6 start.
            dst_end_ip: Remote proxy ID IPv4 end.
            dst_end_ip6: Remote proxy ID IPv6 end.
            dst_subnet: Remote proxy ID IPv4 subnet.
            dst_subnet6: Remote proxy ID IPv6 subnet.
            dst_port: Quick mode destination port (1 - 65535 or 0 for all).
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created name: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Phase2.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Phase2.required_fields()) }}
            
            Use Phase2.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            name=name,
            phase1name=phase1name,
            dhcp_ipsec=dhcp_ipsec,
            use_natip=use_natip,
            selector_match=selector_match,
            proposal=proposal,
            pfs=pfs,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            replay=replay,
            keepalive=keepalive,
            auto_negotiate=auto_negotiate,
            add_route=add_route,
            inbound_dscp_copy=inbound_dscp_copy,
            keylifeseconds=keylifeseconds,
            keylifekbs=keylifekbs,
            keylife_type=keylife_type,
            single_source=single_source,
            route_overlap=route_overlap,
            encapsulation=encapsulation,
            l2tp=l2tp,
            comments=comments,
            initiator_ts_narrow=initiator_ts_narrow,
            diffserv=diffserv,
            diffservcode=diffservcode,
            protocol=protocol,
            src_name=src_name,
            src_name6=src_name6,
            src_addr_type=src_addr_type,
            src_start_ip=src_start_ip,
            src_start_ip6=src_start_ip6,
            src_end_ip=src_end_ip,
            src_end_ip6=src_end_ip6,
            src_subnet=src_subnet,
            src_subnet6=src_subnet6,
            src_port=src_port,
            dst_name=dst_name,
            dst_name6=dst_name6,
            dst_addr_type=dst_addr_type,
            dst_start_ip=dst_start_ip,
            dst_start_ip6=dst_start_ip6,
            dst_end_ip=dst_end_ip,
            dst_end_ip6=dst_end_ip6,
            dst_subnet=dst_subnet,
            dst_subnet6=dst_subnet6,
            dst_port=dst_port,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.phase2 import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/vpn/ipsec/phase2",
            )

        endpoint = "/vpn.ipsec/phase2"
        
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
        Delete vpn/ipsec/phase2 object.

        Configure VPN autokey tunnel.

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
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.delete(name=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not name:
            raise ValueError("name is required for DELETE")
        endpoint = "/vpn.ipsec/phase2/" + str(name)

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
        Check if vpn/ipsec/phase2 object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            name: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.vpn_ipsec_phase2.exists(name=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.vpn_ipsec_phase2.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase2.delete(name=1)

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
        phase1name: str | None = None,
        dhcp_ipsec: Literal["enable", "disable"] | None = None,
        use_natip: Literal["enable", "disable"] | None = None,
        selector_match: Literal["exact", "subset", "auto"] | None = None,
        proposal: Literal["null-md5", "null-sha1", "null-sha256", "null-sha384", "null-sha512", "des-null", "des-md5", "des-sha1", "des-sha256", "des-sha384", "des-sha512", "3des-null", "3des-md5", "3des-sha1", "3des-sha256", "3des-sha384", "3des-sha512", "aes128-null", "aes128-md5", "aes128-sha1", "aes128-sha256", "aes128-sha384", "aes128-sha512", "aes128gcm", "aes192-null", "aes192-md5", "aes192-sha1", "aes192-sha256", "aes192-sha384", "aes192-sha512", "aes256-null", "aes256-md5", "aes256-sha1", "aes256-sha256", "aes256-sha384", "aes256-sha512", "aes256gcm", "chacha20poly1305", "aria128-null", "aria128-md5", "aria128-sha1", "aria128-sha256", "aria128-sha384", "aria128-sha512", "aria192-null", "aria192-md5", "aria192-sha1", "aria192-sha256", "aria192-sha384", "aria192-sha512", "aria256-null", "aria256-md5", "aria256-sha1", "aria256-sha256", "aria256-sha384", "aria256-sha512", "seed-null", "seed-md5", "seed-sha1", "seed-sha256", "seed-sha384", "seed-sha512"] | list[str] | list[dict[str, Any]] | None = None,
        pfs: Literal["enable", "disable"] | None = None,
        dhgrp: Literal["1", "2", "5", "14", "15", "16", "17", "18", "19", "20", "21", "27", "28", "29", "30", "31", "32"] | list[str] | list[dict[str, Any]] | None = None,
        addke1: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke2: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke3: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke4: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke5: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke6: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        addke7: Literal["0", "35", "36", "37", "1080", "1081", "1082", "1083", "1084", "1085", "1089", "1090", "1091", "1092", "1093", "1094"] | list[str] | list[dict[str, Any]] | None = None,
        replay: Literal["enable", "disable"] | None = None,
        keepalive: Literal["enable", "disable"] | None = None,
        auto_negotiate: Literal["enable", "disable"] | None = None,
        add_route: Literal["phase1", "enable", "disable"] | None = None,
        inbound_dscp_copy: Literal["phase1", "enable", "disable"] | None = None,
        keylifeseconds: int | None = None,
        keylifekbs: int | None = None,
        keylife_type: Literal["seconds", "kbs", "both"] | None = None,
        single_source: Literal["enable", "disable"] | None = None,
        route_overlap: Literal["use-old", "use-new", "allow"] | None = None,
        encapsulation: Literal["tunnel-mode", "transport-mode"] | None = None,
        l2tp: Literal["enable", "disable"] | None = None,
        comments: str | None = None,
        initiator_ts_narrow: Literal["enable", "disable"] | None = None,
        diffserv: Literal["enable", "disable"] | None = None,
        diffservcode: str | None = None,
        protocol: int | None = None,
        src_name: str | None = None,
        src_name6: str | None = None,
        src_addr_type: Literal["subnet", "range", "ip", "name"] | None = None,
        src_start_ip: str | None = None,
        src_start_ip6: str | None = None,
        src_end_ip: str | None = None,
        src_end_ip6: str | None = None,
        src_subnet: Any | None = None,
        src_subnet6: str | None = None,
        src_port: int | None = None,
        dst_name: str | None = None,
        dst_name6: str | None = None,
        dst_addr_type: Literal["subnet", "range", "ip", "name"] | None = None,
        dst_start_ip: str | None = None,
        dst_start_ip6: str | None = None,
        dst_end_ip: str | None = None,
        dst_end_ip6: str | None = None,
        dst_subnet: Any | None = None,
        dst_subnet6: str | None = None,
        dst_port: int | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update vpn/ipsec/phase2 object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (name) in the payload.

        Args:
            payload_dict: Resource data including name (primary key)
            name: Field name
            phase1name: Field phase1name
            dhcp_ipsec: Field dhcp-ipsec
            use_natip: Field use-natip
            selector_match: Field selector-match
            proposal: Field proposal
            pfs: Field pfs
            dhgrp: Field dhgrp
            addke1: Field addke1
            addke2: Field addke2
            addke3: Field addke3
            addke4: Field addke4
            addke5: Field addke5
            addke6: Field addke6
            addke7: Field addke7
            replay: Field replay
            keepalive: Field keepalive
            auto_negotiate: Field auto-negotiate
            add_route: Field add-route
            inbound_dscp_copy: Field inbound-dscp-copy
            keylifeseconds: Field keylifeseconds
            keylifekbs: Field keylifekbs
            keylife_type: Field keylife-type
            single_source: Field single-source
            route_overlap: Field route-overlap
            encapsulation: Field encapsulation
            l2tp: Field l2tp
            comments: Field comments
            initiator_ts_narrow: Field initiator-ts-narrow
            diffserv: Field diffserv
            diffservcode: Field diffservcode
            protocol: Field protocol
            src_name: Field src-name
            src_name6: Field src-name6
            src_addr_type: Field src-addr-type
            src_start_ip: Field src-start-ip
            src_start_ip6: Field src-start-ip6
            src_end_ip: Field src-end-ip
            src_end_ip6: Field src-end-ip6
            src_subnet: Field src-subnet
            src_subnet6: Field src-subnet6
            src_port: Field src-port
            dst_name: Field dst-name
            dst_name6: Field dst-name6
            dst_addr_type: Field dst-addr-type
            dst_start_ip: Field dst-start-ip
            dst_start_ip6: Field dst-start-ip6
            dst_end_ip: Field dst-end-ip
            dst_end_ip6: Field dst-end-ip6
            dst_subnet: Field dst-subnet
            dst_subnet6: Field dst-subnet6
            dst_port: Field dst-port
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If name is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.set(
            ...     name=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "name": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.vpn_ipsec_phase2.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.vpn_ipsec_phase2.set(payload_dict=obj_data)
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
            phase1name=phase1name,
            dhcp_ipsec=dhcp_ipsec,
            use_natip=use_natip,
            selector_match=selector_match,
            proposal=proposal,
            pfs=pfs,
            dhgrp=dhgrp,
            addke1=addke1,
            addke2=addke2,
            addke3=addke3,
            addke4=addke4,
            addke5=addke5,
            addke6=addke6,
            addke7=addke7,
            replay=replay,
            keepalive=keepalive,
            auto_negotiate=auto_negotiate,
            add_route=add_route,
            inbound_dscp_copy=inbound_dscp_copy,
            keylifeseconds=keylifeseconds,
            keylifekbs=keylifekbs,
            keylife_type=keylife_type,
            single_source=single_source,
            route_overlap=route_overlap,
            encapsulation=encapsulation,
            l2tp=l2tp,
            comments=comments,
            initiator_ts_narrow=initiator_ts_narrow,
            diffserv=diffserv,
            diffservcode=diffservcode,
            protocol=protocol,
            src_name=src_name,
            src_name6=src_name6,
            src_addr_type=src_addr_type,
            src_start_ip=src_start_ip,
            src_start_ip6=src_start_ip6,
            src_end_ip=src_end_ip,
            src_end_ip6=src_end_ip6,
            src_subnet=src_subnet,
            src_subnet6=src_subnet6,
            src_port=src_port,
            dst_name=dst_name,
            dst_name6=dst_name6,
            dst_addr_type=dst_addr_type,
            dst_start_ip=dst_start_ip,
            dst_start_ip6=dst_start_ip6,
            dst_end_ip=dst_end_ip,
            dst_end_ip6=dst_end_ip6,
            dst_subnet=dst_subnet,
            dst_subnet6=dst_subnet6,
            dst_port=dst_port,
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
        Move vpn/ipsec/phase2 object to a new position.
        
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
            >>> fgt.api.cmdb.vpn_ipsec_phase2.move(
            ...     name=100,
            ...     action="before",
            ...     reference_name=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/vpn.ipsec/phase2",
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
        Clone vpn/ipsec/phase2 object.
        
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
            >>> fgt.api.cmdb.vpn_ipsec_phase2.clone(
            ...     name=1,
            ...     new_name=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/vpn.ipsec/phase2",
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
        Check if vpn/ipsec/phase2 object exists.
        
        Args:
            name: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.vpn_ipsec_phase2.exists(name=1):
            ...     fgt.api.cmdb.vpn_ipsec_phase2.post(payload_dict=data)
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

