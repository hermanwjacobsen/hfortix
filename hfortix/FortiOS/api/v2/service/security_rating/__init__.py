"""
FortiOS Service API - Security rating and recommendations
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ....http_client import HTTPClient

from .security_rating import SecurityRating

__all__ = ["SecurityRating"]
