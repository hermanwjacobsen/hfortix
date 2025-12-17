"""
FortiOS CMDB - CASB Profile

Configure CASB profile.

A CASB profile ties together SaaS applications with various security controls including:
- Safe search control
- Tenant control
- Domain control
- Access rules
- Custom controls

API Endpoints:
    GET    /casb/profile           - List all / Get specific
    POST   /casb/profile           - Create
    PUT    /casb/profile/{name}   - Update
    DELETE /casb/profile/{name}   - Delete
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Profile:
    """CASB profile endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize CASB Profile endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def get(
        self,
        name: Optional[str] = None,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        format: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[int] = None,
        skip_to_datasource: Optional[int] = None,
        acs: Optional[bool] = None,
        search: Optional[str] = None,
        scope: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get CASB profile(s) - List all or get specific

        Args:
            name (str, optional): Profile name (get specific profile)
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include metadata
            skip (bool, optional): Enable CLI skip operator
            action (str, optional): Special actions (default, schema, revision)
            format (str, optional): Field list to return (e.g., 'name|comment')
            filter (str, optional): Filter expression
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (str, optional): Skip to datasource
            acs (bool, optional): Ascending order
            search (str, optional): Search value
            scope (str, optional): Scope [global|vdom|both]
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response with CASB profile(s)

        Examples:
            >>> # Get all CASB profiles
            >>> profiles = fgt.cmdb.casb.profile.get()
            >>> print(f"Total profiles: {len(profiles['results'])}")

            >>> # Get specific profile
            >>> profile = fgt.cmdb.casb.profile.get('security-profile')
            >>> print(f"Comment: {profile['results']['comment']}")

            >>> # Get with filters
            >>> profiles = fgt.cmdb.casb.profile.get(
            ...     format='name|comment',
            ...     count=10
            ... )
        """
        # Build query parameters
        params = {}

        param_map = {
            "datasource": datasource,
            "with_meta": with_meta,
            "skip": skip,
            "action": action,
            "format": format,
            "filter": filter,
            "count": count,
            "skip_to_datasource": skip_to_datasource,
            "acs": acs,
            "search": search,
            "scope": scope,
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        params.update(kwargs)

        # Build path
        path = "casb/profile"
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
        saas_application: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create CASB profile

        Args:
            name (str): Profile name (required)
            comment (str, optional): Profile comment/description
            saas_application (list, optional): List of SaaS application configurations
                Each item can contain:
                - name (str): SaaS application name
                - status (str): 'enable' or 'disable'
                - safe_search (str): 'enable' or 'disable'
                - tenant_control (str): 'enable' or 'disable'
                - domain_control (str): 'enable' or 'disable'
                - log (str): 'enable' or 'disable'
                - access_rule (list): Access rules
                - custom_control (list): Custom controls
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters for the profile

        Returns:
            dict: API response

        Examples:
            >>> # POST - Create basic profile
            >>> result = fgt.cmdb.casb.profile.create(
            ...     name='office365-security',
            ...     comment='Office 365 security profile'
            ... )

            >>> # POST - Create profile with SaaS application
            >>> result = fgt.cmdb.casb.profile.create(
            ...     name='salesforce-profile',
            ...     comment='Salesforce monitoring profile',
            ...     saas_application=[{
            ...         'name': 'salesforce',
            ...         'status': 'enable',
            ...         'log': 'enable',
            ...         'safe_search': 'enable'
            ...     }]
            ... )
        """
        data = {"name": name}

        if comment is not None:
            data["comment"] = comment

        if saas_application is not None:
            # Convert Python naming to FortiOS API naming
            converted_apps = []
            for app in saas_application:
                converted_app = {}
                for key, value in app.items():
                    # Convert snake_case to kebab-case
                    api_key = key.replace("_", "-")
                    converted_app[api_key] = value
                converted_apps.append(converted_app)
            data["saas-application"] = converted_apps

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                # Convert Python naming to API naming
                api_key = key.replace("_", "-")
                data[api_key] = value

        return self._client.post("cmdb", "casb/profile", data=data, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        comment: Optional[str] = None,
        saas_application: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update CASB profile

        Args:
            name (str): Profile name (required)
            comment (str, optional): Profile comment/description
            saas_application (list, optional): List of SaaS application configurations
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters to update

        Returns:
            dict: API response

        Examples:
            >>> # PUT - Update profile comment
            >>> result = fgt.cmdb.casb.profile.update(
            ...     name='office365-security',
            ...     comment='Updated Office 365 security profile'
            ... )

            >>> # Add SaaS application to profile
            >>> result = fgt.cmdb.casb.profile.update(
            ...     name='office365-security',
            ...     saas_application=[{
            ...         'name': 'office365',
            ...         'status': 'enable',
            ...         'tenant_control': 'enable',
            ...         'log': 'enable'
            ...     }]
            ... )
        """
        data = {}

        if comment is not None:
            data["comment"] = comment

        if saas_application is not None:
            # Convert Python naming to FortiOS API naming
            converted_apps = []
            for app in saas_application:
                converted_app = {}
                for key, value in app.items():
                    # Convert snake_case to kebab-case
                    api_key = key.replace("_", "-")
                    converted_app[api_key] = value
                converted_apps.append(converted_app)
            data["saas-application"] = converted_apps

        # Add any additional kwargs
        for key, value in kwargs.items():
            if value is not None:
                # Convert Python naming to API naming
                api_key = key.replace("_", "-")
                data[api_key] = value

        return self._client.put(
            "cmdb", f"casb/profile/{name}", data=data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete a CASB profile

        Args:
            name (str): Profile name to delete
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Delete profile
            >>> result = fgt.cmdb.casb.profile.delete('old-profile')
            >>> if result['status'] == 'success':
            ...     print("Profile deleted successfully")
        """
        return self._client.delete("cmdb", f"casb/profile/{name}", vdom=vdom, raw_json=raw_json)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if a CASB profile exists

        Args:
            name (str): Profile name to check
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if profile exists, False otherwise

        Examples:
            >>> if fgt.cmdb.casb.profile.exists('security-profile'):
            ...     print("Profile exists")
            ... else:
            ...     print("Profile not found")
        """
        try:
            result = self.get(name=name, vdom=vdom, raw_json=True)
            return result.get("status") == "success" and "results" in result
        except Exception:
            return False
