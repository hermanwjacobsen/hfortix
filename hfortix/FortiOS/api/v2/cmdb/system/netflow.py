"""
FortiOS CMDB - Cmdb System Netflow

Configuration endpoint for managing cmdb system netflow objects.

API Endpoints:
    GET    /cmdb/system/netflow
    PUT    /cmdb/system/netflow/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.system.netflow.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.netflow.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.netflow.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.netflow.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.netflow.delete(name="item_name")

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


class Netflow:
    """
    Netflow Operations.

    Provides CRUD operations for FortiOS netflow configuration.

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
        Initialize Netflow endpoint.

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
        endpoint = "/system/netflow"
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
        active_flow_timeout: int | None = None,
        inactive_flow_timeout: int | None = None,
        template_tx_timeout: int | None = None,
        template_tx_counter: int | None = None,
        session_cache_size: str | None = None,
        exclusion_filters: list | None = None,
        collectors: list | None = None,
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
            active_flow_timeout: Timeout to report active flows (60 - 3600 sec,
            default = 1800). (optional)
            inactive_flow_timeout: Timeout for periodic report of finished
            flows (10 - 600 sec, default = 15). (optional)
            template_tx_timeout: Timeout for periodic template flowset
            transmission (60 - 86400 sec, default = 1800). (optional)
            template_tx_counter: Counter of flowset records before resending a
            template flowset record. (optional)
            session_cache_size: Maximum RAM usage allowed for Netflow session
            cache. (optional)
            exclusion_filters: Exclusion filters (optional)
            collectors: Netflow collectors. (optional)
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
        endpoint = "/system/netflow"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if active_flow_timeout is not None:
            data_payload["active-flow-timeout"] = active_flow_timeout
        if inactive_flow_timeout is not None:
            data_payload["inactive-flow-timeout"] = inactive_flow_timeout
        if template_tx_timeout is not None:
            data_payload["template-tx-timeout"] = template_tx_timeout
        if template_tx_counter is not None:
            data_payload["template-tx-counter"] = template_tx_counter
        if session_cache_size is not None:
            data_payload["session-cache-size"] = session_cache_size
        if exclusion_filters is not None:
            data_payload["exclusion-filters"] = exclusion_filters
        if collectors is not None:
            data_payload["collectors"] = collectors
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
