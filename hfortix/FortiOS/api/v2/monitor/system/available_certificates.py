"""
FortiOS MONITOR - Monitor System Available Certificates

Monitoring endpoint for monitor system available certificates data.

API Endpoints:
    GET    /monitor/system/available_certificates

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.available_certificates.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.available_certificates.get(
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


class AvailableCertificates:
    """
    Availablecertificates Operations.

    Provides read-only access for FortiOS availablecertificates data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize AvailableCertificates endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        with_remote: bool | None = None,
        with_ca: bool | None = None,
        with_crl: bool | None = None,
        mkey: str | None = None,
        find_all_references: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get available certificates.

        Args:
            scope: Scope of certificate [vdom*|global]. (optional)
            with_remote: Include remote certificates. (optional)
            with_ca: Include certificate authorities. (optional)
            with_crl: Include certificate revocation lists. (optional)
            mkey: Check if specific certificate is available. (optional)
            find_all_references: Include reference counts across all VDOMs when
            scope is global. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.available_certificates.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params["scope"] = scope
        if with_remote is not None:
            params["with_remote"] = with_remote
        if with_ca is not None:
            params["with_ca"] = with_ca
        if with_crl is not None:
            params["with_crl"] = with_crl
        if mkey is not None:
            params["mkey"] = mkey
        if find_all_references is not None:
            params["find_all_references"] = find_all_references
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/available-certificates", params=params
        )
