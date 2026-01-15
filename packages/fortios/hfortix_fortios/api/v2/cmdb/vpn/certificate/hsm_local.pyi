from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class HsmLocalPayload(TypedDict, total=False):
    """
    Type hints for vpn/certificate/hsm_local payload fields.
    
    Local certificates whose keys are stored on HSM.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.cloud-service.CloudServiceEndpoint` (via: gch-cloud-service-name)

    **Usage:**
        payload: HsmLocalPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 35
    comments: str  # Comment. | MaxLen: 511
    vendor: Literal["unknown", "gch"]  # HSM vendor. | Default: unknown
    api_version: Literal["unknown", "gch-default"]  # API version for communicating with HSM. | Default: unknown
    certificate: str  # PEM format certificate.
    range: Literal["global", "vdom"]  # Either a global or VDOM IP address range for the c | Default: vdom
    source: Literal["factory", "user", "bundle"]  # Certificate source type. | Default: user
    gch_url: str  # Google Cloud HSM key URL | MaxLen: 1024
    gch_project: str  # Google Cloud HSM project ID. | MaxLen: 31
    gch_location: str  # Google Cloud HSM location. | MaxLen: 63
    gch_keyring: str  # Google Cloud HSM keyring. | MaxLen: 63
    gch_cryptokey: str  # Google Cloud HSM cryptokey. | MaxLen: 63
    gch_cryptokey_version: str  # Google Cloud HSM cryptokey version. | MaxLen: 31
    gch_cloud_service_name: str  # Cloud service config name to generate access token | MaxLen: 35
    gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"]  # Google Cloud HSM cryptokey algorithm. | Default: rsa-sign-pkcs1-2048-sha256
    details: str  # Print hsm-local certificate detailed information.

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class HsmLocalResponse(TypedDict):
    """
    Type hints for vpn/certificate/hsm_local API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 35
    comments: str  # Comment. | MaxLen: 511
    vendor: Literal["unknown", "gch"]  # HSM vendor. | Default: unknown
    api_version: Literal["unknown", "gch-default"]  # API version for communicating with HSM. | Default: unknown
    certificate: str  # PEM format certificate.
    range: Literal["global", "vdom"]  # Either a global or VDOM IP address range for the c | Default: vdom
    source: Literal["factory", "user", "bundle"]  # Certificate source type. | Default: user
    gch_url: str  # Google Cloud HSM key URL | MaxLen: 1024
    gch_project: str  # Google Cloud HSM project ID. | MaxLen: 31
    gch_location: str  # Google Cloud HSM location. | MaxLen: 63
    gch_keyring: str  # Google Cloud HSM keyring. | MaxLen: 63
    gch_cryptokey: str  # Google Cloud HSM cryptokey. | MaxLen: 63
    gch_cryptokey_version: str  # Google Cloud HSM cryptokey version. | MaxLen: 31
    gch_cloud_service_name: str  # Cloud service config name to generate access token | MaxLen: 35
    gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"]  # Google Cloud HSM cryptokey algorithm. | Default: rsa-sign-pkcs1-2048-sha256
    details: str  # Print hsm-local certificate detailed information.


@final
class HsmLocalObject:
    """Typed FortiObject for vpn/certificate/hsm_local with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 511
    comments: str
    # HSM vendor. | Default: unknown
    vendor: Literal["unknown", "gch"]
    # API version for communicating with HSM. | Default: unknown
    api_version: Literal["unknown", "gch-default"]
    # PEM format certificate.
    certificate: str
    # Either a global or VDOM IP address range for the certificate | Default: vdom
    range: Literal["global", "vdom"]
    # Certificate source type. | Default: user
    source: Literal["factory", "user", "bundle"]
    # Google Cloud HSM key URL | MaxLen: 1024
    gch_url: str
    # Google Cloud HSM project ID. | MaxLen: 31
    gch_project: str
    # Google Cloud HSM location. | MaxLen: 63
    gch_location: str
    # Google Cloud HSM keyring. | MaxLen: 63
    gch_keyring: str
    # Google Cloud HSM cryptokey. | MaxLen: 63
    gch_cryptokey: str
    # Google Cloud HSM cryptokey version. | MaxLen: 31
    gch_cryptokey_version: str
    # Cloud service config name to generate access token. | MaxLen: 35
    gch_cloud_service_name: str
    # Google Cloud HSM cryptokey algorithm. | Default: rsa-sign-pkcs1-2048-sha256
    gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"]
    # Print hsm-local certificate detailed information.
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
    def to_dict(self) -> HsmLocalPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class HsmLocal:
    """
    Local certificates whose keys are stored on HSM.
    
    Path: vpn/certificate/hsm_local
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
    ) -> HsmLocalObject: ...
    
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
    ) -> HsmLocalObject: ...
    
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
    ) -> list[HsmLocalObject]: ...
    
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[HsmLocalObject]: ...
    
    # raw_json=True returns the full API envelope
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
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> list[HsmLocalObject]: ...
    
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> HsmLocalObject | list[HsmLocalObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
    @overload
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
    @overload
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> HsmLocalObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: HsmLocalPayload | None = ...,
        name: str | None = ...,
        comments: str | None = ...,
        vendor: Literal["unknown", "gch"] | None = ...,
        api_version: Literal["unknown", "gch-default"] | None = ...,
        certificate: str | None = ...,
        range: Literal["global", "vdom"] | None = ...,
        source: Literal["factory", "user", "bundle"] | None = ...,
        gch_url: str | None = ...,
        gch_project: str | None = ...,
        gch_location: str | None = ...,
        gch_keyring: str | None = ...,
        gch_cryptokey: str | None = ...,
        gch_cryptokey_version: str | None = ...,
        gch_cloud_service_name: str | None = ...,
        gch_cryptokey_algorithm: Literal["rsa-sign-pkcs1-2048-sha256", "rsa-sign-pkcs1-3072-sha256", "rsa-sign-pkcs1-4096-sha256", "rsa-sign-pkcs1-4096-sha512", "rsa-sign-pss-2048-sha256", "rsa-sign-pss-3072-sha256", "rsa-sign-pss-4096-sha256", "rsa-sign-pss-4096-sha512", "ec-sign-p256-sha256", "ec-sign-p384-sha384", "ec-sign-secp256k1-sha256"] | None = ...,
        details: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
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
    "HsmLocal",
    "HsmLocalPayload",
    "HsmLocalResponse",
    "HsmLocalObject",
]