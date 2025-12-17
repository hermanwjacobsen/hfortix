"""
FortiOS CMDB - Router Access List

Configure access lists.

API Endpoints:
    GET    /api/v2/cmdb/router/access-list           - List all / Get specific
    POST   /api/v2/cmdb/router/access-list           - Create
    PUT    /api/v2/cmdb/router/access-list/{name}   - Update
    DELETE /api/v2/cmdb/router/access-list/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from hfortix.FortiOS.http_client import encode_path_component

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class AccessList:
    """Router access list endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Router Access List endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get access list(s) - List all or get specific.

        Args:
            name: Access list name (if specified, gets single list)
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional query parameters

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.router.access_list.get()
            >>> result = fgt.api.cmdb.router.access_list.get(name='ACL-1')
        """
        path = "router/access-list"
        if name:
            path = f"{path}/{encode_path_component(name)}"

        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def post(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        comments: Optional[str] = None,
        rule: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create access list.

        Args:
            data_dict: Complete access list dictionary
            name: Access list name
            comments: Comments
            rule: List of rules with id, action, prefix, wildcard, exact-match
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.router.access_list.create(
            ...     name='ACL-1',
            ...     comments='Block private networks'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        if name is not None:
            data["name"] = name
        if comments is not None:
            data["comments"] = comments
        if rule is not None:
            data["rule"] = rule

        data.update(kwargs)
        return self._client.post("cmdb", "router/access-list", data=data, vdom=vdom)

    def put(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        comments: Optional[str] = None,
        rule: Optional[list] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update access list.

        Args:
            name: Access list name (required)
            data_dict: Complete access list dictionary
            comments: Comments
            rule: List of rules
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)
            **kwargs: Additional parameters

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.router.access_list.update(
            ...     name='ACL-1',
            ...     comments='Updated comments'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        if comments is not None:
            data["comments"] = comments
        if rule is not None:
            data["rule"] = rule

        data.update(kwargs)
        path = f"router/access-list/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete access list.

        Args:
            name: Access list name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            API response dict

        Examples:
            >>> result = fgt.api.cmdb.router.access_list.delete(name='ACL-1')
        """
        path = f"router/access-list/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if access list exists.

        Args:
            name: Access list name
            vdom: Virtual domain (None=use default, False=skip vdom, or specific vdom)

        Returns:
            True if access list exists, False otherwise
        """
        try:
            self.get(name=name, vdom=vdom)
            return True
        except Exception:
            return False
