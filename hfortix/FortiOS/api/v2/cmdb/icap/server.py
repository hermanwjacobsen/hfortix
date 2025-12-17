"""
FortiOS CMDB - ICAP Server

Configure ICAP servers for content inspection.

API Endpoints:
    GET    /api/v2/cmdb/icap/server           - List all / Get specific
    POST   /api/v2/cmdb/icap/server           - Create
    PUT    /api/v2/cmdb/icap/server/{name}   - Update
    DELETE /api/v2/cmdb/icap/server/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class Server:
    """ICAP Server endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all ICAP servers.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing list of ICAP servers

        Examples:
            >>> # List all servers
            >>> servers = fgt.api.cmdb.icap.server.list()
            >>> for server in servers['results']:
            ...     print(server['name'], server['ip-address'])
        """
        path = "icap/server"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def get(
        self,
        name: str,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get specific ICAP server.

        Args:
            name: Server name
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Skip hidden properties
            action: Additional action to perform
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing server configuration

        Examples:
            >>> # Get specific server
            >>> server = fgt.api.cmdb.icap.server.get('icap-server1')
            >>> print(server['ip-address'], server['port'])
        """
        params = {}
        param_map = {
            "datasource": datasource,
            "with-meta": with_meta,
            "skip": skip,
            "action": action,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        path = f"icap/server/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        addr_type: Optional[str] = None,
        ip_address: Optional[str] = None,
        ip_version: Optional[str] = None,
        ip6_address: Optional[str] = None,
        fqdn: Optional[str] = None,
        port: Optional[int] = None,
        max_connections: Optional[int] = None,
        secure: Optional[str] = None,
        ssl_cert: Optional[str] = None,
        healthcheck: Optional[str] = None,
        healthcheck_service: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create ICAP server.

        Supports three usage patterns:

        1. Dictionary pattern (template-based):
           >>> config = {'name': 'icap1', 'ip-address': '10.0.1.100', 'port': 1344}
           >>> fgt.api.cmdb.icap.server.create(data_dict=config)

        2. Keyword pattern (explicit parameters):
           >>> fgt.api.cmdb.icap.server.create(
           ...     name='icap1',
           ...     ip_address='10.0.1.100',
           ...     port=1344
           ... )

        3. Mixed pattern (template + overrides):
           >>> base = {'ip-address': '10.0.1.100', 'port': 1344}
           >>> fgt.api.cmdb.icap.server.create(data_dict=base, name='icap1')

        Args:
            data_dict: Complete configuration dictionary (pattern 1 & 3)
            name: Server name
            addr_type: Address type (ip4/ip6/fqdn)
            ip_address: IPv4 address of ICAP server
            ip_version: IP version (4 or 6)
            ip6_address: IPv6 address of ICAP server
            fqdn: Fully Qualified Domain Name
            port: ICAP server port (default: 1344)
            max_connections: Maximum number of connections (0 = unlimited, must not be less than wad-worker-count)
            secure: Enable/disable secure ICAP connection - ICAPS (enable/disable)
            ssl_cert: CA certificate name for ICAPS
            healthcheck: Enable/disable ICAP server health checking (enable/disable)
            healthcheck_service: ICAP Service name for health checks
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing creation result

        Examples:
            >>> # POST - Create with dictionary
            >>> config = {
            ...     'name': 'icap-server1',
            ...     'ip-address': '10.0.1.100',
            ...     'port': 1344,
            ...     'healthcheck': 'enable'
            ... }
            >>> result = fgt.api.cmdb.icap.server.create(data_dict=config)

            >>> # POST - Create with keywords
            >>> result = fgt.api.cmdb.icap.server.create(
            ...     name='icap-server2',
            ...     ip_address='10.0.1.101',
            ...     port=1344,
            ...     max_connections=100
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "name": name,
            "addr_type": addr_type,
            "ip_address": ip_address,
            "ip_version": ip_version,
            "ip6_address": ip6_address,
            "fqdn": fqdn,
            "port": port,
            "max_connections": max_connections,
            "secure": secure,
            "ssl_cert": ssl_cert,
            "healthcheck": healthcheck,
            "healthcheck_service": healthcheck_service,
        }

        api_field_map = {
            "name": "name",
            "addr_type": "addr-type",
            "ip_address": "ip-address",
            "ip_version": "ip-version",
            "ip6_address": "ip6-address",
            "fqdn": "fqdn",
            "port": "port",
            "max_connections": "max-connections",
            "secure": "secure",
            "ssl_cert": "ssl-cert",
            "healthcheck": "healthcheck",
            "healthcheck_service": "healthcheck-service",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = "icap/server"
        return self._client.post("cmdb", path, data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        addr_type: Optional[str] = None,
        ip_address: Optional[str] = None,
        ip_version: Optional[str] = None,
        ip6_address: Optional[str] = None,
        fqdn: Optional[str] = None,
        port: Optional[int] = None,
        max_connections: Optional[int] = None,
        secure: Optional[str] = None,
        ssl_cert: Optional[str] = None,
        healthcheck: Optional[str] = None,
        healthcheck_service: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update ICAP server.

        Supports three usage patterns:

        1. Dictionary pattern (template-based):
           >>> config = {'port': 1345, 'max-connections': 200}
           >>> fgt.api.cmdb.icap.server.update('icap1', data_dict=config)

        2. Keyword pattern (explicit parameters):
           >>> fgt.api.cmdb.icap.server.update(
           ...     'icap1',
           ...     port=1345,
           ...     max_connections=200
           ... )

        3. Mixed pattern (template + overrides):
           >>> base = {'port': 1344}
           >>> fgt.api.cmdb.icap.server.update('icap1', data_dict=base, healthcheck='enable')

        Args:
            name: Server name
            data_dict: Complete configuration dictionary (pattern 1 & 3)
            addr_type: Address type (ip4/ip6/fqdn)
            ip_address: IPv4 address of ICAP server
            ip_version: IP version (4 or 6)
            ip6_address: IPv6 address of ICAP server
            fqdn: Fully Qualified Domain Name
            port: ICAP server port
            max_connections: Maximum number of connections (0 = unlimited)
            secure: Enable/disable secure ICAP connection - ICAPS (enable/disable)
            ssl_cert: CA certificate name for ICAPS
            healthcheck: Enable/disable ICAP server health checking (enable/disable)
            healthcheck_service: ICAP Service name for health checks
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # PUT - Update with dictionary
            >>> config = {'port': 1345, 'healthcheck': 'enable'}
            >>> result = fgt.api.cmdb.icap.server.update('icap-server1', data_dict=config)

            >>> # PUT - Update with keywords
            >>> result = fgt.api.cmdb.icap.server.update(
            ...     'icap-server1',
            ...     max_connections=150
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "addr_type": addr_type,
            "ip_address": ip_address,
            "ip_version": ip_version,
            "ip6_address": ip6_address,
            "fqdn": fqdn,
            "port": port,
            "max_connections": max_connections,
            "secure": secure,
            "ssl_cert": ssl_cert,
            "healthcheck": healthcheck,
            "healthcheck_service": healthcheck_service,
        }

        api_field_map = {
            "addr_type": "addr-type",
            "ip_address": "ip-address",
            "ip_version": "ip-version",
            "ip6_address": "ip6-address",
            "fqdn": "fqdn",
            "port": "port",
            "max_connections": "max-connections",
            "secure": "secure",
            "ssl_cert": "ssl-cert",
            "healthcheck": "healthcheck",
            "healthcheck_service": "healthcheck-service",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = f"icap/server/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete ICAP server.

        Args:
            name: Server name
            vdom: Virtual domain name or False for global

        Returns:
            Dictionary containing deletion result

        Examples:
            >>> # Delete server
            >>> result = fgt.api.cmdb.icap.server.delete('old-server')
            >>> print(result['status'])
        """
        path = f"icap/server/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if ICAP server exists.

        Args:
            name: Server name
            vdom: Virtual domain name or False for global

        Returns:
            True if server exists, False otherwise

        Examples:
            >>> # Check if server exists
            >>> if fgt.api.cmdb.icap.server.exists('icap-server1'):
            ...     print("Server exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
