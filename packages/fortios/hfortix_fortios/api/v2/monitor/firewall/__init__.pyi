"""Type stubs for FIREWALL category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .address6_dynamic import Address6Dynamic
    from .address_dynamic import AddressDynamic
    from .address_fqdns import AddressFqdns
    from .address_fqdns6 import AddressFqdns6
    from .check_addrgrp_exclude_mac_member import CheckAddrgrpExcludeMacMember
    from .gtp_runtime_statistics import GtpRuntimeStatistics
    from .gtp_statistics import GtpStatistics
    from .health import Health
    from .internet_service_basic import InternetServiceBasic
    from .internet_service_details import InternetServiceDetails
    from .internet_service_fqdn import InternetServiceFqdn
    from .internet_service_fqdn_icon_ids import InternetServiceFqdnIconIds
    from .internet_service_match import InternetServiceMatch
    from .internet_service_reputation import InternetServiceReputation
    from .load_balance import LoadBalance
    from .local_in import LocalIn
    from .local_in6 import LocalIn6
    from .network_service_dynamic import NetworkServiceDynamic
    from .policy_lookup import PolicyLookup
    from .saas_application import SaasApplication
    from .sdn_connector_filters import SdnConnectorFilters
    from .sessions import Sessions
    from .uuid_list import UuidList
    from .uuid_type_lookup import UuidTypeLookup
    from .vip_overlap import VipOverlap
    from .acl import Acl
    from .acl6 import Acl6
    from .central_snat_map import CentralSnatMap
    from .clearpass_address import ClearpassAddress
    from .dnat import Dnat
    from .gtp import Gtp
    from .ippool import Ippool
    from .multicast_policy import MulticastPolicy
    from .multicast_policy6 import MulticastPolicy6
    from .per_ip_shaper import PerIpShaper
    from .policy import Policy
    from .proxy import Proxy
    from .proxy_policy import ProxyPolicy
    from .security_policy import SecurityPolicy
    from .session import Session
    from .session6 import Session6
    from .shaper import Shaper
    from .ztna_firewall_policy import ZtnaFirewallPolicy

__all__ = [
    "Address6Dynamic",
    "AddressDynamic",
    "AddressFqdns",
    "AddressFqdns6",
    "CheckAddrgrpExcludeMacMember",
    "GtpRuntimeStatistics",
    "GtpStatistics",
    "Health",
    "InternetServiceBasic",
    "InternetServiceDetails",
    "InternetServiceFqdn",
    "InternetServiceFqdnIconIds",
    "InternetServiceMatch",
    "InternetServiceReputation",
    "LoadBalance",
    "LocalIn",
    "LocalIn6",
    "NetworkServiceDynamic",
    "PolicyLookup",
    "SaasApplication",
    "SdnConnectorFilters",
    "Sessions",
    "UuidList",
    "UuidTypeLookup",
    "VipOverlap",
    "Firewall",
]


class Firewall:
    """FIREWALL API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    acl: Acl
    acl6: Acl6
    central_snat_map: CentralSnatMap
    clearpass_address: ClearpassAddress
    dnat: Dnat
    gtp: Gtp
    ippool: Ippool
    multicast_policy: MulticastPolicy
    multicast_policy6: MulticastPolicy6
    per_ip_shaper: PerIpShaper
    policy: Policy
    proxy: Proxy
    proxy_policy: ProxyPolicy
    security_policy: SecurityPolicy
    session: Session
    session6: Session6
    shaper: Shaper
    ztna_firewall_policy: ZtnaFirewallPolicy
    address6_dynamic: Address6Dynamic
    address_dynamic: AddressDynamic
    address_fqdns: AddressFqdns
    address_fqdns6: AddressFqdns6
    check_addrgrp_exclude_mac_member: CheckAddrgrpExcludeMacMember
    gtp_runtime_statistics: GtpRuntimeStatistics
    gtp_statistics: GtpStatistics
    health: Health
    internet_service_basic: InternetServiceBasic
    internet_service_details: InternetServiceDetails
    internet_service_fqdn: InternetServiceFqdn
    internet_service_fqdn_icon_ids: InternetServiceFqdnIconIds
    internet_service_match: InternetServiceMatch
    internet_service_reputation: InternetServiceReputation
    load_balance: LoadBalance
    local_in: LocalIn
    local_in6: LocalIn6
    network_service_dynamic: NetworkServiceDynamic
    policy_lookup: PolicyLookup
    saas_application: SaasApplication
    sdn_connector_filters: SdnConnectorFilters
    sessions: Sessions
    uuid_list: UuidList
    uuid_type_lookup: UuidTypeLookup
    vip_overlap: VipOverlap

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize firewall category with HTTP client."""
        ...
