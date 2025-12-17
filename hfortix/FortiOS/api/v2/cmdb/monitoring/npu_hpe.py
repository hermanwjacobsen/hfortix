"""
NPU-HPE monitoring endpoint module.

This module provides access to the monitoring/npu-hpe endpoint
for configuring NPU-HPE status monitoring.

API Path: monitoring/npu-hpe
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class NpuHpe:
    """
    Interface for configuring NPU-HPE monitoring settings.

    This class provides methods to manage NPU-HPE (Network Processing Unit -
    High Performance Engine) status monitoring configuration.
    This is a singleton endpoint (GET/PUT only).

    Example usage:
        # Get current NPU-HPE monitoring settings
        settings = fgt.api.cmdb.monitoring.npu_hpe.get()

        # PUT - Update NPU-HPE monitoring settings
        fgt.api.cmdb.monitoring.npu_hpe.update(
            status='enable',
            interval=60
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the NpuHpe instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "monitoring/npu-hpe"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current NPU-HPE monitoring settings.

        Returns:
            Dictionary containing NPU-HPE monitoring settings

        Example:
            >>> result = fgt.api.cmdb.monitoring.npu_hpe.get()
            >>> print(result['status'])
            'enable'
        """
        return self._client.get("cmdb", self._endpoint)

    def put(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        interval: Optional[int] = None,
        multipliers: Optional[list] = None,
        status: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update NPU-HPE monitoring settings.

        Args:
            data_dict: Dictionary with API format parameters
            interval: Monitoring interval in seconds
            multipliers: Monitoring multipliers configuration
            status: Enable/disable NPU-HPE monitoring (enable | disable)
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.monitoring.npu_hpe.update(
            ...     status='enable',
            ...     interval=60
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "interval": "interval",
            "multipliers": "multipliers",
            "status": "status",
        }

        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        payload.update(kwargs)

        return self._client.put("cmdb", self._endpoint, data=payload)
