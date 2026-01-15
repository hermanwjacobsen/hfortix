from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ApcfgProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/apcfg_profile payload fields.
    
    Configure AP local configuration profiles.
    
    **Usage:**
        payload: ApcfgProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # AP local configuration profile name. | MaxLen: 35
    ap_family: Literal["fap", "fap-u", "fap-c"]  # FortiAP family type (default = fap). | Default: fap
    comment: str  # Comment. | MaxLen: 255
    ac_type: Literal["default", "specify", "apcfg"]  # Validation controller type (default = default). | Default: default
    ac_timer: int  # Maximum waiting time for the AP to join the valida | Default: 10 | Min: 3 | Max: 30
    ac_ip: str  # IP address of the validation controller that AP mu | Default: 0.0.0.0
    ac_port: int  # Port of the validation controller that AP must be | Default: 5246 | Min: 1024 | Max: 49150
    command_list: list[dict[str, Any]]  # AP local configuration command list.

# Nested TypedDicts for table field children (dict mode)

class ApcfgProfileCommandlistItem(TypedDict):
    """Type hints for command-list table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Command ID. | Default: 0 | Min: 1 | Max: 255
    type: Literal["non-password", "password"]  # The command type (default = non-password). | Default: non-password
    name: str  # AP local configuration command name. | MaxLen: 63
    value: str  # AP local configuration command value. | MaxLen: 127
    passwd_value: str  # AP local configuration command password value. | MaxLen: 128


# Nested classes for table field children (object mode)

@final
class ApcfgProfileCommandlistObject:
    """Typed object for command-list table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Command ID. | Default: 0 | Min: 1 | Max: 255
    id: int
    # The command type (default = non-password). | Default: non-password
    type: Literal["non-password", "password"]
    # AP local configuration command name. | MaxLen: 63
    name: str
    # AP local configuration command value. | MaxLen: 127
    value: str
    # AP local configuration command password value. | MaxLen: 128
    passwd_value: str
    
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
    def to_dict(self) -> FortiObject: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...



# Response TypedDict for GET returns (all fields present in API response)
class ApcfgProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/apcfg_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # AP local configuration profile name. | MaxLen: 35
    ap_family: Literal["fap", "fap-u", "fap-c"]  # FortiAP family type (default = fap). | Default: fap
    comment: str  # Comment. | MaxLen: 255
    ac_type: Literal["default", "specify", "apcfg"]  # Validation controller type (default = default). | Default: default
    ac_timer: int  # Maximum waiting time for the AP to join the valida | Default: 10 | Min: 3 | Max: 30
    ac_ip: str  # IP address of the validation controller that AP mu | Default: 0.0.0.0
    ac_port: int  # Port of the validation controller that AP must be | Default: 5246 | Min: 1024 | Max: 49150
    command_list: list[ApcfgProfileCommandlistItem]  # AP local configuration command list.


@final
class ApcfgProfileObject:
    """Typed FortiObject for wireless_controller/apcfg_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # AP local configuration profile name. | MaxLen: 35
    name: str
    # FortiAP family type (default = fap). | Default: fap
    ap_family: Literal["fap", "fap-u", "fap-c"]
    # Comment. | MaxLen: 255
    comment: str
    # Validation controller type (default = default). | Default: default
    ac_type: Literal["default", "specify", "apcfg"]
    # Maximum waiting time for the AP to join the validation contr | Default: 10 | Min: 3 | Max: 30
    ac_timer: int
    # IP address of the validation controller that AP must be able | Default: 0.0.0.0
    ac_ip: str
    # Port of the validation controller that AP must be able to jo | Default: 5246 | Min: 1024 | Max: 49150
    ac_port: int
    # AP local configuration command list.
    command_list: list[ApcfgProfileCommandlistObject]
    
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
    def to_dict(self) -> ApcfgProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ApcfgProfile:
    """
    Configure AP local configuration profiles.
    
    Path: wireless_controller/apcfg_profile
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
    ) -> ApcfgProfileObject: ...
    
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
    ) -> ApcfgProfileObject: ...
    
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
    ) -> list[ApcfgProfileObject]: ...
    
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
    ) -> ApcfgProfileObject: ...
    
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
    ) -> ApcfgProfileObject: ...
    
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
    ) -> list[ApcfgProfileObject]: ...
    
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
    ) -> ApcfgProfileObject: ...
    
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
    ) -> ApcfgProfileObject: ...
    
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
    ) -> list[ApcfgProfileObject]: ...
    
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
    ) -> ApcfgProfileObject | list[ApcfgProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ApcfgProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ApcfgProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ApcfgProfileObject: ...
    
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
        payload_dict: ApcfgProfilePayload | None = ...,
        name: str | None = ...,
        ap_family: Literal["fap", "fap-u", "fap-c"] | None = ...,
        comment: str | None = ...,
        ac_type: Literal["default", "specify", "apcfg"] | None = ...,
        ac_timer: int | None = ...,
        ac_ip: str | None = ...,
        ac_port: int | None = ...,
        command_list: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ApcfgProfile",
    "ApcfgProfilePayload",
    "ApcfgProfileResponse",
    "ApcfgProfileObject",
]