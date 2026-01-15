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
    Type hints for dlp/profile payload fields.
    
    Configure DLP profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Name of the DLP profile. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    feature_set: Literal["flow", "proxy"]  # Flow/proxy feature set. | Default: flow
    replacemsg_group: str  # Replacement message group used by this DLP profile | MaxLen: 35
    rule: list[dict[str, Any]]  # Set up DLP rules for this profile.
    dlp_log: Literal["enable", "disable"]  # Enable/disable DLP logging. | Default: enable
    extended_log: Literal["enable", "disable"]  # Enable/disable extended logging for data loss prev | Default: disable
    nac_quar_log: Literal["enable", "disable"]  # Enable/disable NAC quarantine logging. | Default: disable
    full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]  # Protocols to always content archive.
    summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]  # Protocols to always log summary.
    fortidata_error_action: Literal["log-only", "block", "ignore"]  # Action to take if FortiData query fails. | Default: block

# Nested TypedDicts for table field children (dict mode)

class ProfileRuleItem(TypedDict):
    """Type hints for rule table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    id: int  # ID. | Default: 0 | Min: 0 | Max: 4294967295
    name: str  # Filter name. | MaxLen: 35
    severity: Literal["info", "low", "medium", "high", "critical"]  # Select the severity or threat level that matches t | Default: medium
    type: Literal["file", "message"]  # Select whether to check the content of messages | Default: file
    proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]  # Check messages or files over one or more of these
    filter_by: Literal["sensor", "label", "fingerprint", "encrypted", "none"]  # Select the type of content to match. | Default: none
    file_size: int  # Match files greater than or equal to this size | Default: 0 | Min: 0 | Max: 4193280
    sensitivity: str  # Select a DLP file pattern sensitivity to match.
    match_percentage: int  # Percentage of fingerprints in the fingerprint data | Default: 10 | Min: 1 | Max: 100
    file_type: int  # Select the number of a DLP file pattern table to m | Default: 0 | Min: 0 | Max: 4294967295
    sensor: str  # Select DLP sensors.
    label: str  # Select DLP label. | MaxLen: 35
    archive: Literal["disable", "enable"]  # Enable/disable DLP archiving. | Default: disable
    action: Literal["allow", "log-only", "block", "quarantine-ip"]  # Action to take with content that this DLP profile | Default: allow
    expiry: str  # Quarantine duration in days, hours, minutes | Default: 5m


# Nested classes for table field children (object mode)

@final
class ProfileRuleObject:
    """Typed object for rule table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # ID. | Default: 0 | Min: 0 | Max: 4294967295
    id: int
    # Filter name. | MaxLen: 35
    name: str
    # Select the severity or threat level that matches this filter | Default: medium
    severity: Literal["info", "low", "medium", "high", "critical"]
    # Select whether to check the content of messages | Default: file
    type: Literal["file", "message"]
    # Check messages or files over one or more of these protocols.
    proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]
    # Select the type of content to match. | Default: none
    filter_by: Literal["sensor", "label", "fingerprint", "encrypted", "none"]
    # Match files greater than or equal to this size (KB). | Default: 0 | Min: 0 | Max: 4193280
    file_size: int
    # Select a DLP file pattern sensitivity to match.
    sensitivity: str
    # Percentage of fingerprints in the fingerprint databases desi | Default: 10 | Min: 1 | Max: 100
    match_percentage: int
    # Select the number of a DLP file pattern table to match. | Default: 0 | Min: 0 | Max: 4294967295
    file_type: int
    # Select DLP sensors.
    sensor: str
    # Select DLP label. | MaxLen: 35
    label: str
    # Enable/disable DLP archiving. | Default: disable
    archive: Literal["disable", "enable"]
    # Action to take with content that this DLP profile matches. | Default: allow
    action: Literal["allow", "log-only", "block", "quarantine-ip"]
    # Quarantine duration in days, hours, minutes | Default: 5m
    expiry: str
    
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
    Type hints for dlp/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Name of the DLP profile. | MaxLen: 47
    comment: str  # Comment. | MaxLen: 255
    feature_set: Literal["flow", "proxy"]  # Flow/proxy feature set. | Default: flow
    replacemsg_group: str  # Replacement message group used by this DLP profile | MaxLen: 35
    rule: list[ProfileRuleItem]  # Set up DLP rules for this profile.
    dlp_log: Literal["enable", "disable"]  # Enable/disable DLP logging. | Default: enable
    extended_log: Literal["enable", "disable"]  # Enable/disable extended logging for data loss prev | Default: disable
    nac_quar_log: Literal["enable", "disable"]  # Enable/disable NAC quarantine logging. | Default: disable
    full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]  # Protocols to always content archive.
    summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]  # Protocols to always log summary.
    fortidata_error_action: Literal["log-only", "block", "ignore"]  # Action to take if FortiData query fails. | Default: block


@final
class ProfileObject:
    """Typed FortiObject for dlp/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Name of the DLP profile. | MaxLen: 47
    name: str
    # Comment. | MaxLen: 255
    comment: str
    # Flow/proxy feature set. | Default: flow
    feature_set: Literal["flow", "proxy"]
    # Replacement message group used by this DLP profile. | MaxLen: 35
    replacemsg_group: str
    # Set up DLP rules for this profile.
    rule: list[ProfileRuleObject]
    # Enable/disable DLP logging. | Default: enable
    dlp_log: Literal["enable", "disable"]
    # Enable/disable extended logging for data loss prevention. | Default: disable
    extended_log: Literal["enable", "disable"]
    # Enable/disable NAC quarantine logging. | Default: disable
    nac_quar_log: Literal["enable", "disable"]
    # Protocols to always content archive.
    full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]
    # Protocols to always log summary.
    summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"]
    # Action to take if FortiData query fails. | Default: block
    fortidata_error_action: Literal["log-only", "block", "ignore"]
    
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
    Configure DLP profiles.
    
    Path: dlp/profile
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
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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
        rule: str | list[str] | list[dict[str, Any]] | None = ...,
        dlp_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        nac_quar_log: Literal["enable", "disable"] | None = ...,
        full_archive_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        summary_proto: Literal["smtp", "pop3", "imap", "http-get", "http-post", "ftp", "nntp", "mapi", "ssh", "cifs"] | list[str] | None = ...,
        fortidata_error_action: Literal["log-only", "block", "ignore"] | None = ...,
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