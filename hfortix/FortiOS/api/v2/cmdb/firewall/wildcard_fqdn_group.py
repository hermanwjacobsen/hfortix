"""
FortiOS API endpoint: firewall.wildcard-fqdn/group

Config global Wildcard FQDN address groups.
"""

from typing import Any, Dict, Optional

from hfortix.FortiOS.http_client import encode_path_component

from .....http_client import HTTPResponse


class Group:
    """
    Manage wildcard FQDN address groups.

    Groups can contain multiple wildcard FQDN addresses for use in firewall policies.

    API Path: firewall.wildcard-fqdn/group
    """

    def __init__(self, client):
        """
        Initialize the Group endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def list(self, vdom=None, raw_json: bool = False, **params) -> HTTPResponse:
        """
        Get list of wildcard FQDN groups.

        Args:
            vdom (str, optional): Virtual domain name
            raw_json: If True, return raw JSON response without unwrapping
            **params: Additional query parameters (filter, format, etc.)

        Returns:
            dict: API response with list of groups

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.group.list()
        """
        return self._client.get(
            "cmdb", "firewall.wildcard-fqdn/group", vdom=vdom, params=params, raw_json=raw_json
        )

    def get(
        self,
        name: str,
        vdom=None,
        raw_json: bool = False,
        **params,
    ) -> HTTPResponse:
        """
        Get a specific wildcard FQDN group.

        Args:
            name (str): Group name
            vdom (str, optional): Virtual domain name
            **params: Additional query parameters

        Returns:
            dict: API response with group details

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.group.get('example-group')
        """
        return self._client.get(
            "cmdb",
            f"firewall.wildcard-fqdn/group/{name}",
            vdom=vdom,
            params=params,
            raw_json=raw_json,
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        member: list = None,
        color: int = None,
        comment: str = None,
        visibility: str = None,
        uuid: str = None,
        vdom=None,
        raw_json: bool = False,
    ) -> HTTPResponse:
        """
        Create a new wildcard FQDN group.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name (str): Group name
            member (list): List of wildcard FQDN address names (list of dicts with 'name' key)
            color (int): Color code (0-32, default 0)
            comment (str): Comment
            visibility (str): Enable/disable visibility: enable, disable
            uuid (str): Universally Unique Identifier (UUID)
            vdom (str, optional): Virtual domain name

        Returns:
            dict: API response

        Example:
            # Create group with members
            result = fgt.cmdb.firewall.wildcard_fqdn.group.create(
                'web-wildcards',
                member=[
                    {'name': '*.example.com'},
                    {'name': '*.test.com'}
                ],
                comment='Wildcard FQDN group for web domains'
            )
        """
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
            if color is not None:
                payload_dict["color"] = color
            if comment is not None:
                payload_dict["comment"] = comment
            if visibility is not None:
                payload_dict["visibility"] = visibility
            if uuid is not None:
                payload_dict["uuid"] = uuid

        payload_dict = {"name": name}

        if member is not None:
            payload_dict["member"] = member
        if color is not None:
            payload_dict["color"] = color
        if comment is not None:
            payload_dict["comment"] = comment
        if visibility is not None:
            payload_dict["visibility"] = visibility
        if uuid is not None:
            payload_dict["uuid"] = uuid

        return self._client.post(
            "cmdb", "firewall.wildcard-fqdn/group", payload_dict, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        member: list = None,
        color: int = None,
        comment: str = None,
        visibility: str = None,
        uuid: str = None,
        vdom=None,
        raw_json: bool = False,
    ) -> HTTPResponse:
        """
        Update an existing wildcard FQDN group.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name (str): Group name
            member (list): List of wildcard FQDN address names (list of dicts with 'name' key)
            color (int): Color code (0-32)
            comment (str): Comment
            visibility (str): Enable/disable visibility: enable, disable
            uuid (str): Universally Unique Identifier (UUID)
            vdom (str, optional): Virtual domain name

        Returns:
            dict: API response

        Example:
            # Update members
            result = fgt.cmdb.firewall.wildcard_fqdn.group.update(
                'web-wildcards',
                member=[
                    {'name': '*.example.com'},
                    {'name': '*.test.com'},
                    {'name': '*.newdomain.com'}
                ]
            )
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
            if color is not None:
                payload_dict["color"] = color
            if comment is not None:
                payload_dict["comment"] = comment
            if visibility is not None:
                payload_dict["visibility"] = visibility
            if uuid is not None:
                payload_dict["uuid"] = uuid

        payload_dict = {}

        if member is not None:
            payload_dict["member"] = member
        if color is not None:
            payload_dict["color"] = color
        if comment is not None:
            payload_dict["comment"] = comment
        if visibility is not None:
            payload_dict["visibility"] = visibility
        if uuid is not None:
            payload_dict["uuid"] = uuid

        return self._client.put(
            "cmdb",
            f"firewall.wildcard-fqdn/group/{name}",
            payload_dict,
            vdom=vdom,
            raw_json=raw_json,
        )

    def delete(
        self,
        name: str,
        vdom=None,
        raw_json: bool = False,
    ) -> HTTPResponse:
        """
        Delete a wildcard FQDN group.

        Args:
            name (str): Group name
            vdom (str, optional): Virtual domain name

        Returns:
            dict: API response

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.group.delete('web-wildcards')
        """
        return self._client.delete(
            "cmdb", f"firewall.wildcard-fqdn/group/{name}", vdom=vdom, raw_json=raw_json
        )

    def exists(self, name: str, vdom=None) -> HTTPResponse:
        """
        Check if a wildcard FQDN group exists.

        Args:
            name (str): Group name
            vdom (str, optional): Virtual domain name

        Returns:
            bool: True if group exists, False otherwise

        Example:
            if fgt.cmdb.firewall.wildcard_fqdn.group.exists('web-wildcards'):
                print("Group exists")
        """
        try:
            result = self.get(name, vdom=vdom, raw_json=True)
            return result.get("status") == "success" and len(result.get("results", [])) > 0
        except Exception:
            return False
