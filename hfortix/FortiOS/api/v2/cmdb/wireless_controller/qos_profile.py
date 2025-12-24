"""
FortiOS CMDB - Cmdb Wireless Controller Qos Profile

Configuration endpoint for managing cmdb wireless controller qos profile
objects.

API Endpoints:
    GET    /cmdb/wireless-controller/qos_profile
    POST   /cmdb/wireless-controller/qos_profile
    GET    /cmdb/wireless-controller/qos_profile
    PUT    /cmdb/wireless-controller/qos_profile/{identifier}
    DELETE /cmdb/wireless-controller/qos_profile/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.wireless_controller.qos_profile.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item =
    fgt.api.cmdb.wireless_controller.qos_profile.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.wireless_controller.qos_profile.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.wireless_controller.qos_profile.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result =
    fgt.api.cmdb.wireless_controller.qos_profile.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union, cast

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class QosProfile:
    """
    Qosprofile Operations.

    Provides CRUD operations for FortiOS qosprofile configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects
        put(): Update existing configuration objects
        delete(): Remove configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize QosProfile endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
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

        # Build endpoint path
        if name:
            endpoint = f"/wireless-controller/qos-profile/{name}"
        else:
            endpoint = "/wireless-controller/qos-profile"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        comment: str | None = None,
        uplink: int | None = None,
        downlink: int | None = None,
        uplink_sta: int | None = None,
        downlink_sta: int | None = None,
        burst: str | None = None,
        wmm: str | None = None,
        wmm_uapsd: str | None = None,
        call_admission_control: str | None = None,
        call_capacity: int | None = None,
        bandwidth_admission_control: str | None = None,
        bandwidth_capacity: int | None = None,
        dscp_wmm_mapping: str | None = None,
        dscp_wmm_vo: list | None = None,
        dscp_wmm_vi: list | None = None,
        dscp_wmm_be: list | None = None,
        dscp_wmm_bk: list | None = None,
        wmm_dscp_marking: str | None = None,
        wmm_vo_dscp: int | None = None,
        wmm_vi_dscp: int | None = None,
        wmm_be_dscp: int | None = None,
        wmm_bk_dscp: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            name: WiFi QoS profile name. (optional)
            comment: Comment. (optional)
            uplink: Maximum uplink bandwidth for Virtual Access Points (VAPs)
            (0 - 2097152 Kbps, default = 0, 0 means no limit). (optional)
            downlink: Maximum downlink bandwidth for Virtual Access Points
            (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            (optional)
            uplink_sta: Maximum uplink bandwidth for clients (0 - 2097152 Kbps,
            default = 0, 0 means no limit). (optional)
            downlink_sta: Maximum downlink bandwidth for clients (0 - 2097152
            Kbps, default = 0, 0 means no limit). (optional)
            burst: Enable/disable client rate burst. (optional)
            wmm: Enable/disable WiFi multi-media (WMM) control. (optional)
            wmm_uapsd: Enable/disable WMM Unscheduled Automatic Power Save
            Delivery (U-APSD) power save mode. (optional)
            call_admission_control: Enable/disable WMM call admission control.
            (optional)
            call_capacity: Maximum number of Voice over WLAN (VoWLAN) phones
            allowed (0 - 60, default = 10). (optional)
            bandwidth_admission_control: Enable/disable WMM bandwidth admission
            control. (optional)
            bandwidth_capacity: Maximum bandwidth capacity allowed (1 - 600000
            Kbps, default = 2000). (optional)
            dscp_wmm_mapping: Enable/disable Differentiated Services Code Point
            (DSCP) mapping. (optional)
            dscp_wmm_vo: DSCP mapping for voice access (default = 48 56).
            (optional)
            dscp_wmm_vi: DSCP mapping for video access (default = 32 40).
            (optional)
            dscp_wmm_be: DSCP mapping for best effort access (default = 0 24).
            (optional)
            dscp_wmm_bk: DSCP mapping for background access (default = 8 16).
            (optional)
            wmm_dscp_marking: Enable/disable WMM Differentiated Services Code
            Point (DSCP) marking. (optional)
            wmm_vo_dscp: DSCP marking for voice access (default = 48).
            (optional)
            wmm_vi_dscp: DSCP marking for video access (default = 32).
            (optional)
            wmm_be_dscp: DSCP marking for best effort access (default = 0).
            (optional)
            wmm_bk_dscp: DSCP marking for background access (default = 8).
            (optional)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/wireless-controller/qos-profile/{name}"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if uplink is not None:
            data_payload["uplink"] = uplink
        if downlink is not None:
            data_payload["downlink"] = downlink
        if uplink_sta is not None:
            data_payload["uplink-sta"] = uplink_sta
        if downlink_sta is not None:
            data_payload["downlink-sta"] = downlink_sta
        if burst is not None:
            data_payload["burst"] = burst
        if wmm is not None:
            data_payload["wmm"] = wmm
        if wmm_uapsd is not None:
            data_payload["wmm-uapsd"] = wmm_uapsd
        if call_admission_control is not None:
            data_payload["call-admission-control"] = call_admission_control
        if call_capacity is not None:
            data_payload["call-capacity"] = call_capacity
        if bandwidth_admission_control is not None:
            data_payload["bandwidth-admission-control"] = (
                bandwidth_admission_control
            )
        if bandwidth_capacity is not None:
            data_payload["bandwidth-capacity"] = bandwidth_capacity
        if dscp_wmm_mapping is not None:
            data_payload["dscp-wmm-mapping"] = dscp_wmm_mapping
        if dscp_wmm_vo is not None:
            data_payload["dscp-wmm-vo"] = dscp_wmm_vo
        if dscp_wmm_vi is not None:
            data_payload["dscp-wmm-vi"] = dscp_wmm_vi
        if dscp_wmm_be is not None:
            data_payload["dscp-wmm-be"] = dscp_wmm_be
        if dscp_wmm_bk is not None:
            data_payload["dscp-wmm-bk"] = dscp_wmm_bk
        if wmm_dscp_marking is not None:
            data_payload["wmm-dscp-marking"] = wmm_dscp_marking
        if wmm_vo_dscp is not None:
            data_payload["wmm-vo-dscp"] = wmm_vo_dscp
        if wmm_vi_dscp is not None:
            data_payload["wmm-vi-dscp"] = wmm_vi_dscp
        if wmm_be_dscp is not None:
            data_payload["wmm-be-dscp"] = wmm_be_dscp
        if wmm_bk_dscp is not None:
            data_payload["wmm-bk-dscp"] = wmm_bk_dscp
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete this specific resource.

        Args:
            name: Object identifier (required)
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

        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/wireless-controller/qos-profile/{name}"
        params.update(kwargs)
        return self._client.delete(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def exists(
        self,
        name: str,
        vdom: str | bool | None = None,
    ) -> Union[bool, Coroutine[Any, Any, bool]]:
        """
        Check if an object exists.

        Args:
            name: Object identifier
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.

        Returns:
            True if object exists, False otherwise

        Example:
            >>> if fgt.api.cmdb.firewall.address.exists("server1"):
            ...     print("Address exists")
        """
        import inspect

        from hfortix.FortiOS.exceptions_forti import ResourceNotFoundError

        # Call get() - returns dict (sync) or coroutine (async)
        result = self.get(name=name, vdom=vdom)

        # Check if async mode
        if inspect.iscoroutine(result):

            async def _async():
                try:
                    # Runtime check confirms result is a coroutine, cast for
                    # mypy
                    await cast(Coroutine[Any, Any, dict[str, Any]], result)
                    return True
                except ResourceNotFoundError:
                    return False

            # Type ignore justified: mypy can't verify Union return type
            # narrowing

            return _async()
        # Sync mode - get() already executed, no exception means it exists
        return True

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        uplink: int | None = None,
        downlink: int | None = None,
        uplink_sta: int | None = None,
        downlink_sta: int | None = None,
        burst: str | None = None,
        wmm: str | None = None,
        wmm_uapsd: str | None = None,
        call_admission_control: str | None = None,
        call_capacity: int | None = None,
        bandwidth_admission_control: str | None = None,
        bandwidth_capacity: int | None = None,
        dscp_wmm_mapping: str | None = None,
        dscp_wmm_vo: list | None = None,
        dscp_wmm_vi: list | None = None,
        dscp_wmm_be: list | None = None,
        dscp_wmm_bk: list | None = None,
        wmm_dscp_marking: str | None = None,
        wmm_vo_dscp: int | None = None,
        wmm_vi_dscp: int | None = None,
        wmm_be_dscp: int | None = None,
        wmm_bk_dscp: int | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: WiFi QoS profile name. (optional)
            comment: Comment. (optional)
            uplink: Maximum uplink bandwidth for Virtual Access Points (VAPs)
            (0 - 2097152 Kbps, default = 0, 0 means no limit). (optional)
            downlink: Maximum downlink bandwidth for Virtual Access Points
            (VAPs) (0 - 2097152 Kbps, default = 0, 0 means no limit).
            (optional)
            uplink_sta: Maximum uplink bandwidth for clients (0 - 2097152 Kbps,
            default = 0, 0 means no limit). (optional)
            downlink_sta: Maximum downlink bandwidth for clients (0 - 2097152
            Kbps, default = 0, 0 means no limit). (optional)
            burst: Enable/disable client rate burst. (optional)
            wmm: Enable/disable WiFi multi-media (WMM) control. (optional)
            wmm_uapsd: Enable/disable WMM Unscheduled Automatic Power Save
            Delivery (U-APSD) power save mode. (optional)
            call_admission_control: Enable/disable WMM call admission control.
            (optional)
            call_capacity: Maximum number of Voice over WLAN (VoWLAN) phones
            allowed (0 - 60, default = 10). (optional)
            bandwidth_admission_control: Enable/disable WMM bandwidth admission
            control. (optional)
            bandwidth_capacity: Maximum bandwidth capacity allowed (1 - 600000
            Kbps, default = 2000). (optional)
            dscp_wmm_mapping: Enable/disable Differentiated Services Code Point
            (DSCP) mapping. (optional)
            dscp_wmm_vo: DSCP mapping for voice access (default = 48 56).
            (optional)
            dscp_wmm_vi: DSCP mapping for video access (default = 32 40).
            (optional)
            dscp_wmm_be: DSCP mapping for best effort access (default = 0 24).
            (optional)
            dscp_wmm_bk: DSCP mapping for background access (default = 8 16).
            (optional)
            wmm_dscp_marking: Enable/disable WMM Differentiated Services Code
            Point (DSCP) marking. (optional)
            wmm_vo_dscp: DSCP marking for voice access (default = 48).
            (optional)
            wmm_vi_dscp: DSCP marking for video access (default = 32).
            (optional)
            wmm_be_dscp: DSCP marking for best effort access (default = 0).
            (optional)
            wmm_bk_dscp: DSCP marking for background access (default = 8).
            (optional)
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
        endpoint = "/wireless-controller/qos-profile"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if comment is not None:
            data_payload["comment"] = comment
        if uplink is not None:
            data_payload["uplink"] = uplink
        if downlink is not None:
            data_payload["downlink"] = downlink
        if uplink_sta is not None:
            data_payload["uplink-sta"] = uplink_sta
        if downlink_sta is not None:
            data_payload["downlink-sta"] = downlink_sta
        if burst is not None:
            data_payload["burst"] = burst
        if wmm is not None:
            data_payload["wmm"] = wmm
        if wmm_uapsd is not None:
            data_payload["wmm-uapsd"] = wmm_uapsd
        if call_admission_control is not None:
            data_payload["call-admission-control"] = call_admission_control
        if call_capacity is not None:
            data_payload["call-capacity"] = call_capacity
        if bandwidth_admission_control is not None:
            data_payload["bandwidth-admission-control"] = (
                bandwidth_admission_control
            )
        if bandwidth_capacity is not None:
            data_payload["bandwidth-capacity"] = bandwidth_capacity
        if dscp_wmm_mapping is not None:
            data_payload["dscp-wmm-mapping"] = dscp_wmm_mapping
        if dscp_wmm_vo is not None:
            data_payload["dscp-wmm-vo"] = dscp_wmm_vo
        if dscp_wmm_vi is not None:
            data_payload["dscp-wmm-vi"] = dscp_wmm_vi
        if dscp_wmm_be is not None:
            data_payload["dscp-wmm-be"] = dscp_wmm_be
        if dscp_wmm_bk is not None:
            data_payload["dscp-wmm-bk"] = dscp_wmm_bk
        if wmm_dscp_marking is not None:
            data_payload["wmm-dscp-marking"] = wmm_dscp_marking
        if wmm_vo_dscp is not None:
            data_payload["wmm-vo-dscp"] = wmm_vo_dscp
        if wmm_vi_dscp is not None:
            data_payload["wmm-vi-dscp"] = wmm_vi_dscp
        if wmm_be_dscp is not None:
            data_payload["wmm-be-dscp"] = wmm_be_dscp
        if wmm_bk_dscp is not None:
            data_payload["wmm-bk-dscp"] = wmm_bk_dscp
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
