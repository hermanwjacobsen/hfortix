from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class X8021xSettingsPayload(TypedDict, total=False):
    """
    Type hints for switch_controller/x802_1x_settings payload fields.
    
    Configure global 802.1X settings.
    
    **Usage:**
        payload: X8021xSettingsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    link_down_auth: Literal["set-unauth", "no-action"]  # Interface-reauthentication state to set if a link | Default: set-unauth
    reauth_period: int  # Period of time to allow for reauthentication | Default: 60 | Min: 0 | Max: 1440
    max_reauth_attempt: int  # Maximum number of authentication attempts | Default: 3 | Min: 0 | Max: 15
    tx_period: int  # 802.1X Tx period (seconds, default=30). | Default: 30 | Min: 12 | Max: 60
    mab_reauth: Literal["disable", "enable"]  # Enable/disable MAB re-authentication. | Default: disable
    mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]  # MAC authentication username delimiter | Default: hyphen
    mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]  # MAC authentication password delimiter | Default: hyphen
    mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]  # MAC calling station delimiter (default = hyphen). | Default: hyphen
    mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]  # MAC called station delimiter (default = hyphen). | Default: hyphen
    mac_case: Literal["lowercase", "uppercase"]  # MAC case (default = lowercase). | Default: lowercase

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class X8021xSettingsResponse(TypedDict):
    """
    Type hints for switch_controller/x802_1x_settings API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    link_down_auth: Literal["set-unauth", "no-action"]  # Interface-reauthentication state to set if a link | Default: set-unauth
    reauth_period: int  # Period of time to allow for reauthentication | Default: 60 | Min: 0 | Max: 1440
    max_reauth_attempt: int  # Maximum number of authentication attempts | Default: 3 | Min: 0 | Max: 15
    tx_period: int  # 802.1X Tx period (seconds, default=30). | Default: 30 | Min: 12 | Max: 60
    mab_reauth: Literal["disable", "enable"]  # Enable/disable MAB re-authentication. | Default: disable
    mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]  # MAC authentication username delimiter | Default: hyphen
    mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]  # MAC authentication password delimiter | Default: hyphen
    mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]  # MAC calling station delimiter (default = hyphen). | Default: hyphen
    mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]  # MAC called station delimiter (default = hyphen). | Default: hyphen
    mac_case: Literal["lowercase", "uppercase"]  # MAC case (default = lowercase). | Default: lowercase


@final
class X8021xSettingsObject:
    """Typed FortiObject for switch_controller/x802_1x_settings with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Interface-reauthentication state to set if a link is down. | Default: set-unauth
    link_down_auth: Literal["set-unauth", "no-action"]
    # Period of time to allow for reauthentication | Default: 60 | Min: 0 | Max: 1440
    reauth_period: int
    # Maximum number of authentication attempts | Default: 3 | Min: 0 | Max: 15
    max_reauth_attempt: int
    # 802.1X Tx period (seconds, default=30). | Default: 30 | Min: 12 | Max: 60
    tx_period: int
    # Enable/disable MAB re-authentication. | Default: disable
    mab_reauth: Literal["disable", "enable"]
    # MAC authentication username delimiter (default = hyphen). | Default: hyphen
    mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    # MAC authentication password delimiter (default = hyphen). | Default: hyphen
    mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    # MAC calling station delimiter (default = hyphen). | Default: hyphen
    mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    # MAC called station delimiter (default = hyphen). | Default: hyphen
    mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"]
    # MAC case (default = lowercase). | Default: lowercase
    mac_case: Literal["lowercase", "uppercase"]
    
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
    def to_dict(self) -> X8021xSettingsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class X8021xSettings:
    """
    Configure global 802.1X settings.
    
    Path: switch_controller/x802_1x_settings
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject: ...
    
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
    ) -> X8021xSettingsObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> X8021xSettingsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: X8021xSettingsPayload | None = ...,
        link_down_auth: Literal["set-unauth", "no-action"] | None = ...,
        reauth_period: int | None = ...,
        max_reauth_attempt: int | None = ...,
        tx_period: int | None = ...,
        mab_reauth: Literal["disable", "enable"] | None = ...,
        mac_username_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_password_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_calling_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_called_station_delimiter: Literal["colon", "hyphen", "none", "single-hyphen"] | None = ...,
        mac_case: Literal["lowercase", "uppercase"] | None = ...,
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
    "X8021xSettings",
    "X8021xSettingsPayload",
    "X8021xSettingsResponse",
    "X8021xSettingsObject",
]