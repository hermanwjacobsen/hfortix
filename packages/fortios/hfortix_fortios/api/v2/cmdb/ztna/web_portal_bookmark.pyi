from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class WebPortalBookmarkPayload(TypedDict, total=False):
    """
    Type hints for ztna/web_portal_bookmark payload fields.
    
    Configure ztna web-portal bookmark.
    
    **Usage:**
        payload: WebPortalBookmarkPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Bookmark name. | MaxLen: 35
    users: list[dict[str, Any]]  # User name.
    groups: list[dict[str, Any]]  # User groups.
    bookmarks: list[dict[str, Any]]  # Bookmark table.

# Nested TypedDicts for table field children (dict mode)

class WebPortalBookmarkUsersItem(TypedDict):
    """Type hints for users table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # User name. | MaxLen: 79


class WebPortalBookmarkGroupsItem(TypedDict):
    """Type hints for groups table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Group name. | MaxLen: 79


class WebPortalBookmarkBookmarksItem(TypedDict):
    """Type hints for bookmarks table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Bookmark name. | MaxLen: 35
    apptype: Literal["ftp", "rdp", "sftp", "smb", "ssh", "telnet", "vnc", "web"]  # Application type. | Default: web
    url: str  # URL parameter. | MaxLen: 128
    host: str  # Host name/IP parameter. | MaxLen: 128
    folder: str  # Network shared file folder parameter. | MaxLen: 128
    domain: str  # Login domain. | MaxLen: 128
    description: str  # Description. | MaxLen: 128
    keyboard_layout: Literal["ar-101", "ar-102", "ar-102-azerty", "can-mul", "cz", "cz-qwerty", "cz-pr", "da", "nl", "de", "de-ch", "de-ibm", "en-uk", "en-uk-ext", "en-us", "en-us-dvorak", "es", "es-var", "fi", "fi-sami", "fr", "fr-apple", "fr-ca", "fr-ch", "fr-be", "hr", "hu", "hu-101", "it", "it-142", "ja", "ja-106", "ko", "la-am", "lt", "lt-ibm", "lt-std", "lav-std", "lav-leg", "mk", "mk-std", "no", "no-sami", "pol-214", "pol-pr", "pt", "pt-br", "pt-br-abnt2", "ru", "ru-mne", "ru-t", "sl", "sv", "sv-sami", "tuk", "tur-f", "tur-q", "zh-sym-sg-us", "zh-sym-us", "zh-tr-hk", "zh-tr-mo", "zh-tr-us"]  # Keyboard layout. | Default: en-us
    security: Literal["any", "rdp", "nla", "tls"]  # Security mode for RDP connection (default = any). | Default: any
    send_preconnection_id: Literal["enable", "disable"]  # Enable/disable sending of preconnection ID. | Default: disable
    preconnection_id: int  # The numeric ID of the RDP source (0-4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    preconnection_blob: str  # An arbitrary string which identifies the RDP sourc | MaxLen: 511
    load_balancing_info: str  # The load balancing information or cookie which sho | MaxLen: 511
    restricted_admin: Literal["enable", "disable"]  # Enable/disable restricted admin mode for RDP. | Default: disable
    port: int  # Remote port. | Default: 0 | Min: 0 | Max: 65535
    logon_user: str  # Logon user. | MaxLen: 35
    logon_password: str  # Logon password. | MaxLen: 128
    color_depth: Literal["32", "16", "8"]  # Color depth per pixel. | Default: 16
    sso: Literal["disable", "enable"]  # Single sign-on. | Default: disable
    width: int  # Screen width (range from 0 - 65535, default = 0). | Default: 0 | Min: 0 | Max: 65535
    height: int  # Screen height (range from 0 - 65535, default = 0). | Default: 0 | Min: 0 | Max: 65535
    vnc_keyboard_layout: Literal["default", "da", "nl", "en-uk", "en-uk-ext", "fi", "fr", "fr-be", "fr-ca-mul", "de", "de-ch", "it", "it-142", "pt", "pt-br-abnt2", "no", "gd", "es", "sv", "us-intl"]  # Keyboard layout. | Default: default


# Nested classes for table field children (object mode)

