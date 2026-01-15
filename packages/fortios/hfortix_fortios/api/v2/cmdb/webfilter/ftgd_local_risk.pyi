from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class FtgdLocalRiskPayload(TypedDict, total=False):
    """
    Type hints for webfilter/ftgd_local_risk payload fields.
    
    Configure FortiGuard Web Filter local risk score.
    
    **Usage:**
        payload: FtgdLocalRiskPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    url: str  # URL to rate locally. | MaxLen: 511
    status: Literal["enable", "disable"]  # Enable/disable local risk score. | Default: enable
    comment: str  # Comment. | MaxLen: 255
    risk_score: int  # Local risk score. | Default: 0 | Min: 0 | Max: 100

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class FtgdLocalRiskResponse(TypedDict):
    """
    Type hints for webfilter/ftgd_local_risk API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    url: str  # URL to rate locally. | MaxLen: 511
    status: Literal["enable", "disable"]  # Enable/disable local risk score. | Default: enable
    comment: str  # Comment. | MaxLen: 255
    risk_score: int  # Local risk score. | Default: 0 | Min: 0 | Max: 100


@final
class FtgdLocalRiskObject:
    """Typed FortiObject for webfilter/ftgd_local_risk with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # URL to rate locally. | MaxLen: 511
    url: str
    # Enable/disable local risk score. | Default: enable
    status: Literal["enable", "disable"]
    # Comment. | MaxLen: 255
    comment: str
    # Local risk score. | Default: 0 | Min: 0 | Max: 100
    risk_score: int
    
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
    def to_dict(self) -> FtgdLocalRiskPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class FtgdLocalRisk:
    """
    Configure FortiGuard Web Filter local risk score.
    
    Path: webfilter/ftgd_local_risk
    Category: cmdb
    Primary Key: url
    """
    
    # ================================================================
    # GET OVERLOADS - Always returns FortiObject
    # Pylance matches overloads top-to-bottom, so these must come first!
    # ================================================================
    
    # With mkey as positional arg -> returns FortiObject
    @overload
    def get(
        self,
        url: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
    # With mkey as keyword arg -> returns FortiObject
    @overload
    def get(
        self,
        *,
        url: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
    # Without mkey -> returns list of FortiObjects
    @overload
    def get(
        self,
        url: None = None,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObjectList[FtgdLocalRiskObject]: ...
    
    # ================================================================
    # (removed - all GET now returns FortiObject)
    # ================================================================
    
    # With mkey as positional arg -> returns single object
    @overload
    def get(
        self,
        url: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
    # With mkey as keyword arg -> returns single object
    @overload
    def get(
        self,
        *,
        url: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
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
    ) -> FortiObjectList[FtgdLocalRiskObject]: ...
    
    # Dict mode with mkey provided as positional arg (single dict)
    @overload
    def get(
        self,
        url: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
    # Dict mode with mkey provided as keyword arg (single dict)
    @overload
    def get(
        self,
        *,
        url: str,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
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
    ) -> FortiObjectList[FtgdLocalRiskObject]: ...
    
    # Fallback overload for all other cases
    @overload
    def get(
        self,
        url: str | None = ...,
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
        url: str | None = ...,
        filter: str | list[str] | None = ...,
        count: int | None = ...,
        start: int | None = ...,
        payload_dict: dict[str, Any] | None = ...,
        range: list[int] | None = ...,
        sort: str | None = ...,
        format: str | None = ...,
        action: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject | list[FtgdLocalRiskObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
    @overload
    def post(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
    @overload
    def put(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        url: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FtgdLocalRiskObject: ...
    
    @overload
    def delete(
        self,
        url: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        url: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        url: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        url: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: FtgdLocalRiskPayload | None = ...,
        url: str | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        comment: str | None = ...,
        risk_score: int | None = ...,
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
    "FtgdLocalRisk",
    "FtgdLocalRiskPayload",
    "FtgdLocalRiskResponse",
    "FtgdLocalRiskObject",
]