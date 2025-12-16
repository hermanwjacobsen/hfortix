"""
FortiOS CMDB - CASB SaaS Application

Configure CASB SaaS application.

API Endpoints:
    GET    /casb/saas-application       - List all SaaS applications
    GET    /casb/saas-application/{name} - Get specific SaaS application
    POST   /casb/saas-application       - Create SaaS application
    PUT    /casb/saas-application/{name} - Update SaaS application
    DELETE /casb/saas-application/{name} - Delete SaaS application
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, Optional, Union

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class SaasApplication:
    """CASB SaaS application endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize CASB SaaS Application endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all CASB SaaS applications

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response with list of SaaS applications

        Examples:
            >>> # List all SaaS applications
            >>> apps = fgt.cmdb.casb.saas_application.list()
            >>> for app in apps['results']:
            ...     print(f"{app['name']}: {app.get('type', 'N/A')}")
        """
        return self.get(vdom=vdom, **kwargs)

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
        Get CASB SaaS application(s)

        Args:
            name (str, optional): Application name (get specific application)
            datasource (bool, optional): Include datasource information
            with_meta (bool, optional): Include metadata
            skip (bool, optional): Enable CLI skip operator
            action (str, optional): Special actions (default, schema, revision)
            format (str, optional): Field list to return (e.g., 'name|type')
            filter (str, optional): Filter expression
            count (int, optional): Maximum number of entries to return
            skip_to_datasource (str, optional): Skip to datasource
            acs (bool, optional): Ascending order
            search (str, optional): Search value
            scope (str, optional): Scope [global|vdom|both]
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters

        Returns:
            dict: API response with SaaS application(s)

        Examples:
            >>> # Get all SaaS applications
            >>> apps = fgt.cmdb.casb.saas_application.get()
            >>> print(f"Total apps: {len(apps['results'])}")

            >>> # Get specific application
            >>> app = fgt.cmdb.casb.saas_application.get('office365')
            >>> print(f"Type: {app['results']['type']}")

            >>> # Get with filters
            >>> apps = fgt.cmdb.casb.saas_application.get(
            ...     format='name|type',
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

        # Add any additional parameters
        params.update(kwargs)

        # Build path
        path = f"casb/saas-application/{name}" if name else "casb/saas-application"

        return self._client.get(
            "cmdb", path, params=params if params else None, vdom=vdom, raw_json=raw_json
        )

    def create(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        casb_name: Optional[str] = None,
        status: Optional[str] = None,
        domain_control: Optional[str] = None,
        domain_control_domains: Optional[list[dict[str, Any]]] = None,
        log: Optional[str] = None,
        access_rule: Optional[list[dict[str, Any]]] = None,
        safe_search: Optional[str] = None,
        safe_search_control: Optional[list[str]] = None,
        tenant_control: Optional[str] = None,
        tenant_control_tenants: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create CASB SaaS application

        Args:
            name (str): Application name (required)
            type (str, optional): Application type - 'built-in' or 'customized'
            casb_name (str, optional): CASB application name
            status (str, optional): Enable/disable - 'enable' or 'disable'
            domain_control (str, optional): Enable domain control - 'enable' or 'disable'
            domain_control_domains (list, optional): List of domains to control
            log (str, optional): Enable logging - 'enable' or 'disable'
            access_rule (list, optional): List of access rules
            safe_search (str, optional): Enable safe search - 'enable' or 'disable'
            safe_search_control (list, optional): Safe search control settings
            tenant_control (str, optional): Enable tenant control - 'enable' or 'disable'
            tenant_control_tenants (list, optional): List of tenants to control
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Create custom SaaS application
            >>> result = fgt.cmdb.casb.saas_application.create(
            ...     name='my-custom-app',
            ...     type='customized',
            ...     status='enable'
            ... )

            >>> # Create with domain control
            >>> result = fgt.cmdb.casb.saas_application.create(
            ...     name='secure-app',
            ...     type='customized',
            ...     domain_control='enable',
            ...     log='enable'
            ... )
        """
        # Build data dictionary
        data = {"name": name}

        # Map parameters (Python snake_case to API hyphenated-case)
        param_map = {
            "type": type,
            "casb_name": casb_name,
            "status": status,
            "domain_control": domain_control,
            "domain_control_domains": domain_control_domains,
            "log": log,
            "access_rule": access_rule,
            "safe_search": safe_search,
            "safe_search_control": safe_search_control,
            "tenant_control": tenant_control,
            "tenant_control_tenants": tenant_control_tenants,
        }

        api_field_map = {
            "type": "type",
            "casb_name": "casb-name",
            "status": "status",
            "domain_control": "domain-control",
            "domain_control_domains": "domain-control-domains",
            "log": "log",
            "access_rule": "access-rule",
            "safe_search": "safe-search",
            "safe_search_control": "safe-search-control",
            "tenant_control": "tenant-control",
            "tenant_control_tenants": "tenant-control-tenants",
        }

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        # Add any additional parameters
        data.update(kwargs)

        return self._client.post(
            "cmdb", "casb/saas-application", data, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        payload_dict: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        casb_name: Optional[str] = None,
        status: Optional[str] = None,
        domain_control: Optional[str] = None,
        domain_control_domains: Optional[list[dict[str, Any]]] = None,
        log: Optional[str] = None,
        access_rule: Optional[list[dict[str, Any]]] = None,
        safe_search: Optional[str] = None,
        safe_search_control: Optional[list[str]] = None,
        tenant_control: Optional[str] = None,
        tenant_control_tenants: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update CASB SaaS application

        Args:
            name (str): Application name (required)
            type (str, optional): Application type - 'built-in' or 'customized'
            casb_name (str, optional): CASB application name
            status (str, optional): Enable/disable - 'enable' or 'disable'
            domain_control (str, optional): Enable domain control - 'enable' or 'disable'
            domain_control_domains (list, optional): List of domains to control
            log (str, optional): Enable logging - 'enable' or 'disable'
            access_rule (list, optional): List of access rules
            safe_search (str, optional): Enable safe search - 'enable' or 'disable'
            safe_search_control (list, optional): Safe search control settings
            tenant_control (str, optional): Enable tenant control - 'enable' or 'disable'
            tenant_control_tenants (list, optional): List of tenants to control
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional parameters

        Returns:
            dict: API response

        Examples:
            >>> # Update application status
            >>> result = fgt.cmdb.casb.saas_application.update(
            ...     name='my-custom-app',
            ...     status='disable'
            ... )

            >>> # Enable domain control
            >>> result = fgt.cmdb.casb.saas_application.update(
            ...     name='my-custom-app',
            ...     domain_control='enable',
            ...     log='enable'
            ... )
        """
        # Build data dictionary
        data = {}

        # Map parameters (Python snake_case to API hyphenated-case)
        param_map = {
            "type": type,
            "casb_name": casb_name,
            "status": status,
            "domain_control": domain_control,
            "domain_control_domains": domain_control_domains,
            "log": log,
            "access_rule": access_rule,
            "safe_search": safe_search,
            "safe_search_control": safe_search_control,
            "tenant_control": tenant_control,
            "tenant_control_tenants": tenant_control_tenants,
        }

        api_field_map = {
            "type": "type",
            "casb_name": "casb-name",
            "status": "status",
            "domain_control": "domain-control",
            "domain_control_domains": "domain-control-domains",
            "log": "log",
            "access_rule": "access-rule",
            "safe_search": "safe-search",
            "safe_search_control": "safe-search-control",
            "tenant_control": "tenant-control",
            "tenant_control_tenants": "tenant-control-tenants",
        }

        for param_name, value in param_map.items():
            if value is not None:
                api_name = api_field_map[param_name]
                data[api_name] = value

        # Add any additional parameters
        data.update(kwargs)

        return self._client.put(
            "cmdb", f"casb/saas-application/{name}", data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete CASB SaaS application

        Args:
            name (str): Application name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Delete SaaS application
            >>> result = fgt.cmdb.casb.saas_application.delete('my-custom-app')
            >>> print(f"Status: {result['status']}")
        """
        return self._client.delete(
            "cmdb", f"casb/saas-application/{name}", vdom=vdom, raw_json=raw_json
        )
