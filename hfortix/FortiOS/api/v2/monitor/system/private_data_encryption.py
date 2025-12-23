"""
FortiOS MONITOR - Monitor System Private Data Encryption

Monitoring endpoint for monitor system private data encryption data.

API Endpoints:
    GET    /monitor/system/private_data_encryption

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.private_data_encryption.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.private_data_encryption.get(
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


class Set:
    """
    Set Operations.

    Provides read-only access for FortiOS set data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Set endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        enable: bool | None = None,
        password: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Sets private data encryption.

        Args:
            enable: Enable private data encryption. (optional)
            password: Admin password. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.private_data_encryption.set.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if enable is not None:
            data["enable"] = enable
        if password is not None:
            data["password"] = password
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/private-data-encryption/set", data=data
        )


class PrivateDataEncryption:
    """PrivateDataEncryption operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PrivateDataEncryption endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.set = Set(client)
