"""
FortiOS CMDB - Log Syslogd3 Override Setting

Override settings for remote syslog server.

API Endpoints:
    GET  /api/v2/cmdb/log.syslogd3/override-setting  - Get configuration
    PUT  /api/v2/cmdb/log.syslogd3/override-setting  - Update configuration
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Syslogd3OverrideSetting:
    """Log Syslogd3 Override Setting endpoint (singleton)"""

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
        Get syslogd3 override settings.

        Args:
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Enable CLI skip operator
            action: Special actions (default, schema, revision)
            vdom: Virtual domain
            **kwargs: Additional query parameters

        Returns:
            Syslogd override settings configuration

        Examples:
            >>> # Get syslogd3 override settings
            >>> result = fgt.api.cmdb.log.syslogd.override_setting.get()

            >>> # Get with metadata
            >>> result = fgt.api.cmdb.log.syslogd.override_setting.get(with_meta=True)
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

        path = "log.syslogd3/override-setting"
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def put(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        status: Optional[str] = None,
        server: Optional[str] = None,
        mode: Optional[str] = None,
        port: Optional[int] = None,
        facility: Optional[str] = None,
        source_ip: Optional[str] = None,
        format: Optional[str] = None,
        priority: Optional[str] = None,
        max_log_rate: Optional[int] = None,
        enc_algorithm: Optional[str] = None,
        ssl_min_proto_version: Optional[str] = None,
        certificate: Optional[str] = None,
        custom_field_name: Optional[list[dict[str, Any]]] = None,
        interface_select_method: Optional[str] = None,
        interface: Optional[str] = None,
        source_ip_interface: Optional[str] = None,
        use_management_vdom: Optional[str] = None,
        vrf_select: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update syslogd3 override settings.

        Supports three usage patterns:
        1. Dictionary: update(data_dict={'status': 'enable'})
        2. Keywords: update(status='enable', server='192.168.1.100')
        3. Mixed: update(data_dict={...}, status='enable')

        Args:
            data_dict: Complete configuration dictionary
            status: Enable/disable override syslog settings for this VDOM
            server: Address of remote syslog server
            mode: Remote syslog logging over UDP/Reliable TCP
            port: Server listen port
            facility: Remote syslog facility
            source_ip: Source IP address of syslog
            format: Log format
            priority: Set log transmission priority
            max_log_rate: Syslog maximum log rate in MBps (0 = unlimited)
            enc_algorithm: Enable/disable reliable syslogging with TLS encryption
            ssl_min_proto_version: Minimum supported protocol version for SSL/TLS connections
            certificate: Certificate used to communicate with syslog server
            custom_field_name: Custom field name for CEF format logging
            interface_select_method: Specify how to select outgoing interface to reach server
            interface: Specify outgoing interface to reach server
            source_ip_interface: Source IP interface name
            use_management_vdom: Enable/disable use of management VDOM
            vrf_select: Select VRF
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            Update result

        Examples:
            >>> # Enable override with server
            >>> fgt.api.cmdb.log.syslogd.override_setting.update(
            ...     status='enable',
            ...     server='192.168.1.100'
            ... )

            >>> # Configure syslog server settings
            >>> fgt.api.cmdb.log.syslogd.override_setting.update(
            ...     server='syslog.example.com',
            ...     port=514,
            ...     mode='udp',
            ...     facility='local7'
            ... )

            >>> # PUT - Update with dictionary
            >>> config = {
            ...     'status': 'enable',
            ...     'server': '192.168.1.100',
            ...     'port': 514,
            ...     'facility': 'local7'
            ... }
            >>> fgt.api.cmdb.log.syslogd.override_setting.update(data_dict=config)
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "status": status,
            "server": server,
            "mode": mode,
            "port": port,
            "facility": facility,
            "source_ip": source_ip,
            "format": format,
            "priority": priority,
            "max_log_rate": max_log_rate,
            "enc_algorithm": enc_algorithm,
            "ssl_min_proto_version": ssl_min_proto_version,
            "certificate": certificate,
            "custom_field_name": custom_field_name,
            "interface_select_method": interface_select_method,
            "interface": interface,
            "source_ip_interface": source_ip_interface,
            "use_management_vdom": use_management_vdom,
            "vrf_select": vrf_select,
        }

        api_field_map = {
            "status": "status",
            "server": "server",
            "mode": "mode",
            "port": "port",
            "facility": "facility",
            "source_ip": "source-ip",
            "format": "format",
            "priority": "priority",
            "max_log_rate": "max-log-rate",
            "enc_algorithm": "enc-algorithm",
            "ssl_min_proto_version": "ssl-min-proto-version",
            "certificate": "certificate",
            "custom_field_name": "custom-field-name",
            "interface_select_method": "interface-select-method",
            "interface": "interface",
            "source_ip_interface": "source-ip-interface",
            "use_management_vdom": "use-management-vdom",
            "vrf_select": "vrf-select",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = "log.syslogd3/override-setting"
        return self._client.put("cmdb", path, data=data, vdom=vdom)
