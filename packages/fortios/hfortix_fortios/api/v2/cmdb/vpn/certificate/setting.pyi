from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate/setting payload fields.
    
    VPN certificate setting.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.interface.InterfaceEndpoint` (via: interface)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: certname-dsa1024, certname-dsa2048, certname-ecdsa256, +7 more)
        - :class:`~.vpn.certificate.ocsp-server.OcspServerEndpoint` (via: ocsp-default-server)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    ocsp_status: Literal["enable", "mandatory", "disable"]  # Enable/disable receiving certificates using the OC | Default: disable
    ocsp_option: Literal["certificate", "server"]  # Specify whether the OCSP URL is from certificate o | Default: server
    proxy: str  # Proxy server FQDN or IP for OCSP/CA queries during | MaxLen: 127
    proxy_port: int  # Proxy server port (1 - 65535, default = 8080). | Default: 8080 | Min: 1 | Max: 65535
    proxy_username: str  # Proxy server user name. | MaxLen: 63
    proxy_password: str  # Proxy server password. | MaxLen: 128
    source_ip: str  # Source IP address for dynamic AIA and OCSP queries | MaxLen: 63
    ocsp_default_server: str  # Default OCSP server. | MaxLen: 35
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    check_ca_cert: Literal["enable", "disable"]  # Enable/disable verification of the user certificat | Default: enable
    check_ca_chain: Literal["enable", "disable"]  # Enable/disable verification of the entire certific | Default: disable
    subject_match: Literal["substring", "value"]  # When searching for a matching certificate, control | Default: substring
    subject_set: Literal["subset", "superset"]  # When searching for a matching certificate, control | Default: subset
    cn_match: Literal["substring", "value"]  # When searching for a matching certificate, control | Default: substring
    cn_allow_multi: Literal["disable", "enable"]  # When searching for a matching certificate, allow m | Default: enable
    crl_verification: str  # CRL verification options.
    strict_ocsp_check: Literal["enable", "disable"]  # Enable/disable strict mode OCSP checking. | Default: disable
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: default
    cmp_save_extra_certs: Literal["enable", "disable"]  # Enable/disable saving extra certificates in CMP mo | Default: disable
    cmp_key_usage_checking: Literal["enable", "disable"]  # Enable/disable server certificate key usage checki | Default: enable
    cert_expire_warning: int  # Number of days before a certificate expires to sen | Default: 14 | Min: 0 | Max: 100
    certname_rsa1024: str  # 1024 bit RSA key certificate for re-signing server | Default: Fortinet_SSL_RSA1024 | MaxLen: 35
    certname_rsa2048: str  # 2048 bit RSA key certificate for re-signing server | Default: Fortinet_SSL_RSA2048 | MaxLen: 35
    certname_rsa4096: str  # 4096 bit RSA key certificate for re-signing server | Default: Fortinet_SSL_RSA4096 | MaxLen: 35
    certname_dsa1024: str  # 1024 bit DSA key certificate for re-signing server | Default: Fortinet_SSL_DSA1024 | MaxLen: 35
    certname_dsa2048: str  # 2048 bit DSA key certificate for re-signing server | Default: Fortinet_SSL_DSA2048 | MaxLen: 35
    certname_ecdsa256: str  # 256 bit ECDSA key certificate for re-signing serve | Default: Fortinet_SSL_ECDSA256 | MaxLen: 35
    certname_ecdsa384: str  # 384 bit ECDSA key certificate for re-signing serve | Default: Fortinet_SSL_ECDSA384 | MaxLen: 35
    certname_ecdsa521: str  # 521 bit ECDSA key certificate for re-signing serve | Default: Fortinet_SSL_ECDSA521 | MaxLen: 35
    certname_ed25519: str  # 253 bit EdDSA key certificate for re-signing serve | Default: Fortinet_SSL_ED25519 | MaxLen: 35
    certname_ed448: str  # 456 bit EdDSA key certificate for re-signing serve | Default: Fortinet_SSL_ED448 | MaxLen: 35

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for vpn/certificate/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    ocsp_status: Literal["enable", "mandatory", "disable"]  # Enable/disable receiving certificates using the OC | Default: disable
    ocsp_option: Literal["certificate", "server"]  # Specify whether the OCSP URL is from certificate o | Default: server
    proxy: str  # Proxy server FQDN or IP for OCSP/CA queries during | MaxLen: 127
    proxy_port: int  # Proxy server port (1 - 65535, default = 8080). | Default: 8080 | Min: 1 | Max: 65535
    proxy_username: str  # Proxy server user name. | MaxLen: 63
    proxy_password: str  # Proxy server password. | MaxLen: 128
    source_ip: str  # Source IP address for dynamic AIA and OCSP queries | MaxLen: 63
    ocsp_default_server: str  # Default OCSP server. | MaxLen: 35
    interface_select_method: Literal["auto", "sdwan", "specify"]  # Specify how to select outgoing interface to reach | Default: auto
    interface: str  # Specify outgoing interface to reach server. | MaxLen: 15
    vrf_select: int  # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    check_ca_cert: Literal["enable", "disable"]  # Enable/disable verification of the user certificat | Default: enable
    check_ca_chain: Literal["enable", "disable"]  # Enable/disable verification of the entire certific | Default: disable
    subject_match: Literal["substring", "value"]  # When searching for a matching certificate, control | Default: substring
    subject_set: Literal["subset", "superset"]  # When searching for a matching certificate, control | Default: subset
    cn_match: Literal["substring", "value"]  # When searching for a matching certificate, control | Default: substring
    cn_allow_multi: Literal["disable", "enable"]  # When searching for a matching certificate, allow m | Default: enable
    crl_verification: str  # CRL verification options.
    strict_ocsp_check: Literal["enable", "disable"]  # Enable/disable strict mode OCSP checking. | Default: disable
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]  # Minimum supported protocol version for SSL/TLS con | Default: default
    cmp_save_extra_certs: Literal["enable", "disable"]  # Enable/disable saving extra certificates in CMP mo | Default: disable
    cmp_key_usage_checking: Literal["enable", "disable"]  # Enable/disable server certificate key usage checki | Default: enable
    cert_expire_warning: int  # Number of days before a certificate expires to sen | Default: 14 | Min: 0 | Max: 100
    certname_rsa1024: str  # 1024 bit RSA key certificate for re-signing server | Default: Fortinet_SSL_RSA1024 | MaxLen: 35
    certname_rsa2048: str  # 2048 bit RSA key certificate for re-signing server | Default: Fortinet_SSL_RSA2048 | MaxLen: 35
    certname_rsa4096: str  # 4096 bit RSA key certificate for re-signing server | Default: Fortinet_SSL_RSA4096 | MaxLen: 35
    certname_dsa1024: str  # 1024 bit DSA key certificate for re-signing server | Default: Fortinet_SSL_DSA1024 | MaxLen: 35
    certname_dsa2048: str  # 2048 bit DSA key certificate for re-signing server | Default: Fortinet_SSL_DSA2048 | MaxLen: 35
    certname_ecdsa256: str  # 256 bit ECDSA key certificate for re-signing serve | Default: Fortinet_SSL_ECDSA256 | MaxLen: 35
    certname_ecdsa384: str  # 384 bit ECDSA key certificate for re-signing serve | Default: Fortinet_SSL_ECDSA384 | MaxLen: 35
    certname_ecdsa521: str  # 521 bit ECDSA key certificate for re-signing serve | Default: Fortinet_SSL_ECDSA521 | MaxLen: 35
    certname_ed25519: str  # 253 bit EdDSA key certificate for re-signing serve | Default: Fortinet_SSL_ED25519 | MaxLen: 35
    certname_ed448: str  # 456 bit EdDSA key certificate for re-signing serve | Default: Fortinet_SSL_ED448 | MaxLen: 35


@final
class SettingObject:
    """Typed FortiObject for vpn/certificate/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable receiving certificates using the OCSP. | Default: disable
    ocsp_status: Literal["enable", "mandatory", "disable"]
    # Specify whether the OCSP URL is from certificate or configur | Default: server
    ocsp_option: Literal["certificate", "server"]
    # Proxy server FQDN or IP for OCSP/CA queries during certifica | MaxLen: 127
    proxy: str
    # Proxy server port (1 - 65535, default = 8080). | Default: 8080 | Min: 1 | Max: 65535
    proxy_port: int
    # Proxy server user name. | MaxLen: 63
    proxy_username: str
    # Proxy server password. | MaxLen: 128
    proxy_password: str
    # Source IP address for dynamic AIA and OCSP queries. | MaxLen: 63
    source_ip: str
    # Default OCSP server. | MaxLen: 35
    ocsp_default_server: str
    # Specify how to select outgoing interface to reach server. | Default: auto
    interface_select_method: Literal["auto", "sdwan", "specify"]
    # Specify outgoing interface to reach server. | MaxLen: 15
    interface: str
    # VRF ID used for connection to server. | Default: 0 | Min: 0 | Max: 511
    vrf_select: int
    # Enable/disable verification of the user certificate and pass | Default: enable
    check_ca_cert: Literal["enable", "disable"]
    # Enable/disable verification of the entire certificate chain | Default: disable
    check_ca_chain: Literal["enable", "disable"]
    # When searching for a matching certificate, control how to do | Default: substring
    subject_match: Literal["substring", "value"]
    # When searching for a matching certificate, control how to do | Default: subset
    subject_set: Literal["subset", "superset"]
    # When searching for a matching certificate, control how to do | Default: substring
    cn_match: Literal["substring", "value"]
    # When searching for a matching certificate, allow multiple CN | Default: enable
    cn_allow_multi: Literal["disable", "enable"]
    # CRL verification options.
    crl_verification: str
    # Enable/disable strict mode OCSP checking. | Default: disable
    strict_ocsp_check: Literal["enable", "disable"]
    # Minimum supported protocol version for SSL/TLS connections | Default: default
    ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"]
    # Enable/disable saving extra certificates in CMP mode | Default: disable
    cmp_save_extra_certs: Literal["enable", "disable"]
    # Enable/disable server certificate key usage checking in CMP | Default: enable
    cmp_key_usage_checking: Literal["enable", "disable"]
    # Number of days before a certificate expires to send a warnin | Default: 14 | Min: 0 | Max: 100
    cert_expire_warning: int
    # 1024 bit RSA key certificate for re-signing server certifica | Default: Fortinet_SSL_RSA1024 | MaxLen: 35
    certname_rsa1024: str
    # 2048 bit RSA key certificate for re-signing server certifica | Default: Fortinet_SSL_RSA2048 | MaxLen: 35
    certname_rsa2048: str
    # 4096 bit RSA key certificate for re-signing server certifica | Default: Fortinet_SSL_RSA4096 | MaxLen: 35
    certname_rsa4096: str
    # 1024 bit DSA key certificate for re-signing server certifica | Default: Fortinet_SSL_DSA1024 | MaxLen: 35
    certname_dsa1024: str
    # 2048 bit DSA key certificate for re-signing server certifica | Default: Fortinet_SSL_DSA2048 | MaxLen: 35
    certname_dsa2048: str
    # 256 bit ECDSA key certificate for re-signing server certific | Default: Fortinet_SSL_ECDSA256 | MaxLen: 35
    certname_ecdsa256: str
    # 384 bit ECDSA key certificate for re-signing server certific | Default: Fortinet_SSL_ECDSA384 | MaxLen: 35
    certname_ecdsa384: str
    # 521 bit ECDSA key certificate for re-signing server certific | Default: Fortinet_SSL_ECDSA521 | MaxLen: 35
    certname_ecdsa521: str
    # 253 bit EdDSA key certificate for re-signing server certific | Default: Fortinet_SSL_ED25519 | MaxLen: 35
    certname_ed25519: str
    # 456 bit EdDSA key certificate for re-signing server certific | Default: Fortinet_SSL_ED448 | MaxLen: 35
    certname_ed448: str
    
    # Common API response fields
    status: str
    http_status: int | None
    vdom: str | None
    
    # Methods from FortiObject
    @property
    def dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        ...
    @property
    def json(self) -> dict[str, Any]:
        """Convert to dictionary (alias for .dict)."""
        ...
    @property
    def raw(self) -> dict[str, Any]:
        """Get raw API response data."""
        ...
    def get_full(self, name: str) -> Any: ...
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Setting:
    """
    VPN certificate setting.
    
    Path: vpn/certificate/setting
    Category: cmdb
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        name: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # With no mkey -> returns list of objects
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        name: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # Dict mode - list of dicts (no mkey/name provided) - keyword-only signature
    @overload
    def get(
        self,
        *,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> dict[str, Any] | FortiObject: ...
    
    def get(
        self,
        name: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        ocsp_status: Literal["enable", "mandatory", "disable"] | None = ...,
        ocsp_option: Literal["certificate", "server"] | None = ...,
        proxy: str | None = ...,
        proxy_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        source_ip: str | None = ...,
        ocsp_default_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        check_ca_cert: Literal["enable", "disable"] | None = ...,
        check_ca_chain: Literal["enable", "disable"] | None = ...,
        subject_match: Literal["substring", "value"] | None = ...,
        subject_set: Literal["subset", "superset"] | None = ...,
        cn_match: Literal["substring", "value"] | None = ...,
        cn_allow_multi: Literal["disable", "enable"] | None = ...,
        crl_verification: str | None = ...,
        strict_ocsp_check: Literal["enable", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        cmp_save_extra_certs: Literal["enable", "disable"] | None = ...,
        cmp_key_usage_checking: Literal["enable", "disable"] | None = ...,
        cert_expire_warning: int | None = ...,
        certname_rsa1024: str | None = ...,
        certname_rsa2048: str | None = ...,
        certname_rsa4096: str | None = ...,
        certname_dsa1024: str | None = ...,
        certname_dsa2048: str | None = ...,
        certname_ecdsa256: str | None = ...,
        certname_ecdsa384: str | None = ...,
        certname_ecdsa521: str | None = ...,
        certname_ed25519: str | None = ...,
        certname_ed448: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        ocsp_status: Literal["enable", "mandatory", "disable"] | None = ...,
        ocsp_option: Literal["certificate", "server"] | None = ...,
        proxy: str | None = ...,
        proxy_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        source_ip: str | None = ...,
        ocsp_default_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        check_ca_cert: Literal["enable", "disable"] | None = ...,
        check_ca_chain: Literal["enable", "disable"] | None = ...,
        subject_match: Literal["substring", "value"] | None = ...,
        subject_set: Literal["subset", "superset"] | None = ...,
        cn_match: Literal["substring", "value"] | None = ...,
        cn_allow_multi: Literal["disable", "enable"] | None = ...,
        crl_verification: str | None = ...,
        strict_ocsp_check: Literal["enable", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        cmp_save_extra_certs: Literal["enable", "disable"] | None = ...,
        cmp_key_usage_checking: Literal["enable", "disable"] | None = ...,
        cert_expire_warning: int | None = ...,
        certname_rsa1024: str | None = ...,
        certname_rsa2048: str | None = ...,
        certname_rsa4096: str | None = ...,
        certname_dsa1024: str | None = ...,
        certname_dsa2048: str | None = ...,
        certname_ecdsa256: str | None = ...,
        certname_ecdsa384: str | None = ...,
        certname_ecdsa521: str | None = ...,
        certname_ed25519: str | None = ...,
        certname_ed448: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        ocsp_status: Literal["enable", "mandatory", "disable"] | None = ...,
        ocsp_option: Literal["certificate", "server"] | None = ...,
        proxy: str | None = ...,
        proxy_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        source_ip: str | None = ...,
        ocsp_default_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        check_ca_cert: Literal["enable", "disable"] | None = ...,
        check_ca_chain: Literal["enable", "disable"] | None = ...,
        subject_match: Literal["substring", "value"] | None = ...,
        subject_set: Literal["subset", "superset"] | None = ...,
        cn_match: Literal["substring", "value"] | None = ...,
        cn_allow_multi: Literal["disable", "enable"] | None = ...,
        crl_verification: str | None = ...,
        strict_ocsp_check: Literal["enable", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        cmp_save_extra_certs: Literal["enable", "disable"] | None = ...,
        cmp_key_usage_checking: Literal["enable", "disable"] | None = ...,
        cert_expire_warning: int | None = ...,
        certname_rsa1024: str | None = ...,
        certname_rsa2048: str | None = ...,
        certname_rsa4096: str | None = ...,
        certname_dsa1024: str | None = ...,
        certname_dsa2048: str | None = ...,
        certname_ecdsa256: str | None = ...,
        certname_ecdsa384: str | None = ...,
        certname_ecdsa521: str | None = ...,
        certname_ed25519: str | None = ...,
        certname_ed448: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        ocsp_status: Literal["enable", "mandatory", "disable"] | None = ...,
        ocsp_option: Literal["certificate", "server"] | None = ...,
        proxy: str | None = ...,
        proxy_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        source_ip: str | None = ...,
        ocsp_default_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        check_ca_cert: Literal["enable", "disable"] | None = ...,
        check_ca_chain: Literal["enable", "disable"] | None = ...,
        subject_match: Literal["substring", "value"] | None = ...,
        subject_set: Literal["subset", "superset"] | None = ...,
        cn_match: Literal["substring", "value"] | None = ...,
        cn_allow_multi: Literal["disable", "enable"] | None = ...,
        crl_verification: str | None = ...,
        strict_ocsp_check: Literal["enable", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        cmp_save_extra_certs: Literal["enable", "disable"] | None = ...,
        cmp_key_usage_checking: Literal["enable", "disable"] | None = ...,
        cert_expire_warning: int | None = ...,
        certname_rsa1024: str | None = ...,
        certname_rsa2048: str | None = ...,
        certname_rsa4096: str | None = ...,
        certname_dsa1024: str | None = ...,
        certname_dsa2048: str | None = ...,
        certname_ecdsa256: str | None = ...,
        certname_ecdsa384: str | None = ...,
        certname_ecdsa521: str | None = ...,
        certname_ed25519: str | None = ...,
        certname_ed448: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SettingPayload | None = ...,
        ocsp_status: Literal["enable", "mandatory", "disable"] | None = ...,
        ocsp_option: Literal["certificate", "server"] | None = ...,
        proxy: str | None = ...,
        proxy_port: int | None = ...,
        proxy_username: str | None = ...,
        proxy_password: str | None = ...,
        source_ip: str | None = ...,
        ocsp_default_server: str | None = ...,
        interface_select_method: Literal["auto", "sdwan", "specify"] | None = ...,
        interface: str | None = ...,
        vrf_select: int | None = ...,
        check_ca_cert: Literal["enable", "disable"] | None = ...,
        check_ca_chain: Literal["enable", "disable"] | None = ...,
        subject_match: Literal["substring", "value"] | None = ...,
        subject_set: Literal["subset", "superset"] | None = ...,
        cn_match: Literal["substring", "value"] | None = ...,
        cn_allow_multi: Literal["disable", "enable"] | None = ...,
        crl_verification: str | None = ...,
        strict_ocsp_check: Literal["enable", "disable"] | None = ...,
        ssl_min_proto_version: Literal["default", "SSLv3", "TLSv1", "TLSv1-1", "TLSv1-2", "TLSv1-3"] | None = ...,
        cmp_save_extra_certs: Literal["enable", "disable"] | None = ...,
        cmp_key_usage_checking: Literal["enable", "disable"] | None = ...,
        cert_expire_warning: int | None = ...,
        certname_rsa1024: str | None = ...,
        certname_rsa2048: str | None = ...,
        certname_rsa4096: str | None = ...,
        certname_dsa1024: str | None = ...,
        certname_dsa2048: str | None = ...,
        certname_ecdsa256: str | None = ...,
        certname_ecdsa384: str | None = ...,
        certname_ecdsa521: str | None = ...,
        certname_ed25519: str | None = ...,
        certname_ed448: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Helper methods
    @staticmethod
    def help(field_name: str | None = ...) -> str: ...
    
    @staticmethod
    def fields(detailed: bool = ...) -> Union[list[str], list[dict[str, Any]]]: ...
    
    @staticmethod
    def field_info(field_name: str) -> FortiObject: ...
    
    @staticmethod
    def validate_field(name: str, value: Any) -> bool: ...
    
    @staticmethod
    def required_fields() -> list[str]: ...
    
    @staticmethod
    def defaults() -> FortiObject: ...
    
    @staticmethod
    def schema() -> FortiObject: ...


# ================================================================


__all__ = [
    "Setting",
    "SettingPayload",
    "SettingResponse",
    "SettingObject",
]