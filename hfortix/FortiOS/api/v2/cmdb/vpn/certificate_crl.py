"""
FortiOS CMDB - Cmdb Vpn Certificate Crl

Configuration endpoint for managing cmdb vpn certificate crl objects.

API Endpoints:
    GET    /cmdb/vpn/certificate_crl
    POST   /cmdb/vpn/certificate_crl
    GET    /cmdb/vpn/certificate_crl

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn.certificate_crl.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.vpn.certificate_crl.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.vpn.certificate_crl.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.vpn.certificate_crl.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.vpn.certificate_crl.delete(name="item_name")

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


class CertificateCrl:
    """
    Certificatecrl Operations.

    Provides CRUD operations for FortiOS certificatecrl configuration.

    Methods:
        get(): Retrieve configuration objects
        post(): Create new configuration objects

    Important:
        - POST creates new objects (404 if name already exists)
        - PUT updates existing objects (404 if name doesn't exist)
        - GET retrieves objects without making changes
        - DELETE removes objects (404 if name doesn't exist)
    """

    def __init__(self, client: "IHTTPClient"):
        """
        Initialize CertificateCrl endpoint.

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
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Select a specific entry from a CLI table.

        Args:
            name: Object identifier (optional for list, required for specific)
            attr: Attribute name that references other table (optional)
            skip_to_datasource: Skip to provided table's Nth entry. E.g
            {datasource: 'firewall.address', pos: 10, global_entry: false}
            (optional)
            acs: If true, returned result are in ascending order. (optional)
            search: If present, the objects will be filtered by the search
            value. (optional)
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

        # Build endpoint path
        if name:
            endpoint = f"/vpn.certificate/crl/{name}"
        else:
            endpoint = "/vpn.certificate/crl"
        if attr is not None:
            params["attr"] = attr
        if skip_to_datasource is not None:
            params["skip_to_datasource"] = skip_to_datasource
        if acs is not None:
            params["acs"] = acs
        if search is not None:
            params["search"] = search
        params.update(kwargs)
        return self._client.get(
            "cmdb", endpoint, params=params, vdom=vdom, raw_json=raw_json
        )

    def post(
        self,
        payload_dict: dict[str, Any] | None = None,
        nkey: str | None = None,
        name: str | None = None,
        crl: str | None = None,
        range: str | None = None,
        source: str | None = None,
        update_vdom: str | None = None,
        ldap_server: str | None = None,
        ldap_username: str | None = None,
        ldap_password: str | None = None,
        http_url: str | None = None,
        scep_url: str | None = None,
        scep_cert: str | None = None,
        update_interval: int | None = None,
        source_ip: str | None = None,
        vdom: str | bool | None = None,
        raw_json: bool = False,
        **kwargs: Any,
    ) -> Union[dict[str, Any], Coroutine[Any, Any, dict[str, Any]]]:
        """
        Create object(s) in this table.

        Args:
            payload_dict: Optional dictionary of all parameters (can be passed
            as first positional arg)
            nkey: If *action=clone*, use *nkey* to specify the ID for the new
            resource to be created. (optional)
            name: Name. (optional)
            crl: Certificate Revocation List as a PEM file. (optional)
            range: Either global or VDOM IP address range for the certificate.
            (optional)
            source: Certificate source type. (optional)
            update_vdom: VDOM for CRL update. (optional)
            ldap_server: LDAP server name for CRL auto-update. (optional)
            ldap_username: LDAP server user name. (optional)
            ldap_password: LDAP server user password. (optional)
            http_url: HTTP server URL for CRL auto-update. (optional)
            scep_url: SCEP server URL for CRL auto-update. (optional)
            scep_cert: Local certificate for SCEP communication for CRL
            auto-update. (optional)
            update_interval: Time in seconds before the FortiGate checks for an
            updated CRL. Set to 0 to update only when it expires. (optional)
            source_ip: Source IP address for communications to a HTTP or SCEP
            CA server. (optional)
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
        endpoint = "/vpn.certificate/crl"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if crl is not None:
            data_payload["crl"] = crl
        if range is not None:
            data_payload["range"] = range
        if source is not None:
            data_payload["source"] = source
        if update_vdom is not None:
            data_payload["update-vdom"] = update_vdom
        if ldap_server is not None:
            data_payload["ldap-server"] = ldap_server
        if ldap_username is not None:
            data_payload["ldap-username"] = ldap_username
        if ldap_password is not None:
            data_payload["ldap-password"] = ldap_password
        if http_url is not None:
            data_payload["http-url"] = http_url
        if scep_url is not None:
            data_payload["scep-url"] = scep_url
        if scep_cert is not None:
            data_payload["scep-cert"] = scep_cert
        if update_interval is not None:
            data_payload["update-interval"] = update_interval
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
