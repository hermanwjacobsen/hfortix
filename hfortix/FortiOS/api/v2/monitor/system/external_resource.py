"""
FortiOS MONITOR - Monitor System External Resource

Monitoring endpoint for monitor system external resource data.

API Endpoints:
    GET    /monitor/system/external_resource

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.system.external_resource.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.system.external_resource.get(
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


class Dynamic:
    """
    Dynamic Operations.

    Provides read-only access for FortiOS dynamic data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Dynamic endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        commands: list | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Push updates to the specified external resource.

        Args:
            commands: The commands to execute to update dynamic external
            resources. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.external_resource.dynamic.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if commands is not None:
            data["commands"] = commands
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/external-resource/dynamic", data=data
        )


class EntryList:
    """EntryList operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize EntryList endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str,
        status_only: bool | None = None,
        include_notes: bool | None = None,
        counts_only: bool | None = None,
        entry: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve resource file status with a list of valid/invalid entries for
        the specific external resource.

        Args:
            mkey: The external resource name to query. (required)
            status_only: Set to true to retrieve resource file status only.
            (Skip valid/invalid entries.) (optional)
            include_notes: Set to true to retrieve notes on the resource file.
            (optional)
            counts_only: Set to true to retrive valid/invalid counts only.
            (Skip entries.) (optional)
            entry: Entry of external resource. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.external_resource.entry_list.get(mkey='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["mkey"] = mkey
        if status_only is not None:
            params["status_only"] = status_only
        if include_notes is not None:
            params["include_notes"] = include_notes
        if counts_only is not None:
            params["counts_only"] = counts_only
        if entry is not None:
            params["entry"] = entry
        params.update(kwargs)
        return self._client.get(
            "monitor", "/system/external-resource/entry-list", params=params
        )


class GenericAddress:
    """GenericAddress operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize GenericAddress endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        data: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Push JSON data to the specified external resource.

        Args:
            mkey: The name of the external resource to update. (optional)
            data: JSON data. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.external_resource.generic_address.post()
        """
        params: dict[str, Any] = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        if data is not None:
            params["data"] = data
        params.update(kwargs)
        return self._client.post(
            "monitor", "/system/external-resource/generic-address", data=params
        )


class Refresh:
    """Refresh operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Refresh endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def post(
        self,
        mkey: str | None = None,
        check_status_only: bool | None = None,
        last_connection_time: int | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Fetch the external resource file and refresh status for the specified
        external resource.

        Args:
            mkey: The name of the external resource to query. (optional)
            check_status_only: Set to true to return only the refresh status.
            (optional)
            last_connection_time: The timestamp of last connection to the
            resource; used for checking refresh status. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.system.external_resource.refresh.post()
        """
        data = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            data["mkey"] = mkey
        if check_status_only is not None:
            data["check_status_only"] = check_status_only
        if last_connection_time is not None:
            data["last_connection_time"] = last_connection_time
        data.update(kwargs)
        return self._client.post(
            "monitor", "/system/external-resource/refresh", data=data
        )


class ValidateJsonpath:
    """ValidateJsonpath operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ValidateJsonpath endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        path_name: str,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Validate a JSON path name.

        Args:
            path_name: The name of the JSON path to validate. (required)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>>
            fgt.api.monitor.system.external_resource.validate_jsonpath.get(path_name='value')
        """
        params = payload_dict.copy() if payload_dict else {}
        params["path_name"] = path_name
        params.update(kwargs)
        return self._client.get(
            "monitor",
            "/system/external-resource/validate-jsonpath",
            params=params,
        )


class ExternalResource:
    """ExternalResource operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize ExternalResource endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.dynamic = Dynamic(client)
        self.entry_list = EntryList(client)
        self.generic_address = GenericAddress(client)
        self.refresh = Refresh(client)
        self.validate_jsonpath = ValidateJsonpath(client)
