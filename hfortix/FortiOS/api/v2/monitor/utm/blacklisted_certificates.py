"""
FortiOS MONITOR - Monitor Utm Blacklisted Certificates

Monitoring endpoint for monitor utm blacklisted certificates data.

API Endpoints:
    GET    /monitor/utm/blacklisted_certificates

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.utm.blacklisted_certificates.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.utm.blacklisted_certificates.get(
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


class Statistics:
    """
    Statistics Operations.

    Provides read-only access for FortiOS statistics data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Statistics endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve blacklisted SSL certificates statistics.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.utm.blacklisted_certificates.statistics.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/utm/blacklisted-certificates/statistics",
            params=params,
        )


class BlacklistedCertificates:
    """BlacklistedCertificates operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize BlacklistedCertificates endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.statistics = Statistics(client)

    def get(
        self,
        start: int,
        count: int,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of blacklisted SSL certificates.

        Args:
            start: Starting entry index. (required)
            count: Maximum number of entries to return. Limit is set to 2000.
            (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.utm.blacklisted_certificates.get(start=1,
            count=1)
        """
        params = payload_dict.copy() if payload_dict else {}
        params["start"] = start
        params["count"] = count
        params.update(kwargs)
        return self._client.get(
            "monitor", "/utm/blacklisted-certificates", params=params
        )
