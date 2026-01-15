from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingPayload(TypedDict, total=False):
    """
    Type hints for firewall/ssh/setting payload fields.
    
    SSH proxy settings.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.firewall.ssh.local-ca.LocalCaEndpoint` (via: caname, untrusted-caname)
        - :class:`~.firewall.ssh.local-key.LocalKeyEndpoint` (via: hostkey-dsa1024, hostkey-ecdsa256, hostkey-ecdsa384, +3 more)

    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    caname: str  # CA certificate used by SSH Inspection. | MaxLen: 35
    untrusted_caname: str  # Untrusted CA certificate used by SSH Inspection. | MaxLen: 35
    hostkey_rsa2048: str  # RSA certificate used by SSH proxy. | MaxLen: 35
    hostkey_dsa1024: str  # DSA certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa256: str  # ECDSA nid256 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa384: str  # ECDSA nid384 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa521: str  # ECDSA nid384 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ed25519: str  # ED25519 hostkey used by SSH proxy. | MaxLen: 35
    host_trusted_checking: Literal["enable", "disable"]  # Enable/disable host trusted checking. | Default: enable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SettingResponse(TypedDict):
    """
    Type hints for firewall/ssh/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    caname: str  # CA certificate used by SSH Inspection. | MaxLen: 35
    untrusted_caname: str  # Untrusted CA certificate used by SSH Inspection. | MaxLen: 35
    hostkey_rsa2048: str  # RSA certificate used by SSH proxy. | MaxLen: 35
    hostkey_dsa1024: str  # DSA certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa256: str  # ECDSA nid256 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa384: str  # ECDSA nid384 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa521: str  # ECDSA nid384 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ed25519: str  # ED25519 hostkey used by SSH proxy. | MaxLen: 35
    host_trusted_checking: Literal["enable", "disable"]  # Enable/disable host trusted checking. | Default: enable


@final
class SettingObject:
    """Typed FortiObject for firewall/ssh/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # CA certificate used by SSH Inspection. | MaxLen: 35
    caname: str
    # Untrusted CA certificate used by SSH Inspection. | MaxLen: 35
    untrusted_caname: str
    # RSA certificate used by SSH proxy. | MaxLen: 35
    hostkey_rsa2048: str
    # DSA certificate used by SSH proxy. | MaxLen: 35
    hostkey_dsa1024: str
    # ECDSA nid256 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa256: str
    # ECDSA nid384 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa384: str
    # ECDSA nid384 certificate used by SSH proxy. | MaxLen: 35
    hostkey_ecdsa521: str
    # ED25519 hostkey used by SSH proxy. | MaxLen: 35
    hostkey_ed25519: str
    # Enable/disable host trusted checking. | Default: enable
    host_trusted_checking: Literal["enable", "disable"]
    
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
    SSH proxy settings.
    
    Path: firewall/ssh/setting
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
        raw_json: Literal[False] = ...,
        *,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: Literal[False] = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        raw_json: bool = ...,
        **kwargs: Any,
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
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
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
        payload_dict: SettingPayload | None = ...,
        caname: str | None = ...,
        untrusted_caname: str | None = ...,
        hostkey_rsa2048: str | None = ...,
        hostkey_dsa1024: str | None = ...,
        hostkey_ecdsa256: str | None = ...,
        hostkey_ecdsa384: str | None = ...,
        hostkey_ecdsa521: str | None = ...,
        hostkey_ed25519: str | None = ...,
        host_trusted_checking: Literal["enable", "disable"] | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingResponse",
    "SettingObject",
]