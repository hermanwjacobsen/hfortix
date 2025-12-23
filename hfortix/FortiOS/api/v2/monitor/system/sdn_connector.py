"""
FortiOS MONITOR - Monitor System Sdn Connector

Monitoring endpoint for monitor system sdn connector data.

API Endpoints:
    GET    /monitor/system/sdn_connector

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.sdn_connector.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.sdn_connector.get(
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


class NsxSecurityTags:
    """
    Nsxsecuritytags Operations.

    Provides read-only access for FortiOS nsxsecuritytags data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize NsxSecurityTags endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve a list of NSX security tags for connected NSX servers.

        Args:
            mkey: Filter: NSX SDN connector name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sdn_connector.nsx_security_tags.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/sdn-connector/nsx-security-tags", params=params
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
        mkey: str | None = None,
        type: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve connection status for SDN connectors.

        Args:
            mkey: Filter: SDN connector name. (optional)
            type: Filter: SDN connector type. Ignored if mkey is specified.
            (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sdn_connector.status.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        if type is not None:
            params["type"] = type
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/sdn-connector/status", params=params
        )


class Update:
    """Update operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Update endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update an SDN connector's connection status.

        Args:
            mkey: SDN connector name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sdn_connector.update.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/sdn-connector/update", data=data
        )


class ValidateGcpKey:
    """ValidateGcpKey operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ValidateGcpKey endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        private_key: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Validate a string representing a private key from GCP in PEM format.

        Args:
            private_key: Private key in PEM format. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.sdn_connector.validate_gcp_key.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if private_key is not None:
            data["private-key"] = private_key
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/sdn-connector/validate-gcp-key", data=data
        )


class SdnConnector:
    """SdnConnector operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SdnConnector endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.nsx_security_tags = NsxSecurityTags(client)
        self.status = Status(client)
        self.update = Update(client)
        self.validate_gcp_key = ValidateGcpKey(client)
