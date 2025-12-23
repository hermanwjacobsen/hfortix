"""
FortiOS CMDB - Cmdb Log Eventfilter

Configuration endpoint for managing cmdb log eventfilter objects.

API Endpoints:
    GET    /cmdb/log/eventfilter
    PUT    /cmdb/log/eventfilter/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log.eventfilter.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.log.eventfilter.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.log.eventfilter.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.log.eventfilter.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.log.eventfilter.delete(name="item_name")

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


class Eventfilter:
    """
    Eventfilter Operations.

    Provides CRUD operations for FortiOS eventfilter configuration.

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
        Initialize Eventfilter endpoint.

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
        endpoint = "/log/eventfilter"
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
        event: str | None = None,
        system: str | None = None,
        vpn: str | None = None,
        user: str | None = None,
        router: str | None = None,
        wireless_activity: str | None = None,
        wan_opt: str | None = None,
        endpoint: str | None = None,
        ha: str | None = None,
        security_rating: str | None = None,
        fortiextender: str | None = None,
        connector: str | None = None,
        sdwan: str | None = None,
        cifs: str | None = None,
        switch_controller: str | None = None,
        rest_api: str | None = None,
        web_svc: str | None = None,
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
            event: Enable/disable event logging. (optional)
            system: Enable/disable system event logging. (optional)
            vpn: Enable/disable VPN event logging. (optional)
            user: Enable/disable user authentication event logging. (optional)
            router: Enable/disable router event logging. (optional)
            wireless_activity: Enable/disable wireless event logging.
            (optional)
            wan_opt: Enable/disable WAN optimization event logging. (optional)
            endpoint: Enable/disable endpoint event logging. (optional)
            ha: Enable/disable ha event logging. (optional)
            security_rating: Enable/disable Security Rating result logging.
            (optional)
            fortiextender: Enable/disable FortiExtender logging. (optional)
            connector: Enable/disable SDN connector logging. (optional)
            sdwan: Enable/disable SD-WAN logging. (optional)
            cifs: Enable/disable CIFS logging. (optional)
            switch_controller: Enable/disable Switch-Controller logging.
            (optional)
            rest_api: Enable/disable REST API logging. (optional)
            web_svc: Enable/disable web-svc performance logging. (optional)
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
        endpoint = "/log/eventfilter"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if event is not None:
            data_payload["event"] = event
        if system is not None:
            data_payload["system"] = system
        if vpn is not None:
            data_payload["vpn"] = vpn
        if user is not None:
            data_payload["user"] = user
        if router is not None:
            data_payload["router"] = router
        if wireless_activity is not None:
            data_payload["wireless-activity"] = wireless_activity
        if wan_opt is not None:
            data_payload["wan-opt"] = wan_opt
        if endpoint is not None:
            data_payload["endpoint"] = endpoint
        if ha is not None:
            data_payload["ha"] = ha
        if security_rating is not None:
            data_payload["security-rating"] = security_rating
        if fortiextender is not None:
            data_payload["fortiextender"] = fortiextender
        if connector is not None:
            data_payload["connector"] = connector
        if sdwan is not None:
            data_payload["sdwan"] = sdwan
        if cifs is not None:
            data_payload["cifs"] = cifs
        if switch_controller is not None:
            data_payload["switch-controller"] = switch_controller
        if rest_api is not None:
            data_payload["rest-api"] = rest_api
        if web_svc is not None:
            data_payload["web-svc"] = web_svc
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
