"""Monitor API - RatingLookup operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Select:
    """Select operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Select endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        url: list | None = None,
        lang: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Lookup FortiGuard rating for a specific URL.
        
        Args:
            url: List of URLs to query. (optional)
            lang: Language for the rating response. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.utm.rating_lookup.select.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if url is not None:
            data['url'] = url
        if lang is not None:
            data['lang'] = lang
        data.update(kwargs)
        return self._client.post("monitor", "/utm/rating-lookup/select", data=data)


class RatingLookup:
    """RatingLookup operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize RatingLookup endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.select = Select(client)
