"""
FortiOS MONITOR - Monitor Extender Controller Extender

Monitoring endpoint for monitor extender controller extender data.

API Endpoints:
    GET    /monitor/extender_controller/extender

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.extender_controller.extender.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.extender_controller.extender.get(
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


class Diagnose:
    """
    Diagnose Operations.

    Provides read-only access for FortiOS diagnose data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Diagnose endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        id: str | None = None,
        cmd: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Execute diagnotic commands.

        Args:
            id: FortiExtender ID. (optional)
            cmd: Command to execute. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.extender_controller.extender.diagnose.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if id is not None:
            data["id"] = id
        if cmd is not None:
            data["cmd"] = cmd
        data.update(kwargs)
        return self._client.post(
            "monitor", "/extender-controller/extender/diagnose", data=data
        )


class ModemFirmware:
    """ModemFirmware operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ModemFirmware endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        serial: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List all available FortiExtender modem firmware images on FortiCloud.

        Args:
            serial: FortiExtender serial number. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.extender_controller.extender.modem_firmware.get(serial='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["serial"] = serial
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/extender-controller/extender/modem-firmware",
            params=params,
        )


class Reset:
    """Reset operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Reset endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        id: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset a specific FortiExtender unit.

        Args:
            id: FortiExtender ID to reset. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.extender_controller.extender.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if id is not None:
            data["id"] = id
        data.update(kwargs)
        return self._client.post(
            "monitor", "/extender-controller/extender/reset", data=data
        )


class Upgrade:
    """Upgrade operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Upgrade endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        id: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Upgrade FortiExtender.

        Args:
            id: FortiExtender ID to upgrade. (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.extender_controller.extender.upgrade.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if id is not None:
            data["id"] = id
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/extender-controller/extender/upgrade", data=data
        )


class Extender:
    """Extender operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Extender endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.diagnose = Diagnose(client)
        self.modem_firmware = ModemFirmware(client)
        self.reset = Reset(client)
        self.upgrade = Upgrade(client)

    def get(
        self,
        fortiextender_name: Any | None = None,
        type: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve statistics for specific configured FortiExtender units.

        Args:
            fortiextender_name: Filter: single FortiExtender name. Retrieve
            statistics for all configured FortiExtender units unless specified.
            (optional)
            type: Statistic type.'type' options are [system | modem | usage |
            last]. If 'type' is not specified, all types of statistics are
            retrieved. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.extender_controller.extender.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if fortiextender_name is not None:
            params["fortiextender-name"] = fortiextender_name
        if type is not None:
            params["type"] = type
        params.update(kwargs)
        return self._client.get(
            "monitor", "/extender-controller/extender", params=params
        )
