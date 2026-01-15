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
    Type hints for webfilter/profile payload fields.
    
    Configure Web filter profiles.
    
    **Related Resources:**

    Dependencies (resources this endpoint references):
        - :class:`~.system.replacemsg-group.ReplacemsgGroupEndpoint` (via: replacemsg-group)

    **Usage:**
        payload: ProfilePayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    name: str  # Profile name. | MaxLen: 47
    comment: str  # Optional comments. | MaxLen: 255
    feature_set: Literal["flow", "proxy"]  # Flow/proxy feature set. | Default: flow
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"]  # Options.
    https_replacemsg: Literal["enable", "disable"]  # Enable replacement messages for HTTPS. | Default: enable
    web_flow_log_encoding: Literal["utf-8", "punycode"]  # Log encoding in flow mode. | Default: utf-8
    ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"]  # Permitted override types.
    post_action: Literal["normal", "block"]  # Action taken for HTTP POST traffic. | Default: normal
    override: str  # Web Filter override settings.
    web: str  # Web content filtering settings.
    ftgd_wf: str  # FortiGuard Web Filter settings.
    antiphish: str  # AntiPhishing profile.
    wisp: Literal["enable", "disable"]  # Enable/disable web proxy WISP. | Default: disable
    wisp_servers: list[dict[str, Any]]  # WISP servers.
    wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"]  # WISP server selection algorithm. | Default: auto-learning
    log_all_url: Literal["enable", "disable"]  # Enable/disable logging all URLs visited. | Default: disable
    web_content_log: Literal["enable", "disable"]  # Enable/disable logging logging blocked web content | Default: enable
    web_filter_activex_log: Literal["enable", "disable"]  # Enable/disable logging ActiveX. | Default: enable
    web_filter_command_block_log: Literal["enable", "disable"]  # Enable/disable logging blocked commands. | Default: enable
    web_filter_cookie_log: Literal["enable", "disable"]  # Enable/disable logging cookie filtering. | Default: enable
    web_filter_applet_log: Literal["enable", "disable"]  # Enable/disable logging Java applets. | Default: enable
    web_filter_jscript_log: Literal["enable", "disable"]  # Enable/disable logging JScripts. | Default: enable
    web_filter_js_log: Literal["enable", "disable"]  # Enable/disable logging Java scripts. | Default: enable
    web_filter_vbs_log: Literal["enable", "disable"]  # Enable/disable logging VBS scripts. | Default: enable
    web_filter_unknown_log: Literal["enable", "disable"]  # Enable/disable logging unknown scripts. | Default: enable
    web_filter_referer_log: Literal["enable", "disable"]  # Enable/disable logging referrers. | Default: enable
    web_filter_cookie_removal_log: Literal["enable", "disable"]  # Enable/disable logging blocked cookies. | Default: enable
    web_url_log: Literal["enable", "disable"]  # Enable/disable logging URL filtering. | Default: enable
    web_invalid_domain_log: Literal["enable", "disable"]  # Enable/disable logging invalid domain names. | Default: enable
    web_ftgd_err_log: Literal["enable", "disable"]  # Enable/disable logging rating errors. | Default: enable
    web_ftgd_quota_usage: Literal["enable", "disable"]  # Enable/disable logging daily quota usage. | Default: enable
    extended_log: Literal["enable", "disable"]  # Enable/disable extended logging for web filtering. | Default: disable
    web_extended_all_action_log: Literal["enable", "disable"]  # Enable/disable extended any filter action logging | Default: disable
    web_antiphishing_log: Literal["enable", "disable"]  # Enable/disable logging of AntiPhishing checks. | Default: enable

# Nested TypedDicts for table field children (dict mode)

class ProfileWispserversItem(TypedDict):
    """Type hints for wisp-servers table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    name: str  # Server name. | MaxLen: 79


# Nested classes for table field children (object mode)

@final
class ProfileWispserversObject:
    """Typed object for wisp-servers table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Server name. | MaxLen: 79
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



