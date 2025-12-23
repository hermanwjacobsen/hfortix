"""
FortiOS CMDB - Cmdb Vpn Certificate Setting

Configuration endpoint for managing cmdb vpn certificate setting objects.

API Endpoints:
    GET    /cmdb/vpn/certificate_setting
    PUT    /cmdb/vpn/certificate_setting/{identifier}

Example Usage:
    >>> from hfortix.FortiOS import FortiOS
    >>> fgt = FortiOS(host="192.168.1.99", token="your-api-token")
    >>>
    >>> # List all items
    >>> items = fgt.api.cmdb.vpn.certificate_setting.get()
    >>>
    >>> # Get specific item (if supported)
    >>> item = fgt.api.cmdb.vpn.certificate_setting.get(name="item_name")
    >>>
    >>> # Create new item (use POST)
    >>> result = fgt.api.cmdb.vpn.certificate_setting.post(
    ...     name="new_item",
    ...     # ... additional parameters
    ... )
    >>>
    >>> # Update existing item (use PUT)
    >>> result = fgt.api.cmdb.vpn.certificate_setting.put(
    ...     name="existing_item",
    ...     # ... parameters to update
    ... )
    >>>
    >>> # Delete item
    >>> result = fgt.api.cmdb.vpn.certificate_setting.delete(name="item_name")

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


class CertificateSetting:
    """
    Certificatesetting Operations.

    Provides CRUD operations for FortiOS certificatesetting configuration.

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
        Initialize CertificateSetting endpoint.

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
        endpoint = "/vpn.certificate/setting"
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
        ocsp_status: str | None = None,
        ocsp_option: str | None = None,
        proxy: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: str | None = None,
        source_ip: str | None = None,
        ocsp_default_server: str | None = None,
        interface_select_method: str | None = None,
        interface: str | None = None,
        vrf_select: int | None = None,
        check_ca_cert: str | None = None,
        check_ca_chain: str | None = None,
        subject_match: str | None = None,
        subject_set: str | None = None,
        cn_match: str | None = None,
        cn_allow_multi: str | None = None,
        crl_verification: list | None = None,
        strict_ocsp_check: str | None = None,
        ssl_min_proto_version: str | None = None,
        cmp_save_extra_certs: str | None = None,
        cmp_key_usage_checking: str | None = None,
        cert_expire_warning: int | None = None,
        certname_rsa1024: str | None = None,
        certname_rsa2048: str | None = None,
        certname_rsa4096: str | None = None,
        certname_dsa1024: str | None = None,
        certname_dsa2048: str | None = None,
        certname_ecdsa256: str | None = None,
        certname_ecdsa384: str | None = None,
        certname_ecdsa521: str | None = None,
        certname_ed25519: str | None = None,
        certname_ed448: str | None = None,
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
            ocsp_status: Enable/disable receiving certificates using the OCSP.
            (optional)
            ocsp_option: Specify whether the OCSP URL is from certificate or
            configured OCSP server. (optional)
            proxy: Proxy server FQDN or IP for OCSP/CA queries during
            certificate verification. (optional)
            proxy_port: Proxy server port (1 - 65535, default = 8080).
            (optional)
            proxy_username: Proxy server user name. (optional)
            proxy_password: Proxy server password. (optional)
            source_ip: Source IP address for dynamic AIA and OCSP queries.
            (optional)
            ocsp_default_server: Default OCSP server. (optional)
            interface_select_method: Specify how to select outgoing interface
            to reach server. (optional)
            interface: Specify outgoing interface to reach server. (optional)
            vrf_select: VRF ID used for connection to server. (optional)
            check_ca_cert: Enable/disable verification of the user certificate
            and pass authentication if any CA in the chain is trusted (default
            = enable). (optional)
            check_ca_chain: Enable/disable verification of the entire
            certificate chain and pass authentication only if the chain is
            complete and all of the CAs in the chain are trusted (default =
            disable). (optional)
            subject_match: When searching for a matching certificate, control
            how to do RDN value matching with certificate subject name (default
            = substring). (optional)
            subject_set: When searching for a matching certificate, control how
            to do RDN set matching with certificate subject name (default =
            subset). (optional)
            cn_match: When searching for a matching certificate, control how to
            do CN value matching with certificate subject name (default =
            substring). (optional)
            cn_allow_multi: When searching for a matching certificate, allow
            multiple CN fields in certificate subject name (default = enable).
            (optional)
            crl_verification: CRL verification options. (optional)
            strict_ocsp_check: Enable/disable strict mode OCSP checking.
            (optional)
            ssl_min_proto_version: Minimum supported protocol version for
            SSL/TLS connections (default is to follow system global setting).
            (optional)
            cmp_save_extra_certs: Enable/disable saving extra certificates in
            CMP mode (default = disable). (optional)
            cmp_key_usage_checking: Enable/disable server certificate key usage
            checking in CMP mode (default = enable). (optional)
            cert_expire_warning: Number of days before a certificate expires to
            send a warning. Set to 0 to disable sending of the warning (0 -
            100, default = 14). (optional)
            certname_rsa1024: 1024 bit RSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_rsa2048: 2048 bit RSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_rsa4096: 4096 bit RSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_dsa1024: 1024 bit DSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_dsa2048: 2048 bit DSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_ecdsa256: 256 bit ECDSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_ecdsa384: 384 bit ECDSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_ecdsa521: 521 bit ECDSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_ed25519: 253 bit EdDSA key certificate for re-signing
            server certificates for SSL inspection. (optional)
            certname_ed448: 456 bit EdDSA key certificate for re-signing server
            certificates for SSL inspection. (optional)
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
        endpoint = "/vpn.certificate/setting"
        if before is not None:
            data_payload["before"] = before
        if after is not None:
            data_payload["after"] = after
        if ocsp_status is not None:
            data_payload["ocsp-status"] = ocsp_status
        if ocsp_option is not None:
            data_payload["ocsp-option"] = ocsp_option
        if proxy is not None:
            data_payload["proxy"] = proxy
        if proxy_port is not None:
            data_payload["proxy-port"] = proxy_port
        if proxy_username is not None:
            data_payload["proxy-username"] = proxy_username
        if proxy_password is not None:
            data_payload["proxy-password"] = proxy_password
        if source_ip is not None:
            data_payload["source-ip"] = source_ip
        if ocsp_default_server is not None:
            data_payload["ocsp-default-server"] = ocsp_default_server
        if interface_select_method is not None:
            data_payload["interface-select-method"] = interface_select_method
        if interface is not None:
            data_payload["interface"] = interface
        if vrf_select is not None:
            data_payload["vrf-select"] = vrf_select
        if check_ca_cert is not None:
            data_payload["check-ca-cert"] = check_ca_cert
        if check_ca_chain is not None:
            data_payload["check-ca-chain"] = check_ca_chain
        if subject_match is not None:
            data_payload["subject-match"] = subject_match
        if subject_set is not None:
            data_payload["subject-set"] = subject_set
        if cn_match is not None:
            data_payload["cn-match"] = cn_match
        if cn_allow_multi is not None:
            data_payload["cn-allow-multi"] = cn_allow_multi
        if crl_verification is not None:
            data_payload["crl-verification"] = crl_verification
        if strict_ocsp_check is not None:
            data_payload["strict-ocsp-check"] = strict_ocsp_check
        if ssl_min_proto_version is not None:
            data_payload["ssl-min-proto-version"] = ssl_min_proto_version
        if cmp_save_extra_certs is not None:
            data_payload["cmp-save-extra-certs"] = cmp_save_extra_certs
        if cmp_key_usage_checking is not None:
            data_payload["cmp-key-usage-checking"] = cmp_key_usage_checking
        if cert_expire_warning is not None:
            data_payload["cert-expire-warning"] = cert_expire_warning
        if certname_rsa1024 is not None:
            data_payload["certname-rsa1024"] = certname_rsa1024
        if certname_rsa2048 is not None:
            data_payload["certname-rsa2048"] = certname_rsa2048
        if certname_rsa4096 is not None:
            data_payload["certname-rsa4096"] = certname_rsa4096
        if certname_dsa1024 is not None:
            data_payload["certname-dsa1024"] = certname_dsa1024
        if certname_dsa2048 is not None:
            data_payload["certname-dsa2048"] = certname_dsa2048
        if certname_ecdsa256 is not None:
            data_payload["certname-ecdsa256"] = certname_ecdsa256
        if certname_ecdsa384 is not None:
            data_payload["certname-ecdsa384"] = certname_ecdsa384
        if certname_ecdsa521 is not None:
            data_payload["certname-ecdsa521"] = certname_ecdsa521
        if certname_ed25519 is not None:
            data_payload["certname-ed25519"] = certname_ed25519
        if certname_ed448 is not None:
            data_payload["certname-ed448"] = certname_ed448
        data_payload.update(kwargs)
        return self._client.put(
            "cmdb", endpoint, data=data_payload, vdom=vdom, raw_json=raw_json
        )
