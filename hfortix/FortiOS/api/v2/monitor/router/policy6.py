"""Monitor API - Policy6 operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Policy6:
    """Policy6 operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Policy6 endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        count_only: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve a list of active IPv6 policy routes.
        
        Args:
            count_only: Returns the number of IPv6 policy routes only. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.router.policy6.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if count_only is not None:
            params['count_only'] = count_only
        params.update(kwargs)
        return self._client.get("monitor", "/router/policy6", params=params)
