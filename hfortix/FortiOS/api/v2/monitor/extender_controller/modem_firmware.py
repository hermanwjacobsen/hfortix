"""
FortiExtender Modem Firmware Monitor API

Provides access to FortiExtender modem firmware information.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ModemFirmware:
    """
    FortiExtender modem firmware monitoring.

    Provides methods to retrieve modem firmware information.

    Example usage:
        # Get modem firmware info
        firmware = fgt.api.monitor.extender_controller.extender.modem_firmware.get(
            serial='FX201E3X16000024'
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
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
    ) -> dict[str, Any]:
        """
        Get available modem firmware for a FortiExtender.

        Lists all available modem firmware images on FortiCloud for the
        specified FortiExtender serial number.

        Args:
            serial: FortiExtender serial number (required)
            payload_dict: Dictionary containing parameters (alternative to kwargs)
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary with 'current' local firmware and 'available' list

        Examples:
            # Get modem firmware list using serial parameter
            firmware = fgt.api.monitor.extender_controller.extender.modem_firmware.get(
                serial='FX201E3X16000024'
            )

            # Get modem firmware list using payload_dict
            firmware = fgt.api.monitor.extender_controller.extender.modem_firmware.get(
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

        return self._client.get("monitor", "/extender-controller/extender/modem-firmware", params=params)
