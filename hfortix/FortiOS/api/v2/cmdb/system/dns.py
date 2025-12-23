"""
FortiOS CMDB - Cmdb System Dns

Configuration endpoint for managing cmdb system dns objects.

API Endpoints:
    GET    /cmdb/system/dns
    PUT    /cmdb/system/dns/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.dns.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.dns.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.dns.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.dns.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.dns.delete(name="item_name")

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


class Dns:
    """
    Dns Operations.

    Provides CRUD operations for FortiOS dns configuration.

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
        Initialize Dns endpoint.

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
        endpoint = "/system/dns"
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
        primary: str | None = None,
        secondary: str | None = None,
        protocol: str | None = None,
        ssl_certificate: str | None = None,
        server_hostname: list | None = None,
        domain: list | None = None,
        ip6_primary: str | None = None,
        ip6_secondary: str | None = None,
        timeout: int | None = None,
        retry: int | None = None,
        dns_cache_limit: int | None = None,
        dns_cache_ttl: int | None = None,
        cache_notfound_responses: str | None = None,
        source_ip: str | None = None,
        source_ip_interface: str | None = None,
        root_servers: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        server_select_method: str | None = None,
        alt_primary: str | None = None,
        alt_secondary: str | None = None,
        log: str | None = None,
        fqdn_cache_ttl: int | None = None,
        fqdn_max_refresh: int | None = None,
        fqdn_min_refresh: int | None = None,
        hostname_ttl: int | None = None,
        hostname_limit: int | None = None,
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
            primary: Primary DNS server IP address. (optional)
            secondary: Secondary DNS server IP address. (optional)
            protocol: DNS transport protocols. (optional)
            ssl_certificate: Name of local certificate for SSL connections.
            (optional)
            server_hostname: DNS server host name list. (optional)
            domain: Search suffix list for hostname lookup. (optional)
            ip6_primary: Primary DNS server IPv6 address. (optional)
            ip6_secondary: Secondary DNS server IPv6 address. (optional)
            timeout: DNS query timeout interval in seconds (1 - 10). (optional)
            retry: Number of times to retry (0 - 5). (optional)
            dns_cache_limit: Maximum number of records in the DNS cache.
            (optional)
            dns_cache_ttl: Duration in seconds that the DNS cache retains
            information. (optional)
            cache_notfound_responses: Enable/disable response from the DNS
            server when a record is not in cache. (optional)
            source_ip: IP address used by the DNS server as its source IP.
            (optional)
            source_ip_interface: IP address of the specified interface as the
            source IP address. (optional)
            root_servers: Configure up to two preferred servers that serve the
            DNS root zone (default uses all 13 root servers). (optional)
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
            log: Local DNS log setting. (optional)
            fqdn_cache_ttl: FQDN cache time to live in seconds (0 - 86400,
            default = 0). (optional)
            fqdn_max_refresh: FQDN cache maximum refresh time in seconds (3600
            - 86400, default = 3600). (optional)
            fqdn_min_refresh: FQDN cache minimum refresh time in seconds (10 -
            3600, default = 60). (optional)
            hostname_ttl: TTL of hostname table entries (60 - 86400).
            (optional)
            hostname_limit: Limit of the number of hostname table entries (0 -
            50000). (optional)
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
        endpoint = "/system/dns"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
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
        if domain is not None:
            data_payload["domain"] = domain
        if ip6_primary is not None:
            data_payload["ip6-primary"] = ip6_primary
        if ip6_secondary is not None:
            data_payload["ip6-secondary"] = ip6_secondary
        if timeout is not None:
            data_payload["timeout"] = timeout
        if retry is not None:
            data_payload["retry"] = retry
        if dns_cache_limit is not None:
            data_payload["dns-cache-limit"] = dns_cache_limit
        if dns_cache_ttl is not None:
            data_payload["dns-cache-ttl"] = dns_cache_ttl
        if cache_notfound_responses is not None:
            data_payload["cache-notfound-responses"] = cache_notfound_responses
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if root_servers is not None:
            data_payload["root-servers"] = root_servers
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
        if log is not None:
            data_payload["log"] = log
        if fqdn_cache_ttl is not None:
            data_payload["fqdn-cache-ttl"] = fqdn_cache_ttl
        if fqdn_max_refresh is not None:
            data_payload["fqdn-max-refresh"] = fqdn_max_refresh
        if fqdn_min_refresh is not None:
            data_payload["fqdn-min-refresh"] = fqdn_min_refresh
        if hostname_ttl is not None:
            data_payload["hostname-ttl"] = hostname_ttl
        if hostname_limit is not None:
            data_payload["hostname-limit"] = hostname_limit
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
