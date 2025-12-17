"""
FortiExtender Controller Monitor API

This module provides access to FortiExtender monitoring endpoints.
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ExtenderController:
    """
    FortiExtender Controller monitoring.

    Provides methods to monitor and manage FortiExtender devices.

    Example usage:
        # List all FortiExtenders
        extenders = fgt.api.monitor.extender_controller.list()

        # Get specific FortiExtender
        extender = fgt.api.monitor.extender_controller.get(
            fortiextender_name='FX201E...'
        )

        # Get system info only
        system_info = fgt.api.monitor.extender_controller.get(
            fortiextender_name='FX201E...',
            type='system'
        )

        # Run diagnostics
        result = fgt.api.monitor.extender_controller.diagnose(
            fortiextender_name='FX201E...'
        )

        # Upgrade extender
        result = fgt.api.monitor.extender_controller.upgrade(
            fortiextender_name='FX201E...'
        )

        # Get modem firmware info
        firmware = fgt.api.monitor.extender_controller.modem_firmware.get(
            fortiextender_name='FX201E...'
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize ExtenderController monitor.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client
        self._base_path = "/extender-controller"
        self._modem_firmware = None

    def list(
        self, data_dict: Optional[Dict[str, Any]] = None, type: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """
        List all FortiExtender units with statistics.

        Retrieves statistics for all configured FortiExtender units.

        Args:
            data_dict: Dictionary containing parameters (alternative to kwargs)
            type: Statistic type. Options: 'system', 'modem', 'usage', 'last'.
                  If not specified, all types are retrieved.
            **kwargs: Additional parameters as keyword arguments

        Returns:
            List of FortiExtender units with statistics

        Examples:
            # List all extenders (all statistics)
            extenders = fgt.api.monitor.extender_controller.list()

            # List with specific type (keyword)
            extenders = fgt.api.monitor.extender_controller.list(type='system')

            # List with dict parameter
            extenders = fgt.api.monitor.extender_controller.list(
                data_dict={'type': 'modem'}
            )
        """
        params = data_dict.copy() if data_dict else {}

        if type is not None:
            params["type"] = type

        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/extender", params=params)

    def get(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        fortiextender_name: Optional[str] = None,
        type: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """
        Get statistics for a specific FortiExtender unit.

        Retrieves detailed statistics for a specific configured FortiExtender.

        Args:
            data_dict: Dictionary containing parameters (alternative to kwargs)
            fortiextender_name: FortiExtender name to retrieve
            type: Statistic type. Options: 'system', 'modem', 'usage', 'last'.
                  If not specified, all types are retrieved.
            **kwargs: Additional parameters as keyword arguments

        Returns:
            FortiExtender statistics (system, modem, usage info)

        Examples:
            # Get specific extender (all statistics)
            extender = fgt.api.monitor.extender_controller.get(
                fortiextender_name='FX201E3X16000024'
            )

            # Get only system info (keyword)
            system = fgt.api.monitor.extender_controller.get(
                fortiextender_name='FX201E3X16000024',
                type='system'
            )

            # Get modem info (dict)
            modem = fgt.api.monitor.extender_controller.get(
                data_dict={
                    'fortiextender_name': 'FX201E3X16000024',
                    'type': 'modem'
                }
            )
        """
        params = data_dict.copy() if data_dict else {}

        if fortiextender_name is not None:
            params["fortiextender-name"] = fortiextender_name

        if type is not None:
            params["type"] = type

        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/extender", params=params)

    def diagnose(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        id: Optional[str] = None,
        cmd: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """
        Run diagnostic commands on a FortiExtender unit.

        Execute diagnostic commands on the specified FortiExtender.

        Args:
            data_dict: Dictionary containing parameters (alternative to kwargs)
            id: FortiExtender ID
            cmd: Command to execute
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Diagnostic results with 'result' and 'error' fields

        Examples:
            # Run diagnostics (keyword)
            result = fgt.api.monitor.extender_controller.diagnose(
                id='FX201E3X16000024',
                cmd='status'
            )

            # Run diagnostics (dict)
            result = fgt.api.monitor.extender_controller.diagnose(
                data_dict={
                    'id': 'FX201E3X16000024',
                    'cmd': 'status'
                }
            )
        """
        data = data_dict.copy() if data_dict else {}

        if id is not None:
            data["id"] = id

        if cmd is not None:
            data["cmd"] = cmd

        data.update(kwargs)

        return self._client.post("monitor", f"{self._base_path}/extender/diagnose", data=data)

    def upgrade(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        id: Optional[str] = None,
        file_content: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """
        Upgrade a FortiExtender unit.

        Initiates firmware upgrade on the specified FortiExtender.

        Args:
            data_dict: Dictionary containing parameters (alternative to kwargs)
            id: FortiExtender ID to upgrade
            file_content: Base64 encoded firmware file data (no whitespace)
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Upgrade operation status with 'status' and 'error' fields

        Examples:
            # Upgrade extender with firmware file (keyword)
            import base64
            with open('firmware.dat', 'rb') as f:
                file_data = base64.b64encode(f.read()).decode()

            result = fgt.api.monitor.extender_controller.upgrade(
                id='FX201E3X16000024',
                file_content=file_data
            )

            # Upgrade extender (dict)
            result = fgt.api.monitor.extender_controller.upgrade(
                data_dict={
                    'id': 'FX201E3X16000024',
                    'file_content': file_data
                }
            )
        """
        data = data_dict.copy() if data_dict else {}

        if id is not None:
            data["id"] = id

        if file_content is not None:
            data["file_content"] = file_content

        data.update(kwargs)

        return self._client.post("monitor", f"{self._base_path}/extender/upgrade", data=data)

    def reset(
        self, data_dict: Optional[Dict[str, Any]] = None, id: Optional[str] = None, **kwargs: Any
    ) -> Any:
        """
        Reset a FortiExtender unit.

        Resets the specified FortiExtender device.

        Args:
            data_dict: Dictionary containing parameters (alternative to kwargs)
            id: FortiExtender ID to reset
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Reset operation status

        Examples:
            # Reset extender (keyword)
            result = fgt.api.monitor.extender_controller.reset(
                id='FX201E3X16000024'
            )

            # Reset extender (dict)
            result = fgt.api.monitor.extender_controller.reset(
                data_dict={'id': 'FX201E3X16000024'}
            )
        """
        data = data_dict.copy() if data_dict else {}

        if id is not None:
            data["id"] = id

        data.update(kwargs)

        return self._client.post("monitor", f"{self._base_path}/extender/reset", data=data)

    @property
    def modem_firmware(self):
        """
        Access modem firmware sub-endpoint.

        Returns:
            ModemFirmware instance
        """
        if self._modem_firmware is None:
            from .modem_firmware import ModemFirmware

            self._modem_firmware = ModemFirmware(self._client)
        return self._modem_firmware

    def __dir__(self):
        """Return list of available attributes."""
        return ["list", "get", "diagnose", "upgrade", "reset", "modem_firmware"]
