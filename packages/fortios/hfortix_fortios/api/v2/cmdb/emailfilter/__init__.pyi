"""Type stubs for EMAILFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .block_allow_list import BlockAllowList
    from .bword import Bword
    from .dnsbl import Dnsbl
    from .fortishield import Fortishield
    from .iptrust import Iptrust
    from .mheader import Mheader
    from .options import Options
    from .profile import Profile

__all__ = [
    "BlockAllowList",
    "Bword",
    "Dnsbl",
    "Fortishield",
    "Iptrust",
    "Mheader",
    "Options",
    "Profile",
    "Emailfilter",
]


class Emailfilter:
    """EMAILFILTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    block_allow_list: BlockAllowList
    bword: Bword
    dnsbl: Dnsbl
    fortishield: Fortishield
    iptrust: Iptrust
    mheader: Mheader
    options: Options
    profile: Profile

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize emailfilter category with HTTP client."""
        ...
