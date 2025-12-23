"""
FortiOS CMDB - Cmdb Vpn Certificate Ca

Configuration endpoint for managing cmdb vpn certificate ca objects.

API Endpoints:
    GET    /cmdb/vpn/certificate_ca
    POST   /cmdb/vpn/certificate_ca
    GET    /cmdb/vpn/certificate_ca

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn.certificate_ca.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.vpn.certificate_ca.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.vpn.certificate_ca.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.vpn.certificate_ca.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.vpn.certificate_ca.delete(name="item_name")

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


class CertificateCa:
    """
    Certificateca Operations.

    Provides CRUD operations for FortiOS certificateca configuration.

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
        Initialize CertificateCa endpoint.

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
            endpoint = f"/vpn.certificate/ca/{name}"
        else:
            endpoint = "/vpn.certificate/ca"
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
        ca: str | None = None,
        range: str | None = None,
        source: str | None = None,
        ssl_inspection_trusted: str | None = None,
        scep_url: str | None = None,
        est_url: str | None = None,
        auto_update_days: int | None = None,
        auto_update_days_warning: int | None = None,
        source_ip: str | None = None,
        ca_identifier: str | None = None,
        obsolete: str | None = None,
        fabric_ca: str | None = None,
        details: str | None = None,
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
            ca: CA certificate as a PEM file. (optional)
            range: Either global or VDOM IP address range for the CA
            certificate. (optional)
            source: CA certificate source type. (optional)
            ssl_inspection_trusted: Enable/disable this CA as a trusted CA for
            SSL inspection. (optional)
            scep_url: URL of the SCEP server. (optional)
            est_url: URL of the EST server. (optional)
            auto_update_days: Number of days to wait before requesting an
            updated CA certificate (0 - 4294967295, 0 = disabled). (optional)
            auto_update_days_warning: Number of days before an expiry-warning
            message is generated (0 - 4294967295, 0 = disabled). (optional)
            source_ip: Source IP address for communications to the SCEP server.
            (optional)
            ca_identifier: CA identifier of the SCEP server. (optional)
            obsolete: Enable/disable this CA as obsoleted. (optional)
            fabric_ca: Enable/disable synchronization of CA across Security
            Fabric. (optional)
            details: Print CA certificate detailed information. (optional)
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
        endpoint = "/vpn.certificate/ca"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if ca is not None:
            data_payload["ca"] = ca
        if range is not None:
            data_payload["range"] = range
        if source is not None:
            data_payload["source"] = source
        if ssl_inspection_trusted is not None:
            data_payload["ssl-inspection-trusted"] = ssl_inspection_trusted
        if scep_url is not None:
            data_payload["scep-url"] = scep_url
        if est_url is not None:
            data_payload["est-url"] = est_url
        if auto_update_days is not None:
            data_payload["auto-update-days"] = auto_update_days
        if auto_update_days_warning is not None:
            data_payload["auto-update-days-warning"] = auto_update_days_warning
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if ca_identifier is not None:
            data_payload["ca-identifier"] = ca_identifier
        if obsolete is not None:
            data_payload["obsolete"] = obsolete
        if fabric_ca is not None:
            data_payload["fabric-ca"] = fabric_ca
        if details is not None:
            data_payload["details"] = details
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
