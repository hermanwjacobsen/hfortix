"""
FortiOS Access Proxy SSH Client Certificate Endpoint
API endpoint for managing Access Proxy SSH client certificates.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class AccessProxySshClientCert:
    """
    Manage Access Proxy SSH client certificates
    
    This endpoint configures SSH client certificates for access proxy authentication.
    """

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Access Proxy SSH Client Cert endpoint
        
        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._path = 'firewall/access-proxy-ssh-client-cert'

    def list(self, vdom: str | None = None, **params: Any) -> dict[str, Any]:
        """
        List all access proxy SSH client certificates
        
        Args:
            vdom: Virtual domain name
            **params: Additional query parameters
        
        Returns:
            API response containing list of SSH client certificates
            
        Example:
            >>> certs = fgt.cmdb.firewall.access_proxy_ssh_client_cert.list()
            >>> print(f"Total certificates: {len(certs['results'])}")
        """
        return self._client.cmdb._get(self._path, vdom=vdom, params=params)

    def get(self, name: str | None = None, vdom: str | None = None, **params: Any) -> dict[str, Any]:
        """
        Get SSH client certificate by name or all certificates
        
        Args:
            name: Certificate name (None to get all)
            vdom: Virtual domain name
            **params: Additional query parameters (filter, format, etc.)
        
        Returns:
            API response with certificate details
            
        Example:
            >>> # Get specific certificate
            >>> cert = fgt.cmdb.firewall.access_proxy_ssh_client_cert.get('cert1')
            >>> print(f"Auth CA: {cert['results'][0]['auth-ca']}")
            
            >>> # Get all certificates
            >>> certs = fgt.cmdb.firewall.access_proxy_ssh_client_cert.get()
        """
        if name is not None:
            path = f'{self._path}/{name}'
        else:
            path = self._path
        return self._client.cmdb._get(path, vdom=vdom, params=params)

    def create(
        self,
        name: str,
        auth_ca: str,
        cert_extension: list[dict[str, Any]] | None = None,
        permit_agent_forwarding: str = 'enable',
        permit_port_forwarding: str = 'enable',
        permit_pty: str = 'enable',
        permit_user_rc: str = 'enable',
        permit_x11_forwarding: str = 'enable',
        source_address: str = 'enable',
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Create new SSH client certificate configuration
        
        Args:
            name: Certificate name
            auth_ca: SSH CA name for authentication
            cert_extension: Certificate extension configuration
            permit_agent_forwarding: Allow SSH agent forwarding ['enable'|'disable']
            permit_port_forwarding: Allow port forwarding ['enable'|'disable']
            permit_pty: Allow PTY allocation ['enable'|'disable']
            permit_user_rc: Allow user RC file execution ['enable'|'disable']
            permit_x11_forwarding: Allow X11 forwarding ['enable'|'disable']
            source_address: Enable source address validation ['enable'|'disable']
            vdom: Virtual domain name
        
        Returns:
            API response
            
        Example:
            >>> result = fgt.cmdb.firewall.access_proxy_ssh_client_cert.create(
            ...     name='ssh-cert1',
            ...     auth_ca='CA_Cert_1',
            ...     permit_agent_forwarding='enable',
            ...     permit_port_forwarding='disable'
            ... )
        """
        data: dict[str, Any] = {
            'name': name,
            'auth-ca': auth_ca,
            'permit-agent-forwarding': permit_agent_forwarding,
            'permit-port-forwarding': permit_port_forwarding,
            'permit-pty': permit_pty,
            'permit-user-rc': permit_user_rc,
            'permit-x11-forwarding': permit_x11_forwarding,
            'source-address': source_address
        }
        
        if cert_extension is not None:
            data['cert-extension'] = cert_extension
            
        return self._client.cmdb._post(self._path, data=data, vdom=vdom)

    def update(
        self,
        name: str,
        auth_ca: str | None = None,
        cert_extension: list[dict[str, Any]] | None = None,
        permit_agent_forwarding: str | None = None,
        permit_port_forwarding: str | None = None,
        permit_pty: str | None = None,
        permit_user_rc: str | None = None,
        permit_x11_forwarding: str | None = None,
        source_address: str | None = None,
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Update existing SSH client certificate configuration
        
        Args:
            name: Certificate name to update
            auth_ca: SSH CA name for authentication
            cert_extension: Certificate extension configuration
            permit_agent_forwarding: Allow SSH agent forwarding
            permit_port_forwarding: Allow port forwarding
            permit_pty: Allow PTY allocation
            permit_user_rc: Allow user RC file execution
            permit_x11_forwarding: Allow X11 forwarding
            source_address: Enable source address validation
            vdom: Virtual domain name
        
        Returns:
            API response
            
        Example:
            >>> result = fgt.cmdb.firewall.access_proxy_ssh_client_cert.update(
            ...     name='ssh-cert1',
            ...     permit_port_forwarding='enable'
            ... )
        """
        data: dict[str, Any] = {}
        
        if auth_ca is not None:
            data['auth-ca'] = auth_ca
        if cert_extension is not None:
            data['cert-extension'] = cert_extension
        if permit_agent_forwarding is not None:
            data['permit-agent-forwarding'] = permit_agent_forwarding
        if permit_port_forwarding is not None:
            data['permit-port-forwarding'] = permit_port_forwarding
        if permit_pty is not None:
            data['permit-pty'] = permit_pty
        if permit_user_rc is not None:
            data['permit-user-rc'] = permit_user_rc
        if permit_x11_forwarding is not None:
            data['permit-x11-forwarding'] = permit_x11_forwarding
        if source_address is not None:
            data['source-address'] = source_address
            
        path = f'{self._path}/{name}'
        return self._client.cmdb._put(path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: str | None = None) -> dict[str, Any]:
        """
        Delete SSH client certificate configuration
        
        Args:
            name: Certificate name to delete
            vdom: Virtual domain name
        
        Returns:
            API response
            
        Example:
            >>> result = fgt.cmdb.firewall.access_proxy_ssh_client_cert.delete('ssh-cert1')
        """
        path = f'{self._path}/{name}'
        return self._client.cmdb._delete(path, vdom=vdom)

    def exists(self, name: str, vdom: str | None = None) -> bool:
        """
        Check if SSH client certificate exists
        
        Args:
            name: Certificate name to check
            vdom: Virtual domain name
        
        Returns:
            True if certificate exists, False otherwise
            
        Example:
            >>> if fgt.cmdb.firewall.access_proxy_ssh_client_cert.exists('ssh-cert1'):
            ...     print("SSH client certificate exists")
        """
        try:
            result = self.get(name=name, vdom=vdom)
            return result.get('status') == 'success' and len(result.get('results', [])) > 0
        except Exception:
            return False
