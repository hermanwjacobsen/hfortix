"""
Log threat weight endpoint module.

This module provides access to the log/threat-weight endpoint
for configuring threat weight settings.

API Path: log/threat-weight
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class ThreatWeight:
    """
    Interface for configuring threat weight settings.

    This class provides methods to manage threat weight configuration,
    which controls how different threat types are weighted in security ratings.
    This is a singleton endpoint (GET/PUT only).

    Example usage:
        # Get current threat weight settings
        settings = fgt.api.cmdb.log.threat_weight.get()

        # Update threat weight settings
        fgt.api.cmdb.log.threat_weight.update(
            status='enable',
            level={'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the ThreatWeight instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log/threat-weight"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current threat weight settings.

        Returns:
            Dictionary containing threat weight settings

        Example:
            >>> result = fgt.api.cmdb.log.threat_weight.get()
            >>> print(result['status'])
            'enable'
        """
        return self._client.get("cmdb", self._endpoint)

    def update(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        application: Optional[list] = None,
        blocked_connection: Optional[dict] = None,
        botnet_connection_detected: Optional[dict] = None,
        failed_connection: Optional[dict] = None,
        geolocation: Optional[list] = None,
        ips: Optional[dict] = None,
        level: Optional[dict] = None,
        malware: Optional[dict] = None,
        status: Optional[str] = None,
        url_block_detected: Optional[dict] = None,
        web: Optional[list] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update threat weight settings.

        Args:
            data_dict: Dictionary with API format parameters
            application: Application-based threat weight settings
            blocked_connection: Blocked connection threat weight
            botnet_connection_detected: Botnet connection detected threat weight
            failed_connection: Failed connection threat weight
            geolocation: Geolocation-based threat weight settings
            ips: IPS threat weight settings
            level: Threat level weights (low, medium, high, critical)
            malware: Malware threat weight settings
            status: Enable/disable threat weight (enable | disable)
            url_block_detected: URL block detected threat weight
            web: Web-based threat weight settings
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.log.threat_weight.update(
            ...     status='enable',
            ...     level={
            ...         'low': 1,
            ...         'medium': 2,
            ...         'high': 3,
            ...         'critical': 4
            ...     }
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "application": "application",
            "blocked_connection": "blocked-connection",
            "botnet_connection_detected": "botnet-connection-detected",
            "failed_connection": "failed-connection",
            "geolocation": "geolocation",
            "ips": "ips",
            "level": "level",
            "malware": "malware",
            "status": "status",
            "url_block_detected": "url-block-detected",
            "web": "web",
        }

        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        payload.update(kwargs)

        return self._client.put("cmdb", self._endpoint, data=payload)
