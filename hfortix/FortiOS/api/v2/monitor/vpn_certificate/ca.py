"""
FortiOS MONITOR - Monitor Vpn Certificate Ca

Monitoring endpoint for monitor vpn certificate ca data.

API Endpoints:
    GET    /monitor/vpn_certificate/ca

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.vpn_certificate.ca.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.vpn_certificate.ca.get(
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


class ImportCa:
    """
    Importca Operations.

    Provides read-only access for FortiOS importca data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ImportCa endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        import_method: str | None = None,
        scep_url: str | None = None,
        scep_ca_id: str | None = None,
        scope: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Import CA certificate.

        Args:
            import_method: Method of importing CA certificate.[file|scep]
            (optional)
            scep_url: SCEP server URL. Required for import via SCEP (optional)
            scep_ca_id: SCEP server CA identifier for import via SCEP.
            (optional)
            scope: Scope of CA certificate [vdom*|global]. Global scope is only
            accessible for global administrators (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn_certificate.ca.import.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if import_method is not None:
            data["import_method"] = import_method
        if scep_url is not None:
            data["scep_url"] = scep_url
        if scep_ca_id is not None:
            data["scep_ca_id"] = scep_ca_id
        if scope is not None:
            data["scope"] = scope
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/vpn-certificate/ca/import", data=data
        )


class Ca:
    """Ca operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Ca endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.import_ca = ImportCa(client)
