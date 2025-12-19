"""Monitor API - HscalefwLicense operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Upload:
    """Upload operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Upload endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        license_key: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update Hyperscale firewall license for hardware acceleration using license key.
        
        Args:
            license_key: License key. Format:0000-0000-0000-0000-0000-0000-00. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments
        
        Returns:
            Dictionary containing API response
        
        Example:
            >>> fgt.api.monitor.system.hscalefw_license.upload.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if license_key is not None:
            data['license_key'] = license_key
        data.update(kwargs)
        return self._client.post("monitor", "/system/hscalefw-license/upload", data=data)


class HscalefwLicense:
    """HscalefwLicense operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize HscalefwLicense endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.upload = Upload(client)
