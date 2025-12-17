"""
Log GUI display endpoint module.

This module provides access to the log/gui-display endpoint
for configuring how log messages are displayed on the GUI.

API Path: log/gui-display
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class GuiDisplay:
    """
    Interface for configuring log GUI display settings.

    This class provides methods to manage how log messages are displayed
    on the FortiGate GUI. This is a singleton endpoint (GET/PUT only).

    Example usage:
        # Get current GUI display settings
        settings = fgt.api.cmdb.log.gui_display.get()

        # PUT - Update GUI display settings
        fgt.api.cmdb.log.gui_display.update(
            resolve_hosts='enable',
            resolve_apps='enable'
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the GuiDisplay instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log/gui-display"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current log GUI display settings.

        Returns:
            Dictionary containing GUI display settings

        Example:
            >>> result = fgt.api.cmdb.log.gui_display.get()
            >>> print(result['resolve-hosts'])
            'enable'
        """
        return self._client.get("cmdb", self._endpoint)

    def put(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        fortiview_unscanned_apps: Optional[str] = None,
        resolve_apps: Optional[str] = None,
        resolve_hosts: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update log GUI display settings.

        Args:
            data_dict: Dictionary with API format parameters
            fortiview_unscanned_apps: Enable/disable showing unscanned apps in FortiView
                                     (enable | disable)
            resolve_apps: Enable/disable resolving application names (enable | disable)
            resolve_hosts: Enable/disable resolving host names (enable | disable)
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.log.gui_display.update(
            ...     resolve_hosts='enable',
            ...     resolve_apps='enable',
            ...     fortiview_unscanned_apps='disable'
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "fortiview_unscanned_apps": "fortiview-unscanned-apps",
            "resolve_apps": "resolve-apps",
            "resolve_hosts": "resolve-hosts",
        }

        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        payload.update(kwargs)

        return self._client.put("cmdb", self._endpoint, data=payload)
