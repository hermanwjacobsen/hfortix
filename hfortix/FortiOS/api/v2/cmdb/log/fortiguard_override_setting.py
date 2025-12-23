"""
FortiOS CMDB - Cmdb Log Fortiguard Override Setting

Configuration endpoint for managing cmdb log fortiguard override setting
objects.

API Endpoints:
    GET    /cmdb/log/fortiguard_override_setting
    PUT    /cmdb/log/fortiguard_override_setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.log.fortiguard_override_setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.log.fortiguard_override_setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.log.fortiguard_override_setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.log.fortiguard_override_setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.log.fortiguard_override_setting.delete(name="item_name")

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


class FortiguardOverrideSetting:
    """
    Fortiguardoverridesetting Operations.

    Provides CRUD operations for FortiOS fortiguardoverridesetting
    configuration.

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
        Initialize FortiguardOverrideSetting endpoint.

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
        endpoint = "/log.fortiguard/override-setting"
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
        override: str | None = None,
        status: str | None = None,
        upload_option: str | None = None,
        upload_interval: str | None = None,
        upload_day: str | None = None,
        upload_time: str | None = None,
        priority: str | None = None,
        max_log_rate: int | None = None,
        access_config: str | None = None,
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
            override: Overriding FortiCloud settings for this VDOM or use
            global settings. (optional)
            status: Enable/disable logging to FortiCloud. (optional)
            upload_option: Configure how log messages are sent to FortiCloud.
            (optional)
            upload_interval: Frequency of uploading log files to FortiCloud.
            (optional)
            upload_day: Day of week to roll logs. (optional)
            upload_time: Time of day to roll logs (hh:mm). (optional)
            priority: Set log transmission priority. (optional)
            max_log_rate: FortiCloud maximum log rate in MBps (0 = unlimited).
            (optional)
            access_config: Enable/disable FortiCloud access to configuration
            and data. (optional)
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
        endpoint = "/log.fortiguard/override-setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if override is not None:
            data_payload["override"] = override
        if status is not None:
            data_payload["status"] = status
        if upload_option is not None:
            data_payload["upload-option"] = upload_option
        if upload_interval is not None:
            data_payload["upload-interval"] = upload_interval
        if upload_day is not None:
            data_payload["upload-day"] = upload_day
        if upload_time is not None:
            data_payload["upload-time"] = upload_time
        if priority is not None:
            data_payload["priority"] = priority
        if max_log_rate is not None:
            data_payload["max-log-rate"] = max_log_rate
        if access_config is not None:
            data_payload["access-config"] = access_config
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
