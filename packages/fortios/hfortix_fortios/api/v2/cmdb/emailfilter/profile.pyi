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
    Type hints for emailfilter/profile payload fields.
    
    Configure Email Filter profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.emailfilter.block-allow-list.BlockAllowListEndpoint` (via: spam-bal-table)
        - :class:`~.emailfilter.bword.BwordEndpoint` (via: spam-bword-table)
        - :class:`~.emailfilter.dnsbl.DnsblEndpoint` (via: spam-rbl-table)
        - :class:`~.emailfilter.iptrust.IptrustEndpoint` (via: spam-iptrust-table)
        - :class:`~.emailfilter.mheader.MheaderEndpoint` (via: spam-mheader-table)
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    feature_set: Literal["flow", "proxy"]  # Flow/proxy feature set. | Default: flow
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    spam_log: Literal["disable", "enable"]  # Enable/disable spam logging for email filtering. | Default: enable
    spam_log_fortiguard_response: Literal["disable", "enable"]  # Enable/disable logging FortiGuard spam response. | Default: disable
    spam_filtering: Literal["enable", "disable"]  # Enable/disable spam filtering. | Default: disable
    external: Literal["enable", "disable"]  # Enable/disable external Email inspection. | Default: disable
    options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"]  # Options.
    imap: str  # IMAP.
    pop3: str  # POP3.
    smtp: str  # SMTP.
    mapi: str  # MAPI.
    msn_hotmail: str  # MSN Hotmail.
    yahoo_mail: str  # Yahoo! Mail.
    gmail: str  # Gmail.
    other_webmails: str  # Other supported webmails.
    spam_bword_threshold: int  # Spam banned word threshold. | Default: 10 | Min: 0 | Max: 2147483647
    spam_bword_table: int  # Anti-spam banned word table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_bal_table: int  # Anti-spam block/allow list table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_mheader_table: int  # Anti-spam MIME header table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_rbl_table: int  # Anti-spam DNSBL table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_iptrust_table: int  # Anti-spam IP trust table ID. | Default: 0 | Min: 0 | Max: 4294967295

# Nested TypedDicts for table field children (dict mode)

# Nested classes for table field children (object mode)


# Response TypedDict for GET returns (all fields present in API response)
class ProfileResponse(TypedDict):
    """
    Type hints for emailfilter/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Profile name. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    feature_set: Literal["flow", "proxy"]  # Flow/proxy feature set. | Default: flow
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    spam_log: Literal["disable", "enable"]  # Enable/disable spam logging for email filtering. | Default: enable
    spam_log_fortiguard_response: Literal["disable", "enable"]  # Enable/disable logging FortiGuard spam response. | Default: disable
    spam_filtering: Literal["enable", "disable"]  # Enable/disable spam filtering. | Default: disable
    external: Literal["enable", "disable"]  # Enable/disable external Email inspection. | Default: disable
    options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"]  # Options.
    imap: str  # IMAP.
    pop3: str  # POP3.
    smtp: str  # SMTP.
    mapi: str  # MAPI.
    msn_hotmail: str  # MSN Hotmail.
    yahoo_mail: str  # Yahoo! Mail.
    gmail: str  # Gmail.
    other_webmails: str  # Other supported webmails.
    spam_bword_threshold: int  # Spam banned word threshold. | Default: 10 | Min: 0 | Max: 2147483647
    spam_bword_table: int  # Anti-spam banned word table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_bal_table: int  # Anti-spam block/allow list table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_mheader_table: int  # Anti-spam MIME header table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_rbl_table: int  # Anti-spam DNSBL table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_iptrust_table: int  # Anti-spam IP trust table ID. | Default: 0 | Min: 0 | Max: 4294967295


@final
class ProfileObject:
    """Typed FortiObject for emailfilter/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name. | MaxLen: 47
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Flow/proxy feature set. | Default: flow
    feature_set: Literal["flow", "proxy"]
    # Replacement message group. | MaxLen: 35
    replacemsg_group: str
    # Enable/disable spam logging for email filtering. | Default: enable
    spam_log: Literal["disable", "enable"]
    # Enable/disable logging FortiGuard spam response. | Default: disable
    spam_log_fortiguard_response: Literal["disable", "enable"]
    # Enable/disable spam filtering. | Default: disable
    spam_filtering: Literal["enable", "disable"]
    # Enable/disable external Email inspection. | Default: disable
    external: Literal["enable", "disable"]
    # Options.
    options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"]
    # IMAP.
    imap: str
    # POP3.
    pop3: str
    # SMTP.
    smtp: str
    # MAPI.
    mapi: str
    # MSN Hotmail.
    msn_hotmail: str
    # Yahoo! Mail.
    yahoo_mail: str
    # Gmail.
    gmail: str
    # Other supported webmails.
    other_webmails: str
    # Spam banned word threshold. | Default: 10 | Min: 0 | Max: 2147483647
    spam_bword_threshold: int
    # Anti-spam banned word table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_bword_table: int
    # Anti-spam block/allow list table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_bal_table: int
    # Anti-spam MIME header table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_mheader_table: int
    # Anti-spam DNSBL table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_rbl_table: int
    # Anti-spam IP trust table ID. | Default: 0 | Min: 0 | Max: 4294967295
    spam_iptrust_table: int
    
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
    Configure Email Filter profiles.
    
    Path: emailfilter/profile
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
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> ProfileObject: ...
    
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
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
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        spam_log: Literal["disable", "enable"] | None = ...,
        spam_log_fortiguard_response: Literal["disable", "enable"] | None = ...,
        spam_filtering: Literal["enable", "disable"] | None = ...,
        external: Literal["enable", "disable"] | None = ...,
        options: Literal["bannedword", "spambal", "spamfsip", "spamfssubmit", "spamfschksum", "spamfsurl", "spamhelodns", "spamraddrdns", "spamrbl", "spamhdrcheck", "spamfsphish"] | list[str] | None = ...,
        imap: str | None = ...,
        pop3: str | None = ...,
        smtp: str | None = ...,
        mapi: str | None = ...,
        msn_hotmail: str | None = ...,
        yahoo_mail: str | None = ...,
        gmail: str | None = ...,
        other_webmails: str | None = ...,
        spam_bword_threshold: int | None = ...,
        spam_bword_table: int | None = ...,
        spam_bal_table: int | None = ...,
        spam_mheader_table: int | None = ...,
        spam_rbl_table: int | None = ...,
        spam_iptrust_table: int | None = ...,
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