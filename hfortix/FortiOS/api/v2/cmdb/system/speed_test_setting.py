"""
FortiOS CMDB - Cmdb System Speed Test Setting

Configuration endpoint for managing cmdb system speed test setting objects.

API Endpoints:
    GET    /cmdb/system/speed_test_setting
    PUT    /cmdb/system/speed_test_setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>> 
    >>> # List all items
    >>> items = fgt.api.cmdb.system.speed_test_setting.get()
    >>> 
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.system.speed_test_setting.get(name="item_name")
    >>> 
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.system.speed_test_setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>> 
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.system.speed_test_setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>> 
    >>> # Delete item
    >>> result = fgt.api.cmdb.system.speed_test_setting.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class SpeedTestSetting:
    """
    Speedtestsetting Operations.
    
    Provides CRUD operations for FortiOS speedtestsetting configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects
    
    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize SpeedTestSetting endpoint.

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
        endpoint = "/system/speed-test-setting"
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
        latency_threshold: int | None = None,
        multiple_tcp_stream: int | None = None,
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
            latency_threshold: Speed test latency threshold in milliseconds (0 - 2000, default = 60) for the Auto mode. If the latency exceeds this threshold, the speed test will use the UDP protocol; otherwise, it will use the TCP protocol. (optional)
            multiple_tcp_stream: Number of parallel client streams (1 - 64, default = 4) for the TCP protocol to run during the speed test. (optional)
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
        endpoint = "/system/speed-test-setting"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if latency_threshold is not None:
            data_payload['latency-threshold'] = latency_threshold
        if multiple_tcp_stream is not None:
            data_payload['multiple-tcp-stream'] = multiple_tcp_stream
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
