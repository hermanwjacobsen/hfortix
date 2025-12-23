"""
FortiOS MONITOR - Monitor Wifi Region Image

Monitoring endpoint for monitor wifi region image data.

API Endpoints:
    GET    /monitor/wifi/region_image

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.wifi.region_image.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.wifi.region_image.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Upload:
    """
    Upload Operations.

    Provides read-only access for FortiOS upload data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Upload endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        region_name: str | None = None,
        image_type: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Saves a floorplan/region image to an existing region.

        Args:
            region_name: Region name to save image to. (optional)
            image_type: MIME type of the image (png|jpeg|gif). (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.region_image.upload.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if region_name is not None:
            data["region_name"] = region_name
        if image_type is not None:
            data["image_type"] = image_type
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/wifi/region-image/upload", data=data
        )


class RegionImage:
    """RegionImage operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize RegionImage endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.upload = Upload(client)

    def get(
        self,
        region_name: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieves a floorplan/region image from a configured FortiAP region.

        Args:
            region_name: Region name to retrieve image from. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.wifi.region_image.get(region_name='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["region_name"] = region_name
        params.update(kwargs)
        return self._client.get("monitor", "/wifi/region-image", params=params)
