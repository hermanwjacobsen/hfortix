"""
FortiOS CMDB - Firewall Address6 Group

Configure IPv6 address groups.

API Endpoints:
    GET    /api/v2/cmdb/firewall/addrgrp6           - List all / Get specific
    POST   /api/v2/cmdb/firewall/addrgrp6           - Create
    PUT    /api/v2/cmdb/firewall/addrgrp6/{name}   - Update
    DELETE /api/v2/cmdb/firewall/addrgrp6/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Addrgrp6:
    """Firewall IPv6 address group endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Addrgrp6 endpoint

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
        Get IPv6 address group object(s) - List all or get specific.

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
            >>> # List all IPv6 address groups
            >>> result = fgt.cmdb.firewall.addrgrp6.get()

            >>> # Get specific IPv6 address group
            >>> result = fgt.cmdb.firewall.addrgrp6.get('ipv6-internal-networks')

            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.addrgrp6.get('ipv6-internal-networks', with_meta=True)
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

        path = "firewall/addrgrp6"
        if name:
            path = f"{path}/{encode_path_component(name)}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        member: Optional[list[str] | list[dict[str, str]]] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        exclude: Optional[str] = None,
        exclude_member: Optional[list[dict[str, str]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create IPv6 address group object.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Address group name (required)
            member: List of address names (strings) or dicts [{'name': 'addr1'}] (required)
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            exclude: Enable/disable exclude members ('enable'|'disable')
            exclude_member: List of address dicts to exclude [{'name': 'addr1'}]
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # POST - Create IPv6 address group with string list (simplified API)
            >>> result = fgt.cmdb.firewall.addrgrp6.create(
            ...     name='ipv6-internal-networks',
            ...     member=['ipv6-subnet1', 'ipv6-subnet2'],
            ...     comment='All internal IPv6 networks'
            ... )

            >>> # POST - Create IPv6 address group with dict list (explicit format)
            >>> result = fgt.cmdb.firewall.addrgrp6.create(
            ...     name='ipv6-web-servers',
            ...     member=[{'name': 'ipv6-web1'}, {'name': 'ipv6-web2'}],
            ...     comment='IPv6 web server group'
            ... )

            >>> # POST - Create group with excluded members
            >>> result = fgt.cmdb.firewall.addrgrp6.create(
            ...     name='ipv6-trusted-nets',
            ...     member=['ipv6-all-internal'],
            ...     exclude='enable',
            ...     exclude_member=[{'name': 'ipv6-quarantine'}]
            ... )
        """
        # Convert member list if needed (simplified API)
        if member and isinstance(member, list) and len(member) > 0:
            if isinstance(member[0], str):
                member = [{"name": m} for m in member]

        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if name is not None:
                payload_dict["name"] = name
            if member is not None:
                # Convert string list to dict list if needed
                if isinstance(member, list) and len(member) > 0:
                    if isinstance(member[0], str):
                        member = [{"name": m} for m in member]
                payload_dict["member"] = member
            if comment is not None:
                payload_dict["comment"] = comment
            if visibility is not None:
                payload_dict["visibility"] = visibility
            if color is not None:
                payload_dict["color"] = color
            if tags is not None:
                payload_dict["tags"] = tags
            if exclude is not None:
                payload_dict["exclude"] = exclude
            if exclude_member is not None:
                payload_dict["exclude-member"] = exclude_member

        payload_dict = {"name": name, "member": member}

        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            "comment": "comment",
            "visibility": "visibility",
            "color": "color",
            "tags": "tags",
            "exclude": "exclude",
            "exclude_member": "exclude-member",
        }

        param_map = {
            "comment": comment,
            "visibility": visibility,
            "color": color,
            "tags": tags,
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

        path = "firewall/addrgrp6"
        return self._client.post("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        member: Optional[list[str] | list[dict[str, str]]] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        color: Optional[int] = None,
        tags: Optional[list[dict[str, Any]]] = None,
        exclude: Optional[str] = None,
        exclude_member: Optional[list[dict[str, str]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update IPv6 address group object.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Address group name (required)
            member: List of address names (strings) or dicts [{'name': 'addr1'}]
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            color: Icon color (0-32)
            tags: List of tag dicts [{'name': 'tag1'}]
            exclude: Enable/disable exclude members ('enable'|'disable')
            exclude_member: List of address dicts to exclude [{'name': 'addr1'}]
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # PUT - Update members with simplified API
            >>> result = fgt.cmdb.firewall.addrgrp6.update(
            ...     name='ipv6-internal-networks',
            ...     member=['ipv6-subnet1', 'ipv6-subnet2', 'ipv6-subnet3'],
            ...     comment='Updated IPv6 internal networks'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if member is not None:
                # Convert string list to dict list if needed
                if isinstance(member, list) and len(member) > 0:
                    if isinstance(member[0], str):
                        member = [{"name": m} for m in member]
                payload_dict["member"] = member
            if comment is not None:
                payload_dict["comment"] = comment
            if visibility is not None:
                payload_dict["visibility"] = visibility
            if color is not None:
                payload_dict["color"] = color
            if tags is not None:
                payload_dict["tags"] = tags
            if exclude is not None:
                payload_dict["exclude"] = exclude
            if exclude_member is not None:
                payload_dict["exclude-member"] = exclude_member

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
            "exclude": "exclude",
            "exclude_member": "exclude-member",
        }

        param_map = {
            "comment": comment,
            "visibility": visibility,
            "color": color,
            "tags": tags,
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

        path = f"firewall/addrgrp6/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete IPv6 address group object.

        Args:
            name: Address group name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete IPv6 address group
            >>> result = fgt.cmdb.firewall.addrgrp6.delete('test-group6')
        """
        path = f"firewall/addrgrp6/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if IPv6 address group object exists.

        Args:
            name: Address group name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if IPv6 address group exists
            >>> if fgt.cmdb.firewall.addrgrp6.exists('ipv6-internal-networks'):
            ...     print("IPv6 address group exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
