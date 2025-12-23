"""
FortiOS MONITOR - Monitor Extender Controller Modem Firmware

Monitoring endpoint for monitor extender controller modem firmware data.

API Endpoints:
    GET    /monitor/extender_controller/modem_firmware

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.extender_controller.modem_firmware.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.extender_controller.modem_firmware.get(
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


class ModemFirmware:
    """
    Modemfirmware Operations.

    Provides read-only access for FortiOS modemfirmware data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient") -> None:
        """
        Initialize ModemFirmware monitor.

        Args:
            client: HTTPClient instance for API communication
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
        Get available modem firmware for a FortiExtender.

        Lists all available modem firmware images on FortiCloud for the
        specified FortiExtender serial number.

        Args:
            serial: FortiExtender serial number (required)
            payload_dict: Dictionary containing parameters (alternative to
            kwargs)
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary with 'current' local firmware and 'available' list

        Examples:
            # Get modem firmware list using serial parameter
            firmware =
            fgt.api.monitor.extender_controller.extender.modem_firmware.get(
                serial='FX201E3X16000024'
            )

            # Get modem firmware list using payload_dict
            firmware =
            fgt.api.monitor.extender_controller.extender.modem_firmware.get(
                payload_dict={'serial': 'FX201E3X16000024'}
            )

            # Response format:
            # {
            #     'current': 'modem_fw_v1.0.0',
            #     'available': ['modem_fw_v1.0.1', 'modem_fw_v1.0.2']
            # }
        """
        params = payload_dict.copy() if payload_dict else {}
        params["serial"] = serial
        params.update(kwargs)

        return self._client.get(
            "monitor",
            "/extender-controller/extender/modem-firmware",
            params=params,
        )
