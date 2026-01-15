from typing import TypedDict, Literal, Any, Coroutine, Union, overload, Generator, final
from typing_extensions import NotRequired
from hfortix_fortios.models import FortiObject, FortiObjectList
from hfortix_core.types import MutationResponse

# Payload TypedDict for IDE autocomplete (for POST/PUT - fields are optional via total=False)
# NOTE: We intentionally DON'T use NotRequired wrapper because:
# 1. total=False already makes all fields optional
# 2. NotRequired[Literal[...]] prevents Pylance from validating Literal values in dict literals
class SettingPayload(TypedDict, total=False):
    """
    Type hints for log/setting payload fields.
    
    Configure general log settings.
    
    **Usage:**
        payload: SettingPayload = {
            "field": "value",  # <- autocomplete shows all fields
        }
    """
    resolve_ip: Literal["enable", "disable"]  # Enable/disable adding resolved domain names to tra | Default: disable
    resolve_port: Literal["enable", "disable"]  # Enable/disable adding resolved service names to tr | Default: enable
    log_user_in_upper: Literal["enable", "disable"]  # Enable/disable logs with user-in-upper. | Default: disable
    fwpolicy_implicit_log: Literal["enable", "disable"]  # Enable/disable implicit firewall policy logging. | Default: disable
    fwpolicy6_implicit_log: Literal["enable", "disable"]  # Enable/disable implicit firewall policy6 logging. | Default: disable
    extended_log: Literal["enable", "disable"]  # Enable/disable extended traffic logging. | Default: disable
    local_in_allow: Literal["enable", "disable"]  # Enable/disable local-in-allow logging. | Default: disable
    local_in_deny_unicast: Literal["enable", "disable"]  # Enable/disable local-in-deny-unicast logging. | Default: disable
    local_in_deny_broadcast: Literal["enable", "disable"]  # Enable/disable local-in-deny-broadcast logging. | Default: disable
    local_in_policy_log: Literal["enable", "disable"]  # Enable/disable local-in-policy logging. | Default: disable
    local_out: Literal["enable", "disable"]  # Enable/disable local-out logging. | Default: enable
    local_out_ioc_detection: Literal["enable", "disable"]  # Enable/disable local-out traffic IoC detection. Re | Default: enable
    daemon_log: Literal["enable", "disable"]  # Enable/disable daemon logging. | Default: disable
    neighbor_event: Literal["enable", "disable"]  # Enable/disable neighbor event logging. | Default: disable
    brief_traffic_format: Literal["enable", "disable"]  # Enable/disable brief format traffic logging. | Default: disable
    user_anonymize: Literal["enable", "disable"]  # Enable/disable anonymizing user names in log messa | Default: disable
    expolicy_implicit_log: Literal["enable", "disable"]  # Enable/disable proxy firewall implicit policy logg | Default: disable
    log_policy_comment: Literal["enable", "disable"]  # Enable/disable inserting policy comments into traf | Default: disable
    faz_override: Literal["enable", "disable"]  # Enable/disable override FortiAnalyzer settings. | Default: disable
    syslog_override: Literal["enable", "disable"]  # Enable/disable override Syslog settings. | Default: disable
    rest_api_set: Literal["enable", "disable"]  # Enable/disable REST API POST/PUT/DELETE request lo | Default: disable
    rest_api_get: Literal["enable", "disable"]  # Enable/disable REST API GET request logging. | Default: disable
    rest_api_performance: Literal["enable", "disable"]  # Enable/disable REST API memory and performance sta | Default: disable
    long_live_session_stat: Literal["enable", "disable"]  # Enable/disable long-live-session statistics loggin | Default: enable
    extended_utm_log: Literal["enable", "disable"]  # Enable/disable extended UTM logging. | Default: disable
    zone_name: Literal["enable", "disable"]  # Enable/disable zone name logging. | Default: disable
    web_svc_perf: Literal["enable", "disable"]  # Enable/disable web-svc performance logging. | Default: disable
    custom_log_fields: list[dict[str, Any]]  # Custom fields to append to all log messages.
    anonymization_hash: str  # User name anonymization hash salt. | MaxLen: 32

# Nested TypedDicts for table field children (dict mode)

class SettingCustomlogfieldsItem(TypedDict):
    """Type hints for custom-log-fields table item fields (dict mode).
    
    Provides IDE autocomplete for nested table field items.
    All fields are present in API responses.
    """
    
    field_id: str  # Custom log field. | MaxLen: 35


# Nested classes for table field children (object mode)

