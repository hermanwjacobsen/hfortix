from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ThreatWeightPayload(TypedDict, total=False):
    """
    Type hints for log/threat_weight payload fields.
    
    Configure threat weight settings.
    
    **Usage:**
        payload: ThreatWeightPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    status: Literal["enable", "disable"]  # Enable/disable the threat weight feature. | Default: enable
    level: str  # Score mapping for threat weight levels.
    blocked_connection: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for blocked connections. | Default: high
    failed_connection: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for failed connections. | Default: low
    url_block_detected: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for URL blocking. | Default: high
    botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for detected botnet connection | Default: critical
    malware: str  # Anti-virus malware threat weight settings.
    ips: str  # IPS threat weight settings.
    web: list[dict[str, Any]]  # Web filtering threat weight settings.
    geolocation: list[dict[str, Any]]  # Geolocation-based threat weight settings.
    application: list[dict[str, Any]]  # Application-control threat weight settings.

# Nested TypedDicts for table field children (dict mode)

class ThreatWeightWebItem(TypedDict):
    """Type hints for web table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 255
    category: int  # Threat weight score for web category filtering mat | Default: 0 | Min: 0 | Max: 255
    level: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for web category filtering mat | Default: low


class ThreatWeightGeolocationItem(TypedDict):
    """Type hints for geolocation table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 255
    country: str  # Country code. | MaxLen: 2
    level: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for Geolocation-based events. | Default: low


class ThreatWeightApplicationItem(TypedDict):
    """Type hints for application table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # Entry ID. | Default: 0 | Min: 0 | Max: 255
    category: int  # Application category. | Default: 0 | Min: 0 | Max: 65535
    level: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for Application events. | Default: low


# Nested classes for table field children (object mode)

@final
class ThreatWeightWebObject:
    """Typed object for web table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 255
    id: int
    # Threat weight score for web category filtering matches. | Default: 0 | Min: 0 | Max: 255
    category: int
    # Threat weight score for web category filtering matches. | Default: low
    level: Literal["disable", "low", "medium", "high", "critical"]
    
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


@final
class ThreatWeightGeolocationObject:
    """Typed object for geolocation table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 255
    id: int
    # Country code. | MaxLen: 2
    country: str
    # Threat weight score for Geolocation-based events. | Default: low
    level: Literal["disable", "low", "medium", "high", "critical"]
    
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


@final
class ThreatWeightApplicationObject:
    """Typed object for application table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Entry ID. | Default: 0 | Min: 0 | Max: 255
    id: int
    # Application category. | Default: 0 | Min: 0 | Max: 65535
    category: int
    # Threat weight score for Application events. | Default: low
    level: Literal["disable", "low", "medium", "high", "critical"]
    
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
class ThreatWeightResponse(TypedDict):
    """
    Type hints for log/threat_weight API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    status: Literal["enable", "disable"]  # Enable/disable the threat weight feature. | Default: enable
    level: str  # Score mapping for threat weight levels.
    blocked_connection: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for blocked connections. | Default: high
    failed_connection: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for failed connections. | Default: low
    url_block_detected: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for URL blocking. | Default: high
    botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"]  # Threat weight score for detected botnet connection | Default: critical
    malware: str  # Anti-virus malware threat weight settings.
    ips: str  # IPS threat weight settings.
    web: list[ThreatWeightWebItem]  # Web filtering threat weight settings.
    geolocation: list[ThreatWeightGeolocationItem]  # Geolocation-based threat weight settings.
    application: list[ThreatWeightApplicationItem]  # Application-control threat weight settings.


@final
class ThreatWeightObject:
    """Typed FortiObject for log/threat_weight with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable the threat weight feature. | Default: enable
    status: Literal["enable", "disable"]
    # Score mapping for threat weight levels.
    level: str
    # Threat weight score for blocked connections. | Default: high
    blocked_connection: Literal["disable", "low", "medium", "high", "critical"]
    # Threat weight score for failed connections. | Default: low
    failed_connection: Literal["disable", "low", "medium", "high", "critical"]
    # Threat weight score for URL blocking. | Default: high
    url_block_detected: Literal["disable", "low", "medium", "high", "critical"]
    # Threat weight score for detected botnet connections. | Default: critical
    botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"]
    # Anti-virus malware threat weight settings.
    malware: str
    # IPS threat weight settings.
    ips: str
    # Web filtering threat weight settings.
    web: list[ThreatWeightWebObject]
    # Geolocation-based threat weight settings.
    geolocation: list[ThreatWeightGeolocationObject]
    # Application-control threat weight settings.
    application: list[ThreatWeightApplicationObject]
    
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
    def to_dict(self) -> ThreatWeightPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ThreatWeight:
    """
    Configure threat weight settings.
    
    Path: log/threat_weight
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject: ...
    
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
    ) -> ThreatWeightObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ThreatWeightObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ThreatWeightPayload | None = ...,
        status: Literal["enable", "disable"] | None = ...,
        level: str | None = ...,
        blocked_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        failed_connection: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        url_block_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        botnet_connection_detected: Literal["disable", "low", "medium", "high", "critical"] | None = ...,
        malware: str | None = ...,
        ips: str | None = ...,
        web: str | list[str] | list[dict[str, Any]] | None = ...,
        geolocation: str | list[str] | list[dict[str, Any]] | None = ...,
        application: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ThreatWeight",
    "ThreatWeightPayload",
    "ThreatWeightResponse",
    "ThreatWeightObject",
]