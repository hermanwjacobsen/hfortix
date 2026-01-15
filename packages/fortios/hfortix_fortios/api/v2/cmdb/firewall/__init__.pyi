"""Type stubs for FIREWALL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .DoS_policy import DosPolicy
    from .DoS_policy6 import DosPolicy6
    from .access_proxy import AccessProxy
    from .access_proxy6 import AccessProxy6
    from .access_proxy_ssh_client_cert import AccessProxySshClientCert
    from .access_proxy_virtual_host import AccessProxyVirtualHost
    from .address import Address
    from .address6 import Address6
    from .address6_template import Address6Template
    from .addrgrp import Addrgrp
    from .addrgrp6 import Addrgrp6
    from .auth_portal import AuthPortal
    from .central_snat_map import CentralSnatMap
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
    from .ipmacbinding import Ipmacbinding
    from .schedule import Schedule
    from .service import Service
    from .shaper import Shaper
    from .ssh import Ssh
    from .ssl import Ssl
    from .wildcard_fqdn import WildcardFqdn

__all__ = [
    "DosPolicy",
    "DosPolicy6",
    "AccessProxy",
    "AccessProxy6",
    "AccessProxySshClientCert",
    "AccessProxyVirtualHost",
    "Address",
    "Address6",
    "Address6Template",
    "Addrgrp",
    "Addrgrp6",
    "AuthPortal",
    "CentralSnatMap",
    "City",
    "Country",
    "DecryptedTrafficMirror",
    "Dnstranslation",
    "Global",
    "IdentityBasedRoute",
    "InterfacePolicy",
    "InterfacePolicy6",
    "InternetService",
    "InternetServiceAddition",
    "InternetServiceAppend",
    "InternetServiceBotnet",
    "InternetServiceCustom",
    "InternetServiceCustomGroup",
    "InternetServiceDefinition",
    "InternetServiceExtension",
    "InternetServiceFortiguard",
    "InternetServiceGroup",
    "InternetServiceIpblReason",
    "InternetServiceIpblVendor",
    "InternetServiceList",
    "InternetServiceName",
    "InternetServiceOwner",
    "InternetServiceReputation",
    "InternetServiceSld",
    "InternetServiceSubapp",
    "IpTranslation",
    "Ippool",
    "Ippool6",
    "LdbMonitor",
    "LocalInPolicy",
    "LocalInPolicy6",
    "MulticastAddress",
    "MulticastAddress6",
    "MulticastPolicy",
    "MulticastPolicy6",
    "NetworkServiceDynamic",
    "OnDemandSniffer",
    "Policy",
    "ProfileGroup",
    "ProfileProtocolOptions",
    "ProxyAddress",
    "ProxyAddrgrp",
    "ProxyPolicy",
    "Region",
    "SecurityPolicy",
    "ShapingPolicy",
    "ShapingProfile",
    "Sniffer",
    "SslServer",
    "SslSshProfile",
    "TrafficClass",
    "TtlPolicy",
    "VendorMac",
    "VendorMacSummary",
    "Vip",
    "Vip6",
    "Vipgrp",
    "Vipgrp6",
    "Firewall",
]


class Firewall:
    """FIREWALL API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    ipmacbinding: Ipmacbinding
    schedule: Schedule
    service: Service
    shaper: Shaper
    ssh: Ssh
    ssl: Ssl
    wildcard_fqdn: WildcardFqdn
    DoS_policy: DosPolicy
    DoS_policy6: DosPolicy6
    access_proxy: AccessProxy
    access_proxy6: AccessProxy6
    access_proxy_ssh_client_cert: AccessProxySshClientCert
    access_proxy_virtual_host: AccessProxyVirtualHost
    address: Address
    address6: Address6
    address6_template: Address6Template
    addrgrp: Addrgrp
    addrgrp6: Addrgrp6
    auth_portal: AuthPortal
    central_snat_map: CentralSnatMap
    city: City
    country: Country
    decrypted_traffic_mirror: DecryptedTrafficMirror
    dnstranslation: Dnstranslation
    global_: Global
    identity_based_route: IdentityBasedRoute
    interface_policy: InterfacePolicy
    interface_policy6: InterfacePolicy6
    internet_service: InternetService
    internet_service_addition: InternetServiceAddition
    internet_service_append: InternetServiceAppend
    internet_service_botnet: InternetServiceBotnet
    internet_service_custom: InternetServiceCustom
    internet_service_custom_group: InternetServiceCustomGroup
    internet_service_definition: InternetServiceDefinition
    internet_service_extension: InternetServiceExtension
    internet_service_fortiguard: InternetServiceFortiguard
    internet_service_group: InternetServiceGroup
    internet_service_ipbl_reason: InternetServiceIpblReason
    internet_service_ipbl_vendor: InternetServiceIpblVendor
    internet_service_list: InternetServiceList
    internet_service_name: InternetServiceName
    internet_service_owner: InternetServiceOwner
    internet_service_reputation: InternetServiceReputation
    internet_service_sld: InternetServiceSld
    internet_service_subapp: InternetServiceSubapp
    ip_translation: IpTranslation
    ippool: Ippool
    ippool6: Ippool6
    ldb_monitor: LdbMonitor
    local_in_policy: LocalInPolicy
    local_in_policy6: LocalInPolicy6
    multicast_address: MulticastAddress
    multicast_address6: MulticastAddress6
    multicast_policy: MulticastPolicy
    multicast_policy6: MulticastPolicy6
    network_service_dynamic: NetworkServiceDynamic
    on_demand_sniffer: OnDemandSniffer
    policy: Policy
    profile_group: ProfileGroup
    profile_protocol_options: ProfileProtocolOptions
    proxy_address: ProxyAddress
    proxy_addrgrp: ProxyAddrgrp
    proxy_policy: ProxyPolicy
    region: Region
    security_policy: SecurityPolicy
    shaping_policy: ShapingPolicy
    shaping_profile: ShapingProfile
    sniffer: Sniffer
    ssl_server: SslServer
    ssl_ssh_profile: SslSshProfile
    traffic_class: TrafficClass
    ttl_policy: TtlPolicy
    vendor_mac: VendorMac
    vendor_mac_summary: VendorMacSummary
    vip: Vip
    vip6: Vip6
    vipgrp: Vipgrp
    vipgrp6: Vipgrp6

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize firewall category with HTTP client."""
        ...
