"""
Shared utilities for building CMDB payloads across all endpoints.

This module provides reusable helper functions that eliminate code duplication
across different CMDB resource types (firewall, system, user, router, casb,
dnsfilter, access_proxy, etc.).
"""

from typing import Any, Dict, List, Union

# ============================================================================
# List Normalization
# ============================================================================


def normalize_to_name_list(
    value: Union[str, List[str], Dict[str, str], List[Dict[str, str]], None],
) -> List[Dict[str, str]]:
    """
    Normalize various input formats to FortiOS API format: [{'name': 'value'},
    ...]

    This is the most common list format used in FortiOS API for fields like:
    - srcintf, dstintf (firewall policy)
    - member (address groups, service groups)
    - interface (router, system)
    - etc.

    Args:
        value: Can be:
            - String: 'port1' → [{'name': 'port1'}]
            - List of strings: ['port1', 'port2'] → [{'name': 'port1'},
            {'name': 'port2'}]
            - Dict: {'name': 'port1'} → [{'name': 'port1'}]
            - List of dicts: [{'name': 'port1'}, {'name': 'port2'}] → unchanged
            - None: []

    Returns:
        List of dicts in FortiOS format

    Example:
        >>> normalize_to_name_list('port1')
        [{'name': 'port1'}]
        >>> normalize_to_name_list(['port1', 'port2'])
        [{'name': 'port1'}, {'name': 'port2'}]
        >>> normalize_to_name_list([{'name': 'port1'}])
        [{'name': 'port1'}]
    """
    if value is None:
        return []

    # Already a list
    if isinstance(value, list):
        if not value:
            return []
        # If first item is a dict, assume whole list is dicts
        if isinstance(value[0], dict):
            # Filter out empty dicts that sometimes appear in API responses
            filtered: list[dict[str, Any]] = [
                item
                for item in value
                if isinstance(item, dict) and item and "name" in item
            ]
            return filtered
        # List of strings
        return [{"name": str(item)} for item in value]

    # Single dict
    if isinstance(value, dict):
        return [value] if value and "name" in value else []

    # Single string
    return [{"name": str(value)}]


def normalize_member_list(
    value: Union[str, List[str], Dict[str, Any], List[Dict[str, Any]], None],
) -> List[Dict[str, str]]:
    """
    Normalize various input formats for 'member' fields in groups.

    Used for address groups, service groups, and other grouped resources.
    Similar to normalize_to_name_list but specifically for 'member' fields.

    Args:
        value: Can be:
            - String: 'addr1' → [{'name': 'addr1'}]
            - List of strings: ['addr1', 'addr2'] → [{'name': 'addr1'},
            {'name': 'addr2'}]
            - Dict: {'name': 'addr1'} → [{'name': 'addr1'}]
            - List of dicts: [{'name': 'addr1'}, {'name': 'addr2'}] → unchanged
            - None: []

    Returns:
        List of dicts in FortiOS format

    Example:
        >>> normalize_member_list('address1')
        [{'name': 'address1'}]
        >>> normalize_member_list(['address1', 'address2'])
        [{'name': 'address1'}, {'name': 'address2'}]
    """
    # For now, this is identical to normalize_to_name_list
    # But we keep it separate because member lists might need
    # different handling in the future (e.g., additional fields)
    return normalize_to_name_list(value)


# ============================================================================
# Payload Building
# ============================================================================


def build_cmdb_payload(**params: Any) -> dict[str, Any]:
    """
    Build a CMDB payload dictionary from keyword arguments (API layer - no
    normalization).

    Converts Python snake_case parameter names to FortiOS kebab-case API keys
    and filters out None values. This is the base helper used by all CMDB API
    endpoints.

    Does NOT normalize list fields - caller is responsible for providing data
    in the correct FortiOS format (unless using a wrapper with normalization).

    Args:
        **params: All resource parameters (e.g., name=..., member=..., etc.)

    Returns:
        Dictionary with FortiOS API-compatible keys and non-None values

    Example:
        >>> build_cmdb_payload(
        ...     name='my_address',
        ...     subnet='10.0.0.0 255.255.255.0',
        ...     associated_interface='port1'
        ... )
        {
            'name': 'my_address',
            'subnet': '10.0.0.0 255.255.255.0',
            'associated-interface': 'port1'
        }

        >>> build_cmdb_payload(
        ...     member=[{'name': 'addr1'}, {'name': 'addr2'}],
        ...     color=5,
        ...     comment='Test group'
        ... )
        {
            'member': [{'name': 'addr1'}, {'name': 'addr2'}],
            'color': 5,
            'comment': 'Test group'
        }
    """
    payload: dict[str, Any] = {}

    for param_name, value in params.items():
        if value is None:
            continue

        # Convert snake_case to kebab-case for FortiOS API
        api_key = param_name.replace("_", "-")
        payload[api_key] = value

    return payload


