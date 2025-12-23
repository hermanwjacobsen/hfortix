"""
FortiOS CMDB - Cmdb System Vdom Dns

Configuration endpoint for managing cmdb system vdom dns objects.

API Endpoints:
    GET    /cmdb/system/vdom_dns
    PUT    /cmdb/system/vdom_dns/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.vdom_dns.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.vdom_dns.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.vdom_dns.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.vdom_dns.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.vdom_dns.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class VdomDns:
    """
    Vdomdns Operations.

    Provides CRUD operations for FortiOS vdomdns configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize VdomDns endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
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
        endpoint = "/system/vdom-dns"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        vdom_dns: str | None = None,
        primary: str | None = None,
        secondary: str | None = None,
        protocol: str | None = None,
        ssl_certificate: str | None = None,
        server_hostname: list | None = None,
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        server_select_method: str | None = None,
        alt_primary: str | None = None,
        alt_secondary: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            vdom_dns: Enable/disable configuring DNS servers for the current
            VDOM. (optional)
            primary: Primary DNS server IP address for the VDOM. (optional)
            secondary: Secondary DNS server IP address for the VDOM. (optional)
            protocol: DNS transport protocols. (optional)
            ssl_certificate: Name of local certificate for SSL connections.
            (optional)
            server_hostname: DNS server host name list. (optional)
            ip6_primary: Primary IPv6 DNS server IP address for the VDOM.
            (optional)
            ip6_secondary: Secondary IPv6 DNS server IP address for the VDOM.
            (optional)
            source_ip: Source IP for communications with the DNS server.
            (optional)
            source_ip_interface: IP address of the specified interface as the
            source IP address. (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            server_select_method: Specify how configured servers are
            prioritized. (optional)
            alt_primary: Alternate primary DNS server. This is not used as a
            failover DNS server. (optional)
            alt_secondary: Alternate secondary DNS server. This is not used as
            a failover DNS server. (optional)
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
        endpoint = "/system/vdom-dns"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if vdom_dns is not None:
            data_payload["vdom-dns"] = vdom_dns
        if primary is not None:
            data_payload["primary"] = primary
        if secondary is not None:
            data_payload["secondary"] = secondary
        if protocol is not None:
            data_payload["protocol"] = protocol
        if ssl_certificate is not None:
            data_payload["ssl-certificate"] = ssl_certificate
        if server_hostname is not None:
            data_payload["server-hostname"] = server_hostname
        if ip6_primary is not None:
            data_payload["ip6-primary"] = ip6_primary
        if ip6_secondary is not None:
            data_payload["ip6-secondary"] = ip6_secondary
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if server_select_method is not None:
            data_payload["server-select-method"] = server_select_method
        if alt_primary is not None:
            data_payload["alt-primary"] = alt_primary
        if alt_secondary is not None:
            data_payload["alt-secondary"] = alt_secondary
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
