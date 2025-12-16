"""
FortiOS CMDB - Extension Controller Extender

Configure FortiExtender controller settings.

API Endpoints:
    GET    /api/v2/cmdb/extension-controller/extender        - List all extenders
    GET    /api/v2/cmdb/extension-controller/extender/{name} - Get specific extender
    POST   /api/v2/cmdb/extension-controller/extender        - Create extender
    PUT    /api/v2/cmdb/extension-controller/extender/{name} - Update extender
    DELETE /api/v2/cmdb/extension-controller/extender/{name} - Delete extender
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Extender:
    """FortiExtender controller endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Extender endpoint.

        Args:
            client: FortiOS API client instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
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
        Get FortiExtender(s).

        Args:
            name (str, optional): Extender name. If None, retrieves all extenders
            (Other parameters same as dataplan.get())

        Returns:
            dict: API response containing extender data

        Examples:
            >>> extenders = fgt.cmdb.extension_controller.extender.list()
            >>> extender = fgt.cmdb.extension_controller.extender.get('FXT1')
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

        path = "extension-controller/extender"
        if name:
            path = f"{path}/{name}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

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
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Get all FortiExtenders (convenience method)."""
        return self.get(
            name=None,
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
            **kwargs,
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create a new FortiExtender.

        Args:
            name (str): Extender name/ID
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional extender parameters

        Returns:
            dict: API response
        """
        data = {"name": name}

        # Convert snake_case keys to hyphen-case
        for key, value in kwargs.items():
            data[key.replace("_", "-")] = value

        return self._client.post(
            "cmdb", "extension-controller/extender", data=data, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        action: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update a FortiExtender.

        Args:
            name (str): Extender name to update
            action (str, optional): 'add-members', 'replace-members', 'remove-members'
            before (str, optional): Place before given object
            after (str, optional): Place after given object
            scope (str, optional): Scope level
            vdom (str, optional): Virtual Domain name
            **kwargs: Additional parameters to update

        Returns:
            dict: API response
        """
        data = {}

        if action is not None:
            data["action"] = action
        if before is not None:
            data["before"] = before
        if after is not None:
            data["after"] = after
        if scope is not None:
            data["scope"] = scope

        # Convert snake_case keys to hyphen-case
        for key, value in kwargs.items():
            data[key.replace("_", "-")] = value

        return self._client.put(
            "cmdb", f"extension-controller/extender/{name}", data=data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a FortiExtender.

        Args:
            name (str): Extender name to delete
            scope (str, optional): Scope level
            vdom (str, optional): Virtual Domain name

        Returns:
            dict: API response
        """
        params = {}
        if scope is not None:
            params["scope"] = scope

        return self._client.delete(
            "cmdb",
            f"extension-controller/extender/{name}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )
