"""
FortiOS Firewall API
Firewall configuration endpoints
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient
    from .access_proxy import AccessProxy
    from .access_proxy6 import AccessProxy6
    from .access_proxy_ssh_client_cert import AccessProxySshClientCert
    from .access_proxy_virtual_host import AccessProxyVirtualHost
    from .address import Address
    from .address6 import Address6
    from .address6_template import Address6Template
    from .addrgrp import Addrgrp
    from .addrgrp6 import Addrgrp6
    from .dos_policy import DosPolicy
    from .dos_policy6 import DosPolicy6

__all__ = ['Firewall']

from .ipmacbinding import Ipmacbinding
from .schedule import Schedule
from .service import Service
from .shaper import Shaper
from .ssh import Ssh
from .ssl import Ssl
from .wildcard_fqdn import WildcardFqdn


class Firewall:
    """
    Firewall API helper class
    Provides access to firewall configuration endpoints
    """

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Firewall helper

        Args:
            client: HTTPClient instance
        """
        self._client = client

        # Initialize sub-category classes (firewall.* API paths)
        from .ipmacbinding import Ipmacbinding
        from .schedule import Schedule
        from .service import Service
        from .shaper import Shaper
        from .ssh import Ssh

        self.ipmacbinding = Ipmacbinding(client)
        self.schedule = Schedule(client)
        self.service = Service(client)
        self.shaper = Shaper(client)
        self.ssh = Ssh(client)
        self.ssl = Ssl(client)
        self.wildcard_fqdn = WildcardFqdn(client)

    @property
    def dos_policy(self) -> 'DosPolicy':
        """Access DoS policy endpoint"""
        if not hasattr(self, '__dos_policy'):
            from .dos_policy import DosPolicy
            self.__dos_policy = DosPolicy(self._client)
        return self.__dos_policy

    @property
    def dos_policy6(self) -> 'DosPolicy6':
        """Access DoS policy6 endpoint"""
        if not hasattr(self, '__dos_policy6'):
            from .dos_policy6 import DosPolicy6
            self.__dos_policy6 = DosPolicy6(self._client)
        return self.__dos_policy6

    @property
    def address(self) -> 'Address':
        """Access IPv4 address endpoint"""
        if not hasattr(self, '__address'):
            from .address import Address
            self.__address = Address(self._client)
        return self.__address

    @property
    def address6(self) -> 'Address6':
        """Access IPv6 address endpoint"""
        if not hasattr(self, '__address6'):
            from .address6 import Address6
            self.__address6 = Address6(self._client)
        return self.__address6

    @property
    def address6_template(self) -> 'Address6Template':
        """Access IPv6 address template endpoint"""
        if not hasattr(self, '__address6_template'):
            from .address6_template import Address6Template
            self.__address6_template = Address6Template(self._client)
        return self.__address6_template

    @property
    def addrgrp(self) -> 'Addrgrp':
        """Access IPv4 address group endpoint"""
        if not hasattr(self, '__addrgrp'):
            from .addrgrp import Addrgrp
            self.__addrgrp = Addrgrp(self._client)
        return self.__addrgrp

    @property
    def addrgrp6(self) -> 'Addrgrp6':
        """Access IPv6 address group endpoint"""
        if not hasattr(self, '__addrgrp6'):
            from .addrgrp6 import Addrgrp6
            self.__addrgrp6 = Addrgrp6(self._client)
        return self.__addrgrp6

    @property
    def access_proxy(self) -> 'AccessProxy':
        """Access access proxy endpoint"""
        if not hasattr(self, '__access_proxy'):
            from .access_proxy import AccessProxy
            self.__access_proxy = AccessProxy(self._client)
        return self.__access_proxy

    @property
    def access_proxy6(self) -> 'AccessProxy6':
        """Access access proxy6 endpoint"""
        if not hasattr(self, '__access_proxy6'):
            from .access_proxy6 import AccessProxy6
            self.__access_proxy6 = AccessProxy6(self._client)
        return self.__access_proxy6

    @property
    def access_proxy_ssh_client_cert(self) -> 'AccessProxySshClientCert':
        """Access access proxy SSH client cert endpoint"""
        if not hasattr(self, '__access_proxy_ssh_client_cert'):
            from .access_proxy_ssh_client_cert import AccessProxySshClientCert
            self.__access_proxy_ssh_client_cert = AccessProxySshClientCert(self._client)
        return self.__access_proxy_ssh_client_cert

    @property
    def access_proxy_virtual_host(self) -> 'AccessProxyVirtualHost':
        """Access access proxy virtual host endpoint"""
        if not hasattr(self, '__access_proxy_virtual_host'):
            from .access_proxy_virtual_host import AccessProxyVirtualHost
            self.__access_proxy_virtual_host = AccessProxyVirtualHost(self._client)
        return self.__access_proxy_virtual_host
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            'ipmacbinding', 'schedule', 'service', 'shaper', 'ssh', 'ssl', 'wildcard_fqdn',
            'dos_policy', 'dos_policy6', 'address', 'address6', 'address6_template',
            'addrgrp', 'addrgrp6', 'access_proxy', 'access_proxy6',
            'access_proxy_ssh_client_cert', 'access_proxy_virtual_host'
        ]
