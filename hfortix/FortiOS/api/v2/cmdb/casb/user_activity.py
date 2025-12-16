"""
FortiOS CMDB - CASB User Activity Control

Configure CASB user activity controls for monitoring and restricting activities in SaaS applications.

API Endpoints:
    GET    /casb/user-activity       - List all user activity controls
    GET    /casb/user-activity/{name} - Get specific user activity control
    POST   /casb/user-activity       - Create user activity control
    PUT    /casb/user-activity/{name} - Update user activity control
    DELETE /casb/user-activity/{name} - Delete user activity control
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

from .....exceptions import APIError, ResourceNotFoundError

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class UserActivity:
    """CASB user activity endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize UserActivity endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all CASB user activity controls

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters (filter, format, count, search, etc.)

        Returns:
            dict: API response with list of user activity controls

        Examples:
            >>> # List all user activities
            >>> result = fgt.cmdb.casb.user_activity.list()

            >>> # List only custom activities
            >>> result = fgt.cmdb.casb.user_activity.list(filter='type==customized')

            >>> # List activities for specific app
            >>> result = fgt.cmdb.casb.user_activity.list(filter='application==box')
        """
        return self.get(vdom=vdom, **kwargs)

    def get(
        self,
        name: Optional[str] = None,
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
        Get CASB user activity control(s)

        Args:
            name (str, optional): User activity control name (for specific control)
            filter (str): Filter results (e.g., 'type==customized')
            format (str): Response format (name|brief|full)
            count (int): Limit number of results
            with_meta (bool): Include meta information
            skip (int): Skip N results
            search (str): Search string
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Get specific user activity
            >>> result = fgt.cmdb.casb.user_activity.get('box-upload-file')

            >>> # Get all activities
            >>> result = fgt.cmdb.casb.user_activity.get()
        """
        # Build path
        path = f"casb/user-activity/{name}" if name else "casb/user-activity"

        # Build query parameters
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

        # Add any additional parameters
        params.update(kwargs)

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        application: Optional[str] = None,
        casb_name: Optional[str] = None,
        status: str = "enable",
        category: Optional[str] = None,
        description: Optional[str] = None,
        match_strategy: Optional[str] = None,
        match: Optional[list[dict[str, Any]]] = None,
        control_options: Optional[list[dict[str, Any]]] = None,
        type: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Create new CASB user activity control

        Note: Custom user activity controls can only be created for customized SaaS applications

        Args:
            name (str): User activity control name
            application (str): SaaS application name
            casb_name (str): CASB-specific activity name
            status (str): Enable/disable status ('enable'|'disable')
            category (str, optional): Activity category ('activity-control'|'tenant-control'|'app-control')
            description (str, optional): Description of the activity
            match_strategy (str, optional): Match strategy ('or'|'and')
            match (list, optional): List of match rules
            control_options (list, optional): Control options configuration
            type (str, optional): Type ('built-in'|'customized')
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Create custom user activity control
            >>> result = fgt.cmdb.casb.user_activity.create(
            ...     name='my-app-upload',
            ...     application='my-custom-app',
            ...     casb_name='upload-file',
            ...     status='enable',
            ...     category='activity-control',
            ...     match_strategy='or'
            ... )
        """
        data = {"name": name, "application": application, "casb-name": casb_name, "status": status}

        if category is not None:
            data["category"] = category
        if description is not None:
            data["description"] = description
        if match_strategy is not None:
            data["match-strategy"] = match_strategy
        if match is not None:
            data["match"] = match
        if control_options is not None:
            data["control-options"] = control_options
        if type is not None:
            data["type"] = type

        return self._client.post("cmdb", "casb/user-activity", data, vdom=vdom, raw_json=raw_json)

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        status: Optional[str] = None,
        category: Optional[str] = None,
        description: Optional[str] = None,
        match_strategy: Optional[str] = None,
        match: Optional[list[dict[str, Any]]] = None,
        control_options: Optional[list[dict[str, Any]]] = None,
        application: Optional[str] = None,
        casb_name: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Update existing CASB user activity control

        Args:
            name (str): User activity control name to update
            status (str, optional): Enable/disable status
            category (str, optional): Activity category
            description (str, optional): Description
            match_strategy (str, optional): Match strategy
            match (list, optional): Match rules
            control_options (list, optional): Control options
            application (str, optional): SaaS application name
            casb_name (str, optional): CASB activity name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Update status
            >>> result = fgt.cmdb.casb.user_activity.update(
            ...     name='my-app-upload',
            ...     status='disable'
            ... )

            >>> # Update match strategy
            >>> result = fgt.cmdb.casb.user_activity.update(
            ...     name='my-app-upload',
            ...     match_strategy='and'
            ... )
        """
        data = {}

        if status is not None:
            data["status"] = status
        if category is not None:
            data["category"] = category
        if description is not None:
            data["description"] = description
        if match_strategy is not None:
            data["match-strategy"] = match_strategy
        if match is not None:
            data["match"] = match
        if control_options is not None:
            data["control-options"] = control_options
        if application is not None:
            data["application"] = application
        if casb_name is not None:
            data["casb-name"] = casb_name

        return self._client.put(
            "cmdb", f"casb/user-activity/{name}", data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete CASB user activity control

        Note: Built-in user activity controls cannot be deleted, only customized ones

        Args:
            name (str): User activity control name to delete
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Example:
            >>> result = fgt.cmdb.casb.user_activity.delete('my-app-upload')
        """
        return self._client.delete(
            "cmdb", f"casb/user-activity/{name}", vdom=vdom, raw_json=raw_json
        )

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if user activity control exists

        Args:
            name (str): User activity control name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if exists, False otherwise

        Example:
            >>> if fgt.cmdb.casb.user_activity.exists('box-upload-file'):
            ...     print('Activity control exists')
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except (APIError, ResourceNotFoundError):
            return False
