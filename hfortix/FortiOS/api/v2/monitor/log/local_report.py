"""
FortiOS MONITOR - Monitor Log Local Report

Monitoring endpoint for monitor log local report data.

API Endpoints:
    GET    /monitor/log/local_report

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.log.local_report.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.log.local_report.get(
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


class Delete:
    """
    Delete Operations.

    Provides read-only access for FortiOS delete data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Delete endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkeys: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Delete a local report.

        Args:
            mkeys: Local Report Name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.log.local_report.delete.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkeys is not None:
            data["mkeys"] = mkeys
        data.update(kwargs)
        return self._client.post(
            "monitor", "/log/local-report/delete", data=data
        )


class Download:
    """Download operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Download endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        layout: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
                Download local report
        Access Group: loggrp.

                Args:
                    mkey: Local report name. (required)
                    layout: Layout name. (optional)
                    payload_dict: Optional dictionary of parameters
                    raw_json: Return raw JSON response if True
                    **kwargs: Additional parameters as keyword arguments

                Returns:
                    Dictionary containing API response

                Example:
                    >>>
                    fgt.api.monitor.log.local_report.download.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        if layout is not None:
            params["layout"] = layout
        params.update(kwargs)
        return self._client.get(
            "monitor", "/log/local-report/download", params=params
        )


class LocalReport:
    """LocalReport operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize LocalReport endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.delete = Delete(client)
        self.download = Download(client)
