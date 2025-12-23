"""
FortiOS MONITOR - Monitor System Sandbox

Monitoring endpoint for monitor system sandbox data.

API Endpoints:
    GET    /monitor/system/sandbox

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.sandbox.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.sandbox.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class CloudRegions:
    """
    Cloudregions Operations.

    Provides read-only access for FortiOS cloudregions data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CloudRegions endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of FortiSandbox cloud regions.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sandbox.cloud_regions.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/sandbox/cloud-regions", params=params
        )


class Connection:
    """Connection operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Connection endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        server: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Test the connection to FortiSandbox.

        Args:
            server: IP/FQDN of the FortiSandbox to test. Uses the configured
            FortiSandbox IP/FQDN if no server is provided. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sandbox.connection.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if server is not None:
            params["server"] = server
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/sandbox/connection", params=params
        )


class Detect:
    """Detect operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Detect endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve sandbox serial number and connection status.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sandbox.detect.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/sandbox/detect", params=params
        )


class Stats:
    """Stats operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Stats endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve sandbox statistics.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sandbox.stats.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/sandbox/stats", params=params
        )


class Status:
    """Status operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Status endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve sandbox status.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sandbox.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/sandbox/status", params=params
        )


class Sandbox:
    """Sandbox operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Sandbox endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.cloud_regions = CloudRegions(client)
        self.connection = Connection(client)
        self.detect = Detect(client)
        self.stats = Stats(client)
        self.status = Status(client)
