"""
FortiOS MONITOR - Monitor Switch Controller Recommendation

Monitoring endpoint for monitor switch controller recommendation data.

API Endpoints:
    GET    /monitor/switch_controller/recommendation

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.switch_controller.recommendation.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.switch_controller.recommendation.get(
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


class PseConfig:
    """
    Pseconfig Operations.

    Provides read-only access for FortiOS pseconfig data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize PseConfig endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        fortilink: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Execute switch recommendation for pse-config to prevent PSE-PSE
        scenarios.

        Args:
            fortilink: FortiLink interface name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.switch_controller.recommendation.pse_config.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if fortilink is not None:
            data["fortilink"] = fortilink
        data.update(kwargs)
        return self._client.post(
            "monitor",
            "/switch-controller/recommendation/pse-config",
            data=data,
        )


class Recommendation:
    """Recommendation operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Recommendation endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.pse_config = PseConfig(client)
