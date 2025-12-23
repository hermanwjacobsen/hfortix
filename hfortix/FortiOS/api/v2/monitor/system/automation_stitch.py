"""
FortiOS MONITOR - Monitor System Automation Stitch

Monitoring endpoint for monitor system automation stitch data.

API Endpoints:
    GET    /monitor/system/automation_stitch

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.automation_stitch.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.automation_stitch.get(
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


class Stats:
    """
    Stats Operations.

    Provides read-only access for FortiOS stats data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Stats endpoint.

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
        Statistics for automation stitches.

        Args:
            mkey: Filter: Automation stitch name. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.automation_stitch.stats.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/automation-stitch/stats", params=params
        )


class Test:
    """Test operations."""

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
        log: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Triggers an automation stitch for testing purposes.

        Args:
            mkey: ID of automation stitch to trigger. (optional)
            log: Message to store in the log buffer when triggering an event.
            For example, "logid=\"32102\" eventtime=1528840790000000000
            logdesc=\"Sample description\" msg=\"Sample message\"". This
            parameter is required for the 'event-log' event type. For the test
            to run, the 'logid' argument value must match the trigger-defined
            value. If 'logid' is not provided, the test will use the
            trigger-defined value. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.automation_stitch.test.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if log is not None:
            data["log"] = log
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/automation-stitch/test", data=data
        )


class Webhook:
    """Webhook operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Webhook endpoint.

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
        Triggers an incoming webhook for an automation stitch.

        Args:
            mkey: The incoming webhook name to trigger. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.automation_stitch.webhook.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/automation-stitch/webhook", data=data
        )


class AutomationStitch:
    """AutomationStitch operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize AutomationStitch endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.stats = Stats(client)
        self.test = Test(client)
        self.webhook = Webhook(client)
