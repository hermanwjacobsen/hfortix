"""
FortiOS CMDB - System LldpNetworkPolicy

API Endpoints:
    GET    /system.lldp/network-policy
    POST   /system.lldp/network-policy
    GET    /system.lldp/network-policy/{name}
    PUT    /system.lldp/network-policy/{name}
    DELETE /system.lldp/network-policy/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class LldpNetworkPolicy:
    """LldpNetworkPolicy operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LldpNetworkPolicy endpoint.

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
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false} (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search value. (optional)
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
        
        # Build endpoint path
        if name:
            endpoint = f"/system.lldp/network-policy/{name}"
        else:
            endpoint = "/system.lldp/network-policy"
        if attr is not None:
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        comment: str | None = None,
        voice: list | None = None,
        voice_signaling: list | None = None,
        guest: list | None = None,
        guest_voice_signaling: list | None = None,
        softphone: list | None = None,
        video_conferencing: list | None = None,
        streaming_video: list | None = None,
        video_signaling: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: LLDP network policy name. (optional)
            comment: Comment. (optional)
            voice: Voice. (optional)
            voice_signaling: Voice signaling. (optional)
            guest: Guest. (optional)
            guest_voice_signaling: Guest Voice Signaling. (optional)
            softphone: Softphone. (optional)
            video_conferencing: Video Conferencing. (optional)
            streaming_video: Streaming Video. (optional)
            video_signaling: Video Signaling. (optional)
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
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/system.lldp/network-policy/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if voice is not None:
            data_payload['voice'] = voice
        if voice_signaling is not None:
            data_payload['voice-signaling'] = voice_signaling
        if guest is not None:
            data_payload['guest'] = guest
        if guest_voice_signaling is not None:
            data_payload['guest-voice-signaling'] = guest_voice_signaling
        if softphone is not None:
            data_payload['softphone'] = softphone
        if video_conferencing is not None:
            data_payload['video-conferencing'] = video_conferencing
        if streaming_video is not None:
            data_payload['streaming-video'] = streaming_video
        if video_signaling is not None:
            data_payload['video-signaling'] = video_signaling
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            name: Object identifier (required)
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
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/system.lldp/network-policy/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        comment: str | None = None,
        voice: list | None = None,
        voice_signaling: list | None = None,
        guest: list | None = None,
        guest_voice_signaling: list | None = None,
        softphone: list | None = None,
        video_conferencing: list | None = None,
        streaming_video: list | None = None,
        video_signaling: list | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: LLDP network policy name. (optional)
            comment: Comment. (optional)
            voice: Voice. (optional)
            voice_signaling: Voice signaling. (optional)
            guest: Guest. (optional)
            guest_voice_signaling: Guest Voice Signaling. (optional)
            softphone: Softphone. (optional)
            video_conferencing: Video Conferencing. (optional)
            streaming_video: Streaming Video. (optional)
            video_signaling: Video Signaling. (optional)
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
        endpoint = "/system.lldp/network-policy"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if comment is not None:
            data_payload['comment'] = comment
        if voice is not None:
            data_payload['voice'] = voice
        if voice_signaling is not None:
            data_payload['voice-signaling'] = voice_signaling
        if guest is not None:
            data_payload['guest'] = guest
        if guest_voice_signaling is not None:
            data_payload['guest-voice-signaling'] = guest_voice_signaling
        if softphone is not None:
            data_payload['softphone'] = softphone
        if video_conferencing is not None:
            data_payload['video-conferencing'] = video_conferencing
        if streaming_video is not None:
            data_payload['streaming-video'] = streaming_video
        if video_signaling is not None:
            data_payload['video-signaling'] = video_signaling
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
