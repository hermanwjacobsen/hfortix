"""Type stubs for USER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
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
    from .tacacs_plus import TacacsPlus

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
    "User",
]


class User:
    """USER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    adgrp: Adgrp
    certificate: Certificate
    domain_controller: DomainController
    exchange: Exchange
    external_identity_provider: ExternalIdentityProvider
    fortitoken: Fortitoken
    fsso: Fsso
    fsso_polling: FssoPolling
    group: Group
    krb_keytab: KrbKeytab
    ldap: Ldap
    local: Local
    nac_policy: NacPolicy
    password_policy: PasswordPolicy
    peer: Peer
    peergrp: Peergrp
    pop3: Pop3
    quarantine: Quarantine
    radius: Radius
    saml: Saml
    scim: Scim
    security_exempt_list: SecurityExemptList
    setting: Setting
    tacacs_plus: TacacsPlus

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize user category with HTTP client."""
        ...
