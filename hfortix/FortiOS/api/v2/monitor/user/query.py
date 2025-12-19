"""Monitor API - Query operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Abort:
    """Abort operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Abort endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        query_id: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Abort a running user device unified query.
        
        Args:
            query_id: Provide a query ID to abort an unified type query. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.user.query.abort.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if query_id is not None:
            data['query_id'] = query_id
        data.update(kwargs)
        return self._client.post("monitor", "/user/query/abort", data=data)


class Query:
    """Query operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Query endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.abort = Abort(client)
