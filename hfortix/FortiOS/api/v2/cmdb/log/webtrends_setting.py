"""
WebTrends setting endpoint module.

This module provides access to the log.webtrends/setting endpoint
for configuring WebTrends server settings.

API Path: log.webtrends/setting
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class WebtrendsSetting:
    """
    Interface for configuring WebTrends server settings.

    This class provides methods to manage WebTrends server configuration.

    Supports three types of parameters:
    - data_dict: Standard dictionary format matching API structure
    - keyword arguments: Python snake_case parameters
    - mixed: Both data_dict and keyword arguments combined

    Example usage:
        # Using keyword arguments (snake_case)
        fgt.api.cmdb.log.webtrends.setting.update(
            status='enable',
            server='192.168.1.100'
        )

        # Using data_dict (hyphenated)
        fgt.api.cmdb.log.webtrends.setting.update(
            data_dict={
                'status': 'enable',
                'server': '192.168.1.100'
            }
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the WebtrendsSetting instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log.webtrends/setting"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current WebTrends server settings.

        Returns:
            Dictionary containing WebTrends server configuration

        Example:
            >>> result = fgt.api.cmdb.log.webtrends.setting.get()
            >>> print(result['status'])
            'enable'
        """
        path = "log.webtrends/setting"
        return self._client.get("cmdb", path)

    def put(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        server: Optional[str] = None,
        status: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update WebTrends server settings.

        Accepts parameters in multiple formats for flexibility:
        1. data_dict with API format (hyphenated keys)
        2. Python snake_case keyword arguments
        3. Both data_dict and kwargs combined

        Args:
            data_dict: Dictionary with API format parameters (hyphenated)
            server: Server name
            status: Enable/disable WebTrends logging (enable | disable)
            **kwargs: Additional parameters in API format (hyphenated)

        Returns:
            Dictionary containing API response

        Example:
            >>> # Using keyword arguments
            >>> fgt.api.cmdb.log.webtrends.setting.update(
            ...     status='enable',
            ...     server='webtrends.example.com'
            ... )

            >>> # Using data_dict
            >>> fgt.api.cmdb.log.webtrends.setting.update(
            ...     data_dict={
            ...         'status': 'enable',
            ...         'server': '192.168.1.100'
            ...     }
            ... )
        """
        # Start with data_dict if provided, otherwise empty dict
        payload = dict(data_dict) if data_dict else {}

        # Map Python parameter names to API format and add to payload
        param_map = {
            "server": "server",
            "status": "status",
        }

        # Add mapped parameters
        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        # Add any additional kwargs
        payload.update(kwargs)

        path = "log.webtrends/setting"
        return self._client.put("cmdb", path, data=payload)