@final
class SettingCustomlogfieldsObject:
    """Typed object for custom-log-fields table items.
    
    Provides IDE autocomplete for nested table field attributes.
    At runtime, this is a FortiObject instance.
    """
    
    # Custom log field. | MaxLen: 35
    field_id: str
    
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
class SettingResponse(TypedDict):
    """
    Type hints for log/setting API response fields.
    
    All fields are present in the response from the FortiGate API.
    """
    resolve_ip: Literal["enable", "disable"]  # Enable/disable adding resolved domain names to tra | Default: disable
    resolve_port: Literal["enable", "disable"]  # Enable/disable adding resolved service names to tr | Default: enable
    log_user_in_upper: Literal["enable", "disable"]  # Enable/disable logs with user-in-upper. | Default: disable
    fwpolicy_implicit_log: Literal["enable", "disable"]  # Enable/disable implicit firewall policy logging. | Default: disable
    fwpolicy6_implicit_log: Literal["enable", "disable"]  # Enable/disable implicit firewall policy6 logging. | Default: disable
    extended_log: Literal["enable", "disable"]  # Enable/disable extended traffic logging. | Default: disable
    local_in_allow: Literal["enable", "disable"]  # Enable/disable local-in-allow logging. | Default: disable
    local_in_deny_unicast: Literal["enable", "disable"]  # Enable/disable local-in-deny-unicast logging. | Default: disable
    local_in_deny_broadcast: Literal["enable", "disable"]  # Enable/disable local-in-deny-broadcast logging. | Default: disable
    local_in_policy_log: Literal["enable", "disable"]  # Enable/disable local-in-policy logging. | Default: disable
    local_out: Literal["enable", "disable"]  # Enable/disable local-out logging. | Default: enable
    local_out_ioc_detection: Literal["enable", "disable"]  # Enable/disable local-out traffic IoC detection. Re | Default: enable
    daemon_log: Literal["enable", "disable"]  # Enable/disable daemon logging. | Default: disable
    neighbor_event: Literal["enable", "disable"]  # Enable/disable neighbor event logging. | Default: disable
    brief_traffic_format: Literal["enable", "disable"]  # Enable/disable brief format traffic logging. | Default: disable
    user_anonymize: Literal["enable", "disable"]  # Enable/disable anonymizing user names in log messa | Default: disable
    expolicy_implicit_log: Literal["enable", "disable"]  # Enable/disable proxy firewall implicit policy logg | Default: disable
    log_policy_comment: Literal["enable", "disable"]  # Enable/disable inserting policy comments into traf | Default: disable
    faz_override: Literal["enable", "disable"]  # Enable/disable override FortiAnalyzer settings. | Default: disable
    syslog_override: Literal["enable", "disable"]  # Enable/disable override Syslog settings. | Default: disable
    rest_api_set: Literal["enable", "disable"]  # Enable/disable REST API POST/PUT/DELETE request lo | Default: disable
    rest_api_get: Literal["enable", "disable"]  # Enable/disable REST API GET request logging. | Default: disable
    rest_api_performance: Literal["enable", "disable"]  # Enable/disable REST API memory and performance sta | Default: disable
    long_live_session_stat: Literal["enable", "disable"]  # Enable/disable long-live-session statistics loggin | Default: enable
    extended_utm_log: Literal["enable", "disable"]  # Enable/disable extended UTM logging. | Default: disable
    zone_name: Literal["enable", "disable"]  # Enable/disable zone name logging. | Default: disable
    web_svc_perf: Literal["enable", "disable"]  # Enable/disable web-svc performance logging. | Default: disable
    custom_log_fields: list[SettingCustomlogfieldsItem]  # Custom fields to append to all log messages.
    anonymization_hash: str  # User name anonymization hash salt. | MaxLen: 32


