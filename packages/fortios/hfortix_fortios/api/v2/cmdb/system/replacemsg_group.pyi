from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject
from hfortix_core.types import MutationResponse, RawAPIResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ReplacemsgGroupPayload(TypedDict, total=False):
    """
    Type hints for system/replacemsg_group payload fields.
    
    Configure replacement message groups.
    
    **Usage:**
        payload: ReplacemsgGroupPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Group name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    group_type: Literal["default", "utm", "auth"]  # Group type. | Default: default
    mail: list[dict[str, Any]]  # Replacement message table entries.
    http: list[dict[str, Any]]  # Replacement message table entries.
    webproxy: list[dict[str, Any]]  # Replacement message table entries.
    ftp: list[dict[str, Any]]  # Replacement message table entries.
    fortiguard_wf: list[dict[str, Any]]  # Replacement message table entries.
    spam: list[dict[str, Any]]  # Replacement message table entries.
    alertmail: list[dict[str, Any]]  # Replacement message table entries.
    admin: list[dict[str, Any]]  # Replacement message table entries.
    auth: list[dict[str, Any]]  # Replacement message table entries.
    sslvpn: list[dict[str, Any]]  # Replacement message table entries.
    nac_quar: list[dict[str, Any]]  # Replacement message table entries.
    traffic_quota: list[dict[str, Any]]  # Replacement message table entries.
    utm: list[dict[str, Any]]  # Replacement message table entries.
    custom_message: list[dict[str, Any]]  # Replacement message table entries.
    icap: list[dict[str, Any]]  # Replacement message table entries.
    automation: list[dict[str, Any]]  # Replacement message table entries.

# Nested TypedDicts for table field children (dict mode)

class ReplacemsgGroupMailItem(TypedDict):
    """Type hints for mail table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupHttpItem(TypedDict):
    """Type hints for http table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupWebproxyItem(TypedDict):
    """Type hints for webproxy table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupFtpItem(TypedDict):
    """Type hints for ftp table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupFortiguardwfItem(TypedDict):
    """Type hints for fortiguard-wf table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupSpamItem(TypedDict):
    """Type hints for spam table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupAlertmailItem(TypedDict):
    """Type hints for alertmail table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupAdminItem(TypedDict):
    """Type hints for admin table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupAuthItem(TypedDict):
    """Type hints for auth table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupSslvpnItem(TypedDict):
    """Type hints for sslvpn table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupNacquarItem(TypedDict):
    """Type hints for nac-quar table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupTrafficquotaItem(TypedDict):
    """Type hints for traffic-quota table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupUtmItem(TypedDict):
    """Type hints for utm table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupCustommessageItem(TypedDict):
    """Type hints for custom-message table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupIcapItem(TypedDict):
    """Type hints for icap table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


class ReplacemsgGroupAutomationItem(TypedDict):
    """Type hints for automation table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    msg_type: str  # Message type. | MaxLen: 28
    buffer: str  # Message string. | MaxLen: 32768
    header: Literal["none", "http", "8bit"]  # Header flag. | Default: none
    format: Literal["none", "text", "html"]  # Format flag. | Default: none


# Nested classes for table field children (object mode)

@final
class ReplacemsgGroupMailObject:
    """Typed object for mail table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupHttpObject:
    """Typed object for http table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupWebproxyObject:
    """Typed object for webproxy table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupFtpObject:
    """Typed object for ftp table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupFortiguardwfObject:
    """Typed object for fortiguard-wf table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupSpamObject:
    """Typed object for spam table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupAlertmailObject:
    """Typed object for alertmail table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupAdminObject:
    """Typed object for admin table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupAuthObject:
    """Typed object for auth table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupSslvpnObject:
    """Typed object for sslvpn table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupNacquarObject:
    """Typed object for nac-quar table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupTrafficquotaObject:
    """Typed object for traffic-quota table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupUtmObject:
    """Typed object for utm table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupCustommessageObject:
    """Typed object for custom-message table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupIcapObject:
    """Typed object for icap table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupAutomationObject:
    """Typed object for automation table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Message type. | MaxLen: 28
    msg_type: str
    # Message string. | MaxLen: 32768
    buffer: str
    # Header flag. | Default: none
    header: Literal["none", "http", "8bit"]
    # Format flag. | Default: none
    format: Literal["none", "text", "html"]
    
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
class ReplacemsgGroupResponse(TypedDict):
    """
    Type hints for system/replacemsg_group API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Group name. | MaxLen: 35
    comment: str  # Comment. | MaxLen: 255
    group_type: Literal["default", "utm", "auth"]  # Group type. | Default: default
    mail: list[ReplacemsgGroupMailItem]  # Replacement message table entries.
    http: list[ReplacemsgGroupHttpItem]  # Replacement message table entries.
    webproxy: list[ReplacemsgGroupWebproxyItem]  # Replacement message table entries.
    ftp: list[ReplacemsgGroupFtpItem]  # Replacement message table entries.
    fortiguard_wf: list[ReplacemsgGroupFortiguardwfItem]  # Replacement message table entries.
    spam: list[ReplacemsgGroupSpamItem]  # Replacement message table entries.
    alertmail: list[ReplacemsgGroupAlertmailItem]  # Replacement message table entries.
    admin: list[ReplacemsgGroupAdminItem]  # Replacement message table entries.
    auth: list[ReplacemsgGroupAuthItem]  # Replacement message table entries.
    sslvpn: list[ReplacemsgGroupSslvpnItem]  # Replacement message table entries.
    nac_quar: list[ReplacemsgGroupNacquarItem]  # Replacement message table entries.
    traffic_quota: list[ReplacemsgGroupTrafficquotaItem]  # Replacement message table entries.
    utm: list[ReplacemsgGroupUtmItem]  # Replacement message table entries.
    custom_message: list[ReplacemsgGroupCustommessageItem]  # Replacement message table entries.
    icap: list[ReplacemsgGroupIcapItem]  # Replacement message table entries.
    automation: list[ReplacemsgGroupAutomationItem]  # Replacement message table entries.


