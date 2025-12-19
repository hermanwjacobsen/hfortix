"""Monitor API - HistoricalStatistics operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class HistoricalStatistics:
    """HistoricalStatistics operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize HistoricalStatistics endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        filter: str | None = None,
        sessionid: int | None = None,
        device: str | None = None,
        report_by: str | None = None,
        sort_by: str | None = None,
        chart_only: bool | None = None,
        end: int | None = None,
        ip_version: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve historical drill-down and summary data for FortiView.
        
        Args:
            filter: A map of filter keys to arrays of values. (optional)
            sessionid: FortiView request Session ID. (optional)
            device: FortiView source device [disk|fortianalyzer|forticloud]. (optional)
            report_by: Report by field. (optional)
            sort_by: Sort by field. (optional)
            chart_only: Only return graph values in results. (optional)
            end: End timestamp. (optional)
            ip_version: IP version [*ipv4 | ipv6 | ipboth]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.fortiview.historical_statistics.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if filter is not None:
            params['filter'] = filter
        if sessionid is not None:
            params['sessionid'] = sessionid
        if device is not None:
            params['device'] = device
        if report_by is not None:
            params['report_by'] = report_by
        if sort_by is not None:
            params['sort_by'] = sort_by
        if chart_only is not None:
            params['chart_only'] = chart_only
        if end is not None:
            params['end'] = end
        if ip_version is not None:
            params['ip_version'] = ip_version
        params.update(kwargs)
        return self._client.get("monitor", "/fortiview/historical-statistics", params=params)
