"""
WebTrends filter endpoint module.

This module provides access to the log.webtrends/filter endpoint
for configuring which log types to send to WebTrends.

API Path: log.webtrends/filter
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class WebtrendsFilter:
    """
    Interface for configuring WebTrends filter settings.

    This class provides methods to manage WebTrends filter configuration,
    controlling which log types are sent to WebTrends servers.

    Supports three types of parameters:
    - data_dict: Standard dictionary format matching API structure
    - keyword arguments: Python snake_case parameters
    - mixed: Both data_dict and keyword arguments combined

    Example usage:
        # Using keyword arguments (snake_case)
        fgt.api.cmdb.log.webtrends.filter.update(
            severity='information',
            forward_traffic='enable'
        )

        # Using data_dict (hyphenated)
        fgt.api.cmdb.log.webtrends.filter.update(
            data_dict={
                'severity': 'information',
                'forward-traffic': 'enable'
            }
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the WebtrendsFilter instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log.webtrends/filter"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current WebTrends filter configuration.

        Returns:
            Dictionary containing WebTrends filter settings

        Example:
            >>> result = fgt.api.cmdb.log.webtrends.filter.get()
            >>> print(result['severity'])
            'information'
        """
        path = "log.webtrends/filter"
        return self._client.get("cmdb", path)

    def put(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        anomaly: Optional[str] = None,
        debug: Optional[str] = None,
        forti_switch: Optional[str] = None,
        forward_traffic: Optional[str] = None,
        free_style: Optional[str] = None,
        http_transaction: Optional[str] = None,
        local_traffic: Optional[str] = None,
        multicast_traffic: Optional[str] = None,
        severity: Optional[str] = None,
        sniffer_traffic: Optional[str] = None,
        voip: Optional[str] = None,
        ztna_traffic: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update WebTrends filter configuration.

        Accepts parameters in multiple formats for flexibility:
        1. data_dict with API format (hyphenated keys)
        2. Python snake_case keyword arguments
        3. Both data_dict and kwargs combined

        Args:
            data_dict: Dictionary with API format parameters (hyphenated)
            anomaly: Enable/disable anomaly logging (enable | disable)
            debug: Enable/disable debug logging (enable | disable)
            forti_switch: Enable/disable FortiSwitch logging (enable | disable)
            forward_traffic: Enable/disable forward traffic logging (enable | disable)
            free_style: Enable/disable free style logging (enable | disable)
            http_transaction: Enable/disable HTTP transaction logging (enable | disable)
            local_traffic: Enable/disable local traffic logging (enable | disable)
            multicast_traffic: Enable/disable multicast traffic logging (enable | disable)
            severity: Minimum severity level to log
                     (emergency | alert | critical | error | warning | notification | information | debug)
            sniffer_traffic: Enable/disable sniffer traffic logging (enable | disable)
            voip: Enable/disable VoIP logging (enable | disable)
            ztna_traffic: Enable/disable ZTNA traffic logging (enable | disable)
            **kwargs: Additional parameters in API format (hyphenated)

        Returns:
            Dictionary containing API response

        Example:
            >>> # Using keyword arguments
            >>> fgt.api.cmdb.log.webtrends.filter.update(
            ...     severity='information',
            ...     forward_traffic='enable',
            ...     local_traffic='disable'
            ... )

            >>> # Using data_dict
            >>> fgt.api.cmdb.log.webtrends.filter.update(
            ...     data_dict={
            ...         'severity': 'warning',
            ...         'forward-traffic': 'enable'
            ...     }
            ... )
        """
        # Start with data_dict if provided, otherwise empty dict
        payload = dict(data_dict) if data_dict else {}

        # Map Python parameter names to API format and add to payload
        param_map = {
            "anomaly": "anomaly",
            "debug": "debug",
            "forti_switch": "forti-switch",
            "forward_traffic": "forward-traffic",
            "free_style": "free-style",
            "http_transaction": "http-transaction",
            "local_traffic": "local-traffic",
            "multicast_traffic": "multicast-traffic",
            "severity": "severity",
            "sniffer_traffic": "sniffer-traffic",
            "voip": "voip",
            "ztna_traffic": "ztna-traffic",
        }

        # Add mapped parameters
        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        # Add any additional kwargs
        payload.update(kwargs)

        path = "log.webtrends/filter"
        return self._client.put("cmdb", path, data=payload)
