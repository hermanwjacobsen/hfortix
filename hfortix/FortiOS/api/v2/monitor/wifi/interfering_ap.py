"""
FortiOS MONITOR - Monitor Wifi Interfering Ap

Monitoring endpoint for monitor wifi interfering ap data.

API Endpoints:
    GET    /monitor/wifi/interfering_ap

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.interfering_ap.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.interfering_ap.get(
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


class InterferingAp:
    """
    Interferingap Operations.

    Provides read-only access for FortiOS interferingap data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize InterferingAp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        wtp: str | None = None,
        radio: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of interfering APs for one FortiAP radio.

        Args:
            wtp: FortiAP ID to query. (optional)
            radio: Radio ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.interfering_ap.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if wtp is not None:
            params["wtp"] = wtp
        if radio is not None:
            params["radio"] = radio
        params.update(kwargs)
        return self._client.get(
            "monitor", "/wifi/interfering_ap", params=params
        )
