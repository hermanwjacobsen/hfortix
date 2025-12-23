"""
FortiOS MONITOR - Monitor Fortiview Session

Monitoring endpoint for monitor fortiview session data.

API Endpoints:
    GET    /monitor/fortiview/session

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.fortiview.session.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.fortiview.session.get(
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


class Cancel:
    """
    Cancel Operations.

    Provides read-only access for FortiOS cancel data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Cancel endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        sessionid: int | None = None,
        device: str | None = None,
        report_by: str | None = None,
        view_level: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Cancel a FortiView request session.

        Args:
            sessionid: Session ID to cancel. (optional)
            device: FortiView request session's device. [disk|faz] (optional)
            report_by: Report by field. (optional)
            view_level: FortiView View level. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.fortiview.session.cancel.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if sessionid is not None:
            data["sessionid"] = sessionid
        if device is not None:
            data["device"] = device
        if report_by is not None:
            data["report_by"] = report_by
        if view_level is not None:
            data["view_level"] = view_level
        data.update(kwargs)
        return self._client.post(
            "monitor", "/fortiview/session/cancel", data=data
        )


class Session:
    """Session operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Session endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.cancel = Cancel(client)