@final
class ReplacemsgGroupObject:
    """Typed FortiObject for system/replacemsg_group with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Group name. | MaxLen: 35
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Group type. | Default: default
    group_type: Literal["default", "utm", "auth"]
    # Replacement message table entries.
    mail: list[ReplacemsgGroupMailObject]
    # Replacement message table entries.
    http: list[ReplacemsgGroupHttpObject]
    # Replacement message table entries.
    webproxy: list[ReplacemsgGroupWebproxyObject]
    # Replacement message table entries.
    ftp: list[ReplacemsgGroupFtpObject]
    # Replacement message table entries.
    fortiguard_wf: list[ReplacemsgGroupFortiguardwfObject]
    # Replacement message table entries.
    spam: list[ReplacemsgGroupSpamObject]
    # Replacement message table entries.
    alertmail: list[ReplacemsgGroupAlertmailObject]
    # Replacement message table entries.
    admin: list[ReplacemsgGroupAdminObject]
    # Replacement message table entries.
    auth: list[ReplacemsgGroupAuthObject]
    # Replacement message table entries.
    sslvpn: list[ReplacemsgGroupSslvpnObject]
    # Replacement message table entries.
    nac_quar: list[ReplacemsgGroupNacquarObject]
    # Replacement message table entries.
    traffic_quota: list[ReplacemsgGroupTrafficquotaObject]
    # Replacement message table entries.
    utm: list[ReplacemsgGroupUtmObject]
    # Replacement message table entries.
    custom_message: list[ReplacemsgGroupCustommessageObject]
    # Replacement message table entries.
    icap: list[ReplacemsgGroupIcapObject]
    # Replacement message table entries.
    automation: list[ReplacemsgGroupAutomationObject]
    
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
    def to_dict(self) -> ReplacemsgGroupPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ReplacemsgGroup:
    """
    Configure replacement message groups.
    
    Path: system/replacemsg_group
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> list[ReplacemsgGroupObject]: ...
    
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> list[ReplacemsgGroupObject]: ...
    
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> ReplacemsgGroupObject: ...
    
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
    ) -> list[ReplacemsgGroupObject]: ...
    
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
    ) -> ReplacemsgGroupObject | list[ReplacemsgGroupObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ReplacemsgGroupObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: bool = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> ReplacemsgGroupObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[False] = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    # raw_json=True returns the full API envelope
    @overload
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        raw_json: Literal[True] = ...,
        **kwargs: Any,
    ) -> RawAPIResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
        vdom: str | bool | None = ...,
        **kwargs: Any,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
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
    ) -> ReplacemsgGroupObject: ...
    
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
        payload_dict: ReplacemsgGroupPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        group_type: Literal["default", "utm", "auth"] | None = ...,
        mail: str | list[str] | list[dict[str, Any]] | None = ...,
        http: str | list[str] | list[dict[str, Any]] | None = ...,
        webproxy: str | list[str] | list[dict[str, Any]] | None = ...,
        ftp: str | list[str] | list[dict[str, Any]] | None = ...,
        fortiguard_wf: str | list[str] | list[dict[str, Any]] | None = ...,
        spam: str | list[str] | list[dict[str, Any]] | None = ...,
        alertmail: str | list[str] | list[dict[str, Any]] | None = ...,
        admin: str | list[str] | list[dict[str, Any]] | None = ...,
        auth: str | list[str] | list[dict[str, Any]] | None = ...,
        sslvpn: str | list[str] | list[dict[str, Any]] | None = ...,
        nac_quar: str | list[str] | list[dict[str, Any]] | None = ...,
        traffic_quota: str | list[str] | list[dict[str, Any]] | None = ...,
        utm: str | list[str] | list[dict[str, Any]] | None = ...,
        custom_message: str | list[str] | list[dict[str, Any]] | None = ...,
        icap: str | list[str] | list[dict[str, Any]] | None = ...,
        automation: str | list[str] | list[dict[str, Any]] | None = ...,
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
    "ReplacemsgGroup",
    "ReplacemsgGroupPayload",
    "ReplacemsgGroupResponse",
    "ReplacemsgGroupObject",
]