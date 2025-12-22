"""
Helpers module for firewall API endpoints.

Provides shared helper functions to eliminate code duplication
across different firewall resource types (policy, address, addrgrp, etc.).

Includes functions for:
- Payload building
- List normalization
- Validation
- Data cleaning

Note: This module imports from the central API helpers and adds
firewall-specific functionality on top.
"""

# Import from central API helpers
from ...._helpers import (
    build_cmdb_payload,
    normalize_member_list,
    normalize_to_name_list,
)

__all__ = [
    # Central API helpers (re-exported for convenience)
    "build_cmdb_payload",
    "normalize_to_name_list",
    "normalize_member_list",
]
