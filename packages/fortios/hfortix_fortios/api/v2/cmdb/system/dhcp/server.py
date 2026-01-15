"""
FortiOS CMDB - System dhcp server

Configuration endpoint for managing cmdb system/dhcp/server objects.

API Endpoints:
    GET    /cmdb/system/dhcp/server
    POST   /cmdb/system/dhcp/server
    PUT    /cmdb/system/dhcp/server/{identifier}
    DELETE /cmdb/system/dhcp/server/{identifier}

Example Usage:
    >>> from hfortix_fortios import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system_dhcp_server.get()
    >>>
    >>> # Create with auto-normalization (strings/lists converted automatically)
    >>> result = fgt.api.cmdb.system_dhcp_server.post(
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

class Server(CRUDEndpoint, MetadataMixin):
    """Server Operations."""
    
    # Configure metadata mixin to use this endpoint's helper module
    _helper_module_name = "server"
    
    # ========================================================================
    # Table Fields Metadata (for normalization)
    # Auto-generated from schema - supports flexible input formats
    # ========================================================================
    _TABLE_FIELDS = {
        "ip_range": {
            "mkey": "id",
            "required_fields": ['id', 'start-ip', 'end-ip'],
            "example": "[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
        },
        "tftp_server": {
            "mkey": "tftp-server",
            "required_fields": ['tftp-server'],
            "example": "[{'tftp-server': 'value'}]",
        },
        "options": {
            "mkey": "id",
            "required_fields": ['id', 'code'],
            "example": "[{'id': 1, 'code': 1}]",
        },
        "vci_string": {
            "mkey": "vci-string",
            "required_fields": ['vci-string'],
            "example": "[{'vci-string': 'value'}]",
        },
        "exclude_range": {
            "mkey": "id",
            "required_fields": ['id', 'start-ip', 'end-ip'],
            "example": "[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
        },
        "reserved_address": {
            "mkey": "id",
            "required_fields": ['id', 'ip', 'mac'],
            "example": "[{'id': 1, 'ip': '192.168.1.10', 'mac': 'value'}]",
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
        """Initialize Server endpoint."""
        self._client = client

    # ========================================================================
    # GET Method
    # Type hints provided by CRUDEndpoint protocol (no local @overload needed)
    # ========================================================================
    
    def get(
        self,
        id: int | None = None,
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
        Retrieve system/dhcp/server configuration.

        Configure DHCP servers.

        Args:
            id: Integer identifier to retrieve specific object.
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
            >>> # Get all system/dhcp/server objects
            >>> result = fgt.api.cmdb.system_dhcp_server.get()
            >>> print(f"Found {len(result['results'])} objects")
            
            >>> # Get specific system/dhcp/server by id
            >>> result = fgt.api.cmdb.system_dhcp_server.get(id=1)
            >>> print(result['results'])
            
            >>> # Get with filter
            >>> result = fgt.api.cmdb.system_dhcp_server.get(
            ...     filter=["name==test", "status==enable"]
            ... )
            
            >>> # Get with pagination
            >>> result = fgt.api.cmdb.system_dhcp_server.get(
            ...     start=0, count=100
            ... )
            
            >>> # Get schema information  
            >>> schema = fgt.api.cmdb.system_dhcp_server.get_schema()

        See Also:
            - post(): Create new system/dhcp/server object
            - put(): Update existing system/dhcp/server object
            - delete(): Remove system/dhcp/server object
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
        
        if id:
            endpoint = "/system.dhcp/server/" + str(id)
            unwrap_single = True
        else:
            endpoint = "/system.dhcp/server"
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
            >>> schema = fgt.api.cmdb.system_dhcp_server.get_schema()
            >>> print(schema['results'])
            
            >>> # Get JSON Schema format (if supported)
            >>> json_schema = fgt.api.cmdb.system_dhcp_server.get_schema(format="json-schema")
        
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
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        lease_time: int | None = None,
        mac_acl_default_action: Literal["assign", "block"] | None = None,
        forticlient_on_net_status: Literal["disable", "enable"] | None = None,
        dns_service: Literal["local", "default", "specify"] | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        wifi_ac_service: Literal["specify", "local"] | None = None,
        wifi_ac1: str | None = None,
        wifi_ac2: str | None = None,
        wifi_ac3: str | None = None,
        ntp_service: Literal["local", "default", "specify"] | None = None,
        ntp_server1: str | None = None,
        ntp_server2: str | None = None,
        ntp_server3: str | None = None,
        domain: str | None = None,
        wins_server1: str | None = None,
        wins_server2: str | None = None,
        default_gateway: str | None = None,
        next_server: str | None = None,
        netmask: str | None = None,
        interface: str | None = None,
        ip_range: str | list[str] | list[dict[str, Any]] | None = None,
        timezone_option: Literal["disable", "default", "specify"] | None = None,
        timezone: str | None = None,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = None,
        filename: str | None = None,
        options: str | list[str] | list[dict[str, Any]] | None = None,
        server_type: Literal["regular", "ipsec"] | None = None,
        ip_mode: Literal["range", "usrgrp"] | None = None,
        conflicted_ip_timeout: int | None = None,
        ipsec_lease_hold: int | None = None,
        auto_configuration: Literal["disable", "enable"] | None = None,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = None,
        auto_managed_status: Literal["disable", "enable"] | None = None,
        ddns_update: Literal["disable", "enable"] | None = None,
        ddns_update_override: Literal["disable", "enable"] | None = None,
        ddns_server_ip: str | None = None,
        ddns_zone: str | None = None,
        ddns_auth: Literal["disable", "tsig"] | None = None,
        ddns_keyname: str | None = None,
        ddns_key: Any | None = None,
        ddns_ttl: int | None = None,
        vci_match: Literal["disable", "enable"] | None = None,
        vci_string: str | list[str] | list[dict[str, Any]] | None = None,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        shared_subnet: Literal["disable", "enable"] | None = None,
        relay_agent: str | None = None,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["move"] | None = None,
        q_before: str | None = None,
        q_after: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Update existing system/dhcp/server object.

        Configure DHCP servers.

        Args:
            payload_dict: Object data as dict. Must include id (primary key).
            id: ID.
            status: Enable/disable this DHCP configuration.
            lease_time: Lease time in seconds, 0 means unlimited.
            mac_acl_default_action: MAC access control default action (allow or block assigning IP settings).
            forticlient_on_net_status: Enable/disable FortiClient-On-Net service for this DHCP server.
            dns_service: Options for assigning DNS servers to DHCP clients.
            dns_server1: DNS server 1.
            dns_server2: DNS server 2.
            dns_server3: DNS server 3.
            dns_server4: DNS server 4.
            wifi_ac_service: Options for assigning WiFi access controllers to DHCP clients.
            wifi_ac1: WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).
            wifi_ac2: WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).
            wifi_ac3: WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).
            ntp_service: Options for assigning Network Time Protocol (NTP) servers to DHCP clients.
            ntp_server1: NTP server 1.
            ntp_server2: NTP server 2.
            ntp_server3: NTP server 3.
            domain: Domain name suffix for the IP addresses that the DHCP server assigns to clients.
            wins_server1: WINS server 1.
            wins_server2: WINS server 2.
            default_gateway: Default gateway IP address assigned by the DHCP server.
            next_server: IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.
            netmask: Netmask assigned by the DHCP server.
            interface: DHCP server can assign IP configurations to clients connected to this interface.
            ip_range: DHCP IP range configuration.
                Default format: [{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]
                Required format: List of dicts with keys: id, start-ip, end-ip
                  (String format not allowed due to multiple required fields)
            timezone_option: Options for the DHCP server to set the client's time zone.
            timezone: Select the time zone to be assigned to DHCP clients.
            tftp_server: One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces.
                Default format: [{'tftp-server': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'tftp-server': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'tftp-server': 'val1'}, ...]
                  - List of dicts: [{'tftp-server': 'value'}] (recommended)
            filename: Name of the boot file on the TFTP server.
            options: DHCP options.
                Default format: [{'id': 1, 'code': 1}]
                Required format: List of dicts with keys: id, code
                  (String format not allowed due to multiple required fields)
            server_type: DHCP server can be a normal DHCP server or an IPsec DHCP server.
            ip_mode: Method used to assign client IP.
            conflicted_ip_timeout: Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.
            ipsec_lease_hold: DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).
            auto_configuration: Enable/disable auto configuration.
            dhcp_settings_from_fortiipam: Enable/disable populating of DHCP server settings from FortiIPAM.
            auto_managed_status: Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM.
            ddns_update: Enable/disable DDNS update for DHCP.
            ddns_update_override: Enable/disable DDNS update override for DHCP.
            ddns_server_ip: DDNS server IP.
            ddns_zone: Zone of your domain name (ex. DDNS.com).
            ddns_auth: DDNS authentication mode.
            ddns_keyname: DDNS update key name.
            ddns_key: DDNS update key (base 64 encoding).
            ddns_ttl: TTL.
            vci_match: Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.
            vci_string: One or more VCI strings in quotes separated by spaces.
                Default format: [{'vci-string': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'vci-string': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'vci-string': 'val1'}, ...]
                  - List of dicts: [{'vci-string': 'value'}] (recommended)
            exclude_range: Exclude one or more ranges of IP addresses from being assigned to clients.
                Default format: [{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]
                Required format: List of dicts with keys: id, start-ip, end-ip
                  (String format not allowed due to multiple required fields)
            shared_subnet: Enable/disable shared subnet.
            relay_agent: Relay agent IP.
            reserved_address: Options for the DHCP server to assign IP settings to specific MAC addresses.
                Default format: [{'id': 1, 'ip': '192.168.1.10', 'mac': 'value'}]
                Required format: List of dicts with keys: id, ip, mac
                  (String format not allowed due to multiple required fields)
            vdom: Virtual domain name.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary.

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Update specific fields
            >>> result = fgt.api.cmdb.system_dhcp_server.put(
            ...     id=1,
            ...     # ... fields to update
            ... )
            
            >>> # Update using payload dict
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "new-value",
            ... }
            >>> result = fgt.api.cmdb.system_dhcp_server.put(payload_dict=payload)

        See Also:
            - post(): Create new object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if ip_range is not None:
            ip_range = normalize_table_field(
                ip_range,
                mkey="id",
                required_fields=['id', 'start-ip', 'end-ip'],
                field_name="ip_range",
                example="[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
            )
        if tftp_server is not None:
            tftp_server = normalize_table_field(
                tftp_server,
                mkey="tftp-server",
                required_fields=['tftp-server'],
                field_name="tftp_server",
                example="[{'tftp-server': 'value'}]",
            )
        if options is not None:
            options = normalize_table_field(
                options,
                mkey="id",
                required_fields=['id', 'code'],
                field_name="options",
                example="[{'id': 1, 'code': 1}]",
            )
        if vci_string is not None:
            vci_string = normalize_table_field(
                vci_string,
                mkey="vci-string",
                required_fields=['vci-string'],
                field_name="vci_string",
                example="[{'vci-string': 'value'}]",
            )
        if exclude_range is not None:
            exclude_range = normalize_table_field(
                exclude_range,
                mkey="id",
                required_fields=['id', 'start-ip', 'end-ip'],
                field_name="exclude_range",
                example="[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
            )
        if reserved_address is not None:
            reserved_address = normalize_table_field(
                reserved_address,
                mkey="id",
                required_fields=['id', 'ip', 'mac'],
                field_name="reserved_address",
                example="[{'id': 1, 'ip': '192.168.1.10', 'mac': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            id=id,
            status=status,
            lease_time=lease_time,
            mac_acl_default_action=mac_acl_default_action,
            forticlient_on_net_status=forticlient_on_net_status,
            dns_service=dns_service,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            wifi_ac_service=wifi_ac_service,
            wifi_ac1=wifi_ac1,
            wifi_ac2=wifi_ac2,
            wifi_ac3=wifi_ac3,
            ntp_service=ntp_service,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            ntp_server3=ntp_server3,
            domain=domain,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            default_gateway=default_gateway,
            next_server=next_server,
            netmask=netmask,
            interface=interface,
            ip_range=ip_range,
            timezone_option=timezone_option,
            timezone=timezone,
            tftp_server=tftp_server,
            filename=filename,
            options=options,
            server_type=server_type,
            ip_mode=ip_mode,
            conflicted_ip_timeout=conflicted_ip_timeout,
            ipsec_lease_hold=ipsec_lease_hold,
            auto_configuration=auto_configuration,
            dhcp_settings_from_fortiipam=dhcp_settings_from_fortiipam,
            auto_managed_status=auto_managed_status,
            ddns_update=ddns_update,
            ddns_update_override=ddns_update_override,
            ddns_server_ip=ddns_server_ip,
            ddns_zone=ddns_zone,
            ddns_auth=ddns_auth,
            ddns_keyname=ddns_keyname,
            ddns_key=ddns_key,
            ddns_ttl=ddns_ttl,
            vci_match=vci_match,
            vci_string=vci_string,
            exclude_range=exclude_range,
            shared_subnet=shared_subnet,
            relay_agent=relay_agent,
            reserved_address=reserved_address,
            data=payload_dict,
        )
        
        # Check for deprecated fields and warn users
        from ._helpers.server import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/dhcp/server",
            )
        
        id_value = payload_data.get("id")
        if not id_value:
            raise ValueError("id is required for PUT")
        endpoint = "/system.dhcp/server/" + str(id_value)

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
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        lease_time: int | None = None,
        mac_acl_default_action: Literal["assign", "block"] | None = None,
        forticlient_on_net_status: Literal["disable", "enable"] | None = None,
        dns_service: Literal["local", "default", "specify"] | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        wifi_ac_service: Literal["specify", "local"] | None = None,
        wifi_ac1: str | None = None,
        wifi_ac2: str | None = None,
        wifi_ac3: str | None = None,
        ntp_service: Literal["local", "default", "specify"] | None = None,
        ntp_server1: str | None = None,
        ntp_server2: str | None = None,
        ntp_server3: str | None = None,
        domain: str | None = None,
        wins_server1: str | None = None,
        wins_server2: str | None = None,
        default_gateway: str | None = None,
        next_server: str | None = None,
        netmask: str | None = None,
        interface: str | None = None,
        ip_range: str | list[str] | list[dict[str, Any]] | None = None,
        timezone_option: Literal["disable", "default", "specify"] | None = None,
        timezone: str | None = None,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = None,
        filename: str | None = None,
        options: str | list[str] | list[dict[str, Any]] | None = None,
        server_type: Literal["regular", "ipsec"] | None = None,
        ip_mode: Literal["range", "usrgrp"] | None = None,
        conflicted_ip_timeout: int | None = None,
        ipsec_lease_hold: int | None = None,
        auto_configuration: Literal["disable", "enable"] | None = None,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = None,
        auto_managed_status: Literal["disable", "enable"] | None = None,
        ddns_update: Literal["disable", "enable"] | None = None,
        ddns_update_override: Literal["disable", "enable"] | None = None,
        ddns_server_ip: str | None = None,
        ddns_zone: str | None = None,
        ddns_auth: Literal["disable", "tsig"] | None = None,
        ddns_keyname: str | None = None,
        ddns_key: Any | None = None,
        ddns_ttl: int | None = None,
        vci_match: Literal["disable", "enable"] | None = None,
        vci_string: str | list[str] | list[dict[str, Any]] | None = None,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        shared_subnet: Literal["disable", "enable"] | None = None,
        relay_agent: str | None = None,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = None,
        q_action: Literal["clone"] | None = None,
        q_nkey: str | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Create new system/dhcp/server object.

        Configure DHCP servers.

        Args:
            payload_dict: Complete object data as dict. Alternative to individual parameters.
            id: ID.
            status: Enable/disable this DHCP configuration.
            lease_time: Lease time in seconds, 0 means unlimited.
            mac_acl_default_action: MAC access control default action (allow or block assigning IP settings).
            forticlient_on_net_status: Enable/disable FortiClient-On-Net service for this DHCP server.
            dns_service: Options for assigning DNS servers to DHCP clients.
            dns_server1: DNS server 1.
            dns_server2: DNS server 2.
            dns_server3: DNS server 3.
            dns_server4: DNS server 4.
            wifi_ac_service: Options for assigning WiFi access controllers to DHCP clients.
            wifi_ac1: WiFi Access Controller 1 IP address (DHCP option 138, RFC 5417).
            wifi_ac2: WiFi Access Controller 2 IP address (DHCP option 138, RFC 5417).
            wifi_ac3: WiFi Access Controller 3 IP address (DHCP option 138, RFC 5417).
            ntp_service: Options for assigning Network Time Protocol (NTP) servers to DHCP clients.
            ntp_server1: NTP server 1.
            ntp_server2: NTP server 2.
            ntp_server3: NTP server 3.
            domain: Domain name suffix for the IP addresses that the DHCP server assigns to clients.
            wins_server1: WINS server 1.
            wins_server2: WINS server 2.
            default_gateway: Default gateway IP address assigned by the DHCP server.
            next_server: IP address of a server (for example, a TFTP sever) that DHCP clients can download a boot file from.
            netmask: Netmask assigned by the DHCP server.
            interface: DHCP server can assign IP configurations to clients connected to this interface.
            ip_range: DHCP IP range configuration.
                Default format: [{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]
                Required format: List of dicts with keys: id, start-ip, end-ip
                  (String format not allowed due to multiple required fields)
            timezone_option: Options for the DHCP server to set the client's time zone.
            timezone: Select the time zone to be assigned to DHCP clients.
            tftp_server: One or more hostnames or IP addresses of the TFTP servers in quotes separated by spaces.
                Default format: [{'tftp-server': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'tftp-server': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'tftp-server': 'val1'}, ...]
                  - List of dicts: [{'tftp-server': 'value'}] (recommended)
            filename: Name of the boot file on the TFTP server.
            options: DHCP options.
                Default format: [{'id': 1, 'code': 1}]
                Required format: List of dicts with keys: id, code
                  (String format not allowed due to multiple required fields)
            server_type: DHCP server can be a normal DHCP server or an IPsec DHCP server.
            ip_mode: Method used to assign client IP.
            conflicted_ip_timeout: Time in seconds to wait after a conflicted IP address is removed from the DHCP range before it can be reused.
            ipsec_lease_hold: DHCP over IPsec leases expire this many seconds after tunnel down (0 to disable forced-expiry).
            auto_configuration: Enable/disable auto configuration.
            dhcp_settings_from_fortiipam: Enable/disable populating of DHCP server settings from FortiIPAM.
            auto_managed_status: Enable/disable use of this DHCP server once this interface has been assigned an IP address from FortiIPAM.
            ddns_update: Enable/disable DDNS update for DHCP.
            ddns_update_override: Enable/disable DDNS update override for DHCP.
            ddns_server_ip: DDNS server IP.
            ddns_zone: Zone of your domain name (ex. DDNS.com).
            ddns_auth: DDNS authentication mode.
            ddns_keyname: DDNS update key name.
            ddns_key: DDNS update key (base 64 encoding).
            ddns_ttl: TTL.
            vci_match: Enable/disable vendor class identifier (VCI) matching. When enabled only DHCP requests with a matching VCI are served.
            vci_string: One or more VCI strings in quotes separated by spaces.
                Default format: [{'vci-string': 'value'}]
                Supported formats:
                  - Single string: "value" → [{'vci-string': 'value'}]
                  - List of strings: ["val1", "val2"] → [{'vci-string': 'val1'}, ...]
                  - List of dicts: [{'vci-string': 'value'}] (recommended)
            exclude_range: Exclude one or more ranges of IP addresses from being assigned to clients.
                Default format: [{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]
                Required format: List of dicts with keys: id, start-ip, end-ip
                  (String format not allowed due to multiple required fields)
            shared_subnet: Enable/disable shared subnet.
            relay_agent: Relay agent IP.
            reserved_address: Options for the DHCP server to assign IP settings to specific MAC addresses.
                Default format: [{'id': 1, 'ip': '192.168.1.10', 'mac': 'value'}]
                Required format: List of dicts with keys: id, ip, mac
                  (String format not allowed due to multiple required fields)
            vdom: Virtual domain name. Use True for global, string for specific VDOM.
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance with created object. Use .dict, .json, or .raw to access as dictionary.

        Examples:
            >>> # Create using individual parameters
            >>> result = fgt.api.cmdb.system_dhcp_server.post(
            ...     name="example",
            ...     # ... other required fields
            ... )
            >>> print(f"Created id: {result['results']}")
            
            >>> # Create using payload dict
            >>> payload = Server.defaults()  # Start with defaults
            >>> payload['name'] = 'my-object'
            >>> result = fgt.api.cmdb.system_dhcp_server.post(payload_dict=payload)

        Note:
            Required fields: {{ ", ".join(Server.required_fields()) }}
            
            Use Server.help('field_name') to get field details.

        See Also:
            - get(): Retrieve objects
            - put(): Update existing object
            - set(): Intelligent create or update
        """
        # Apply normalization for table fields (supports flexible input formats)
        if ip_range is not None:
            ip_range = normalize_table_field(
                ip_range,
                mkey="id",
                required_fields=['id', 'start-ip', 'end-ip'],
                field_name="ip_range",
                example="[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
            )
        if tftp_server is not None:
            tftp_server = normalize_table_field(
                tftp_server,
                mkey="tftp-server",
                required_fields=['tftp-server'],
                field_name="tftp_server",
                example="[{'tftp-server': 'value'}]",
            )
        if options is not None:
            options = normalize_table_field(
                options,
                mkey="id",
                required_fields=['id', 'code'],
                field_name="options",
                example="[{'id': 1, 'code': 1}]",
            )
        if vci_string is not None:
            vci_string = normalize_table_field(
                vci_string,
                mkey="vci-string",
                required_fields=['vci-string'],
                field_name="vci_string",
                example="[{'vci-string': 'value'}]",
            )
        if exclude_range is not None:
            exclude_range = normalize_table_field(
                exclude_range,
                mkey="id",
                required_fields=['id', 'start-ip', 'end-ip'],
                field_name="exclude_range",
                example="[{'id': 1, 'start-ip': '192.168.1.10', 'end-ip': '192.168.1.10'}]",
            )
        if reserved_address is not None:
            reserved_address = normalize_table_field(
                reserved_address,
                mkey="id",
                required_fields=['id', 'ip', 'mac'],
                field_name="reserved_address",
                example="[{'id': 1, 'ip': '192.168.1.10', 'mac': 'value'}]",
            )
        
        # Build payload using helper function with auto-normalization
        # This automatically converts strings/lists to [{'name': '...'}] format for list fields
        # To disable auto-normalization, use build_cmdb_payload directly
        payload_data = build_api_payload(
            id=id,
            status=status,
            lease_time=lease_time,
            mac_acl_default_action=mac_acl_default_action,
            forticlient_on_net_status=forticlient_on_net_status,
            dns_service=dns_service,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            wifi_ac_service=wifi_ac_service,
            wifi_ac1=wifi_ac1,
            wifi_ac2=wifi_ac2,
            wifi_ac3=wifi_ac3,
            ntp_service=ntp_service,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            ntp_server3=ntp_server3,
            domain=domain,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            default_gateway=default_gateway,
            next_server=next_server,
            netmask=netmask,
            interface=interface,
            ip_range=ip_range,
            timezone_option=timezone_option,
            timezone=timezone,
            tftp_server=tftp_server,
            filename=filename,
            options=options,
            server_type=server_type,
            ip_mode=ip_mode,
            conflicted_ip_timeout=conflicted_ip_timeout,
            ipsec_lease_hold=ipsec_lease_hold,
            auto_configuration=auto_configuration,
            dhcp_settings_from_fortiipam=dhcp_settings_from_fortiipam,
            auto_managed_status=auto_managed_status,
            ddns_update=ddns_update,
            ddns_update_override=ddns_update_override,
            ddns_server_ip=ddns_server_ip,
            ddns_zone=ddns_zone,
            ddns_auth=ddns_auth,
            ddns_keyname=ddns_keyname,
            ddns_key=ddns_key,
            ddns_ttl=ddns_ttl,
            vci_match=vci_match,
            vci_string=vci_string,
            exclude_range=exclude_range,
            shared_subnet=shared_subnet,
            relay_agent=relay_agent,
            reserved_address=reserved_address,
            data=payload_dict,
        )

        # Check for deprecated fields and warn users
        from ._helpers.server import DEPRECATED_FIELDS
        if DEPRECATED_FIELDS:
            from hfortix_core import check_deprecated_fields
            check_deprecated_fields(
                payload=payload_data,
                deprecated_fields=DEPRECATED_FIELDS,
                endpoint="cmdb/system/dhcp/server",
            )

        endpoint = "/system.dhcp/server"
        
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
        id: int | None = None,
        q_scope: str | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
    ):  # type: ignore[no-untyped-def]
        """
        Delete system/dhcp/server object.

        Configure DHCP servers.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name
            error_mode: Override client-level error_mode. "raise" raises exceptions, "return" returns error dict, "print" prints errors.
            error_format: Override client-level error_format. "detailed" provides full context, "simple" is concise, "code_only" returns just status code.

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If id is not provided

        Examples:
            >>> # Delete specific object
            >>> result = fgt.api.cmdb.system_dhcp_server.delete(id=1)
            
            >>> # Check for errors
            >>> if result.get('status') != 'success':
            ...     print(f"Delete failed: {result.get('error')}")

        See Also:
            - exists(): Check if object exists before deleting
            - get(): Retrieve object to verify it exists
        """
        if not id:
            raise ValueError("id is required for DELETE")
        endpoint = "/system.dhcp/server/" + str(id)

        # Add explicit query parameters for DELETE
        params: dict[str, Any] = {}
        if q_scope is not None:
            params["scope"] = q_scope
        
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom
        )

    def exists(
        self,
        id: int,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if system/dhcp/server object exists.

        Verifies whether an object exists by attempting to retrieve it and checking the response status.

        Args:
            id: Primary key identifier
            vdom: Virtual domain name

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if object exists before operations
            >>> if fgt.api.cmdb.system_dhcp_server.exists(id=1):
            ...     print("Object exists")
            ... else:
            ...     print("Object not found")
            
            >>> # Conditional delete
            >>> if fgt.api.cmdb.system_dhcp_server.exists(id=1):
            ...     fgt.api.cmdb.system_dhcp_server.delete(id=1)

        See Also:
            - get(): Retrieve full object data
            - set(): Create or update automatically based on existence
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                id=id,
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
        id: int | None = None,
        status: Literal["disable", "enable"] | None = None,
        lease_time: int | None = None,
        mac_acl_default_action: Literal["assign", "block"] | None = None,
        forticlient_on_net_status: Literal["disable", "enable"] | None = None,
        dns_service: Literal["local", "default", "specify"] | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        wifi_ac_service: Literal["specify", "local"] | None = None,
        wifi_ac1: str | None = None,
        wifi_ac2: str | None = None,
        wifi_ac3: str | None = None,
        ntp_service: Literal["local", "default", "specify"] | None = None,
        ntp_server1: str | None = None,
        ntp_server2: str | None = None,
        ntp_server3: str | None = None,
        domain: str | None = None,
        wins_server1: str | None = None,
        wins_server2: str | None = None,
        default_gateway: str | None = None,
        next_server: str | None = None,
        netmask: str | None = None,
        interface: str | None = None,
        ip_range: str | list[str] | list[dict[str, Any]] | None = None,
        timezone_option: Literal["disable", "default", "specify"] | None = None,
        timezone: str | None = None,
        tftp_server: str | list[str] | list[dict[str, Any]] | None = None,
        filename: str | None = None,
        options: str | list[str] | list[dict[str, Any]] | None = None,
        server_type: Literal["regular", "ipsec"] | None = None,
        ip_mode: Literal["range", "usrgrp"] | None = None,
        conflicted_ip_timeout: int | None = None,
        ipsec_lease_hold: int | None = None,
        auto_configuration: Literal["disable", "enable"] | None = None,
        dhcp_settings_from_fortiipam: Literal["disable", "enable"] | None = None,
        auto_managed_status: Literal["disable", "enable"] | None = None,
        ddns_update: Literal["disable", "enable"] | None = None,
        ddns_update_override: Literal["disable", "enable"] | None = None,
        ddns_server_ip: str | None = None,
        ddns_zone: str | None = None,
        ddns_auth: Literal["disable", "tsig"] | None = None,
        ddns_keyname: str | None = None,
        ddns_key: Any | None = None,
        ddns_ttl: int | None = None,
        vci_match: Literal["disable", "enable"] | None = None,
        vci_string: str | list[str] | list[dict[str, Any]] | None = None,
        exclude_range: str | list[str] | list[dict[str, Any]] | None = None,
        shared_subnet: Literal["disable", "enable"] | None = None,
        relay_agent: str | None = None,
        reserved_address: str | list[str] | list[dict[str, Any]] | None = None,
        vdom: str | bool | None = None,
        error_mode: Literal["raise", "return", "print"] | None = None,
        error_format: Literal["detailed", "simple", "code_only"] | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create or update system/dhcp/server object (intelligent operation).

        Automatically determines whether to create (POST) or update (PUT) based on
        whether the resource exists. Requires the primary key (id) in the payload.

        Args:
            payload_dict: Resource data including id (primary key)
            id: Field id
            status: Field status
            lease_time: Field lease-time
            mac_acl_default_action: Field mac-acl-default-action
            forticlient_on_net_status: Field forticlient-on-net-status
            dns_service: Field dns-service
            dns_server1: Field dns-server1
            dns_server2: Field dns-server2
            dns_server3: Field dns-server3
            dns_server4: Field dns-server4
            wifi_ac_service: Field wifi-ac-service
            wifi_ac1: Field wifi-ac1
            wifi_ac2: Field wifi-ac2
            wifi_ac3: Field wifi-ac3
            ntp_service: Field ntp-service
            ntp_server1: Field ntp-server1
            ntp_server2: Field ntp-server2
            ntp_server3: Field ntp-server3
            domain: Field domain
            wins_server1: Field wins-server1
            wins_server2: Field wins-server2
            default_gateway: Field default-gateway
            next_server: Field next-server
            netmask: Field netmask
            interface: Field interface
            ip_range: Field ip-range
            timezone_option: Field timezone-option
            timezone: Field timezone
            tftp_server: Field tftp-server
            filename: Field filename
            options: Field options
            server_type: Field server-type
            ip_mode: Field ip-mode
            conflicted_ip_timeout: Field conflicted-ip-timeout
            ipsec_lease_hold: Field ipsec-lease-hold
            auto_configuration: Field auto-configuration
            dhcp_settings_from_fortiipam: Field dhcp-settings-from-fortiipam
            auto_managed_status: Field auto-managed-status
            ddns_update: Field ddns-update
            ddns_update_override: Field ddns-update-override
            ddns_server_ip: Field ddns-server-ip
            ddns_zone: Field ddns-zone
            ddns_auth: Field ddns-auth
            ddns_keyname: Field ddns-keyname
            ddns_key: Field ddns-key
            ddns_ttl: Field ddns-ttl
            vci_match: Field vci-match
            vci_string: Field vci-string
            exclude_range: Field exclude-range
            shared_subnet: Field shared-subnet
            relay_agent: Field relay-agent
            reserved_address: Field reserved-address
            vdom: Virtual domain name
            **kwargs: Additional parameters passed to PUT or POST

        Returns:
            FortiObject instance. Use .dict, .json, or .raw to access as dictionary

        Raises:
            ValueError: If id is missing from payload

        Examples:
            >>> # Intelligent create or update using field parameters
            >>> result = fgt.api.cmdb.system_dhcp_server.set(
            ...     id=1,
            ...     # ... other fields
            ... )
            
            >>> # Or using payload dict
            >>> payload = {
            ...     "id": 1,
            ...     "field1": "value1",
            ...     "field2": "value2",
            ... }
            >>> result = fgt.api.cmdb.system_dhcp_server.set(payload_dict=payload)
            >>> # Will POST if object doesn't exist, PUT if it does
            
            >>> # Idempotent configuration
            >>> for obj_data in configuration_list:
            ...     fgt.api.cmdb.system_dhcp_server.set(payload_dict=obj_data)
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
            id=id,
            status=status,
            lease_time=lease_time,
            mac_acl_default_action=mac_acl_default_action,
            forticlient_on_net_status=forticlient_on_net_status,
            dns_service=dns_service,
            dns_server1=dns_server1,
            dns_server2=dns_server2,
            dns_server3=dns_server3,
            dns_server4=dns_server4,
            wifi_ac_service=wifi_ac_service,
            wifi_ac1=wifi_ac1,
            wifi_ac2=wifi_ac2,
            wifi_ac3=wifi_ac3,
            ntp_service=ntp_service,
            ntp_server1=ntp_server1,
            ntp_server2=ntp_server2,
            ntp_server3=ntp_server3,
            domain=domain,
            wins_server1=wins_server1,
            wins_server2=wins_server2,
            default_gateway=default_gateway,
            next_server=next_server,
            netmask=netmask,
            interface=interface,
            ip_range=ip_range,
            timezone_option=timezone_option,
            timezone=timezone,
            tftp_server=tftp_server,
            filename=filename,
            options=options,
            server_type=server_type,
            ip_mode=ip_mode,
            conflicted_ip_timeout=conflicted_ip_timeout,
            ipsec_lease_hold=ipsec_lease_hold,
            auto_configuration=auto_configuration,
            dhcp_settings_from_fortiipam=dhcp_settings_from_fortiipam,
            auto_managed_status=auto_managed_status,
            ddns_update=ddns_update,
            ddns_update_override=ddns_update_override,
            ddns_server_ip=ddns_server_ip,
            ddns_zone=ddns_zone,
            ddns_auth=ddns_auth,
            ddns_keyname=ddns_keyname,
            ddns_key=ddns_key,
            ddns_ttl=ddns_ttl,
            vci_match=vci_match,
            vci_string=vci_string,
            exclude_range=exclude_range,
            shared_subnet=shared_subnet,
            relay_agent=relay_agent,
            reserved_address=reserved_address,
            data=payload_dict,
        )
        
        mkey_value = payload_data.get("id")
        if not mkey_value:
            raise ValueError("id is required for set()")
        
        # Check if resource exists
        if self.exists(id=mkey_value, vdom=vdom):
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
        id: int,
        action: Literal["before", "after"],
        reference_id: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Move system/dhcp/server object to a new position.
        
        Reorders objects by moving one before or after another.
        
        Args:
            id: Identifier of object to move
            action: Move "before" or "after" reference object
            reference_id: Identifier of reference object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Move policy 100 before policy 50
            >>> fgt.api.cmdb.system_dhcp_server.move(
            ...     id=100,
            ...     action="before",
            ...     reference_id=50
            ... )
        """
        return self._client.request(
            method="PUT",
            path=f"/api/v2/cmdb/system.dhcp/server",
            params={
                "id": id,
                "action": "move",
                action: reference_id,
                "vdom": vdom,
                **kwargs,
            },
        )

    # ========================================================================
    # Action: Clone
    # ========================================================================
    
    def clone(
        self,
        id: int,
        new_id: int,
        vdom: str | bool | None = None,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Clone system/dhcp/server object.
        
        Creates a copy of an existing object with a new identifier.
        
        Args:
            id: Identifier of object to clone
            new_id: Identifier for the cloned object
            vdom: Virtual domain name
            **kwargs: Additional parameters
            
        Returns:
            API response dictionary
            
        Example:
            >>> # Clone an existing object
            >>> fgt.api.cmdb.system_dhcp_server.clone(
            ...     id=1,
            ...     new_id=100
            ... )
        """
        return self._client.request(
            method="POST",
            path=f"/api/v2/cmdb/system.dhcp/server",
            params={
                "id": id,
                "new_id": new_id,
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
        id: int,
        vdom: str | bool | None = None,
    ) -> bool:
        """
        Check if system/dhcp/server object exists.
        
        Args:
            id: Identifier to check
            vdom: Virtual domain name
            
        Returns:
            True if object exists, False otherwise
            
        Example:
            >>> # Check before creating
            >>> if not fgt.api.cmdb.system_dhcp_server.exists(id=1):
            ...     fgt.api.cmdb.system_dhcp_server.post(payload_dict=data)
        """
        # Try to fetch the object - 404 means it doesn't exist
        try:
            result = self.get(
                id=id,
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

