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
    _raw_envelope: dict[str, Any] | None
    _response_time: float | None

    # ========================================================================
    # Explicit envelope properties (for autocomplete - these are common fields)
    # ========================================================================

    @property
    def http_status(self) -> int | None:
        """HTTP status code (200, 404, 500, etc.)."""
        ...

    @property
    def status(self) -> str | None:
        """API response status ('success' or 'error')."""
        ...

    @property
    def http_method(self) -> str | None:
        """HTTP method used (GET, POST, PUT, DELETE)."""
        ...

    @property
    def vdom(self) -> str | None:
        """Virtual domain name."""
        ...

    @property
    def mkey(self) -> str | int | None:
        """Primary key (mkey) of created/modified object."""
        ...

    @property
    def revision(self) -> str | None:
        """Configuration revision number."""
        ...

    @property
    def serial(self) -> str | None:
        """Device serial number."""
        ...

    @property
    def version(self) -> str | None:
        """FortiOS version string (e.g., 'v7.6.5')."""
        ...

    @property
    def build(self) -> int | None:
        """FortiOS firmware build number."""
        ...

    @property
    def http_response_time(self) -> float | None:
        """
        Response time in milliseconds for this API request.
        
        Returns None if timing was not tracked.
        
        Examples:
            >>> result = fgt.api.cmdb.firewall.address.get()
            >>> print(f"Query took {result.http_response_time:.1f}ms")
            Query took 45.2ms
        """
        ...

    @property
    def http_stats(self) -> dict[str, Any]:
        """
        HTTP request/response statistics summary.
        
        Returns a dictionary with key HTTP stats for debugging and monitoring.
        
        Returns:
            Dictionary with:
                - status_code: HTTP status code (200, 404, etc.)
                - response_time_ms: Response time in milliseconds
                - method: HTTP method (GET, POST, PUT, DELETE)
                - status: API status ('success' or 'error')
                - vdom: Virtual domain name
        
        Examples:
            >>> result = fgt.api.cmdb.firewall.address.get()
            >>> print(result.http_stats)
            {'status_code': 200, 'response_time_ms': 45.2, 'method': 'GET', 'status': 'success', 'vdom': 'root'}
        """
        ...

    def __init__(
        self,
        data: dict[str, Any],
        raw_envelope: dict[str, Any] | None = None,
        response_time: float | None = None,
    ) -> None:
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
        Get the raw/full API response envelope.

        Returns the complete API response including metadata like http_status,
        status, vdom, revision, etc. Use this when you need to check response
        status or access envelope-level information.

        Returns:
            Full API response envelope dictionary

        Examples:
            >>> policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
            >>> policy.raw
            {'http_status': 200, 'status': 'success', 'vdom': 'root', 'results': {...}}
            >>> policy.raw['status']
            'success'
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


_ObjectT = TypeVar("_ObjectT", bound=FortiObject)


