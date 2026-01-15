"""Type stubs for HOTSPOT20 category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .anqp_3gpp_cellular import Anqp3gppCellular
    from .anqp_ip_address_type import AnqpIpAddressType
    from .anqp_nai_realm import AnqpNaiRealm
    from .anqp_network_auth_type import AnqpNetworkAuthType
    from .anqp_roaming_consortium import AnqpRoamingConsortium
    from .anqp_venue_name import AnqpVenueName
    from .anqp_venue_url import AnqpVenueUrl
    from .h2qp_advice_of_charge import H2qpAdviceOfCharge
    from .h2qp_conn_capability import H2qpConnCapability
    from .h2qp_operator_name import H2qpOperatorName
    from .h2qp_osu_provider import H2qpOsuProvider
    from .h2qp_osu_provider_nai import H2qpOsuProviderNai
    from .h2qp_terms_and_conditions import H2qpTermsAndConditions
    from .h2qp_wan_metric import H2qpWanMetric
    from .hs_profile import HsProfile
    from .icon import Icon
    from .qos_map import QosMap

__all__ = [
    "Anqp3gppCellular",
    "AnqpIpAddressType",
    "AnqpNaiRealm",
    "AnqpNetworkAuthType",
    "AnqpRoamingConsortium",
    "AnqpVenueName",
    "AnqpVenueUrl",
    "H2qpAdviceOfCharge",
    "H2qpConnCapability",
    "H2qpOperatorName",
    "H2qpOsuProvider",
    "H2qpOsuProviderNai",
    "H2qpTermsAndConditions",
    "H2qpWanMetric",
    "HsProfile",
    "Icon",
    "QosMap",
    "Hotspot20",
]


class Hotspot20:
    """HOTSPOT20 API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    anqp_3gpp_cellular: Anqp3gppCellular
    anqp_ip_address_type: AnqpIpAddressType
    anqp_nai_realm: AnqpNaiRealm
    anqp_network_auth_type: AnqpNetworkAuthType
    anqp_roaming_consortium: AnqpRoamingConsortium
    anqp_venue_name: AnqpVenueName
    anqp_venue_url: AnqpVenueUrl
    h2qp_advice_of_charge: H2qpAdviceOfCharge
    h2qp_conn_capability: H2qpConnCapability
    h2qp_operator_name: H2qpOperatorName
    h2qp_osu_provider: H2qpOsuProvider
    h2qp_osu_provider_nai: H2qpOsuProviderNai
    h2qp_terms_and_conditions: H2qpTermsAndConditions
    h2qp_wan_metric: H2qpWanMetric
    hs_profile: HsProfile
    icon: Icon
    qos_map: QosMap

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize hotspot20 category with HTTP client."""
        ...
