"""
Endpoint Control EMS endpoint

GET  /api/v2/monitor/endpoint-control/ems/status
GET  /api/v2/monitor/endpoint-control/ems/cert-status
POST /api/v2/monitor/endpoint-control/ems/unverify-cert
POST /api/v2/monitor/endpoint-control/ems/verify-cert
GET  /api/v2/monitor/endpoint-control/ems/status-summary
GET  /api/v2/monitor/endpoint-control/ems/malware-hash
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["Ems"]


class Ems:
    """
    Endpoint Control EMS operations.

    Monitor and manage FortiClient EMS server connections.
    """

    def __init__(self, client: "HTTPClient"):
        """
        Initialize EMS endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._base_path = "endpoint-control/ems"

    def status(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        ems_name: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve EMS connection status for a specific EMS.

        Get detailed connection status including connectivity state,
        last communication time, and synchronization status.

        Args:
            data_dict: Dictionary containing query parameters
            ems_name: Name of the EMS server to query
            **kwargs: Additional query parameters

        Returns:
            dict: EMS connection status information

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Get EMS status using dict
            >>> status = fgt.api.monitor.endpoint_control.ems.status(
            ...     data_dict={'ems_name': 'ems-server1'}
            ... )
            >>> print(f"Status: {status.get('status')}")
            >>> print(f"Last sync: {status.get('last_sync')}")

            >>> # Get EMS status using keyword
            >>> status = fgt.api.monitor.endpoint_control.ems.status(
            ...     ems_name='ems-server1'
            ... )
        """
        params = data_dict.copy() if data_dict else {}

        if ems_name is not None:
            params["ems_name"] = ems_name

        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/status", params=params)

    def cert_status(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        ems_name: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve authentication status of the EMS server certificate.

        Get certificate validation status for a specific EMS server,
        including verification state and certificate details.

        Args:
            data_dict: Dictionary containing query parameters
            ems_name: Name of the EMS server to query
            **kwargs: Additional query parameters

        Returns:
            dict: EMS certificate status information

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Get cert status using dict
            >>> cert_status = fgt.api.monitor.endpoint_control.ems.cert_status(
            ...     data_dict={'ems_name': 'ems-server1'}
            ... )
            >>> print(f"Verified: {cert_status.get('verified')}")

            >>> # Get cert status using keyword
            >>> cert_status = fgt.api.monitor.endpoint_control.ems.cert_status(
            ...     ems_name='ems-server1'
            ... )
        """
        params = data_dict.copy() if data_dict else {}

        if ems_name is not None:
            params["ems_name"] = ems_name

        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/cert-status", params=params)

    def unverify_cert(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        ems_name: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Unverify EMS server certificate for a specific EMS.

        Mark the EMS server certificate as unverified, requiring
        manual verification before connection can proceed.

        Args:
            data_dict: Dictionary containing body parameters
            ems_name: Name of the EMS server
            **kwargs: Additional parameters

        Returns:
            dict: Operation result

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Unverify cert using dict
            >>> result = fgt.api.monitor.endpoint_control.ems.unverify_cert(
            ...     data_dict={'ems_name': 'ems-server1'}
            ... )

            >>> # Unverify cert using keyword
            >>> result = fgt.api.monitor.endpoint_control.ems.unverify_cert(
            ...     ems_name='ems-server1'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        if ems_name is not None:
            data["ems_name"] = ems_name

        data.update(kwargs)

        return self._client.post("monitor", f"{self._base_path}/unverify-cert", data=data)

    def verify_cert(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        ems_name: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Verify EMS server certificate for a specific EMS.

        Mark the EMS server certificate as verified, allowing
        connection to proceed with the certificate.

        Args:
            data_dict: Dictionary containing body parameters
            ems_name: Name of the EMS server
            **kwargs: Additional parameters

        Returns:
            dict: Operation result

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Verify cert using dict
            >>> result = fgt.api.monitor.endpoint_control.ems.verify_cert(
            ...     data_dict={'ems_name': 'ems-server1'}
            ... )

            >>> # Verify cert using keyword
            >>> result = fgt.api.monitor.endpoint_control.ems.verify_cert(
            ...     ems_name='ems-server1'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        if ems_name is not None:
            data["ems_name"] = ems_name

        data.update(kwargs)

        return self._client.post("monitor", f"{self._base_path}/verify-cert", data=data)

    def status_summary(
        self, data_dict: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> dict[str, Any] | list[dict]:
        """
        Retrieve status summary for all configured EMS.

        Get connection status summary for all configured EMS servers,
        including overall health and individual server states.

        Args:
            data_dict: Dictionary containing query parameters
            **kwargs: Additional query parameters

        Returns:
            dict or list: Status summary for all EMS servers

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Get status summary
            >>> summary = fgt.api.monitor.endpoint_control.ems.status_summary()
            >>> for ems in summary:
            ...     print(f"{ems.get('name')}: {ems.get('status')}")

            >>> # With filters using dict
            >>> summary = fgt.api.monitor.endpoint_control.ems.status_summary(
            ...     data_dict={'filter': 'online'}
            ... )
        """
        params = data_dict.copy() if data_dict else {}
        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/status-summary", params=params)

    def malware_hash(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        ems_name: Optional[str] = None,
        hash_value: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Retrieve malware hash information from EMS.

        Query EMS for details about a specific malware hash,
        including threat intelligence and detection information.

        Args:
            data_dict: Dictionary containing query parameters
            ems_name: Name of the EMS server to query
            hash_value: Malware hash to lookup
            **kwargs: Additional query parameters

        Returns:
            dict: Malware hash information

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Query malware hash using dict
            >>> info = fgt.api.monitor.endpoint_control.ems.malware_hash(
            ...     data_dict={
            ...         'ems_name': 'ems-server1',
            ...         'hash': 'abc123def456...'
            ...     }
            ... )

            >>> # Query malware hash using keywords
            >>> info = fgt.api.monitor.endpoint_control.ems.malware_hash(
            ...     ems_name='ems-server1',
            ...     hash_value='abc123def456...'
            ... )
            >>> print(f"Threat: {info.get('threat_name')}")
        """
        params = data_dict.copy() if data_dict else {}

        if ems_name is not None:
            params["ems_name"] = ems_name

        if hash_value is not None:
            params["hash"] = hash_value

        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/malware-hash", params=params)
