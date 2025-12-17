"""GTP tunnel monitoring operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class GTP:
    """GTP tunnel monitoring."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize GTP endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Retrieve a list of GTP tunnels.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing GTP tunnel information

        Example:
            >>> fgt.api.monitor.firewall.gtp.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/gtp", params=params)

    def flush(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        tunnel_id: Optional[str] = None,
        apn: Optional[str] = None,
        imsi: Optional[str] = None,
        msisdn: Optional[str] = None,
        ms_addr: Optional[str] = None,
        cteid: Optional[str] = None,
        version: Optional[int] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Flush GTP tunnels.

        Args:
            data_dict: Optional dictionary of parameters
            tunnel_id: Specific tunnel ID to flush
            apn: Access Point Name filter
            imsi: International Mobile Subscriber Identity filter
            msisdn: Mobile Station ISDN Number filter
            ms_addr: Mobile Station address filter
            cteid: Control Plane Tunnel Endpoint Identifier filter
            version: GTP version filter (0, 1, or 2)
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing operation result

        Example:
            >>> # Flush all tunnels
            >>> fgt.api.monitor.firewall.gtp.flush()
            >>> # Flush specific tunnel
            >>> fgt.api.monitor.firewall.gtp.flush(tunnel_id='12345')
        """
        data = data_dict.copy() if data_dict else {}
        if tunnel_id is not None:
            data["tunnel_id"] = tunnel_id
        if apn is not None:
            data["apn"] = apn
        if imsi is not None:
            data["imsi"] = imsi
        if msisdn is not None:
            data["msisdn"] = msisdn
        if ms_addr is not None:
            data["ms_addr"] = ms_addr
        if cteid is not None:
            data["cteid"] = cteid
        if version is not None:
            data["version"] = version
        data.update(kwargs)
        return self._client.post("monitor", "/firewall/gtp/flush", data=data)
