"""
FortiOS CMDB - Certificate Local

View local certificates.

API Endpoints:
    GET    /certificate/local       - List all local certificates
    GET    /certificate/local/{name} - Get specific local certificate

Note: This is a READ-ONLY endpoint. Local certificates are typically:
    - Factory certificates (pre-installed by Fortinet)
    - User-uploaded certificates via GUI/CLI
    - ACME/Let's Encrypt certificates
    - SCEP certificates
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from .....exceptions import APIError, ResourceNotFoundError

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Local:
    """Certificate Local endpoint (read-only)"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Local endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all local certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters (filter, format, count, search, etc.)

        Returns:
            dict: API response with list of local certificates

        Examples:
            >>> # List all local certificates
            >>> result = fgt.cmdb.certificate.local.list()

            >>> # List only factory certificates
            >>> result = fgt.cmdb.certificate.local.list(filter='source==factory')

            >>> # List user-uploaded certificates
            >>> result = fgt.cmdb.certificate.local.list(filter='source==user')
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
        Get local certificate(s)

        Args:
            name (str, optional): Local certificate name (for specific certificate)
            filter (str): Filter results (e.g., 'source==factory')
            format (str): Response format (name|brief|full)
            count (int): Limit number of results
            with_meta (bool): Include meta information
            skip (int): Skip N results
            search (str): Search string
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Get specific local certificate
            >>> result = fgt.cmdb.certificate.local.get('Fortinet_CA_SSL')

            >>> # Get all local certificates
            >>> result = fgt.cmdb.certificate.local.get()

            >>> # Get with details
            >>> result = fgt.cmdb.certificate.local.get('Fortinet_CA_SSL', with_meta=True)
        """
        # Build path
        path = f"certificate/local/{encode_path_component(name)}" if name else "certificate/local"

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

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if local certificate exists

        Args:
            name (str): Local certificate name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if exists, False otherwise

        Example:
            >>> if fgt.cmdb.certificate.local.exists('Fortinet_CA_SSL'):
            ...     print('Local certificate exists')
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except (APIError, ResourceNotFoundError):
            return False

    def get_factory_certificates(
        self, vdom: Optional[Union[str, bool]] = None, raw_json: bool = False
    ) -> dict[str, Any]:
        """
        Get all factory (pre-installed) local certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            raw_json (bool, optional): Return raw JSON response

        Returns:
            dict: API response with factory certificates

        Example:
            >>> result = fgt.cmdb.certificate.local.get_factory_certificates()
            >>> print(f"Factory certificates: {len(result['results'])}")
        """
        return self.get(filter="source==factory", vdom=vdom, raw_json=raw_json)

    def get_user_certificates(
        self, vdom: Optional[Union[str, bool]] = None, raw_json: bool = False
    ) -> dict[str, Any]:
        """
        Get all user-uploaded local certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            raw_json (bool, optional): Return raw JSON response

        Returns:
            dict: API response with user certificates

        Example:
            >>> result = fgt.cmdb.certificate.local.get_user_certificates()
            >>> print(f"User certificates: {len(result['results'])}")
        """
        return self.get(filter="source==user", vdom=vdom, raw_json=raw_json)
