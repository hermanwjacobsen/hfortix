"""
FortiOS MONITOR - Monitor Log Historic Daily Remote Logs

Monitoring endpoint for monitor log historic daily remote logs data.

API Endpoints:
    GET    /monitor/log/historic_daily_remote_logs

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.log.historic_daily_remote_logs.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.log.historic_daily_remote_logs.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    pass


class HistoricDailyRemoteLogs:
    """
    Historicdailyremotelogs Operations.

    Provides read-only access for FortiOS historicdailyremotelogs data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
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
        params["server"] = server
        params.update(kwargs)
        return self._client.get("monitor", "/log/historic-daily-remote-logs", params=params)
