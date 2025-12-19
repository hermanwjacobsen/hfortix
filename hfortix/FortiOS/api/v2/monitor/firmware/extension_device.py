"""Monitor API - ExtensionDevice operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ExtensionDevice:
    """ExtensionDevice operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ExtensionDevice endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        type: str,
        timeout: int | None = None,
        version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a list of recommended firmwares for the specified extension device type.
        
        Args:
            type: Extension device type to get recommended firmwares for. [fortiswitch|fortiap|fortiextender] (required)
            timeout: FortiGuard connection timeout. (optional)
            version: Target firmware version of the parent FortiGate. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.firmware.extension_device.get(type='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['type'] = type
        if timeout is not None:
            params['timeout'] = timeout
        if version is not None:
            params['version'] = version
        params.update(kwargs)
        return self._client.get("monitor", "/firmware/extension-device", params=params)
