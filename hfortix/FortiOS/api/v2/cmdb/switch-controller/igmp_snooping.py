"""
FortiOS CMDB - Switch-controller IgmpSnooping

API Endpoints:
    GET    /switch-controller/igmp-snooping
    PUT    /switch-controller/igmp-snooping
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class IgmpSnooping:
    """IgmpSnooping operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize IgmpSnooping endpoint.

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
    ) -> dict[str, Any]:
        """
        Select all entries in a CLI table.
        
        Args:
            exclude_default_values: Exclude properties/objects with default value (optional)
            stat_items: Items to count occurrence in entire response (multiple items should be separated by '|'). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        endpoint = "/switch-controller/igmp-snooping"
        if exclude_default_values is not None:
            params['exclude-default-values'] = exclude_default_values
        if stat_items is not None:
            params['stat-items'] = stat_items
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        aging_time: int | None = None,
        flood_unknown_multicast: str | None = None,
        query_interval: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            aging_time: Maximum number of seconds to retain a multicast snooping entry for which no packets have been seen (15 - 3600 sec, default = 300). (optional)
            flood_unknown_multicast: Enable/disable unknown multicast flooding. (optional)
            query_interval: Maximum time after which IGMP query will be sent (10 - 1200 sec, default = 125). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/switch-controller/igmp-snooping"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if aging_time is not None:
            data_payload['aging-time'] = aging_time
        if flood_unknown_multicast is not None:
            data_payload['flood-unknown-multicast'] = flood_unknown_multicast
        if query_interval is not None:
            data_payload['query-interval'] = query_interval
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
