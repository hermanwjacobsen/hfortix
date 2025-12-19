"""Monitor API - ForticareResellers operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ForticareResellers:
    """ForticareResellers operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize ForticareResellers endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        country_code: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get current FortiCare resellers for the requested country.
        
        Args:
            country_code: FortiGuard country code (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.license.forticare_resellers.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if country_code is not None:
            params['country_code'] = country_code
        params.update(kwargs)
        return self._client.get("monitor", "/license/forticare-resellers", params=params)
