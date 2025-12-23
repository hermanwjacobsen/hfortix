"""
FortiOS MONITOR - Monitor User Tacacs Plus

Monitoring endpoint for monitor user tacacs plus data.

API Endpoints:
    GET    /monitor/user/tacacs_plus

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.user.tacacs_plus.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.user.tacacs_plus.get(
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


class Test:
    """
    Test Operations.

    Provides read-only access for FortiOS test data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Test endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        ordinal: str | None = None,
        server: str | None = None,
        secret: str | None = None,
        port: int | None = None,
        source_ip: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Test the connectivity of the given TACACS+ server.

        Args:
            mkey: Name of FortiGate's TACACS+ object whose settings to test.
            (optional)
            ordinal: If 'mkey' is provided, the server-key pair to use from the
            object: 'primary', 'secondary' or 'tertiary'. Defaults to
            'primary'. (optional)
            server: Host name of IP of a TACACS+ server. If 'mkey' is provided,
            this overrides the 'server' value in the object. (optional)
            secret: Secret key for the TACACS+ server. If 'mkey' is provided,
            this overrides the 'key' value in the object. (optional)
            port: Port number of the TACACS+ server. If 'mkey' is provided,
            this overrides the 'port' value in the object. Defaults to 49.
            (optional)
            source_ip: Source IP for communications to TACACS+ server. If
            'mkey' is provided, this overrides the 'source-ip' value in the
            object. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.user.tacacs_plus.test.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if ordinal is not None:
            data["ordinal"] = ordinal
        if server is not None:
            data["server"] = server
        if secret is not None:
            data["secret"] = secret
        if port is not None:
            data["port"] = port
        if source_ip is not None:
            data["source_ip"] = source_ip
        data.update(kwargs)
        return self._client.post(
            "monitor", "/user/tacacs-plus/test", data=data
        )


class TacacsPlus:
    """TacacsPlus operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize TacacsPlus endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.test = Test(client)
