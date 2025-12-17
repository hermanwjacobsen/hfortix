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

from typing import TYPE_CHECKING, Any, Dict, Optional

if TYPE_CHECKING:
    from hfortix.FortiOS.http_client import HTTPClient


class Firewall:
    """Firewall Monitor API endpoints."""

    def __init__(self, client: "HTTPClient"):
        """
        Initialize Firewall Monitor API.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

        # Simple .list() endpoints
        # ZTNA policy
        # Proxy sessions sub-endpoint
        # Special operations endpoints
        # .list() and .get() endpoints
        from . import (acl, acl6, address6_dynamic, address_dynamic,
                       address_fqdns, address_fqdns6, central_snat_map,
                       check_addrgrp_exclude_mac_member, clearpass_address,
                       dnat, gtp, gtp_runtime_statistics, gtp_statistics,
                       health, internet_service, internet_service_basic,
                       internet_service_fqdn, internet_service_fqdn_icon_ids,
                       ippool, load_balance, local_in, local_in6,
                       multicast_policy, multicast_policy6,
                       network_service_dynamic, per_ip_shaper, policy,
                       policy_lookup, proxy, proxy_policy, saas_application,
                       sdn_connector_filters, security_policy)
        from . import sessions as sessions_module
        from . import shaper, shaper_multi_class_shaper
        from . import uuid as uuid_module
        from . import vip_overlap, ztna_firewall_policy

        # Initialize all sub-endpoints
        self._health = health.Health(client)
        self._local_in = local_in.LocalIn(client)
        self._local_in6 = local_in6.LocalIn6(client)
        self._acl = acl.ACL(client)
        self._acl6 = acl6.ACL6(client)
        self._central_snat_map = central_snat_map.CentralSnatMap(client)
        self._dnat = dnat.DNAT(client)
        self._check_addrgrp_exclude_mac_member = (
            check_addrgrp_exclude_mac_member.CheckAddrgrpExcludeMacMember(client)
        )
        self._internet_service = internet_service.InternetService(client)
        self._internet_service_fqdn = internet_service_fqdn.InternetServiceFqdn(client)
        self._internet_service_fqdn_icon_ids = (
            internet_service_fqdn_icon_ids.InternetServiceFqdnIconIds(client)
        )
        self._internet_service_basic = internet_service_basic.InternetServiceBasic(client)
        self._network_service_dynamic = network_service_dynamic.NetworkServiceDynamic(client)
        self._proxy = proxy.Proxy(client)
        self._policy = policy.Policy(client)
        self._security_policy = security_policy.SecurityPolicy(client)
        self._proxy_policy = proxy_policy.ProxyPolicy(client)
        self._multicast_policy = multicast_policy.MulticastPolicy(client)
        self._multicast_policy6 = multicast_policy6.MulticastPolicy6(client)
        self._saas_application = saas_application.SaasApplication(client)
        self._policy_lookup = policy_lookup.PolicyLookup(client)
        self._sessions = sessions_module.Sessions(client)
        self._shaper = shaper.Shaper(client)
        self._shaper_multi_class_shaper = shaper_multi_class_shaper.ShaperMultiClassShaper(client)
        self._per_ip_shaper = per_ip_shaper.PerIpShaper(client)
        self._load_balance = load_balance.LoadBalance(client)
        self._vip_overlap = vip_overlap.VipOverlap(client)
        self._address_fqdns = address_fqdns.AddressFqdns(client)
        self._address_fqdns6 = address_fqdns6.AddressFqdns6(client)
        self._clearpass_address = clearpass_address.ClearpassAddress(client)
        self._ippool = ippool.IPPool(client)
        self._uuid = uuid_module.UUID(client)
        self._gtp = gtp.GTP(client)
        self._gtp_statistics = gtp_statistics.GTPStatistics(client)
        self._gtp_runtime_statistics = gtp_runtime_statistics.GTPRuntimeStatistics(client)
        self._address_dynamic = address_dynamic.AddressDynamic(client)
        self._address6_dynamic = address6_dynamic.Address6Dynamic(client)
        self._sdn_connector_filters = sdn_connector_filters.SdnConnectorFilters(client)
        self._ztna_firewall_policy = ztna_firewall_policy.ZTNAFirewallPolicy(client)

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
    def check_addrgrp_exclude_mac_member(self):
        """Check if address group should exclude MAC address members."""
        return self._check_addrgrp_exclude_mac_member

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
