"""
FortiOS CMDB - Firewall SSH Settings
SSH proxy settings.

API Endpoints:
    GET    /api/v2/cmdb/firewall.ssh/setting  - Get SSH proxy settings
    PUT    /api/v2/cmdb/firewall.ssh/setting  - Update SSH proxy settings
"""

from typing import Optional, Union, List


class Setting:
    """SSH proxy settings endpoint (singleton)"""
    
    def __init__(self, client):
        self._client = client
    
    def get(
        self,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Get SSH proxy settings.
        
        Args:
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Enable skip operator
            action: Special actions - 'default', 'schema', 'revision'
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Get SSH proxy settings
            >>> result = fgt.cmdb.firewall.ssh.setting.get()
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.ssh.setting.get(with_meta=True)
        """
        params = {}
        param_map = {
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'action': action,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)
        
        return self._client.get('cmdb', 'firewall.ssh/setting', params=params if params else None, vdom=vdom)
    
    def update(
        self,
        caname: Optional[str] = None,
        untrusted_caname: Optional[str] = None,
        host_trusted_checking: Optional[str] = None,
        hostkey_rsa2048: Optional[str] = None,
        hostkey_dsa1024: Optional[str] = None,
        hostkey_ecdsa256: Optional[str] = None,
        hostkey_ecdsa384: Optional[str] = None,
        hostkey_ecdsa521: Optional[str] = None,
        hostkey_ed25519: Optional[str] = None,
        ssh_policy_check: Optional[str] = None,
        ssh_tun_policy_check: Optional[str] = None,
        log_violation: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs
    ) -> HTTPResponse:
        """
        Update SSH proxy settings.
        
        Args:
            caname: CA certificate name
            untrusted_caname: Untrusted CA certificate name
            host_trusted_checking: Enable/disable host trusted checking - 'enable' or 'disable'
            hostkey_rsa2048: RSA 2048-bit host key name
            hostkey_dsa1024: DSA 1024-bit host key name
            hostkey_ecdsa256: ECDSA 256-bit host key name
            hostkey_ecdsa384: ECDSA 384-bit host key name
            hostkey_ecdsa521: ECDSA 521-bit host key name
            hostkey_ed25519: ED25519 host key name
            ssh_policy_check: Enable/disable SSH policy check - 'enable' or 'disable'
            ssh_tun_policy_check: Enable/disable SSH tunnel policy check - 'enable' or 'disable'
            log_violation: Enable/disable logging of violations - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update CA certificate
            >>> result = fgt.cmdb.firewall.ssh.setting.update(
            ...     caname='Fortinet_CA_SSL',
            ...     host_trusted_checking='enable'
            ... )
            
            >>> # Enable SSH policy check
            >>> result = fgt.cmdb.firewall.ssh.setting.update(
            ...     ssh_policy_check='enable',
            ...     log_violation='enable'
            ... )
            
            >>> # Configure host keys
            >>> result = fgt.cmdb.firewall.ssh.setting.update(
            ...     hostkey_rsa2048='rsa-key-2048',
            ...     hostkey_ecdsa256='ecdsa-key-256'
            ... )
        """
        data = {}
        
        param_map = {
            'caname': caname,
            'untrusted_caname': untrusted_caname,
            'host_trusted_checking': host_trusted_checking,
            'hostkey_rsa2048': hostkey_rsa2048,
            'hostkey_dsa1024': hostkey_dsa1024,
            'hostkey_ecdsa256': hostkey_ecdsa256,
            'hostkey_ecdsa384': hostkey_ecdsa384,
            'hostkey_ecdsa521': hostkey_ecdsa521,
            'hostkey_ed25519': hostkey_ed25519,
            'ssh_policy_check': ssh_policy_check,
            'ssh_tun_policy_check': ssh_tun_policy_check,
            'log_violation': log_violation,
        }
        
        api_field_map = {
            'caname': 'caname',
            'untrusted_caname': 'untrusted-caname',
            'host_trusted_checking': 'host-trusted-checking',
            'hostkey_rsa2048': 'hostkey-rsa2048',
            'hostkey_dsa1024': 'hostkey-dsa1024',
            'hostkey_ecdsa256': 'hostkey-ecdsa256',
            'hostkey_ecdsa384': 'hostkey-ecdsa384',
            'hostkey_ecdsa521': 'hostkey-ecdsa521',
            'hostkey_ed25519': 'hostkey-ed25519',
            'ssh_policy_check': 'ssh-policy-check',
            'ssh_tun_policy_check': 'ssh-tun-policy-check',
            'log_violation': 'log-violation',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        data.update(kwargs)
        
        return self._client.put('cmdb', 'firewall.ssh/setting', data, vdom=vdom)
