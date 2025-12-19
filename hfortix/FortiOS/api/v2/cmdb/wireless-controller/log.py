"""
FortiOS CMDB - Wireless-controller Log

API Endpoints:
    GET    /wireless-controller/log
    PUT    /wireless-controller/log
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Log:
    """Log operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Log endpoint.

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
        endpoint = "/wireless-controller/log"
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
        addrgrp_log: str | None = None,
        ble_log: str | None = None,
        clb_log: str | None = None,
        dhcp_starv_log: str | None = None,
        led_sched_log: str | None = None,
        radio_event_log: str | None = None,
        rogue_event_log: str | None = None,
        sta_event_log: str | None = None,
        sta_locate_log: str | None = None,
        wids_log: str | None = None,
        wtp_event_log: str | None = None,
        wtp_fips_event_log: str | None = None,
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
            status: Enable/disable wireless event logging. (optional)
            addrgrp_log: Lowest severity level to log address group message. (optional)
            ble_log: Lowest severity level to log BLE detection message. (optional)
            clb_log: Lowest severity level to log client load balancing message. (optional)
            dhcp_starv_log: Lowest severity level to log DHCP starvation event message. (optional)
            led_sched_log: Lowest severity level to log LED schedule event message. (optional)
            radio_event_log: Lowest severity level to log radio event message. (optional)
            rogue_event_log: Lowest severity level to log rogue AP event message. (optional)
            sta_event_log: Lowest severity level to log station event message. (optional)
            sta_locate_log: Lowest severity level to log station locate message. (optional)
            wids_log: Lowest severity level to log WIDS message. (optional)
            wtp_event_log: Lowest severity level to log WTP event message. (optional)
            wtp_fips_event_log: Lowest severity level to log FAP fips event message. (optional)
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
        endpoint = "/wireless-controller/log"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if addrgrp_log is not None:
            data_payload['addrgrp-log'] = addrgrp_log
        if ble_log is not None:
            data_payload['ble-log'] = ble_log
        if clb_log is not None:
            data_payload['clb-log'] = clb_log
        if dhcp_starv_log is not None:
            data_payload['dhcp-starv-log'] = dhcp_starv_log
        if led_sched_log is not None:
            data_payload['led-sched-log'] = led_sched_log
        if radio_event_log is not None:
            data_payload['radio-event-log'] = radio_event_log
        if rogue_event_log is not None:
            data_payload['rogue-event-log'] = rogue_event_log
        if sta_event_log is not None:
            data_payload['sta-event-log'] = sta_event_log
        if sta_locate_log is not None:
            data_payload['sta-locate-log'] = sta_locate_log
        if wids_log is not None:
            data_payload['wids-log'] = wids_log
        if wtp_event_log is not None:
            data_payload['wtp-event-log'] = wtp_event_log
        if wtp_fips_event_log is not None:
            data_payload['wtp-fips-event-log'] = wtp_fips_event_log
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
