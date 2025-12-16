"""
FortiOS CMDB - File Filter Profile

Configure file-filter profiles for content inspection and filtering.

API Endpoints:
    GET    /api/v2/cmdb/file-filter/profile        - List all file filter profiles
    GET    /api/v2/cmdb/file-filter/profile/{name} - Get specific file filter profile
    POST   /api/v2/cmdb/file-filter/profile        - Create file filter profile
    PUT    /api/v2/cmdb/file-filter/profile/{name} - Update file filter profile
    DELETE /api/v2/cmdb/file-filter/profile/{name} - Delete file filter profile
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Profile:
    """File filter profile endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
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
        Get file filter profile(s).

        Args:
            name: Profile name (if specified, gets single profile)
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
            >>> # List all file filter profiles
            >>> result = fgt.cmdb.file_filter.profile.list()

            >>> # Get specific profile
            >>> result = fgt.cmdb.file_filter.profile.get('default')

            >>> # Get with metadata
            >>> result = fgt.cmdb.file_filter.profile.get('default', with_meta=True)
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

        path = "file-filter/profile"
        if name:
            path = f"{path}/{name}"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        Get all file filter profiles.

        Args:
            vdom: Virtual domain
            **kwargs: Additional query parameters

        Returns:
            API response dict with list of profiles

        Examples:
            >>> # List all profiles
            >>> result = fgt.cmdb.file_filter.profile.list()
        """
        return self.get(name=None, vdom=vdom, **kwargs)

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create a new file filter profile.

        Args:
            name: Profile name
            vdom: Virtual domain
            **kwargs: Additional profile parameters including:
                - comment: Comment
                - feature_set: Feature set (flow, proxy)
                - replacemsg_group: Replacement message group
                - log: Enable/disable logging
                - extended_log: Enable/disable extended logging
                - scan_archive_contents: Enable/disable archive scanning
                - rules: List of file filter rules with:
                  - name: Rule name
                  - comment: Comment
                  - protocol: Protocol (http, ftp, etc.)
                  - filter: File type filter
                  - action: Action (log, block)
                  - direction: Direction (incoming, outgoing, any)
                  - password_protected: Action for password-protected files
                  - file_type: List of file types to filter

        Returns:
            API response dict

        Examples:
            >>> # Create basic profile
            >>> result = fgt.cmdb.file_filter.profile.create(
            ...     name='strict-filter',
            ...     comment='Strict file filtering',
            ...     log='enable'
            ... )

            >>> # Create with rules
            >>> result = fgt.cmdb.file_filter.profile.create(
            ...     name='office-filter',
            ...     comment='Block executable files',
            ...     rules=[{
            ...         'name': 'block-exe',
            ...         'protocol': 'http',
            ...         'action': 'block',
            ...         'file_type': ['exe', 'com', 'bat']
            ...     }]
            ... )
        """
        data = {"name": name}

        # Convert snake_case to hyphen-case for API
        for key, value in kwargs.items():
            api_key = key.replace("_", "-")
            data[api_key] = value

        return self._client.post(
            "cmdb", "file-filter/profile", data=data, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update a file filter profile.

        Args:
            name: Profile name
            vdom: Virtual domain
            **kwargs: Profile parameters to update (see create() for available parameters)

        Returns:
            API response dict

        Examples:
            >>> # Update logging settings
            >>> result = fgt.cmdb.file_filter.profile.update(
            ...     'strict-filter',
            ...     log='enable',
            ...     extended_log='enable'
            ... )

            >>> # Update rules
            >>> result = fgt.cmdb.file_filter.profile.update(
            ...     'office-filter',
            ...     rules=[{
            ...         'name': 'block-exe',
            ...         'protocol': 'http',
            ...         'action': 'block',
            ...         'file_type': ['exe', 'dll', 'sys']
            ...     }]
            ... )
        """
        data = {}

        # Convert snake_case to hyphen-case for API
        for key, value in kwargs.items():
            api_key = key.replace("_", "-")
            data[api_key] = value

        return self._client.put(
            "cmdb", f"file-filter/profile/{name}", data=data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a file filter profile.

        Args:
            name: Profile name
            scope: Scope level (global, vdom)
            vdom: Virtual domain

        Returns:
            API response dict

        Examples:
            >>> # Delete profile
            >>> result = fgt.cmdb.file_filter.profile.delete('strict-filter')
        """
        params = {}
        if scope is not None:
            params["scope"] = scope

        return self._client.delete(
            "cmdb",
            f"file-filter/profile/{name}",
            params=params if params else None,
            vdom=vdom,
            raw_json=raw_json,
        )
