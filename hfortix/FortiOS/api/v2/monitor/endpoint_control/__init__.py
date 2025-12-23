"""
Endpoint Control Monitor API

Provides monitoring and management of FortiClient endpoints via EMS
integration.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient

    from .avatar import Avatar
    from .ems import Ems
    from .installer import Installer

__all__ = ["EndpointControl"]


class EndpointControl:
    """
    Endpoint Control Monitor API.

    Provides access to FortiClient endpoint information, EMS status,
    and installer management.
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize EndpointControl monitor.

        Args:
            client: HTTP client implementing IHTTPClient protocol
        """
        self._client = client
        self._installer: Installer | None = None
        self._avatar: Avatar | None = None
        self._ems: Ems | None = None

    def record_list(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        ems_name: Optional[str] = None,
        **kwargs: Any,
    ) -> Union[
        dict[str, Any],
        list[dict],
        Coroutine[Any, Any, Union[dict[str, Any], list[dict]]],
    ]:
        """
        List endpoint records from FortiEMS.

        Retrieve endpoint information from FortiEMS including endpoint details,
        compliance status, and security posture.

        Args:
            data_dict: Dictionary containing query parameters
            ems_name: Name of the EMS server to query
            **kwargs: Additional query parameters

        Returns:
            dict or list: Endpoint records. Format depends on API response.

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Get all endpoint records
            >>> records = fgt.api.monitor.endpoint_control.record_list()
            >>> for record in records:
            ...     print(f"{record.get('host')}: {record.get('status')}")

            >>> # Get records from specific EMS using dict
            >>> records = fgt.api.monitor.endpoint_control.record_list(
            ...     data_dict={'ems_name': 'ems-server1'}
            ... )

            >>> # Get records from specific EMS using keyword
            >>> records = fgt.api.monitor.endpoint_control.record_list(
            ...     ems_name='ems-server1'
            ... )

        Note:
            This endpoint requires FortiEMS integration to be configured.
            Returns endpoint information only when FortiEMS is connected.
        """
        params = data_dict.copy() if data_dict else {}

        if ems_name is not None:
            params["ems_name"] = ems_name

        params.update(kwargs)

        return self._client.get(
            "monitor", "endpoint-control/record-list", params=params
        )

    def summary(
        self, data_dict: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Get summary of FortiClient endpoint records.

        Retrieve aggregated statistics about FortiClient endpoints including
        total count, online/offline status, compliance summary, etc.

        Args:
            data_dict: Dictionary containing query parameters
            **kwargs: Additional query parameters

        Returns:
            dict: Summary statistics of endpoint records

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Get endpoint summary
            >>> summary = fgt.api.monitor.endpoint_control.summary()
            >>> print(f"Total endpoints: {summary.get('total')}")
            >>> print(f"Online: {summary.get('online')}")
            >>> print(f"Offline: {summary.get('offline')}")

            >>> # With additional filters using dict
            >>> summary = fgt.api.monitor.endpoint_control.summary(
            ...     data_dict={'ems_name': 'ems-server1'}
            ... )

        Note:
            This endpoint requires FortiEMS integration to be configured.
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)

        return self._client.get(
            "monitor", "endpoint-control/summary", params=params
        )

    @property
    def installer(self):
        """Access installer endpoint."""
        if self._installer is None:
            self._installer = Installer(self._client)
        return self._installer

    @property
    def avatar(self):
        """Access avatar endpoint."""
        if self._avatar is None:
            self._avatar = Avatar(self._client)
        return self._avatar

    @property
    def ems(self):
        """Access EMS endpoint."""
        if self._ems is None:
            self._ems = Ems(self._client)
        return self._ems
