"""Monitor API - LocalReport operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Delete:
    """Delete operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
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
            data['mkeys'] = mkeys
        data.update(kwargs)
        return self._client.post("monitor", "/log/local-report/delete", data=data)


class Download:
    """Download operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
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
            >>> fgt.api.monitor.log.local_report.download.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params['mkey'] = mkey
        if layout is not None:
            params['layout'] = layout
        params.update(kwargs)
        return self._client.get("monitor", "/log/local-report/download", params=params)


class LocalReport:
    """LocalReport operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize LocalReport endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.delete = Delete(client)
        self.download = Download(client)
