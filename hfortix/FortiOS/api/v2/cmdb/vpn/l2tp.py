"""
FortiOS CMDB - Vpn L2tp

API Endpoints:
    GET    /vpn/l2tp
    PUT    /vpn/l2tp
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class L2tp:
    """L2tp operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize L2tp endpoint.

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
        endpoint = "/vpn/l2tp"
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
        eip: str | None = None,
        sip: str | None = None,
        usrgrp: str | None = None,
        enforce_ipsec: str | None = None,
        lcp_echo_interval: int | None = None,
        lcp_max_echo_fails: int | None = None,
        hello_interval: int | None = None,
        compress: str | None = None,
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
            status: Enable/disable FortiGate as a L2TP gateway. (optional)
            eip: End IP. (optional)
            sip: Start IP. (optional)
            usrgrp: User group. (optional)
            enforce_ipsec: Enable/disable IPsec enforcement. (optional)
            lcp_echo_interval: Time in seconds between PPPoE Link Control Protocol (LCP) echo requests. (optional)
            lcp_max_echo_fails: Maximum number of missed LCP echo messages before disconnect. (optional)
            hello_interval: L2TP hello message interval in seconds (0 - 3600 sec, default = 60). (optional)
            compress: Enable/disable data compression. (optional)
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
        endpoint = "/vpn/l2tp"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if eip is not None:
            data_payload['eip'] = eip
        if sip is not None:
            data_payload['sip'] = sip
        if usrgrp is not None:
            data_payload['usrgrp'] = usrgrp
        if enforce_ipsec is not None:
            data_payload['enforce-ipsec'] = enforce_ipsec
        if lcp_echo_interval is not None:
            data_payload['lcp-echo-interval'] = lcp_echo_interval
        if lcp_max_echo_fails is not None:
            data_payload['lcp-max-echo-fails'] = lcp_max_echo_fails
        if hello_interval is not None:
            data_payload['hello-interval'] = hello_interval
        if compress is not None:
            data_payload['compress'] = compress
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