# Response TypedDict for GET returns (all fields present in API response)
class ProfileResponse(TypedDict):
    """
    Type hints for webfilter/profile API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    name: str  # Profile name. | MaxLen: 47
    comment: str  # Optional comments. | MaxLen: 255
    feature_set: Literal["flow", "proxy"]  # Flow/proxy feature set. | Default: flow
    replacemsg_group: str  # Replacement message group. | MaxLen: 35
    options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"]  # Options.
    https_replacemsg: Literal["enable", "disable"]  # Enable replacement messages for HTTPS. | Default: enable
    web_flow_log_encoding: Literal["utf-8", "punycode"]  # Log encoding in flow mode. | Default: utf-8
    ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"]  # Permitted override types.
    post_action: Literal["normal", "block"]  # Action taken for HTTP POST traffic. | Default: normal
    override: str  # Web Filter override settings.
    web: str  # Web content filtering settings.
    ftgd_wf: str  # FortiGuard Web Filter settings.
    antiphish: str  # AntiPhishing profile.
    wisp: Literal["enable", "disable"]  # Enable/disable web proxy WISP. | Default: disable
    wisp_servers: list[ProfileWispserversItem]  # WISP servers.
    wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"]  # WISP server selection algorithm. | Default: auto-learning
    log_all_url: Literal["enable", "disable"]  # Enable/disable logging all URLs visited. | Default: disable
    web_content_log: Literal["enable", "disable"]  # Enable/disable logging logging blocked web content | Default: enable
    web_filter_activex_log: Literal["enable", "disable"]  # Enable/disable logging ActiveX. | Default: enable
    web_filter_command_block_log: Literal["enable", "disable"]  # Enable/disable logging blocked commands. | Default: enable
    web_filter_cookie_log: Literal["enable", "disable"]  # Enable/disable logging cookie filtering. | Default: enable
    web_filter_applet_log: Literal["enable", "disable"]  # Enable/disable logging Java applets. | Default: enable
    web_filter_jscript_log: Literal["enable", "disable"]  # Enable/disable logging JScripts. | Default: enable
    web_filter_js_log: Literal["enable", "disable"]  # Enable/disable logging Java scripts. | Default: enable
    web_filter_vbs_log: Literal["enable", "disable"]  # Enable/disable logging VBS scripts. | Default: enable
    web_filter_unknown_log: Literal["enable", "disable"]  # Enable/disable logging unknown scripts. | Default: enable
    web_filter_referer_log: Literal["enable", "disable"]  # Enable/disable logging referrers. | Default: enable
    web_filter_cookie_removal_log: Literal["enable", "disable"]  # Enable/disable logging blocked cookies. | Default: enable
    web_url_log: Literal["enable", "disable"]  # Enable/disable logging URL filtering. | Default: enable
    web_invalid_domain_log: Literal["enable", "disable"]  # Enable/disable logging invalid domain names. | Default: enable
    web_ftgd_err_log: Literal["enable", "disable"]  # Enable/disable logging rating errors. | Default: enable
    web_ftgd_quota_usage: Literal["enable", "disable"]  # Enable/disable logging daily quota usage. | Default: enable
    extended_log: Literal["enable", "disable"]  # Enable/disable extended logging for web filtering. | Default: disable
    web_extended_all_action_log: Literal["enable", "disable"]  # Enable/disable extended any filter action logging | Default: disable
    web_antiphishing_log: Literal["enable", "disable"]  # Enable/disable logging of AntiPhishing checks. | Default: enable


@final
class ProfileObject:
    """Typed FortiObject for webfilter/profile with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Profile name. | MaxLen: 47
    name: str
    # Optional comments. | MaxLen: 255
    comment: str
    # Flow/proxy feature set. | Default: flow
    feature_set: Literal["flow", "proxy"]
    # Replacement message group. | MaxLen: 35
    replacemsg_group: str
    # Options.
    options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"]
    # Enable replacement messages for HTTPS. | Default: enable
    https_replacemsg: Literal["enable", "disable"]
    # Log encoding in flow mode. | Default: utf-8
    web_flow_log_encoding: Literal["utf-8", "punycode"]
    # Permitted override types.
    ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"]
    # Action taken for HTTP POST traffic. | Default: normal
    post_action: Literal["normal", "block"]
    # Web Filter override settings.
    override: str
    # Web content filtering settings.
    web: str
    # FortiGuard Web Filter settings.
    ftgd_wf: str
    # AntiPhishing profile.
    antiphish: str
    # Enable/disable web proxy WISP. | Default: disable
    wisp: Literal["enable", "disable"]
    # WISP servers.
    wisp_servers: list[ProfileWispserversObject]
    # WISP server selection algorithm. | Default: auto-learning
    wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"]
    # Enable/disable logging all URLs visited. | Default: disable
    log_all_url: Literal["enable", "disable"]
    # Enable/disable logging logging blocked web content. | Default: enable
    web_content_log: Literal["enable", "disable"]
    # Enable/disable logging ActiveX. | Default: enable
    web_filter_activex_log: Literal["enable", "disable"]
    # Enable/disable logging blocked commands. | Default: enable
    web_filter_command_block_log: Literal["enable", "disable"]
    # Enable/disable logging cookie filtering. | Default: enable
    web_filter_cookie_log: Literal["enable", "disable"]
    # Enable/disable logging Java applets. | Default: enable
    web_filter_applet_log: Literal["enable", "disable"]
    # Enable/disable logging JScripts. | Default: enable
    web_filter_jscript_log: Literal["enable", "disable"]
    # Enable/disable logging Java scripts. | Default: enable
    web_filter_js_log: Literal["enable", "disable"]
    # Enable/disable logging VBS scripts. | Default: enable
    web_filter_vbs_log: Literal["enable", "disable"]
    # Enable/disable logging unknown scripts. | Default: enable
    web_filter_unknown_log: Literal["enable", "disable"]
    # Enable/disable logging referrers. | Default: enable
    web_filter_referer_log: Literal["enable", "disable"]
    # Enable/disable logging blocked cookies. | Default: enable
    web_filter_cookie_removal_log: Literal["enable", "disable"]
    # Enable/disable logging URL filtering. | Default: enable
    web_url_log: Literal["enable", "disable"]
    # Enable/disable logging invalid domain names. | Default: enable
    web_invalid_domain_log: Literal["enable", "disable"]
    # Enable/disable logging rating errors. | Default: enable
    web_ftgd_err_log: Literal["enable", "disable"]
    # Enable/disable logging daily quota usage. | Default: enable
    web_ftgd_quota_usage: Literal["enable", "disable"]
    # Enable/disable extended logging for web filtering. | Default: disable
    extended_log: Literal["enable", "disable"]
    # Enable/disable extended any filter action logging for web fi | Default: disable
    web_extended_all_action_log: Literal["enable", "disable"]
    # Enable/disable logging of AntiPhishing checks. | Default: enable
    web_antiphishing_log: Literal["enable", "disable"]
    
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
    Configure Web filter profiles.
    
    Path: webfilter/profile
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
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def post(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: ProfilePayload | None = ...,
        name: str | None = ...,
        comment: str | None = ...,
        feature_set: Literal["flow", "proxy"] | None = ...,
        replacemsg_group: str | None = ...,
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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
        options: Literal["activexfilter", "cookiefilter", "javafilter", "block-invalid-url", "jscript", "js", "vbs", "unknown", "intrinsic", "wf-referer", "wf-cookie", "per-user-bal"] | list[str] | None = ...,
        https_replacemsg: Literal["enable", "disable"] | None = ...,
        web_flow_log_encoding: Literal["utf-8", "punycode"] | None = ...,
        ovrd_perm: Literal["bannedword-override", "urlfilter-override", "fortiguard-wf-override", "contenttype-check-override"] | list[str] | None = ...,
        post_action: Literal["normal", "block"] | None = ...,
        override: str | None = ...,
        web: str | None = ...,
        ftgd_wf: str | None = ...,
        antiphish: str | None = ...,
        wisp: Literal["enable", "disable"] | None = ...,
        wisp_servers: str | list[str] | list[dict[str, Any]] | None = ...,
        wisp_algorithm: Literal["primary-secondary", "round-robin", "auto-learning"] | None = ...,
        log_all_url: Literal["enable", "disable"] | None = ...,
        web_content_log: Literal["enable", "disable"] | None = ...,
        web_filter_activex_log: Literal["enable", "disable"] | None = ...,
        web_filter_command_block_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_log: Literal["enable", "disable"] | None = ...,
        web_filter_applet_log: Literal["enable", "disable"] | None = ...,
        web_filter_jscript_log: Literal["enable", "disable"] | None = ...,
        web_filter_js_log: Literal["enable", "disable"] | None = ...,
        web_filter_vbs_log: Literal["enable", "disable"] | None = ...,
        web_filter_unknown_log: Literal["enable", "disable"] | None = ...,
        web_filter_referer_log: Literal["enable", "disable"] | None = ...,
        web_filter_cookie_removal_log: Literal["enable", "disable"] | None = ...,
        web_url_log: Literal["enable", "disable"] | None = ...,
        web_invalid_domain_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_err_log: Literal["enable", "disable"] | None = ...,
        web_ftgd_quota_usage: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        web_extended_all_action_log: Literal["enable", "disable"] | None = ...,
        web_antiphishing_log: Literal["enable", "disable"] | None = ...,
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