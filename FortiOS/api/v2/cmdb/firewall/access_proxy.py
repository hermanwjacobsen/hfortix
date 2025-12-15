"""
FortiOS Access Proxy Endpoint
API endpoint for managing IPv4 access proxy configuration.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class AccessProxy:
    """
    Manage IPv4 access proxy configuration
    
    This endpoint configures IPv4 access proxy for secure application access.
    """

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Access Proxy endpoint
        
        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._path = 'firewall/access-proxy'

    def list(self, vdom: str | None = None, **params: Any) -> dict[str, Any]:
        """
        List all IPv4 access proxies
        
        Args:
            vdom: Virtual domain name
            **params: Additional query parameters
        
        Returns:
            API response containing list of access proxies
            
        Example:
            >>> proxies = fgt.cmdb.firewall.access_proxy.list()
            >>> print(f"Total proxies: {len(proxies['results'])}")
        """
        return self._client.cmdb._get(self._path, vdom=vdom, params=params)

    def get(self, name: str | None = None, vdom: str | None = None, **params: Any) -> dict[str, Any]:
        """
        Get IPv4 access proxy by name or all proxies
        
        Args:
            name: Access proxy name (None to get all)
            vdom: Virtual domain name
            **params: Additional query parameters (filter, format, etc.)
        
        Returns:
            API response with proxy details
            
        Example:
            >>> # Get specific proxy
            >>> proxy = fgt.cmdb.firewall.access_proxy.get('proxy1')
            >>> print(f"VIP: {proxy['results'][0]['vip']}")
            
            >>> # Get all proxies
            >>> proxies = fgt.cmdb.firewall.access_proxy.get()
        """
        if name is not None:
            path = f'{self._path}/{name}'
        else:
            path = self._path
        return self._client.cmdb._get(path, vdom=vdom, params=params)

    def create(
        self,
        name: str,
        vip: str | dict[str, str] | None = None,
        client_cert: str | None = None,
        auth_portal: str = 'disable',
        auth_virtual_host: str | None = None,
        empty_cert_action: str = 'accept',
        log_blocked_traffic: str = 'enable',
        add_vhost_domain_to_dnsdb: str = 'disable',
        http_supported_max_version: str = '1.1',
        svr_pool_multiplex: str = 'enable',
        svr_pool_ttl: int = 15,
        svr_pool_server_max_request: int = 1000,
        svr_pool_server_max_concurrent_request: int = 0,
        decapped_traffic_mirror: str | None = None,
        api_gateway: list[dict[str, Any]] | None = None,
        api_gateway6: list[dict[str, Any]] | None = None,
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Create new IPv4 access proxy
        
        Args:
            name: Access proxy name
            vip: Virtual IP name (string) or dict with q_origin_key
            client_cert: Enable/disable client certificate request
            auth_portal: Enable/disable authentication portal ['enable'|'disable']
            auth_virtual_host: Virtual host for authentication portal
            empty_cert_action: Action when client certificate is missing ['accept'|'block']
            log_blocked_traffic: Enable/disable logging blocked traffic
            add_vhost_domain_to_dnsdb: Add vhost domain to DNS database
            http_supported_max_version: Maximum HTTP version ['1.1'|'2.0']
            svr_pool_multiplex: Enable reusing server connections
            svr_pool_ttl: Server pool TTL (1-3600 seconds)
            svr_pool_server_max_request: Maximum requests per server
            svr_pool_server_max_concurrent_request: Max concurrent requests
            decapped_traffic_mirror: Decapped traffic mirror
            api_gateway: API gateway configuration
            api_gateway6: IPv6 API gateway configuration
            vdom: Virtual domain name
        
        Returns:
            API response
            
        Example:
            >>> # Simple format (recommended)
            >>> result = fgt.cmdb.firewall.access_proxy.create(
            ...     name='proxy1',
            ...     vip='vip1',
            ...     auth_portal='enable',
            ...     log_blocked_traffic='enable'
            ... )
            
            >>> # Dict format also supported
            >>> result = fgt.cmdb.firewall.access_proxy.create(
            ...     name='proxy1',
            ...     vip={'q_origin_key': 'vip1'},
            ...     auth_portal='enable'
            ... )
        """
        data: dict[str, Any] = {
            'name': name,
            'auth-portal': auth_portal,
            'empty-cert-action': empty_cert_action,
            'log-blocked-traffic': log_blocked_traffic,
            'add-vhost-domain-to-dnsdb': add_vhost_domain_to_dnsdb,
            'http-supported-max-version': http_supported_max_version,
            'svr-pool-multiplex': svr_pool_multiplex,
            'svr-pool-ttl': svr_pool_ttl,
            'svr-pool-server-max-request': svr_pool_server_max_request,
            'svr-pool-server-max-concurrent-request': svr_pool_server_max_concurrent_request
        }
        
        if vip is not None:
            # VIP should be a string (VIP name from firewall/vip)
            if isinstance(vip, dict):
                # If dict provided, extract the name/q_origin_key
                vip_name = vip.get('q_origin_key') or vip.get('name', '')
                data['vip'] = vip_name
            else:
                data['vip'] = vip
        if client_cert is not None:
            data['client-cert'] = client_cert
        if auth_virtual_host is not None:
            data['auth-virtual-host'] = auth_virtual_host
        if decapped_traffic_mirror is not None:
            data['decapped-traffic-mirror'] = decapped_traffic_mirror
        if api_gateway is not None:
            data['api-gateway'] = api_gateway
        if api_gateway6 is not None:
            data['api-gateway6'] = api_gateway6
            
        return self._client.cmdb._post(self._path, data=data, vdom=vdom)

    def update(
        self,
        name: str,
        vip: str | None = None,
        client_cert: str | None = None,
        auth_portal: str | None = None,
        auth_virtual_host: str | None = None,
        empty_cert_action: str | None = None,
        log_blocked_traffic: str | None = None,
        add_vhost_domain_to_dnsdb: str | None = None,
        http_supported_max_version: str | None = None,
        svr_pool_multiplex: str | None = None,
        svr_pool_ttl: int | None = None,
        svr_pool_server_max_request: int | None = None,
        svr_pool_server_max_concurrent_request: int | None = None,
        decapped_traffic_mirror: str | None = None,
        api_gateway: list[dict[str, Any]] | None = None,
        api_gateway6: list[dict[str, Any]] | None = None,
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Update existing IPv4 access proxy
        
        Args:
            name: Access proxy name to update
            vip: Virtual IP name
            client_cert: Enable/disable client certificate request
            auth_portal: Enable/disable authentication portal
            auth_virtual_host: Virtual host for authentication portal
            empty_cert_action: Action when client certificate is missing
            log_blocked_traffic: Enable/disable logging blocked traffic
            add_vhost_domain_to_dnsdb: Add vhost domain to DNS database
            http_supported_max_version: Maximum HTTP version
            svr_pool_multiplex: Enable reusing server connections
            svr_pool_ttl: Server pool TTL
            svr_pool_server_max_request: Maximum requests per server
            svr_pool_server_max_concurrent_request: Max concurrent requests
            decapped_traffic_mirror: Decapped traffic mirror
            api_gateway: API gateway configuration
            api_gateway6: IPv6 API gateway configuration
            vdom: Virtual domain name
        
        Returns:
            API response
            
        Example:
            >>> result = fgt.cmdb.firewall.access_proxy.update(
            ...     name='proxy1',
            ...     auth_portal='disable'
            ... )
        """
        data: dict[str, Any] = {}
        
        if vip is not None:
            data['vip'] = vip
        if client_cert is not None:
            data['client-cert'] = client_cert
        if auth_portal is not None:
            data['auth-portal'] = auth_portal
        if auth_virtual_host is not None:
            data['auth-virtual-host'] = auth_virtual_host
        if empty_cert_action is not None:
            data['empty-cert-action'] = empty_cert_action
        if log_blocked_traffic is not None:
            data['log-blocked-traffic'] = log_blocked_traffic
        if add_vhost_domain_to_dnsdb is not None:
            data['add-vhost-domain-to-dnsdb'] = add_vhost_domain_to_dnsdb
        if http_supported_max_version is not None:
            data['http-supported-max-version'] = http_supported_max_version
        if svr_pool_multiplex is not None:
            data['svr-pool-multiplex'] = svr_pool_multiplex
        if svr_pool_ttl is not None:
            data['svr-pool-ttl'] = svr_pool_ttl
        if svr_pool_server_max_request is not None:
            data['svr-pool-server-max-request'] = svr_pool_server_max_request
        if svr_pool_server_max_concurrent_request is not None:
            data['svr-pool-server-max-concurrent-request'] = svr_pool_server_max_concurrent_request
        if decapped_traffic_mirror is not None:
            data['decapped-traffic-mirror'] = decapped_traffic_mirror
        if api_gateway is not None:
            data['api-gateway'] = api_gateway
        if api_gateway6 is not None:
            data['api-gateway6'] = api_gateway6
            
        path = f'{self._path}/{name}'
        return self._client.cmdb._put(path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: str | None = None) -> dict[str, Any]:
        """
        Delete IPv4 access proxy
        
        Args:
            name: Access proxy name to delete
            vdom: Virtual domain name
        
        Returns:
            API response
            
        Example:
            >>> result = fgt.cmdb.firewall.access_proxy.delete('proxy1')
        """
        path = f'{self._path}/{name}'
        return self._client.cmdb._delete(path, vdom=vdom)

    def exists(self, name: str, vdom: str | None = None) -> bool:
        """
        Check if IPv4 access proxy exists
        
        Args:
            name: Access proxy name to check
            vdom: Virtual domain name
        
        Returns:
            True if proxy exists, False otherwise
            
        Example:
            >>> if fgt.cmdb.firewall.access_proxy.exists('proxy1'):
            ...     print("Access proxy exists")
        """
        try:
            result = self.get(name=name, vdom=vdom)
            return result.get('status') == 'success' and len(result.get('results', [])) > 0
        except Exception:
            return False
