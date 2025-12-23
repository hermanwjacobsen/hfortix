"""
FortiOS CMDB - Cmdb Log Syslogd Setting

Configuration endpoint for managing cmdb log syslogd setting objects.

API Endpoints:
    GET    /cmdb/log/syslogd_setting
    PUT    /cmdb/log/syslogd_setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log.syslogd_setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.log.syslogd_setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.log.syslogd_setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.log.syslogd_setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.log.syslogd_setting.delete(name="item_name")

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


class SyslogdSetting:
    """
    Syslogdsetting Operations.

    Provides CRUD operations for FortiOS syslogdsetting configuration.

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
        Initialize SyslogdSetting endpoint.

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
        endpoint = "/log.syslogd/setting"
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
        server: str | None = None,
        mode: str | None = None,
        port: int | None = None,
        facility: str | None = None,
        source_ip_interface: str | None = None,
        source_ip: str | None = None,
        priority: str | None = None,
        max_log_rate: int | None = None,
        enc_algorithm: str | None = None,
        ssl_min_proto_version: str | None = None,
        certificate: str | None = None,
        custom_field_name: list | None = None,
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
            status: Enable/disable remote syslog logging. (optional)
            server: Address of remote syslog server. (optional)
            mode: Remote syslog logging over UDP/Reliable TCP. (optional)
            port: Server listen port. (optional)
            facility: Remote syslog facility. (optional)
            source_ip_interface: Source interface of syslog. (optional)
            source_ip: Source IP address of syslog. (optional)
            priority: Set log transmission priority. (optional)
            max_log_rate: Syslog maximum log rate in MBps (0 = unlimited).
            (optional)
            enc_algorithm: Enable/disable reliable syslogging with TLS
            encryption. (optional)
            ssl_min_proto_version: Minimum supported protocol version for
            SSL/TLS connections (default is to follow system global setting).
            (optional)
            certificate: Certificate used to communicate with Syslog server.
            (optional)
            custom_field_name: Custom field name for CEF format logging.
            (optional)
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
        endpoint = "/log.syslogd/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if status is not None:
            data_payload["status"] = status
        if server is not None:
            data_payload["server"] = server
        if mode is not None:
            data_payload["mode"] = mode
        if port is not None:
            data_payload["port"] = port
        if facility is not None:
            data_payload["facility"] = facility
        if source_ip_interface is not None:
            data_payload["source-ip-interface"] = source_ip_interface
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if priority is not None:
            data_payload["priority"] = priority
        if max_log_rate is not None:
            data_payload["max-log-rate"] = max_log_rate
        if enc_algorithm is not None:
            data_payload["enc-algorithm"] = enc_algorithm
        if ssl_min_proto_version is not None:
            data_payload["ssl-min-proto-version"] = ssl_min_proto_version
        if certificate is not None:
            data_payload["certificate"] = certificate
        if custom_field_name is not None:
            data_payload["custom-field-name"] = custom_field_name
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
