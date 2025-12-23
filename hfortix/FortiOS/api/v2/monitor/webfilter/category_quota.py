"""
FortiOS MONITOR - Monitor Webfilter Category Quota

Monitoring endpoint for monitor webfilter category quota data.

API Endpoints:
    GET    /monitor/webfilter/category_quota

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.webfilter.category_quota.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.webfilter.category_quota.get(
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


class Reset:
    """
    Reset Operations.

    Provides read-only access for FortiOS reset data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Reset endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        profile: str | None = None,
        user: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Reset webfilter quota for user or IP.

        Args:
            profile: Webfilter profile to reset. (optional)
            user: User or IP to reset with. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.webfilter.category_quota.reset.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if profile is not None:
            data["profile"] = profile
        if user is not None:
            data["user"] = user
        data.update(kwargs)
        return self._client.post(
            "monitor", "/webfilter/category-quota/reset", data=data
        )


class CategoryQuota:
    """CategoryQuota operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CategoryQuota endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.reset = Reset(client)

    def get(
        self,
        profile: str | None = None,
        user: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve quota usage statistics for webfilter categories.

        Args:
            profile: Webfilter profile. (optional)
            user: User or IP (required if profile specified). (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.webfilter.category_quota.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if profile is not None:
            params["profile"] = profile
        if user is not None:
            params["user"] = user
        params.update(kwargs)
        return self._client.get(
            "monitor", "/webfilter/category-quota", params=params
        )
