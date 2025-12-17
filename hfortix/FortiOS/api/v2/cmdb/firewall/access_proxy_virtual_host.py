"""
FortiOS Access Proxy Virtual Host Endpoint
API endpoint for managing Access Proxy virtual hosts.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class AccessProxyVirtualHost:
    """
    Manage Access Proxy virtual hosts

    This endpoint configures virtual hosts for access proxy.
    """

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Access Proxy Virtual Host endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._path = "firewall/access-proxy-virtual-host"

    def list(
        self, vdom: str | None = None, raw_json: bool = False, **params: Any
    ) -> dict[str, Any]:
        """
        List all access proxy virtual hosts

        Args:
            vdom: Virtual domain name
            raw_json: If True, return raw JSON response without unwrapping
            **params: Additional query parameters

        Returns:
            API response containing list of virtual hosts

        Example:
            >>> vhosts = fgt.cmdb.firewall.access_proxy_virtual_host.list()
            >>> print(f"Total virtual hosts: {len(vhosts['results'])}")
        """
        return self._client.get("cmdb", self._path, vdom=vdom, params=params, raw_json=raw_json)

    def get(
        self,
        name: str | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
        **params: Any,
    ) -> dict[str, Any]:
        """
        Get virtual host by name or all virtual hosts

        Args:
            name: Virtual host name (None to get all)
            vdom: Virtual domain name
            **params: Additional query parameters (filter, format, etc.)

        Returns:
            API response with virtual host details

        Example:
            >>> # Get specific virtual host
            >>> vhost = fgt.cmdb.firewall.access_proxy_virtual_host.get('vhost1')
            >>> print(f"Host: {vhost['results'][0]['host']}")

            >>> # Get all virtual hosts
            >>> vhosts = fgt.cmdb.firewall.access_proxy_virtual_host.get()
        """
        if name is not None:
            path = f"{self._path}/{encode_path_component(name)}"
        else:
            path = self._path
        return self._client.get("cmdb", path, vdom=vdom, params=params, raw_json=raw_json)

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        host: Optional[str] = None,
        host_type: str = "sub-string",
        ssl_certificate: str | list[dict[str, str]] | None = None,
        replacemsg_group: str | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Create virtual host

        Args:
            name: Virtual host name
            host: Domain name or IP address pattern
            host_type: Host matching type ['sub-string'|'wildcard'|'regex']
            ssl_certificate: SSL certificate name (string) or list of cert dicts
            replacemsg_group: Replacement message group
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> # Simple format (recommended)
            >>> result = fgt.cmdb.firewall.access_proxy_virtual_host.create(
            ...     name='vhost1',
            ...     host='*.example.com',
            ...     host_type='wildcard',
            ...     ssl_certificate='Fortinet_Factory'
            ... )

            >>> # Dict format also supported
            >>> result = fgt.cmdb.firewall.access_proxy_virtual_host.create(
            ...     name='vhost1',
            ...     host='*.example.com',
            ...     host_type='wildcard',
            ...     ssl_certificate=[{'name': 'Fortinet_Factory'}]
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
            if host_type is not None:
                payload["host-type"] = host_type
            if host is not None:
                payload["host"] = host
            if ssl_certificate is not None:
                # Convert string to list of dicts format
                if isinstance(ssl_certificate, str):
                    payload["ssl-certificate"] = [{"name": ssl_certificate}]
                else:
                    payload["ssl-certificate"] = ssl_certificate
            if replacemsg_group is not None:
                payload["replacemsg-group"] = replacemsg_group

        return self._client.post("cmdb", self._path, data=payload, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        host: Optional[str] = None,
        host_type: str | None = None,
        ssl_certificate: str | list[dict[str, str]] | None = None,
        replacemsg_group: str | None = None,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Update virtual host

        Args:
            name: Virtual host name to update
            host: Domain name or IP address pattern
            host_type: Host matching type
            ssl_certificate: SSL certificate name (string) or list of cert dicts
            replacemsg_group: Replacement message group
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> result = fgt.cmdb.firewall.access_proxy_virtual_host.update(
            ...     name='vhost1',
            ...     ssl_certificate='NewCertificate'
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

            if host is not None:
                payload["host"] = host
            if host_type is not None:
                payload["host-type"] = host_type
            if ssl_certificate is not None:
                # Convert string to list of dicts format
                if isinstance(ssl_certificate, str):
                    payload["ssl-certificate"] = [{"name": ssl_certificate}]
                else:
                    payload["ssl-certificate"] = ssl_certificate
            if replacemsg_group is not None:
                payload["replacemsg-group"] = replacemsg_group

        path = f"{self._path}/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: str | None = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete virtual host

        Args:
            name: Virtual host name to delete
            vdom: Virtual domain name

        Returns:
            API response

        Example:
            >>> result = fgt.cmdb.firewall.access_proxy_virtual_host.delete('vhost1')
        """
        path = f"{self._path}/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, name: str, vdom: str | None = None) -> bool:
        """
        Check if virtual host exists

        Args:
            name: Virtual host name to check
            vdom: Virtual domain name

        Returns:
            True if virtual host exists, False otherwise

        Example:
            >>> if fgt.cmdb.firewall.access_proxy_virtual_host.exists('vhost1'):
            ...     print("Virtual host exists")
        """
        try:
            result = self.get(name=name, vdom=vdom, raw_json=True)
            return result.get("status") == "success" and len(result.get("results", [])) > 0
        except Exception:
            return False
