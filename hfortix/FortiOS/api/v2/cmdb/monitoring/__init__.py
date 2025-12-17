"""
FortiOS Monitoring API

Monitoring configuration endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Monitoring:
    """Monitoring API endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def npu_hpe(self):
        """Access NPU-HPE monitoring endpoint"""
        if not hasattr(self, "_npu_hpe"):
            from .npu_hpe import NpuHpe

            self._npu_hpe = NpuHpe(self._client)
        return self._npu_hpe
