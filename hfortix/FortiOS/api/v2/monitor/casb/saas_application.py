"""Monitor API - SaasApplication operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Details:
    """Details operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Details endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve details for CASB SaaS applications.
        
        Args:
            mkey: Filter: Key of the application to be fetched (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.casb.saas_application.details.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params['mkey'] = mkey
        params.update(kwargs)
        return self._client.get("monitor", "/casb/saas-application/details", params=params)


class SaasApplication:
    """SaasApplication operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize SaasApplication endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.details = Details(client)
