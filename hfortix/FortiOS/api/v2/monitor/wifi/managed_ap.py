"""
FortiOS MONITOR - Monitor Wifi Managed Ap

Monitoring endpoint for monitor wifi managed ap data.

API Endpoints:
    GET    /monitor/wifi/managed_ap

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.managed_ap.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.managed_ap.get(
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


class LedBlink:
    """
    Ledblink Operations.

    Provides read-only access for FortiOS ledblink data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize LedBlink endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        serials: list | None = None,
        blink: bool | None = None,
        duration: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Turn a managed FortiAP's LED blinking on or off.

        Args:
            serials: FortiAP IDs to turn LED blink on/off. (optional)
            blink: True to turn on blinking, false to turn off. (optional)
            duration: Time to blink, in seconds. 0 or omit for indefinite.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.managed_ap.led_blink.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if serials is not None:
            data["serials"] = serials
        if blink is not None:
            data["blink"] = blink
        if duration is not None:
            data["duration"] = duration
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/managed_ap/led-blink", data=data
        )


class Restart:
    """Restart operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Restart endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        wtpname: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Restart a given FortiAP.

        Args:
            wtpname: FortiAP name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.managed_ap.restart.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if wtpname is not None:
            data["wtpname"] = wtpname
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/managed_ap/restart", data=data
        )


class SetStatus:
    """SetStatus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SetStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        wtpname: str | None = None,
        admin: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update administrative state for a given FortiAP (enable or disable
        authorization).

        Args:
            wtpname: FortiAP name. (optional)
            admin: New FortiAP administrative state
            [enable|disable|discovered]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.managed_ap.set_status.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if wtpname is not None:
            data["wtpname"] = wtpname
        if admin is not None:
            data["admin"] = admin
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/managed_ap/set_status", data=data
        )


class ManagedAp:
    """ManagedAp operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ManagedAp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.led_blink = LedBlink(client)
        self.restart = Restart(client)
        self.set_status = SetStatus(client)

    def get(
        self,
        wtp_id: str | None = None,
        incl_local: bool | None = None,
        skip_eos: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of managed FortiAPs.

        Args:
            wtp_id: Filter: single managed FortiAP by ID. (optional)
            incl_local: Enable to include the local FortiWiFi device in the
            results. (optional)
            skip_eos: Skip adding Fortiguard end-of-support data. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.managed_ap.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if wtp_id is not None:
            params["wtp_id"] = wtp_id
        if incl_local is not None:
            params["incl_local"] = incl_local
        if skip_eos is not None:
            params["skip_eos"] = skip_eos
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/managed_ap", params=params)
