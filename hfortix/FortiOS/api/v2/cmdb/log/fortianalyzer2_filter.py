"""
FortiOS CMDB - Log FortiAnalyzer2 Filter

Filters for FortiAnalyzer (secondary server).

API Endpoints:
    GET  /api/v2/cmdb/log.fortianalyzer2/filter  - Get configuration
    PUT  /api/v2/cmdb/log.fortianalyzer2/filter  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Fortianalyzer2Filter:
    """Log FortiAnalyzer2 Filter endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get FortiAnalyzer2 filter settings.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing FortiAnalyzer2 filter settings

        Examples:
            >>> settings = fgt.api.cmdb.log.fortianalyzer2_filter.get()
        """
        path = "log.fortianalyzer2/filter"
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
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update FortiAnalyzer2 filter settings.

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
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # PUT - Update severity level
            >>> fgt.api.cmdb.log.fortianalyzer2_filter.update(severity='warning')
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
        }

        for key, value in param_map.items():
            if value is not None:
                data[key] = value

        data.update(kwargs)

        path = "log.fortianalyzer2/filter"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
