"""Type stubs for BGP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .clear_soft_in import ClearSoftIn
    from .clear_soft_out import ClearSoftOut
    from .neighbors import Neighbors
    from .neighbors6 import Neighbors6
    from .neighbors_statistics import NeighborsStatistics
    from .paths import Paths
    from .paths6 import Paths6
    from .paths_statistics import PathsStatistics
    from .soft_reset_neighbor import SoftResetNeighbor

__all__ = [
    "ClearSoftIn",
    "ClearSoftOut",
    "Neighbors",
    "Neighbors6",
    "NeighborsStatistics",
    "Paths",
    "Paths6",
    "PathsStatistics",
    "SoftResetNeighbor",
    "Bgp",
]


class Bgp:
    """BGP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    clear_soft_in: ClearSoftIn
    clear_soft_out: ClearSoftOut
    neighbors: Neighbors
    neighbors6: Neighbors6
    neighbors_statistics: NeighborsStatistics
    paths: Paths
    paths6: Paths6
    paths_statistics: PathsStatistics
    soft_reset_neighbor: SoftResetNeighbor

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize bgp category with HTTP client."""
        ...
