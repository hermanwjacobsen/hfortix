"""Monitor API - HistoricDailyRemoteLogs operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class HistoricDailyRemoteLogs:
    """HistoricDailyRemoteLogs operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize HistoricDailyRemoteLogs endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        server: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Returns the amount of logs in bytes sent daily to a remote logging service (FortiCloud or FortiAnalyzer).
        
        Args:
            server: Service name [forticloud | fortianalyzer | fortianalyzercloud | nulldevice]. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.log.historic_daily_remote_logs.get(server='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['server'] = server
        params.update(kwargs)
        return self._client.get("monitor", "/log/historic-daily-remote-logs", params=params)
