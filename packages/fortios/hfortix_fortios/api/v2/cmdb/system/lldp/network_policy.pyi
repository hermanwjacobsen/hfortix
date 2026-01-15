from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class NetworkPolicyPayload(TypedDict, total=False):
    """
    Type hints for system/lldp/network_policy payload fields.
    
    Configure LLDP network policy.
    
    **Usage:**
        payload: NetworkPolicyPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # LLDP network policy name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 1023
    voice: str  # Voice.
    voice_signaling: str  # Voice signaling.
    guest: str  # Guest.
    guest_voice_signaling: str  # Guest Voice Signaling.
    softphone: str  # Softphone.
    video_conferencing: str  # Video Conferencing.
    streaming_video: str  # Streaming Video.
    video_signaling: str  # Video Signaling.

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class NetworkPolicyResponse(TypedDict):
    """
    Type hints for system/lldp/network_policy API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # LLDP network policy name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 1023
    voice: str  # Voice.
    voice_signaling: str  # Voice signaling.
    guest: str  # Guest.
    guest_voice_signaling: str  # Guest Voice Signaling.
    softphone: str  # Softphone.
    video_conferencing: str  # Video Conferencing.
    streaming_video: str  # Streaming Video.
    video_signaling: str  # Video Signaling.


@final
class NetworkPolicyObject:
    """Typed FortiObject for system/lldp/network_policy with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # LLDP network policy name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 1023
    comment: str
    # Voice.
    voice: str
    # Voice signaling.
    voice_signaling: str
    # Guest.
    guest: str
    # Guest Voice Signaling.
    guest_voice_signaling: str
    # Softphone.
    softphone: str
    # Video Conferencing.
    video_conferencing: str
    # Streaming Video.
    streaming_video: str
    # Video Signaling.
    video_signaling: str
    
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
    def to_dict(self) -> NetworkPolicyPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class NetworkPolicy:
    """
    Configure LLDP network policy.
    
    Path: system/lldp/network_policy
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
    ) -> NetworkPolicyObject: ...
    
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
    ) -> NetworkPolicyObject: ...
    
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
    ) -> list[NetworkPolicyObject]: ...
    
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
    ) -> NetworkPolicyObject: ...
    
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
    ) -> NetworkPolicyObject: ...
    
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
    ) -> list[NetworkPolicyObject]: ...
    
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
    ) -> NetworkPolicyObject: ...
    
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
    ) -> NetworkPolicyObject: ...
    
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
    ) -> list[NetworkPolicyObject]: ...
    
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
    ) -> NetworkPolicyObject | list[NetworkPolicyObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> NetworkPolicyObject: ...
    
    @overload
    def post(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> NetworkPolicyObject: ...
    
    @overload
    def put(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
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
    ) -> NetworkPolicyObject: ...
    
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
        payload_dict: NetworkPolicyPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        voice: str | None = ...,
        voice_signaling: str | None = ...,
        guest: str | None = ...,
        guest_voice_signaling: str | None = ...,
        softphone: str | None = ...,
        video_conferencing: str | None = ...,
        streaming_video: str | None = ...,
        video_signaling: str | None = ...,
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
    "NetworkPolicy",
    "NetworkPolicyPayload",
    "NetworkPolicyResponse",
    "NetworkPolicyObject",
]