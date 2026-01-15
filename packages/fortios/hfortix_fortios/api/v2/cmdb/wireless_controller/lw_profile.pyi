from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class LwProfilePayload(TypedDict, total=False):
    """
    Type hints for wireless_controller/lw_profile payload fields.
    
    Configure LoRaWAN profile.
    
    **Usage:**
        payload: LwProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # LoRaWAN profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    lw_protocol: Literal["basics-station", "packet-forwarder"]  # Configure LoRaWAN protocol | Default: basics-station
    cups_server: str  # CUPS (Configuration and Update Server) domain name | MaxLen: 255
    cups_server_port: int  # CUPS Port value of LoRaWAN device. | Default: 0 | Min: 0 | Max: 65535
    cups_api_key: str  # CUPS API key of LoRaWAN device. | MaxLen: 128
    tc_server: str  # TC (Traffic Controller) domain name or IP address | MaxLen: 255
    tc_server_port: int  # TC Port value of LoRaWAN device. | Default: 0 | Min: 0 | Max: 65535
    tc_api_key: str  # TC API key of LoRaWAN device. | MaxLen: 128

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class LwProfileResponse(TypedDict):
    """
    Type hints for wireless_controller/lw_profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # LoRaWAN profile name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 63
    lw_protocol: Literal["basics-station", "packet-forwarder"]  # Configure LoRaWAN protocol | Default: basics-station
    cups_server: str  # CUPS (Configuration and Update Server) domain name | MaxLen: 255
    cups_server_port: int  # CUPS Port value of LoRaWAN device. | Default: 0 | Min: 0 | Max: 65535
    cups_api_key: str  # CUPS API key of LoRaWAN device. | MaxLen: 128
    tc_server: str  # TC (Traffic Controller) domain name or IP address | MaxLen: 255
    tc_server_port: int  # TC Port value of LoRaWAN device. | Default: 0 | Min: 0 | Max: 65535
    tc_api_key: str  # TC API key of LoRaWAN device. | MaxLen: 128


@final
class LwProfileObject:
    """Typed FortiObject for wireless_controller/lw_profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # LoRaWAN profile name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 63
    comment: str
    # Configure LoRaWAN protocol (default = basics-station) | Default: basics-station
    lw_protocol: Literal["basics-station", "packet-forwarder"]
    # CUPS (Configuration and Update Server) domain name or IP add | MaxLen: 255
    cups_server: str
    # CUPS Port value of LoRaWAN device. | Default: 0 | Min: 0 | Max: 65535
    cups_server_port: int
    # CUPS API key of LoRaWAN device. | MaxLen: 128
    cups_api_key: str
    # TC (Traffic Controller) domain name or IP address of LoRaWAN | MaxLen: 255
    tc_server: str
    # TC Port value of LoRaWAN device. | Default: 0 | Min: 0 | Max: 65535
    tc_server_port: int
    # TC API key of LoRaWAN device. | MaxLen: 128
    tc_api_key: str
    
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
    def to_dict(self) -> LwProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class LwProfile:
    """
    Configure LoRaWAN profile.
    
    Path: wireless_controller/lw_profile
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
    ) -> LwProfileObject: ...
    
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
    ) -> LwProfileObject: ...
    
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
    ) -> FortiObjectList[LwProfileObject]: ...
    
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
    ) -> LwProfileObject: ...
    
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
    ) -> LwProfileObject: ...
    
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
    ) -> FortiObjectList[LwProfileObject]: ...
    
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
    ) -> LwProfileObject: ...
    
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
    ) -> LwProfileObject: ...
    
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
    ) -> FortiObjectList[LwProfileObject]: ...
    
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
    ) -> LwProfileObject | list[LwProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LwProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LwProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> LwProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: LwProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        lw_protocol: Literal["basics-station", "packet-forwarder"] | None = ...,
        cups_server: str | None = ...,
        cups_server_port: int | None = ...,
        cups_api_key: str | None = ...,
        tc_server: str | None = ...,
        tc_server_port: int | None = ...,
        tc_api_key: str | None = ...,
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
    "LwProfile",
    "LwProfilePayload",
    "LwProfileResponse",
    "LwProfileObject",
]