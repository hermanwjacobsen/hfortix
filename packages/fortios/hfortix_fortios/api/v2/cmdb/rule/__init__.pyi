"""Type stubs for RULE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .fmwp import Fmwp
    from .iotd import Iotd
    from .otdt import Otdt
    from .otvp import Otvp

__all__ = [
    "Fmwp",
    "Iotd",
    "Otdt",
    "Otvp",
    "Rule",
]


class Rule:
    """RULE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    fmwp: Fmwp
    iotd: Iotd
    otdt: Otdt
    otvp: Otvp

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize rule category with HTTP client."""
        ...
