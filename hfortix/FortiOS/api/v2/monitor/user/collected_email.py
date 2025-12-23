"""
FortiOS MONITOR - Monitor User Collected Email

Monitoring endpoint for monitor user collected email data.

API Endpoints:
    GET    /monitor/user/collected_email

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.collected_email.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.collected_email.get(
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


class CollectedEmail:
    """
    Collectedemail Operations.

    Provides read-only access for FortiOS collectedemail data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CollectedEmail endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        ipv6: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        List email addresses collected from captive portal.

        Args:
            ipv6: Include collected email from IPv6 users. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.collected_email.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ipv6 is not None:
            params["ipv6"] = ipv6
        params.update(kwargs)
        return self._client.get(
            "monitor", "/user/collected-email", params=params
        )
