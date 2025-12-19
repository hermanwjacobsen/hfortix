"""Monitor API - KnownNacDeviceCriteriaList operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class KnownNacDeviceCriteriaList:
    """KnownNacDeviceCriteriaList operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize KnownNacDeviceCriteriaList endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a list of commonly configured NAC devices.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.switch_controller.known_nac_device_criteria_list.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get("monitor", "/switch-controller/known-nac-device-criteria-list", params=params)
