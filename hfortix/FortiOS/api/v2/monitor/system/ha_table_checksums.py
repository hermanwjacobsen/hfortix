"""Monitor API - HaTableChecksums operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class HaTableChecksums:
    """HaTableChecksums operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize HaTableChecksums endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        serial_no: str,
        vdom_name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        List of table checksums for members of HA cluster.
        
        Args:
            serial_no: Serial number of the HA member. (required)
            vdom_name: VDOM name of the HA member. If not specified, fetch table checksums for global. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.ha_table_checksums.get(serial_no='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['serial_no'] = serial_no
        if vdom_name is not None:
            params['vdom_name'] = vdom_name
        params.update(kwargs)
        return self._client.get("monitor", "/system/ha-table-checksums", params=params)
