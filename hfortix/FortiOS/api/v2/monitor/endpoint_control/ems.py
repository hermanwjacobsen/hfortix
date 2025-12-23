"""
FortiOS MONITOR - Monitor Endpoint Control Ems

Monitoring endpoint for monitor endpoint control ems data.

API Endpoints:
    GET    /monitor/endpoint_control/ems

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.endpoint_control.ems.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.endpoint_control.ems.get(
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


class CertStatus:
    """
    Certstatus Operations.

    Provides read-only access for FortiOS certstatus data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CertStatus endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        ems_id: int,
        scope: str | None = None,
        with_cert: bool | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve authentication status of the EMS server certificate for a
        specific EMS.

        Args:
            ems_id: EMS server ID (as defined in CLI table
            endpoint-control.fctems). (required)
            scope: Scope from which to retrieve EMS certificate status
            [vdom*|global]. (optional)
            with_cert: Return detailed certificate information. Available when
            the certificate is authenticated by installed CA certificates.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.endpoint_control.ems.cert_status.get(ems_id=1)
        """
        params = payload_dict.copy() if payload_dict else {}
        params["ems_id"] = ems_id
        if scope is not None:
            params["scope"] = scope
        if with_cert is not None:
            params["with_cert"] = with_cert
        params.update(kwargs)
        return self._client.get(
            "monitor", "/endpoint-control/ems/cert-status", params=params
        )


class MalwareHash:
    """MalwareHash operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize MalwareHash endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve malware hash from EMS.

        Args:
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.endpoint_control.ems.malware_hash.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        params.update(kwargs)
        return self._client.get(
            "monitor", "/endpoint-control/ems/malware-hash", params=params
        )


class Status:
    """Status operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Status endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        ems_id: int | None = None,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve EMS connection status for a specific EMS.

        Args:
            ems_id: EMS server ID (as defined in CLI table
            endpoint-control.fctems). (optional)
            scope: Scope from which to retrieve EMS connection status
            [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.endpoint_control.ems.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if ems_id is not None:
            params["ems_id"] = ems_id
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get(
            "monitor", "/endpoint-control/ems/status", params=params
        )


class StatusSummary:
    """StatusSummary operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize StatusSummary endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve status summary for all configured EMS.

        Args:
            scope: Scope from which to retrieve EMS status summary
            [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.endpoint_control.ems.status_summary.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if scope is not None:
            params["scope"] = scope
        params.update(kwargs)
        return self._client.get(
            "monitor", "/endpoint-control/ems/status-summary", params=params
        )


class UnverifyCert:
    """UnverifyCert operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize UnverifyCert endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ems_id: int | None = None,
        scope: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Unverify EMS server certificate for a specific EMS.

        Args:
            ems_id: EMS server ID (as defined in CLI table
            endpoint-control.fctems). (optional)
            scope: Scope from which to retrieve EMS certificate status
            [vdom*|global]. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.endpoint_control.ems.unverify_cert.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ems_id is not None:
            data["ems_id"] = ems_id
        if scope is not None:
            data["scope"] = scope
        data.update(kwargs)
        return self._client.post(
            "monitor", "/endpoint-control/ems/unverify-cert", data=data
        )


class VerifyCert:
    """VerifyCert operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize VerifyCert endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        ems_id: int | None = None,
        scope: str | None = None,
        fingerprint: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Verify EMS server certificate for a specific EMS.

        Args:
            ems_id: EMS server ID (as defined in CLI table
            endpoint-control.fctems). (optional)
            scope: Scope from which to verify EMS [vdom*|global]. (optional)
            fingerprint: EMS server certificate fingerprint to check with.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.endpoint_control.ems.verify_cert.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if ems_id is not None:
            data["ems_id"] = ems_id
        if scope is not None:
            data["scope"] = scope
        if fingerprint is not None:
            data["fingerprint"] = fingerprint
        data.update(kwargs)
        return self._client.post(
            "monitor", "/endpoint-control/ems/verify-cert", data=data
        )


class Ems:
    """Ems operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Ems endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.cert_status = CertStatus(client)
        self.malware_hash = MalwareHash(client)
        self.status = Status(client)
        self.status_summary = StatusSummary(client)
        self.unverify_cert = UnverifyCert(client)
        self.verify_cert = VerifyCert(client)
