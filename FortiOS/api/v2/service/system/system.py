"""
FortiOS Service - System Operations

Provides system-level service operations for Security Fabric and vulnerability management.

API Endpoints:
    GET /system/psirt-vulnerabilities/                           - Get PSIRT vulnerability advisories
    GET /system/fabric-time-in-sync/                             - Check Fabric time synchronization
    GET /system/fabric-admin-lockout-exists-on-firmware-update/  - Check admin lockout on firmware update
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class System:
    """System service endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize System service endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def psirt_vulnerabilities(
        self,
        severity: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Retrieve PSIRT vulnerability advisories for the Security Fabric.

        Returns a list of PSIRT advisories that devices in the Security Fabric
        are vulnerable to, filtered by severity level.

        Args:
            severity (str, optional): Filter by severity level
                Valid values: 'none', 'low', 'medium', 'high', 'critical'
            scope (str, optional): Scope of the query
                Valid values: 'global' (Security Fabric), 'vdom' (single VDOM)
            vdom (str, optional): Virtual domain name
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing:
                - status: 'success' or 'error'
                - http_status: HTTP status code
                - results: List of PSIRT vulnerabilities with:
                    - name: Vulnerability name
                    - irNumber: IR number identifying the vulnerability
                    - serial: Device ID of vulnerable device
                    - upgradeToVersion: Recommended upgrade version
                    - severity: Severity level (none, low, medium, high, critical)

        Examples:
            # Get all PSIRT vulnerabilities
            result = fgt.service.system.psirt_vulnerabilities()

            # Get critical vulnerabilities only
            result = fgt.service.system.psirt_vulnerabilities(severity='critical')

            # Get vulnerabilities across Security Fabric
            result = fgt.service.system.psirt_vulnerabilities(scope='global')
        """
        endpoint = 'system/psirt-vulnerabilities/'
        params = {}

        if severity is not None:
            params['severity'] = severity
        if scope is not None:
            params['scope'] = scope
        if vdom is not None:
            params['vdom'] = vdom

        params.update(kwargs)

        return self._client.get('service', endpoint, params=params)

    def fabric_time_in_sync(
        self,
        utc: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Check whether Security Fabric device times are synchronized.

        Checks if other FortiGate devices in the Security Fabric have their time
        in sync with the specified UTC timestamp. Times are considered synchronized
        if the difference is within 2 minutes.

        Args:
            utc (str, optional): UTC timestamp in seconds to check against
                If not provided, checks against current device time
            vdom (str, optional): Virtual domain name
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing:
                - status: 'success' or 'error'
                - http_status: HTTP status code
                - results: Synchronization status with:
                    - synchronized: True if times are in sync (within 2 minutes)

        Examples:
            # Check if Fabric times are synchronized
            result = fgt.service.system.fabric_time_in_sync()

            # Check against specific UTC timestamp
            import time
            current_utc = str(int(time.time()))
            result = fgt.service.system.fabric_time_in_sync(utc=current_utc)

            # Check synchronization status
            if result['results']['synchronized']:
                print("Security Fabric times are synchronized")
            else:
                print("Security Fabric times are NOT synchronized")
        """
        endpoint = 'system/fabric-time-in-sync/'
        params = {}

        if utc is not None:
            params['utc'] = utc
        if vdom is not None:
            params['vdom'] = vdom

        params.update(kwargs)

        return self._client.get('service', endpoint, params=params)

    def fabric_admin_lockout_exists(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Check for admin lockout risks on firmware update.

        Checks if any FortiGate in the Security Fabric has administrative users
        that will get locked out if the firmware is updated to a version that
        does not support safer passwords.

        Args:
            vdom (str, optional): Virtual domain name
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing:
                - status: 'success' or 'error'
                - http_status: HTTP status code
                - results: Lockout risk status with:
                    - exists: True if at least one admin will be locked out

        Examples:
            # Check for admin lockout risks
            result = fgt.service.system.fabric_admin_lockout_exists()

            # Check lockout risk before firmware upgrade
            if result['results']['exists']:
                print("⚠️  WARNING: Admins will be locked out on firmware update!")
                print("Update admin passwords before upgrading firmware.")
            else:
                print("✅ Safe to upgrade firmware - no admin lockout risk")
        """
        endpoint = 'system/fabric-admin-lockout-exists-on-firmware-update/'
        params = {}

        if vdom is not None:
            params['vdom'] = vdom

        params.update(kwargs)

        return self._client.get('service', endpoint, params=params)