class FortiObjectList(list[_ObjectT], Generic[_ObjectT]):
    """
    A list of FortiObject instances with convenient access to raw API response.
    
    This class extends the standard list to provide additional properties
    for accessing the data in different formats. It stores the full API
    envelope so you can access metadata like http_status, vdom, etc.
    
    Properties:
        dict: Returns list of dictionaries (each FortiObject as dict)
        json: Returns pretty-printed JSON string  
        raw: Returns the full API response envelope
        response_time: Response time in seconds
        response_time_ms: Response time in milliseconds
    
    Examples:
        >>> policies = fgt.api.cmdb.firewall.policy.get()
        >>> policies[0].name  # Access like normal list of FortiObjects
        'my-policy'
        >>> 
        >>> # Get as list of dicts
        >>> policies.dict
        [{'policyid': 1, 'name': 'my-policy', ...}, ...]
        >>>
        >>> # Get pretty JSON string
        >>> print(policies.json)
        [
          {
            "policyid": 1,
            "name": "my-policy",
            ...
          }
        ]
        >>>
        >>> # Get full API envelope with metadata
        >>> policies.raw
        {'http_status': 200, 'vdom': 'root', 'results': [...], ...}
        >>>
        >>> # Check response timing
        >>> print(f"Query took {policies.response_time_ms:.1f}ms")
        Query took 125.3ms
    """
    
    _raw_envelope: dict[str, Any] | None
    _response_time: float | None
    
    def __init__(
        self, 
        items: list[_ObjectT] | None = None, 
        raw_envelope: dict[str, Any] | None = None,
        response_time: float | None = None,
    ) -> None:
        """
        Initialize FortiObjectList.
        
        Args:
            items: List of FortiObject instances or other items
            raw_envelope: The full API response envelope (optional)
            response_time: Response time in seconds (optional)
        """
        ...

    # ========================================================================
    # Response timing properties
    # ========================================================================

    @property
    def http_response_time(self) -> float | None:
        """Response time in milliseconds for this API request."""
        ...

    @property
    def http_stats(self) -> dict[str, Any]:
        """
        HTTP request/response statistics summary.
        
        Returns a dictionary with key HTTP stats for debugging and monitoring.
        
        Returns:
            Dictionary with:
                - status_code: HTTP status code (200, 404, etc.)
                - response_time_ms: Response time in milliseconds
                - method: HTTP method (GET, POST, PUT, DELETE)
                - status: API status ('success' or 'error')
                - vdom: Virtual domain name
        """
        ...

    # ========================================================================
    # Envelope properties (common API response fields)
    # ========================================================================

    @property
    def http_status(self) -> int | None:
        """HTTP status code (200, 404, 500, etc.)."""
        ...

    @property
    def status(self) -> str | None:
        """API response status ('success' or 'error')."""
        ...

    @property
    def http_method(self) -> str | None:
        """HTTP method used (GET, POST, PUT, DELETE)."""
        ...

    @property
    def vdom(self) -> str | None:
        """Virtual domain name."""
        ...

    @property
    def serial(self) -> str | None:
        """Device serial number."""
        ...

    @property
    def version(self) -> str | None:
        """FortiOS version string (e.g., 'v7.6.5')."""
        ...

    @property
    def build(self) -> int | None:
        """FortiOS firmware build number."""
        ...
    
    @property
    def dict(self) -> list[dict[str, Any]]:
        """
        Get list of dictionaries.
        
        Converts each FortiObject back to its dictionary representation.
        Non-FortiObject items are returned as-is.
        
        Returns:
            List of dictionaries
        """
        ...
    
    @property
    def json(self) -> str:
        """
        Get pretty-printed JSON string of the list.
        
        Returns:
            JSON string with 2-space indentation
        """
        ...
    
    @property
    def raw(self) -> dict[str, Any] | list[dict[str, Any]]:
        """
        Get the full API response envelope.
        
        Returns the complete API response including metadata like
        http_status, vdom, revision, build, etc. If no envelope
        was stored, returns the list of dicts.
        
        Returns:
            Full API envelope dict, or list of dicts if no envelope available
        """
        ...


# Overloads for process_response to provide accurate return types
@overload
def process_response(
    result: list[dict[str, Any]],
    unwrap_single: Literal[False] = False,
    raw_envelope: dict[str, Any] | None = None,
    response_time: float | None = None,
) -> FortiObjectList:
    """Process list response - returns FortiObjectList."""
    ...

@overload
def process_response(
    result: list[dict[str, Any]],
    unwrap_single: Literal[True],
    raw_envelope: dict[str, Any] | None = None,
    response_time: float | None = None,
) -> FortiObject:
    """Process list response with unwrap_single - returns single FortiObject."""
    ...

@overload
def process_response(
    result: dict[str, Any],
    unwrap_single: bool = False,
    raw_envelope: dict[str, Any] | None = None,
    response_time: float | None = None,
) -> FortiObject | FortiObjectList:
    """Process dict response - may return FortiObject or FortiObjectList."""
    ...

# Fallback overload for any other types (strings, None, etc.)
@overload
def process_response(
    result: Any,
    unwrap_single: bool = False,
    raw_envelope: dict[str, Any] | None = None,
    response_time: float | None = None,
) -> Any:
    """Fallback for non-dict/list types - returns result as-is."""
    ...

def process_response(
    result: Any,
    unwrap_single: bool = False,
    raw_envelope: dict[str, Any] | None = None,
    response_time: float | None = None,
) -> Any:
    """
    Process API response - always returns FortiObject instances.

    Args:
        result: Raw API response (list or dict)
        unwrap_single: If True and result is single-item list, return just the item
        raw_envelope: Optional full API envelope to attach to FortiObjectList
        response_time: Optional response time in seconds for the HTTP request

    Returns:
        Processed response - FortiObject, FortiObjectList, or dict with FortiObjects

    Examples:
        >>> # List response - returns FortiObjectList
        >>> result = [{"name": "policy1", "srcaddr": [{"name": "addr1"}]}]
        >>> objects = process_response(result)
        >>> objects[0].name
        'policy1'
        >>> objects.raw  # Access full API envelope
        {'http_status': 200, 'results': [...]}

        >>> # Single item with unwrap_single
        >>> result = [{"name": "policy1"}]
        >>> obj = process_response(result, unwrap_single=True)
        >>> obj.name
        'policy1'

        >>> # Dict response with 'results' key
        >>> result = {'results': [{"name": "policy1"}], 'http_status': 200}
        >>> response = process_response(result)
        >>> response[0].name  # FortiObjectList
        'policy1'
    """
    ...
