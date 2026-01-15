from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ProfilePayload(TypedDict, total=False):
    """
    Type hints for casb/profile payload fields.
    
    Configure CASB profile.
    
    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # CASB profile name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    saas_application: list[dict[str, Any]]  # CASB profile SaaS application.

# Nested TypedDicts for table field children (dict mode)

class ProfileSaasapplicationItem(TypedDict):
    """Type hints for saas-application table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # CASB profile SaaS application name. | MaxLen: 79
    status: Literal["enable", "disable"]  # Enable/disable setting. | Default: enable
    safe_search: Literal["enable", "disable"]  # Enable/disable safe search. | Default: disable
    safe_search_control: str  # CASB profile safe search control.
    tenant_control: Literal["enable", "disable"]  # Enable/disable tenant control. | Default: disable
    tenant_control_tenants: str  # CASB profile tenant control tenants.
    advanced_tenant_control: str  # CASB profile advanced tenant control.
    domain_control: Literal["enable", "disable"]  # Enable/disable domain control. | Default: disable
    domain_control_domains: str  # CASB profile domain control domains.
    log: Literal["enable", "disable"]  # Enable/disable log settings. | Default: enable
    access_rule: str  # CASB profile access rule.
    custom_control: str  # CASB profile custom control.


# Nested classes for table field children (object mode)

@final
class ProfileSaasapplicationObject:
    """Typed object for saas-application table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # CASB profile SaaS application name. | MaxLen: 79
    name: str
    # Enable/disable setting. | Default: enable
    status: Literal["enable", "disable"]
    # Enable/disable safe search. | Default: disable
    safe_search: Literal["enable", "disable"]
    # CASB profile safe search control.
    safe_search_control: str
    # Enable/disable tenant control. | Default: disable
    tenant_control: Literal["enable", "disable"]
    # CASB profile tenant control tenants.
    tenant_control_tenants: str
    # CASB profile advanced tenant control.
    advanced_tenant_control: str
    # Enable/disable domain control. | Default: disable
    domain_control: Literal["enable", "disable"]
    # CASB profile domain control domains.
    domain_control_domains: str
    # Enable/disable log settings. | Default: enable
    log: Literal["enable", "disable"]
    # CASB profile access rule.
    access_rule: str
    # CASB profile custom control.
    custom_control: str
    
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
class ProfileResponse(TypedDict):
    """
    Type hints for casb/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # CASB profile name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    saas_application: list[ProfileSaasapplicationItem]  # CASB profile SaaS application.


@final
class ProfileObject:
    """Typed FortiObject for casb/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # CASB profile name. | MaxLen: 47
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # CASB profile SaaS application.
    saas_application: list[ProfileSaasapplicationObject]
    
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
    def to_dict(self) -> ProfilePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Profile:
    """
    Configure CASB profile.
    
    Path: casb/profile
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> FortiObjectList[ProfileObject]: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> FortiObjectList[ProfileObject]: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> ProfileObject: ...
    
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
    ) -> FortiObjectList[ProfileObject]: ...
    
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
    ) -> ProfileObject | list[ProfileObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        saas_application: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "Profile",
    "ProfilePayload",
    "ProfileResponse",
    "ProfileObject",
]