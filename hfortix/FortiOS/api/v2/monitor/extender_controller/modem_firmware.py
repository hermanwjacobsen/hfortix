"""
FortiExtender Modem Firmware Monitor API

Provides access to FortiExtender modem firmware information.
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ModemFirmware:
    """
    FortiExtender modem firmware monitoring.

    Provides methods to retrieve modem firmware information.

    Example usage:
        # Get modem firmware info
        firmware = fgt.api.monitor.extender_controller.modem_firmware.get(
            fortiextender_name='FX201E3X16000024'
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize ModemFirmware monitor.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client
        self._base_path = "/extender-controller/modem-firmware"

    def get(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        serial: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """
        Get available modem firmware for a FortiExtender.

        Lists all available modem firmware images on FortiCloud for the
        specified FortiExtender serial number.

        Args:
            data_dict: Dictionary containing parameters (alternative to kwargs)
            serial: FortiExtender serial number (required)
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary with 'current' local firmware and 'available' list

        Examples:
            # Get modem firmware list (keyword)
            firmware = fgt.api.monitor.extender_controller.modem_firmware.get(
                serial='FX201E3X16000024'
            )

            # Get modem firmware list (dict)
            firmware = fgt.api.monitor.extender_controller.modem_firmware.get(
                data_dict={'serial': 'FX201E3X16000024'}
            )

            # Response format:
            # {
            #     'current': 'modem_fw_v1.0.0',
            #     'available': ['modem_fw_v1.0.1', 'modem_fw_v1.0.2']
            # }
        """
        params = data_dict.copy() if data_dict else {}

        if serial is not None:
            params["serial"] = serial

        params.update(kwargs)

        return self._client.get("monitor", self._base_path, params=params)

    def __dir__(self):
        """Return list of available attributes."""
        return ["get"]
