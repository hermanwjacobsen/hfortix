"""
CASB SaaS Application endpoint

GET    /api/v2/monitor/casb/saas-application/details
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ....http_client import HTTPClient

__all__ = ["SaasApplication"]


class SaasApplication:
    """
    CASB SaaS Application operations.

    Retrieve details about predefined SaaS applications.
    """

    def __init__(self, client: "HTTPClient"):
        """
        Initialize SaasApplication endpoint.

        Args:
            client: HTTPClient instance
        """
        self._client = client
        self._base_path = "casb/saas-application"

    def details(
        self, data_dict: Optional[dict[str, Any]] = None, mkey: Optional[str] = None, **kwargs: Any
    ) -> dict[str, Any]:
        """
        Retrieve details for CASB SaaS applications.

        Get details about predefined SaaS applications with matching domains,
        icons, and other metadata. Can filter by specific application key.

        Args:
            data_dict: Dictionary containing query parameters
            mkey: Optional application key to filter results. If not provided,
                  returns all SaaS applications.
            **kwargs: Additional parameters

        Returns:
            dict: Response containing SaaS application details. Returns a list
                  of applications with name, domains, icon_id, casb_display_name,
                  and other metadata.

        Raises:
            FortinetError: If the API request fails

        Examples:
            >>> # Get all SaaS applications
            >>> apps = fgt.api.monitor.casb.saas_application.details()
            >>> for app in apps.get("results", []):
            ...     print(f"{app['casb_display_name']}: {app['name']}")
            ...     print(f"  Domains: {', '.join(app['domains'])}")

            >>> # Get specific application using dict
            >>> salesforce = fgt.api.monitor.casb.saas_application.details(
            ...     data_dict={'mkey': 'Salesforce'}
            ... )

            >>> # Get specific application using keyword
            >>> salesforce = fgt.api.monitor.casb.saas_application.details(
            ...     mkey='Salesforce'
            ... )
            >>> print(f"Icon ID: {salesforce['results'][0]['icon_id']}")
        """
        params = data_dict.copy() if data_dict else {}

        # Map parameters
        if mkey is not None:
            params["mkey"] = mkey

        # Add any additional kwargs
        params.update(kwargs)

        return self._client.get("monitor", f"{self._base_path}/details", params=params)
