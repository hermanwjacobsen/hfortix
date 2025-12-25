"""
Helpers module for FortiOS API endpoints.

Provides shared helper functions to eliminate code duplication
across all API resource types (CMDB, Monitor, etc.).

Includes functions for:
- Payload building (snake_case to kebab-case conversion)
- List normalization (various formats to FortiOS [{'name': '...'}] format)
- Type conversion (bool to enable/disable, etc.)
- Data cleaning and filtering
- Validation helpers (color, status, IP, MAC, etc.)

This is the central API helpers module that can be used by:
- hfortix.FortiOS.api.v2.cmdb.* (Configuration endpoints)
- hfortix.FortiOS.api.v2.monitor.* (Monitoring endpoints)
- hfortix.FortiOS.firewall.* (Convenience wrappers)
- hfortix.FortiOS.system.* (Future convenience wrappers)
- Any other API categories
"""

from .helpers import (
    build_cmdb_payload,
    build_cmdb_payload_normalized,
    convert_boolean_to_str,
    filter_empty_values,
    get_mkey,
    get_name,
    get_results,
    is_success,
    normalize_member_list,
    normalize_to_name_list,
    validate_color,
    validate_ip_address,
    validate_ip_network,
    validate_ipv6_address,
    validate_mac_address,
    validate_required_fields,
    validate_status,
)

__all__ = [
    # Payload building
    "build_cmdb_payload",
    "build_cmdb_payload_normalized",
    # List normalization
    "normalize_to_name_list",
    "normalize_member_list",
    # Data cleaning
    "filter_empty_values",
    # Type conversion
    "convert_boolean_to_str",
    # Response helpers
    "get_name",  # Recommended - more intuitive
    "get_mkey",  # Alias for backward compatibility
    "get_results",
    "is_success",
    # Validation - Generic (used across all modules)
    "validate_required_fields",
    "validate_color",
    "validate_status",
    "validate_mac_address",
    "validate_ip_address",
    "validate_ipv6_address",
    "validate_ip_network",
]
