"""
FortiOS CMDB - Email Filter Banned Word List

Configure AntiSpam banned word list.

API Endpoints:
    GET    /api/v2/cmdb/emailfilter/bword           - List all / Get specific
    POST   /api/v2/cmdb/emailfilter/bword           - Create
    PUT    /api/v2/cmdb/emailfilter/bword/{id}   - Update
    DELETE /api/v2/cmdb/emailfilter/bword/{id}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Bword:
    """Email filter banned word list endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Bword endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        list_id: Optional[int] = None,
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
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get email filter banned word list(s) - List all or get specific.

        Args:
            list_id (int, optional): List ID to retrieve. If None, retrieves all lists
            attr (str, optional): Attribute name that references other table
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (int, optional): Skip to provided table's Nth entry
            acs (bool, optional): If true, returned results are in ascending order
            search (str, optional): Filter objects by search value
            scope (str, optional): Scope level - 'global', 'vdom', or 'both'
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include meta information
            skip (bool, optional): Enable CLI skip operator
            format (str, optional): List of property names to include, separated by |
            action (str, optional): Special action - 'default', 'schema', 'revision'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional query parameters

        Returns:
            dict: API response containing banned word list data

        Examples:
            >>> # List all banned word lists
            >>> lists = fgt.cmdb.emailfilter.bword.list()

            >>> # Get a specific list by ID
            >>> list_data = fgt.cmdb.emailfilter.bword.get(1)

            >>> # Get with filtering
            >>> lists = fgt.cmdb.emailfilter.bword.get(
            ...     format='id|name|comment',
            ...     count=10
            ... )
        """
        params = {}
        param_map = {
            "attr": attr,
            "count": count,
            "skip_to_datasource": skip_to_datasource,
            "acs": acs,
            "search": search,
            "scope": scope,
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "format": format,
            "action": action,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = "emailfilter/bword"
        if list_id is not None:
            path = f"{path}/{list_id}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        # List configuration
        comment: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create email filter banned word list.

        Args:
            name (str): Banned word list name
            comment (str, optional): Optional comment
            entries (list, optional): List entries with pattern (banned word/phrase),
                                     status (enable/disable), where (subject/body/all),
                                     language (western/simch/trch/japanese/korean/french/thai/spanish),
                                     action (spam/clear/mark/tag), score (1-99999)
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # POST - Create banned word list
            >>> result = fgt.cmdb.emailfilter.bword.create(
            ...     name='profanity-filter',
            ...     comment='Block profanity in emails',
            ...     entries=[
            ...         {'pattern': 'badword', 'where': 'all', 'action': 'spam'},
            ...         {'pattern': 'inappropriate', 'where': 'subject', 'action': 'mark'}
            ...     ]
            ... )
        """
        data = {"name": name}

        if comment is not None:
            data["comment"] = comment
        if entries is not None:
            converted_entries = []
            for entry in entries:
                converted = {}
                for key, value in entry.items():
                    converted[key.replace("_", "-")] = value
                converted_entries.append(converted)
            data["entries"] = converted_entries

        data.update(kwargs)

        return self._client.post(
            "cmdb", "emailfilter/bword", data=data, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        list_id: Optional[int] = None,
        # List configuration
        name: Optional[str] = None,
        comment: Optional[str] = None,
        entries: Optional[list[dict[str, Any]]] = None,
        # PUT - Update parameters
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update an email filter banned word list.

        Args:
            list_id (int): List ID to update
            name (str, optional): Banned word list name
            comment (str, optional): Optional comment
            entries (list, optional): List entries with pattern, where, action, status
            action (str, optional): 'add-members', 'replace-members', 'remove-members'
            before (str, optional): Place new object before given object ID
            after (str, optional): Place new object after given object ID
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update banned word list
            >>> result = fgt.cmdb.emailfilter.bword.update(
            ...     list_id=1,
            ...     entries=[
            ...         {'pattern': 'newbadword', 'where': 'body', 'action': 'spam'}
            ...     ]
            ... )
        """
        data = {}

        if name is not None:
            data["name"] = name
        if comment is not None:
            data["comment"] = comment
        if entries is not None:
            converted_entries = []
            for entry in entries:
                converted = {}
                for key, value in entry.items():
                    converted[key.replace("_", "-")] = value
                converted_entries.append(converted)
            data["entries"] = converted_entries
        if action is not None:
            data["action"] = action
        if before is not None:
            data["before"] = before
        if after is not None:
            data["after"] = after
        if scope is not None:
            data["scope"] = scope

        data.update(kwargs)

        return self._client.put(
            "cmdb", f"emailfilter/bword/{list_id}", data=data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        list_id: int,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete an email filter banned word list.

        Args:
            list_id (int): List ID to delete
            scope (str, optional): Scope level - 'global' or 'vdom'
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response

        Examples:
            >>> result = fgt.cmdb.emailfilter.bword.delete(1)
        """
        params = {}
        if scope is not None:
            params["scope"] = scope

        return self._client.delete(
            "cmdb",
            f"emailfilter/bword/{list_id}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )
