"""
Endpoint Control Installer endpoint

GET /api/v2/monitor/endpoint-control/installer
GET /api/v2/monitor/endpoint-control/installer/download
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Installer"]


class Installer:
    """
    Endpoint Control Installer operations.

    List and download FortiClient installers via FortiGuard.
    """

    def __init__(self, client: "HTTPClient"):
        """
        Initialize Installer endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._base_path = "endpoint-control/installer"

    def list(
        self, data_dict: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> dict[str, Any] | list[dict]:
        """
        List available FortiClient installers.

        Retrieve list of FortiClient installers available for download
        from FortiGuard, including version information and platform details.

        Args:
            data_dict: Dictionary containing query parameters
            **kwargs: Additional query parameters

        Returns:
            dict or list: Available FortiClient installers

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # List all available installers
            >>> installers = fgt.api.monitor.endpoint_control.installer.list()
            >>> for installer in installers:
            ...     print(f"{installer.get('platform')}: {installer.get('version')}")

            >>> # List with filters using dict
            >>> installers = fgt.api.monitor.endpoint_control.installer.list(
            ...     data_dict={'platform': 'windows'}
            ... )

        Note:
            Requires FortiGuard connection to retrieve installer list.
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)

        return self._client.get("monitor", self._base_path, params=params)

    def download(
        self, data_dict: Optional[dict[str, Any]] = None, id: Optional[str] = None, **kwargs: Any
    ) -> bytes:
        """
        Download a FortiClient installer via FortiGuard.

        Download a specific FortiClient installer package from FortiGuard.

        Args:
            data_dict: Dictionary containing query parameters
            id: Installer ID to download
            **kwargs: Additional query parameters

        Returns:
            bytes: Installer file content

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Download specific installer using dict
            >>> installer_data = fgt.api.monitor.endpoint_control.installer.download(
            ...     data_dict={'id': 'FCT_7.0.1_WIN_x64'}
            ... )
            >>> with open('forticlient.exe', 'wb') as f:
            ...     f.write(installer_data)

            >>> # Download using keyword argument
            >>> installer_data = fgt.api.monitor.endpoint_control.installer.download(
            ...     id='FCT_7.0.1_WIN_x64'
            ... )

        Note:
            - Requires FortiGuard connection
            - Large file download - may take time
            - Returns binary data, not JSON
        """
        params = data_dict.copy() if data_dict else {}

        if id is not None:
            params["id"] = id

        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/download", params=params)
