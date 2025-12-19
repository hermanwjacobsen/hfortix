"""Monitor API - Fortianalyzer operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Fortianalyzer:
    """Fortianalyzer operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Fortianalyzer endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        server: str | None = None,
        srcip: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Return FortiAnalyzer/FortiManager log status.
        
        Args:
            scope: Scope from which to test the connectivity of the FortiAnalyzer address [vdom|global]. (optional)
            server: FortiAnalyzer/FortiManager address. (optional)
            srcip: The IP to use to make the request to the FortiAnalyzer [<ip>|auto]. When set to "auto" it will use the FortiGate's routing table to determine the IP to make the request from. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.log.fortianalyzer.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params['scope'] = scope
        if server is not None:
            params['server'] = server
        if srcip is not None:
            params['srcip'] = srcip
        params.update(kwargs)
        return self._client.get("monitor", "/log/fortianalyzer", params=params)
