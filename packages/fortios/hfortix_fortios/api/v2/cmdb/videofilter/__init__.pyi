"""Type stubs for VIDEOFILTER category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .keyword import Keyword
    from .profile import Profile
    from .youtube_key import YoutubeKey

__all__ = [
    "Keyword",
    "Profile",
    "YoutubeKey",
    "Videofilter",
]


class Videofilter:
    """VIDEOFILTER API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    keyword: Keyword
    profile: Profile
    youtube_key: YoutubeKey

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize videofilter category with HTTP client."""
        ...
