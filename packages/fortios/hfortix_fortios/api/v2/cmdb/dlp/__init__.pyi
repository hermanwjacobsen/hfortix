"""Type stubs for DLP category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .data_type import DataType
    from .dictionary import Dictionary
    from .exact_data_match import ExactDataMatch
    from .filepattern import Filepattern
    from .label import Label
    from .profile import Profile
    from .sensor import Sensor
    from .settings import Settings

__all__ = [
    "DataType",
    "Dictionary",
    "ExactDataMatch",
    "Filepattern",
    "Label",
    "Profile",
    "Sensor",
    "Settings",
    "Dlp",
]


class Dlp:
    """DLP API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    data_type: DataType
    dictionary: Dictionary
    exact_data_match: ExactDataMatch
    filepattern: Filepattern
    label: Label
    profile: Profile
    sensor: Sensor
    settings: Settings

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize dlp category with HTTP client."""
        ...
