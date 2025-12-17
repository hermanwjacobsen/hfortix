"""Multi-class traffic shaper statistics operations."""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ShaperMultiClassShaper:
    """Multi-class shaper statistics."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize ShaperMultiClassShaper endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def list(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs) -> Dict[str, Any]:
        """
        List of statistics for multi-class shapers.

        Args:
            data_dict: Optional dictionary of parameters
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing multi-class shaper statistics

        Example:
            >>> fgt.api.monitor.firewall.shaper_multi_class_shaper.list()
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/firewall/shaper/multi-class-shaper", params=params)
