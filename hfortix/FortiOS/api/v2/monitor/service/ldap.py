"""
FortiOS MONITOR - Monitor Service Ldap

Monitoring endpoint for monitor service ldap data.

API Endpoints:
    GET    /monitor/service/ldap

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.monitor.service.ldap.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.monitor.service.ldap.get(
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


class Query:
    """
    Query Operations.

    Provides read-only access for FortiOS query data.

    Methods:
        get(): Retrieve monitoring/log data (read-only)

    Note:
        This is a read-only endpoint. Configuration changes are not supported.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Query endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        mkey: str | None = None,
        server_info_only: bool | None = None,
        skip_schema: bool | None = None,
        ldap_filter: str | None = None,
        ldap: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Retrieve LDAP server information and LDAP entries.

        Args:
            mkey: Name of the LDAP server setting object. (optional)
            server_info_only: Only retrieve server information. (optional)
            skip_schema: Explicitly skip schema retrieval. (optional)
            ldap_filter: LDAP filter string. (optional)
            ldap: Object containing overriden values of the LDAP server setting
            object. (optional)
            payload_dict: Optional dictionary of parameters
            raw_json: Return raw JSON response if True
            **kwargs: Additional parameters as keyword arguments

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.monitor.service.ldap.query.get()
        """
        params = payload_dict.copy() if payload_dict else {}
        if mkey is not None:
            params["mkey"] = mkey
        if server_info_only is not None:
            params["server_info_only"] = server_info_only
        if skip_schema is not None:
            params["skip_schema"] = skip_schema
        if ldap_filter is not None:
            params["ldap_filter"] = ldap_filter
        if ldap is not None:
            params["ldap"] = ldap
        params.update(kwargs)
        return self._client.get(
            "monitor", "/service/ldap/query", params=params
        )


class Ldap:
    """Ldap operations."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Ldap endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Initialize nested resources
        self.query = Query(client)
