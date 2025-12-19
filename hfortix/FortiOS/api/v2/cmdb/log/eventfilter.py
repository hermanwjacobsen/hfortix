"""
FortiOS CMDB - Log Eventfilter

API Endpoints:
    GET    /log/eventfilter
    PUT    /log/eventfilter
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Eventfilter:
    """Eventfilter operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Eventfilter endpoint.

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
        endpoint = "/log/eventfilter"
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
        event: str | None = None,
        system: str | None = None,
        vpn: str | None = None,
        user: str | None = None,
        router: str | None = None,
        wireless_activity: str | None = None,
        wan_opt: str | None = None,
        endpoint: str | None = None,
        ha: str | None = None,
        security_rating: str | None = None,
        fortiextender: str | None = None,
        connector: str | None = None,
        sdwan: str | None = None,
        cifs: str | None = None,
        switch_controller: str | None = None,
        rest_api: str | None = None,
        web_svc: str | None = None,
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
            event: Enable/disable event logging. (optional)
            system: Enable/disable system event logging. (optional)
            vpn: Enable/disable VPN event logging. (optional)
            user: Enable/disable user authentication event logging. (optional)
            router: Enable/disable router event logging. (optional)
            wireless_activity: Enable/disable wireless event logging. (optional)
            wan_opt: Enable/disable WAN optimization event logging. (optional)
            endpoint: Enable/disable endpoint event logging. (optional)
            ha: Enable/disable ha event logging. (optional)
            security_rating: Enable/disable Security Rating result logging. (optional)
            fortiextender: Enable/disable FortiExtender logging. (optional)
            connector: Enable/disable SDN connector logging. (optional)
            sdwan: Enable/disable SD-WAN logging. (optional)
            cifs: Enable/disable CIFS logging. (optional)
            switch_controller: Enable/disable Switch-Controller logging. (optional)
            rest_api: Enable/disable REST API logging. (optional)
            web_svc: Enable/disable web-svc performance logging. (optional)
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
        endpoint = "/log/eventfilter"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if event is not None:
            data_payload['event'] = event
        if system is not None:
            data_payload['system'] = system
        if vpn is not None:
            data_payload['vpn'] = vpn
        if user is not None:
            data_payload['user'] = user
        if router is not None:
            data_payload['router'] = router
        if wireless_activity is not None:
            data_payload['wireless-activity'] = wireless_activity
        if wan_opt is not None:
            data_payload['wan-opt'] = wan_opt
        if endpoint is not None:
            data_payload['endpoint'] = endpoint
        if ha is not None:
            data_payload['ha'] = ha
        if security_rating is not None:
            data_payload['security-rating'] = security_rating
        if fortiextender is not None:
            data_payload['fortiextender'] = fortiextender
        if connector is not None:
            data_payload['connector'] = connector
        if sdwan is not None:
            data_payload['sdwan'] = sdwan
        if cifs is not None:
            data_payload['cifs'] = cifs
        if switch_controller is not None:
            data_payload['switch-controller'] = switch_controller
        if rest_api is not None:
            data_payload['rest-api'] = rest_api
        if web_svc is not None:
            data_payload['web-svc'] = web_svc
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
