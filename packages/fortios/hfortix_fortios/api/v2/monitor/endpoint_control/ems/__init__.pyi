"""Type stubs for EMS category."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from .cert_status import CertStatus
    from .malware_hash import MalwareHash
    from .status import Status
    from .status_summary import StatusSummary
    from .unverify_cert import UnverifyCert
    from .verify_cert import VerifyCert

__all__ = [
    "CertStatus",
    "MalwareHash",
    "Status",
    "StatusSummary",
    "UnverifyCert",
    "VerifyCert",
    "Ems",
]


class Ems:
    """EMS API category.
    
    All endpoints return FortiObject instances with:
    - Attribute access: response.field
    - Dictionary access: response["field"]
    - Convert to dict: response.dict or response.json
    """
    
    cert_status: CertStatus
    malware_hash: MalwareHash
    status: Status
    status_summary: StatusSummary
    unverify_cert: UnverifyCert
    verify_cert: VerifyCert

    def __init__(self, client: IHTTPClient, vdom: str | None = None) -> None:
        """Initialize ems category with HTTP client."""
        ...