@final
class WebPortalBookmarkUsersObject:
    """Typed object for users table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # User name. | MaxLen: 79
    name: str
    
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
class WebPortalBookmarkGroupsObject:
    """Typed object for groups table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Group name. | MaxLen: 79
    name: str
    
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
class WebPortalBookmarkBookmarksObject:
    """Typed object for bookmarks table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Bookmark name. | MaxLen: 35
    name: str
    # Application type. | Default: web
    apptype: Literal["ftp", "rdp", "sftp", "smb", "ssh", "telnet", "vnc", "web"]
    # URL parameter. | MaxLen: 128
    url: str
    # Host name/IP parameter. | MaxLen: 128
    host: str
    # Network shared file folder parameter. | MaxLen: 128
    folder: str
    # Login domain. | MaxLen: 128
    domain: str
    # Description. | MaxLen: 128
    description: str
    # Keyboard layout. | Default: en-us
    keyboard_layout: Literal["ar-101", "ar-102", "ar-102-azerty", "can-mul", "cz", "cz-qwerty", "cz-pr", "da", "nl", "de", "de-ch", "de-ibm", "en-uk", "en-uk-ext", "en-us", "en-us-dvorak", "es", "es-var", "fi", "fi-sami", "fr", "fr-apple", "fr-ca", "fr-ch", "fr-be", "hr", "hu", "hu-101", "it", "it-142", "ja", "ja-106", "ko", "la-am", "lt", "lt-ibm", "lt-std", "lav-std", "lav-leg", "mk", "mk-std", "no", "no-sami", "pol-214", "pol-pr", "pt", "pt-br", "pt-br-abnt2", "ru", "ru-mne", "ru-t", "sl", "sv", "sv-sami", "tuk", "tur-f", "tur-q", "zh-sym-sg-us", "zh-sym-us", "zh-tr-hk", "zh-tr-mo", "zh-tr-us"]
    # Security mode for RDP connection (default = any). | Default: any
    security: Literal["any", "rdp", "nla", "tls"]
    # Enable/disable sending of preconnection ID. | Default: disable
    send_preconnection_id: Literal["enable", "disable"]
    # The numeric ID of the RDP source (0-4294967295). | Default: 0 | Min: 0 | Max: 4294967295
    preconnection_id: int
    # An arbitrary string which identifies the RDP source. | MaxLen: 511
    preconnection_blob: str
    # The load balancing information or cookie which should be pro | MaxLen: 511
    load_balancing_info: str
    # Enable/disable restricted admin mode for RDP. | Default: disable
    restricted_admin: Literal["enable", "disable"]
    # Remote port. | Default: 0 | Min: 0 | Max: 65535
    port: int
    # Logon user. | MaxLen: 35
    logon_user: str
    # Logon password. | MaxLen: 128
    logon_password: str
    # Color depth per pixel. | Default: 16
    color_depth: Literal["32", "16", "8"]
    # Single sign-on. | Default: disable
    sso: Literal["disable", "enable"]
    # Screen width (range from 0 - 65535, default = 0). | Default: 0 | Min: 0 | Max: 65535
    width: int
    # Screen height (range from 0 - 65535, default = 0). | Default: 0 | Min: 0 | Max: 65535
    height: int
    # Keyboard layout. | Default: default
    vnc_keyboard_layout: Literal["default", "da", "nl", "en-uk", "en-uk-ext", "fi", "fr", "fr-be", "fr-ca-mul", "de", "de-ch", "it", "it-142", "pt", "pt-br-abnt2", "no", "gd", "es", "sv", "us-intl"]
    
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
class WebPortalBookmarkResponse(TypedDict):
    """
    Type hints for ztna/web_portal_bookmark API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Bookmark name. | MaxLen: 35
    users: list[WebPortalBookmarkUsersItem]  # User name.
    groups: list[WebPortalBookmarkGroupsItem]  # User groups.
    bookmarks: list[WebPortalBookmarkBookmarksItem]  # Bookmark table.


@final
class WebPortalBookmarkObject:
    """Typed FortiObject for ztna/web_portal_bookmark with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Bookmark name. | MaxLen: 35
    name: str
    # User name.
    users: list[WebPortalBookmarkUsersObject]
    # User groups.
    groups: list[WebPortalBookmarkGroupsObject]
    # Bookmark table.
    bookmarks: list[WebPortalBookmarkBookmarksObject]
    
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
    def to_dict(self) -> WebPortalBookmarkPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class WebPortalBookmark:
    """
    Configure ztna web-portal bookmark.
    
    Path: ztna/web_portal_bookmark
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
    ) -> WebPortalBookmarkObject: ...
    
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
    ) -> WebPortalBookmarkObject: ...
    
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
    ) -> FortiObjectList[WebPortalBookmarkObject]: ...
    
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
    ) -> WebPortalBookmarkObject: ...
    
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
    ) -> WebPortalBookmarkObject: ...
    
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
    ) -> FortiObjectList[WebPortalBookmarkObject]: ...
    
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
    ) -> WebPortalBookmarkObject: ...
    
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
    ) -> WebPortalBookmarkObject: ...
    
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
    ) -> FortiObjectList[WebPortalBookmarkObject]: ...
    
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
    ) -> WebPortalBookmarkObject | list[WebPortalBookmarkObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> WebPortalBookmarkObject: ...
    
    @overload
    def post(
        self,
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> WebPortalBookmarkObject: ...
    
    @overload
    def put(
        self,
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> WebPortalBookmarkObject: ...
    
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
        payload_dict: WebPortalBookmarkPayload | None = ...,
        name: str | None = ...,
        users: str | list[str] | list[dict[str, Any]] | None = ...,
        groups: str | list[str] | list[dict[str, Any]] | None = ...,
        bookmarks: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "WebPortalBookmark",
    "WebPortalBookmarkPayload",
    "WebPortalBookmarkResponse",
    "WebPortalBookmarkObject",
]