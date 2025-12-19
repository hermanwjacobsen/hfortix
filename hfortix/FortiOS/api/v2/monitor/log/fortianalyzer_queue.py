"""Monitor API - FortianalyzerQueue operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class FortianalyzerQueue:
    """FortianalyzerQueue operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize FortianalyzerQueue endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve information on FortiAnalyzer's queue state.
        
        Args:
            scope: Scope from which to retrieve FortiAnalyzer's queue state [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.log.fortianalyzer_queue.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params['scope'] = scope
        params.update(kwargs)
        return self._client.get("monitor", "/log/fortianalyzer-queue", params=params)
