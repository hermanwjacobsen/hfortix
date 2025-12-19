"""Monitor API - Session operations."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Cancel:
    """Cancel operations."""

    def __init__(self, client: 'HTTPClient'):
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
    ) -> dict[str, Any]:
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
            data['sessionid'] = sessionid
        if device is not None:
            data['device'] = device
        if report_by is not None:
            data['report_by'] = report_by
        if view_level is not None:
            data['view_level'] = view_level
        data.update(kwargs)
        return self._client.post("monitor", "/fortiview/session/cancel", data=data)


class Session:
    """Session operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Session endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.cancel = Cancel(client)
