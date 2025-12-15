"""
FortiOS CMDB - Certificate Remote

View remote certificates.

API Endpoints:
    GET    /certificate/remote       - List all remote certificates
    GET    /certificate/remote/{name} - Get specific remote certificate

Note: This is a READ-ONLY endpoint. Remote certificates are typically:
    - Certificates from remote servers
    - SSL/TLS certificates from external services
    - Certificates retrieved during SSL inspection
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from FortiOS.exceptions import APIError, ResourceNotFoundError

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Remote:
    """Certificate Remote endpoint (read-only)"""

    def __init__(self, client: 'HTTPClient') -> None:
        """
        Initialize Remote endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all remote certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters (filter, format, count, search, etc.)

        Returns:
            dict: API response with list of remote certificates

        Examples:
            >>> # List all remote certificates
            >>> result = fgt.cmdb.certificate.remote.list()

            >>> # List with search
            >>> result = fgt.cmdb.certificate.remote.list(search='vpn')
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
        Get remote certificate(s)

        Args:
            name (str, optional): Remote certificate name (for specific certificate)
            filter (str): Filter results
            format (str): Response format (name|brief|full)
            count (int): Limit number of results
            with_meta (bool): Include meta information
            skip (int): Skip N results
            search (str): Search string
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Examples:
            >>> # Get specific remote certificate
            >>> result = fgt.cmdb.certificate.remote.get('RemoteCert1')

            >>> # Get all remote certificates
            >>> result = fgt.cmdb.certificate.remote.get()

            >>> # Get with details
            >>> result = fgt.cmdb.certificate.remote.get('RemoteCert1', with_meta=True)
        """
        # Build path
        path = f'certificate/remote/{name}' if name else 'certificate/remote'

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
        Check if remote certificate exists

        Args:
            name (str): Remote certificate name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if exists, False otherwise

        Example:
            >>> if fgt.cmdb.certificate.remote.exists('RemoteCert1'):
            ...     print('Remote certificate exists')
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except (APIError, ResourceNotFoundError):
            return False
