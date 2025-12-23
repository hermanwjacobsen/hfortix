"""
FortiOS CMDB - Cmdb Log Fortianalyzer2 Setting

Configuration endpoint for managing cmdb log fortianalyzer2 setting objects.

API Endpoints:
    GET    /cmdb/log/fortianalyzer2_setting
    PUT    /cmdb/log/fortianalyzer2_setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log.fortianalyzer2_setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.log.fortianalyzer2_setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.log.fortianalyzer2_setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.log.fortianalyzer2_setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.log.fortianalyzer2_setting.delete(name="item_name")

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


class Fortianalyzer2Setting:
    """
    Fortianalyzer2Setting Operations.

    Provides CRUD operations for FortiOS fortianalyzer2setting configuration.

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
        Initialize Fortianalyzer2Setting endpoint.

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
        endpoint = "/log.fortianalyzer2/setting"
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
        status: str | None = None,
        ips_archive: str | None = None,
        server: str | None = None,
        alt_server: str | None = None,
        fallback_to_primary: str | None = None,
        certificate_verification: str | None = None,
        serial: list | None = None,
        server_cert_ca: str | None = None,
        preshared_key: str | None = None,
        access_config: str | None = None,
        hmac_algorithm: str | None = None,
        enc_algorithm: str | None = None,
        ssl_min_proto_version: str | None = None,
        conn_timeout: int | None = None,
        monitor_keepalive_period: int | None = None,
        monitor_failure_retry_period: int | None = None,
        certificate: str | None = None,
        source_ip: str | None = None,
        upload_option: str | None = None,
        upload_interval: str | None = None,
        upload_day: str | None = None,
        upload_time: str | None = None,
        reliable: str | None = None,
        priority: str | None = None,
        max_log_rate: int | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
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
            status: Enable/disable logging to FortiAnalyzer. (optional)
            ips_archive: Enable/disable IPS packet archive logging. (optional)
            server: The remote FortiAnalyzer. (optional)
            alt_server: Alternate FortiAnalyzer. (optional)
            fallback_to_primary: Enable/disable this FortiGate unit to fallback
            to the primary FortiAnalyzer when it is available. (optional)
            certificate_verification: Enable/disable identity verification of
            FortiAnalyzer by use of certificate. (optional)
            serial: Serial numbers of the FortiAnalyzer. (optional)
            server_cert_ca: Mandatory CA on FortiGate in certificate chain of
            server. (optional)
            preshared_key: Preshared-key used for auto-authorization on
            FortiAnalyzer. (optional)
            access_config: Enable/disable FortiAnalyzer access to configuration
            and data. (optional)
            hmac_algorithm: OFTP login hash algorithm. (optional)
            enc_algorithm: Configure the level of SSL protection for secure
            communication with FortiAnalyzer. (optional)
            ssl_min_proto_version: Minimum supported protocol version for
            SSL/TLS connections (default is to follow system global setting).
            (optional)
            conn_timeout: FortiAnalyzer connection time-out in seconds (for
            status and log buffer). (optional)
            monitor_keepalive_period: Time between OFTP keepalives in seconds
            (for status and log buffer). (optional)
            monitor_failure_retry_period: Time between FortiAnalyzer connection
            retries in seconds (for status and log buffer). (optional)
            certificate: Certificate used to communicate with FortiAnalyzer.
            (optional)
            source_ip: Source IPv4 or IPv6 address used to communicate with
            FortiAnalyzer. (optional)
            upload_option: Enable/disable logging to hard disk and then
            uploading to FortiAnalyzer. (optional)
            upload_interval: Frequency to upload log files to FortiAnalyzer.
            (optional)
            upload_day: Day of week (month) to upload logs. (optional)
            upload_time: Time to upload logs (hh:mm). (optional)
            reliable: Enable/disable reliable logging to FortiAnalyzer.
            (optional)
            priority: Set log transmission priority. (optional)
            max_log_rate: FortiAnalyzer maximum log rate in MBps (0 =
            unlimited). (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
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
        endpoint = "/log.fortianalyzer2/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if ips_archive is not None:
            data_payload["ips-archive"] = ips_archive
        if server is not None:
            data_payload["server"] = server
        if alt_server is not None:
            data_payload["alt-server"] = alt_server
        if fallback_to_primary is not None:
            data_payload["fallback-to-primary"] = fallback_to_primary
        if certificate_verification is not None:
            data_payload["certificate-verification"] = certificate_verification
        if serial is not None:
            data_payload["serial"] = serial
        if server_cert_ca is not None:
            data_payload["server-cert-ca"] = server_cert_ca
        if preshared_key is not None:
            data_payload["preshared-key"] = preshared_key
        if access_config is not None:
            data_payload["access-config"] = access_config
        if hmac_algorithm is not None:
            data_payload["hmac-algorithm"] = hmac_algorithm
        if enc_algorithm is not None:
            data_payload["enc-algorithm"] = enc_algorithm
        if ssl_min_proto_version is not None:
            data_payload["ssl-min-proto-version"] = ssl_min_proto_version
        if conn_timeout is not None:
            data_payload["conn-timeout"] = conn_timeout
        if monitor_keepalive_period is not None:
            data_payload["monitor-keepalive-period"] = monitor_keepalive_period
        if monitor_failure_retry_period is not None:
            data_payload["monitor-failure-retry-period"] = (
                monitor_failure_retry_period
            )
        if certificate is not None:
            data_payload["certificate"] = certificate
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if upload_option is not None:
            data_payload["upload-option"] = upload_option
        if upload_interval is not None:
            data_payload["upload-interval"] = upload_interval
        if upload_day is not None:
            data_payload["upload-day"] = upload_day
        if upload_time is not None:
            data_payload["upload-time"] = upload_time
        if reliable is not None:
            data_payload["reliable"] = reliable
        if priority is not None:
            data_payload["priority"] = priority
        if max_log_rate is not None:
            data_payload["max-log-rate"] = max_log_rate
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
