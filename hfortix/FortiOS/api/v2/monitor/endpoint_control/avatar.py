"""Monitor API - Avatar operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Download:
    """Download operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Download endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        uid: str | None = None,
        user: str | None = None,
        fingerprint: str | None = None,
        default: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Download an endpoint avatar image.
        
        Args:
            uid: Single FortiClient UID. (optional)
            user: User name of the endpoint. (optional)
            fingerprint: Avatar fingerprint. (optional)
            default: Default avatar name ['authuser'|'unauthuser'|'authuser_72'|'unauthuser_72']. Default avatar when endpoint / device avatar is not available. If default is not set, Not found 404 is returned. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.endpoint_control.avatar.download.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if uid is not None:
            params['uid'] = uid
        if user is not None:
            params['user'] = user
        if fingerprint is not None:
            params['fingerprint'] = fingerprint
        if default is not None:
            params['default'] = default
        params.update(kwargs)
        return self._client.get("monitor", "/endpoint-control/avatar/download", params=params)


class Avatar:
    """Avatar operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Avatar endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.download = Download(client)
