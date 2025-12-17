"""
FortiOS API endpoint: firewall.wildcard-fqdn/custom

Config global/VDOM Wildcard FQDN address.
"""

from typing import Any, Dict, Optional

from hfortix.FortiOS.http_client import encode_path_component

from .....http_client import HTTPResponse


class Custom:
    """
    Manage wildcard FQDN custom addresses.

    Wildcard FQDN addresses allow matching domain names with wildcards.
    These can be used in firewall policies for more flexible domain matching.

    API Path: firewall.wildcard-fqdn/custom
    """

    def __init__(self, client):
        """
        Initialize the Custom endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def list(self, vdom=None, raw_json: bool = False, **params) -> HTTPResponse:
        """
        Get list of wildcard FQDN custom addresses.

        Args:
            vdom (str, optional): Virtual domain name
            raw_json: If True, return raw JSON response without unwrapping
            **params: Additional query parameters (filter, format, etc.)

        Returns:
            dict: API response with list of wildcard FQDN addresses

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.custom.list()
        """
        return self._client.get(
            "cmdb", "firewall.wildcard-fqdn/custom", vdom=vdom, params=params, raw_json=raw_json
        )

    def get(
        self,
        name: str,
        vdom=None,
        raw_json: bool = False,
        **params,
    ) -> HTTPResponse:
        """
        Get a specific wildcard FQDN custom address.

        Args:
            name (str): Address name
            vdom (str, optional): Virtual domain name
            **params: Additional query parameters

        Returns:
            dict: API response with address details

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.custom.get('*.example.com')
        """
        return self._client.get(
            "cmdb",
            f"firewall.wildcard-fqdn/custom/{name}",
            vdom=vdom,
            params=params,
            raw_json=raw_json,
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        wildcard_fqdn: str = None,
        color: int = None,
        comment: str = None,
        visibility: str = None,
        uuid: str = None,
        vdom=None,
        raw_json: bool = False,
    ) -> HTTPResponse:
        """
        Create a new wildcard FQDN custom address.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name (str): Address name
            wildcard_fqdn (str): Wildcard FQDN (e.g., *.example.com, mail.*.com)
            color (int): Color code (0-32, default 0)
            comment (str): Comment
            visibility (str): Enable/disable visibility: enable, disable
            uuid (str): Universally Unique Identifier (UUID)
            vdom (str, optional): Virtual domain name

        Returns:
            dict: API response

        Example:
            # Create wildcard FQDN address
            result = fgt.cmdb.firewall.wildcard_fqdn.custom.create(
                'wildcard-example',
                wildcard_fqdn='*.example.com',
                comment='Match all example.com subdomains'
            )

            # Create with color
            result = fgt.cmdb.firewall.wildcard_fqdn.custom.create(
                'mail-wildcard',
                wildcard_fqdn='mail.*',
                color=3,
                visibility='enable'
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
            if wildcard_fqdn is not None:
                payload_dict["wildcard-fqdn"] = wildcard_fqdn
            if color is not None:
                payload_dict["color"] = color
            if comment is not None:
                payload_dict["comment"] = comment
            if visibility is not None:
                payload_dict["visibility"] = visibility
            if uuid is not None:
                payload_dict["uuid"] = uuid

        payload_dict = {"name": name}

        if wildcard_fqdn is not None:
            payload_dict["wildcard-fqdn"] = wildcard_fqdn
        if color is not None:
            payload_dict["color"] = color
        if comment is not None:
            payload_dict["comment"] = comment
        if visibility is not None:
            payload_dict["visibility"] = visibility
        if uuid is not None:
            payload_dict["uuid"] = uuid

        return self._client.post(
            "cmdb", "firewall.wildcard-fqdn/custom", payload_dict, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        wildcard_fqdn: str = None,
        color: int = None,
        comment: str = None,
        visibility: str = None,
        uuid: str = None,
        vdom=None,
        raw_json: bool = False,
    ) -> HTTPResponse:
        """
        Update an existing wildcard FQDN custom address.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name (str): Address name
            wildcard_fqdn (str): Wildcard FQDN
            color (int): Color code (0-32)
            comment (str): Comment
            visibility (str): Enable/disable visibility: enable, disable
            uuid (str): Universally Unique Identifier (UUID)
            vdom (str, optional): Virtual domain name

        Returns:
            dict: API response

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.custom.update(
                'wildcard-example',
                comment='Updated comment',
                color=5
            )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if wildcard_fqdn is not None:
                payload_dict["wildcard-fqdn"] = wildcard_fqdn
            if color is not None:
                payload_dict["color"] = color
            if comment is not None:
                payload_dict["comment"] = comment
            if visibility is not None:
                payload_dict["visibility"] = visibility
            if uuid is not None:
                payload_dict["uuid"] = uuid

        payload_dict = {}

        if wildcard_fqdn is not None:
            payload_dict["wildcard-fqdn"] = wildcard_fqdn
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
            f"firewall.wildcard-fqdn/custom/{name}",
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
        Delete a wildcard FQDN custom address.

        Args:
            name (str): Address name
            vdom (str, optional): Virtual domain name

        Returns:
            dict: API response

        Example:
            result = fgt.cmdb.firewall.wildcard_fqdn.custom.delete('wildcard-example')
        """
        return self._client.delete(
            "cmdb", f"firewall.wildcard-fqdn/custom/{name}", vdom=vdom, raw_json=raw_json
        )

    def exists(self, name: str, vdom=None) -> HTTPResponse:
        """
        Check if a wildcard FQDN custom address exists.

        Args:
            name (str): Address name
            vdom (str, optional): Virtual domain name

        Returns:
            bool: True if address exists, False otherwise

        Example:
            if fgt.cmdb.firewall.wildcard_fqdn.custom.exists('wildcard-example'):
                print("Address exists")
        """
        try:
            result = self.get(name, vdom=vdom, raw_json=True)
            return result.get("status") == "success" and len(result.get("results", [])) > 0
        except Exception:
            return False
