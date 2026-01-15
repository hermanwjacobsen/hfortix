"""Type stubs for VMLICENSE category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .download import Download
    from .download_eval import DownloadEval
    from .upload import Upload

__all__ = [
    "Download",
    "DownloadEval",
    "Upload",
    "Vmlicense",
]


class Vmlicense:
    """VMLICENSE API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    download: Download
    download_eval: DownloadEval
    upload: Upload

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize vmlicense category with HTTP client."""
        ...
