"""
FortiOS MONITOR - Monitor License Forticare Resellers

Monitoring endpoint for monitor license forticare resellers data.

API Endpoints:
    GET    /monitor/license/forticare_resellers

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.license.forticare_resellers.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.license.forticare_resellers.get(
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


class ForticareResellers:
    """
    Forticareresellers Operations.

    Provides read-only access for FortiOS forticareresellers data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ForticareResellers endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        country_code: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get current FortiCare resellers for the requested country.

        Args:
            country_code: FortiGuard country code (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.license.forticare_resellers.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if country_code is not None:
            params["country_code"] = country_code
        params.update(kwargs)
        return self._client.get(
            "monitor", "/license/forticare-resellers", params=params
        )
