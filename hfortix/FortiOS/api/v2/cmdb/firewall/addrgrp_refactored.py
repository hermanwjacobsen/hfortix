"""
FortiOS CMDB - Firewall Address Group

Configure IPv4 address groups.

API Endpoints:
    GET    /api/v2/cmdb/firewall/addrgrp           - List all / Get specific
    POST   /api/v2/cmdb/firewall/addrgrp           - Create
    PUT    /api/v2/cmdb/firewall/addrgrp/{name}   - Update
    DELETE /api/v2/cmdb/firewall/addrgrp/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Addrgrp:
    """Firewall IPv4 address group endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Addrgrp endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        attr: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[dict] = None,
        acs: Optional[int] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        format: Optional[list] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get IPv4 address group object(s) - List all or get specific.

        Args:
            name: Object name (if specified, gets single object)
            attr: Attribute name that references other table
            count: Maximum number of entries to return
            skip_to_datasource: Skip to provided table's Nth entry
            acs: If true, returned result are in ascending order
            search: Filter objects by search value
            scope: Scope level (global, vdom, or both)
            datasource: Enable to include datasource information
            with_meta: Enable to include meta information
            skip: Enable to call CLI skip operator
            format: List of property names to include in results
            action: Special action (datasource, stats, schema, etc.)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> # List all address groups
            >>> result = fgt.cmdb.firewall.addrgrp.get()

            >>> # Get specific address group
            >>> result = fgt.cmdb.firewall.addrgrp.get('internal-networks')

            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.addrgrp.get('internal-networks', with_meta=True)
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

        path = "firewall/addrgrp"
        if name:
            path = f"{path}/{encode_path_component(name)}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        member: Optional[list[str] | list[dict[str, str]]] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        allow_routing: Optional[str] = None,
        exclude: Optional[str] = None,
        exclude_member: Optional[list[dict[str, str]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create IPv4 address group object.

        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'name': 'grp1', 'member': [...]}, vdom='root')
        2. Pass kwargs: create(name='grp1', member=[...], vdom='root')

        Args:
            payload_dict: Complete address group configuration dict (optional if using kwargs)
            name: Address group name (required if not using data)
            member: List of address names (strings) or dicts [{'name': 'addr1'}] (required if not using data)
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            allow_routing: Enable/disable routing ('enable'|'disable')
            exclude: Enable/disable exclude members ('enable'|'disable')
            exclude_member: List of address dicts to exclude [{'name': 'addr1'}]
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # POST - Create with data dict
            >>> result = fgt.cmdb.firewall.addrgrp.create(
            ...     payload_dict={'name': 'internal-networks', 'member': [{'name': 'subnet1'}]},
            ...     vdom='root'
            ... )

            >>> # POST - Create address group with string list (simplified API)
            >>> result = fgt.cmdb.firewall.addrgrp.create(
            ...     name='internal-networks',
            ...     member=['subnet1', 'subnet2', 'subnet3'],
            ...     comment='All internal networks'
            ... )

            >>> # POST - Create address group with dict list (explicit format)
            >>> result = fgt.cmdb.firewall.addrgrp.create(
            ...     name='web-servers',
            ...     member=[{'name': 'web1'}, {'name': 'web2'}],
            ...     comment='Web server group'
            ... )

            >>> # POST - Create group with excluded members
            >>> result = fgt.cmdb.firewall.addrgrp.create(
            ...     name='trusted-nets',
            ...     member=['all-internal'],
            ...     exclude='enable',
            ...     exclude_member=[{'name': 'quarantine-net'}]
            ... )
        """
        # Build data from kwargs if not provided
        if payload_dict is None:
            if name is None or member is None:
                raise ValueError("Either 'data' dict or both 'name' and 'member' must be provided")

            # Convert member list if needed (simplified API)
            if member and isinstance(member, list) and len(member) > 0:
                if isinstance(member[0], str):
                    member = [{"name": m} for m in member]

            payload_dict = {"name": name, "member": member}
        else:
            # If data dict is provided, process member field if needed
            if (
                "member" in data
                and isinstance(payload_dict["member"], list)
                and len(payload_dict["member"]) > 0
            ):
                if isinstance(payload_dict["member"][0], str):
                    payload_dict["member"] = [{"name": m} for m in payload_dict["member"]]

        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            "comment": "comment",
            "visibility": "visibility",
            "color": "color",
            "tags": "tags",
            "allow_routing": "allow-routing",
            "exclude": "exclude",
            "exclude_member": "exclude-member",
        }

        param_map = {
            "comment": comment,
            "visibility": visibility,
            "color": color,
            "tags": tags,
            "allow_routing": allow_routing,
            "exclude": exclude,
            "exclude_member": exclude_member,
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                payload_dict[api_key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = "firewall/addrgrp"
        return self._client.post("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str,
        payload_dict: Optional[dict[str, Any]] = None,
        member: Optional[list[str] | list[dict[str, str]]] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        allow_routing: Optional[str] = None,
        exclude: Optional[str] = None,
        exclude_member: Optional[list[dict[str, str]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update IPv4 address group object.

        Supports two usage patterns:
        1. Pass data dict: update(name='grp1', payload_dict={'member': [...]}, vdom='root')
        2. Pass kwargs: update(name='grp1', member=[...], vdom='root')

        Args:
            name: Address group name (required)
            payload_dict: Update configuration dict (optional if using kwargs)
            member: List of address names (strings) or dicts [{'name': 'addr1'}]
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            allow_routing: Enable/disable routing ('enable'|'disable')
            exclude: Enable/disable exclude members ('enable'|'disable')
            exclude_member: List of address dicts to exclude [{'name': 'addr1'}]
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # PUT - Update with data dict
            >>> result = fgt.cmdb.firewall.addrgrp.update(
            ...     name='internal-networks',
            ...     payload_dict={'comment': 'Updated comment'},
            ...     vdom='root'
            ... )

            >>> # PUT - Update members with simplified API
            >>> result = fgt.cmdb.firewall.addrgrp.update(
            ...     name='internal-networks',
            ...     member=['subnet1', 'subnet2', 'subnet3', 'subnet4'],
            ...     comment='Updated internal networks'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Handle member conversion in data dict pattern
            if (
                "member" in data
                and isinstance(payload_dict["member"], list)
                and len(payload_dict["member"]) > 0
            ):
                if isinstance(payload_dict["member"][0], str):
                    payload_dict["member"] = [{"name": m} for m in payload_dict["member"]]
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}

            # Convert member list if needed (simplified API)
            if member is not None:
                if isinstance(member, list) and len(member) > 0:
                    if isinstance(member[0], str):
                        member = [{"name": m} for m in member]
                payload_dict["member"] = member

            # Parameter mapping (convert snake_case to hyphenated-case)
            api_field_map = {
                "comment": "comment",
                "visibility": "visibility",
                "color": "color",
                "tags": "tags",
                "allow_routing": "allow-routing",
                "exclude": "exclude",
                "exclude_member": "exclude-member",
            }

            param_map = {
                "comment": comment,
                "visibility": visibility,
                "color": color,
                "tags": tags,
                "allow_routing": allow_routing,
                "exclude": exclude,
                "exclude_member": exclude_member,
            }

            for python_key, value in param_map.items():
                if value is not None:
                    api_key = api_field_map.get(python_key, python_key)
                    payload_dict[api_key] = value

            # Add any additional kwargs
            for key, value in kwargs.items():
                if value is not None:
                    payload_dict[key] = value

        path = f"firewall/addrgrp/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete IPv4 address group object.

        Args:
            name: Address group name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete address group
            >>> result = fgt.cmdb.firewall.addrgrp.delete('test-group')
        """
        path = f"firewall/addrgrp/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if IPv4 address group object exists.

        Args:
            name: Address group name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if address group exists
            >>> if fgt.cmdb.firewall.addrgrp.exists('internal-networks'):
            ...     print("Address group exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
