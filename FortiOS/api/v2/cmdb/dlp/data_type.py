"""
from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient

FortiOS CMDB - DLP Data Type

Configure predefined data type used by DLP blocking.

API Endpoints:
    GET    /dlp/data-type       - List all data types
    GET    /dlp/data-type/{name} - Get specific data type
    POST   /dlp/data-type       - Create new data type
    PUT    /dlp/data-type/{name} - Update data type
    DELETE /dlp/data-type/{name} - Delete data type
"""

from __future__ import annotations
from typing import Any


class DataType:
    """DLP data-type endpoint"""
    
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
        Get DLP data type(s).
        
        Args:
            name: Data type name. If provided, gets specific data type.
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
            API response dictionary with data type configuration(s)
        
        Examples:
            >>> # Get all data types
            >>> result = fgt.cmdb.dlp.data_type.get()
            >>> print(f"Total data types: {len(result['results'])}")
            
            >>> # Get specific data type
            >>> result = fgt.cmdb.dlp.data_type.get('credit-card')
            >>> print(f"Pattern: {result['results']['pattern']}")
            
            >>> # Get with metadata
            >>> result = fgt.cmdb.dlp.data_type.get(with_meta=True)
        """
        # Build path
        path = 'dlp/data-type'
        if name:
            path = f'dlp/data-type/{name}'
        
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
        List all DLP data types (convenience method).
        
        Args:
            vdom: Virtual Domain(s)
            **kwargs: Additional query parameters
        
        Returns:
            API response dictionary with all data types
        
        Examples:
            >>> # List all data types
            >>> result = fgt.cmdb.dlp.data_type.list()
            >>> for dt in result['results']:
            ...     print(f"{dt['name']}: {dt.get('comment', 'N/A')}")
        """
        return self.get(vdom=vdom, **kwargs)
    
    def create(
        self,
        name: str,
        # Data type configuration
        pattern: str | None = None,
        verify: str | None = None,
        verify2: str | None = None,
        match_around: str | None = None,
        look_back: int | None = None,
        look_ahead: int | None = None,
        match_back: int | None = None,
        match_ahead: int | None = None,
        transform: str | None = None,
        verify_transformed_pattern: str | None = None,
        comment: str | None = None,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Create a new DLP data type.
        
        Args:
            name: Name of the data type (max 35 chars)
            pattern: Regular expression pattern string without look around (max 255 chars)
            verify: Regular expression pattern string used to verify the data type (max 255 chars)
            verify2: Extra regular expression pattern string used to verify the data type (max 255 chars)
            match_around: Dictionary to check for match around (max 35 chars)
            look_back: Number of characters required to save for verification (1-255, default=1)
            look_ahead: Number of characters to obtain in advance for verification (1-255, default=1)
            match_back: Number of characters in front for match-around (1-4096, default=1)
            match_ahead: Number of characters behind for match-around (1-4096, default=1)
            transform: Template to transform user input to a pattern using capture group (max 255 chars)
            verify_transformed_pattern: Enable/disable verification for transformed pattern - 'enable' or 'disable'
            comment: Optional comments (max 255 chars)
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Create simple data type
            >>> result = fgt.cmdb.dlp.data_type.create(
            ...     name='custom-ssn',
            ...     pattern=r'\\d{3}-\\d{2}-\\d{4}',
            ...     comment='Custom SSN pattern'
            ... )
            
            >>> # Create with verification
            >>> result = fgt.cmdb.dlp.data_type.create(
            ...     name='custom-credit-card',
            ...     pattern=r'\\d{4}[\\s-]?\\d{4}[\\s-]?\\d{4}[\\s-]?\\d{4}',
            ...     verify=r'^[0-9]{13,19}$',
            ...     look_back=4,
            ...     look_ahead=4,
            ...     comment='Credit card with Luhn verification'
            ... )
        """
        data = {}
        param_map = {
            'name': name,
            'pattern': pattern,
            'verify': verify,
            'verify2': verify2,
            'match_around': match_around,
            'look_back': look_back,
            'look_ahead': look_ahead,
            'match_back': match_back,
            'match_ahead': match_ahead,
            'transform': transform,
            'verify_transformed_pattern': verify_transformed_pattern,
            'comment': comment,
        }
        
        # Map to API field names
        api_field_map = {
            'name': 'name',
            'pattern': 'pattern',
            'verify': 'verify',
            'verify2': 'verify2',
            'match_around': 'match-around',
            'look_back': 'look-back',
            'look_ahead': 'look-ahead',
            'match_back': 'match-back',
            'match_ahead': 'match-ahead',
            'transform': 'transform',
            'verify_transformed_pattern': 'verify-transformed-pattern',
            'comment': 'comment',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.post('cmdb', 'dlp/data-type', data, vdom=vdom)
    
    def update(
        self,
        name: str,
        # Data type configuration
        pattern: str | None = None,
        verify: str | None = None,
        verify2: str | None = None,
        match_around: str | None = None,
        look_back: int | None = None,
        look_ahead: int | None = None,
        match_back: int | None = None,
        match_ahead: int | None = None,
        transform: str | None = None,
        verify_transformed_pattern: str | None = None,
        comment: str | None = None,
        vdom: str | None = None,
        **kwargs
    ) -> dict[str, Any]:
        """
        Update an existing DLP data type.
        
        Args:
            name: Name of the data type to update
            pattern: Regular expression pattern string without look around (max 255 chars)
            verify: Regular expression pattern string used to verify the data type (max 255 chars)
            verify2: Extra regular expression pattern string used to verify the data type (max 255 chars)
            match_around: Dictionary to check for match around (max 35 chars)
            look_back: Number of characters required to save for verification (1-255)
            look_ahead: Number of characters to obtain in advance for verification (1-255)
            match_back: Number of characters in front for match-around (1-4096)
            match_ahead: Number of characters behind for match-around (1-4096)
            transform: Template to transform user input to a pattern using capture group (max 255 chars)
            verify_transformed_pattern: Enable/disable verification for transformed pattern - 'enable' or 'disable'
            comment: Optional comments (max 255 chars)
            vdom: Virtual Domain(s)
            **kwargs: Additional data parameters
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Update pattern
            >>> result = fgt.cmdb.dlp.data_type.update(
            ...     name='custom-ssn',
            ...     pattern=r'\\d{3}-?\\d{2}-?\\d{4}',
            ...     comment='Updated SSN pattern - optional hyphens'
            ... )
            
            >>> # Update verification settings
            >>> result = fgt.cmdb.dlp.data_type.update(
            ...     name='custom-credit-card',
            ...     look_back=8,
            ...     look_ahead=8,
            ...     verify_transformed_pattern='enable'
            ... )
        """
        data = {}
        param_map = {
            'name': name,
            'pattern': pattern,
            'verify': verify,
            'verify2': verify2,
            'match_around': match_around,
            'look_back': look_back,
            'look_ahead': look_ahead,
            'match_back': match_back,
            'match_ahead': match_ahead,
            'transform': transform,
            'verify_transformed_pattern': verify_transformed_pattern,
            'comment': comment,
        }
        
        # Map to API field names
        api_field_map = {
            'name': 'name',
            'pattern': 'pattern',
            'verify': 'verify',
            'verify2': 'verify2',
            'match_around': 'match-around',
            'look_back': 'look-back',
            'look_ahead': 'look-ahead',
            'match_back': 'match-back',
            'match_ahead': 'match-ahead',
            'transform': 'transform',
            'verify_transformed_pattern': 'verify-transformed-pattern',
            'comment': 'comment',
        }
        
        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value
        
        data.update(kwargs)
        
        return self._client.put('cmdb', f'dlp/data-type/{name}', data, vdom=vdom)
    
    def delete(
        self,
        name: str,
        vdom: str | None = None
    ) -> dict[str, Any]:
        """
        Delete a DLP data type.
        
        Args:
            name: Name of the data type to delete
            vdom: Virtual Domain(s)
        
        Returns:
            API response dictionary
        
        Examples:
            >>> # Delete data type
            >>> result = fgt.cmdb.dlp.data_type.delete('custom-ssn')
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete('cmdb', f'dlp/data-type/{name}', vdom=vdom)
