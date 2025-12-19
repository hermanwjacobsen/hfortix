"""Monitor API - Members operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Members:
    """Members operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Members endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        interface: Any | None = None,
        zone: str | None = None,
        sla: str | None = None,
        skip_vpn_child: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve interface statistics for each SD-WAN link.
        
        Args:
            interface: Interface name. "interface" param take precedence over "zone" or "sla". If set, will return only return the member that matches the interface. (optional)
            zone: SD-WAN zone name. "zone" param take precedence over "sla". If set, will only return members of the zone. (optional)
            sla: SLA name. If set, will only return members that are participants of the SLA. (optional)
            skip_vpn_child: If set, will skip all VPN child interfaces. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.virtual_wan.members.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if interface is not None:
            params['interface'] = interface
        if zone is not None:
            params['zone'] = zone
        if sla is not None:
            params['sla'] = sla
        if skip_vpn_child is not None:
            params['skip_vpn_child'] = skip_vpn_child
        params.update(kwargs)
        return self._client.get("monitor", "/virtual-wan/members", params=params)
