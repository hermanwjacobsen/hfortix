"""Monitor API - History operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Reset:
    """Reset operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Reset endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Reset WAN opt.
        
        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wanopt.history.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        data.update(kwargs)
        return self._client.post("monitor", "/wanopt/history/reset", data=data)


class History:
    """History operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize History endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.reset = Reset(client)

    def get(
        self,
        period: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve WAN opt.
        
        Args:
            period: Statistics period [10-min*|hour|day|week|30-day]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.wanopt.history.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if period is not None:
            params['period'] = period
        params.update(kwargs)
        return self._client.get("monitor", "/wanopt/history", params=params)
