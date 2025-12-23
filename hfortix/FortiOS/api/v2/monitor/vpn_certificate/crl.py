"""
FortiOS MONITOR - Monitor Vpn Certificate Crl

Monitoring endpoint for monitor vpn certificate crl data.

API Endpoints:
    GET    /monitor/vpn_certificate/crl

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.vpn_certificate.crl.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.vpn_certificate.crl.get(
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


class ImportCrl:
    """
    Importcrl Operations.

    Provides read-only access for FortiOS importcrl data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ImportCrl endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        scope: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Import certificate revocation lists (CRL) from file content.

        Args:
            scope: Scope of CRL [vdom*|global]. Global scope is only accessible
            for global administrators (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn_certificate.crl.import.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            data["scope"] = scope
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/vpn-certificate/crl/import", data=data
        )


class Crl:
    """Crl operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Crl endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.import_crl = ImportCrl(client)
