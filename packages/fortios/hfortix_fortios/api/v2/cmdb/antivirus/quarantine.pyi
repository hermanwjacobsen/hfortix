from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class QuarantinePayload(TypedDict, total=False):
    """
    Type hints for antivirus/quarantine payload fields.
    
    Configure quarantine options.
    
    **Usage:**
        payload: QuarantinePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    agelimit: int  # Age limit for quarantined files | Default: 0 | Min: 0 | Max: 479
    maxfilesize: int  # Maximum file size to quarantine | Default: 0 | Min: 0 | Max: 500
    quarantine_quota: int  # The amount of disk space to reserve for quarantini | Default: 0 | Min: 0 | Max: 4294967295
    drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]  # Do not quarantine infected files found in sessions
    store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]  # Quarantine infected files found in sessions using | Default: imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh
    drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]  # Do not quarantine files detected by machine learni
    store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]  # Quarantine files detected by machine learning foun | Default: imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh
    lowspace: Literal["drop-new", "ovrw-old"]  # Select the method for handling additional files wh | Default: ovrw-old
    destination: Literal["NULL", "disk", "FortiAnalyzer"]  # Choose whether to quarantine files to the FortiGat | Default: disk

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class QuarantineResponse(TypedDict):
    """
    Type hints for antivirus/quarantine API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    agelimit: int  # Age limit for quarantined files | Default: 0 | Min: 0 | Max: 479
    maxfilesize: int  # Maximum file size to quarantine | Default: 0 | Min: 0 | Max: 500
    quarantine_quota: int  # The amount of disk space to reserve for quarantini | Default: 0 | Min: 0 | Max: 4294967295
    drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]  # Do not quarantine infected files found in sessions
    store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]  # Quarantine infected files found in sessions using | Default: imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh
    drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]  # Do not quarantine files detected by machine learni
    store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]  # Quarantine files detected by machine learning foun | Default: imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh
    lowspace: Literal["drop-new", "ovrw-old"]  # Select the method for handling additional files wh | Default: ovrw-old
    destination: Literal["NULL", "disk", "FortiAnalyzer"]  # Choose whether to quarantine files to the FortiGat | Default: disk


@final
class QuarantineObject:
    """Typed FortiObject for antivirus/quarantine with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Age limit for quarantined files | Default: 0 | Min: 0 | Max: 479
    agelimit: int
    # Maximum file size to quarantine | Default: 0 | Min: 0 | Max: 500
    maxfilesize: int
    # The amount of disk space to reserve for quarantining files | Default: 0 | Min: 0 | Max: 4294967295
    quarantine_quota: int
    # Do not quarantine infected files found in sessions using the
    drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]
    # Quarantine infected files found in sessions using the select | Default: imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh
    store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]
    # Do not quarantine files detected by machine learning found i
    drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]
    # Quarantine files detected by machine learning found in sessi | Default: imap smtp pop3 http ftp nntp imaps smtps pop3s https ftps mapi cifs ssh
    store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"]
    # Select the method for handling additional files when running | Default: ovrw-old
    lowspace: Literal["drop-new", "ovrw-old"]
    # Choose whether to quarantine files to the FortiGate disk or | Default: disk
    destination: Literal["NULL", "disk", "FortiAnalyzer"]
    
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
    def to_dict(self) -> QuarantinePayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Quarantine:
    """
    Configure quarantine options.
    
    Path: antivirus/quarantine
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject: ...
    
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
    ) -> QuarantineObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> QuarantineObject: ...
    
    @overload
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: QuarantinePayload | None = ...,
        agelimit: int | None = ...,
        maxfilesize: int | None = ...,
        quarantine_quota: int | None = ...,
        drop_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_infected: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        drop_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        store_machine_learning: Literal["imap", "smtp", "pop3", "http", "ftp", "nntp", "imaps", "smtps", "pop3s", "https", "ftps", "mapi", "cifs", "ssh"] | list[str] | None = ...,
        lowspace: Literal["drop-new", "ovrw-old"] | None = ...,
        destination: Literal["NULL", "disk", "FortiAnalyzer"] | None = ...,
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
    "Quarantine",
    "QuarantinePayload",
    "QuarantineResponse",
    "QuarantineObject",
]