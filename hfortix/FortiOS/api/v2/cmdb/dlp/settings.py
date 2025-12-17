"""FortiOS CMDB DLP Settings API module.

This module provides methods for managing global DLP settings configuration.

Note: This is a singleton endpoint - settings exist globally and cannot be created or deleted.
Only GET and UPDATE operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient, HTTPResponse


from hfortix.FortiOS.http_client import encode_path_component


class Settings:
    """Manage global DLP settings.

    This class provides methods to retrieve and update global DLP settings configuration.
    Settings are singleton resources (only one instance exists globally).
    """

    def __init__(self, client: "HTTPClient") -> None:
        """Initialize Settings API module.

        Args:
            client: The FortiOS API client instance.
        """
        self._client = client

    def get(self, vdom=None, raw_json: bool = False, **kwargs) -> HTTPResponse:
        """Retrieve current DLP settings.

        Args:
            vdom (str, optional): Virtual domain name. Defaults to 'root' if not specified.
            **kwargs: Additional parameters to pass to the API:
                - format (list): List of property names to include in results
                - with_meta (bool): Include meta information
                - datasource (bool): Include datasource information

        Returns:
            dict: API response containing current DLP settings:
                - config_builder_timeout (int): Maximum time allowed for building
                    a single DLP profile (10-100000 seconds, default 60)

        Example:
            >>> settings = client.cmdb.dlp.settings.get()
            >>> print(f"Timeout: {settings['results']['config-builder-timeout']}")
        """
        return self._client.get("cmdb", "dlp/settings", vdom=vdom, params=kwargs, raw_json=raw_json)

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        raw_json: bool = False,
        config_builder_timeout=None,
        vdom=None,
        **kwargs,
    ) -> HTTPResponse:
        """Update DLP settings.

        Args:
            config_builder_timeout (int, optional): Maximum time allowed for building
                a single DLP profile in seconds. Valid range: 10-100000 (default 60).
            vdom (str, optional): Virtual domain name. Defaults to 'root' if not specified.
            **kwargs: Additional parameters (not commonly used for settings).

        Returns:
            dict: API response containing operation results.

        Raises:
            ValueError: If config_builder_timeout is outside valid range.

        Example:
            >>> # Increase profile build timeout to 120 seconds
            >>> client.cmdb.dlp.settings.update(config_builder_timeout=120)
        """
        data = {}

        if config_builder_timeout is not None:
            if not isinstance(config_builder_timeout, int):
                raise ValueError("config_builder_timeout must be an integer")
            if not (10 <= config_builder_timeout <= 100000):
                raise ValueError("config_builder_timeout must be between 10 and 100000")
            data["config-builder-timeout"] = config_builder_timeout

        return self._client.put("cmdb", "dlp/settings", data, vdom, raw_json=raw_json)
