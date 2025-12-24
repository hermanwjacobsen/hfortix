"""
FortiOS CMDB - Cmdb Vpn Certificate Local

Configuration endpoint for managing cmdb vpn certificate local objects.

API Endpoints:
    GET    /cmdb/vpn/certificate_local
    POST   /cmdb/vpn/certificate_local
    GET    /cmdb/vpn/certificate_local

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn.certificate_local.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.vpn.certificate_local.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.vpn.certificate_local.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.vpn.certificate_local.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.vpn.certificate_local.delete(name="item_name")

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


class CertificateLocal:
    """
    Certificatelocal Operations.

    Provides CRUD operations for FortiOS certificatelocal configuration.

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
        Initialize CertificateLocal endpoint.

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
            endpoint = f"/vpn.certificate/local/{name}"
        else:
            endpoint = "/vpn.certificate/local"
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
        password: str | None = None,
        comments: str | None = None,
        private_key: str | None = None,
        certificate: str | None = None,
        csr: str | None = None,
        state: str | None = None,
        scep_url: str | None = None,
        range: str | None = None,
        source: str | None = None,
        auto_regenerate_days: int | None = None,
        auto_regenerate_days_warning: int | None = None,
        scep_password: str | None = None,
        ca_identifier: str | None = None,
        name_encoding: str | None = None,
        source_ip: str | None = None,
        ike_localid: str | None = None,
        ike_localid_type: str | None = None,
        enroll_protocol: str | None = None,
        private_key_retain: str | None = None,
        cmp_server: str | None = None,
        cmp_path: str | None = None,
        cmp_server_cert: str | None = None,
        cmp_regeneration_method: str | None = None,
        acme_ca_url: str | None = None,
        acme_domain: str | None = None,
        acme_email: str | None = None,
        acme_eab_key_id: str | None = None,
        acme_eab_key_hmac: str | None = None,
        acme_rsa_key_size: int | None = None,
        acme_renew_window: int | None = None,
        est_server: str | None = None,
        est_ca_id: str | None = None,
        est_http_username: str | None = None,
        est_http_password: str | None = None,
        est_client_cert: str | None = None,
        est_server_cert: str | None = None,
        est_srp_username: str | None = None,
        est_srp_password: str | None = None,
        est_regeneration_method: str | None = None,
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
            password: Password as a PEM file. (optional)
            comments: Comment. (optional)
            private_key: PEM format key encrypted with a password. (optional)
            certificate: PEM format certificate. (optional)
            csr: Certificate Signing Request. (optional)
            state: Certificate Signing Request State. (optional)
            scep_url: SCEP server URL. (optional)
            range: Either a global or VDOM IP address range for the
            certificate. (optional)
            source: Certificate source type. (optional)
            auto_regenerate_days: Number of days to wait before expiry of an
            updated local certificate is requested (0 = disabled). (optional)
            auto_regenerate_days_warning: Number of days to wait before an
            expiry warning message is generated (0 = disabled). (optional)
            scep_password: SCEP server challenge password for
            auto-regeneration. (optional)
            ca_identifier: CA identifier of the CA server for signing via SCEP.
            (optional)
            name_encoding: Name encoding method for auto-regeneration.
            (optional)
            source_ip: Source IP address for communications to the SCEP server.
            (optional)
            ike_localid: Local ID the FortiGate uses for authentication as a
            VPN client. (optional)
            ike_localid_type: IKE local ID type. (optional)
            enroll_protocol: Certificate enrollment protocol. (optional)
            private_key_retain: Enable/disable retention of private key during
            SCEP renewal (default = disable). (optional)
            cmp_server: Address and port for CMP server (format =
            address:port). (optional)
            cmp_path: Path location inside CMP server. (optional)
            cmp_server_cert: CMP server certificate. (optional)
            cmp_regeneration_method: CMP auto-regeneration method. (optional)
            acme_ca_url: The URL for the ACME CA server (Let's Encrypt is the
            default provider). (optional)
            acme_domain: A valid domain that resolves to this FortiGate unit.
            (optional)
            acme_email: Contact email address that is required by some CAs like
            LetsEncrypt. (optional)
            acme_eab_key_id: External Account Binding Key ID (optional
            setting). (optional)
            acme_eab_key_hmac: External Account Binding HMAC Key (URL-encoded
            base64). (optional)
            acme_rsa_key_size: Length of the RSA private key of the generated
            cert (Minimum 2048 bits). (optional)
            acme_renew_window: Beginning of the renewal window (in days before
            certificate expiration, 30 by default). (optional)
            est_server: Address and port for EST server (e.g. https://example.com:1234). (optional)
            est_ca_id: CA identifier of the CA server for signing via EST.
            (optional)
            est_http_username: HTTP Authentication username for signing via
            EST. (optional)
            est_http_password: HTTP Authentication password for signing via
            EST. (optional)
            est_client_cert: Certificate used to authenticate this FortiGate to
            EST server. (optional)
            est_server_cert: EST server's certificate must be verifiable by
            this certificate to be authenticated. (optional)
            est_srp_username: EST SRP authentication username. (optional)
            est_srp_password: EST SRP authentication password. (optional)
            est_regeneration_method: EST behavioral options during
            re-enrollment. (optional)
            details: Print local certificate detailed information. (optional)
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
        endpoint = "/vpn.certificate/local"
        if nkey is not None:
            data_payload["nkey"] = nkey
        if name is not None:
            data_payload["name"] = name
        if password is not None:
            data_payload["password"] = password
        if comments is not None:
            data_payload["comments"] = comments
        if private_key is not None:
            data_payload["private-key"] = private_key
        if certificate is not None:
            data_payload["certificate"] = certificate
        if csr is not None:
            data_payload["csr"] = csr
        if state is not None:
            data_payload["state"] = state
        if scep_url is not None:
            data_payload["scep-url"] = scep_url
        if range is not None:
            data_payload["range"] = range
        if source is not None:
            data_payload["source"] = source
        if auto_regenerate_days is not None:
            data_payload["auto-regenerate-days"] = auto_regenerate_days
        if auto_regenerate_days_warning is not None:
            data_payload["auto-regenerate-days-warning"] = (
                auto_regenerate_days_warning
            )
        if scep_password is not None:
            data_payload["scep-password"] = scep_password
        if ca_identifier is not None:
            data_payload["ca-identifier"] = ca_identifier
        if name_encoding is not None:
            data_payload["name-encoding"] = name_encoding
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if ike_localid is not None:
            data_payload["ike-localid"] = ike_localid
        if ike_localid_type is not None:
            data_payload["ike-localid-type"] = ike_localid_type
        if enroll_protocol is not None:
            data_payload["enroll-protocol"] = enroll_protocol
        if private_key_retain is not None:
            data_payload["private-key-retain"] = private_key_retain
        if cmp_server is not None:
            data_payload["cmp-server"] = cmp_server
        if cmp_path is not None:
            data_payload["cmp-path"] = cmp_path
        if cmp_server_cert is not None:
            data_payload["cmp-server-cert"] = cmp_server_cert
        if cmp_regeneration_method is not None:
            data_payload["cmp-regeneration-method"] = cmp_regeneration_method
        if acme_ca_url is not None:
            data_payload["acme-ca-url"] = acme_ca_url
        if acme_domain is not None:
            data_payload["acme-domain"] = acme_domain
        if acme_email is not None:
            data_payload["acme-email"] = acme_email
        if acme_eab_key_id is not None:
            data_payload["acme-eab-key-id"] = acme_eab_key_id
        if acme_eab_key_hmac is not None:
            data_payload["acme-eab-key-hmac"] = acme_eab_key_hmac
        if acme_rsa_key_size is not None:
            data_payload["acme-rsa-key-size"] = acme_rsa_key_size
        if acme_renew_window is not None:
            data_payload["acme-renew-window"] = acme_renew_window
        if est_server is not None:
            data_payload["est-server"] = est_server
        if est_ca_id is not None:
            data_payload["est-ca-id"] = est_ca_id
        if est_http_username is not None:
            data_payload["est-http-username"] = est_http_username
        if est_http_password is not None:
            data_payload["est-http-password"] = est_http_password
        if est_client_cert is not None:
            data_payload["est-client-cert"] = est_client_cert
        if est_server_cert is not None:
            data_payload["est-server-cert"] = est_server_cert
        if est_srp_username is not None:
            data_payload["est-srp-username"] = est_srp_username
        if est_srp_password is not None:
            data_payload["est-srp-password"] = est_srp_password
        if est_regeneration_method is not None:
            data_payload["est-regeneration-method"] = est_regeneration_method
        if details is not None:
            data_payload["details"] = details
        data_payload.update(kwargs)
        return self._client.post(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
