"""
FortiOS CMDB - Wireless-controller InterController

API Endpoints:
    GET    /wireless-controller/inter-controller
    PUT    /wireless-controller/inter-controller
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class InterController:
    """InterController operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize InterController endpoint.

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
        endpoint = "/wireless-controller/inter-controller"
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
        inter_controller_mode: str | None = None,
        l3_roaming: str | None = None,
        inter_controller_key: str | None = None,
        inter_controller_pri: str | None = None,
        fast_failover_max: int | None = None,
        fast_failover_wait: int | None = None,
        inter_controller_peer: list | None = None,
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
            inter_controller_mode: Configure inter-controller mode (disable, l2-roaming, 1+1, default = disable). (optional)
            l3_roaming: Enable/disable layer 3 roaming (default = disable). (optional)
            inter_controller_key: Secret key for inter-controller communications. (optional)
            inter_controller_pri: Configure inter-controller's priority (primary or secondary, default = primary). (optional)
            fast_failover_max: Maximum number of retransmissions for fast failover HA messages between peer wireless controllers (3 - 64, default = 10). (optional)
            fast_failover_wait: Minimum wait time before an AP transitions from secondary controller to primary controller (10 - 86400 sec, default = 10). (optional)
            inter_controller_peer: Fast failover peer wireless controller list. (optional)
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
        endpoint = "/wireless-controller/inter-controller"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if inter_controller_mode is not None:
            data_payload['inter-controller-mode'] = inter_controller_mode
        if l3_roaming is not None:
            data_payload['l3-roaming'] = l3_roaming
        if inter_controller_key is not None:
            data_payload['inter-controller-key'] = inter_controller_key
        if inter_controller_pri is not None:
            data_payload['inter-controller-pri'] = inter_controller_pri
        if fast_failover_max is not None:
            data_payload['fast-failover-max'] = fast_failover_max
        if fast_failover_wait is not None:
            data_payload['fast-failover-wait'] = fast_failover_wait
        if inter_controller_peer is not None:
            data_payload['inter-controller-peer'] = inter_controller_peer
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
