"""
FortiOS CMDB - Certificate CRL (Certificate Revocation List)

View CRL (Certificate Revocation List) certificates.

API Endpoints:
    GET    /certificate/crl       - List all CRL certificates
    GET    /certificate/crl/{name} - Get specific CRL certificate

Note: This is a READ-ONLY endpoint. CRL certificates are typically:
    - Factory CRLs (pre-installed)
    - User-uploaded CRLs via GUI/CLI
    - Auto-updated CRLs from LDAP/HTTP/SCEP sources
"""
from typing import TYPE_CHECKING, Any, Optional, Union

from FortiOS.exceptions import APIError, ResourceNotFoundError

if TYPE_CHECKING:
    from ....client import FortiOS


class Crl:
    """Certificate CRL endpoint (read-only)"""

    def __init__(self, client: 'FortiOS') -> None:
        """
        Initialize Crl endpoint

        Args:
            client: FortiOS client instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all CRL certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters (filter, format, count, search, etc.)

        Returns:
            dict: API response with list of CRL certificates

        Examples:
            >>> # List all CRL certificates
            >>> result = fgt.cmdb.certificate.crl.list()

            >>> # List only factory CRLs
            >>> result = fgt.cmdb.certificate.crl.list(filter='source==factory')

            >>> # List user-uploaded CRLs
            >>> result = fgt.cmdb.certificate.crl.list(filter='source==user')
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
        **kwargs: Any
    ) -> dict[str, Any]:
        """
        Get CRL certificate(s)

        Args:
            name (str, optional): CRL certificate name (for specific certificate)
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
            >>> # Get specific CRL certificate
            >>> result = fgt.cmdb.certificate.crl.get('my-crl')

            >>> # Get all CRL certificates
            >>> result = fgt.cmdb.certificate.crl.get()

            >>> # Get with details
            >>> result = fgt.cmdb.certificate.crl.get('my-crl', with_meta=True)
        """
        # Build path
        path = f'certificate/crl/{name}' if name else 'certificate/crl'

        # Build query parameters
        params = {}
        param_map = {
            'attr': attr,
            'count': count,
            'skip_to_datasource': skip_to_datasource,
            'acs': acs,
            'search': search,
            'scope': scope,
            'datasource': datasource,
            'with_meta': with_meta,
            'skip': skip,
            'format': format,
            'action': action
        }

        for key, value in param_map.items():
            if value is not None:
                params[key] = value

        # Add any additional parameters
        params.update(kwargs)

        return self._client.get('cmdb', path, params=params if params else None, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if CRL certificate exists

        Args:
            name (str): CRL certificate name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if exists, False otherwise

        Example:
            >>> if fgt.cmdb.certificate.crl.exists('my-crl'):
            ...     print('CRL certificate exists')
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except (APIError, ResourceNotFoundError):
            return False

    def get_factory_certificates(self, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Get all factory (pre-installed) CRL certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response with factory certificates

        Example:
            >>> result = fgt.cmdb.certificate.crl.get_factory_certificates()
            >>> print(f"Factory CRLs: {len(result['results'])}")
        """
        return self.get(filter='source==factory', vdom=vdom)

    def get_user_certificates(self, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Get all user-uploaded CRL certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response with user certificates

        Example:
            >>> result = fgt.cmdb.certificate.crl.get_user_certificates()
            >>> print(f"User CRLs: {len(result['results'])}")
        """
        return self.get(filter='source==user', vdom=vdom)

    def get_ldap_certificates(self, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Get all LDAP-sourced CRL certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response with LDAP certificates

        Example:
            >>> result = fgt.cmdb.certificate.crl.get_ldap_certificates()
            >>> print(f"LDAP CRLs: {len(result['results'])}")
        """
        return self.get(filter='ldap-server!=', vdom=vdom)

    def get_http_certificates(self, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Get all HTTP-sourced CRL certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response with HTTP certificates

        Example:
            >>> result = fgt.cmdb.certificate.crl.get_http_certificates()
            >>> print(f"HTTP CRLs: {len(result['results'])}")
        """
        return self.get(filter='http-url!=', vdom=vdom)
