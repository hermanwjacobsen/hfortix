"""
FortiOS MONITOR - Monitor User Query

Monitoring endpoint for monitor user query data.

API Endpoints:
    GET    /monitor/user/query

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.query.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.query.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    pass


class Abort:
    """
    Abort Operations.

    Provides read-only access for FortiOS abort data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
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
            data["query_id"] = query_id
        data.update(kwargs)
        return self._client.post("monitor", "/user/query/abort", data=data)


class Query:
    """Query operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Query endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.abort = Abort(client)
