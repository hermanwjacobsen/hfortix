"""
FortiOS CMDB - Cmdb System Resource Limits

Configuration endpoint for managing cmdb system resource limits objects.

API Endpoints:
    GET    /cmdb/system/resource_limits
    PUT    /cmdb/system/resource_limits/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.resource_limits.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.resource_limits.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.resource_limits.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.resource_limits.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.resource_limits.delete(name="item_name")

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


class ResourceLimits:
    """
    Resourcelimits Operations.

    Provides CRUD operations for FortiOS resourcelimits configuration.

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
        Initialize ResourceLimits endpoint.

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
        endpoint = "/system/resource-limits"
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
        session: int | None = None,
        ipsec_phase1: int | None = None,
        ipsec_phase2: int | None = None,
        ipsec_phase1_interface: int | None = None,
        ipsec_phase2_interface: int | None = None,
        dialup_tunnel: int | None = None,
        firewall_policy: int | None = None,
        firewall_address: int | None = None,
        firewall_addrgrp: int | None = None,
        custom_service: int | None = None,
        service_group: int | None = None,
        onetime_schedule: int | None = None,
        recurring_schedule: int | None = None,
        user: int | None = None,
        user_group: int | None = None,
        log_disk_quota: int | None = None,
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
            session: Maximum number of sessions. (optional)
            ipsec_phase1: Maximum number of VPN IPsec phase1 tunnels.
            (optional)
            ipsec_phase2: Maximum number of VPN IPsec phase2 tunnels.
            (optional)
            ipsec_phase1_interface: Maximum number of VPN IPsec phase1
            interface tunnels. (optional)
            ipsec_phase2_interface: Maximum number of VPN IPsec phase2
            interface tunnels. (optional)
            dialup_tunnel: Maximum number of dial-up tunnels. (optional)
            firewall_policy: Maximum number of firewall policies (policy,
            DoS-policy4, DoS-policy6, multicast). (optional)
            firewall_address: Maximum number of firewall addresses (IPv4, IPv6,
            multicast). (optional)
            firewall_addrgrp: Maximum number of firewall address groups (IPv4,
            IPv6). (optional)
            custom_service: Maximum number of firewall custom services.
            (optional)
            service_group: Maximum number of firewall service groups.
            (optional)
            onetime_schedule: Maximum number of firewall one-time schedules.
            (optional)
            recurring_schedule: Maximum number of firewall recurring schedules.
            (optional)
            user: Maximum number of local users. (optional)
            user_group: Maximum number of user groups. (optional)
            log_disk_quota: Log disk quota in megabytes (MB). (optional)
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
        endpoint = "/system/resource-limits"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if session is not None:
            data_payload["session"] = session
        if ipsec_phase1 is not None:
            data_payload["ipsec-phase1"] = ipsec_phase1
        if ipsec_phase2 is not None:
            data_payload["ipsec-phase2"] = ipsec_phase2
        if ipsec_phase1_interface is not None:
            data_payload["ipsec-phase1-interface"] = ipsec_phase1_interface
        if ipsec_phase2_interface is not None:
            data_payload["ipsec-phase2-interface"] = ipsec_phase2_interface
        if dialup_tunnel is not None:
            data_payload["dialup-tunnel"] = dialup_tunnel
        if firewall_policy is not None:
            data_payload["firewall-policy"] = firewall_policy
        if firewall_address is not None:
            data_payload["firewall-address"] = firewall_address
        if firewall_addrgrp is not None:
            data_payload["firewall-addrgrp"] = firewall_addrgrp
        if custom_service is not None:
            data_payload["custom-service"] = custom_service
        if service_group is not None:
            data_payload["service-group"] = service_group
        if onetime_schedule is not None:
            data_payload["onetime-schedule"] = onetime_schedule
        if recurring_schedule is not None:
            data_payload["recurring-schedule"] = recurring_schedule
        if user is not None:
            data_payload["user"] = user
        if user_group is not None:
            data_payload["user-group"] = user_group
        if log_disk_quota is not None:
            data_payload["log-disk-quota"] = log_disk_quota
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
