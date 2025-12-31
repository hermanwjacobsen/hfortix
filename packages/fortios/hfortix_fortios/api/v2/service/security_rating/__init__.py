"""
FortiOS Service API - Security rating and recommendations
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from .security_rating import SecurityRating

__all__ = ["SecurityRating"]
