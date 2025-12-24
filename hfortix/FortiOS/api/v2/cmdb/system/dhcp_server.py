"""
FortiOS CMDB - Cmdb System Dhcp Server

Configuration endpoint for managing cmdb system dhcp server objects.

API Endpoints:
    GET    /cmdb/system/dhcp_server
    POST   /cmdb/system/dhcp_server
    GET    /cmdb/system/dhcp_server
    PUT    /cmdb/system/dhcp_server/{identifier}
    DELETE /cmdb/system/dhcp_server/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.dhcp_server.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.dhcp_server.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.dhcp_server.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.dhcp_server.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.dhcp_server.delete(name="item_name")

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


class DhcpServer:
    """
    Dhcpserver Operations.

    Provides CRUD operations for FortiOS dhcpserver configuration.

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
        Initialize DhcpServer endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        id: str | None = None,
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
            id: Object identifier (optional for list, required for specific)
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
        if id:
            endpoint = f"/system.dhcp/server/{id}"
        else:
            endpoint = "/system.dhcp/server"
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
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        status: str | None = None,
        lease_time: int | None = None,
        mac_acl_default_action: str | None = None,
        forticlient_on_net_status: str | None = None,
        dns_service: str | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        wifi_ac_service: str | None = None,
        wifi_ac1: str | None = None,
        wifi_ac2: str | None = None,
        wifi_ac3: str | None = None,
        ntp_service: str | None = None,
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
        ip_range: list | None = None,
        timezone_option: str | None = None,
        timezone: str | None = None,
        tftp_server: list | None = None,
        filename: str | None = None,
        options: list | None = None,
        server_type: str | None = None,
        ip_mode: str | None = None,
        conflicted_ip_timeout: int | None = None,
        ipsec_lease_hold: int | None = None,
        auto_configuration: str | None = None,
        dhcp_settings_from_fortiipam: str | None = None,
        auto_managed_status: str | None = None,
        ddns_update: str | None = None,
        ddns_update_override: str | None = None,
        ddns_server_ip: str | None = None,
        ddns_zone: str | None = None,
        ddns_auth: str | None = None,
        ddns_keyname: str | None = None,
        ddns_key: str | None = None,
        ddns_ttl: int | None = None,
        vci_match: str | None = None,
        vci_string: list | None = None,
        exclude_range: list | None = None,
        shared_subnet: str | None = None,
        relay_agent: str | None = None,
        reserved_address: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            id: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            id: ID. (optional)
            status: Enable/disable this DHCP configuration. (optional)
            lease_time: Lease time in seconds, 0 means unlimited. (optional)
            mac_acl_default_action: MAC access control default action (allow or
            block assigning IP settings). (optional)
            forticlient_on_net_status: Enable/disable FortiClient-On-Net
            service for this DHCP server. (optional)
            dns_service: Options for assigning DNS servers to DHCP clients.
            (optional)
            dns_server1: DNS server 1. (optional)
            dns_server2: DNS server 2. (optional)
            dns_server3: DNS server 3. (optional)
            dns_server4: DNS server 4. (optional)
            wifi_ac_service: Options for assigning WiFi access controllers to
            DHCP clients. (optional)
            wifi_ac1: WiFi Access Controller 1 IP address (DHCP option 138, RFC
            5417). (optional)
            wifi_ac2: WiFi Access Controller 2 IP address (DHCP option 138, RFC
            5417). (optional)
            wifi_ac3: WiFi Access Controller 3 IP address (DHCP option 138, RFC
            5417). (optional)
            ntp_service: Options for assigning Network Time Protocol (NTP)
            servers to DHCP clients. (optional)
            ntp_server1: NTP server 1. (optional)
            ntp_server2: NTP server 2. (optional)
            ntp_server3: NTP server 3. (optional)
            domain: Domain name suffix for the IP addresses that the DHCP
            server assigns to clients. (optional)
            wins_server1: WINS server 1. (optional)
            wins_server2: WINS server 2. (optional)
            default_gateway: Default gateway IP address assigned by the DHCP
            server. (optional)
            next_server: IP address of a server (for example, a TFTP sever)
            that DHCP clients can download a boot file from. (optional)
            netmask: Netmask assigned by the DHCP server. (optional)
            interface: DHCP server can assign IP configurations to clients
            connected to this interface. (optional)
            ip_range: DHCP IP range configuration. (optional)
            timezone_option: Options for the DHCP server to set the client's
            time zone. (optional)
            timezone: Select the time zone to be assigned to DHCP clients.
            (optional)
            tftp_server: One or more hostnames or IP addresses of the TFTP
            servers in quotes separated by spaces. (optional)
            filename: Name of the boot file on the TFTP server. (optional)
            options: DHCP options. (optional)
            server_type: DHCP server can be a normal DHCP server or an IPsec
            DHCP server. (optional)
            ip_mode: Method used to assign client IP. (optional)
            conflicted_ip_timeout: Time in seconds to wait after a conflicted
            IP address is removed from the DHCP range before it can be reused.
            (optional)
            ipsec_lease_hold: DHCP over IPsec leases expire this many seconds
            after tunnel down (0 to disable forced-expiry). (optional)
            auto_configuration: Enable/disable auto configuration. (optional)
            dhcp_settings_from_fortiipam: Enable/disable populating of DHCP
            server settings from FortiIPAM. (optional)
            auto_managed_status: Enable/disable use of this DHCP server once
            this interface has been assigned an IP address from FortiIPAM.
            (optional)
            ddns_update: Enable/disable DDNS update for DHCP. (optional)
            ddns_update_override: Enable/disable DDNS update override for DHCP.
            (optional)
            ddns_server_ip: DDNS server IP. (optional)
            ddns_zone: Zone of your domain name (ex. DDNS.com). (optional)
            ddns_auth: DDNS authentication mode. (optional)
            ddns_keyname: DDNS update key name. (optional)
            ddns_key: DDNS update key (base 64 encoding). (optional)
            ddns_ttl: TTL. (optional)
            vci_match: Enable/disable vendor class identifier (VCI) matching.
            When enabled only DHCP requests with a matching VCI are served.
            (optional)
            vci_string: One or more VCI strings in quotes separated by spaces.
            (optional)
            exclude_range: Exclude one or more ranges of IP addresses from
            being assigned to clients. (optional)
            shared_subnet: Enable/disable shared subnet. (optional)
            relay_agent: Relay agent IP. (optional)
            reserved_address: Options for the DHCP server to assign IP settings
            to specific MAC addresses. (optional)
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
        if not id:
            raise ValueError("id is required for put()")
        endpoint = f"/system.dhcp/server/{id}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if id is not None:
            data_payload["id"] = id
        if status is not None:
            data_payload["status"] = status
        if lease_time is not None:
            data_payload["lease-time"] = lease_time
        if mac_acl_default_action is not None:
            data_payload["mac-acl-default-action"] = mac_acl_default_action
        if forticlient_on_net_status is not None:
            data_payload["forticlient-on-net-status"] = (
                forticlient_on_net_status
            )
        if dns_service is not None:
            data_payload["dns-service"] = dns_service
        if dns_server1 is not None:
            data_payload["dns-server1"] = dns_server1
        if dns_server2 is not None:
            data_payload["dns-server2"] = dns_server2
        if dns_server3 is not None:
            data_payload["dns-server3"] = dns_server3
        if dns_server4 is not None:
            data_payload["dns-server4"] = dns_server4
        if wifi_ac_service is not None:
            data_payload["wifi-ac-service"] = wifi_ac_service
        if wifi_ac1 is not None:
            data_payload["wifi-ac1"] = wifi_ac1
        if wifi_ac2 is not None:
            data_payload["wifi-ac2"] = wifi_ac2
        if wifi_ac3 is not None:
            data_payload["wifi-ac3"] = wifi_ac3
        if ntp_service is not None:
            data_payload["ntp-service"] = ntp_service
        if ntp_server1 is not None:
            data_payload["ntp-server1"] = ntp_server1
        if ntp_server2 is not None:
            data_payload["ntp-server2"] = ntp_server2
        if ntp_server3 is not None:
            data_payload["ntp-server3"] = ntp_server3
        if domain is not None:
            data_payload["domain"] = domain
        if wins_server1 is not None:
            data_payload["wins-server1"] = wins_server1
        if wins_server2 is not None:
            data_payload["wins-server2"] = wins_server2
        if default_gateway is not None:
            data_payload["default-gateway"] = default_gateway
        if next_server is not None:
            data_payload["next-server"] = next_server
        if netmask is not None:
            data_payload["netmask"] = netmask
        if interface is not None:
            data_payload["interface"] = interface
        if ip_range is not None:
            data_payload["ip-range"] = ip_range
        if timezone_option is not None:
            data_payload["timezone-option"] = timezone_option
        if timezone is not None:
            data_payload["timezone"] = timezone
        if tftp_server is not None:
            data_payload["tftp-server"] = tftp_server
        if filename is not None:
            data_payload["filename"] = filename
        if options is not None:
            data_payload["options"] = options
        if server_type is not None:
            data_payload["server-type"] = server_type
        if ip_mode is not None:
            data_payload["ip-mode"] = ip_mode
        if conflicted_ip_timeout is not None:
            data_payload["conflicted-ip-timeout"] = conflicted_ip_timeout
        if ipsec_lease_hold is not None:
            data_payload["ipsec-lease-hold"] = ipsec_lease_hold
        if auto_configuration is not None:
            data_payload["auto-configuration"] = auto_configuration
        if dhcp_settings_from_fortiipam is not None:
            data_payload["dhcp-settings-from-fortiipam"] = (
                dhcp_settings_from_fortiipam
            )
        if auto_managed_status is not None:
            data_payload["auto-managed-status"] = auto_managed_status
        if ddns_update is not None:
            data_payload["ddns-update"] = ddns_update
        if ddns_update_override is not None:
            data_payload["ddns-update-override"] = ddns_update_override
        if ddns_server_ip is not None:
            data_payload["ddns-server-ip"] = ddns_server_ip
        if ddns_zone is not None:
            data_payload["ddns-zone"] = ddns_zone
        if ddns_auth is not None:
            data_payload["ddns-auth"] = ddns_auth
        if ddns_keyname is not None:
            data_payload["ddns-keyname"] = ddns_keyname
        if ddns_key is not None:
            data_payload["ddns-key"] = ddns_key
        if ddns_ttl is not None:
            data_payload["ddns-ttl"] = ddns_ttl
        if vci_match is not None:
            data_payload["vci-match"] = vci_match
        if vci_string is not None:
            data_payload["vci-string"] = vci_string
        if exclude_range is not None:
            data_payload["exclude-range"] = exclude_range
        if shared_subnet is not None:
            data_payload["shared-subnet"] = shared_subnet
        if relay_agent is not None:
            data_payload["relay-agent"] = relay_agent
        if reserved_address is not None:
            data_payload["reserved-address"] = reserved_address
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            id: Object identifier (required)
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
        if not id:
            raise ValueError("id is required for delete()")
        endpoint = f"/system.dhcp/server/{id}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        id: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            id: Object identifier
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
        result = self.get(id=id, vdom=vdom)

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
        id: int | None = None,
        status: str | None = None,
        lease_time: int | None = None,
        mac_acl_default_action: str | None = None,
        forticlient_on_net_status: str | None = None,
        dns_service: str | None = None,
        dns_server1: str | None = None,
        dns_server2: str | None = None,
        dns_server3: str | None = None,
        dns_server4: str | None = None,
        wifi_ac_service: str | None = None,
        wifi_ac1: str | None = None,
        wifi_ac2: str | None = None,
        wifi_ac3: str | None = None,
        ntp_service: str | None = None,
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
        ip_range: list | None = None,
        timezone_option: str | None = None,
        timezone: str | None = None,
        tftp_server: list | None = None,
        filename: str | None = None,
        options: list | None = None,
        server_type: str | None = None,
        ip_mode: str | None = None,
        conflicted_ip_timeout: int | None = None,
        ipsec_lease_hold: int | None = None,
        auto_configuration: str | None = None,
        dhcp_settings_from_fortiipam: str | None = None,
        auto_managed_status: str | None = None,
        ddns_update: str | None = None,
        ddns_update_override: str | None = None,
        ddns_server_ip: str | None = None,
        ddns_zone: str | None = None,
        ddns_auth: str | None = None,
        ddns_keyname: str | None = None,
        ddns_key: str | None = None,
        ddns_ttl: int | None = None,
        vci_match: str | None = None,
        vci_string: list | None = None,
        exclude_range: list | None = None,
        shared_subnet: str | None = None,
        relay_agent: str | None = None,
        reserved_address: list | None = None,
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
            id: ID. (optional)
            status: Enable/disable this DHCP configuration. (optional)
            lease_time: Lease time in seconds, 0 means unlimited. (optional)
            mac_acl_default_action: MAC access control default action (allow or
            block assigning IP settings). (optional)
            forticlient_on_net_status: Enable/disable FortiClient-On-Net
            service for this DHCP server. (optional)
            dns_service: Options for assigning DNS servers to DHCP clients.
            (optional)
            dns_server1: DNS server 1. (optional)
            dns_server2: DNS server 2. (optional)
            dns_server3: DNS server 3. (optional)
            dns_server4: DNS server 4. (optional)
            wifi_ac_service: Options for assigning WiFi access controllers to
            DHCP clients. (optional)
            wifi_ac1: WiFi Access Controller 1 IP address (DHCP option 138, RFC
            5417). (optional)
            wifi_ac2: WiFi Access Controller 2 IP address (DHCP option 138, RFC
            5417). (optional)
            wifi_ac3: WiFi Access Controller 3 IP address (DHCP option 138, RFC
            5417). (optional)
            ntp_service: Options for assigning Network Time Protocol (NTP)
            servers to DHCP clients. (optional)
            ntp_server1: NTP server 1. (optional)
            ntp_server2: NTP server 2. (optional)
            ntp_server3: NTP server 3. (optional)
            domain: Domain name suffix for the IP addresses that the DHCP
            server assigns to clients. (optional)
            wins_server1: WINS server 1. (optional)
            wins_server2: WINS server 2. (optional)
            default_gateway: Default gateway IP address assigned by the DHCP
            server. (optional)
            next_server: IP address of a server (for example, a TFTP sever)
            that DHCP clients can download a boot file from. (optional)
            netmask: Netmask assigned by the DHCP server. (optional)
            interface: DHCP server can assign IP configurations to clients
            connected to this interface. (optional)
            ip_range: DHCP IP range configuration. (optional)
            timezone_option: Options for the DHCP server to set the client's
            time zone. (optional)
            timezone: Select the time zone to be assigned to DHCP clients.
            (optional)
            tftp_server: One or more hostnames or IP addresses of the TFTP
            servers in quotes separated by spaces. (optional)
            filename: Name of the boot file on the TFTP server. (optional)
            options: DHCP options. (optional)
            server_type: DHCP server can be a normal DHCP server or an IPsec
            DHCP server. (optional)
            ip_mode: Method used to assign client IP. (optional)
            conflicted_ip_timeout: Time in seconds to wait after a conflicted
            IP address is removed from the DHCP range before it can be reused.
            (optional)
            ipsec_lease_hold: DHCP over IPsec leases expire this many seconds
            after tunnel down (0 to disable forced-expiry). (optional)
            auto_configuration: Enable/disable auto configuration. (optional)
            dhcp_settings_from_fortiipam: Enable/disable populating of DHCP
            server settings from FortiIPAM. (optional)
            auto_managed_status: Enable/disable use of this DHCP server once
            this interface has been assigned an IP address from FortiIPAM.
            (optional)
            ddns_update: Enable/disable DDNS update for DHCP. (optional)
            ddns_update_override: Enable/disable DDNS update override for DHCP.
            (optional)
            ddns_server_ip: DDNS server IP. (optional)
            ddns_zone: Zone of your domain name (ex. DDNS.com). (optional)
            ddns_auth: DDNS authentication mode. (optional)
            ddns_keyname: DDNS update key name. (optional)
            ddns_key: DDNS update key (base 64 encoding). (optional)
            ddns_ttl: TTL. (optional)
            vci_match: Enable/disable vendor class identifier (VCI) matching.
            When enabled only DHCP requests with a matching VCI are served.
            (optional)
            vci_string: One or more VCI strings in quotes separated by spaces.
            (optional)
            exclude_range: Exclude one or more ranges of IP addresses from
            being assigned to clients. (optional)
            shared_subnet: Enable/disable shared subnet. (optional)
            relay_agent: Relay agent IP. (optional)
            reserved_address: Options for the DHCP server to assign IP settings
            to specific MAC addresses. (optional)
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
        endpoint = "/system.dhcp/server"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if id is not None:
            data_payload["id"] = id
        if status is not None:
            data_payload["status"] = status
        if lease_time is not None:
            data_payload["lease-time"] = lease_time
        if mac_acl_default_action is not None:
            data_payload["mac-acl-default-action"] = mac_acl_default_action
        if forticlient_on_net_status is not None:
            data_payload["forticlient-on-net-status"] = (
                forticlient_on_net_status
            )
        if dns_service is not None:
            data_payload["dns-service"] = dns_service
        if dns_server1 is not None:
            data_payload["dns-server1"] = dns_server1
        if dns_server2 is not None:
            data_payload["dns-server2"] = dns_server2
        if dns_server3 is not None:
            data_payload["dns-server3"] = dns_server3
        if dns_server4 is not None:
            data_payload["dns-server4"] = dns_server4
        if wifi_ac_service is not None:
            data_payload["wifi-ac-service"] = wifi_ac_service
        if wifi_ac1 is not None:
            data_payload["wifi-ac1"] = wifi_ac1
        if wifi_ac2 is not None:
            data_payload["wifi-ac2"] = wifi_ac2
        if wifi_ac3 is not None:
            data_payload["wifi-ac3"] = wifi_ac3
        if ntp_service is not None:
            data_payload["ntp-service"] = ntp_service
        if ntp_server1 is not None:
            data_payload["ntp-server1"] = ntp_server1
        if ntp_server2 is not None:
            data_payload["ntp-server2"] = ntp_server2
        if ntp_server3 is not None:
            data_payload["ntp-server3"] = ntp_server3
        if domain is not None:
            data_payload["domain"] = domain
        if wins_server1 is not None:
            data_payload["wins-server1"] = wins_server1
        if wins_server2 is not None:
            data_payload["wins-server2"] = wins_server2
        if default_gateway is not None:
            data_payload["default-gateway"] = default_gateway
        if next_server is not None:
            data_payload["next-server"] = next_server
        if netmask is not None:
            data_payload["netmask"] = netmask
        if interface is not None:
            data_payload["interface"] = interface
        if ip_range is not None:
            data_payload["ip-range"] = ip_range
        if timezone_option is not None:
            data_payload["timezone-option"] = timezone_option
        if timezone is not None:
            data_payload["timezone"] = timezone
        if tftp_server is not None:
            data_payload["tftp-server"] = tftp_server
        if filename is not None:
            data_payload["filename"] = filename
        if options is not None:
            data_payload["options"] = options
        if server_type is not None:
            data_payload["server-type"] = server_type
        if ip_mode is not None:
            data_payload["ip-mode"] = ip_mode
        if conflicted_ip_timeout is not None:
            data_payload["conflicted-ip-timeout"] = conflicted_ip_timeout
        if ipsec_lease_hold is not None:
            data_payload["ipsec-lease-hold"] = ipsec_lease_hold
        if auto_configuration is not None:
            data_payload["auto-configuration"] = auto_configuration
        if dhcp_settings_from_fortiipam is not None:
            data_payload["dhcp-settings-from-fortiipam"] = (
                dhcp_settings_from_fortiipam
            )
        if auto_managed_status is not None:
            data_payload["auto-managed-status"] = auto_managed_status
        if ddns_update is not None:
            data_payload["ddns-update"] = ddns_update
        if ddns_update_override is not None:
            data_payload["ddns-update-override"] = ddns_update_override
        if ddns_server_ip is not None:
            data_payload["ddns-server-ip"] = ddns_server_ip
        if ddns_zone is not None:
            data_payload["ddns-zone"] = ddns_zone
        if ddns_auth is not None:
            data_payload["ddns-auth"] = ddns_auth
        if ddns_keyname is not None:
            data_payload["ddns-keyname"] = ddns_keyname
        if ddns_key is not None:
            data_payload["ddns-key"] = ddns_key
        if ddns_ttl is not None:
            data_payload["ddns-ttl"] = ddns_ttl
        if vci_match is not None:
            data_payload["vci-match"] = vci_match
        if vci_string is not None:
            data_payload["vci-string"] = vci_string
        if exclude_range is not None:
            data_payload["exclude-range"] = exclude_range
        if shared_subnet is not None:
            data_payload["shared-subnet"] = shared_subnet
        if relay_agent is not None:
            data_payload["relay-agent"] = relay_agent
        if reserved_address is not None:
            data_payload["reserved-address"] = reserved_address
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
