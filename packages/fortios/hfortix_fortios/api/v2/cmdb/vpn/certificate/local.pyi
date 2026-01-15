from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LocalPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate/local payload fields.
    
    Local keys and certificates.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.vpn.certificate.ca.CaEndpoint` (via: cmp-server-cert, est-server-cert)
        - :class:`~.vpn.certificate.local.LocalEndpoint` (via: est-client-cert)
        - :class:`~.vpn.certificate.remote.RemoteEndpoint` (via: cmp-server-cert, est-server-cert)

    **Usage:**
        payload: LocalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 35
    password: str  # Password as a PEM file. | MaxLen: 128
    comments: str  # Comment. | MaxLen: 511
    private_key: str  # PEM format key encrypted with a password.
    certificate: str  # PEM format certificate.
    csr: str  # Certificate Signing Request.
    state: str  # Certificate Signing Request State.
    scep_url: str  # SCEP server URL. | MaxLen: 255
    range: Literal["global", "vdom"]  # Either a global or VDOM IP address range for the c | Default: vdom
    source: Literal["factory", "user", "bundle"]  # Certificate source type. | Default: user
    auto_regenerate_days: int  # Number of days to wait before expiry of an updated | Default: 0 | Min: 0 | Max: 4294967295
    auto_regenerate_days_warning: int  # Number of days to wait before an expiry warning me | Default: 0 | Min: 0 | Max: 4294967295
    scep_password: str  # SCEP server challenge password for auto-regenerati | MaxLen: 128
    ca_identifier: str  # CA identifier of the CA server for signing via SCE | MaxLen: 255
    name_encoding: Literal["printable", "utf8"]  # Name encoding method for auto-regeneration. | Default: printable
    source_ip: str  # Source IP address for communications to the SCEP s | Default: 0.0.0.0
    ike_localid: str  # Local ID the FortiGate uses for authentication as | MaxLen: 63
    ike_localid_type: Literal["asn1dn", "fqdn"]  # IKE local ID type. | Default: asn1dn
    enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"]  # Certificate enrollment protocol. | Default: none
    private_key_retain: Literal["enable", "disable"]  # Enable/disable retention of private key during SCE | Default: disable
    cmp_server: str  # Address and port for CMP server | MaxLen: 63
    cmp_path: str  # Path location inside CMP server. | MaxLen: 255
    cmp_server_cert: str  # CMP server certificate. | MaxLen: 79
    cmp_regeneration_method: Literal["keyupate", "renewal"]  # CMP auto-regeneration method. | Default: keyupate
    acme_ca_url: str  # The URL for the ACME CA server | Default: https://acme-v02.api.letsencrypt.org/directory | MaxLen: 255
    acme_domain: str  # A valid domain that resolves to this FortiGate uni | MaxLen: 255
    acme_email: str  # Contact email address that is required by some CAs | MaxLen: 255
    acme_eab_key_id: str  # External Account Binding Key ID (optional setting) | MaxLen: 255
    acme_eab_key_hmac: str  # External Account Binding HMAC Key | MaxLen: 128
    acme_rsa_key_size: int  # Length of the RSA private key of the generated cer | Default: 2048 | Min: 2048 | Max: 4096
    acme_renew_window: int  # Beginning of the renewal window | Default: 30 | Min: 1 | Max: 60
    est_server: str  # Address and port for EST server | MaxLen: 255
    est_ca_id: str  # CA identifier of the CA server for signing via EST | MaxLen: 255
    est_http_username: str  # HTTP Authentication username for signing via EST. | MaxLen: 63
    est_http_password: str  # HTTP Authentication password for signing via EST. | MaxLen: 128
    est_client_cert: str  # Certificate used to authenticate this FortiGate to | MaxLen: 79
    est_server_cert: str  # EST server's certificate must be verifiable by thi | MaxLen: 79
    est_srp_username: str  # EST SRP authentication username. | MaxLen: 63
    est_srp_password: str  # EST SRP authentication password. | MaxLen: 128
    est_regeneration_method: Literal["create-new-key", "use-existing-key"]  # EST behavioral options during re-enrollment. | Default: create-new-key
    details: str  # Print local certificate detailed information.

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class LocalResponse(TypedDict):
    """
    Type hints for vpn/certificate/local API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 35
    password: str  # Password as a PEM file. | MaxLen: 128
    comments: str  # Comment. | MaxLen: 511
    private_key: str  # PEM format key encrypted with a password.
    certificate: str  # PEM format certificate.
    csr: str  # Certificate Signing Request.
    state: str  # Certificate Signing Request State.
    scep_url: str  # SCEP server URL. | MaxLen: 255
    range: Literal["global", "vdom"]  # Either a global or VDOM IP address range for the c | Default: vdom
    source: Literal["factory", "user", "bundle"]  # Certificate source type. | Default: user
    auto_regenerate_days: int  # Number of days to wait before expiry of an updated | Default: 0 | Min: 0 | Max: 4294967295
    auto_regenerate_days_warning: int  # Number of days to wait before an expiry warning me | Default: 0 | Min: 0 | Max: 4294967295
    scep_password: str  # SCEP server challenge password for auto-regenerati | MaxLen: 128
    ca_identifier: str  # CA identifier of the CA server for signing via SCE | MaxLen: 255
    name_encoding: Literal["printable", "utf8"]  # Name encoding method for auto-regeneration. | Default: printable
    source_ip: str  # Source IP address for communications to the SCEP s | Default: 0.0.0.0
    ike_localid: str  # Local ID the FortiGate uses for authentication as | MaxLen: 63
    ike_localid_type: Literal["asn1dn", "fqdn"]  # IKE local ID type. | Default: asn1dn
    enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"]  # Certificate enrollment protocol. | Default: none
    private_key_retain: Literal["enable", "disable"]  # Enable/disable retention of private key during SCE | Default: disable
    cmp_server: str  # Address and port for CMP server | MaxLen: 63
    cmp_path: str  # Path location inside CMP server. | MaxLen: 255
    cmp_server_cert: str  # CMP server certificate. | MaxLen: 79
    cmp_regeneration_method: Literal["keyupate", "renewal"]  # CMP auto-regeneration method. | Default: keyupate
    acme_ca_url: str  # The URL for the ACME CA server | Default: https://acme-v02.api.letsencrypt.org/directory | MaxLen: 255
    acme_domain: str  # A valid domain that resolves to this FortiGate uni | MaxLen: 255
    acme_email: str  # Contact email address that is required by some CAs | MaxLen: 255
    acme_eab_key_id: str  # External Account Binding Key ID (optional setting) | MaxLen: 255
    acme_eab_key_hmac: str  # External Account Binding HMAC Key | MaxLen: 128
    acme_rsa_key_size: int  # Length of the RSA private key of the generated cer | Default: 2048 | Min: 2048 | Max: 4096
    acme_renew_window: int  # Beginning of the renewal window | Default: 30 | Min: 1 | Max: 60
    est_server: str  # Address and port for EST server | MaxLen: 255
    est_ca_id: str  # CA identifier of the CA server for signing via EST | MaxLen: 255
    est_http_username: str  # HTTP Authentication username for signing via EST. | MaxLen: 63
    est_http_password: str  # HTTP Authentication password for signing via EST. | MaxLen: 128
    est_client_cert: str  # Certificate used to authenticate this FortiGate to | MaxLen: 79
    est_server_cert: str  # EST server's certificate must be verifiable by thi | MaxLen: 79
    est_srp_username: str  # EST SRP authentication username. | MaxLen: 63
    est_srp_password: str  # EST SRP authentication password. | MaxLen: 128
    est_regeneration_method: Literal["create-new-key", "use-existing-key"]  # EST behavioral options during re-enrollment. | Default: create-new-key
    details: str  # Print local certificate detailed information.


@final
class LocalObject:
    """Typed FortiObject for vpn/certificate/local with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Password as a PEM file. | MaxLen: 128
    password: str
    # Comment. | MaxLen: 511
    comments: str
    # PEM format key encrypted with a password.
    private_key: str
    # PEM format certificate.
    certificate: str
    # Certificate Signing Request.
    csr: str
    # Certificate Signing Request State.
    state: str
    # SCEP server URL. | MaxLen: 255
    scep_url: str
    # Either a global or VDOM IP address range for the certificate | Default: vdom
    range: Literal["global", "vdom"]
    # Certificate source type. | Default: user
    source: Literal["factory", "user", "bundle"]
    # Number of days to wait before expiry of an updated local cer | Default: 0 | Min: 0 | Max: 4294967295
    auto_regenerate_days: int
    # Number of days to wait before an expiry warning message is g | Default: 0 | Min: 0 | Max: 4294967295
    auto_regenerate_days_warning: int
    # SCEP server challenge password for auto-regeneration. | MaxLen: 128
    scep_password: str
    # CA identifier of the CA server for signing via SCEP. | MaxLen: 255
    ca_identifier: str
    # Name encoding method for auto-regeneration. | Default: printable
    name_encoding: Literal["printable", "utf8"]
    # Source IP address for communications to the SCEP server. | Default: 0.0.0.0
    source_ip: str
    # Local ID the FortiGate uses for authentication as a VPN clie | MaxLen: 63
    ike_localid: str
    # IKE local ID type. | Default: asn1dn
    ike_localid_type: Literal["asn1dn", "fqdn"]
    # Certificate enrollment protocol. | Default: none
    enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"]
    # Enable/disable retention of private key during SCEP renewal | Default: disable
    private_key_retain: Literal["enable", "disable"]
    # Address and port for CMP server (format = address:port). | MaxLen: 63
    cmp_server: str
    # Path location inside CMP server. | MaxLen: 255
    cmp_path: str
    # CMP server certificate. | MaxLen: 79
    cmp_server_cert: str
    # CMP auto-regeneration method. | Default: keyupate
    cmp_regeneration_method: Literal["keyupate", "renewal"]
    # The URL for the ACME CA server | Default: https://acme-v02.api.letsencrypt.org/directory | MaxLen: 255
    acme_ca_url: str
    # A valid domain that resolves to this FortiGate unit. | MaxLen: 255
    acme_domain: str
    # Contact email address that is required by some CAs like Lets | MaxLen: 255
    acme_email: str
    # External Account Binding Key ID (optional setting). | MaxLen: 255
    acme_eab_key_id: str
    # External Account Binding HMAC Key (URL-encoded base64). | MaxLen: 128
    acme_eab_key_hmac: str
    # Length of the RSA private key of the generated cert | Default: 2048 | Min: 2048 | Max: 4096
    acme_rsa_key_size: int
    # Beginning of the renewal window | Default: 30 | Min: 1 | Max: 60
    acme_renew_window: int
    # Address and port for EST server | MaxLen: 255
    est_server: str
    # CA identifier of the CA server for signing via EST. | MaxLen: 255
    est_ca_id: str
    # HTTP Authentication username for signing via EST. | MaxLen: 63
    est_http_username: str
    # HTTP Authentication password for signing via EST. | MaxLen: 128
    est_http_password: str
    # Certificate used to authenticate this FortiGate to EST serve | MaxLen: 79
    est_client_cert: str
    # EST server's certificate must be verifiable by this certific | MaxLen: 79
    est_server_cert: str
    # EST SRP authentication username. | MaxLen: 63
    est_srp_username: str
    # EST SRP authentication password. | MaxLen: 128
    est_srp_password: str
    # EST behavioral options during re-enrollment. | Default: create-new-key
    est_regeneration_method: Literal["create-new-key", "use-existing-key"]
    # Print local certificate detailed information.
    details: str
    
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
    def to_dict(self) -> LocalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Local:
    """
    Local keys and certificates.
    
    Path: vpn/certificate/local
    Category: cmdb
    Primary Key: name
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
    ) -> LocalObject: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> FortiObjectList[LocalObject]: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> FortiObjectList[LocalObject]: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> LocalObject: ...
    
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
    ) -> FortiObjectList[LocalObject]: ...
    
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
    ) -> Union[dict[str, Any], list[dict[str, Any]], FortiObject, list[FortiObject]]: ...
    
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
    ) -> LocalObject | list[LocalObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LocalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: LocalPayload | None = ...,
        name: str | None = ...,
        password: str | None = ...,
        comments: str | None = ...,
        private_key: str | None = ...,
        certificate: str | None = ...,
        csr: str | None = ...,
        state: str | None = ...,
        scep_url: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        auto_regenerate_days: int | None = ...,
        auto_regenerate_days_warning: int | None = ...,
        scep_password: str | None = ...,
        ca_identifier: str | None = ...,
        name_encoding: Literal["printable", "utf8"] | None = ...,
        source_ip: str | None = ...,
        ike_localid: str | None = ...,
        ike_localid_type: Literal["asn1dn", "fqdn"] | None = ...,
        enroll_protocol: Literal["none", "scep", "cmpv2", "acme2", "est"] | None = ...,
        private_key_retain: Literal["enable", "disable"] | None = ...,
        cmp_server: str | None = ...,
        cmp_path: str | None = ...,
        cmp_server_cert: str | None = ...,
        cmp_regeneration_method: Literal["keyupate", "renewal"] | None = ...,
        acme_ca_url: str | None = ...,
        acme_domain: str | None = ...,
        acme_email: str | None = ...,
        acme_eab_key_id: str | None = ...,
        acme_eab_key_hmac: str | None = ...,
        acme_rsa_key_size: int | None = ...,
        acme_renew_window: int | None = ...,
        est_server: str | None = ...,
        est_ca_id: str | None = ...,
        est_http_username: str | None = ...,
        est_http_password: str | None = ...,
        est_client_cert: str | None = ...,
        est_server_cert: str | None = ...,
        est_srp_username: str | None = ...,
        est_srp_password: str | None = ...,
        est_regeneration_method: Literal["create-new-key", "use-existing-key"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
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
    "Local",
    "LocalPayload",
    "LocalResponse",
    "LocalObject",
]