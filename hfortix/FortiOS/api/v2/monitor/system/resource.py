"""Monitor API - Resource operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Usage:
    """Usage operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Usage endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        resource: str | None = None,
        interval: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retreive current and historical usage data for a provided resource.
        
        Args:
            scope: Scope of resource [vdom|global]. This parameter is only applicable if the FGT is in VDOM mode. (optional)
            resource: Resource to get usage data for [cpu|mem|disk|session|session6|setuprate|setuprate6|disk_lograte|faz_lograte|forticloud_lograte|gtp_tunnel|gtp_tunnel_setup_rate]. Defaults to all resources if not provided. Additionally, [npu_session|npu_session6] data is available for devices that have an NPU and [nturbo_session|nturbo_session6] data is available for NP6 devices that support NTurbo. [gtp_tunnel|gtp_tunnel_setup_rate] data is available for carrier platforms only. (optional)
            interval: Time interval of resource usage [1-min|10-min|30-min|1-hour|12-hour|24-hour]. Defaults to all intervals if not provided. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.resource.usage.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params['scope'] = scope
        if resource is not None:
            params['resource'] = resource
        if interval is not None:
            params['interval'] = interval
        params.update(kwargs)
        return self._client.get("monitor", "/system/resource/usage", params=params)


class Resource:
    """Resource operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Resource endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.usage = Usage(client)
