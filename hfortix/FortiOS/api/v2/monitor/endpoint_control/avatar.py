"""
Endpoint Control Avatar endpoint

GET /api/v2/monitor/endpoint-control/avatar/download
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Avatar"]


class Avatar:
    """
    Endpoint Control Avatar operations.

    Download endpoint avatar images.
    """

    def __init__(self, client: "HTTPClient"):
        """
        Initialize Avatar endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._base_path = "endpoint-control/avatar"

    def download(
        self, data_dict: Optional[dict[str, Any]] = None, uid: Optional[str] = None, **kwargs: Any
    ) -> bytes:
        """
        Download an endpoint avatar image.

        Retrieve the avatar image associated with a specific endpoint.

        Args:
            data_dict: Dictionary containing query parameters
            uid: Endpoint UID to get avatar for
            **kwargs: Additional query parameters

        Returns:
            bytes: Image file content (typically PNG or JPEG)

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Download avatar using dict
            >>> avatar_data = fgt.api.monitor.endpoint_control.avatar.download(
            ...     data_dict={'uid': 'EP12345'}
            ... )
            >>> with open('endpoint_avatar.png', 'wb') as f:
            ...     f.write(avatar_data)

            >>> # Download avatar using keyword
            >>> avatar_data = fgt.api.monitor.endpoint_control.avatar.download(
            ...     uid='EP12345'
            ... )

        Note:
            Returns binary image data, not JSON.
        """
        params = data_dict.copy() if data_dict else {}

        if uid is not None:
            params["uid"] = uid

        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/download", params=params)
