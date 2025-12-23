"""
FortiOS CMDB - Cmdb Ips Global

Configuration endpoint for managing cmdb ips global objects.

API Endpoints:
    GET    /cmdb/ips/global_
    PUT    /cmdb/ips/global_/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.ips.global_.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.ips.global_.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.ips.global_.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.ips.global_.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.ips.global_.delete(name="item_name")

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


class Global:
    """
    Global Operations.

    Provides CRUD operations for FortiOS global configuration.

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
        Initialize Global endpoint.

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
        endpoint = "/ips/global"
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
        fail_open: str | None = None,
        database: str | None = None,
        traffic_submit: str | None = None,
        anomaly_mode: str | None = None,
        session_limit_mode: str | None = None,
        socket_size: int | None = None,
        engine_count: int | None = None,
        sync_session_ttl: str | None = None,
        np_accel_mode: str | None = None,
        ips_reserve_cpu: str | None = None,
        cp_accel_mode: str | None = None,
        deep_app_insp_timeout: int | None = None,
        deep_app_insp_db_limit: int | None = None,
        exclude_signatures: str | None = None,
        packet_log_queue_depth: int | None = None,
        ngfw_max_scan_range: int | None = None,
        av_mem_limit: int | None = None,
        machine_learning_detection: str | None = None,
        tls_active_probe: list | None = None,
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
            fail_open: Enable to allow traffic if the IPS buffer is full.
            Default is disable and IPS traffic is blocked when the IPS buffer
            is full. (optional)
            database: Regular or extended IPS database. Regular protects
            against the latest common and in-the-wild attacks. Extended
            includes protection from legacy attacks. (optional)
            traffic_submit: Enable/disable submitting attack data found by this
            FortiGate to FortiGuard. (optional)
            anomaly_mode: Global blocking mode for rate-based anomalies.
            (optional)
            session_limit_mode: Method of counting concurrent sessions used by
            session limit anomalies. Choose between greater accuracy (accurate)
            or improved performance (heuristics). (optional)
            socket_size: IPS socket buffer size. Max and default value depend
            on available memory. Can be changed to tune performance. (optional)
            engine_count: Number of IPS engines running. If set to the default
            value of 0, FortiOS sets the number to optimize performance
            depending on the number of CPU cores. (optional)
            sync_session_ttl: Enable/disable use of kernel session TTL for IPS
            sessions. (optional)
            np_accel_mode: Acceleration mode for IPS processing by NPx
            processors. (optional)
            ips_reserve_cpu: Enable/disable IPS daemon's use of CPUs other than
            CPU 0. (optional)
            cp_accel_mode: IPS Pattern matching acceleration/offloading to CPx
            processors. (optional)
            deep_app_insp_timeout: Timeout for Deep application inspection (1 -
            2147483647 sec., 0 = use recommended setting). (optional)
            deep_app_insp_db_limit: Limit on number of entries in deep
            application inspection database (1 - 2147483647, use recommended
            setting = 0). (optional)
            exclude_signatures: Excluded signatures. (optional)
            packet_log_queue_depth: Packet/pcap log queue depth per IPS engine.
            (optional)
            ngfw_max_scan_range: NGFW policy-mode app detection threshold.
            (optional)
            av_mem_limit: Maximum percentage of system memory allowed for use
            on AV scanning (10 - 50, default = zero). To disable set to zero.
            When disabled, there is no limit on the AV memory usage. (optional)
            machine_learning_detection: Enable/disable machine learning
            detection. (optional)
            tls_active_probe: TLS active probe configuration. (optional)
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
        endpoint = "/ips/global"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if fail_open is not None:
            data_payload["fail-open"] = fail_open
        if database is not None:
            data_payload["database"] = database
        if traffic_submit is not None:
            data_payload["traffic-submit"] = traffic_submit
        if anomaly_mode is not None:
            data_payload["anomaly-mode"] = anomaly_mode
        if session_limit_mode is not None:
            data_payload["session-limit-mode"] = session_limit_mode
        if socket_size is not None:
            data_payload["socket-size"] = socket_size
        if engine_count is not None:
            data_payload["engine-count"] = engine_count
        if sync_session_ttl is not None:
            data_payload["sync-session-ttl"] = sync_session_ttl
        if np_accel_mode is not None:
            data_payload["np-accel-mode"] = np_accel_mode
        if ips_reserve_cpu is not None:
            data_payload["ips-reserve-cpu"] = ips_reserve_cpu
        if cp_accel_mode is not None:
            data_payload["cp-accel-mode"] = cp_accel_mode
        if deep_app_insp_timeout is not None:
            data_payload["deep-app-insp-timeout"] = deep_app_insp_timeout
        if deep_app_insp_db_limit is not None:
            data_payload["deep-app-insp-db-limit"] = deep_app_insp_db_limit
        if exclude_signatures is not None:
            data_payload["exclude-signatures"] = exclude_signatures
        if packet_log_queue_depth is not None:
            data_payload["packet-log-queue-depth"] = packet_log_queue_depth
        if ngfw_max_scan_range is not None:
            data_payload["ngfw-max-scan-range"] = ngfw_max_scan_range
        if av_mem_limit is not None:
            data_payload["av-mem-limit"] = av_mem_limit
        if machine_learning_detection is not None:
            data_payload["machine-learning-detection"] = (
                machine_learning_detection
            )
        if tls_active_probe is not None:
            data_payload["tls-active-probe"] = tls_active_probe
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
