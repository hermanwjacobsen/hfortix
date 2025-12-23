"""
FortiOS MONITOR - Monitor License Database

Monitoring endpoint for monitor license database data.

API Endpoints:
    GET    /monitor/license/database

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.license.database.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.license.database.get(
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


class Upgrade:
    """
    Upgrade Operations.

    Provides read-only access for FortiOS upgrade data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Upgrade endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        db_name: str | None = None,
        confirm_not_signed: bool | None = None,
        confirm_not_ga_certified: bool | None = None,
        file_id: str | None = None,
        file_content: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Upgrade or downgrade UTM engine or signature package
        (IPS/AntiVirus/Application Control/Industrial database/Security
        Rating/Internet Service Database) using uploaded file.

        Args:
            db_name: Security service database name
            [ips|appctrl|industrial_db|antivirus|security_rating|isdb|iotddb]
            (optional)
            confirm_not_signed: Confirm whether unsigned pkg files may be
            uploaded. (optional)
            confirm_not_ga_certified: Confirm whether non GA-certified pkg
            files may be uploaded. (optional)
            file_id: File id of existing pkg file from a previous upload.
            (optional)
            file_content: Provided when uploading a file: base64 encoded file
            data. Must not contain whitespace or other invalid base64
            characters. Must be included in HTTP body. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.license.database.upgrade.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if db_name is not None:
            data["db_name"] = db_name
        if confirm_not_signed is not None:
            data["confirm_not_signed"] = confirm_not_signed
        if confirm_not_ga_certified is not None:
            data["confirm_not_ga_certified"] = confirm_not_ga_certified
        if file_id is not None:
            data["file_id"] = file_id
        if file_content is not None:
            data["file_content"] = file_content
        data.update(kwargs)
        return self._client.post(
            "monitor", "/license/database/upgrade", data=data
        )


class Database:
    """Database operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Database endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.upgrade = Upgrade(client)
