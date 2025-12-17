"""
FortiOS CMDB - IPS Settings

Configure IPS VDOM parameter (singleton).

API Endpoints:
    GET  /api/v2/cmdb/ips/settings  - Get configuration
    PUT  /api/v2/cmdb/ips/settings  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Settings:
    """IPS Settings endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get IPS VDOM settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing IPS VDOM settings

        Examples:
            >>> settings = fgt.api.cmdb.ips.settings.get()
        """
        path = "ips/settings"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        ha_session_pickup: Optional[str] = None,
        ips_packet_quota: Optional[int] = None,
        packet_log_history: Optional[int] = None,
        packet_log_memory: Optional[int] = None,
        packet_log_post_attack: Optional[int] = None,
        proxy_inline_ips: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update IPS VDOM settings.

        Args:
            data_dict: Complete configuration dictionary
            ha_session_pickup: Enable/disable HA session pickup (enable|disable)
            ips_packet_quota: Maximum packet quota for IPS
            packet_log_history: Number of packets to capture before attack (0-255)
            packet_log_memory: Maximum memory for packet log (64-8192 KB)
            packet_log_post_attack: Number of packets to log after attack (0-255)
            proxy_inline_ips: Enable/disable inline IPS inspection (enable|disable)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> fgt.api.cmdb.ips.settings.update(
            ...     ips_packet_quota=10000,
            ...     packet_log_history=50
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "ha-session-pickup": ha_session_pickup,
            "ips-packet-quota": ips_packet_quota,
            "packet-log-history": packet_log_history,
            "packet-log-memory": packet_log_memory,
            "packet-log-post-attack": packet_log_post_attack,
            "proxy-inline-ips": proxy_inline_ips,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "ips/settings"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
