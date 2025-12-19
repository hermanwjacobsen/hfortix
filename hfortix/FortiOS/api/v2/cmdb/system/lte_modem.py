"""
FortiOS CMDB - System LteModem

API Endpoints:
    GET    /system/lte-modem
    PUT    /system/lte-modem
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class LteModem:
    """LteModem operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LteModem endpoint.

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
        endpoint = "/system/lte-modem"
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
        extra_init: str | None = None,
        pdptype: str | None = None,
        authtype: str | None = None,
        username: str | None = None,
        passwd: str | None = None,
        apn: str | None = None,
        modem_port: int | None = None,
        mode: str | None = None,
        holddown_timer: int | None = None,
        interface: str | None = None,
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
            status: Enable/disable USB LTE/WIMAX device. (optional)
            extra_init: Extra initialization string for USB LTE/WIMAX devices. (optional)
            pdptype: Packet Data Protocol (PDP) context type. (optional)
            authtype: Authentication type for PDP-IP packet data calls. (optional)
            username: Authentication username for PDP-IP packet data calls. (optional)
            passwd: Authentication password for PDP-IP packet data calls. (optional)
            apn: Login APN string for PDP-IP packet data calls. (optional)
            modem_port: Modem port index (0 - 20). (optional)
            mode: Modem operation mode. (optional)
            holddown_timer: Hold down timer (10 - 60 sec). (optional)
            interface: The interface that the modem is acting as a redundant interface for. (optional)
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
        endpoint = "/system/lte-modem"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if status is not None:
            data_payload['status'] = status
        if extra_init is not None:
            data_payload['extra-init'] = extra_init
        if pdptype is not None:
            data_payload['pdptype'] = pdptype
        if authtype is not None:
            data_payload['authtype'] = authtype
        if username is not None:
            data_payload['username'] = username
        if passwd is not None:
            data_payload['passwd'] = passwd
        if apn is not None:
            data_payload['apn'] = apn
        if modem_port is not None:
            data_payload['modem-port'] = modem_port
        if mode is not None:
            data_payload['mode'] = mode
        if holddown_timer is not None:
            data_payload['holddown-timer'] = holddown_timer
        if interface is not None:
            data_payload['interface'] = interface
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
