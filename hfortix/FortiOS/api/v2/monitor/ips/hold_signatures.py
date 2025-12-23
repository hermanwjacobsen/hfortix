"""
FortiOS MONITOR - Monitor Ips Hold Signatures

Monitoring endpoint for monitor ips hold signatures data.

API Endpoints:
    GET    /monitor/ips/hold_signatures

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.ips.hold_signatures.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.ips.hold_signatures.get(
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


class HoldSignatures:
    """
    Holdsignatures Operations.

    Provides read-only access for FortiOS holdsignatures data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize HoldSignatures endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ips_sensor: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Return a list of IPS signatures that are on hold due to active hold
        time.

        Args:
            ips_sensor: Optional filter: Provide the name of the IPS sensor to
            retrieve only the hold signatures being used by that sensor.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.ips.hold_signatures.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ips_sensor is not None:
            params["ips_sensor"] = ips_sensor
        params.update(kwargs)
        return self._client.get(
            "monitor", "/ips/hold-signatures", params=params
        )
