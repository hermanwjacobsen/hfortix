"""
FortiOS Access Proxy6 Endpoint
API endpoint for managing IPv6 access proxy configuration.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class AccessProxy6:
    """
    Manage IPv6 access proxy configuration

    This endpoint configures IPv6 access proxy for secure application access.
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Access Proxy6 endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._path = "firewall/access-proxy6"

    def list(
        self, vdom: str | None = None, raw_json: bool = False, **params: Any
    ) -> dict[str, Any]:
        """
        List all IPv6 access proxies

        Args:
            vdom: Virtual domain name
            **params: Additional query parameters

        Returns:
            API response containing list of IPv6 access proxies

        Example:
            >>> proxies = fgt.cmdb.firewall.access_proxy6.list()
            >>> print(f"Total IPv6 proxies: {len(proxies['results'])}")
        """
        return self._client.get("cmdb", self._path, params=params, vdom=vdom, raw_json=raw_json)

    def get(
        self,
        name: str | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """
        Get IPv6 access proxy by name or all proxies

        Args:
            name: Access proxy name (None to get all)
            vdom: Virtual domain name
            **params: Additional query parameters (filter, format, etc.)

        Returns:
            API response with proxy details

        Example:
            >>> # Get specific proxy
            >>> proxy = fgt.cmdb.firewall.access_proxy6.get('proxy6-1')
            >>> print(f"VIP: {proxy['results'][0]['vip']}")

            >>> # Get all proxies
            >>> proxies = fgt.cmdb.firewall.access_proxy6.get()
        """
        if name is not None:
            path = f"{self._path}/{encode_path_component(name)}"
        else:
            path = self._path
        return self._client.get("cmdb", path, params=params, vdom=vdom, raw_json=raw_json)

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        vip: Optional[str] = None,
        client_cert: str | None = None,
        auth_portal: str = "disable",
        auth_virtual_host: str | None = None,
        empty_cert_action: str = "accept",
        log_blocked_traffic: str = "enable",
        add_vhost_domain_to_dnsdb: str = "disable",
        http_supported_max_version: str = "1.1",
        svr_pool_multiplex: str = "enable",
        svr_pool_ttl: int = 15,
        svr_pool_server_max_request: int = 1000,
        svr_pool_server_max_concurrent_request: int = 0,
        decapped_traffic_mirror: str | None = None,
        api_gateway: list[dict[str, Any]] | None = None,
        api_gateway6: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Create new IPv6 access proxy

        Args:
            name: Access proxy name
            vip: IPv6 Virtual IP name
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
            api_gateway: IPv4 API gateway configuration
            api_gateway6: IPv6 API gateway configuration
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> result = fgt.cmdb.firewall.access_proxy6.create(
            ...     name='proxy6-1',
            ...     vip='vip6-1',
            ...     auth_portal='enable',
            ...     log_blocked_traffic='enable'
            ... )
        """
        # Support both patterns: data dict or individual kwargs
        if payload_dict is not None:
            # Pattern 1: data dict provided
            payload = payload_dict.copy()
        else:
            # Pattern 2: build from kwargs
            payload: Dict[str, Any] = {}
            if name is not None:
                payload["name"] = name
            if auth_portal is not None:
                payload["auth-portal"] = auth_portal
            if empty_cert_action is not None:
                payload["empty-cert-action"] = empty_cert_action
            if log_blocked_traffic is not None:
                payload["log-blocked-traffic"] = log_blocked_traffic
            if add_vhost_domain_to_dnsdb is not None:
                payload["add-vhost-domain-to-dnsdb"] = add_vhost_domain_to_dnsdb
            if http_supported_max_version is not None:
                payload["http-supported-max-version"] = http_supported_max_version
            if svr_pool_multiplex is not None:
                payload["svr-pool-multiplex"] = svr_pool_multiplex
            if svr_pool_ttl is not None:
                payload["svr-pool-ttl"] = svr_pool_ttl
            if svr_pool_server_max_request is not None:
                payload["svr-pool-server-max-request"] = svr_pool_server_max_request
            if svr_pool_server_max_concurrent_request is not None:
                payload["svr-pool-server-max-concurrent-request"] = (
                    svr_pool_server_max_concurrent_request
                )

            if vip is not None:
                payload["vip"] = vip
            if client_cert is not None:
                payload["client-cert"] = client_cert
            if auth_virtual_host is not None:
                payload["auth-virtual-host"] = auth_virtual_host
            if decapped_traffic_mirror is not None:
                payload["decapped-traffic-mirror"] = decapped_traffic_mirror
            if api_gateway is not None:
                payload["api-gateway"] = api_gateway
            if api_gateway6 is not None:
                payload["api-gateway6"] = api_gateway6

        return self._client.post("cmdb", self._path, data=payload, vdom=vdom, raw_json=raw_json)

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        vip: Optional[str] = None,
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
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Update existing IPv6 access proxy

        Args:
            name: Access proxy name to update
            vip: IPv6 Virtual IP name
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
            api_gateway: IPv4 API gateway configuration
            api_gateway6: IPv6 API gateway configuration
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> result = fgt.cmdb.firewall.access_proxy6.update(
            ...     name='proxy6-1',
            ...     auth_portal='disable'
            ... )
        """
        # Support both patterns: data dict or individual kwargs
        if payload_dict is not None:
            # Pattern 1: data dict provided
            payload = payload_dict.copy()
            # Extract name from data if not provided as param
            if name is None:
                name = payload.get("name")
        else:
            # Pattern 2: build from kwargs
            payload: Dict[str, Any] = {}

            if vip is not None:
                payload["vip"] = vip
            if client_cert is not None:
                payload["client-cert"] = client_cert
            if auth_portal is not None:
                payload["auth-portal"] = auth_portal
            if auth_virtual_host is not None:
                payload["auth-virtual-host"] = auth_virtual_host
            if empty_cert_action is not None:
                payload["empty-cert-action"] = empty_cert_action
            if log_blocked_traffic is not None:
                payload["log-blocked-traffic"] = log_blocked_traffic
            if add_vhost_domain_to_dnsdb is not None:
                payload["add-vhost-domain-to-dnsdb"] = add_vhost_domain_to_dnsdb
            if http_supported_max_version is not None:
                payload["http-supported-max-version"] = http_supported_max_version
            if svr_pool_multiplex is not None:
                payload["svr-pool-multiplex"] = svr_pool_multiplex
            if svr_pool_ttl is not None:
                payload["svr-pool-ttl"] = svr_pool_ttl
            if svr_pool_server_max_request is not None:
                payload["svr-pool-server-max-request"] = svr_pool_server_max_request
            if svr_pool_server_max_concurrent_request is not None:
                payload["svr-pool-server-max-concurrent-request"] = (
                    svr_pool_server_max_concurrent_request
                )
            if decapped_traffic_mirror is not None:
                payload["decapped-traffic-mirror"] = decapped_traffic_mirror
            if api_gateway is not None:
                payload["api-gateway"] = api_gateway
            if api_gateway6 is not None:
                payload["api-gateway6"] = api_gateway6

        path = f"{self._path}/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete IPv6 access proxy

        Args:
            name: Access proxy name to delete
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> result = fgt.cmdb.firewall.access_proxy6.delete('proxy6-1')
        """
        path = f"{self._path}/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, name: str, vdom: str | None = None) -> bool:
        """
        Check if IPv6 access proxy exists

        Args:
            name: Access proxy name to check
            vdom: Virtual domain name

        Returns:
            True if proxy exists, False otherwise

        Example:
            >>> if fgt.cmdb.firewall.access_proxy6.exists('proxy6-1'):
            ...     print("IPv6 access proxy exists")
        """
        try:
            result = self.get(name=name, vdom=vdom, raw_json=True)
            return result.get("status") == "success" and len(result.get("results", [])) > 0
        except Exception:
            return False
