"""Monitor API - HoldSignatures operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class HoldSignatures:
    """HoldSignatures operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
        """
        Return a list of IPS signatures that are on hold due to active hold time.
        
        Args:
            ips_sensor: Optional filter: Provide the name of the IPS sensor to retrieve only the hold signatures being used by that sensor. (optional)
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
            params['ips_sensor'] = ips_sensor
        params.update(kwargs)
        return self._client.get("monitor", "/ips/hold-signatures", params=params)
