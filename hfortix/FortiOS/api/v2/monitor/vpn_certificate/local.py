"""
FortiOS MONITOR - Monitor Vpn Certificate Local

Monitoring endpoint for monitor vpn certificate local data.

API Endpoints:
    GET    /monitor/vpn_certificate/local

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.vpn_certificate.local.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.vpn_certificate.local.get(
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


class Create:
    """
    Create Operations.

    Provides read-only access for FortiOS create data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Create endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        certname: str | None = None,
        common_name: str | None = None,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Generate a new certificate signed by Fortinet_CA_SSL.

        Args:
            certname: Certificate name. (optional)
            common_name: Certificate common name. (optional)
            scope: Scope of local certificate [vdom*|global]. Global scope is
            only accessible for global administrators. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn_certificate.local.create.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if certname is not None:
            data["certname"] = certname
        if common_name is not None:
            data["common_name"] = common_name
        if scope is not None:
            data["scope"] = scope
        data.update(kwargs)
        return self._client.post(
            "monitor", "/vpn-certificate/local/create", data=data
        )


class ImportLocal:
    """ImportLocal operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ImportLocal endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        type: str | None = None,
        certname: str | None = None,
        password: str | None = None,
        key_file_content: str | None = None,
        scope: str | None = None,
        acme_domain: str | None = None,
        acme_email: str | None = None,
        acme_ca_url: str | None = None,
        acme_rsa_key_size: int | None = None,
        acme_renew_window: int | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Import local certificate.

        Args:
            type: Type of certificate.[local|pkcs12|regular] (optional)
            certname: Certificate name for pkcs12 and regular certificate
            types. (optional)
            password: Optional password for pkcs12 and regular certificate
            types. (optional)
            key_file_content: Key content encoded in BASE64 for regular
            certificate type. (optional)
            scope: Scope of local certificate [vdom*|global]. Global scope is
            only accessible for global administrators (optional)
            acme_domain: A valid domain that resolves to an IP whose TCP port
            443 reaches this FortiGate. (optional)
            acme_email: Contact email address that is required by some CAs such
            as LetsEncrypt. (optional)
            acme_ca_url: URL for the ACME CA server. (optional)
            acme_rsa_key_size: Length of the RSA private key for the generated
            cert. (optional)
            acme_renew_window: Certificate renewal window in days. (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn_certificate.local.import.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if type is not None:
            data["type"] = type
        if certname is not None:
            data["certname"] = certname
        if password is not None:
            data["password"] = password
        if key_file_content is not None:
            data["key_file_content"] = key_file_content
        if scope is not None:
            data["scope"] = scope
        if acme_domain is not None:
            data["acme_domain"] = acme_domain
        if acme_email is not None:
            data["acme_email"] = acme_email
        if acme_ca_url is not None:
            data["acme_ca_url"] = acme_ca_url
        if acme_rsa_key_size is not None:
            data["acme_rsa_key_size"] = acme_rsa_key_size
        if acme_renew_window is not None:
            data["acme_renew_window"] = acme_renew_window
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/vpn-certificate/local/import", data=data
        )


class Local:
    """Local operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Local endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.create = Create(client)
        self.import_local = ImportLocal(client)
