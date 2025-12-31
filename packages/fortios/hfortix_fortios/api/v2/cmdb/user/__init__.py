"""FortiOS CMDB - User category"""

from .adgrp import Adgrp
from .certificate import Certificate
from .domain_controller import DomainController
from .exchange import Exchange
from .external_identity_provider import ExternalIdentityProvider
from .fortitoken import Fortitoken
from .fsso import Fsso
from .fsso_polling import FssoPolling
from .group import Group
from .krb_keytab import KrbKeytab
from .ldap import Ldap
from .local import Local
from .nac_policy import NacPolicy
from .password_policy import PasswordPolicy
from .peer import Peer
from .peergrp import Peergrp
from .pop3 import Pop3
from .quarantine import Quarantine
from .radius import Radius
from .saml import Saml
from .scim import Scim
from .security_exempt_list import SecurityExemptList
from .setting import Setting
from .tacacs_plus_ import TacacsPlus

__all__ = [
    "Adgrp",
    "Certificate",
    "DomainController",
    "Exchange",
    "ExternalIdentityProvider",
    "Fortitoken",
    "Fsso",
    "FssoPolling",
    "Group",
    "KrbKeytab",
    "Ldap",
    "Local",
    "NacPolicy",
    "PasswordPolicy",
    "Peer",
    "Peergrp",
    "Pop3",
    "Quarantine",
    "Radius",
    "Saml",
    "Scim",
    "SecurityExemptList",
    "Setting",
    "TacacsPlus",
]


class User:
    """
    User category wrapper.

    This class provides access to all user CMDB endpoints.
    """

    def __init__(self, client):
        """
        Initialize User with all endpoint classes.

        Args:
            client: HTTPClient instance
        """
        self.adgrp = Adgrp(client)
        self.certificate = Certificate(client)
        self.domain_controller = DomainController(client)
        self.exchange = Exchange(client)
        self.external_identity_provider = ExternalIdentityProvider(client)
        self.fortitoken = Fortitoken(client)
        self.fsso = Fsso(client)
        self.fsso_polling = FssoPolling(client)
        self.group = Group(client)
        self.krb_keytab = KrbKeytab(client)
        self.ldap = Ldap(client)
        self.local = Local(client)
        self.nac_policy = NacPolicy(client)
        self.password_policy = PasswordPolicy(client)
        self.peer = Peer(client)
        self.peergrp = Peergrp(client)
        self.pop3 = Pop3(client)
        self.quarantine = Quarantine(client)
        self.radius = Radius(client)
        self.saml = Saml(client)
        self.scim = Scim(client)
        self.security_exempt_list = SecurityExemptList(client)
        self.setting = Setting(client)
        self.tacacs_plus_ = TacacsPlus(client)
