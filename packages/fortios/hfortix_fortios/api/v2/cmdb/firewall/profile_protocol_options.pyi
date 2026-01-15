from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class ProfileProtocolOptionsPayload(TypedDict, total=False):
    """
    Type hints for firewall/profile_protocol_options payload fields.
    
    Configure protocol options.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ProfileProtocolOptionsPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name. | MaxLen: 47
    comment: str  # Optional comments. | MaxLen: 255
    replacemsg_group: str  # Name of the replacement message group to be used. | MaxLen: 35
    oversize_log: Literal["disable", "enable"]  # Enable/disable logging for antivirus oversize file | Default: disable
    switching_protocols_log: Literal["disable", "enable"]  # Enable/disable logging for HTTP/HTTPS switching pr | Default: disable
    http: str  # Configure HTTP protocol options.
    ftp: str  # Configure FTP protocol options.
    imap: str  # Configure IMAP protocol options.
    mapi: str  # Configure MAPI protocol options.
    pop3: str  # Configure POP3 protocol options.
    smtp: str  # Configure SMTP protocol options.
    nntp: str  # Configure NNTP protocol options.
    ssh: str  # Configure SFTP and SCP protocol options.
    dns: str  # Configure DNS protocol options.
    cifs: str  # Configure CIFS protocol options.
    mail_signature: str  # Configure Mail signature.
    rpc_over_http: Literal["enable", "disable"]  # Enable/disable inspection of RPC over HTTP. | Default: disable

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ProfileProtocolOptionsResponse(TypedDict):
    """
    Type hints for firewall/profile_protocol_options API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name. | MaxLen: 47
    comment: str  # Optional comments. | MaxLen: 255
    replacemsg_group: str  # Name of the replacement message group to be used. | MaxLen: 35
    oversize_log: Literal["disable", "enable"]  # Enable/disable logging for antivirus oversize file | Default: disable
    switching_protocols_log: Literal["disable", "enable"]  # Enable/disable logging for HTTP/HTTPS switching pr | Default: disable
    http: str  # Configure HTTP protocol options.
    ftp: str  # Configure FTP protocol options.
    imap: str  # Configure IMAP protocol options.
    mapi: str  # Configure MAPI protocol options.
    pop3: str  # Configure POP3 protocol options.
    smtp: str  # Configure SMTP protocol options.
    nntp: str  # Configure NNTP protocol options.
    ssh: str  # Configure SFTP and SCP protocol options.
    dns: str  # Configure DNS protocol options.
    cifs: str  # Configure CIFS protocol options.
    mail_signature: str  # Configure Mail signature.
    rpc_over_http: Literal["enable", "disable"]  # Enable/disable inspection of RPC over HTTP. | Default: disable


@final
class ProfileProtocolOptionsObject:
    """Typed FortiObject for firewall/profile_protocol_options with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name. | MaxLen: 47
    name: str
    # Optional comments. | MaxLen: 255
    comment: str
    # Name of the replacement message group to be used. | MaxLen: 35
    replacemsg_group: str
    # Enable/disable logging for antivirus oversize file blocking. | Default: disable
    oversize_log: Literal["disable", "enable"]
    # Enable/disable logging for HTTP/HTTPS switching protocols. | Default: disable
    switching_protocols_log: Literal["disable", "enable"]
    # Configure HTTP protocol options.
    http: str
    # Configure FTP protocol options.
    ftp: str
    # Configure IMAP protocol options.
    imap: str
    # Configure MAPI protocol options.
    mapi: str
    # Configure POP3 protocol options.
    pop3: str
    # Configure SMTP protocol options.
    smtp: str
    # Configure NNTP protocol options.
    nntp: str
    # Configure SFTP and SCP protocol options.
    ssh: str
    # Configure DNS protocol options.
    dns: str
    # Configure CIFS protocol options.
    cifs: str
    # Configure Mail signature.
    mail_signature: str
    # Enable/disable inspection of RPC over HTTP. | Default: disable
    rpc_over_http: Literal["enable", "disable"]
    
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
    def to_dict(self) -> ProfileProtocolOptionsPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class ProfileProtocolOptions:
    """
    Configure protocol options.
    
    Path: firewall/profile_protocol_options
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
    ) -> ProfileProtocolOptionsObject: ...
    
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
    ) -> ProfileProtocolOptionsObject: ...
    
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
    ) -> FortiObjectList[ProfileProtocolOptionsObject]: ...
    
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
    ) -> ProfileProtocolOptionsObject: ...
    
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
    ) -> ProfileProtocolOptionsObject: ...
    
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
    ) -> FortiObjectList[ProfileProtocolOptionsObject]: ...
    
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
    ) -> ProfileProtocolOptionsObject: ...
    
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
    ) -> ProfileProtocolOptionsObject: ...
    
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
    ) -> FortiObjectList[ProfileProtocolOptionsObject]: ...
    
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
    ) -> ProfileProtocolOptionsObject | list[ProfileProtocolOptionsObject] | dict[str, Any] | list[dict[str, Any]]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # POST overloads
    @overload
    def post(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileProtocolOptionsObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def post(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileProtocolOptionsObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def put(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # DELETE overloads
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileProtocolOptionsObject: ...
    
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    # Default overload
    @overload
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def delete(
        self,
        name: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> FortiObject: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: ProfileProtocolOptionsPayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        replacemsg_group: str | None = ...,
        oversize_log: Literal["disable", "enable"] | None = ...,
        switching_protocols_log: Literal["disable", "enable"] | None = ...,
        http: str | None = ...,
        ftp: str | None = ...,
        imap: str | None = ...,
        mapi: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        nntp: str | None = ...,
        ssh: str | None = ...,
        dns: str | None = ...,
        cifs: str | None = ...,
        mail_signature: str | None = ...,
        rpc_over_http: Literal["enable", "disable"] | None = ...,
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
    "ProfileProtocolOptions",
    "ProfileProtocolOptionsPayload",
    "ProfileProtocolOptionsResponse",
    "ProfileProtocolOptionsObject",
]