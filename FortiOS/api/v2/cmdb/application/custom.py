"""
FortiOS CMDB - Application Custom Signatures

Configure custom application signatures.

API Endpoints:
    GET    /api/v2/cmdb/application/custom       - List all custom application signatures
    GET    /api/v2/cmdb/application/custom/{tag} - Get a specific custom application signature
    POST   /api/v2/cmdb/application/custom       - Create a new custom application signature
    PUT    /api/v2/cmdb/application/custom/{tag} - Update a custom application signature
    DELETE /api/v2/cmdb/application/custom/{tag} - Delete a custom application signature
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Custom:
    """Application custom signatures endpoint"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Custom endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        tag: Optional[str] = None,
        # Query parameters
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get custom application signature(s).

        Retrieves either a specific custom application signature by tag, or lists
        all custom application signatures with optional filtering.

        Args:
            tag (str, optional): Signature tag to retrieve. If None, retrieves all signatures
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (dict, optional): Skip to provided table's Nth entry
            acs (int, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            datasource (bool, optional): Include datasource information for each linked object
            with_meta (bool, optional): Include meta information about each object
            skip (bool, optional): Enable CLI skip operator to hide skipped properties
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing custom application signature data

        Examples:
            >>> # List all custom signatures
            >>> signatures = fgt.cmdb.application.custom.list()
            >>> for sig in signatures['results']:
            ...     print(sig['tag'], sig.get('comment', ''))

            >>> # Get a specific signature
            >>> sig = fgt.cmdb.application.custom.get('MyCustomApp')
            >>> print(sig['results']['signature'])

            >>> # Get with filtering
            >>> signatures = fgt.cmdb.application.custom.get(
            ...     format='tag|comment|protocol',
            ...     count=10
            ... )
        """
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

        # Build path
        path = 'application/custom'
        if tag:
            path = f'{path}/{tag}'

        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def list(
        self,
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[str] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        List all custom application signatures.

        Convenience method that calls get() without a specific tag.

        Args:
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (dict, optional): Skip to provided table's Nth entry
            acs (int, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            datasource (bool, optional): Include datasource information for each linked object
            with_meta (bool, optional): Include meta information about each object
            skip (bool, optional): Enable CLI skip operator to hide skipped properties
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing list of custom application signatures

        Examples:
            >>> # List all signatures
            >>> signatures = fgt.cmdb.application.custom.list()
            >>> print(f"Total signatures: {len(signatures['results'])}")

            >>> # List with count limit
            >>> signatures = fgt.cmdb.application.custom.list(count=5)
        """
        return self.get(
            tag=None,
            attr=attr,
            count=count,
            skip_to_datasource=skip_to_datasource,
            acs=acs,
            search=search,
            scope=scope,
            datasource=datasource,
            with_meta=with_meta,
            skip=skip,
            format=format,
            action=action,
            vdom=vdom,
            **kwargs
        )

    def create(
        self,
        tag: str,
        # Signature parameters
        id: Optional[int] = None,
        comment: Optional[str] = None,
        signature: Optional[str] = None,
        category: Optional[int] = None,
        protocol: Optional[str] = None,
        technology: Optional[str] = None,
        behavior: Optional[str] = None,
        vendor: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Create a new custom application signature.

        Args:
            tag (str, required): Signature tag (max 63 chars)
            id (int, optional): Custom application category ID (0-4294967295)
            comment (str, optional): Comment (max 63 chars)
            signature (str, optional): The actual custom application signature text (max 4095 chars)
            category (int, required): Custom application category ID (0-4294967295) - REQUIRED field!
            protocol (str, optional): Custom application signature protocol
            technology (str, optional): Custom application signature technology
            behavior (str, optional): Custom application signature behavior
            vendor (str, optional): Custom application signature vendor
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing creation status

        Examples:
            >>> # Create a simple custom signature (category is required!)
            >>> result = fgt.cmdb.application.custom.create(
            ...     tag='MyCustomApp',
            ...     comment='Custom web application',
            ...     signature='F-SBID( --protocol tcp; --service HTTP; --pattern "mycustomapp"; )',
            ...     category=15,  # Required!
            ...     protocol='HTTP'
            ... )

            >>> # Create with full details
            >>> result = fgt.cmdb.application.custom.create(
            ...     tag='CustomDatabase',
            ...     comment='Custom database protocol',
            ...     signature='F-SBID( --protocol tcp; --dst_port 5432; )',
            ...     protocol='TCP',
            ...     category=15,
            ...     technology='Client-Server',
            ...     behavior='Business'
            ... )
        """
        # Build data dictionary
        data = {}
        param_map = {
            'tag': tag,
            'id': id,
            'comment': comment,
            'signature': signature,
            'category': category,
            'protocol': protocol,
            'technology': technology,
            'behavior': behavior,
            'vendor': vendor,
        }

        # No special field mapping needed - all fields use same name
        for param_name, value in param_map.items():
            if value is not None:
                data[param_name] = value

        data.update(kwargs)

        return self._client.post('cmdb', 'application/custom', data, vdom=vdom)

    def update(
        self,
        tag: str,
        # Signature parameters
        id: Optional[int] = None,
        comment: Optional[str] = None,
        signature: Optional[str] = None,
        category: Optional[int] = None,
        protocol: Optional[str] = None,
        technology: Optional[str] = None,
        behavior: Optional[str] = None,
        vendor: Optional[str] = None,
        # Action parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Update an existing custom application signature.

        Args:
            tag (str, required): Signature tag to update
            id (int, optional): Custom application category ID (0-4294967295)
            comment (str, optional): Comment (max 63 chars)
            signature (str, optional): The actual custom application signature text (max 4095 chars)
            category (int, optional): Custom application category ID (0-4294967295)
            protocol (str, optional): Custom application signature protocol
            technology (str, optional): Custom application signature technology
            behavior (str, optional): Custom application signature behavior
            vendor (str, optional): Custom application signature vendor
            action (str, optional): Action to perform - 'move'
            before (str, optional): Move before this tag (requires action='move')
            after (str, optional): Move after this tag (requires action='move')
            scope (str, optional): Scope level - 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters to pass to the API

        Returns:
            dict: API response containing update status

        Examples:
            >>> # Update signature text
            >>> result = fgt.cmdb.application.custom.update(
            ...     tag='MyCustomApp',
            ...     signature='F-SBID( --protocol tcp; --service HTTPS; --pattern "newpattern"; )'
            ... )

            >>> # Update comment and protocol
            >>> result = fgt.cmdb.application.custom.update(
            ...     tag='CustomDatabase',
            ...     comment='Updated database protocol',
            ...     protocol='TCP/UDP'
            ... )

            >>> # Move signature in list
            >>> result = fgt.cmdb.application.custom.update(
            ...     tag='MyCustomApp',
            ...     action='move',
            ...     after='AnotherApp'
            ... )
        """
        # Build data dictionary
        data = {}
        param_map = {
            'tag': tag,
            'id': id,
            'comment': comment,
            'signature': signature,
            'category': category,
            'protocol': protocol,
            'technology': technology,
            'behavior': behavior,
            'vendor': vendor,
        }

        # No special field mapping needed
        for param_name, value in param_map.items():
            if value is not None:
                data[param_name] = value

        data.update(kwargs)

        # Build query parameters for action/move
        params = {}
        query_param_map = {
            'action': action,
            'before': before,
            'after': after,
            'scope': scope,
        }

        for key, value in query_param_map.items():
            if value is not None:
                params[key] = value

        return self._client.put(
            'cmdb',
            f'application/custom/{tag}',
            data,
            params=params if params else None,
            vdom=vdom
        )

    def delete(
        self,
        tag: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None
    ) -> dict[str, Any]:
        """
        Delete a custom application signature.

        Args:
            tag (str, required): Signature tag to delete
            scope (str, optional): Scope level - 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response containing deletion status

        Examples:
            >>> # Delete a custom signature
            >>> result = fgt.cmdb.application.custom.delete('MyCustomApp')
            >>> print(result['status'])

            >>> # Delete with specific scope
            >>> result = fgt.cmdb.application.custom.delete(
            ...     tag='CustomDatabase',
            ...     scope='vdom'
            ... )
        """
        params = {}
        if scope is not None:
            params['scope'] = scope

        return self._client.delete(
            'cmdb',
            f'application/custom/{tag}',
            params=params if params else None,
            vdom=vdom
        )
