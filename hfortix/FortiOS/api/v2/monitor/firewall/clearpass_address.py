"""ClearPass address management operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ClearpassAddress:
    """ClearPass address management."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize ClearpassAddress endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def add(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        spt: Optional[str] = None,
        endpoint_ip: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Add ClearPass address with SPT (System Posture Token) value.

        Args:
            data_dict: Optional dictionary of parameters
            spt: System Posture Token value
            endpoint_ip: Endpoint IP address
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.clearpass_address.add(
            ...     spt='[Healthy]',
            ...     endpoint_ip='10.1.1.100'
            ... )
        """
        data = data_dict.copy() if data_dict else {}
        if spt is not None:
            data["spt"] = spt
        if endpoint_ip is not None:
            data["endpoint_ip"] = endpoint_ip
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/clearpass-address/add", data=data)

    def delete(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        spt: Optional[str] = None,
        endpoint_ip: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Delete ClearPass address with SPT (System Posture Token) value.

        Args:
            data_dict: Optional dictionary of parameters
            spt: System Posture Token value
            endpoint_ip: Endpoint IP address
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> fgt.api.monitor.firewall.clearpass_address.delete(
            ...     spt='[Healthy]',
            ...     endpoint_ip='10.1.1.100'
            ... )
        """
        data = data_dict.copy() if data_dict else {}
        if spt is not None:
            data["spt"] = spt
        if endpoint_ip is not None:
            data["endpoint_ip"] = endpoint_ip
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/clearpass-address/delete", data=data)