@final
class SettingObject:
    """Typed FortiObject for log/setting with IDE autocomplete support.
    
    This is a typed wrapper that provides IDE autocomplete for API response fields.
    At runtime, this is actually a FortiObject instance.
    """
    
    # Enable/disable adding resolved domain names to traffic logs | Default: disable
    resolve_ip: Literal["enable", "disable"]
    # Enable/disable adding resolved service names to traffic logs | Default: enable
    resolve_port: Literal["enable", "disable"]
    # Enable/disable logs with user-in-upper. | Default: disable
    log_user_in_upper: Literal["enable", "disable"]
    # Enable/disable implicit firewall policy logging. | Default: disable
    fwpolicy_implicit_log: Literal["enable", "disable"]
    # Enable/disable implicit firewall policy6 logging. | Default: disable
    fwpolicy6_implicit_log: Literal["enable", "disable"]
    # Enable/disable extended traffic logging. | Default: disable
    extended_log: Literal["enable", "disable"]
    # Enable/disable local-in-allow logging. | Default: disable
    local_in_allow: Literal["enable", "disable"]
    # Enable/disable local-in-deny-unicast logging. | Default: disable
    local_in_deny_unicast: Literal["enable", "disable"]
    # Enable/disable local-in-deny-broadcast logging. | Default: disable
    local_in_deny_broadcast: Literal["enable", "disable"]
    # Enable/disable local-in-policy logging. | Default: disable
    local_in_policy_log: Literal["enable", "disable"]
    # Enable/disable local-out logging. | Default: enable
    local_out: Literal["enable", "disable"]
    # Enable/disable local-out traffic IoC detection. Requires loc | Default: enable
    local_out_ioc_detection: Literal["enable", "disable"]
    # Enable/disable daemon logging. | Default: disable
    daemon_log: Literal["enable", "disable"]
    # Enable/disable neighbor event logging. | Default: disable
    neighbor_event: Literal["enable", "disable"]
    # Enable/disable brief format traffic logging. | Default: disable
    brief_traffic_format: Literal["enable", "disable"]
    # Enable/disable anonymizing user names in log messages. | Default: disable
    user_anonymize: Literal["enable", "disable"]
    # Enable/disable proxy firewall implicit policy logging. | Default: disable
    expolicy_implicit_log: Literal["enable", "disable"]
    # Enable/disable inserting policy comments into traffic logs. | Default: disable
    log_policy_comment: Literal["enable", "disable"]
    # Enable/disable override FortiAnalyzer settings. | Default: disable
    faz_override: Literal["enable", "disable"]
    # Enable/disable override Syslog settings. | Default: disable
    syslog_override: Literal["enable", "disable"]
    # Enable/disable REST API POST/PUT/DELETE request logging. | Default: disable
    rest_api_set: Literal["enable", "disable"]
    # Enable/disable REST API GET request logging. | Default: disable
    rest_api_get: Literal["enable", "disable"]
    # Enable/disable REST API memory and performance stats in rest | Default: disable
    rest_api_performance: Literal["enable", "disable"]
    # Enable/disable long-live-session statistics logging. | Default: enable
    long_live_session_stat: Literal["enable", "disable"]
    # Enable/disable extended UTM logging. | Default: disable
    extended_utm_log: Literal["enable", "disable"]
    # Enable/disable zone name logging. | Default: disable
    zone_name: Literal["enable", "disable"]
    # Enable/disable web-svc performance logging. | Default: disable
    web_svc_perf: Literal["enable", "disable"]
    # Custom fields to append to all log messages.
    custom_log_fields: list[SettingCustomlogfieldsObject]
    # User name anonymization hash salt. | MaxLen: 32
    anonymization_hash: str
    
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
    def to_dict(self) -> SettingPayload: ...
    def keys(self) -> Any: ...
    def values(self) -> Generator[Any, None, None]: ...
    def items(self) -> Generator[tuple[str, Any], None, None]: ...
    def get(self, key: str, default: Any = None) -> Any: ...


class Setting:
    """
    Configure general log settings.
    
    Path: log/setting
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject: ...
    
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
    ) -> SettingObject | dict[str, Any]: ...
    
    def get_schema(
        self,
        vdom: str | None = ...,
        format: str = ...,
    ) -> FortiObject: ...
    
    # PUT overloads
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> SettingObject: ...
    
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    # Default overload
    @overload
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def put(
        self,
        payload_dict: SettingPayload | None = ...,
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
        vdom: str | bool | None = ...,
    ) -> MutationResponse: ...
    
    def exists(
        self,
        name: str,
        vdom: str | bool | None = ...,
    ) -> bool: ...
    
    def set(
        self,
        payload_dict: SettingPayload | None = ...,
        resolve_ip: Literal["enable", "disable"] | None = ...,
        resolve_port: Literal["enable", "disable"] | None = ...,
        log_user_in_upper: Literal["enable", "disable"] | None = ...,
        fwpolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        fwpolicy6_implicit_log: Literal["enable", "disable"] | None = ...,
        extended_log: Literal["enable", "disable"] | None = ...,
        local_in_allow: Literal["enable", "disable"] | None = ...,
        local_in_deny_unicast: Literal["enable", "disable"] | None = ...,
        local_in_deny_broadcast: Literal["enable", "disable"] | None = ...,
        local_in_policy_log: Literal["enable", "disable"] | None = ...,
        local_out: Literal["enable", "disable"] | None = ...,
        local_out_ioc_detection: Literal["enable", "disable"] | None = ...,
        daemon_log: Literal["enable", "disable"] | None = ...,
        neighbor_event: Literal["enable", "disable"] | None = ...,
        brief_traffic_format: Literal["enable", "disable"] | None = ...,
        user_anonymize: Literal["enable", "disable"] | None = ...,
        expolicy_implicit_log: Literal["enable", "disable"] | None = ...,
        log_policy_comment: Literal["enable", "disable"] | None = ...,
        faz_override: Literal["enable", "disable"] | None = ...,
        syslog_override: Literal["enable", "disable"] | None = ...,
        rest_api_set: Literal["enable", "disable"] | None = ...,
        rest_api_get: Literal["enable", "disable"] | None = ...,
        rest_api_performance: Literal["enable", "disable"] | None = ...,
        long_live_session_stat: Literal["enable", "disable"] | None = ...,
        extended_utm_log: Literal["enable", "disable"] | None = ...,
        zone_name: Literal["enable", "disable"] | None = ...,
        web_svc_perf: Literal["enable", "disable"] | None = ...,
        custom_log_fields: str | list[str] | list[dict[str, Any]] | None = ...,
        anonymization_hash: str | None = ...,
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
    "Setting",
    "SettingPayload",
    "SettingResponse",
    "SettingObject",
]