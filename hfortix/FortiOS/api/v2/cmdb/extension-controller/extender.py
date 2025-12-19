"""
FortiOS CMDB - Extension-controller Extender

API Endpoints:
    GET    /extension-controller/extender
    POST   /extension-controller/extender
    GET    /extension-controller/extender/{name}
    PUT    /extension-controller/extender/{name}
    DELETE /extension-controller/extender/{name}
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class Extender:
    """Extender operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize Extender endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        attr: str | None = None,
        skip_to_datasource: dict | None = None,
        acs: int | None = None,
        search: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select a specific entry from a CLI table.
        
        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g {datasource: 'firewall.address', pos: 10, global_entry: false} (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search value. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if name:
            endpoint = f"/extension-controller/extender/{name}"
        else:
            endpoint = "/extension-controller/extender"
        if attr is not None:
            params['attr'] = attr
        if skip_to_datasource is not None:
            params['skip_to_datasource'] = skip_to_datasource
        if acs is not None:
            params['acs'] = acs
        if search is not None:
            params['search'] = search
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        id: str | None = None,
        authorized: str | None = None,
        ext_name: str | None = None,
        description: str | None = None,
        device_id: int | None = None,
        extension_type: str | None = None,
        profile: str | None = None,
        override_allowaccess: str | None = None,
        allowaccess: str | None = None,
        override_login_password_change: str | None = None,
        login_password_change: str | None = None,
        login_password: str | None = None,
        override_enforce_bandwidth: str | None = None,
        enforce_bandwidth: str | None = None,
        bandwidth_limit: int | None = None,
        wan_extension: list | None = None,
        firmware_provision_latest: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            name: Object identifier (required)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            name: FortiExtender entry name. (optional)
            id: FortiExtender serial number. (optional)
            authorized: FortiExtender Administration (enable or disable). (optional)
            ext_name: FortiExtender name. (optional)
            description: Description. (optional)
            device_id: Device ID. (optional)
            extension_type: Extension type for this FortiExtender. (optional)
            profile: FortiExtender profile configuration. (optional)
            override_allowaccess: Enable to override the extender profile management access configuration. (optional)
            allowaccess: Control management access to the managed extender. Separate entries with a space. (optional)
            override_login_password_change: Enable to override the extender profile login-password (administrator password) setting. (optional)
            login_password_change: Change or reset the administrator password of a managed extender (yes, default, or no, default = no). (optional)
            login_password: Set the managed extender's administrator password. (optional)
            override_enforce_bandwidth: Enable to override the extender profile enforce-bandwidth setting. (optional)
            enforce_bandwidth: Enable/disable enforcement of bandwidth on LAN extension interface. (optional)
            bandwidth_limit: FortiExtender LAN extension bandwidth limit (Mbps). (optional)
            wan_extension: FortiExtender wan extension configuration. (optional)
            firmware_provision_latest: Enable/disable one-time automatic provisioning of the latest firmware version. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for put()")
        endpoint = f"/extension-controller/extender/{name}"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if name is not None:
            data_payload['name'] = name
        if id is not None:
            data_payload['id'] = id
        if authorized is not None:
            data_payload['authorized'] = authorized
        if ext_name is not None:
            data_payload['ext-name'] = ext_name
        if description is not None:
            data_payload['description'] = description
        if device_id is not None:
            data_payload['device-id'] = device_id
        if extension_type is not None:
            data_payload['extension-type'] = extension_type
        if profile is not None:
            data_payload['profile'] = profile
        if override_allowaccess is not None:
            data_payload['override-allowaccess'] = override_allowaccess
        if allowaccess is not None:
            data_payload['allowaccess'] = allowaccess
        if override_login_password_change is not None:
            data_payload['override-login-password-change'] = override_login_password_change
        if login_password_change is not None:
            data_payload['login-password-change'] = login_password_change
        if login_password is not None:
            data_payload['login-password'] = login_password
        if override_enforce_bandwidth is not None:
            data_payload['override-enforce-bandwidth'] = override_enforce_bandwidth
        if enforce_bandwidth is not None:
            data_payload['enforce-bandwidth'] = enforce_bandwidth
        if bandwidth_limit is not None:
            data_payload['bandwidth-limit'] = bandwidth_limit
        if wan_extension is not None:
            data_payload['wan-extension'] = wan_extension
        if firmware_provision_latest is not None:
            data_payload['firmware-provision-latest'] = firmware_provision_latest
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)

    def delete(
        self,
        name: str | None = None,
        payload_dict: dict[str, Any] | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Delete this specific resource.
        
        Args:
            name: Object identifier (required)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        
        # Build endpoint path
        if not name:
            raise ValueError("name is required for delete()")
        endpoint = f"/extension-controller/extender/{name}"
        params.update(kwargs)
        return self._client.delete("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        id: str | None = None,
        authorized: str | None = None,
        ext_name: str | None = None,
        description: str | None = None,
        device_id: int | None = None,
        extension_type: str | None = None,
        profile: str | None = None,
        override_allowaccess: str | None = None,
        allowaccess: str | None = None,
        override_login_password_change: str | None = None,
        login_password_change: str | None = None,
        login_password: str | None = None,
        override_enforce_bandwidth: str | None = None,
        enforce_bandwidth: str | None = None,
        bandwidth_limit: int | None = None,
        wan_extension: list | None = None,
        firmware_provision_latest: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Create object(s) in this table.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new resource to be created. (optional)
            name: FortiExtender entry name. (optional)
            id: FortiExtender serial number. (optional)
            authorized: FortiExtender Administration (enable or disable). (optional)
            ext_name: FortiExtender name. (optional)
            description: Description. (optional)
            device_id: Device ID. (optional)
            extension_type: Extension type for this FortiExtender. (optional)
            profile: FortiExtender profile configuration. (optional)
            override_allowaccess: Enable to override the extender profile management access configuration. (optional)
            allowaccess: Control management access to the managed extender. Separate entries with a space. (optional)
            override_login_password_change: Enable to override the extender profile login-password (administrator password) setting. (optional)
            login_password_change: Change or reset the administrator password of a managed extender (yes, default, or no, default = no). (optional)
            login_password: Set the managed extender's administrator password. (optional)
            override_enforce_bandwidth: Enable to override the extender profile enforce-bandwidth setting. (optional)
            enforce_bandwidth: Enable/disable enforcement of bandwidth on LAN extension interface. (optional)
            bandwidth_limit: FortiExtender LAN extension bandwidth limit (Mbps). (optional)
            wan_extension: FortiExtender wan extension configuration. (optional)
            firmware_provision_latest: Enable/disable one-time automatic provisioning of the latest firmware version. (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count, format, etc.)
        
        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query parameters
        
        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        params = {}
        endpoint = "/extension-controller/extender"
        if nkey is not None:
            data_payload['nkey'] = nkey
        if name is not None:
            data_payload['name'] = name
        if id is not None:
            data_payload['id'] = id
        if authorized is not None:
            data_payload['authorized'] = authorized
        if ext_name is not None:
            data_payload['ext-name'] = ext_name
        if description is not None:
            data_payload['description'] = description
        if device_id is not None:
            data_payload['device-id'] = device_id
        if extension_type is not None:
            data_payload['extension-type'] = extension_type
        if profile is not None:
            data_payload['profile'] = profile
        if override_allowaccess is not None:
            data_payload['override-allowaccess'] = override_allowaccess
        if allowaccess is not None:
            data_payload['allowaccess'] = allowaccess
        if override_login_password_change is not None:
            data_payload['override-login-password-change'] = override_login_password_change
        if login_password_change is not None:
            data_payload['login-password-change'] = login_password_change
        if login_password is not None:
            data_payload['login-password'] = login_password
        if override_enforce_bandwidth is not None:
            data_payload['override-enforce-bandwidth'] = override_enforce_bandwidth
        if enforce_bandwidth is not None:
            data_payload['enforce-bandwidth'] = enforce_bandwidth
        if bandwidth_limit is not None:
            data_payload['bandwidth-limit'] = bandwidth_limit
        if wan_extension is not None:
            data_payload['wan-extension'] = wan_extension
        if firmware_provision_latest is not None:
            data_payload['firmware-provision-latest'] = firmware_provision_latest
        data_payload.update(kwargs)
        return self._client.post("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
