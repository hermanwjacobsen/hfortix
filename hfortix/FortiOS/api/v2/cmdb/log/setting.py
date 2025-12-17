"""
Log setting endpoint module.

This module provides access to the log/setting endpoint
for configuring general log settings.

API Path: log/setting
"""

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Setting:
    """
    Interface for configuring general log settings.

    This class provides methods to manage general log configuration settings.
    This is a singleton endpoint (GET/PUT only).

    Example usage:
        # Get current log settings
        settings = fgt.api.cmdb.log.setting.get()

        # Update log settings
        fgt.api.cmdb.log.setting.update(
            resolve_ip='enable',
            resolve_port='enable',
            log_user_in_upper='enable'
        )
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize the Setting instance.

        Args:
            client: The HTTP client used to communicate with the FortiOS device
        """
        self._client = client
        self._endpoint = "log/setting"

    def get(self) -> Dict[str, Any]:
        """
        Retrieve current general log settings.

        Returns:
            Dictionary containing log settings

        Example:
            >>> result = fgt.api.cmdb.log.setting.get()
            >>> print(result['resolve-ip'])
            'enable'
        """
        return self._client.get("cmdb", self._endpoint)

    def update(
        self,
        data_dict: Optional[Dict[str, Any]] = None,
        anonymization_hash: Optional[str] = None,
        brief_traffic_format: Optional[str] = None,
        custom_log_fields: Optional[list] = None,
        daemon_log: Optional[str] = None,
        expolicy_implicit_log: Optional[str] = None,
        extended_log: Optional[str] = None,
        extended_utm_log: Optional[str] = None,
        faz_override: Optional[str] = None,
        fwpolicy_implicit_log: Optional[str] = None,
        fwpolicy6_implicit_log: Optional[str] = None,
        local_in_allow: Optional[str] = None,
        local_in_deny_broadcast: Optional[str] = None,
        local_in_deny_unicast: Optional[str] = None,
        local_in_policy_log: Optional[str] = None,
        local_out: Optional[str] = None,
        local_out_ioc_detection: Optional[str] = None,
        log_policy_comment: Optional[str] = None,
        log_user_in_upper: Optional[str] = None,
        long_live_session_stat: Optional[str] = None,
        neighbor_event: Optional[str] = None,
        resolve_ip: Optional[str] = None,
        resolve_port: Optional[str] = None,
        rest_api_get: Optional[str] = None,
        rest_api_performance: Optional[str] = None,
        rest_api_set: Optional[str] = None,
        syslog_override: Optional[str] = None,
        user_anonymize: Optional[str] = None,
        web_svc_perf: Optional[str] = None,
        zone_name: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Update general log settings.

        Args:
            data_dict: Dictionary with API format parameters
            anonymization_hash: Anonymization hash salt
            brief_traffic_format: Enable/disable brief format traffic logging (enable | disable)
            custom_log_fields: Custom log fields to add to logs
            daemon_log: Enable/disable daemon logging (enable | disable)
            expolicy_implicit_log: Enable/disable explicit proxy implicit policy logging (enable | disable)
            extended_log: Enable/disable extended logging (enable | disable)
            extended_utm_log: Enable/disable extended UTM logging (enable | disable)
            faz_override: Override FortiAnalyzer settings (enable | disable)
            fwpolicy_implicit_log: Enable/disable implicit firewall policy logging (enable | disable)
            fwpolicy6_implicit_log: Enable/disable implicit IPv6 firewall policy logging (enable | disable)
            local_in_allow: Enable/disable local-in-allow logging (enable | disable)
            local_in_deny_broadcast: Enable/disable local-in denied broadcast logging (enable | disable)
            local_in_deny_unicast: Enable/disable local-in denied unicast logging (enable | disable)
            local_in_policy_log: Enable/disable local-in policy logging (enable | disable)
            local_out: Enable/disable local-out logging (enable | disable)
            local_out_ioc_detection: Enable/disable local-out IOC detection (enable | disable)
            log_policy_comment: Enable/disable policy comment in logs (enable | disable)
            log_user_in_upper: Enable/disable logging username in uppercase (enable | disable)
            long_live_session_stat: Enable/disable long live session statistics (enable | disable)
            neighbor_event: Enable/disable neighbor event logging (enable | disable)
            resolve_ip: Enable/disable resolving IP addresses to hostnames (enable | disable)
            resolve_port: Enable/disable resolving port numbers to service names (enable | disable)
            rest_api_get: Enable/disable REST API GET logging (enable | disable)
            rest_api_performance: REST API performance logging (enable | disable)
            rest_api_set: Enable/disable REST API SET logging (enable | disable)
            syslog_override: Override syslog settings (enable | disable)
            user_anonymize: Anonymize user names (enable | disable)
            web_svc_perf: Web service performance logging (enable | disable)
            zone_name: Zone name format (enable | disable)
            **kwargs: Additional parameters

        Returns:
            Dictionary containing API response

        Example:
            >>> fgt.api.cmdb.log.setting.update(
            ...     resolve_ip='enable',
            ...     resolve_port='enable',
            ...     log_user_in_upper='enable',
            ...     extended_log='enable'
            ... )
        """
        payload = dict(data_dict) if data_dict else {}

        param_map = {
            "anonymization_hash": "anonymization-hash",
            "brief_traffic_format": "brief-traffic-format",
            "custom_log_fields": "custom-log-fields",
            "daemon_log": "daemon-log",
            "expolicy_implicit_log": "expolicy-implicit-log",
            "extended_log": "extended-log",
            "extended_utm_log": "extended-utm-log",
            "faz_override": "faz-override",
            "fwpolicy_implicit_log": "fwpolicy-implicit-log",
            "fwpolicy6_implicit_log": "fwpolicy6-implicit-log",
            "local_in_allow": "local-in-allow",
            "local_in_deny_broadcast": "local-in-deny-broadcast",
            "local_in_deny_unicast": "local-in-deny-unicast",
            "local_in_policy_log": "local-in-policy-log",
            "local_out": "local-out",
            "local_out_ioc_detection": "local-out-ioc-detection",
            "log_policy_comment": "log-policy-comment",
            "log_user_in_upper": "log-user-in-upper",
            "long_live_session_stat": "long-live-session-stat",
            "neighbor_event": "neighbor-event",
            "resolve_ip": "resolve-ip",
            "resolve_port": "resolve-port",
            "rest_api_get": "rest-api-get",
            "rest_api_performance": "rest-api-performance",
            "rest_api_set": "rest-api-set",
            "syslog_override": "syslog-override",
            "user_anonymize": "user-anonymize",
            "web_svc_perf": "web-svc-perf",
            "zone_name": "zone-name",
        }

        for py_name, api_name in param_map.items():
            value = locals().get(py_name)
            if value is not None:
                payload[api_name] = value

        payload.update(kwargs)

        return self._client.put("cmdb", self._endpoint, data=payload)
