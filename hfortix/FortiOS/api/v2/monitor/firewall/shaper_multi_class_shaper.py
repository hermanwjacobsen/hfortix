"""
FortiOS MONITOR - Monitor Firewall Shaper Multi Class Shaper

Monitoring endpoint for monitor firewall shaper multi class shaper data.

API Endpoints:
    GET    /monitor/firewall/shaper_multi_class_shaper

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.firewall.shaper_multi_class_shaper.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.firewall.shaper_multi_class_shaper.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    pass


class ShaperMultiClassShaper:
    """
    Shapermulticlassshaper Operations.

    Provides read-only access for FortiOS shapermulticlassshaper data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
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
