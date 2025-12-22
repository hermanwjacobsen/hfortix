"""
FortiOS Service API - Packet capture management
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass

from .sniffer import Sniffer

__all__ = ["Sniffer"]
