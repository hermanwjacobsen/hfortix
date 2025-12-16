"""
FortiOS Firewall API
Firewall configuration endpoints
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient
    from .auth_portal import AuthPortal
    from .central_snat_map import CentralSnatMap
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
    from .city import City
    from .country import Country
    from .decrypted_traffic_mirror import DecryptedTrafficMirror
    from .dnstranslation import Dnstranslation
    from .global_ import Global
    from .identity_based_route import IdentityBasedRoute
    from .interface_policy import InterfacePolicy
    from .interface_policy6 import InterfacePolicy6
    from .internet_service import InternetService
    from .internet_service_addition import InternetServiceAddition
    from .internet_service_append import InternetServiceAppend
    from .internet_service_botnet import InternetServiceBotnet
    from .internet_service_custom import InternetServiceCustom
    from .internet_service_custom_group import InternetServiceCustomGroup
    from .internet_service_definition import InternetServiceDefinition
    from .internet_service_extension import InternetServiceExtension
    from .internet_service_fortiguard import InternetServiceFortiguard
    from .internet_service_group import InternetServiceGroup
    from .internet_service_ipbl_reason import InternetServiceIpblReason
    from .internet_service_ipbl_vendor import InternetServiceIpblVendor
    from .internet_service_list import InternetServiceList
    from .internet_service_name import InternetServiceName
    from .internet_service_owner import InternetServiceOwner
    from .internet_service_reputation import InternetServiceReputation
    from .internet_service_sld import InternetServiceSld
    from .internet_service_subapp import InternetServiceSubapp
    from .ip_translation import IpTranslation
    from .ippool import Ippool
    from .ippool6 import Ippool6
    from .ldb_monitor import LdbMonitor
    from .local_in_policy import LocalInPolicy
    from .local_in_policy6 import LocalInPolicy6
    from .multicast_address import MulticastAddress
    from .multicast_address6 import MulticastAddress6
    from .multicast_policy import MulticastPolicy
    from .multicast_policy6 import MulticastPolicy6
    from .network_service_dynamic import NetworkServiceDynamic
    from .on_demand_sniffer import OnDemandSniffer
    from .policy import Policy
    from .profile_group import ProfileGroup
    from .profile_protocol_options import ProfileProtocolOptions
    from .proxy_address import ProxyAddress
    from .proxy_addrgrp import ProxyAddrgrp
    from .proxy_policy import ProxyPolicy
    from .region import Region
    from .security_policy import SecurityPolicy
    from .shaping_policy import ShapingPolicy
    from .shaping_profile import ShapingProfile
    from .sniffer import Sniffer
    from .ssl_server import SslServer
    from .ssl_ssh_profile import SslSshProfile
    from .traffic_class import TrafficClass
    from .ttl_policy import TtlPolicy
    from .vendor_mac import VendorMac
    from .vendor_mac_summary import VendorMacSummary
    from .vip import Vip
    from .vip6 import Vip6
    from .vipgrp import Vipgrp
    from .vipgrp6 import Vipgrp6

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

    @property
    def auth_portal(self) -> 'AuthPortal':
        """Access firewall authentication portal endpoint"""
        if not hasattr(self, '__auth_portal'):
            from .auth_portal import AuthPortal
            self.__auth_portal = AuthPortal(self._client)
        return self.__auth_portal

    @property
    def central_snat_map(self) -> 'CentralSnatMap':
        """Access central SNAT map endpoint"""
        if not hasattr(self, '__central_snat_map'):
            from .central_snat_map import CentralSnatMap
            self.__central_snat_map = CentralSnatMap(self._client)
        return self.__central_snat_map

    @property
    def city(self) -> 'City':
        """Access firewall city table endpoint"""
        if not hasattr(self, '__city'):
            from .city import City
            self.__city = City(self._client)
        return self.__city

    @property
    def country(self) -> 'Country':
        """Access firewall country table endpoint"""
        if not hasattr(self, '__country'):
            from .country import Country
            self.__country = Country(self._client)
        return self.__country

    @property
    def decrypted_traffic_mirror(self) -> 'DecryptedTrafficMirror':
        """Access decrypted traffic mirror endpoint"""
        if not hasattr(self, '__decrypted_traffic_mirror'):
            from .decrypted_traffic_mirror import DecryptedTrafficMirror
            self.__decrypted_traffic_mirror = DecryptedTrafficMirror(self._client)
        return self.__decrypted_traffic_mirror

    @property
    def dnstranslation(self) -> 'Dnstranslation':
        """Access firewall dnstranslation table endpoint"""
        if not hasattr(self, '__dnstranslation'):
            from .dnstranslation import Dnstranslation
            self.__dnstranslation = Dnstranslation(self._client)
        return self.__dnstranslation

    @property
    def global_(self) -> 'Global':
        """Access firewall global singleton endpoint"""
        if not hasattr(self, '__global_'):
            from .global_ import Global
            self.__global_ = Global(self._client)
        return self.__global_

    @property
    def identity_based_route(self) -> 'IdentityBasedRoute':
        """Access firewall identity-based-route table endpoint"""
        if not hasattr(self, '__identity_based_route'):
            from .identity_based_route import IdentityBasedRoute
            self.__identity_based_route = IdentityBasedRoute(self._client)
        return self.__identity_based_route

    @property
    def interface_policy(self) -> 'InterfacePolicy':
        """Access firewall interface-policy table endpoint"""
        if not hasattr(self, '__interface_policy'):
            from .interface_policy import InterfacePolicy
            self.__interface_policy = InterfacePolicy(self._client)
        return self.__interface_policy

    @property
    def interface_policy6(self) -> 'InterfacePolicy6':
        """Access firewall interface-policy6 table endpoint"""
        if not hasattr(self, '__interface_policy6'):
            from .interface_policy6 import InterfacePolicy6
            self.__interface_policy6 = InterfacePolicy6(self._client)
        return self.__interface_policy6

    @property
    def internet_service(self) -> 'InternetService':
        """Access firewall internet-service table endpoint (read-only)"""
        if not hasattr(self, '__internet_service'):
            from .internet_service import InternetService
            self.__internet_service = InternetService(self._client)
        return self.__internet_service

    @property
    def internet_service_addition(self) -> 'InternetServiceAddition':
        """Access firewall internet-service-addition table endpoint"""
        if not hasattr(self, '__internet_service_addition'):
            from .internet_service_addition import InternetServiceAddition
            self.__internet_service_addition = InternetServiceAddition(self._client)
        return self.__internet_service_addition

    @property
    def internet_service_append(self) -> 'InternetServiceAppend':
        """Access firewall internet-service-append singleton endpoint"""
        if not hasattr(self, '__internet_service_append'):
            from .internet_service_append import InternetServiceAppend
            self.__internet_service_append = InternetServiceAppend(self._client)
        return self.__internet_service_append

    @property
    def internet_service_botnet(self) -> 'InternetServiceBotnet':
        """Access firewall internet-service-botnet table endpoint (read-only)"""
        if not hasattr(self, '__internet_service_botnet'):
            from .internet_service_botnet import InternetServiceBotnet
            self.__internet_service_botnet = InternetServiceBotnet(self._client)
        return self.__internet_service_botnet

    @property
    def internet_service_custom(self) -> 'InternetServiceCustom':
        """Access firewall internet-service-custom table endpoint"""
        if not hasattr(self, '__internet_service_custom'):
            from .internet_service_custom import InternetServiceCustom
            self.__internet_service_custom = InternetServiceCustom(self._client)
        return self.__internet_service_custom

    @property
    def internet_service_custom_group(self) -> 'InternetServiceCustomGroup':
        """Access firewall internet-service-custom-group table endpoint"""
        if not hasattr(self, '__internet_service_custom_group'):
            from .internet_service_custom_group import InternetServiceCustomGroup
            self.__internet_service_custom_group = InternetServiceCustomGroup(self._client)
        return self.__internet_service_custom_group

    @property
    def internet_service_definition(self) -> 'InternetServiceDefinition':
        """Access firewall internet-service-definition table endpoint"""
        if not hasattr(self, '__internet_service_definition'):
            from .internet_service_definition import InternetServiceDefinition
            self.__internet_service_definition = InternetServiceDefinition(self._client)
        return self.__internet_service_definition

    @property
    def internet_service_extension(self) -> 'InternetServiceExtension':
        """Access firewall internet-service-extension table endpoint"""
        if not hasattr(self, '__internet_service_extension'):
            from .internet_service_extension import InternetServiceExtension
            self.__internet_service_extension = InternetServiceExtension(self._client)
        return self.__internet_service_extension

    @property
    def internet_service_fortiguard(self) -> 'InternetServiceFortiguard':
        """Access firewall internet-service-fortiguard table endpoint (read-only)"""
        if not hasattr(self, '__internet_service_fortiguard'):
            from .internet_service_fortiguard import InternetServiceFortiguard
            self.__internet_service_fortiguard = InternetServiceFortiguard(self._client)
        return self.__internet_service_fortiguard

    @property
    def internet_service_group(self) -> 'InternetServiceGroup':
        """Access firewall internet-service-group table endpoint"""
        if not hasattr(self, '__internet_service_group'):
            from .internet_service_group import InternetServiceGroup
            self.__internet_service_group = InternetServiceGroup(self._client)
        return self.__internet_service_group

    @property
    def internet_service_ipbl_reason(self) -> 'InternetServiceIpblReason':
        """Access firewall internet-service-ipbl-reason table endpoint (read-only)"""
        if not hasattr(self, '__internet_service_ipbl_reason'):
            from .internet_service_ipbl_reason import InternetServiceIpblReason
            self.__internet_service_ipbl_reason = InternetServiceIpblReason(self._client)
        return self.__internet_service_ipbl_reason

    @property
    def internet_service_ipbl_vendor(self) -> 'InternetServiceIpblVendor':
        """Access firewall internet-service-ipbl-vendor table endpoint (read-only)"""
        if not hasattr(self, '__internet_service_ipbl_vendor'):
            from .internet_service_ipbl_vendor import InternetServiceIpblVendor
            self.__internet_service_ipbl_vendor = InternetServiceIpblVendor(self._client)
        return self.__internet_service_ipbl_vendor

    @property
    def internet_service_list(self) -> 'InternetServiceList':
        """Access firewall internet-service-list table endpoint"""
        if not hasattr(self, '__internet_service_list'):
            from .internet_service_list import InternetServiceList
            self.__internet_service_list = InternetServiceList(self._client)
        return self.__internet_service_list

    @property
    def internet_service_name(self) -> 'InternetServiceName':
        """Access firewall internet-service-name table endpoint"""
        if not hasattr(self, '__internet_service_name'):
            from .internet_service_name import InternetServiceName
            self.__internet_service_name = InternetServiceName(self._client)
        return self.__internet_service_name

    @property
    def internet_service_owner(self) -> 'InternetServiceOwner':
        """Access firewall internet-service-owner table endpoint (read-only)"""
        if not hasattr(self, '__internet_service_owner'):
            from .internet_service_owner import InternetServiceOwner
            self.__internet_service_owner = InternetServiceOwner(self._client)
        return self.__internet_service_owner

    @property
    def internet_service_reputation(self) -> 'InternetServiceReputation':
        """Access firewall internet-service-reputation table endpoint (read-only)"""
        if not hasattr(self, '__internet_service_reputation'):
            from .internet_service_reputation import InternetServiceReputation
            self.__internet_service_reputation = InternetServiceReputation(self._client)
        return self.__internet_service_reputation

    @property
    def internet_service_sld(self) -> 'InternetServiceSld':
        """Access firewall internet-service-sld table endpoint (read-only)"""
        if not hasattr(self, '__internet_service_sld'):
            from .internet_service_sld import InternetServiceSld
            self.__internet_service_sld = InternetServiceSld(self._client)
        return self.__internet_service_sld

    @property
    def internet_service_subapp(self) -> 'InternetServiceSubapp':
        """Access firewall internet-service-subapp table endpoint (read-only)"""
        if not hasattr(self, '__internet_service_subapp'):
            from .internet_service_subapp import InternetServiceSubapp
            self.__internet_service_subapp = InternetServiceSubapp(self._client)
        return self.__internet_service_subapp

    @property
    def ip_translation(self) -> 'IPTranslation':
        """Access firewall IP translation endpoint"""
        if not hasattr(self, '__ip_translation'):
            from .ip_translation import IpTranslation
            self.__ip_translation = IpTranslation(self._client)
        return self.__ip_translation

    @property
    def ippool(self) -> 'IPPool':
        """Access firewall IPv4 IP pool endpoint"""
        if not hasattr(self, '__ippool'):
            from .ippool import Ippool
            self.__ippool = Ippool(self._client)
        return self.__ippool

    @property
    def ippool6(self) -> 'IPPool6':
        """Access firewall IPv6 IP pool endpoint"""
        if not hasattr(self, '__ippool6'):
            from .ippool6 import Ippool6
            self.__ippool6 = Ippool6(self._client)
        return self.__ippool6

    @property
    def ldb_monitor(self) -> 'LDBMonitor':
        """Access firewall load balancing health monitor endpoint"""
        if not hasattr(self, '__ldb_monitor'):
            from .ldb_monitor import LdbMonitor
            self.__ldb_monitor = LdbMonitor(self._client)
        return self.__ldb_monitor

    @property
    def local_in_policy(self) -> 'LocalInPolicy':
        """Access firewall IPv4 local-in policy endpoint"""
        if not hasattr(self, '__local_in_policy'):
            from .local_in_policy import LocalInPolicy
            self.__local_in_policy = LocalInPolicy(self._client)
        return self.__local_in_policy

    @property
    def local_in_policy6(self) -> 'LocalInPolicy6':
        """Access firewall IPv6 local-in policy endpoint"""
        if not hasattr(self, '__local_in_policy6'):
            from .local_in_policy6 import LocalInPolicy6
            self.__local_in_policy6 = LocalInPolicy6(self._client)
        return self.__local_in_policy6

    @property
    def multicast_address(self) -> 'MulticastAddress':
        """Access firewall multicast address endpoint"""
        if not hasattr(self, '__multicast_address'):
            from .multicast_address import MulticastAddress
            self.__multicast_address = MulticastAddress(self._client)
        return self.__multicast_address

    @property
    def multicast_address6(self) -> 'MulticastAddress6':
        """Access firewall IPv6 multicast address endpoint"""
        if not hasattr(self, '__multicast_address6'):
            from .multicast_address6 import MulticastAddress6
            self.__multicast_address6 = MulticastAddress6(self._client)
        return self.__multicast_address6

    @property
    def multicast_policy(self) -> 'MulticastPolicy':
        """Access firewall multicast NAT policy endpoint"""
        if not hasattr(self, '__multicast_policy'):
            from .multicast_policy import MulticastPolicy
            self.__multicast_policy = MulticastPolicy(self._client)
        return self.__multicast_policy

    @property
    def multicast_policy6(self) -> 'MulticastPolicy6':
        """Access firewall IPv6 multicast NAT policy endpoint"""
        if not hasattr(self, '__multicast_policy6'):
            from .multicast_policy6 import MulticastPolicy6
            self.__multicast_policy6 = MulticastPolicy6(self._client)
        return self.__multicast_policy6

    @property
    def network_service_dynamic(self) -> 'NetworkServiceDynamic':
        """Access firewall dynamic network service endpoint"""
        if not hasattr(self, '__network_service_dynamic'):
            from .network_service_dynamic import NetworkServiceDynamic
            self.__network_service_dynamic = NetworkServiceDynamic(self._client)
        return self.__network_service_dynamic

    @property
    def on_demand_sniffer(self) -> 'OnDemandSniffer':
        """Access firewall on-demand packet sniffer endpoint"""
        if not hasattr(self, '__on_demand_sniffer'):
            from .on_demand_sniffer import OnDemandSniffer
            self.__on_demand_sniffer = OnDemandSniffer(self._client)
        return self.__on_demand_sniffer

    @property
    def policy(self) -> 'Policy':
        """Access firewall firewall policy endpoint"""
        if not hasattr(self, '__policy'):
            from .policy import Policy
            self.__policy = Policy(self._client)
        return self.__policy

    @property
    def profile_group(self) -> 'ProfileGroup':
        """Access firewall profile group endpoint"""
        if not hasattr(self, '__profile_group'):
            from .profile_group import ProfileGroup
            self.__profile_group = ProfileGroup(self._client)
        return self.__profile_group

    @property
    def profile_protocol_options(self) -> 'ProfileProtocolOptions':
        """Access firewall protocol options profile endpoint"""
        if not hasattr(self, '__profile_protocol_options'):
            from .profile_protocol_options import ProfileProtocolOptions
            self.__profile_protocol_options = ProfileProtocolOptions(self._client)
        return self.__profile_protocol_options

    @property
    def proxy_address(self) -> 'ProxyAddress':
        """Access firewall web proxy address endpoint"""
        if not hasattr(self, '__proxy_address'):
            from .proxy_address import ProxyAddress
            self.__proxy_address = ProxyAddress(self._client)
        return self.__proxy_address

    @property
    def proxy_addrgrp(self) -> 'ProxyAddressGroup':
        """Access firewall web proxy address group endpoint"""
        if not hasattr(self, '__proxy_addrgrp'):
            from .proxy_addrgrp import ProxyAddrgrp
            self.__proxy_addrgrp = ProxyAddrgrp(self._client)
        return self.__proxy_addrgrp

    @property
    def proxy_policy(self) -> 'ProxyPolicy':
        """Access firewall proxy policy endpoint"""
        if not hasattr(self, '__proxy_policy'):
            from .proxy_policy import ProxyPolicy
            self.__proxy_policy = ProxyPolicy(self._client)
        return self.__proxy_policy

    @property
    def region(self) -> 'Region':
        """Access firewall region table endpoint"""
        if not hasattr(self, '__region'):
            from .region import Region
            self.__region = Region(self._client)
        return self.__region

    @property
    def security_policy(self) -> 'SecurityPolicy':
        """Access firewall security policy endpoint"""
        if not hasattr(self, '__security_policy'):
            from .security_policy import SecurityPolicy
            self.__security_policy = SecurityPolicy(self._client)
        return self.__security_policy

    @property
    def shaping_policy(self) -> 'ShapingPolicy':
        """Access firewall shaping policy endpoint"""
        if not hasattr(self, '__shaping_policy'):
            from .shaping_policy import ShapingPolicy
            self.__shaping_policy = ShapingPolicy(self._client)
        return self.__shaping_policy

    @property
    def shaping_profile(self) -> 'ShapingProfile':
        """Access firewall shaping profile endpoint"""
        if not hasattr(self, '__shaping_profile'):
            from .shaping_profile import ShapingProfile
            self.__shaping_profile = ShapingProfile(self._client)
        return self.__shaping_profile

    @property
    def sniffer(self) -> 'Sniffer':
        """Access firewall packet sniffer endpoint"""
        if not hasattr(self, '__sniffer'):
            from .sniffer import Sniffer
            self.__sniffer = Sniffer(self._client)
        return self.__sniffer

    @property
    def ssl_server(self) -> 'SSLServer':
        """Access firewall SSL server endpoint"""
        if not hasattr(self, '__ssl_server'):
            from .ssl_server import SslServer
            self.__ssl_server = SslServer(self._client)
        return self.__ssl_server

    @property
    def ssl_ssh_profile(self) -> 'SSLSSHProfile':
        """Access firewall SSL/SSH protocol options profile endpoint"""
        if not hasattr(self, '__ssl_ssh_profile'):
            from .ssl_ssh_profile import SslSshProfile
            self.__ssl_ssh_profile = SslSshProfile(self._client)
        return self.__ssl_ssh_profile

    @property
    def traffic_class(self) -> 'TrafficClass':
        """Access firewall traffic class endpoint"""
        if not hasattr(self, '__traffic_class'):
            from .traffic_class import TrafficClass
            self.__traffic_class = TrafficClass(self._client)
        return self.__traffic_class

    @property
    def ttl_policy(self) -> 'TTLPolicy':
        """Access firewall TTL policy endpoint"""
        if not hasattr(self, '__ttl_policy'):
            from .ttl_policy import TtlPolicy
            self.__ttl_policy = TtlPolicy(self._client)
        return self.__ttl_policy

    @property
    def vendor_mac(self) -> 'VendorMAC':
        """Access firewall vendor MAC endpoint"""
        if not hasattr(self, '__vendor_mac'):
            from .vendor_mac import VendorMac
            self.__vendor_mac = VendorMac(self._client)
        return self.__vendor_mac

    @property
    def vendor_mac_summary(self) -> 'VendorMACSummary':
        """Access firewall vendor MAC summary endpoint"""
        if not hasattr(self, '__vendor_mac_summary'):
            from .vendor_mac_summary import VendorMacSummary
            self.__vendor_mac_summary = VendorMacSummary(self._client)
        return self.__vendor_mac_summary

    @property
    def vip(self) -> 'VIP':
        """Access firewall IPv4 virtual IP endpoint"""
        if not hasattr(self, '__vip'):
            from .vip import Vip
            self.__vip = Vip(self._client)
        return self.__vip

    @property
    def vip6(self) -> 'VIP6':
        """Access firewall IPv6 virtual IP endpoint"""
        if not hasattr(self, '__vip6'):
            from .vip6 import Vip6
            self.__vip6 = Vip6(self._client)
        return self.__vip6

    @property
    def vipgrp(self) -> 'VIPGroup':
        """Access firewall IPv4 virtual IP group endpoint"""
        if not hasattr(self, '__vipgrp'):
            from .vipgrp import Vipgrp
            self.__vipgrp = Vipgrp(self._client)
        return self.__vipgrp

    @property
    def vipgrp6(self) -> 'VIPGroup6':
        """Access firewall IPv6 virtual IP group endpoint"""
        if not hasattr(self, '__vipgrp6'):
            from .vipgrp6 import Vipgrp6
            self.__vipgrp6 = Vipgrp6(self._client)
        return self.__vipgrp6
    
    def __dir__(self):
        """Control autocomplete to show only public attributes"""
        return [
            'ipmacbinding', 'schedule', 'service', 'shaper', 'ssh', 'ssl', 'wildcard_fqdn',
            'dos_policy', 'dos_policy6', 'address', 'address6', 'address6_template',
            'addrgrp', 'addrgrp6', 'access_proxy', 'access_proxy6',
            'access_proxy_ssh_client_cert', 'access_proxy_virtual_host',
            'auth_portal',
            'central_snat_map',
            'city',
            'country',
            'decrypted_traffic_mirror',
            'dnstranslation',
            'global_',
            'identity_based_route',
            'interface_policy',
            'interface_policy6',
            'internet_service',
            'internet_service_addition',
            'internet_service_append',
            'internet_service_botnet',
            'internet_service_custom',
            'internet_service_custom_group',
            'internet_service_definition',
            'internet_service_extension',
            'internet_service_fortiguard',
            'internet_service_group',
            'internet_service_ipbl_reason',
            'internet_service_ipbl_vendor',
            'internet_service_list',
            'internet_service_name',
            'internet_service_owner',
            'internet_service_reputation',
            'internet_service_sld',
            'internet_service_subapp',
            'ip_translation',
            'ippool',
            'ippool6',
            'ldb_monitor',
            'local_in_policy',
            'local_in_policy6',
            'multicast_address',
            'multicast_address6',
            'multicast_policy',
            'multicast_policy6',
            'network_service_dynamic',
            'on_demand_sniffer',
            'policy',
            'profile_group',
            'profile_protocol_options',
            'proxy_address',
            'proxy_addrgrp',
            'proxy_policy',
            'region',
            'security_policy',
            'shaping_policy',
            'shaping_profile',
            'sniffer',
            'ssl_server',
            'ssl_ssh_profile',
            'traffic_class',
            'ttl_policy',
            'vendor_mac',
            'vendor_mac_summary',
            'vip',
            'vip6',
            'vipgrp',
            'vipgrp6',
        ]
