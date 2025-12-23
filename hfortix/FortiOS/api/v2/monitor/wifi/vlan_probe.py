"""
FortiOS MONITOR - Monitor Wifi Vlan Probe

Monitoring endpoint for monitor wifi vlan probe data.

API Endpoints:
    GET    /monitor/wifi/vlan_probe

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.vlan_probe.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.vlan_probe.get(
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


class Start:
    """
    Start Operations.

    Provides read-only access for FortiOS start data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Start endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ap_interface: int | None = None,
        wtp: str | None = None,
        start_vlan_id: int | None = None,
        end_vlan_id: int | None = None,
        retries: int | None = None,
        timeout: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Start a VLAN probe.

        Args:
            ap_interface: FortiAP interface to send the probe on. (optional)
            wtp: FortiAP ID. (optional)
            start_vlan_id: The starting VLAN ID for the probe. (optional)
            end_vlan_id: The ending VLAN ID for the probe. (optional)
            retries: Number of times to retry a probe for a particular VLAN.
            (optional)
            timeout: Timeout duration (in seconds) to wait for a VLAN probe
            response. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.vlan_probe.start.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ap_interface is not None:
            data["ap_interface"] = ap_interface
        if wtp is not None:
            data["wtp"] = wtp
        if start_vlan_id is not None:
            data["start_vlan_id"] = start_vlan_id
        if end_vlan_id is not None:
            data["end_vlan_id"] = end_vlan_id
        if retries is not None:
            data["retries"] = retries
        if timeout is not None:
            data["timeout"] = timeout
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/vlan-probe/start", data=data
        )


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
        ap_interface: int | None = None,
        wtp: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Stop a VLAN probe.

        Args:
            ap_interface: FortiAP interface to send the probe on. (optional)
            wtp: FortiAP ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.vlan_probe.stop.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ap_interface is not None:
            data["ap_interface"] = ap_interface
        if wtp is not None:
            data["wtp"] = wtp
        data.update(kwargs)
        return self._client.post("monitor", "/wifi/vlan-probe/stop", data=data)


class VlanProbe:
    """VlanProbe operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize VlanProbe endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.start = Start(client)
        self.stop = Stop(client)

    def get(
        self,
        ap_interface: int,
        wtp: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve the VLAN probe results.

        Args:
            ap_interface: FortiAP interface to send the probe on. (required)
            wtp: FortiAP ID. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.vlan_probe.get(ap_interface=1,
            wtp='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["ap_interface"] = ap_interface
        params["wtp"] = wtp
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/vlan-probe", params=params)
