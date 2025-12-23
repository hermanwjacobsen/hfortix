"""
FortiOS MONITOR - Monitor Wifi Spectrum

Monitoring endpoint for monitor wifi spectrum data.

API Endpoints:
    GET    /monitor/wifi/spectrum

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.spectrum.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.spectrum.get(
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


class KeepAlive:
    """
    Keepalive Operations.

    Provides read-only access for FortiOS keepalive data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize KeepAlive endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        wtp_id: str | None = None,
        radio_id: int | None = None,
        duration: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Extend duration of an existing spectrum analysis for a specific
        FortiAP.

        Args:
            wtp_id: FortiAP ID. (optional)
            radio_id: Radio ID. (optional)
            duration: Duration in seconds. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.spectrum.keep_alive.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if wtp_id is not None:
            data["wtp_id"] = wtp_id
        if radio_id is not None:
            data["radio_id"] = radio_id
        if duration is not None:
            data["duration"] = duration
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/spectrum/keep-alive", data=data
        )


class Start:
    """Start operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Start endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        wtp_id: str | None = None,
        radio_id: int | None = None,
        channels: list | None = None,
        duration: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Start spectrum analysis for a specific FortiAP for a duration of time.

        Args:
            wtp_id: FortiAP ID. (optional)
            radio_id: Radio ID. (optional)
            channels: Channels. (optional)
            duration: Duration in seconds. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.spectrum.start.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if wtp_id is not None:
            data["wtp_id"] = wtp_id
        if radio_id is not None:
            data["radio_id"] = radio_id
        if channels is not None:
            data["channels"] = channels
        if duration is not None:
            data["duration"] = duration
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/spectrum/start", data=data)


class Stop:
    """Stop operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Stop endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        wtp_id: str | None = None,
        radio_id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Stop spectrum analysis for a specific FortiAP.

        Args:
            wtp_id: FortiAP ID. (optional)
            radio_id: Radio ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.spectrum.stop.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if wtp_id is not None:
            data["wtp_id"] = wtp_id
        if radio_id is not None:
            data["radio_id"] = radio_id
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/spectrum/stop", data=data)


class Spectrum:
    """Spectrum operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Spectrum endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.keep_alive = KeepAlive(client)
        self.start = Start(client)
        self.stop = Stop(client)

    def get(
        self,
        wtp_id: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve spectrum analysis information for a specific FortiAP.

        Args:
            wtp_id: FortiAP ID to query. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.spectrum.get(wtp_id='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["wtp_id"] = wtp_id
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/spectrum", params=params)
