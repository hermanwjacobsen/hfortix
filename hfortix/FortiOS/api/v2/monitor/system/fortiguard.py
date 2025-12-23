"""
FortiOS MONITOR - Monitor System Fortiguard

Monitoring endpoint for monitor system fortiguard data.

API Endpoints:
    GET    /monitor/system/fortiguard

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.fortiguard.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.fortiguard.get(
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


class ClearStatistics:
    """
    Clearstatistics Operations.

    Provides read-only access for FortiOS clearstatistics data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ClearStatistics endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Immediately clear all FortiGuard statistics.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.fortiguard.clear_statistics.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/fortiguard/clear-statistics", data=data
        )


class ManualUpdate:
    """ManualUpdate operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ManualUpdate endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Manually update entitlements.

        Args:
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.fortiguard.manual_update.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/fortiguard/manual-update", data=data
        )


class ServerInfo:
    """ServerInfo operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ServerInfo endpoint.

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
        Get FortiGuard server list and information.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.fortiguard.server_info.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/fortiguard/server-info", params=params
        )


class TestAvailability:
    """TestAvailability operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TestAvailability endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        protocol: str | None = None,
        port: int | None = None,
        service: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Test availability of FortiGuard services.

        Args:
            protocol: Protocol to check. [https | udp | http] (optional)
            port: Port to check. (optional)
            service: Service to check. [emailfilter | webfilter] (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.fortiguard.test_availability.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if protocol is not None:
            data["protocol"] = protocol
        if port is not None:
            data["port"] = port
        if service is not None:
            data["service"] = service
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/fortiguard/test-availability", data=data
        )


class Update:
    """Update operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Update endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Immediately update status for FortiGuard services.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.fortiguard.update.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/fortiguard/update", data=data
        )


class Fortiguard:
    """Fortiguard operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Fortiguard endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.clear_statistics = ClearStatistics(client)
        self.manual_update = ManualUpdate(client)
        self.server_info = ServerInfo(client)
        self.test_availability = TestAvailability(client)
        self.update = Update(client)
