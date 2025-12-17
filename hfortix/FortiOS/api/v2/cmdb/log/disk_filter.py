"""
FortiOS CMDB - Log Disk Filter

Configure filters for local disk logging. Use these filters to determine
the log messages to record according to severity and type.

API Endpoints:
    GET  /api/v2/cmdb/log.disk/filter  - Get configuration
    PUT  /api/v2/cmdb/log.disk/filter  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class DiskFilter:
    """Log Disk Filter endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get disk log filter settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing disk log filter settings

        Examples:
            >>> # Get current disk filter settings
            >>> settings = fgt.api.cmdb.log.disk_filter.get()
            >>> print(settings['severity'])
        """
        path = "log.disk/filter"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        severity: Optional[str] = None,
        forward_traffic: Optional[str] = None,
        local_traffic: Optional[str] = None,
        multicast_traffic: Optional[str] = None,
        sniffer_traffic: Optional[str] = None,
        ztna_traffic: Optional[str] = None,
        anomaly: Optional[str] = None,
        voip: Optional[str] = None,
        dlp_archive: Optional[str] = None,
        forti_switch: Optional[str] = None,
        http_transaction: Optional[str] = None,
        free_style: Optional[list[dict[str, Any]]] = None,
        debug: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update disk log filter settings.

        Args:
            data_dict: Complete configuration dictionary
            severity: Lowest severity level to log (emergency|alert|critical|error|warning|notification|information|debug)
            forward_traffic: Enable/disable forward traffic logging (enable|disable)
            local_traffic: Enable/disable local traffic logging (enable|disable)
            multicast_traffic: Enable/disable multicast traffic logging (enable|disable)
            sniffer_traffic: Enable/disable sniffer traffic logging (enable|disable)
            ztna_traffic: Enable/disable ZTNA traffic logging (enable|disable)
            anomaly: Enable/disable anomaly logging (enable|disable)
            voip: Enable/disable VoIP logging (enable|disable)
            dlp_archive: Enable/disable DLP archive logging (enable|disable)
            forti_switch: Enable/disable FortiSwitch logging (enable|disable)
            http_transaction: Enable/disable HTTP transaction logging (enable|disable)
            free_style: Free-style log filters (list of filter objects)
            debug: Enable/disable debug logging (enable|disable)
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # PUT - Update severity level
            >>> fgt.api.cmdb.log.disk_filter.update(severity='warning')

            >>> # Enable specific traffic types
            >>> fgt.api.cmdb.log.disk_filter.update(
            ...     forward_traffic='enable',
            ...     local_traffic='enable',
            ...     anomaly='enable'
            ... )

            >>> # Use data_dict pattern
            >>> fgt.api.cmdb.log.disk_filter.update(
            ...     data_dict={
            ...         'severity': 'information',
            ...         'forward-traffic': 'enable',
            ...         'ztna-traffic': 'enable'
            ...     }
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "severity": severity,
            "forward-traffic": forward_traffic,
            "local-traffic": local_traffic,
            "multicast-traffic": multicast_traffic,
            "sniffer-traffic": sniffer_traffic,
            "ztna-traffic": ztna_traffic,
            "anomaly": anomaly,
            "voip": voip,
            "dlp-archive": dlp_archive,
            "forti-switch": forti_switch,
            "http-transaction": http_transaction,
            "free-style": free_style,
            "debug": debug,
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "log.disk/filter"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
