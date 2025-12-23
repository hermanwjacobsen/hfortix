"""
FortiOS MONITOR - Monitor System Acme Certificate Status

Monitoring endpoint for monitor system acme certificate status data.

API Endpoints:
    GET    /monitor/system/acme_certificate_status

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.acme_certificate_status.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.acme_certificate_status.get(
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


class AcmeCertificateStatus:
    """
    Acmecertificatestatus Operations.

    Provides read-only access for FortiOS acmecertificatestatus data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize AcmeCertificateStatus endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        mkey: str,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get ACME certificate status.

        Args:
            mkey: Check if specific certificate is available. (required)
            scope: Scope of certificate [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.acme_certificate_status.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/acme-certificate-status", params=params
        )
