"""
FortiOS CMDB - Log FortiguardSetting

API Endpoints:
    GET    /log.fortiguard/setting
    PUT    /log.fortiguard/setting
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class FortiguardSetting:
    """FortiguardSetting operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize FortiguardSetting endpoint.

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
        endpoint = "/log.fortiguard/setting"
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
        status: str | None = None,
        upload_option: str | None = None,
        upload_interval: str | None = None,
        upload_day: str | None = None,
        upload_time: str | None = None,
        priority: str | None = None,
        max_log_rate: int | None = None,
        access_config: str | None = None,
        enc_algorithm: str | None = None,
        ssl_min_proto_version: str | None = None,
        conn_timeout: int | None = None,
        source_ip: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            status: Enable/disable logging to FortiCloud. (optional)
            upload_option: Configure how log messages are sent to FortiCloud. (optional)
            upload_interval: Frequency of uploading log files to FortiCloud. (optional)
            upload_day: Day of week to roll logs. (optional)
            upload_time: Time of day to roll logs (hh:mm). (optional)
            priority: Set log transmission priority. (optional)
            max_log_rate: FortiCloud maximum log rate in MBps (0 = unlimited). (optional)
            access_config: Enable/disable FortiCloud access to configuration and data. (optional)
            enc_algorithm: Configure the level of SSL protection for secure communication with FortiCloud. (optional)
            ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections (default is to follow system global setting). (optional)
            conn_timeout: FortiGate Cloud connection timeout in seconds. (optional)
            source_ip: Source IP address used to connect FortiCloud. (optional)
            interface_select_method: Specify how to select outgoing interface to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = "/log.fortiguard/setting"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if upload_option is not None:
            data_payload['upload-option'] = upload_option
        if upload_interval is not None:
            data_payload['upload-interval'] = upload_interval
        if upload_day is not None:
            data_payload['upload-day'] = upload_day
        if upload_time is not None:
            data_payload['upload-time'] = upload_time
        if priority is not None:
            data_payload['priority'] = priority
        if max_log_rate is not None:
            data_payload['max-log-rate'] = max_log_rate
        if access_config is not None:
            data_payload['access-config'] = access_config
        if enc_algorithm is not None:
            data_payload['enc-algorithm'] = enc_algorithm
        if ssl_min_proto_version is not None:
            data_payload['ssl-min-proto-version'] = ssl_min_proto_version
        if conn_timeout is not None:
            data_payload['conn-timeout'] = conn_timeout
        if source_ip is not None:
            data_payload['source-ip'] = source_ip
        if interface_select_method is not None:
            data_payload['interface-select-method'] = interface_select_method
        if interface is not None:
            data_payload['interface'] = interface
        if vrf_select is not None:
            data_payload['vrf-select'] = vrf_select
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
