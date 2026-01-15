from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingsPayload(TypedDict, total=False):
    """
    Type hints for dlp/settings payload fields.
    
    Configure settings for DLP.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.storage.StorageEndpoint` (via: storage-device)

    **Usage:**
        payload: SettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    storage_device: str  # Storage device name. | MaxLen: 35
    size: int  # Maximum total size of files within the DLP fingerp | Default: 16 | Min: 16 | Max: 4294967295
    db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"]  # Behavior when the maximum size is reached in the D | Default: stop-adding
    cache_mem_percent: int  # Maximum percentage of available memory allocated t | Default: 2 | Min: 1 | Max: 15
    chunk_size: int  # Maximum fingerprint chunk size. Caution, changing | Default: 2800 | Min: 100 | Max: 100000
    config_builder_timeout: int  # Maximum time allowed for building a single DLP pro | Default: 60 | Min: 10 | Max: 100000

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class SettingsResponse(TypedDict):
    """
    Type hints for dlp/settings API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    storage_device: str  # Storage device name. | MaxLen: 35
    size: int  # Maximum total size of files within the DLP fingerp | Default: 16 | Min: 16 | Max: 4294967295
    db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"]  # Behavior when the maximum size is reached in the D | Default: stop-adding
    cache_mem_percent: int  # Maximum percentage of available memory allocated t | Default: 2 | Min: 1 | Max: 15
    chunk_size: int  # Maximum fingerprint chunk size. Caution, changing | Default: 2800 | Min: 100 | Max: 100000
    config_builder_timeout: int  # Maximum time allowed for building a single DLP pro | Default: 60 | Min: 10 | Max: 100000


@final
class SettingsObject:
    """Typed FortiObject for dlp/settings with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Storage device name. | MaxLen: 35
    storage_device: str
    # Maximum total size of files within the DLP fingerprint datab | Default: 16 | Min: 16 | Max: 4294967295
    size: int
    # Behavior when the maximum size is reached in the DLP fingerp | Default: stop-adding
    db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"]
    # Maximum percentage of available memory allocated to caching | Default: 2 | Min: 1 | Max: 15
    cache_mem_percent: int
    # Maximum fingerprint chunk size. Caution, changing this setti | Default: 2800 | Min: 100 | Max: 100000
    chunk_size: int
    # Maximum time allowed for building a single DLP profile | Default: 60 | Min: 10 | Max: 100000
    config_builder_timeout: int
    
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
    def to_dict(self) -> SettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Settings:
    """
    Configure settings for DLP.
    
    Path: dlp/settings
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject: ...
    
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
    ) -> SettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SettingsPayload | None = ...,
        storage_device: str | None = ...,
        size: int | None = ...,
        db_mode: Literal["stop-adding", "remove-modified-then-oldest", "remove-oldest"] | None = ...,
        cache_mem_percent: int | None = ...,
        chunk_size: int | None = ...,
        config_builder_timeout: int | None = ...,
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
    "Settings",
    "SettingsPayload",
    "SettingsResponse",
    "SettingsObject",
]