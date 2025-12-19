"""
FortiOS CMDB - System ProbeResponse

API Endpoints:
    GET    /system/probe-response
    PUT    /system/probe-response
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class ProbeResponse:
    """ProbeResponse operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ProbeResponse endpoint.

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
        endpoint = "/system/probe-response"
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
        port: int | None = None,
        http_probe_value: str | None = None,
        ttl_mode: str | None = None,
        mode: str | None = None,
        security_mode: str | None = None,
        password: str | None = None,
        timeout: int | None = None,
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
            port: Port number to response. (optional)
            http_probe_value: Value to respond to the monitoring server. (optional)
            ttl_mode: Mode for TWAMP packet TTL modification. (optional)
            mode: SLA response mode. (optional)
            security_mode: TWAMP responder security mode. (optional)
            password: TWAMP responder password in authentication mode. (optional)
            timeout: An inactivity timer for a twamp test session. (optional)
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
        endpoint = "/system/probe-response"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if port is not None:
            data_payload['port'] = port
        if http_probe_value is not None:
            data_payload['http-probe-value'] = http_probe_value
        if ttl_mode is not None:
            data_payload['ttl-mode'] = ttl_mode
        if mode is not None:
            data_payload['mode'] = mode
        if security_mode is not None:
            data_payload['security-mode'] = security_mode
        if password is not None:
            data_payload['password'] = password
        if timeout is not None:
            data_payload['timeout'] = timeout
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
