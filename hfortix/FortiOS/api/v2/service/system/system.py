"""
FortiOS SERVICE - Service System System

Service endpoint.

API Endpoints:
    GET    /service/system/system

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # Get monitoring/log data (read-only)
    >>> data = fgt.api.service.system.system.get()
    >>>
    >>> # With filters and parameters
    >>> data = fgt.api.service.system.system.get(
    ...     count=100,
    ...     start=0
    ... )

Note:
    This is a read-only endpoint. Only GET operations are supported.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class FabricAdminLockoutExistsOnFirmwareUpdate:
    """
    Fabricadminlockoutexistsonfirmwareupdate Operations.

    Provides CRUD operations for FortiOS
    fabricadminlockoutexistsonfirmwareupdate configuration.

    Methods:
        get(): Retrieve configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def get(
        self,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
               Check if there exists a FortiGate in the Fabric that has an
               administrative user that will get locked out if firmware is
               updated to a version that does not support safer passwords.
        Access Group: any

               Supports dual approach:
               1. Individual parameters: get(param='value')
               2. Payload dict: get(payload_dict={'param': 'value'})

               Args:
                   No parameters
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass
                   all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result =
                   fgt.api.service.system.fabric-admin-lockout-exists-on-firmware-update.get()

                   # Using payload_dict
                   result =
                   fgt.api.service.system.fabric-admin-lockout-exists-on-firmware-update.get(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}

        params.update(kwargs)

        return self._client.get(
            "service",
            "system/fabric-admin-lockout-exists-on-firmware-update/",
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class FabricTimeInSync:
    """FabricTimeInSync resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def get(
        self,
        utc: Optional[str] = None,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
               Checks whether the other FortiGate device's time in the Security
               Fabric is in sync with the specified utc timestamp (in seconds)
        Access Group: any

               Supports dual approach:
               1. Individual parameters: get(param='value')
               2. Payload dict: get(payload_dict={'param': 'value'})

               Args:
                   utc: UTC, in seconds, to check against to see if the
                   device's current time is syncronized with.
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass
                   all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.system.fabric-time-in-sync.get()

                   # Using payload_dict
                   result = fgt.api.service.system.fabric-time-in-sync.get(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}
        if utc is not None:
            params["utc"] = utc

        params.update(kwargs)

        return self._client.get(
            "service",
            "system/fabric-time-in-sync/",
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class PsirtVulnerabilities:
    """PsirtVulnerabilities resource"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client

    def get(
        self,
        vdom: Optional[str] = None,
        payload_dict: Optional[dict[str, Any]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
               Retrieve a list of N number of PSIRT advisories that the
               Security Fabric is vulnerable to for a given severity.
        Access Group: sysgrp.mnt

               Supports dual approach:
               1. Individual parameters: get(param='value')
               2. Payload dict: get(payload_dict={'param': 'value'})

               Args:
                   No parameters
                   vdom: Virtual Domain name
                   payload_dict: Alternative to individual parameters - pass
                   all params as dict
                   raw_json: Return raw JSON response without parsing
                   **kwargs: Additional parameters to pass to the API

               Returns:
                   Dictionary containing response data

               Examples:
                   # Using individual parameters
                   result = fgt.api.service.system.psirt-vulnerabilities.get()

                   # Using payload_dict
                   result = fgt.api.service.system.psirt-vulnerabilities.get(
                       payload_dict={'param': 'value'}
                   )
        """
        if payload_dict:
            params = payload_dict.copy()
        else:
            params = {}

        params.update(kwargs)

        return self._client.get(
            "service",
            "system/psirt-vulnerabilities/",
            params=params,
            vdom=vdom,
            raw_json=raw_json,
        )


class System:
    """Main System service class"""

    def __init__(self, client: "IHTTPClient") -> None:
        self._client = client
        self._fabricAdminLockoutExistsOnFirmwareUpdate: (
            FabricAdminLockoutExistsOnFirmwareUpdate | None
        ) = None
        self._fabricTimeInSync: FabricTimeInSync | None = None
        self._psirtVulnerabilities: PsirtVulnerabilities | None = None

    @property
    def fabricAdminLockoutExistsOnFirmwareUpdate(
        self,
    ) -> FabricAdminLockoutExistsOnFirmwareUpdate:
        """Access FabricAdminLockoutExistsOnFirmwareUpdate resource"""
        if self._fabricAdminLockoutExistsOnFirmwareUpdate is None:
            self._fabricAdminLockoutExistsOnFirmwareUpdate = (
                FabricAdminLockoutExistsOnFirmwareUpdate(self._client)
            )
        return self._fabricAdminLockoutExistsOnFirmwareUpdate

    @property
    def fabricTimeInSync(self) -> FabricTimeInSync:
        """Access FabricTimeInSync resource"""
        if self._fabricTimeInSync is None:
            self._fabricTimeInSync = FabricTimeInSync(self._client)
        return self._fabricTimeInSync

    @property
    def psirtVulnerabilities(self) -> PsirtVulnerabilities:
        """Access PsirtVulnerabilities resource"""
        if self._psirtVulnerabilities is None:
            self._psirtVulnerabilities = PsirtVulnerabilities(self._client)
        return self._psirtVulnerabilities
