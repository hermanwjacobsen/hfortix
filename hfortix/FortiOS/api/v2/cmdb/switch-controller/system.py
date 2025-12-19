"""
FortiOS CMDB - Switch-controller System

API Endpoints:
    GET    /switch-controller/system
    PUT    /switch-controller/system
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class System:
    """System operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize System endpoint.

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
        endpoint = "/switch-controller/system"
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
        parallel_process_override: str | None = None,
        parallel_process: int | None = None,
        data_sync_interval: int | None = None,
        iot_weight_threshold: int | None = None,
        iot_scan_interval: int | None = None,
        iot_holdoff: int | None = None,
        iot_mac_idle: int | None = None,
        nac_periodic_interval: int | None = None,
        dynamic_periodic_interval: int | None = None,
        tunnel_mode: str | None = None,
        caputp_echo_interval: int | None = None,
        caputp_max_retransmit: int | None = None,
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
            parallel_process_override: Enable/disable parallel process override. (optional)
            parallel_process: Maximum number of parallel processes. (optional)
            data_sync_interval: Time interval between collection of switch data (30 - 1800 sec, default = 60, 0 = disable). (optional)
            iot_weight_threshold: MAC entry's confidence value. Value is re-queried when below this value (default = 1, 0 = disable). (optional)
            iot_scan_interval: IoT scan interval (2 - 10080 mins, default = 60 mins, 0 = disable). (optional)
            iot_holdoff: MAC entry's creation time. Time must be greater than this value for an entry to be created (0 - 10080 mins, default = 5 mins). (optional)
            iot_mac_idle: MAC entry's idle time. MAC entry is removed after this value (0 - 10080 mins, default = 1440 mins). (optional)
            nac_periodic_interval: Periodic time interval to run NAC engine (5 - 180 sec, default = 60). (optional)
            dynamic_periodic_interval: Periodic time interval to run Dynamic port policy engine (5 - 180 sec, default = 60). (optional)
            tunnel_mode: Compatible/strict tunnel mode. (optional)
            caputp_echo_interval: Echo interval for the caputp echo requests from swtp. (optional)
            caputp_max_retransmit: Maximum retransmission count for the caputp tunnel packets. (optional)
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
        endpoint = "/switch-controller/system"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if parallel_process_override is not None:
            data_payload['parallel-process-override'] = parallel_process_override
        if parallel_process is not None:
            data_payload['parallel-process'] = parallel_process
        if data_sync_interval is not None:
            data_payload['data-sync-interval'] = data_sync_interval
        if iot_weight_threshold is not None:
            data_payload['iot-weight-threshold'] = iot_weight_threshold
        if iot_scan_interval is not None:
            data_payload['iot-scan-interval'] = iot_scan_interval
        if iot_holdoff is not None:
            data_payload['iot-holdoff'] = iot_holdoff
        if iot_mac_idle is not None:
            data_payload['iot-mac-idle'] = iot_mac_idle
        if nac_periodic_interval is not None:
            data_payload['nac-periodic-interval'] = nac_periodic_interval
        if dynamic_periodic_interval is not None:
            data_payload['dynamic-periodic-interval'] = dynamic_periodic_interval
        if tunnel_mode is not None:
            data_payload['tunnel-mode'] = tunnel_mode
        if caputp_echo_interval is not None:
            data_payload['caputp-echo-interval'] = caputp_echo_interval
        if caputp_max_retransmit is not None:
            data_payload['caputp-max-retransmit'] = caputp_max_retransmit
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
