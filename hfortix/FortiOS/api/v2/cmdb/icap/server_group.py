"""
FortiOS CMDB - ICAP Server Group

Configure ICAP server groups consisting of multiple forward servers with failover and load balancing.

API Endpoints:
    GET    /api/v2/cmdb/icap/server-group        - List all ICAP server groups
    GET    /api/v2/cmdb/icap/server-group/{name} - Get specific ICAP server group
    POST   /api/v2/cmdb/icap/server-group        - Create ICAP server group
    PUT    /api/v2/cmdb/icap/server-group/{name} - Update ICAP server group
    DELETE /api/v2/cmdb/icap/server-group/{name} - Delete ICAP server group
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Union

if TYPE_CHECKING:
    from ...http_client import HTTPClient

from hfortix.FortiOS.http_client import encode_path_component


class ServerGroup:
    """ICAP Server Group endpoint"""

    def __init__(self, client: "HTTPClient") -> None:
        self._client = client

    def list(self, vdom: Optional[Union[str, bool]] = None, **kwargs: Any) -> dict[str, Any]:
        """
        List all ICAP server groups.

        Args:
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing list of ICAP server groups

        Examples:
            >>> # List all server groups
            >>> groups = fgt.api.cmdb.icap.server_group.list()
            >>> for group in groups['results']:
            ...     print(group['name'], group['ldb-method'])
        """
        path = "icap/server-group"
        return self._client.get("cmdb", path, params=kwargs if kwargs else None, vdom=vdom)

    def get(
        self,
        name: str,
        datasource: Optional[bool] = None,
        with_meta: Optional[bool] = None,
        skip: Optional[bool] = None,
        action: Optional[str] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Get specific ICAP server group.

        Args:
            name: Server group name
            datasource: Include datasource information
            with_meta: Include metadata
            skip: Skip hidden properties
            action: Additional action to perform
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing server group configuration

        Examples:
            >>> # Get specific server group
            >>> group = fgt.api.cmdb.icap.server_group.get('icap-group1')
            >>> print(group['ldb-method'], group['server-list'])
        """
        params = {}
        param_map = {
            "datasource": datasource,
            "with-meta": with_meta,
            "skip": skip,
            "action": action,
        }
        for key, value in param_map.items():
            if value is not None:
                params[key] = value
        params.update(kwargs)

        path = f"icap/server-group/{encode_path_component(name)}"
        return self._client.get("cmdb", path, params=params if params else None, vdom=vdom)

    def create(
        self,
        data_dict: Optional[dict[str, Any]] = None,
        name: Optional[str] = None,
        ldb_method: Optional[str] = None,
        server_list: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create ICAP server group.

        Supports three usage patterns:

        1. Dictionary pattern (template-based):
           >>> config = {
           ...     'name': 'icap-group1',
           ...     'ldb-method': 'weighted',
           ...     'server-list': [{'name': 'icap-server1'}]
           ... }
           >>> fgt.api.cmdb.icap.server_group.create(data_dict=config)

        2. Keyword pattern (explicit parameters):
           >>> fgt.api.cmdb.icap.server_group.create(
           ...     name='icap-group1',
           ...     ldb_method='weighted',
           ...     server_list=[{'name': 'icap-server1'}]
           ... )

        3. Mixed pattern (template + overrides):
           >>> base = {'ldb-method': 'weighted'}
           >>> fgt.api.cmdb.icap.server_group.create(data_dict=base, name='icap-group1')

        Args:
            data_dict: Complete configuration dictionary (pattern 1 & 3)
            name: Server group name
            ldb_method: Load balancing method (weighted, least-session, active-passive)
            server_list: List of ICAP servers in group [{'name': 'server1'}, ...]
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing creation result

        Examples:
            >>> # Create with dictionary
            >>> config = {
            ...     'name': 'icap-group1',
            ...     'ldb-method': 'weighted',
            ...     'server-list': [
            ...         {'name': 'icap-server1'},
            ...         {'name': 'icap-server2'}
            ...     ]
            ... }
            >>> result = fgt.api.cmdb.icap.server_group.create(data_dict=config)

            >>> # Create with keywords
            >>> result = fgt.api.cmdb.icap.server_group.create(
            ...     name='icap-group2',
            ...     ldb_method='least-session',
            ...     server_list=[{'name': 'icap-server1'}]
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "name": name,
            "ldb_method": ldb_method,
            "server_list": server_list,
        }

        api_field_map = {
            "name": "name",
            "ldb_method": "ldb-method",
            "server_list": "server-list",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = "icap/server-group"
        return self._client.post("cmdb", path, data=data, vdom=vdom)

    def update(
        self,
        name: str,
        data_dict: Optional[dict[str, Any]] = None,
        ldb_method: Optional[str] = None,
        server_list: Optional[list[dict[str, Any]]] = None,
        vdom: Optional[Union[str, bool]] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update ICAP server group.

        Supports three usage patterns:

        1. Dictionary pattern (template-based):
           >>> config = {'ldb-method': 'least-session'}
           >>> fgt.api.cmdb.icap.server_group.update('icap-group1', data_dict=config)

        2. Keyword pattern (explicit parameters):
           >>> fgt.api.cmdb.icap.server_group.update(
           ...     'icap-group1',
           ...     ldb_method='active-passive'
           ... )

        3. Mixed pattern (template + overrides):
           >>> base = {'ldb-method': 'weighted'}
           >>> fgt.api.cmdb.icap.server_group.update('icap-group1', data_dict=base)

        Args:
            name: Server group name
            data_dict: Complete configuration dictionary (pattern 1 & 3)
            ldb_method: Load balancing method (weighted, least-session, active-passive)
            server_list: List of ICAP servers in group [{'name': 'server1'}, ...]
            vdom: Virtual domain name or False for global
            **kwargs: Additional parameters

        Returns:
            Dictionary containing update result

        Examples:
            >>> # Update with dictionary
            >>> config = {
            ...     'ldb-method': 'least-session',
            ...     'server-list': [
            ...         {'name': 'icap-server1'},
            ...         {'name': 'icap-server2'},
            ...         {'name': 'icap-server3'}
            ...     ]
            ... }
            >>> result = fgt.api.cmdb.icap.server_group.update('icap-group1', data_dict=config)

            >>> # Update with keywords
            >>> result = fgt.api.cmdb.icap.server_group.update(
            ...     'icap-group1',
            ...     ldb_method='weighted'
            ... )
        """
        data = data_dict.copy() if data_dict else {}

        param_map = {
            "ldb_method": ldb_method,
            "server_list": server_list,
        }

        api_field_map = {
            "ldb_method": "ldb-method",
            "server_list": "server-list",
        }

        for python_key, value in param_map.items():
            if value is not None:
                api_key = api_field_map[python_key]
                data[api_key] = value

        data.update(kwargs)

        path = f"icap/server-group/{encode_path_component(name)}"
        return self._client.put("cmdb", path, data=data, vdom=vdom)

    def delete(self, name: str, vdom: Optional[Union[str, bool]] = None) -> dict[str, Any]:
        """
        Delete ICAP server group.

        Args:
            name: Server group name
            vdom: Virtual domain name or False for global

        Returns:
            Dictionary containing deletion result

        Examples:
            >>> # Delete server group
            >>> result = fgt.api.cmdb.icap.server_group.delete('old-group')
            >>> print(result['status'])
        """
        path = f"icap/server-group/{encode_path_component(name)}"
        return self._client.delete("cmdb", path, vdom=vdom)

    def exists(self, name: str, vdom: Optional[Union[str, bool]] = None) -> bool:
        """
        Check if ICAP server group exists.

        Args:
            name: Server group name
            vdom: Virtual domain name or False for global

        Returns:
            True if server group exists, False otherwise

        Examples:
            >>> # Check if server group exists
            >>> if fgt.api.cmdb.icap.server_group.exists('icap-group1'):
            ...     print("Server group exists")
        """
        try:
            self.get(name, vdom=vdom)
            return True
        except Exception:
            return False
