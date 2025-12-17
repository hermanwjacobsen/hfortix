"""
FortiOS CMDB - Firewall Service Category

Configure service categories.

API Endpoints:
    GET    /api/v2/cmdb/firewall.service/category           - List all / Get specific
    POST   /api/v2/cmdb/firewall.service/category           - Create
    PUT    /api/v2/cmdb/firewall.service/category/{name}   - Update
    DELETE /api/v2/cmdb/firewall.service/category/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class ServiceCategory:
    """Firewall service category endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize ServiceCategory endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        filter: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
        with_meta: Optional[bool] = None,
        datasource: Optional[bool] = None,
        format: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get service category configuration.

        Args:
            name: Category name (if None, returns all)
            filter: Filter results
            start: Starting entry index
            count: Maximum number of entries to return
            with_meta: Include metadata
            datasource: Include datasource information
            format: List of fields to return
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # Get all categories
            >>> result = fgt.cmdb.firewall.service.category.get()

            >>> # Get specific category
            >>> result = fgt.cmdb.firewall.service.category.get('General')

            >>> # Get with metadata
            >>> result = fgt.cmdb.firewall.service.category.get(
            ...     'Web Access',
            ...     with_meta=True
            ... )
        """
        params = {}
        param_map = {
            "filter": filter,
            "start": start,
            "count": count,
            "with_meta": with_meta,
            "datasource": datasource,
            "format": format,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        path = "firewall.service/category"
        if name:
            path = f"{path}/{encode_path_component(name)}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create service category.


        Supports two usage patterns:
        1. Pass data dict: create(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: create(key='value', vdom='root')
        Args:
            name: Category name (required)
            comment: Comment text (max 255 chars)
            fabric_object: Security Fabric global object setting - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # POST - Create basic category
            >>> result = fgt.cmdb.firewall.service.category.create(
            ...     name='Custom-Apps',
            ...     comment='Custom application services'
            ... )

            >>> # POST - Create with fabric object
            >>> result = fgt.cmdb.firewall.service.category.create(
            ...     name='Enterprise-Apps',
            ...     comment='Enterprise applications',
            ...     fabric_object='enable'
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
            if comment is not None:
                payload_dict["comment"] = comment
            if fabric_object is not None:
                payload_dict["fabric-object"] = fabric_object

        return self._client.post(
            "cmdb", "firewall.service/category", payload_dict, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        name: str,
        payload_dict: Optional[Dict[str, Any]] = None,
        comment: Optional[str] = None,
        fabric_object: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update service category.


        Supports two usage patterns:
        1. Pass data dict: update(payload_dict={'key': 'value'}, vdom='root')
        2. Pass kwargs: update(key='value', vdom='root')
        Args:
            name: Category name (required)
            comment: Comment text (max 255 chars)
            fabric_object: Security Fabric global object setting - 'enable' or 'disable'
            vdom: Virtual domain
            **kwargs: Additional parameters

        Returns:
            API response dictionary

        Examples:
            >>> # PUT - Update comment
            >>> result = fgt.cmdb.firewall.service.category.update(
            ...     name='Custom-Apps',
            ...     comment='Updated description'
            ... )

            >>> # Enable fabric object
            >>> result = fgt.cmdb.firewall.service.category.update(
            ...     name='Custom-Apps',
            ...     fabric_object='enable'
            ... )
        """
        # Pattern 1: data dict provided
        if payload_dict is not None:
            # Use provided data dict
            pass
        # Pattern 2: kwargs pattern - build data dict
        else:
            payload_dict = {}
            if comment is not None:
                payload_dict["comment"] = comment
            if fabric_object is not None:
                payload_dict["fabric-object"] = fabric_object

        return self._client.put(
            "cmdb", f"firewall.service/category/{name}", payload_dict, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a service category.

        Args:
            name: Category name
            vdom: Virtual domain

        Returns:
            API response dictionary

        Examples:
            >>> # Delete category
            >>> result = fgt.cmdb.firewall.service.category.delete('Custom-Apps')
        """
        return self._client.delete(
            "cmdb", f"firewall.service/category/{name}", vdom=vdom, raw_json=raw_json
        )

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if a service category exists.

        Args:
            name: Category name
            vdom: Virtual domain

        Returns:
            True if category exists, False otherwise

        Examples:
            >>> if fgt.cmdb.firewall.service.category.exists('General'):
            ...     print("Category exists")
        """
        try:
            result = self.get(name, vdom=vdom, raw_json=True)
            return (
                result.get("status") == "success"
                and result.get("http_status") == 200
                and len(result.get("results", [])) > 0
            )
        except Exception:
            return False
