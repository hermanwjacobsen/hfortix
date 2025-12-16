"""
FortiOS CMDB - Certificate HSM-Local

Manage HSM (Hardware Security Module) local certificates.

API Endpoints:
    GET    /certificate/hsm-local           - List all HSM local certificates
    GET    /certificate/hsm-local/{name}    - Get specific HSM local certificate
    POST   /certificate/hsm-local           - Create new HSM local certificate
    PUT    /certificate/hsm-local/{name}    - Update HSM local certificate
    DELETE /certificate/hsm-local/{name}    - Delete HSM local certificate

Note: This endpoint supports full CRUD operations for HSM certificates.
HSM certificates require HSM hardware or cloud HSM service (e.g., Google Cloud HSM).
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

from .....exceptions import APIError, ResourceNotFoundError

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class HsmLocal:
    """Certificate HSM-Local endpoint (full CRUD)"""

    def __init__(self, client: "HTTPClient") -> None:
        """
        Initialize HsmLocal endpoint

        Args:
            client: HTTPClient instance
        """
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all HSM local certificates

        Args:
            vdom (str/bool, optional): Virtual domain, False to skip
            **kwargs: Additional query parameters (filter, format, count, search, etc.)

        Returns:
            dict: API response with list of HSM local certificates

        Examples:
            >>> # List all HSM local certificates
            >>> result = fgt.cmdb.certificate.hsm_local.list()

            >>> # List with filter
            >>> result = fgt.cmdb.certificate.hsm_local.list(filter='vendor==google')
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
        Get HSM local certificate(s)

        Args:
            name (str, optional): HSM local certificate name (for specific certificate)
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
            >>> # Get specific HSM local certificate
            >>> result = fgt.cmdb.certificate.hsm_local.get('my-hsm-cert')

            >>> # Get all HSM local certificates
            >>> result = fgt.cmdb.certificate.hsm_local.get()

            >>> # Get schema
            >>> result = fgt.cmdb.certificate.hsm_local.get(action='schema')
        """
        # Build path
        path = f"certificate/hsm-local/{name}" if name else "certificate/hsm-local"

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
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Create new HSM local certificate

        Args:
            data (dict): Certificate data including:
                - name (str, required): Certificate name
                - vendor (str): HSM vendor (google, aws, azure, etc.)
                - certificate (str): Certificate content
                - comments (str): Comments
                - gch-* fields: Google Cloud HSM specific fields
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Example:
            >>> data = {
            ...     'name': 'my-hsm-cert',
            ...     'vendor': 'google',
            ...     'gch-project': 'my-project',
            ...     'gch-location': 'us-east1',
            ...     'gch-keyring': 'my-keyring',
            ...     'gch-cryptokey': 'my-key'
            ... }
            >>> result = fgt.cmdb.certificate.hsm_local.create(data)
        """
        return self._client.post(
            "cmdb", "certificate/hsm-local", data=data, vdom=vdom, raw_json=raw_json
        )

    def update(
        self,
        name: str,
        data: dict[str, Any],
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Update existing HSM local certificate

        Args:
            name (str): Certificate name to update
            data (dict): Updated certificate data
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Example:
            >>> data = {'comments': 'Updated HSM certificate'}
            >>> result = fgt.cmdb.certificate.hsm_local.update('my-hsm-cert', data)
        """
        return self._client.put(
            "cmdb", f"certificate/hsm-local/{name}", data=data, vdom=vdom, raw_json=raw_json
        )

    def delete(
        self,
        name: str,
        vdom: Optional[Union[str, bool]] = None,
        raw_json: bool = False,
    ) -> dict[str, Any]:
        """
        Delete HSM local certificate

        Args:
            name (str): Certificate name to delete
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            dict: API response

        Example:
            >>> result = fgt.cmdb.certificate.hsm_local.delete('my-hsm-cert')
        """
        return self._client.delete(
            "cmdb", f"certificate/hsm-local/{name}", vdom=vdom, raw_json=raw_json
        )

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if HSM local certificate exists

        Args:
            name (str): Certificate name
            vdom (str/bool, optional): Virtual domain, False to skip

        Returns:
            bool: True if exists, False otherwise

        Example:
            >>> if fgt.cmdb.certificate.hsm_local.exists('my-hsm-cert'):
            ...     print('HSM certificate exists')
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except (APIError, ResourceNotFoundError):
            return False
