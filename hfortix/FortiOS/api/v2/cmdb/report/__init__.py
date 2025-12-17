"""
FortiOS Report API

Report configuration endpoints.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...http_client import HTTPClient


class Report:
    """Report API endpoints"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    @property
    def layout(self):
        """Access report layout endpoint"""
        if not hasattr(self, "_layout"):
            from .layout import Layout

            self._layout = Layout(self._client)
        return self._layout

    @property
    def setting(self):
        """Access report setting endpoint"""
        if not hasattr(self, "_setting"):
            from .setting import Setting

            self._setting = Setting(self._client)
        return self._setting
