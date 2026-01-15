"""
Type stubs for FortiOS Object Models

Provides type hints for zero-maintenance object wrappers for FortiOS API responses.
"""

from typing import Any, Generator, Generic, Literal, TypeVar, overload

_T = TypeVar("_T")
_DataT = TypeVar("_DataT", bound=dict[str, Any])

class FortiObject(Generic[_DataT]):
    """
    Zero-maintenance wrapper for FortiOS API responses.

    Provides clean attribute access to API response data with automatic
    flattening of member_table fields (lists of dicts with 'name' keys).

    Features:
    - No schemas required - works with any FortiOS version
    - No code generation - same class for all endpoints
    - No maintenance - automatically handles new fields
    - Auto-flattening of member_table fields for clean access
    - Escape hatch via get_full() for raw data access

    Common Response Fields (present in most API responses):
        status: API response status ("success" or "error")
        http_status: HTTP status code (200, 404, 500, etc.)
        error: Error code (integer, present when status="error")
        error_description: Human-readable error message
        vdom: Virtual domain name
        serial: Device serial number
        version: API version string
        build: Firmware build number

    Examples:
        >>> # From dict response
        >>> data = {"name": "policy1", "srcaddr": [{"name": "addr1"}]}
        >>> obj = FortiObject(data)
        >>>
        >>> # Clean attribute access
        >>> obj.name
        'policy1'
        >>>
        >>> # Auto-flattened member_table fields
        >>> obj.srcaddr
        ['addr1']
        >>>
        >>> # Get raw data when needed
        >>> obj.get_full('srcaddr')
        [{'name': 'addr1'}]
        >>>
        >>> # Convert back to dict
        >>> obj.to_dict()
        {'name': 'policy1', 'srcaddr': [{'name': 'addr1'}]}
        >>>
        >>> # Common response fields (autocomplete available)
        >>> result = fgt.api.cmdb.firewall.policy.delete(policyid=1)
        >>> result.status  # "success" or "error"
        >>> result.http_status  # 200, 404, etc.

    Args:
        data: Dictionary from FortiOS API response
    """

    _data: dict[str, Any]

    # Common API response fields (present in most responses, autocomplete available)
    status: str  # "success" or "error"
    http_status: int | None  # HTTP status code
    error: int | None  # Error code (when status="error")
    error_description: str | None  # Error message
    vdom: str | None  # Virtual domain
    serial: str | None  # Device serial number
    version: str | None  # API version
    build: int | None  # Firmware build number

    def __init__(self, data: dict[str, Any]) -> None:
        """
        Initialize FortiObject with API response data.

        Args:
            data: Dictionary containing the API response fields
        """
        ...

    def __getattr__(self, name: str) -> list | str | int | bool | dict | None:
        """
        Dynamic attribute access with automatic member_table flattening.

        For most FortiOS fields (strings, ints, etc.), returns the value as-is.
        For member_table fields (lists of dicts with 'name' key), automatically
        flattens to a FortiList of name strings for cleaner access with helper methods.

        NOTE: For autocomplete on list fields, use typing.cast():
            from typing import cast
            srcintf = cast(FortiList, policy.srcintf)
            srcintf.csv()  # <-- Now has full autocomplete!

        Args:
            name: Attribute name to access

        Returns:
            Field value - FortiList for list fields, original value otherwise

        Raises:
            AttributeError: If accessing private attributes (starting with '_')

        Examples:
            >>> obj.srcaddr  # Member table
            ['addr1', 'addr2']
            >>> obj.action  # Regular field
            'accept'
        """
        ...

    def get_full(self, name: str) -> Any:
        """
        Get raw field value without automatic processing.

        Use this when you need the full object structure from a member_table
        field instead of the auto-flattened name list.

        Args:
            name: Field name to retrieve

        Returns:
            Raw field value without any processing

        Examples:
            >>> obj.get_full('srcaddr')
            [{'name': 'addr1', 'q_origin_key': 'addr1'}]
        """
        ...

    def to_dict(self) -> dict[str, Any]:
        """
        Get the original dictionary data.

        Returns:
            Original API response dictionary

        Examples:
            >>> obj.to_dict()
            {'policyid': 1, 'name': 'policy1', ...}
        """
        ...
    
    @property
    def json(self) -> dict[str, Any]:
        """
        Get the raw JSON data as a dictionary.

        Alias for to_dict() providing a more intuitive interface.
        Use this when you need the complete API response structure.

        Returns:
            Original API response dictionary

        Examples:
            >>> policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
            >>> policy.json
            {'policyid': 1, 'name': 'my-policy', 'action': 'accept', ...}
        """
        ...
    
    @property
    def dict(self) -> dict[str, Any]:
        """
        Get the dictionary representation of the object.

        Alias for `.json` - provides an intuitive way to convert
        FortiObject back to a plain dictionary when needed.

        Returns:
            Original API response dictionary

        Examples:
            >>> policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
            >>> policy.dict
            {'policyid': 1, 'name': 'my-policy', ...}
        """
        ...
    
    @property
    def raw(self) -> dict[str, Any]:
        """
        Get the raw API response data.

        For most responses, this is identical to `.dict` and `.json`.
        Reserved for future use if we need to store additional metadata.

        Returns:
            Original API response dictionary

        Examples:
            >>> policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
            >>> policy.raw
            {'policyid': 1, 'name': 'my-policy', ...}
        """
        ...

    def __repr__(self) -> str:
        """
        String representation of the object.

        Returns:
            String showing object type and identifier (name or policyid)
        """
        ...

    def __contains__(self, key: str) -> bool:
        """
        Check if field exists in the object.

        Args:
            key: Field name to check

        Returns:
            True if field exists, False otherwise

        Examples:
            >>> 'srcaddr' in obj
            True
        """
        ...

    def __getitem__(self, key: str) -> Any:
        """
        Dictionary-style access to fields.

        Provides dict-like bracket notation access to object fields,
        with the same auto-flattening behavior as attribute access.

        Args:
            key: Field name to access

        Returns:
            Field value, with member_table fields auto-flattened

        Raises:
            KeyError: If the field does not exist

        Examples:
            >>> obj['srcaddr']
            ['addr1', 'addr2']
            >>> obj['action']
            'accept'
        """
        ...

    def __len__(self) -> int:
        """
        Get number of fields in the object.

        Returns:
            Number of fields in the response data

        Examples:
            >>> len(obj)
            15
        """
        ...

    def keys(self) -> Any:
        """
        Get all field names.

        Returns:
            Dictionary keys view of all field names

        Examples:
            >>> list(obj.keys())
            ['policyid', 'name', 'srcaddr', 'dstaddr', ...]
        """
        ...

    def values(self) -> Generator[Any, None, None]:
        """
        Get all field values (processed).

        Note: This returns processed values (with auto-flattening).
        Use to_dict().values() for raw values.

        Returns:
            Generator of processed field values
        """
        ...

    def items(self) -> Generator[tuple[str, Any], None, None]:
        """
        Get all field name-value pairs (processed).

        Note: This returns processed values (with auto-flattening).
        Use to_dict().items() for raw values.

        Returns:
            Generator of (key, processed_value) tuples
        """
        ...

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get field value with optional default (dict-like interface).

        Args:
            key: Field name to retrieve
            default: Value to return if field doesn't exist

        Returns:
            Processed field value or default

        Examples:
            >>> obj.get('action', 'deny')
            'accept'
            >>> obj.get('nonexistent', 'default')
            'default'
        """
        ...

# Overloads for process_response to provide accurate return types
@overload
def process_response(
    result: list[dict[str, Any]],
    unwrap_single: Literal[False] = False,
) -> list[FortiObject]:
    """Process list response - returns list of FortiObjects."""
    ...

@overload
def process_response(
    result: list[dict[str, Any]],
    unwrap_single: Literal[True],
) -> FortiObject:
    """Process list response with unwrap_single - returns single FortiObject."""
    ...

@overload
def process_response(
    result: dict[str, Any],
    unwrap_single: bool = False,
) -> FortiObject | dict[str, Any]:
    """Process dict response - may return FortiObject or dict with wrapped results."""
    ...

# Fallback overload for any other types (strings, None, etc.)
@overload
def process_response(
    result: Any,
    unwrap_single: bool = False,
) -> Any:
    """Fallback for non-dict/list types - returns result as-is."""
    ...

def process_response(
    result: Any,
    unwrap_single: bool = False,
) -> Any:
    """
    Process API response - always returns FortiObject instances.

    Handles both raw_json=False (list of results) and raw_json=True (full response dict).

    Args:
        result: Raw API response (list or dict)
        unwrap_single: If True and result is single-item list, return just the item

    Returns:
        Processed response - FortiObject or list[FortiObject]

    Examples:
        >>> # List response
        >>> result = [{"name": "policy1", "srcaddr": [{"name": "addr1"}]}]
        >>> objects = process_response(result)
        >>> objects[0].name
        'policy1'

        >>> # Single item with unwrap_single
        >>> result = [{"name": "policy1"}]
        >>> obj = process_response(result, unwrap_single=True)
        >>> obj.name
        'policy1'

        >>> # Dict response with 'results' key (raw_json=True)
        >>> result = {'results': [{"name": "policy1"}], 'http_status': 200}
        >>> response = process_response(result)
        >>> response['results'][0].name
        'policy1'
    """
    ...
