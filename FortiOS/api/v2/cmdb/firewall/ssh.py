"""
FortiOS CMDB - Firewall SSH Sub-category

This module provides access to firewall SSH proxy endpoints.
"""


class Ssh:
    """Firewall SSH proxy sub-category"""
    
    def __init__(self, client):
        self._client = client
        self._host_key = None
        self._local_ca = None
        self._local_key = None
        self._setting = None
    
    @property
    def host_key(self):
        """Access firewall.ssh/host-key endpoint"""
        if self._host_key is None:
            from .ssh_host_key import HostKey
            self._host_key = HostKey(self._client)
        return self._host_key
    
    @property
    def local_ca(self):
        """Access firewall.ssh/local-ca endpoint"""
        if self._local_ca is None:
            from .ssh_local_ca import LocalCa
            self._local_ca = LocalCa(self._client)
        return self._local_ca
    
    @property
    def local_key(self):
        """Access firewall.ssh/local-key endpoint"""
        if self._local_key is None:
            from .ssh_local_key import LocalKey
            self._local_key = LocalKey(self._client)
        return self._local_key
    
    @property
    def setting(self):
        """Access firewall.ssh/setting endpoint"""
        if self._setting is None:
            from .ssh_setting import Setting
            self._setting = Setting(self._client)
        return self._setting
