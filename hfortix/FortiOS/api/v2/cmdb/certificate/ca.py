"""
FortiOS CMDB - Certificate CA

View CA (Certificate Authority) certificates.

API Endpoints:
    GET    /certificate/ca       - List all CA certificates
    GET    /certificate/ca/{name} - Get specific CA certificate

Note: This is a READ-ONLY endpoint. CA certificates are typically:
    - Bundle certificates (pre-installed by Fortinet)
    - User-uploaded certificates via GUI/CLI
    - Factory certificates
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from .....exceptions import APIError, ResourceNotFoundError

if TYPE_CHECKING:
    from ....http_client import HTTPClient


from hfortix.FortiOS.http_client import encode_path_component


class Ca:
    """Certificate CA endpoint (read-only)"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize Ca endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all CA certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters (filter, format, count, search, etc.)

        Returns:
            dict: API response with list of CA certificates

        Examples:
            >>> # List all CA certificates
            >>> result = fgt.cmdb.certificate.ca.list()

            >>> # List only user-uploaded certificates
            >>> result = fgt.cmdb.certificate.ca.list(filter='source==user')

            >>> # List trusted certificates
            >>> result = fgt.cmdb.certificate.ca.list(filter='ssl-inspection-trusted==enable')
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
        Get CA certificate(s)

        Args:
            name (str, optional): CA certificate name (for specific certificate)
            filter (str): Filter results (e.g., 'source==bundle')
            format (str): Response format (name|brief|full)
            count (int): Limit number of results
            with_meta (bool): Include meta information
            skip (int): Skip N results
            search (str): Search string
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Get specific CA certificate
            >>> result = fgt.cmdb.certificate.ca.get('Fortinet_CA_SSL')

            >>> # Get all CA certificates
            >>> result = fgt.cmdb.certificate.ca.get()

            >>> # Get with details
            >>> result = fgt.cmdb.certificate.ca.get('Fortinet_CA_SSL', with_meta=True)
        """
        # Build path
        path = f"certificate/ca/{encode_path_component(name)}" if name else "certificate/ca"

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
        Check if CA certificate exists

        Args:
            name (str): CA certificate name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if exists, False otherwise

        Example:
            >>> if fgt.cmdb.certificate.ca.exists('Fortinet_CA_SSL'):
            ...     print('CA certificate exists')
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except (APIError, ResourceNotFoundError):
            return False

    def get_bundle_certificates(
        self, vdom: Optional[Union[str, bool]] = None, raw_json: bool = False
    ) -> dict[str, Any]:
        """
        Get all bundle (pre-installed) CA certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            raw_json (bool, optional): Return raw JSON response

        Returns:
            dict: API response with bundle certificates

        Example:
            >>> result = fgt.cmdb.certificate.ca.get_bundle_certificates()
            >>> print(f"Bundle CAs: {len(result['results'])}")
        """
        return self.get(filter="source==bundle", vdom=vdom, raw_json=raw_json)

    def get_user_certificates(
        self, vdom: Optional[Union[str, bool]] = None, raw_json: bool = False
    ) -> dict[str, Any]:
        """
        Get all user-uploaded CA certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            raw_json (bool, optional): Return raw JSON response

        Returns:
            dict: API response with user certificates

        Example:
            >>> result = fgt.cmdb.certificate.ca.get_user_certificates()
            >>> print(f"User CAs: {len(result['results'])}")
        """
        return self.get(filter="source==user", vdom=vdom, raw_json=raw_json)

    def get_trusted_certificates(
        self, vdom: Optional[Union[str, bool]] = None, raw_json: bool = False
    ) -> dict[str, Any]:
        """
        Get all trusted CA certificates (for SSL inspection)

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            raw_json (bool, optional): Return raw JSON response

        Returns:
            dict: API response with trusted certificates

        Example:
            >>> result = fgt.cmdb.certificate.ca.get_trusted_certificates()
            >>> print(f"Trusted CAs: {len(result['results'])}")
        """
        return self.get(filter="ssl-inspection-trusted==enable", vdom=vdom, raw_json=raw_json)
