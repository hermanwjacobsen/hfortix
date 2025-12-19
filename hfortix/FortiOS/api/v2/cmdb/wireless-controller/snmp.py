"""
FortiOS CMDB - Wireless-controller Snmp

API Endpoints:
    GET    /wireless-controller/snmp
    PUT    /wireless-controller/snmp
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Snmp:
    """Snmp operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Snmp endpoint.

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
        endpoint = "/wireless-controller/snmp"
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
        engine_id: str | None = None,
        contact_info: str | None = None,
        trap_high_cpu_threshold: int | None = None,
        trap_high_mem_threshold: int | None = None,
        community: list | None = None,
        user: list | None = None,
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
            engine_id: AC SNMP engineID string (maximum 24 characters). (optional)
            contact_info: Contact Information. (optional)
            trap_high_cpu_threshold: CPU usage when trap is sent. (optional)
            trap_high_mem_threshold: Memory usage when trap is sent. (optional)
            community: SNMP Community Configuration. (optional)
            user: SNMP User Configuration. (optional)
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
        endpoint = "/wireless-controller/snmp"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if engine_id is not None:
            data_payload['engine-id'] = engine_id
        if contact_info is not None:
            data_payload['contact-info'] = contact_info
        if trap_high_cpu_threshold is not None:
            data_payload['trap-high-cpu-threshold'] = trap_high_cpu_threshold
        if trap_high_mem_threshold is not None:
            data_payload['trap-high-mem-threshold'] = trap_high_mem_threshold
        if community is not None:
            data_payload['community'] = community
        if user is not None:
            data_payload['user'] = user
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
