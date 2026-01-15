from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class AutoInstallPayload(TypedDict, total=False):
    """
    Type hints for system/auto_install payload fields.
    
    Configure USB auto installation.
    
    **Usage:**
        payload: AutoInstallPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    auto_install_config: Literal["enable", "disable"]  # Enable/disable auto install the config in USB disk | Default: disable
    auto_install_image: Literal["enable", "disable"]  # Enable/disable auto install the image in USB disk. | Default: disable
    default_config_file: str  # Default config file name in USB disk. | Default: fgt_system.conf | MaxLen: 127
    default_image_file: str  # Default image file name in USB disk. | Default: image.out | MaxLen: 127

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class AutoInstallResponse(TypedDict):
    """
    Type hints for system/auto_install API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    auto_install_config: Literal["enable", "disable"]  # Enable/disable auto install the config in USB disk | Default: disable
    auto_install_image: Literal["enable", "disable"]  # Enable/disable auto install the image in USB disk. | Default: disable
    default_config_file: str  # Default config file name in USB disk. | Default: fgt_system.conf | MaxLen: 127
    default_image_file: str  # Default image file name in USB disk. | Default: image.out | MaxLen: 127


@final
class AutoInstallObject:
    """Typed FortiObject for system/auto_install with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable auto install the config in USB disk. | Default: disable
    auto_install_config: Literal["enable", "disable"]
    # Enable/disable auto install the image in USB disk. | Default: disable
    auto_install_image: Literal["enable", "disable"]
    # Default config file name in USB disk. | Default: fgt_system.conf | MaxLen: 127
    default_config_file: str
    # Default image file name in USB disk. | Default: image.out | MaxLen: 127
    default_image_file: str
    
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
    def to_dict(self) -> AutoInstallPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class AutoInstall:
    """
    Configure USB auto installation.
    
    Path: system/auto_install
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject: ...
    
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
    ) -> AutoInstallObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: AutoInstallPayload | None = ...,
        auto_install_config: Literal["enable", "disable"] | None = ...,
        auto_install_image: Literal["enable", "disable"] | None = ...,
        default_config_file: str | None = ...,
        default_image_file: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> AutoInstallObject: ...
    
    @overload
    def put(
        self,
        payload_dict: AutoInstallPayload | None = ...,
        auto_install_config: Literal["enable", "disable"] | None = ...,
        auto_install_image: Literal["enable", "disable"] | None = ...,
        default_config_file: str | None = ...,
        default_image_file: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: AutoInstallPayload | None = ...,
        auto_install_config: Literal["enable", "disable"] | None = ...,
        auto_install_image: Literal["enable", "disable"] | None = ...,
        default_config_file: str | None = ...,
        default_image_file: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: AutoInstallPayload | None = ...,
        auto_install_config: Literal["enable", "disable"] | None = ...,
        auto_install_image: Literal["enable", "disable"] | None = ...,
        default_config_file: str | None = ...,
        default_image_file: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: AutoInstallPayload | None = ...,
        auto_install_config: Literal["enable", "disable"] | None = ...,
        auto_install_image: Literal["enable", "disable"] | None = ...,
        default_config_file: str | None = ...,
        default_image_file: str | None = ...,
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
    "AutoInstall",
    "AutoInstallPayload",
    "AutoInstallResponse",
    "AutoInstallObject",
]