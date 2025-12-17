"""
Log event filter endpoint module.

This module provides access to the log/eventfilter endpoint
for configuring log event filters.

API Path: log/eventfilter
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Eventfilter:
    """
    Interface for configuring log event filters.

    This class provides methods to manage log event filter configuration.
    This is a singleton endpoint (GET/PUT only).

    Example usage:
        # Get current event filter settings
        settings = fgt.api.cmdb.log.eventfilter.get()

        # Update event filter settings
        fgt.api.cmdb.log.eventfilter.update(
            system='enable',
            vpn='enable',
            user='enable'
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the Eventfilter instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log/eventfilter"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current log event filter settings.

        Returns:
            Dictionary containing event filter settings

        Example:
            >>> result = fgt.api.cmdb.log.eventfilter.get()
            >>> print(result['system'])
            'enable'
        """
        return self._client.get("cmdb", self._endpoint)

    def update(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        cifs: Optional[str] = None,
        connector: Optional[str] = None,
        endpoint: Optional[str] = None,
        event: Optional[str] = None,
        fortiextender: Optional[str] = None,
        ha: Optional[str] = None,
        rest_api: Optional[str] = None,
        router: Optional[str] = None,
        sdwan: Optional[str] = None,
        security_rating: Optional[str] = None,
        switch_controller: Optional[str] = None,
        system: Optional[str] = None,
        user: Optional[str] = None,
        vpn: Optional[str] = None,
        wan_opt: Optional[str] = None,
        web_svc: Optional[str] = None,
        wireless_activity: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update log event filter settings.

        Args:
            data_dict: Dictionary with API format parameters
            cifs: Enable/disable CIFS logging (enable | disable)
            connector: Enable/disable connector logging (enable | disable)
            endpoint: Enable/disable endpoint logging (enable | disable)
            event: Enable/disable event logging (enable | disable)
            fortiextender: Enable/disable FortiExtender logging (enable | disable)
            ha: Enable/disable HA logging (enable | disable)
            rest_api: Enable/disable REST API logging (enable | disable)
            router: Enable/disable router logging (enable | disable)
            sdwan: Enable/disable SD-WAN logging (enable | disable)
            security_rating: Enable/disable security rating logging (enable | disable)
            switch_controller: Enable/disable switch controller logging (enable | disable)
            system: Enable/disable system event logging (enable | disable)
            user: Enable/disable user logging (enable | disable)
            vpn: Enable/disable VPN logging (enable | disable)
            wan_opt: Enable/disable WAN optimization logging (enable | disable)
            web_svc: Enable/disable web service logging (enable | disable)
            wireless_activity: Enable/disable wireless activity logging (enable | disable)
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.log.eventfilter.update(
            ...     system='enable',
            ...     vpn='enable',
            ...     user='enable',
            ...     router='disable'
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "cifs": "cifs",
            "connector": "connector",
            "endpoint": "endpoint",
            "event": "event",
            "fortiextender": "fortiextender",
            "ha": "ha",
            "rest_api": "rest-api",
            "router": "router",
            "sdwan": "sdwan",
            "security_rating": "security-rating",
            "switch_controller": "switch-controller",
            "system": "system",
            "user": "user",
            "vpn": "vpn",
            "wan_opt": "wan-opt",
            "web_svc": "web-svc",
            "wireless_activity": "wireless-activity",
        }

        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        payload.update(kwargs)

        return self._client.put("cmdb", self._endpoint, data=payload)
