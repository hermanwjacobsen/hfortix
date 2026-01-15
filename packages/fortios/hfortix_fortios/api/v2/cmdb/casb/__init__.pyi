"""Type stubs for CASB category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .attribute_match import AttributeMatch
    from .profile import Profile
    from .saas_application import SaasApplication
    from .user_activity import UserActivity

__all__ = [
    "AttributeMatch",
    "Profile",
    "SaasApplication",
    "UserActivity",
    "Casb",
]


class Casb:
    """CASB API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    attribute_match: AttributeMatch
    profile: Profile
    saas_application: SaasApplication
    user_activity: UserActivity

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize casb category with HTTP client."""
        ...
