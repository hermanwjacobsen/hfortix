"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient

FortiOS CMDB - DLP Dictionary

Configure dictionaries used by DLP blocking.

API Endpoints:
    GET    /dlp/dictionary       - List all dictionaries
    GET    /dlp/dictionary/{name} - Get specific dictionary
    POST   /dlp/dictionary       - Create new dictionary
    PUT    /dlp/dictionary/{name} - Update dictionary
    DELETE /dlp/dictionary/{name} - Delete dictionary
"""

from __future__ import annotations
from typing import Any


class Dictionary:
    """DLP dictionary endpoint"""
    
    def __init__(self, client: 'HTTPClient') -> None:
        self._client = client
    
    def get(
        self,
        name: str | None = None,
        # Query parameters
        attr: str | None = None,
        count: int | None = None,
        skip_to_datasource: dict[str, Any] | None = None,
        acs: int | None = None,
        search: str | None = None,
        scope: str | None = None,
        datasource: bool | None = None,
        with_meta: bool | None = None,
        skip: bool | None = None,
        format: str | None = None,
        action: str | None = None,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Get DLP dictionary(s).
        
        Args:
            name: Dictionary name. If provided, gets specific dictionary.
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned results are in ascending order
            search: Filter objects by search value
            scope: Scope - 'global', 'vdom', or 'both'
            datasource: Include datasource information for each linked object
            with_meta: Include meta information (type id, references, etc)
            skip: Enable CLI skip operator to hide skipped properties
            format: List of property names to include (pipe-separated)
            action: Special actions - 'default', 'schema', 'revision'
            vdom: Virtual Domain(s). Use 'root' for single VDOM, or '*' for all
            **kwargs: Additional query parameters
        
        Returns:
            API response dictionary with dictionary configuration(s)
        
        Examples:
            >>> # Get all dictionaries
            >>> result = fgt.cmdb.dlp.dictionary.get()
            >>> print(f"Total dictionaries: {len(result['results'])}")
            
            >>> # Get specific dictionary
            >>> result = fgt.cmdb.dlp.dictionary.get('banned-words')
            >>> print(f"Match type: {result['results']['match-type']}")
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.dlp.dictionary.get(with_meta=True)
        """
        # Build path
        path = 'dlp/dictionary'
        if name:
            path = f'dlp/dictionary/{name}'
        
        # Build query parameters
        params = {}
        param_map = {
            'attr': attr,
            'count': count,
            'skip_to_datasource': skip_to_datasource,
            'acs': acs,
            'search': search,
            'scope': scope,
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'format': format,
            'action': action,
        }
        
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        
        params.update(kwargs)
        
        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)
    
    def list(
        self,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        List all DLP dictionaries (convenience method).
        
        Args:
            vdom: Virtual Domain(s)
            **kwargs: Additional query parameters
        
        Returns:
            API response dictionary with all dictionaries
        
        Examples:
            >>> # List all dictionaries
            >>> result = fgt.cmdb.dlp.dictionary.list()
            >>> for d in result['results']:
            ...     print(f"{d['name']}: {d.get('comment', 'N/A')}")
        """
        return self.get(vdom=vdom, **kwargs)
    
    def create(
        self,
        name: str,
        # Dictionary configuration
        uuid: str | None = None,
        match_type: str | None = None,
        match_around: str | None = None,
        comment: str | None = None,
        entries: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a new DLP dictionary.
        
        Args:
            name: Name of the dictionary (max 35 chars)
            uuid: Universally Unique Identifier (UUID; automatically assigned but can be manually reset)
            match_type: Logical relation between entries - 'match-all' or 'match-any' (default)
            match_around: Enable/disable match-around support - 'enable' or 'disable'
            comment: Optional comments (max 255 chars)
            entries: List of dictionary entries. Each entry is a dict with:
                - id (int): Entry ID (0-4294967295)
                - type (str): Pattern type to match (max 35 chars)
                - pattern (str): Pattern to match (max 255 chars)
                - ignore_case (str): Enable/disable ignore case - 'enable' or 'disable'
                - repeat (str): Enable/disable repeat match - 'enable' or 'disable'
                - status (str): Enable/disable this pattern - 'enable' or 'disable'
                - comment (str): Optional comments (max 255 chars)
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Create simple dictionary
            >>> result = fgt.cmdb.dlp.dictionary.create(
            ...     name='banned-words',
            ...     match_type='match-any',
            ...     comment='List of banned words',
            ...     entries=[
            ...         {'id': 1, 'type': 'keyword', 'pattern': 'confidential', 'status': 'enable'},
            ...         {'id': 2, 'type': 'keyword', 'pattern': 'secret', 'status': 'enable'}
            ...     ]
            ... )
            
            >>> # Create with case-insensitive matching
            >>> result = fgt.cmdb.dlp.dictionary.create(
            ...     name='pii-keywords',
            ...     match_type='match-any',
            ...     entries=[
            ...         {'id': 1, 'type': 'keyword', 'pattern': 'SSN', 
            ...          'ignore_case': 'enable', 'status': 'enable'},
            ...         {'id': 2, 'type': 'keyword', 'pattern': 'credit card',
            ...          'ignore_case': 'enable', 'status': 'enable'}
            ...     ]
            ... )
        """
        data = {}
        param_map = {
            'name': name,
            'uuid': uuid,
            'match_type': match_type,
            'match_around': match_around,
            'comment': comment,
            'entries': entries,
        }
        
        # Map to API field names
        api_field_map = {
            'name': 'name',
            'uuid': 'uuid',
            'match_type': 'match-type',
            'match_around': 'match-around',
            'comment': 'comment',
            'entries': 'entries',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                # Handle entries list - convert snake_case keys to hyphen-case
                if param_name == 'entries' and isinstance(value, list):
                    converted_entries = []
                    for entry in value:
                        converted_entry = {}
                        for k, v in entry.items():
                            # Convert snake_case to hyphen-case
                            api_key = k.replace('_', '-')
                            converted_entry[api_key] = v
                        converted_entries.append(converted_entry)
                    data[api_name] = converted_entries
                else:
                    data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.post('cmdb', 'dlp/dictionary', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        # Dictionary configuration
        uuid: str | None = None,
        match_type: str | None = None,
        match_around: str | None = None,
        comment: str | None = None,
        entries: list[dict[str, Any]] | None = None,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update an existing DLP dictionary.
        
        Args:
            name: Name of the dictionary to update
            uuid: Universally Unique Identifier (UUID)
            match_type: Logical relation between entries - 'match-all' or 'match-any'
            match_around: Enable/disable match-around support - 'enable' or 'disable'
            comment: Optional comments (max 255 chars)
            entries: List of dictionary entries. Each entry is a dict with:
                - id (int): Entry ID (0-4294967295)
                - type (str): Pattern type to match (max 35 chars)
                - pattern (str): Pattern to match (max 255 chars)
                - ignore_case (str): Enable/disable ignore case - 'enable' or 'disable'
                - repeat (str): Enable/disable repeat match - 'enable' or 'disable'
                - status (str): Enable/disable this pattern - 'enable' or 'disable'
                - comment (str): Optional comments (max 255 chars)
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update dictionary comment
            >>> result = fgt.cmdb.dlp.dictionary.update(
            ...     name='banned-words',
            ...     comment='Updated list of banned words'
            ... )
            
            >>> # Add new entries
            >>> result = fgt.cmdb.dlp.dictionary.update(
            ...     name='banned-words',
            ...     entries=[
            ...         {'id': 1, 'type': 'keyword', 'pattern': 'confidential', 'status': 'enable'},
            ...         {'id': 2, 'type': 'keyword', 'pattern': 'secret', 'status': 'enable'},
            ...         {'id': 3, 'type': 'keyword', 'pattern': 'private', 'status': 'enable'}
            ...     ]
            ... )
            
            >>> # Change match type
            >>> result = fgt.cmdb.dlp.dictionary.update(
            ...     name='banned-words',
            ...     match_type='match-all'
            ... )
        """
        data = {}
        param_map = {
            'name': name,
            'uuid': uuid,
            'match_type': match_type,
            'match_around': match_around,
            'comment': comment,
            'entries': entries,
        }
        
        # Map to API field names
        api_field_map = {
            'name': 'name',
            'uuid': 'uuid',
            'match_type': 'match-type',
            'match_around': 'match-around',
            'comment': 'comment',
            'entries': 'entries',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                # Handle entries list - convert snake_case keys to hyphen-case
                if param_name == 'entries' and isinstance(value, list):
                    converted_entries = []
                    for entry in value:
                        converted_entry = {}
                        for k, v in entry.items():
                            # Convert snake_case to hyphen-case
                            api_key = k.replace('_', '-')
                            converted_entry[api_key] = v
                        converted_entries.append(converted_entry)
                    data[api_name] = converted_entries
                else:
                    data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.put('cmdb', f'dlp/dictionary/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Delete a DLP dictionary.
        
        Args:
            name: Name of the dictionary to delete
            vdom: Virtual Domain(s)
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Delete dictionary
            >>> result = fgt.cmdb.dlp.dictionary.delete('banned-words')
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete('cmdb', f'dlp/dictionary/{name}', vdom=vdom)