def build_cmdb_payload_normalized(
    normalize_fields: set[str] | None = None, **params: Any
) -> dict[str, Any]:
    """
    Build a CMDB payload with automatic normalization (convenience wrapper
    layer).

    Converts Python snake_case parameter names to FortiOS kebab-case API keys,
    filters out None values, AND normalizes specified list fields to FortiOS
    format.

    This is used by convenience wrappers to accept flexible inputs like strings
    or lists and automatically convert them to FortiOS [{'name': '...'}]
    format.

    Args:
        normalize_fields: Set of field names (snake_case) that should be
        normalized
                         to [{'name': '...'}] format. If None, common fields
                         like
                         'member', 'interface', 'allowaccess' are normalized.
        **params: All resource parameters

    Returns:
        Dictionary with FortiOS API-compatible keys and normalized values

    Example:
        >>> # Address group with member normalization
        >>> build_cmdb_payload_normalized(
        ...     normalize_fields={'member'},
        ...     name='my_group',
        ...     member=['addr1', 'addr2'],  # Gets normalized
        ...     comment='Test'
        ... )
        {
            'name': 'my_group',
            'member': [{'name': 'addr1'}, {'name': 'addr2'}],
            'comment': 'Test'
        }

        >>> # System interface with default normalization
        >>> build_cmdb_payload_normalized(
        ...     name='port1.100',
        ...     allowaccess=['ping', 'https'],  # Auto-normalized
        ...     ip='10.0.0.1 255.255.255.0'
        ... )
        {
            'name': 'port1.100',
            'allowaccess': [{'name': 'ping'}, {'name': 'https'}],
            'ip': '10.0.0.1 255.255.255.0'
        }
    """
    # Default fields that commonly need normalization across CMDB endpoints
    DEFAULT_NORMALIZE_FIELDS = {
        "member",  # address groups, service groups, user groups
        "interface",  # various config objects
        "allowaccess",  # system interfaces
        "srcintf",  # firewall policies, routes
        "dstintf",  # firewall policies, routes
        "srcaddr",  # firewall policies
        "dstaddr",  # firewall policies
        "service",  # firewall policies
        "users",  # various auth/policy objects
        "groups",  # various auth/policy objects
    }

    # Use provided fields or defaults
    fields_to_normalize = (
        normalize_fields
        if normalize_fields is not None
        else DEFAULT_NORMALIZE_FIELDS
    )

    payload: dict[str, Any] = {}

    for param_name, value in params.items():
        if value is None:
            continue

        # Convert snake_case to kebab-case for FortiOS API
        api_key = param_name.replace("_", "-")

        # Normalize list parameters to FortiOS format if specified
        if param_name in fields_to_normalize:
            normalized = normalize_to_name_list(value)
            # Only add if normalization resulted in non-empty list
            if normalized:
                payload[api_key] = normalized
        else:
            payload[api_key] = value

    return payload


# ============================================================================
# Data Cleaning
# ============================================================================


def filter_empty_values(payload: dict[str, Any]) -> dict[str, Any]:
    """
    Remove None values and empty collections from payload.

    Useful for cleaning up payloads before sending to FortiOS API,
    which may reject empty lists or None values in certain contexts.

    Args:
        payload: Dictionary to clean

    Returns:
        Dictionary with None and empty values removed

    Example:
        >>> filter_empty_values({
        ...     'name': 'test',
        ...     'member': [],
        ...     'comment': None,
        ...     'color': 5
        ... })
        {'name': 'test', 'color': 5}
    """
    cleaned: dict[str, Any] = {}

    for key, value in payload.items():
        # Skip None values
        if value is None:
            continue

        # Skip empty lists and dicts
        if isinstance(value, (list, dict)) and not value:
            continue

        cleaned[key] = value

    return cleaned


# ============================================================================
# Type Conversion
# ============================================================================


def convert_boolean_to_str(value: bool | str | None) -> str | None:
    """
    Convert Python boolean to FortiOS enable/disable string.

    FortiOS API typically uses 'enable'/'disable' instead of true/false.

    Args:
        value: Boolean, string, or None

    Returns:
        'enable', 'disable', the original string, or None

    Example:
        >>> convert_boolean_to_str(True)
        'enable'
        >>> convert_boolean_to_str(False)
        'disable'
        >>> convert_boolean_to_str('custom-value')
        'custom-value'
    """
    if value is None:
        return None
    if isinstance(value, bool):
        return "enable" if value else "disable"
    return str(value)


# ============================================================================
# Validation
# ============================================================================


def validate_required_fields(
    payload: dict[str, Any],
    required_fields: list[str],
) -> tuple[bool, list[str]]:
    """
    Validate that required fields are present in payload.

    Args:
        payload: Payload dictionary to validate
        required_fields: List of required field names (in kebab-case)

    Returns:
        Tuple of (is_valid, missing_fields)

    Example:
        >>> payload = {'name': 'test', 'subnet': '10.0.0.0/24'}
        >>> validate_required_fields(payload, ['name', 'subnet'])
        (True, [])
        >>> validate_required_fields(payload, ['name', 'subnet', 'interface'])
        (False, ['interface'])
    """
    missing = [field for field in required_fields if field not in payload]
    return (len(missing) == 0, missing)
