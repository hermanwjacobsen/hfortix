"""
FortiGate LAN Extension Connector Monitor API

Provides access to FortiGate LAN Extension Connector statistics.
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class FortiGate:
    """
    FortiGate LAN Extension Connector monitoring.

    Provides methods to retrieve statistics for configured FortiGate
    LAN Extension Connectors.

    Example usage:
        # Get all connector statistics
        stats = fgt.api.monitor.extension_controller.fortigate.stats()

        # Get connector statistics (dict)
        stats = fgt.api.monitor.extension_controller.fortigate.stats(
            data_dict={}
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize FortiGate connector monitor.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client
        self._base_path = "/extension-controller/fortigate"

    def stats(self, data_dict: Optional[Dict[str, Any]] = None, **kwargs: Any) -> Any:
        """
        Get FortiGate LAN Extension Connector statistics.

        Retrieves statistics for all configured FortiGate LAN Extension Connectors.

        Args:
            data_dict: Dictionary containing parameters (alternative to kwargs)
            **kwargs: Additional parameters as keyword arguments

        Returns:
            List of FortiGate Connector details with name, ip, status, uptime, port,
            and authorization_status_locked fields

        Examples:
            # Get connector statistics
            stats = fgt.api.monitor.extension_controller.fortigate.stats()

            # Get connector statistics (dict)
            stats = fgt.api.monitor.extension_controller.fortigate.stats(
                data_dict={}
            )

            # Response format:
            # [
            #     {
            #         'name': 'connector1',
            #         'ip': '192.168.1.10',
            #         'status': 'running',
            #         'uptime': 3600,
            #         'port': 443,
            #         'authorization_status_locked': False
            #     }
            # ]
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)

        return self._client.get("monitor", self._base_path, params=params)

    def __dir__(self):
        """Return list of available attributes."""
        return ["stats"]
