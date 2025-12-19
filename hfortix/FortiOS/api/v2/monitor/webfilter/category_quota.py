"""Monitor API - CategoryQuota operations."""

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
        profile: str | None = None,
        user: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Reset webfilter quota for user or IP.
        
        Args:
            profile: Webfilter profile to reset. (optional)
            user: User or IP to reset with. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.webfilter.category_quota.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if profile is not None:
            data['profile'] = profile
        if user is not None:
            data['user'] = user
        data.update(kwargs)
        return self._client.post("monitor", "/webfilter/category-quota/reset", data=data)


class CategoryQuota:
    """CategoryQuota operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize CategoryQuota endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.reset = Reset(client)

    def get(
        self,
        profile: str | None = None,
        user: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve quota usage statistics for webfilter categories.
        
        Args:
            profile: Webfilter profile. (optional)
            user: User or IP (required if profile specified). (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.webfilter.category_quota.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if profile is not None:
            params['profile'] = profile
        if user is not None:
            params['user'] = user
        params.update(kwargs)
        return self._client.get("monitor", "/webfilter/category-quota", params=params)
