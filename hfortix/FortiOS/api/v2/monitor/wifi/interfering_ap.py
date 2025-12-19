"""Monitor API - InterferingAp operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class InterferingAp:
    """InterferingAp operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize InterferingAp endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        wtp: str | None = None,
        radio: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a list of interfering APs for one FortiAP radio.
        
        Args:
            wtp: FortiAP ID to query. (optional)
            radio: Radio ID. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wifi.interfering_ap.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if wtp is not None:
            params['wtp'] = wtp
        if radio is not None:
            params['radio'] = radio
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/interfering_ap", params=params)
