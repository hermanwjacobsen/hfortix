"""
FortiOS Firewall Monitor API

This module provides access to firewall monitoring endpoints including:
- Policy statistics and management
- Session monitoring and control
- Traffic shaping statistics
- Internet service lookups
- Address resolution monitoring
- Load balancing statistics
- GTP tunnel monitoring
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client_interface import IHTTPClient


class Firewall:
    """Firewall Monitor API endpoints."""

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize Firewall Monitor API.

        Args:
            client: HTTP client implementing IHTTPClient protocol for API
            communication
        """
        self._client = client

        # Import classes directly for cleaner code
        from .acl import Acl
        from .acl6 import Acl6
        from .address6_dynamic import Address6Dynamic
        from .address_dynamic import AddressDynamic
        from .address_fqdns import AddressFqdns
        from .address_fqdns6 import AddressFqdns6
        from .central_snat_map import CentralSnatMap
        from .check_addrgrp_exclude_mac_member import (
            CheckAddrgrpExcludeMacMember,
        )
        from .clearpass_address import ClearpassAddress
        from .dnat import Dnat
        from .gtp import Gtp
        from .gtp_runtime_statistics import GtpRuntimeStatistics
        from .gtp_statistics import GtpStatistics
        from .health import Health
        from .internet_service import InternetService
        from .internet_service_basic import InternetServiceBasic
        from .internet_service_fqdn import InternetServiceFqdn
        from .internet_service_fqdn_icon_ids import InternetServiceFqdnIconIds
        from .ippool import Ippool
        from .load_balance import LoadBalance
        from .local_in import LocalIn
        from .local_in6 import LocalIn6
        from .multicast_policy import MulticastPolicy
        from .multicast_policy6 import MulticastPolicy6
        from .network_service_dynamic import NetworkServiceDynamic
        from .per_ip_shaper import PerIpShaper
        from .policy import Policy
        from .policy_lookup import PolicyLookup
        from .proxy import Proxy
        from .proxy_policy import ProxyPolicy
        from .saas_application import SaasApplication
        from .sdn_connector_filters import SdnConnectorFilters
        from .security_policy import SecurityPolicy
        from .sessions import Sessions
        from .shaper import Shaper
        from .shaper_multi_class_shaper import ShaperMultiClassShaper
        from .uuid import UUID
        from .vip_overlap import VipOverlap
        from .ztna_firewall_policy import ZtnaFirewallPolicy

        # Initialize all sub-endpoints
        self._health = Health(client)
        self._local_in = LocalIn(client)
        self._local_in6 = LocalIn6(client)
        self._acl = Acl(client)
        self._acl6 = Acl6(client)
        self._central_snat_map = CentralSnatMap(client)
        self._dnat = Dnat(client)
        self._check_addrgrp_exclude_mac_member = CheckAddrgrpExcludeMacMember(
            client
        )
        self._internet_service = InternetService(client)
        self._internet_service_fqdn = InternetServiceFqdn(client)
        self._internet_service_fqdn_icon_ids = InternetServiceFqdnIconIds(
            client
        )
        self._internet_service_basic = InternetServiceBasic(client)
        self._network_service_dynamic = NetworkServiceDynamic(client)
        self._proxy = Proxy(client)
        self._policy = Policy(client)
        self._security_policy = SecurityPolicy(client)
        self._proxy_policy = ProxyPolicy(client)
        self._multicast_policy = MulticastPolicy(client)
        self._multicast_policy6 = MulticastPolicy6(client)
        self._saas_application = SaasApplication(client)
        self._policy_lookup = PolicyLookup(client)
        self._sessions = Sessions(client)
        self._shaper = Shaper(client)
        self._shaper_multi_class_shaper = ShaperMultiClassShaper(client)
        self._per_ip_shaper = PerIpShaper(client)
        self._load_balance = LoadBalance(client)
        self._vip_overlap = VipOverlap(client)
        self._address_fqdns = AddressFqdns(client)
        self._address_fqdns6 = AddressFqdns6(client)
        self._clearpass_address = ClearpassAddress(client)
        self._ippool = Ippool(client)
        self._uuid = UUID(client)
        self._gtp = Gtp(client)
        self._gtp_statistics = GtpStatistics(client)
        self._gtp_runtime_statistics = GtpRuntimeStatistics(client)
        self._address_dynamic = AddressDynamic(client)
        self._address6_dynamic = Address6Dynamic(client)
        self._sdn_connector_filters = SdnConnectorFilters(client)
        self._ztna_firewall_policy = ZtnaFirewallPolicy(client)

    @property
    def health(self):
        """Load balance server health monitors."""
        return self._health

    @property
    def local_in(self):
        """Implicit and explicit local-in firewall policies."""
        return self._local_in

    @property
    def local_in6(self):
        """Implicit and explicit IPv6 local-in firewall policies."""
        return self._local_in6

    @property
    def acl(self):
        """IPv4 ACL counters and operations."""
        return self._acl

    @property
    def acl6(self):
        """IPv6 ACL counters and operations."""
        return self._acl6

    @property
    def central_snat_map(self):
        """Central SNAT policy statistics."""
        return self._central_snat_map

    @property
    def dnat(self):
        """Virtual IP/server statistics."""
        return self._dnat

    @property
    def check_addrgrp_exclude_mac_member_endpoint(self):
        """Check if address group should exclude MAC address members."""
        return self._check_addrgrp_exclude_mac_member

    def __getattr__(self, name: str):
        # Backwards compatible alias: keep the public attribute name that
        # callers expect, while avoiding a flake8 name collision with the
        # package-level imported module.
        if name == "check_addrgrp_exclude_mac_member":
            return self.check_addrgrp_exclude_mac_member_endpoint
        raise AttributeError(name)

    @property
    def internet_service(self):
        """Internet service matching and lookup operations."""
        return self._internet_service

    @property
    def internet_service_fqdn(self):
        """Internet service FQDN mappings."""
        return self._internet_service_fqdn

    @property
    def internet_service_fqdn_icon_ids(self):
        """Internet service FQDN icon ID mappings."""
        return self._internet_service_fqdn_icon_ids

    @property
    def internet_service_basic(self):
        """Internet services with basic information."""
        return self._internet_service_basic

    @property
    def network_service_dynamic(self):
        """Dynamic network service IP address and port pairs."""
        return self._network_service_dynamic

    @property
    def proxy(self):
        """Proxy session monitoring."""
        return self._proxy

    @property
    def policy(self):
        """Firewall policy statistics and operations."""
        return self._policy

    @property
    def security_policy(self):
        """Security policy IPS engine statistics."""
        return self._security_policy

    @property
    def proxy_policy(self):
        """Explicit proxy policy statistics."""
        return self._proxy_policy

    @property
    def multicast_policy(self):
        """IPv4 multicast policy statistics."""
        return self._multicast_policy

    @property
    def multicast_policy6(self):
        """IPv6 multicast policy statistics."""
        return self._multicast_policy6

    @property
    def saas_application(self):
        """SaaS application list."""
        return self._saas_application

    @property
    def policy_lookup(self):
        """Policy lookup by creating dummy packet."""
        return self._policy_lookup

    @property
    def sessions(self):
        """Active firewall session monitoring and control."""
        return self._sessions

    @property
    def shaper(self):
        """Traffic shaper statistics."""
        return self._shaper

    @property
    def shaper_multi_class_shaper(self):
        """Multi-class shaper statistics."""
        return self._shaper_multi_class_shaper

    @property
    def per_ip_shaper(self):
        """Per-IP traffic shaper statistics."""
        return self._per_ip_shaper

    @property
    def load_balance(self):
        """Load balance server statistics."""
        return self._load_balance

    @property
    def vip_overlap(self):
        """Overlapping Virtual IP detection."""
        return self._vip_overlap

    @property
    def address_fqdns(self):
        """FQDN address objects and resolved IPs."""
        return self._address_fqdns

    @property
    def address_fqdns6(self):
        """IPv6 FQDN address objects and resolved IPs."""
        return self._address_fqdns6

    @property
    def clearpass_address(self):
        """ClearPass address management."""
        return self._clearpass_address

    @property
    def ippool(self):
        """IPv4 pool statistics and mappings."""
        return self._ippool

    @property
    def uuid(self):
        """UUID list and type lookup operations."""
        return self._uuid

    @property
    def gtp(self):
        """GTP tunnel monitoring."""
        return self._gtp

    @property
    def gtp_statistics(self):
        """GTP statistics."""
        return self._gtp_statistics

    @property
    def gtp_runtime_statistics(self):
        """GTP runtime statistics."""
        return self._gtp_runtime_statistics

    @property
    def address_dynamic(self):
        """Fabric Connector address objects and resolved IPs."""
        return self._address_dynamic

    @property
    def address6_dynamic(self):
        """IPv6 Fabric Connector address objects and resolved IPs."""
        return self._address6_dynamic

    @property
    def sdn_connector_filters(self):
        """SDN Fabric Connector available filters."""
        return self._sdn_connector_filters

    @property
    def ztna_firewall_policy(self):
        """ZTNA firewall policy statistics."""
        return self._ztna_firewall_policy

    def __dir__(self):
        """Return list of available attributes."""
        return [
            "health",
            "local_in",
            "local_in6",
            "acl",
            "acl6",
            "central_snat_map",
            "dnat",
            "check_addrgrp_exclude_mac_member",
            "check_addrgrp_exclude_mac_member_endpoint",
            "internet_service",
            "internet_service_fqdn",
            "internet_service_fqdn_icon_ids",
            "internet_service_basic",
            "network_service_dynamic",
            "proxy",
            "policy",
            "security_policy",
            "proxy_policy",
            "multicast_policy",
            "multicast_policy6",
            "saas_application",
            "policy_lookup",
            "sessions",
            "shaper",
            "shaper_multi_class_shaper",
            "per_ip_shaper",
            "load_balance",
            "vip_overlap",
            "address_fqdns",
            "address_fqdns6",
            "clearpass_address",
            "ippool",
            "uuid",
            "gtp",
            "gtp_statistics",
            "gtp_runtime_statistics",
            "address_dynamic",
            "address6_dynamic",
            "sdn_connector_filters",
            "ztna_firewall_policy",
        ]
