"""
FortiOS CMDB - Cmdb Firewall Ssh Setting

Configuration endpoint for managing cmdb firewall ssh setting objects.

API Endpoints:
    GET    /cmdb/firewall/ssh_setting
    PUT    /cmdb/firewall/ssh_setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.firewall.ssh_setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.firewall.ssh_setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.firewall.ssh_setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.firewall.ssh_setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.firewall.ssh_setting.delete(name="item_name")

Important:
    - Use **POST** to create new objects (404 error if already exists)
    - Use **PUT** to update existing objects (404 error if doesn't exist)
    - Use **GET** to retrieve configuration (no changes made)
    - Use **DELETE** to remove objects (404 error if doesn't exist)
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    from collections.abc import Coroutine

    from hfortix.FortiOS.http_client_interface import IHTTPClient


class SshSetting:
    """
    Sshsetting Operations.

    Provides CRUD operations for FortiOS sshsetting configuration.

    Methods:
        get(): Retrieve configuration objects
        put(): Update existing configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize SshSetting endpoint.

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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select all entries in a CLI table.

        Args:
            exclude_default_values: Exclude properties/objects with default
            value (optional)
            stat_items: Items to count occurrence in entire response (multiple
            items should be separated by '|'). (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        params = payload_dict.copy() if payload_dict else {}
        endpoint = "/firewall.ssh/setting"
        if exclude_default_values is not None:
            params["exclude-default-values"] = exclude_default_values
        if stat_items is not None:
            params["stat-items"] = stat_items
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def put(
        self,
        payload_dict: dict[str, Any] | None = None,
        before: str | None = None,
        after: str | None = None,
        caname: str | None = None,
        untrusted_caname: str | None = None,
        hostkey_rsa2048: str | None = None,
        hostkey_dsa1024: str | None = None,
        hostkey_ecdsa256: str | None = None,
        hostkey_ecdsa384: str | None = None,
        hostkey_ecdsa521: str | None = None,
        hostkey_ed25519: str | None = None,
        host_trusted_checking: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Update this specific resource.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            before: If *action=move*, use *before* to specify the ID of the
            resource that this resource will be moved before. (optional)
            after: If *action=move*, use *after* to specify the ID of the
            resource that this resource will be moved after. (optional)
            caname: CA certificate used by SSH Inspection. (optional)
            untrusted_caname: Untrusted CA certificate used by SSH Inspection.
            (optional)
            hostkey_rsa2048: RSA certificate used by SSH proxy. (optional)
            hostkey_dsa1024: DSA certificate used by SSH proxy. (optional)
            hostkey_ecdsa256: ECDSA nid256 certificate used by SSH proxy.
            (optional)
            hostkey_ecdsa384: ECDSA nid384 certificate used by SSH proxy.
            (optional)
            hostkey_ecdsa521: ECDSA nid384 certificate used by SSH proxy.
            (optional)
            hostkey_ed25519: ED25519 hostkey used by SSH proxy. (optional)
            host_trusted_checking: Enable/disable host trusted checking.
            (optional)
            vdom: Virtual domain name, or False to skip. Handled by HTTPClient.
            raw_json: If True, return full API response with metadata. If
            False, return only results.
            **kwargs: Additional query parameters (filter, sort, start, count,
            format, etc.)

        Common Query Parameters (via **kwargs):
            filter: Filter results (e.g., filter='name==value')
            sort: Sort results (e.g., sort='name,asc')
            start: Starting entry index for paging
            count: Maximum number of entries to return
            format: Fields to return (e.g., format='name|type')
            See FortiOS REST API documentation for full list of query
            parameters

        Returns:
            Dictionary containing API response
        """
        data_payload = payload_dict.copy() if payload_dict else {}
        endpoint = "/firewall.ssh/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if caname is not None:
            data_payload["caname"] = caname
        if untrusted_caname is not None:
            data_payload["untrusted-caname"] = untrusted_caname
        if hostkey_rsa2048 is not None:
            data_payload["hostkey-rsa2048"] = hostkey_rsa2048
        if hostkey_dsa1024 is not None:
            data_payload["hostkey-dsa1024"] = hostkey_dsa1024
        if hostkey_ecdsa256 is not None:
            data_payload["hostkey-ecdsa256"] = hostkey_ecdsa256
        if hostkey_ecdsa384 is not None:
            data_payload["hostkey-ecdsa384"] = hostkey_ecdsa384
        if hostkey_ecdsa521 is not None:
            data_payload["hostkey-ecdsa521"] = hostkey_ecdsa521
        if hostkey_ed25519 is not None:
            data_payload["hostkey-ed25519"] = hostkey_ed25519
        if host_trusted_checking is not None:
            data_payload["host-trusted-checking"] = host_trusted_checking
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
