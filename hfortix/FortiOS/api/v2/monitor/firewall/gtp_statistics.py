"""GTP statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class GTPStatistics:
    """GTP statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize GTPStatistics endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        Retrieve statistics for GTP.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing GTP statistics

        Example:
            >>> fgt.api.monitor.firewall.gtp_statistics.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/gtp-statistics", params=params)
