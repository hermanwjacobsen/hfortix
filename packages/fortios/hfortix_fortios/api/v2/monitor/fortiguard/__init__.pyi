"""Type stubs for FORTIGUARD category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .answers import Answers
    from .redirect_portal import RedirectPortal
    from .service_communication_stats import ServiceCommunicationStats

__all__ = [
    "Answers",
    "RedirectPortal",
    "ServiceCommunicationStats",
    "Fortiguard",
]


class Fortiguard:
    """FORTIGUARD API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    answers: Answers
    redirect_portal: RedirectPortal
    service_communication_stats: ServiceCommunicationStats

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize fortiguard category with HTTP client."""
        ...
