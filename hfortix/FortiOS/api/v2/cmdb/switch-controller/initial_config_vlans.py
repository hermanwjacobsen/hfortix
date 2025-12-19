"""
FortiOS CMDB - Switch-controller InitialConfigVlans

API Endpoints:
    GET    /switch-controller.initial-config/vlans
    PUT    /switch-controller.initial-config/vlans
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class InitialConfigVlans:
    """InitialConfigVlans operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize InitialConfigVlans endpoint.

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
        endpoint = "/switch-controller.initial-config/vlans"
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
        optional_vlans: str | None = None,
        default_vlan: str | None = None,
        quarantine: str | None = None,
        rspan: str | None = None,
        voice: str | None = None,
        video: str | None = None,
        nac: str | None = None,
        nac_segment: str | None = None,
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
            optional_vlans: Auto-generate pre-configured VLANs upon switch discovery. (optional)
            default_vlan: Default VLAN (native) assigned to all switch ports upon discovery. (optional)
            quarantine: VLAN for quarantined traffic. (optional)
            rspan: VLAN for RSPAN/ERSPAN mirrored traffic. (optional)
            voice: VLAN dedicated for voice devices. (optional)
            video: VLAN dedicated for video devices. (optional)
            nac: VLAN for NAC onboarding devices. (optional)
            nac_segment: VLAN for NAC segment primary interface. (optional)
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
        endpoint = "/switch-controller.initial-config/vlans"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if optional_vlans is not None:
            data_payload['optional-vlans'] = optional_vlans
        if default_vlan is not None:
            data_payload['default-vlan'] = default_vlan
        if quarantine is not None:
            data_payload['quarantine'] = quarantine
        if rspan is not None:
            data_payload['rspan'] = rspan
        if voice is not None:
            data_payload['voice'] = voice
        if video is not None:
            data_payload['video'] = video
        if nac is not None:
            data_payload['nac'] = nac
        if nac_segment is not None:
            data_payload['nac-segment'] = nac_segment
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
