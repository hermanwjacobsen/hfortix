"""
FortiOS CMDB - Firewall Address6 Template

Configure IPv6 address templates.

API Endpoints:
    GET    /api/v2/cmdb/firewall/address6-template           - List all / Get specific
    POST   /api/v2/cmdb/firewall/address6-template           - Create
    PUT    /api/v2/cmdb/firewall/address6-template/{name}   - Update
    DELETE /api/v2/cmdb/firewall/address6-template/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Address6Template:
    """Firewall IPv6 address template endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Address6Template endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all IPv6 address template objects.

        Args:
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters (filter, format, count, etc.)

        Returns:
            API response dict with list of address template objects

        Examples:
            >>> # List all IPv6 address templates
            >>> result = fgt.cmdb.firewall.address6_template.list()
            >>> for tmpl in result['results']:
            ...     print(f"{tmpl['name']}: {tmpl.get('ip6', 'N/A')}")

            >>> # List with filters
            >>> result = fgt.cmdb.firewall.address6_template.list(
            ...     format=['name', 'ip6', 'comment']
            ... )
        """
        return self.get(vdom=vdom, **kwargs)

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
        Get IPv6 address template object(s) - List all or get specific.

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
            >>> # List all templates
            >>> result = fgt.cmdb.firewall.address6_template.get()

            >>> # Get specific template
            >>> result = fgt.cmdb.firewall.address6_template.get('ipv6-template')

            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.address6_template.get('ipv6-template', with_meta=True)
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

        path = "firewall/address6-template"
        if name:
            path = f"{path}/{encode_path_component(name)}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        ip6: Optional[str] = None,
        subnet_segment_count: Optional[int] = None,
        subnet_segment: Optional[list[dict[str, Any]]] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create IPv6 address template object.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Address template name (required)
            ip6: IPv6 prefix (required, e.g., '2001:db8::/32')
            subnet_segment_count: Number of subnet segments (default: 1)
            subnet_segment: List of subnet segment dicts with keys: 'id', 'name', 'bits', 'exclusive', 'values'
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # POST - Create IPv6 address template
            >>> result = fgt.cmdb.firewall.address6_template.create(
            ...     name='ipv6-subnet-template',
            ...     ip6='2001:db8::/32',
            ...     subnet_segment_count=2,
            ...     subnet_segment=[
            ...         {'id': 1, 'name': 'site', 'bits': 8, 'exclusive': 'disable'},
            ...         {'id': 2, 'name': 'vlan', 'bits': 8, 'exclusive': 'disable'}
            ...     ],
            ...     comment='IPv6 subnet template for site/vlan'
            ... )
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
            if ip6 is not None:
                payload_dict["ip6"] = ip6
            if subnet_segment_count is not None:
                payload_dict["subnet-segment-count"] = subnet_segment_count
            if subnet_segment is not None:
                payload_dict["subnet-segment"] = subnet_segment
            if comment is not None:
                payload_dict["comment"] = comment
            if visibility is not None:
                payload_dict["visibility"] = visibility

        payload_dict = {"name": name, "ip6": ip6, "subnet-segment-count": subnet_segment_count}

        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            "subnet_segment": "subnet-segment",
            "comment": "comment",
            "visibility": "visibility",
        }

        param_map = {
            "subnet_segment": subnet_segment,
            "comment": comment,
            "visibility": visibility,
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                payload_dict[api_key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = "firewall/address6-template"
        return self._client.post("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        ip6: Optional[str] = None,
        subnet_segment_count: Optional[int] = None,
        subnet_segment: Optional[list[dict[str, Any]]] = None,
        comment: Optional[str] = None,
        visibility: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update IPv6 address template object.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Address template name (required)
            ip6: IPv6 prefix (e.g., '2001:db8::/32')
            subnet_segment_count: Number of subnet segments
            subnet_segment: List of subnet segment dicts
            comment: Description/comment
            visibility: Enable/disable visibility ('enable'|'disable')
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> # PUT - Update IPv6 address template
            >>> result = fgt.cmdb.firewall.address6_template.update(
            ...     name='ipv6-subnet-template',
            ...     comment='Updated IPv6 subnet template'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if ip6 is not None:
                payload_dict["ip6"] = ip6
            if subnet_segment_count is not None:
                payload_dict["subnet-segment-count"] = subnet_segment_count
            if subnet_segment is not None:
                payload_dict["subnet-segment"] = subnet_segment
            if comment is not None:
                payload_dict["comment"] = comment
            if visibility is not None:
                payload_dict["visibility"] = visibility

        payload_dict = {}

        # Parameter mapping (convert snake_case to hyphenated-case)
        api_field_map = {
            "ip6": "ip6",
            "subnet_segment_count": "subnet-segment-count",
            "subnet_segment": "subnet-segment",
            "comment": "comment",
            "visibility": "visibility",
        }

        param_map = {
            "ip6": ip6,
            "subnet_segment_count": subnet_segment_count,
            "subnet_segment": subnet_segment,
            "comment": comment,
            "visibility": visibility,
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map.get(python_key, python_key)
                payload_dict[api_key] = value

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                payload_dict[key] = value

        path = f"firewall/address6-template/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=payload_dict, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete IPv6 address template object.

        Args:
            name: Address template name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> # Delete address template
            >>> result = fgt.cmdb.firewall.address6_template.delete('test-template')
        """
        path = f"firewall/address6-template/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom, raw_json=raw_json)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if IPv6 address template object exists.

        Args:
            name: Address template name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if object exists, False otherwise

        Examples:
            >>> # Check if template exists
            >>> if fgt.cmdb.firewall.address6_template.exists('ipv6-subnet-template'):
            ...     print("Template exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
