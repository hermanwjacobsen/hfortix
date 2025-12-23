"""
FortiOS MONITOR - Monitor Vpn Certificate Csr

Monitoring endpoint for monitor vpn certificate csr data.

API Endpoints:
    GET    /monitor/vpn_certificate/csr

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.vpn_certificate.csr.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.vpn_certificate.csr.get(
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


class Generate:
    """
    Generate Operations.

    Provides read-only access for FortiOS generate data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Generate endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        certname: str | None = None,
        subject: str | None = None,
        keytype: str | None = None,
        keysize: int | None = None,
        curvename: str | None = None,
        orgunits: list | None = None,
        org: str | None = None,
        city: str | None = None,
        state: str | None = None,
        countrycode: str | None = None,
        email: str | None = None,
        subject_alt_name: str | None = None,
        password: str | None = None,
        scep_url: str | None = None,
        scep_password: str | None = None,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Generate a certificate signing request (CSR) and a private key.

        Args:
            certname: Certicate name. Used to retrieve / download the CSR. Not
            included in CSR and key content. (optional)
            subject: Subject (Host IP/Domain Name/E-Mail). Common Name (CN) of
            the certificate subject. (optional)
            keytype: Generate a RSA or an elliptic curve certificate request
            [rsa|ec]. The Elliptic Curve option is unavailable if the FortiGate
            is a Low Encryption Device (LENC) (optional)
            keysize: Key size.[1024|1536|2048|4096]. 512 only if the FortiGate
            is a Low Encryption Device (LENC). Required when keytype is RSA.
            (optional)
            curvename: Elliptic curve name. [secp256r1|secp384r1|secp521r1].
            Unavailable if the FortiGate is a Low Encryption Device (LENC).
            Required when keytype is ec. (optional)
            orgunits: List of organization units. Organization Units (OU) of
            the certificate subject. (optional)
            org: Organization (O) of the certificate subject. (optional)
            city: Locality (L) of the certificate subject. (optional)
            state: State (ST) of the certificate subject. (optional)
            countrycode: Country (C) of the certificate subject. (optional)
            email: Email of the certificate subject. (optional)
            subject_alt_name: Subject alternative name (SAN) of the
            certificate. (optional)
            password: Password / pass phrase for the private key. If not
            provided, FortiGate generates a random one. (optional)
            scep_url: SCEP server URL. If provided, use the url to enroll the
            csr through SCEP. (optional)
            scep_password: SCEP challenge password. Some SCEP servers may
            require challege password. Provide it when SCEP server requires.
            (optional)
            scope: Scope of CSR [vdom*|global]. Global scope is only accessible
            for global administrators (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.vpn_certificate.csr.generate.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if certname is not None:
            data["certname"] = certname
        if subject is not None:
            data["subject"] = subject
        if keytype is not None:
            data["keytype"] = keytype
        if keysize is not None:
            data["keysize"] = keysize
        if curvename is not None:
            data["curvename"] = curvename
        if orgunits is not None:
            data["orgunits"] = orgunits
        if org is not None:
            data["org"] = org
        if city is not None:
            data["city"] = city
        if state is not None:
            data["state"] = state
        if countrycode is not None:
            data["countrycode"] = countrycode
        if email is not None:
            data["email"] = email
        if subject_alt_name is not None:
            data["subject_alt_name"] = subject_alt_name
        if password is not None:
            data["password"] = password
        if scep_url is not None:
            data["scep_url"] = scep_url
        if scep_password is not None:
            data["scep_password"] = scep_password
        if scope is not None:
            data["scope"] = scope
        data.update(kwargs)
        return self._client.post(
            "monitor", "/vpn-certificate/csr/generate", data=data
        )


class Csr:
    """Csr operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Csr endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.generate = Generate(client)
