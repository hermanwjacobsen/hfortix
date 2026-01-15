"""
FortiOS Object Models

Provides zero-maintenance object wrappers for FortiOS API responses.
"""

from __future__ import annotations

from typing import Any


class FortiObject:
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

    Args:
        data: Dictionary from FortiOS API response
    """

    def __init__(self, data: dict):
        """
        Initialize FortiObject with API response data.

        Args:
            data: Dictionary containing the API response fields
        """
        self._data = data

    def __getattr__(self, name: str) -> Any:
        """
        Dynamic attribute access with automatic member_table flattening.

        For most FortiOS fields (strings, ints, etc.), returns the value as-is.
        For member_table fields (lists of dicts with 'name' key), automatically
        wraps each dict in a FortiObject for clean attribute access.

        Args:
            name: Attribute name to access

        Returns:
            Field value, with member_table dicts wrapped in FortiObject

        Raises:
            AttributeError: If accessing private attributes (starting with '_')

        Examples:
            >>> obj.srcaddr  # Member table as list of FortiObjects
            [FortiObject({'name': 'addr1'}), FortiObject({'name': 'addr2'})]
            >>> obj.srcaddr[0].name  # Access name attribute
            'addr1'
            >>> obj.action  # Regular field
            'accept'
        """
        if name.startswith("_"):
            raise AttributeError(
                f"'{type(self).__name__}' object has no attribute '{name}'"
            )

        # Resolve key: try exact name first, then snake_case -> hyphen-case
        key = name if name in self._data else name.replace("_", "-")

        # If key not present, behave like previous implementation and return None
        if key not in self._data:
            return None

        value = self._data.get(key)

        # Auto-wrap member_table fields (lists of dicts) in FortiObject
        if isinstance(value, list) and value:
            if isinstance(value[0], dict):
                return [FortiObject(item) for item in value]

        return value

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
        # Support both snake_case attribute names and hyphenated keys
        key = name if name in self._data else name.replace("_", "-")
        return self._data.get(key)

    def to_dict(self) -> dict:
        """
        Get the original dictionary data.

        Returns:
            Original API response dictionary

        Examples:
            >>> obj.to_dict()
            {'policyid': 1, 'name': 'policy1', ...}
        """
        return self._data

    @property
    def json(self) -> dict:
        """
        Get the raw JSON data as a dictionary.

        This is an alias for to_dict() providing a more intuitive interface.
        Use this when you need the complete API response structure.

        Returns:
            Original API response dictionary

        Examples:
            >>> policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
            >>> policy.json
            {'policyid': 1, 'name': 'my-policy', 'action': 'accept', ...}
            >>> policy.json['action']
            'accept'
        """
        return self._data
    
    @property
    def dict(self) -> dict:
        """
        Get the dictionary representation of the object.

        Alias for `.json` property - provides an intuitive way to convert
        FortiObject back to a plain dictionary when needed.

        Returns:
            Original API response dictionary

        Examples:
            >>> policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
            >>> policy.dict
            {'policyid': 1, 'name': 'my-policy', 'action': 'accept', ...}
            >>> 
            >>> # Use when you need dict operations
            >>> policy_dict = policy.dict
            >>> policy_dict.update({'comment': 'Updated via API'})
        """
        return self._data
    
    @property
    def raw(self) -> dict:
        """
        Get the raw API response data.

        For most responses, this is identical to `.dict` and `.json`.
        Reserved for future use if we need to store additional metadata
        like HTTP headers, status codes, or request information.

        Returns:
            Original API response dictionary

        Examples:
            >>> policy = fgt.api.cmdb.firewall.policy.get(policyid=1)
            >>> policy.raw
            {'policyid': 1, 'name': 'my-policy', 'action': 'accept', ...}
        """
        # For now, returns the same as .dict and .json
        # In future, could return full response with metadata if stored
        return self._data

    def __repr__(self) -> str:
        """
        String representation of the object.

        For simple objects (only containing 'name' and optionally 'q_origin_key'),
        returns just the name for cleaner output in lists. Otherwise, returns
        full FortiObject representation.

        Returns:
            String showing object identifier or full representation

        Examples:
            >>> repr(simple_member)  # Object with just {name: 'test'}
            "'test'"
            >>> repr(complex_obj)  # Object with multiple fields
            "FortiObject(test)"
        """
        # Try to find a meaningful identifier
        identifier = self._data.get("name") or self._data.get("policyid")

        # For simple member objects (only name + q_origin_key), just show the name
        # This makes lists of members much cleaner: ['addr1', 'addr2'] vs [FortiObject(addr1), ...]
        keys = set(self._data.keys())
        if keys == {"name"} or keys == {"name", "q_origin_key"}:
            return repr(self._data.get("name"))

        # For complex objects, show the full FortiObject representation
        if identifier:
            return f"FortiObject({identifier})"
        return f"FortiObject({len(self._data)} fields)"

    def __str__(self) -> str:
        """
        User-friendly string representation.

        Returns the primary identifier (name) for cleaner output in lists.
        Falls back to policyid or generic representation if name is not available.

        Examples:
            >>> str(obj)  # With name field
            'firewall_policy'
            >>> str(obj)  # With policyid field
            '1'
        """
        # Try to find a meaningful identifier - prefer name, then policyid
        return str(
            self._data.get("name")
            or self._data.get("policyid")
            or f"FortiObject({len(self._data)} fields)"
        )

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
        # Consider both exact key and underscore->hyphen variants
        return key in self._data or key.replace("_", "-") in self._data

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
        # Resolve key presence for both formats
        if key in self._data:
            raw_key = key
        elif key.replace("_", "-") in self._data:
            raw_key = key.replace("_", "-")
        else:
            raise KeyError(key)

        # Return processed value (apply same logic as attribute access)
        value = self._data[raw_key]
        if isinstance(value, list) and value and isinstance(value[0], dict):
            return [FortiObject(item) for item in value]
        return value

    def __len__(self) -> int:
        """
        Get number of fields in the object.

        Returns:
            Number of fields in the response data

        Examples:
            >>> len(obj)
            15
        """
        return len(self._data)

    def keys(self):
        """
        Get all field names.

        Returns:
            Dictionary keys view of all field names

        Examples:
            >>> list(obj.keys())
            ['policyid', 'name', 'srcaddr', 'dstaddr', ...]
        """
        return self._data.keys()

    def values(self):
        """
        Get all field values (processed).

        Note: This returns processed values (with auto-flattening).
        Use to_dict().values() for raw values.

        Returns:
            Generator of processed field values
        """
        for key in self._data.keys():
            yield getattr(self, key)

    def items(self):
        """
        Get all field name-value pairs (processed).

        Note: This returns processed values (with auto-flattening).
        Use to_dict().items() for raw values.

        Returns:
            Generator of (key, processed_value) tuples
        """
        for key in self._data.keys():
            yield (key, getattr(self, key))

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
        # Resolve raw key (support snake_case attribute to hyphenated keys)
        raw_key = key if key in self._data else key.replace("_", "-")
        if raw_key not in self._data:
            return default

        value = self._data[raw_key]
        if isinstance(value, list) and value and isinstance(value[0], dict):
            return [FortiObject(item) for item in value]
        return value


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
        >>> objects[0].srcaddr  # Auto-flattened!
        ['addr1']

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
        >>> response['http_status']
        200
    """
    # Wrap in FortiObject based on response type
    if isinstance(result, list):
        # raw_json=False: Direct list of results
        # Only wrap dict items in FortiObject; pass through non-dicts (strings, ints, etc.)
        wrapped = [
            FortiObject(item) if isinstance(item, dict) else item
            for item in result
        ]

        # If unwrap_single=True and we have exactly 1 item, return just that item
        # This happens when querying by mkey (e.g., get(name="specific_object"))
        if unwrap_single and len(wrapped) == 1:
            return wrapped[0]

        return wrapped
    elif isinstance(result, dict):
        # Check if this is a raw_json=True response with 'results' key
        if "results" in result and isinstance(result["results"], list):
            # raw_json=True: Preserve full response but wrap results in FortiObject
            # Only wrap dict items; pass through non-dicts
            wrapped_results = [
                FortiObject(item) if isinstance(item, dict) else item
                for item in result["results"]
            ]

            # If unwrap_single=True and we have exactly 1 item, unwrap it
            if unwrap_single and len(wrapped_results) == 1:
                return {**result, "results": wrapped_results[0]}

            return {**result, "results": wrapped_results}
        else:
            # Single object response (e.g., get with specific ID)
            return FortiObject(result)

    # Return as-is for any other type
    return result
