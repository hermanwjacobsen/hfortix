"""
FortiOS CMDB - Log Syslogd2 Override Filter

Override filters for remote syslog server.

API Endpoints:
    GET  /api/v2/cmdb/log.syslogd2/override-filter  - Get configuration
    PUT  /api/v2/cmdb/log.syslogd2/override-filter  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Syslogd2OverrideFilter:
    """Log Syslogd2 Override Filter endpoint (singleton)"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def get(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get syslogd2 override filter settings.

        Args:
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Enable CLI skip operator
            action: Special actions (default, schema, revision)
            vdom: Virtual domain
            **kwargs: Additional query parameters

        Returns:
            Syslogd override filter configuration

        Examples:
            >>> # Get syslogd2 override filter settings
            >>> result = fgt.api.cmdb.log.syslogd.override_filter.get()

            >>> # Get with metadata
            >>> result = fgt.api.cmdb.log.syslogd.override_filter.get(with_meta=True)
        """
        params = {}
        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = "log.syslogd2/override-filter"
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

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
        http_transaction: Optional[str] = None,
        forti_switch: Optional[str] = None,
        free_style: Optional[str] = None,
        debug: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update syslogd2 override filter settings.

        Supports three usage patterns:
        1. Dictionary: update(data_dict={'severity': 'information'})
        2. Keywords: update(severity='information', forward_traffic='enable')
        3. Mixed: update(data_dict={...}, severity='information')

        Args:
            data_dict: Complete configuration dictionary
            severity: Lowest severity level to log
            forward_traffic: Enable/disable forward traffic logging
            local_traffic: Enable/disable local traffic logging
            multicast_traffic: Enable/disable multicast traffic logging
            sniffer_traffic: Enable/disable sniffer traffic logging
            ztna_traffic: Enable/disable ZTNA traffic logging
            anomaly: Enable/disable anomaly logging
            voip: Enable/disable VoIP logging
            http_transaction: Enable/disable HTTP transaction logging
            forti_switch: Enable/disable FortiSwitch logging
            free_style: Enable/disable free style logging
            debug: Enable/disable debug logging
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            Update result

        Examples:
            >>> # PUT - Update severity level
            >>> fgt.api.cmdb.log.syslogd.override_filter.update(severity='warning')

            >>> # Enable forward traffic logging
            >>> fgt.api.cmdb.log.syslogd.override_filter.update(
            ...     forward_traffic='enable',
            ...     local_traffic='enable'
            ... )

            >>> # PUT - Update with dictionary
            >>> config = {
            ...     'severity': 'information',
            ...     'forward-traffic': 'enable',
            ...     'local-traffic': 'enable'
            ... }
            >>> fgt.api.cmdb.log.syslogd.override_filter.update(data_dict=config)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "severity": severity,
            "forward_traffic": forward_traffic,
            "local_traffic": local_traffic,
            "multicast_traffic": multicast_traffic,
            "sniffer_traffic": sniffer_traffic,
            "ztna_traffic": ztna_traffic,
            "anomaly": anomaly,
            "voip": voip,
            "http_transaction": http_transaction,
            "forti_switch": forti_switch,
            "free_style": free_style,
            "debug": debug,
        }

        api_field_map = {
            "severity": "severity",
            "forward_traffic": "forward-traffic",
            "local_traffic": "local-traffic",
            "multicast_traffic": "multicast-traffic",
            "sniffer_traffic": "sniffer-traffic",
            "ztna_traffic": "ztna-traffic",
            "anomaly": "anomaly",
            "voip": "voip",
            "http_transaction": "http-transaction",
            "forti_switch": "forti-switch",
            "free_style": "free-style",
            "debug": "debug",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = "log.syslogd2/override-filter"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
