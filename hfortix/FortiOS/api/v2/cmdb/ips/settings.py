"""
FortiOS CMDB - Ips Settings

API Endpoints:
    GET    /ips/settings
    PUT    /ips/settings
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Settings:
    """Settings operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Settings endpoint.

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
        endpoint = "/ips/settings"
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
        packet_log_history: int | None = None,
        packet_log_post_attack: int | None = None,
        packet_log_memory: int | None = None,
        ips_packet_quota: int | None = None,
        proxy_inline_ips: str | None = None,
        ha_session_pickup: str | None = None,
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
            packet_log_history: Number of packets to capture before and including the one in which the IPS signature is detected (1 - 255). (optional)
            packet_log_post_attack: Number of packets to log after the IPS signature is detected (0 - 255). (optional)
            packet_log_memory: Maximum memory can be used by packet log (64 - 8192 kB). (optional)
            ips_packet_quota: Maximum amount of disk space in MB for logged packets when logging to disk. Range depends on disk size. (optional)
            proxy_inline_ips: Enable/disable proxy-mode policy inline IPS support. (optional)
            ha_session_pickup: IPS HA failover session pickup preference. (optional)
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
        endpoint = "/ips/settings"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if packet_log_history is not None:
            data_payload['packet-log-history'] = packet_log_history
        if packet_log_post_attack is not None:
            data_payload['packet-log-post-attack'] = packet_log_post_attack
        if packet_log_memory is not None:
            data_payload['packet-log-memory'] = packet_log_memory
        if ips_packet_quota is not None:
            data_payload['ips-packet-quota'] = ips_packet_quota
        if proxy_inline_ips is not None:
            data_payload['proxy-inline-ips'] = proxy_inline_ips
        if ha_session_pickup is not None:
            data_payload['ha-session-pickup'] = ha_session_pickup
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
