"""Type stubs for IPSEC category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .concentrator import Concentrator
    from .fec import Fec
    from .manualkey import Manualkey
    from .manualkey_interface import ManualkeyInterface
    from .phase1 import Phase1
    from .phase1_interface import Phase1Interface
    from .phase2 import Phase2
    from .phase2_interface import Phase2Interface

__all__ = [
    "Concentrator",
    "Fec",
    "Manualkey",
    "ManualkeyInterface",
    "Phase1",
    "Phase1Interface",
    "Phase2",
    "Phase2Interface",
    "Ipsec",
]


class Ipsec:
    """IPSEC API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    concentrator: Concentrator
    fec: Fec
    manualkey: Manualkey
    manualkey_interface: ManualkeyInterface
    phase1: Phase1
    phase1_interface: Phase1Interface
    phase2: Phase2
    phase2_interface: Phase2Interface

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ipsec category with HTTP client."""
        ...
