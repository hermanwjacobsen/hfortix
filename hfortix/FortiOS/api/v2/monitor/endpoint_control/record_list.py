"""Monitor API - RecordList operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class RecordList:
    """RecordList operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize RecordList endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        intf_name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List endpoint records.
        
        Args:
            intf_name: Filter: Name of interface where the endpoint was detected. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.endpoint_control.record_list.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if intf_name is not None:
            params['intf_name'] = intf_name
        params.update(kwargs)
        return self._client.get("monitor", "/endpoint-control/record-list", params=params)
