"""
FortiOS CMDB - System SshConfig

API Endpoints:
    GET    /system/ssh-config
    PUT    /system/ssh-config
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ....http_client import HTTPClient


class SshConfig:
    """SshConfig operations."""

    def __init__(self, client: 'HTTPClient'):
        """
        Initialize SshConfig endpoint.

        Args:
            client: HTTPClient instance for API communication
        """
        self._client = client

    def get(
        self,
        payload_dict: dict[str, Any] | None = None,
        exclude_default_values: bool | None = None,
        stat_items: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Select all entries in a CLI table.
        
        Args:
            exclude_default_values: Exclude properties/objects with default value (optional)
            stat_items: Items to count occurrence in entire response (multiple items should be separated by '|'). (optional)
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
        endpoint = "/system/ssh-config"
        if exclude_default_values is not None:
            params['exclude-default-values'] = exclude_default_values
        if stat_items is not None:
            params['stat-items'] = stat_items
        params.update(kwargs)
        return self._client.get("cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json)

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        ssh_kex_algo: str | None = None,
        ssh_enc_algo: str | None = None,
        ssh_mac_algo: str | None = None,
        ssh_hsk_algo: str | None = None,
        ssh_hsk_override: str | None = None,
        ssh_hsk_password: str | None = None,
        ssh_hsk: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Update this specific resource.
        
        Args:
            payload_dict: Optional dictionary of all parameters (can be passed as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the resource that this resource will be moved after. (optional)
            ssh_kex_algo: Select one or more SSH kex algorithms. (optional)
            ssh_enc_algo: Select one or more SSH ciphers. (optional)
            ssh_mac_algo: Select one or more SSH MAC algorithms. (optional)
            ssh_hsk_algo: Select one or more SSH hostkey algorithms. (optional)
            ssh_hsk_override: Enable/disable SSH host key override in SSH daemon. (optional)
            ssh_hsk_password: Password for ssh-hostkey. (optional)
            ssh_hsk: Config SSH host key. (optional)
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
        endpoint = "/system/ssh-config"
        if before is not None:
            data_payload['before'] = before
        if after is not None:
            data_payload['after'] = after
        if ssh_kex_algo is not None:
            data_payload['ssh-kex-algo'] = ssh_kex_algo
        if ssh_enc_algo is not None:
            data_payload['ssh-enc-algo'] = ssh_enc_algo
        if ssh_mac_algo is not None:
            data_payload['ssh-mac-algo'] = ssh_mac_algo
        if ssh_hsk_algo is not None:
            data_payload['ssh-hsk-algo'] = ssh_hsk_algo
        if ssh_hsk_override is not None:
            data_payload['ssh-hsk-override'] = ssh_hsk_override
        if ssh_hsk_password is not None:
            data_payload['ssh-hsk-password'] = ssh_hsk_password
        if ssh_hsk is not None:
            data_payload['ssh-hsk'] = ssh_hsk
        data_payload.update(kwargs)
        return self._client.put("cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json)
