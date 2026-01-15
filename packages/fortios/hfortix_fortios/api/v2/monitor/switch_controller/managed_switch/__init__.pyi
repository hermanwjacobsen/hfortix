"""Type stubs for MANAGED_SWITCH category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .bios import Bios
    from .bounce_port import BouncePort
    from .cable_status import CableStatus
    from .dhcp_snooping import DhcpSnooping
    from .faceplate_xml import FaceplateXml
    from .factory_reset import FactoryReset
    from .health_status import HealthStatus
    from .models import Models
    from .poe_reset import PoeReset
    from .port_health import PortHealth
    from .port_stats import PortStats
    from .port_stats_reset import PortStatsReset
    from .restart import Restart
    from .status import Status
    from .transceivers import Transceivers
    from .tx_rx import TxRx
    from .update import Update

__all__ = [
    "Bios",
    "BouncePort",
    "CableStatus",
    "DhcpSnooping",
    "FaceplateXml",
    "FactoryReset",
    "HealthStatus",
    "Models",
    "PoeReset",
    "PortHealth",
    "PortStats",
    "PortStatsReset",
    "Restart",
    "Status",
    "Transceivers",
    "TxRx",
    "Update",
    "ManagedSwitch",
]


class ManagedSwitch:
    """MANAGED_SWITCH API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    bios: Bios
    bounce_port: BouncePort
    cable_status: CableStatus
    dhcp_snooping: DhcpSnooping
    faceplate_xml: FaceplateXml
    factory_reset: FactoryReset
    health_status: HealthStatus
    models: Models
    poe_reset: PoeReset
    port_health: PortHealth
    port_stats: PortStats
    port_stats_reset: PortStatsReset
    restart: Restart
    status: Status
    transceivers: Transceivers
    tx_rx: TxRx
    update: Update

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize managed_switch category with HTTP client."""
        ...
