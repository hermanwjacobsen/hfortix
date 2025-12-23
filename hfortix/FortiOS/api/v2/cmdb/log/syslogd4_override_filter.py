"""
FortiOS CMDB - Cmdb Log Syslogd4 Override Filter

Configuration endpoint for managing cmdb log syslogd4 override filter objects.

API Endpoints:
    GET    /cmdb/log/syslogd4_override_filter
    PUT    /cmdb/log/syslogd4_override_filter/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log.syslogd4_override_filter.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.log.syslogd4_override_filter.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.log.syslogd4_override_filter.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.log.syslogd4_override_filter.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.log.syslogd4_override_filter.delete(name="item_name")

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


class Syslogd4OverrideFilter:
    """
    Syslogd4Overridefilter Operations.

    Provides CRUD operations for FortiOS syslogd4overridefilter configuration.

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
        Initialize Syslogd4OverrideFilter endpoint.

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
        endpoint = "/log.syslogd4/override-filter"
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
        severity: str | None = None,
        forward_traffic: str | None = None,
        local_traffic: str | None = None,
        multicast_traffic: str | None = None,
        sniffer_traffic: str | None = None,
        ztna_traffic: str | None = None,
        http_transaction: str | None = None,
        anomaly: str | None = None,
        voip: str | None = None,
        forti_switch: str | None = None,
        debug: str | None = None,
        free_style: list | None = None,
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
            severity: Lowest severity level to log. (optional)
            forward_traffic: Enable/disable forward traffic logging. (optional)
            local_traffic: Enable/disable local in or out traffic logging.
            (optional)
            multicast_traffic: Enable/disable multicast traffic logging.
            (optional)
            sniffer_traffic: Enable/disable sniffer traffic logging. (optional)
            ztna_traffic: Enable/disable ztna traffic logging. (optional)
            http_transaction: Enable/disable log HTTP transaction messages.
            (optional)
            anomaly: Enable/disable anomaly logging. (optional)
            voip: Enable/disable VoIP logging. (optional)
            forti_switch: Enable/disable Forti-Switch logging. (optional)
            debug: Enable/disable debug logging. (optional)
            free_style: Free style filters. (optional)
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
        endpoint = "/log.syslogd4/override-filter"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if severity is not None:
            data_payload["severity"] = severity
        if forward_traffic is not None:
            data_payload["forward-traffic"] = forward_traffic
        if local_traffic is not None:
            data_payload["local-traffic"] = local_traffic
        if multicast_traffic is not None:
            data_payload["multicast-traffic"] = multicast_traffic
        if sniffer_traffic is not None:
            data_payload["sniffer-traffic"] = sniffer_traffic
        if ztna_traffic is not None:
            data_payload["ztna-traffic"] = ztna_traffic
        if http_transaction is not None:
            data_payload["http-transaction"] = http_transaction
        if anomaly is not None:
            data_payload["anomaly"] = anomaly
        if voip is not None:
            data_payload["voip"] = voip
        if forti_switch is not None:
            data_payload["forti-switch"] = forti_switch
        if debug is not None:
            data_payload["debug"] = debug
        if free_style is not None:
            data_payload["free-style"] = free_style
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
