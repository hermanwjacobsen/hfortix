"""FortiOS CMDB DNS Filter Domain Filter API module.

This module provides methods for managing DNS domain filters.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class DomainFilter:
    """Manage DNS domain filter objects.

    This class provides methods to create, read, update, and delete DNS domain filter
    objects that contain domain filtering entries.
    """

    def __init__(self, client: Any) -> None:
        """Initialize DomainFilter API module.

        Args:
            client: The FortiOS API client instance.
        """
        self._client = client

    def get(
        self,
        filter_id: Optional[int] = None,
        vdom: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Retrieve DNS domain filter configuration.

        Args:
            filter_id (int, optional): Domain filter ID. If provided, retrieves specific filter.
                If not provided, retrieves all filters.
            vdom (str, optional): Virtual domain name. Defaults to 'root' if not specified.
            **kwargs: Additional parameters to pass to the API:
                - datasource (bool): Include datasource information
                - with_meta (bool): Include meta information
                - skip (bool): Enable skip operator
                - format (list): List of property names to include
                - filter (str): Filter expression
                - count (int): Maximum number of entries to return
                - start (int): Starting entry index

        Returns:
            dict: API response containing domain filter configuration.

        Example:
            >>> # Get all domain filters
            >>> filters = client.cmdb.dnsfilter.domain_filter.list()

            >>> # Get specific filter by ID
            >>> filter_obj = client.cmdb.dnsfilter.domain_filter.get(filter_id=1)
        """
        if filter_id is not None:
            path = f"dnsfilter/domain-filter/{filter_id}"
        else:
            path = "dnsfilter/domain-filter"

        params = {}
        if kwargs:
            params.update(kwargs)

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def list(self, vdom: Optional[str] = None, **kwargs: Any) -> dict[str, Any]:
        """List all DNS domain filters.

        Convenience method that calls get() without a filter_id.

        Args:
            vdom (str, optional): Virtual domain name.
            **kwargs: Additional query parameters.

        Returns:
            dict: API response containing list of all domain filters.

        Example:
            >>> filters = client.cmdb.dnsfilter.domain_filter.list()
            >>> for f in filters['results']:
            ...     print(f['id'], f['name'])
        """
        return self.get(vdom=vdom, **kwargs)

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        filter_id: Optional[int] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create a new DNS domain filter.

        Args:
            filter_id (int): Domain filter ID (0-4294967295).
            name (str): Name of the domain filter table (max 63 chars).
            comment (str, optional): Optional comment (max 255 chars).
            entries (list, optional): List of domain filter entries. Each entry is a dict with:
                - id (int): Entry ID
                - domain (str): Domain to filter (max 511 chars)
                - type (str): Filter type - 'simple', 'regex', 'wildcard'
                - action (str): Action to take - 'block', 'allow', 'monitor'
                - status (str): Enable/disable - 'enable' or 'disable'
                - comment (str, optional): Entry comment
            vdom (str, optional): Virtual domain name.
            **kwargs: Additional parameters.

        Returns:
            dict: API response containing operation results.

        Example:
            >>> # Create filter with blocking entries
            >>> client.cmdb.dnsfilter.domain_filter.create(
            ...     filter_id=10,
            ...     name='social-media-block',
            ...     comment='Block social media sites',
            ...     entries=[
            ...         {
            ...             'id': 1,
            ...             'domain': '*.facebook.com',
            ...             'type': 'wildcard',
            ...             'action': 'block',
            ...             'status': 'enable'
            ...         },
            ...         {
            ...             'id': 2,
            ...             'domain': '*.twitter.com',
            ...             'type': 'wildcard',
            ...             'action': 'block',
            ...             'status': 'enable'
            ...         }
            ...     ]
            ... )
        """
        data = {"id": filter_id, "name": name}

        if comment is not None:
            data["comment"] = comment

        if entries is not None:
            data["entries"] = entries

        if kwargs:
            data.update(kwargs)

        return self._client.post(
            "cmdb", "dnsfilter/domain-filter", data, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        filter_id: Optional[int] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[str] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Update an existing DNS domain filter.

        Args:
            filter_id (int): Domain filter ID to update.
            name (str, optional): Updated name (max 63 chars).
            comment (str, optional): Updated comment (max 255 chars).
            entries (list, optional): Updated list of domain filter entries. Each entry is a dict with:
                - id (int): Entry ID
                - domain (str): Domain to filter (max 511 chars)
                - type (str): Filter type - 'simple', 'regex', 'wildcard'
                - action (str): Action to take - 'block', 'allow', 'monitor'
                - status (str): Enable/disable - 'enable' or 'disable'
                - comment (str, optional): Entry comment
            vdom (str, optional): Virtual domain name.
            **kwargs: Additional parameters.

        Returns:
            dict: API response containing operation results.

        Example:
            >>> # Add monitoring entry to existing filter
            >>> client.cmdb.dnsfilter.domain_filter.update(
            ...     filter_id=10,
            ...     entries=[
            ...         {'id': 1, 'domain': '*.facebook.com', 'type': 'wildcard',
            ...          'action': 'block', 'status': 'enable'},
            ...         {'id': 2, 'domain': '*.linkedin.com', 'type': 'wildcard',
            ...          'action': 'monitor', 'status': 'enable'}
            ...     ]
            ... )
        """
        data = {}

        if name is not None:
            data["name"] = name

        if comment is not None:
            data["comment"] = comment

        if entries is not None:
            data["entries"] = entries

        if kwargs:
            data.update(kwargs)

        return self._client.put(
            "cmdb", f"dnsfilter/domain-filter/{filter_id}", data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        filter_id: int,
        vdom: Optional[str] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """Delete a DNS domain filter.

        Args:
            filter_id (int): Domain filter ID to delete.
            vdom (str, optional): Virtual domain name.

        Returns:
            dict: API response containing operation results.

        Example:
            >>> client.cmdb.dnsfilter.domain_filter.delete(filter_id=10)
        """
        return self._client.delete(
            "cmdb", f"dnsfilter/domain-filter/{filter_id}", vdom=vdom, raw_json=raw_json
        )
